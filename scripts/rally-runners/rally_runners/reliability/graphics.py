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

import matplotlib as mpl
mpl.use('Agg')  # do not require X server

import matplotlib.pyplot as plt


def draw_area(plot, area, color, label):
    for i, c in enumerate(area):
        plot.axvspan(c.start, c.end, color=color, label=label)
        label = None  # show label only once


def draw_plot(run_result, show_etalon=True, show_errors=True,
              show_anomalies=False, show_degradation=True):
    table = run_result.data
    x = [p.time for p in table]
    y = [p.duration for p in table]

    x2 = [p.time for p in table if p.error]
    y2 = [p.duration for p in table if p.error]

    figure = plt.figure()
    plot = figure.add_subplot(111)
    plot.plot(x, y, 'b.', label='Successful operations')
    plot.plot(x2, y2, 'r.', label='Failed operations')
    plot.set_ylim(0)

    plot.axhline(run_result.etalon_threshold, color='violet',
                 label='Degradation threshold')

    # highlight etalon
    if show_etalon:
        plot.axvspan(run_result.etalon_interval.inf,
                     run_result.etalon_interval.sup,
                     color='#b0efa0', label='Baseline')

    # highlight anomalies
    if show_anomalies:
        draw_area(plot, run_result.anomaly_area,
                  color='#f0f0f0', label='Anomaly')

    # highlight degradation
    if show_degradation:
        draw_area(plot, run_result.degradation_area,
                  color='#f8efa8', label='Degradation')

    # highlight errors
    if show_errors:
        draw_area(plot, run_result.error_area,
                  color='#ffc0a7', label='Downtime')

    # draw mean
    plot.plot([p.time for p in run_result.smooth_data],
              [p.duration for p in run_result.smooth_data],
              color='cyan', label='Mean duration')

    plot.grid(True)
    plot.set_xlabel('time, s')
    plot.set_ylabel('operation duration, s')

    # add legend
    legend = plot.legend(loc='right', shadow=True)
    for label in legend.get_texts():
        label.set_fontsize('small')

    return figure
