# coding=utf-8

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import math

from interval import interval
import numpy as np
from scipy import stats
from sklearn import cluster as skl

from rally_runners.reliability import types

MIN_CLUSTER_WIDTH = 3  # filter cluster with less items
MAX_CLUSTER_GAP = 6  # max allowed gap in the cluster (otherwise split them)
WINDOW_SIZE = 21  # window size for average duration calculation
WARM_UP_CUTOFF = 10  # drop first N points from etalon
DEGRADATION_THRESHOLD = 4  # how many sigmas duration differs from etalon mean


def find_clusters(arr, filter_fn, max_gap=MAX_CLUSTER_GAP,
                  min_cluster_width=MIN_CLUSTER_WIDTH):
    """Find clusters of 1 in the sequence containing (0, 1)

    The given array is filtered through filter_fn function which produces
    sequence of 0s or 1s. Then 1s are grouped into clusters so that:
     * there can not be more than max_gap 0s inside
     * there are at least min_cluster_width of 1s

    :param arr: initial array
    :param filter_fn: transformation x -> [0, 1]
    :param max_gap: maximum allowed number of consequent 0s inside the cluster
    :param min_cluster_width: minimum cluster width
    :return: multi-interval (i.e. list of intervals)
    """
    clusters = interval()

    start = None
    end = None

    for i, y in enumerate(arr):
        v = filter_fn(y)
        if v:
            if not start:
                start = i
            end = i
        else:
            if end and i - end > max_gap:
                if end - start >= min_cluster_width:
                    clusters |= interval([start, end])
                start = end = None

    if end:
        if end - start >= MIN_CLUSTER_WIDTH:
            clusters |= interval([start, end])

    return clusters


def convert_rally_data(data):
    """Convert raw Rally data into [DataRow]

    :param data: raw Rally data
    :return: ([DataRow], index of hook)
    """
    results = data['result']
    start = results[0]['timestamp']  # start of the run

    hooks = data['hooks']
    hook_index = 0

    if hooks:
        # when the hook started
        hook_start_time = hooks[0]['started_at'] - start
    else:
        # let all data be etalon
        hook_start_time = results[-1]['timestamp']

    table = []
    for index, result in enumerate(results):
        time = result['timestamp'] - start
        duration = result['duration']

        if time + duration < hook_start_time:
            hook_index = index

        table.append(types.DataRow(index=index, time=time, duration=duration,
                                   error=bool(result['error'])))

    return table, hook_index


def calculate_array_stats(data):
    data = np.array(data)
    return types.ArrayStats(mean=np.mean(data), median=np.median(data),
                            p95=np.percentile(data, 95), var=np.var(data),
                            std=np.std(data), count=len(data))


def indexed_interval_to_time_interval(table, src_interval):
    """For given indexes in the table return time interval

    :param table: [DataRow] source data
    :param src_interval: interval of array indexes
    :return: ClusterStats
    """
    start_index = int(src_interval.inf)
    end_index = int(src_interval.sup)

    if start_index > 0:
        d_start = (table[start_index].time - table[start_index - 1].time) / 2
    else:
        d_start = 0

    if end_index < len(table) - 1:
        d_end = (table[end_index + 1].time - table[end_index].time) / 2
    else:
        d_end = 0

    start_time = table[start_index].time - d_start
    end_time = table[end_index].time + d_end
    var = d_start + d_end
    duration = end_time - start_time
    count = sum(1 if start_time <= p.time <= end_time else 0 for p in table)

    return types.ClusterStats(start=start_time, end=end_time, count=count,
                              duration=types.MeanVar(duration, var))


def calculate_error_area(table):
    """Calculates error statistics

    :param table:
    :return: list of time intervals where errors occur
    """
    error_clusters = find_clusters(
        (p.error for p in table),
        filter_fn=lambda x: 1 if x else 0,
        min_cluster_width=0
    )
    error_stats = [indexed_interval_to_time_interval(table, cluster)
                   for cluster in error_clusters]
    return error_stats


