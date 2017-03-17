#!/bin/python

import optparse
import re
import requests
from requests.adapters import HTTPAdapter
import sys
import subprocess
import time

KUBECTL_CMD = 'kubectl --namespace minions get pods -l k8s-app=minion'
TIMEOUT = 1200  # in seconds


class Monitor(object):
    def __init__(self, **options):
        self.options = options

    def check_direction(self, n, l):
        if self.direction == 'up':
            if n > 0 and l == n + 1:
                print 'Done.'
                sys.exit(0)
        if self.direction == 'down':
            if l == 0:
                print 'Done.'
                sys.exit(0)

    def run(self):
        self.direction = self.options.get('direction', 'up')
        base_time = int(time.time() * 1000000000)

        s = requests.Session()
        s.mount('http://master.minions:8888', HTTPAdapter(max_retries=10))

        while True:
            start = int(time.time() * 1000000000)
            stdout = subprocess.Popen(KUBECTL_CMD, shell=True,
                                      stdout=subprocess.PIPE).stdout.read()

            n = 0
            for line in stdout.split('\n')[1:]:
                if line:
                    tokens = re.split('\s+', line)
                    name = tokens[0]
                    status = tokens[2]

                    if status == 'Running':
                        n += 1

                    url = "http://master.minions:8888/monitor?minion_time=%s&" \
                          "minion_name=%s&minion_status=%s&direction=%s" % (
                              start, name, status, self.direction)

                    s.get(url)

            length_lines = len(stdout.split('\n')[1:])
            self.check_direction(n, length_lines)

            if (start - base_time) / 1000000000 > TIMEOUT:
                print 'Timeout.(%d)' % TIMEOUT
                sys.exit(0)

            time.sleep(1)


def main():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--direction', dest='direction', default='up')
    options, args = parser.parse_args()

    Monitor(**vars(options)).run()

if __name__ == '__main__':
    main()
