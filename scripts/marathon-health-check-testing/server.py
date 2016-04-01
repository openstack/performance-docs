#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler
import os
import time

VERSION = 1.0


class ServerStatus(object):
    collecting = 0
    status = 1
    last_timestamp = 0
    interval_arr = []
    timestamp_arr = []


class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/start':
            ServerStatus.status = 1
            self.send_response(200)
            self.end_headers()
        elif self.path == '/stop':
            ServerStatus.status = 0
            self.send_response(200)
            self.end_headers()
        elif self.path == '/start_collect':
            ServerStatus.collecting = 1
            self.send_response(200)
            self.end_headers()
        elif self.path == '/stop_collect':
            ServerStatus.collecting = 0
            self.send_response(200)
            self.end_headers()
        elif self.path == '/get_intervals':
            self.send_response(200)
            self.send_header("Context-Type", "text/plain")
            self.end_headers()
            tmp_str = ','.join(str(x) for x in ServerStatus.interval_arr)
            self.wfile.write(tmp_str)
            self.wfile.close()
        elif self.path == '/version':
            self.send_response(200)
            self.send_header("Context-Type", "text/plain")
            self.end_headers()
            self.wfile.write(VERSION)
            self.wfile.close()
        elif self.path == '/get_stats':
            if ServerStatus.collecting == 0:
                self.send_response(202)
            else:
                self.send_response(200)
            self.send_header("Context-Type", "text/plain")
            self.end_headers()
            timestamp_str = ','.join(str(x)
                                     for x in ServerStatus.timestamp_arr)
            intervals_str = ','.join(str(x) for x in ServerStatus.interval_arr)
            self.wfile.write(timestamp_str+'\n'+intervals_str)
            self.wfile.close()
        elif self.path == '/get_timestamps':
            if ServerStatus.collecting == 0:
                self.send_response(202)
            else:
                self.send_response(200)
            self.send_header("Context-Type", "text/plain")
            self.end_headers()
            tmp_str = ','.join(str(x) for x in ServerStatus.timestamp_arr)
            self.wfile.write(tmp_str)
            self.wfile.close()
        elif self.path == '/is_collecter_start':
            self.send_response(200)
            self.send_header("Context-Type", "text/plain")
            self.end_headers()
            if ServerStatus.collecting == 1:
                self.wfile.write("Yes")
            else:
                self.wfile.write("No")
            self.wfile.close()
        elif self.path == '/clear_stats':
            ServerStatus.interval_arr = []
            ServerStatus.timestamp_arr = []
            ServerStatus.last_timestamp = 0
            self.send_response(200)
            self.end_headers()
        elif self.path == '/status':
            if ServerStatus.collecting == 1:
                if ServerStatus.last_timestamp == 0:
                    ServerStatus.last_timestamp = time.time()
                else:
                    current_time = time.time()
                    interval = round(current_time -
                                     ServerStatus.last_timestamp, 3)
                    ServerStatus.interval_arr.append(interval)
                    ServerStatus.timestamp_arr.append(round(current_time, 3))
                    ServerStatus.last_timestamp = current_time
            if ServerStatus.status == 0:
                self.send_response(503)
            else:
                self.send_response(200)
            self.end_headers()

        return

if __name__ == '__main__':
    port = int(os.getenv('SERVER_PORT', '80'))
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('0.0.0.0', port), GetHandler)
    server.serve_forever()
