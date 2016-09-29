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

import collections

MinMax = collections.namedtuple('MinMax', ('min', 'max'))
Mean = collections.namedtuple('Mean', ('statistic', 'minmax'))
MeanVar = collections.namedtuple('MeanVar', ('statistic', 'var'))
ArrayStats = collections.namedtuple(
    'ArrayStats', ['mean', 'median', 'p95', 'var', 'std', 'count'])
ClusterStats = collections.namedtuple(
    'ClusterStats', ['start', 'end', 'duration', 'count'])
DegradationClusterStats = collections.namedtuple(
    'DegradationClusterStats',
    ['start', 'end', 'duration', 'count', 'degradation', 'degradation_ratio'])
RunResult = collections.namedtuple(
    'RunResult', ['data', 'error_area', 'anomaly_area', 'degradation_area',
                  'etalon_stats', 'etalon_interval', 'etalon_threshold',
                  'smooth_data'])
SummaryResult = collections.namedtuple(
    'SummaryResult', ['run_results', 'mttr', 'degradation',
                      'degradation_ratio', 'downtime'])
SmoothData = collections.namedtuple('SmoothData', ['time', 'duration', 'var'])
DataRow = collections.namedtuple(
    'DataRow', ['index', 'time', 'duration', 'error'])
