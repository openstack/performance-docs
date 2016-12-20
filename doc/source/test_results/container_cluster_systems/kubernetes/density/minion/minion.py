#!/usr/bin/python2

import httplib
import signal
import sys
import time
import uuid


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        print('Signal caught')
        self.kill_now = True
        sys.exit(0)


if __name__ == '__main__':
    killer = GracefulKiller()

    t = int(time.time() * (10 ** 3))
    u = str(uuid.uuid4())
    e = ''
    c = httplib.HTTPConnection('172.20.9.7:8000')
    q = '%s' % t
    print(q)
    c.request('GET', q)
    r = c.getresponse()
    print(r.status)
    time.sleep(2 << 20)