def calculate_anomaly_area(table, quantile=0.9):
    """Find anomalies

    :param quantile: float, default 0.3
    :param table:
    :return: list of time intervals where anomalies occur
    """
    table = [p for p in table if not p.error]  # rm errors
    x = [p.duration for p in table]
    X = np.array(zip(x, np.zeros(len(x))), dtype=np.float)
    bandwidth = skl.estimate_bandwidth(X, quantile=quantile)
    mean_shift_algo = skl.MeanShift(bandwidth=bandwidth, bin_seeding=True)
    mean_shift_algo.fit(X)
    labels = mean_shift_algo.labels_
    lm = stats.mode(labels)

    # filter out the largest cluster
    vl = [(0 if labels[i] == lm.mode else 1) for i, p in enumerate(x)]

    anomaly_clusters = find_clusters(vl, filter_fn=lambda y: y)
    anomaly_stats = [indexed_interval_to_time_interval(table, cluster)
                     for cluster in anomaly_clusters]
    return anomaly_stats


def calculate_smooth_data(table, window_size):
    """Calculate mean for the data

    :param table:
    :param window_size:
    :return: list of points in mean data
    """
    table = [p for p in table if not p.error]  # rm errors
    smooth = []

    for i in range(0, len(table) - window_size):
        durations = [p.duration for p in table[i: i + window_size]]

        time = np.mean([p.time for p in table[i: i + window_size]])
        duration = np.mean(durations)
        var = abs(time - np.mean(
            [p.time for p in table[i + 1: i + window_size - 1]]))

        smooth.append(types.SmoothData(time=time, duration=duration, var=var))

    return smooth


def calculate_degradation_area(table, smooth, etalon_stats, etalon_threshold):
    table = [p for p in table if not p.error]  # rm errors
    if len(table) <= WINDOW_SIZE:
        return []

    mean_times = [p.time for p in smooth]
    mean_durations = [p.duration for p in smooth]
    mean_vars = [p.var for p in smooth]

    clusters = find_clusters(
        mean_durations,
        filter_fn=lambda y: 0 if abs(y) < etalon_threshold else 1)

    # calculate cluster duration
    degradation_cluster_stats = []
    for cluster in clusters:
        start_idx = int(cluster.inf)
        end_idx = int(cluster.sup)
        start_time = mean_times[start_idx]
        end_time = mean_times[end_idx]
        duration = end_time - start_time
        var = np.mean(mean_vars[start_idx: end_idx])

        # point durations
        point_durations = []
        for p in table:
            if start_time < p.time < end_time:
                point_durations.append(p.duration)

        # calculate difference between means
        # http://onlinestatbook.com/2/tests_of_means/difference_means.html
        anomaly_mean = np.mean(point_durations)
        anomaly_var = np.var(point_durations)
        se = math.sqrt(anomaly_var / len(point_durations) +
                       etalon_stats.var / etalon_stats.count)
        dof = etalon_stats.count + len(point_durations) - 2
        mean_diff = anomaly_mean - etalon_stats.mean
        conf_interval = stats.t.interval(0.95, dof, loc=mean_diff, scale=se)

        degradation = types.MeanVar(
            mean_diff, np.mean([mean_diff - conf_interval[0],
                                conf_interval[1] - mean_diff]))
        degradation_ratio = types.MeanVar(
            anomaly_mean / etalon_stats.mean,
            np.mean([(mean_diff - conf_interval[0]) / etalon_stats.mean,
                     (conf_interval[1] - mean_diff) / etalon_stats.mean]))

        logging.debug('Mean diff: %s' % mean_diff)
        logging.debug('Conf int: %s' % str(conf_interval))

        degradation_cluster_stats.append(types.DegradationClusterStats(
            start=start_time, end=end_time,
            duration=types.MeanVar(duration, var),
            degradation=degradation, degradation_ratio=degradation_ratio,
            count=len(point_durations)
        ))

    return degradation_cluster_stats


