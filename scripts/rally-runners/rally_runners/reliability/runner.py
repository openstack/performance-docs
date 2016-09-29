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
import itertools
import logging
import os
import shlex

from oslo_concurrency import processutils

import rally_runners.reliability as me
import rally_runners.reliability.rally_plugins as plugins
from rally_runners.reliability import report
from rally_runners import utils

SCENARIOS_DIR = 'rally_runners/reliability/scenarios/'


def make_help_options(base, type_filter=None):
    path = utils.resolve_relative_path(base)
    files = itertools.chain.from_iterable(
        [map(functools.partial(os.path.join, root), files)
         for root, dirs, files in os.walk(path)])  # list of files in a tree
    if type_filter:
        files = (f for f in files if type_filter(f))  # filtered list
    rel_files = map(functools.partial(os.path.relpath, start=path), files)
    return '\n    '.join('%s' % f.partition('.')[0] for f in sorted(rel_files))


SCENARIOS_LIST = make_help_options(SCENARIOS_DIR,
                                   type_filter=lambda x: x.endswith('.yaml'))
USAGE = """rally-reliability [-h] -s SCENARIO -o OUTPUT -b BOOK

Scenario is one of:
    %s
""" % SCENARIOS_LIST


def main():
    parser = argparse.ArgumentParser(prog='rally-reliability', usage=USAGE)
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-s', '--scenario', dest='scenario', required=True,
                        help='Rally scenario')
    parser.add_argument('-o', '--output', dest='output', required=True,
                        help='raw Rally output')
    parser.add_argument('-b', '--book', dest='book', required=True,
                        help='folder where to write RST book')
    args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        level=logging.DEBUG if args.debug else logging.INFO)

    plugin_paths = os.path.dirname(plugins.__file__)
    scenario_dir = os.path.join(os.path.dirname(me.__file__), 'scenarios')
    scenario_path = os.path.join(scenario_dir, args.scenario)
    if not scenario_path.endswith('.yaml'):
        scenario_path += '.yaml'

    run_cmd = ('rally --plugin-paths %(path)s task start --task %(scenario)s' %
               dict(path=plugin_paths, scenario=scenario_path))
    logging.info('Executing %s' % run_cmd)
    command_stdout, command_stderr = processutils.execute(
        *shlex.split(run_cmd))

    logging.info('Execution is done: %s' % command_stdout)
    command_stdout, command_stderr = processutils.execute(
        *shlex.split('rally task results'))

    with open(args.output, 'w') as fd:
        fd.write(command_stdout)

    report.make_report(args.scenario, [args.output], args.book)


if __name__ == '__main__':
    main()
