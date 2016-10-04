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

import argparse
import functools
import json
import logging
import math
import os

import jinja2
from tabulate import tabulate
import yaml

from rally_runners.reliability import analytics
from rally_runners.reliability import graphics
from rally_runners import utils

REPORT_TEMPLATE = 'rally_runners/reliability/templates/report.rst'
SCENARIOS_DIR = 'rally_runners/reliability/scenarios/'


def round2(number, variance=None):
    if not variance:
        variance = number
    return round(number, int(math.ceil(-(math.log10(variance)))) + 1)


def mean_var_to_str(mv):
    if not mv:
        return 'N/A'

    if mv.var == 0:
        precision = 4
    else:
        precision = int(math.ceil(-(math.log10(mv.var)))) + 1
    if precision > 0:
        pattern = '%%.%df' % precision
        pattern_1 = '%%.%df' % (precision)
    else:
        pattern = pattern_1 = '%d'

    return '%s ~%s' % (pattern % round(mv.statistic, precision),
                       pattern_1 % round(mv.var, precision + 1))


def tabulate2(*args, **kwargs):
    return (u'%s' % tabulate(*args, **kwargs)).replace(' ~', u'\u00A0±')


def get_runs(raw_rally_reports):
    for one_report in raw_rally_reports:
        for one_run in one_report:
            yield one_run


def indent(text, distance):
    return '\n'.join((' ' * distance + line) for line in text.split('\n'))


def process(raw_rally_reports, book_folder, scenario, scenario_name):
    scenario_text = indent(scenario, 4)
    report = dict(runs=[], scenario=scenario_text, scenario_name=scenario_name)

    summary = analytics.process_all_runs(get_runs(raw_rally_reports))
    logging.debug('Summary: %s', summary)

    has_errors = False
    has_degradation = False

    for i, one_run in enumerate(summary.run_results):
        report_one_run = {}

        plot = graphics.draw_plot(one_run)
        plot.savefig(os.path.join(book_folder, 'plot_%d.svg' % (i + 1)))

        headers = ['Samples', 'Median, s', 'Mean, s', 'Std dev',
                   '95% percentile, s']
        t = [[one_run.etalon_stats.count,
              round2(one_run.etalon_stats.median),
              round2(one_run.etalon_stats.mean),
              round2(one_run.etalon_stats.std),
              round2(one_run.etalon_stats.p95)]]
        report_one_run['etalon_table'] = tabulate2(
            t, headers=headers, tablefmt='grid')

        headers = ['#', 'Downtime, s']
        t = []
        for index, stat in enumerate(one_run.error_area):
            t.append([index + 1, mean_var_to_str(stat.duration)])

        if one_run.error_area:
            has_errors = True
            report_one_run['errors_table'] = tabulate2(
                t, headers=headers, tablefmt='grid')

        headers = ['#', 'Time to recover, s', 'Absolute degradation, s',
                   'Relative degradation']
        t = []
        for index, stat in enumerate(one_run.degradation_area):
            t.append([index + 1,
                      mean_var_to_str(stat.duration),
                      mean_var_to_str(stat.degradation),
                      mean_var_to_str(stat.degradation_ratio)])

        if one_run.degradation_area:
            has_degradation = True
            report_one_run['degradation_table'] = tabulate2(
                t, headers=headers, tablefmt="grid")

        report['runs'].append(report_one_run)

    headers = ['Service downtime, s', 'MTTR, s',
               'Absolute performance degradation, s',
               'Relative performance degradation, ratio']
    t = [[mean_var_to_str(summary.downtime),
          mean_var_to_str(summary.mttr),
          mean_var_to_str(summary.degradation),
          mean_var_to_str(summary.degradation_ratio)]]
    report['summary_table'] = tabulate2(t, headers=headers, tablefmt='grid')

    report['has_errors'] = has_errors
    report['has_degradation'] = has_degradation

    jinja_env = jinja2.Environment()
    jinja_env.filters['json'] = json.dumps
    jinja_env.filters['yaml'] = functools.partial(
        yaml.safe_dump, indent=2, default_flow_style=False)

    path = utils.resolve_relative_path(REPORT_TEMPLATE)
    with open(path) as fd:
        template = fd.read()
        compiled_template = jinja_env.from_string(template)
        rendered_template = compiled_template.render(dict(report=report))

        index_path = os.path.join(book_folder, 'index.rst')
        with open(index_path, 'w') as fd2:
            fd2.write(rendered_template.encode('utf8'))

    logging.info('The book is written to: %s', book_folder)


def make_report(scenario_name, raw_rally_file_names, book_folder):
    scenario_dir = utils.resolve_relative_path(SCENARIOS_DIR)
    scenario_path = os.path.join(scenario_dir, scenario_name)
    if not scenario_path.endswith('.yaml'):
        scenario_path += '.yaml'

    with open(scenario_path) as fd:
        scenario = fd.read()

    raw_rally_reports = []
    for file_name in raw_rally_file_names:
        with open(file_name) as fd:
            raw_rally_reports.append(json.loads(fd.read()))

    utils.mkdir_tree(book_folder)
    process(raw_rally_reports, book_folder, scenario, scenario_name)


def main():
    parser = argparse.ArgumentParser(prog='rally-reliability-report')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-i', '--input', dest='input', nargs='+',
                        help='Rally raw json output')
    parser.add_argument('-b', '--book', dest='book', required=True,
                        help='folder where to write RST book')
    parser.add_argument('-s', '--scenario', dest='scenario', required=True,
                        help='Rally scenario')
    args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        level=logging.DEBUG if args.debug else logging.INFO)

    make_report(args.scenario, args.input, args.book)


if __name__ == '__main__':
    main()
