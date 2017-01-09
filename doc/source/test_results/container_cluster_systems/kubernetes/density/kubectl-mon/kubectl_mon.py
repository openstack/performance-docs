#!/bin/python

import re
import subprocess
import time

KUBECTL_CMD = 'kubectl --namespace minions get pods -l k8s-app=minion'


def main():
    while True:
        start = time.time()
        stdout = subprocess.Popen(KUBECTL_CMD, shell=True,
                                  stdout=subprocess.PIPE).stdout.read()
        print('time,name,status')
        for line in stdout.split('\n')[1:]:
            if line:
                tokens = re.split('\s+', line)
                name = tokens[0]
                status = tokens[2]
                print('%f,%s,%s' % (start, name, status))

        d = 1 - (time.time() - start)
        time.sleep(d)

if __name__ == '__main__':
    main()
