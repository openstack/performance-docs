#!/usr/bin/python
# This script setups simple HTTP server that listens on a given port.
# When a server is started it creates a log file with name in the format
# "instance_<timestamp>.txt". Save directory is also configured
# (defaults to /tmp).
# Once special incoming POST request comes this server logs it
# to the log file."

import argparse
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from datetime import datetime
import logging
import os
import sys
import json

LOG = logging.getLogger(__name__)
FILE_NAME = "instances_{:%Y_%m_%d_%H:%M:%S}.txt".format(datetime.now())


class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            data = self._receive_data()
        except Exception as err:
            LOG.exception("Failed to process request: %s", err)
            raise
        else:
            LOG.info("Incoming connection: ip=%(ip)s, %(data)s",
                     {"ip": self.client_address[0], "data": data})

    def _receive_data(self):
        length = int(self.headers.getheader('content-length'))
        data = json.loads(self.rfile.read(length))

        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello!\n")
        return data


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log-dir', default="/tmp")
    parser.add_argument('-p', '--port', required=True)
    return parser


def main():
    # Parse CLI arguments
    args = get_parser().parse_args()
    file_name = os.path.join(args.log_dir, FILE_NAME)

    # Set up logging
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                        level=logging.INFO,
                        filename=file_name)
    console = logging.StreamHandler(stream=sys.stdout)
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    # Initialize and start server
    server = HTTPServer(('0.0.0.0', int(args.port)), PostHandler)
    LOG.info("Starting server on %s:%s, use <Ctrl-C> to stop",
             server.server_address[0], args.port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        LOG.info("Server terminated")
    except Exception as err:
        LOG.exception("Server terminated unexpectedly: %s", err)
        raise
    finally:
        logging.shutdown()

if __name__ == '__main__':
    main()