def process_one_run(rally_data):
    """Process single Rally run (raw output for single task iteration)

    This function calculates statistics for a single run, including
    baseline stats (etalon), error stats, anomalies and areas with degraded
    performance.

    :param rally_data: raw Rally data
    :return: RunResult
    """
    data, hook_index = convert_rally_data(rally_data)
    etalon = [p.duration for p in data[WARM_UP_CUTOFF:hook_index]]

    etalon_stats = calculate_array_stats(etalon)
    etalon_threshold = abs(etalon_stats.mean +
                           DEGRADATION_THRESHOLD * etalon_stats.std)
    etalon_interval = interval([data[WARM_UP_CUTOFF].time,
                                data[hook_index].time])[0]

    logging.debug('Hook index: %s' % hook_index)
    logging.debug('Etalon stats: %s' % str(etalon_stats))

    # Calculate stats
    error_area = calculate_error_area(data)

    anomaly_area = calculate_anomaly_area(data)

    smooth_data = calculate_smooth_data(data, window_size=WINDOW_SIZE)

    degradation_area = calculate_degradation_area(
        data, smooth_data, etalon_stats, etalon_threshold)

    # logging.debug stats
    logging.debug('Error area: %s' % error_area)
    logging.debug('Anomaly area: %s' % anomaly_area)
    logging.debug('Degradation area: %s' % degradation_area)

    return types.RunResult(
        data=data,
        error_area=error_area,
        anomaly_area=anomaly_area,
        degradation_area=degradation_area,
        etalon_stats=etalon_stats,
        etalon_interval=etalon_interval,
        etalon_threshold=etalon_threshold,
        smooth_data=smooth_data,
    )


def process_all_runs(runs):
    """Process all runs from Rally raw data report

    This function returns summary stats for all runs, including downtime
    duration, MTTR, performance degradation.

    :param runs: collection of Rally runs
    :return: SummaryResult
    """
    run_results = []
    downtime_statistic = []
    downtime_var = []
    ttr_statistic = []
    ttr_var = []
    degradation_statistic = []
    degradation_var = []
    degradation_ratio_statistic = []
    degradation_ratio_var = []

    for i, one_run in enumerate(runs):
        run_result = process_one_run(one_run)
        run_results.append(run_result)

        ds = 0
        for index, stat in enumerate(run_result.error_area):
            ds += stat.duration.statistic
            downtime_var.append(stat.duration.var)

        if run_result.error_area:
            downtime_statistic.append(ds)

        ts = ss = sr = 0
        for index, stat in enumerate(run_result.degradation_area):
            ts += stat.duration.statistic
            ttr_var.append(stat.duration.var)
            ss += stat.degradation.statistic
            degradation_var.append(stat.degradation.var)
            sr += stat.degradation_ratio.statistic
            degradation_ratio_var.append(stat.degradation_ratio.var)

        if run_result.degradation_area:
            ttr_statistic.append(ts)
            degradation_statistic.append(ss)
            degradation_ratio_statistic.append(sr)

    downtime = None
    if downtime_statistic:
        downtime_mean = np.mean(downtime_statistic)
        se = math.sqrt((sum(downtime_var) +
                       np.var(downtime_statistic)) / len(downtime_statistic))
        downtime = types.MeanVar(downtime_mean, se)
    mttr = None
    if ttr_statistic:
        ttr_mean = np.mean(ttr_statistic)
        se = math.sqrt((sum(ttr_var) +
                        np.var(ttr_statistic)) / len(ttr_statistic))
        mttr = types.MeanVar(ttr_mean, se)
    degradation = None
    degradation_ratio = None
    if degradation_statistic:
        degradation = types.MeanVar(np.mean(degradation_statistic),
                                    np.mean(degradation_var))
        degradation_ratio = types.MeanVar(np.mean(degradation_ratio_statistic),
                                          np.mean(degradation_ratio_var))

    return types.SummaryResult(run_results=run_results, mttr=mttr,
                               degradation=degradation,
                               degradation_ratio=degradation_ratio,
                               downtime=downtime)
