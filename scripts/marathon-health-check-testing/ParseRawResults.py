#!/usr/bin/python
from argparse import ArgumentParser
import numpy as np


def parse(file, percentile, interval):
    data = {}
    with open(file) as fp:
        for line in fp:
            record = line.rstrip().split(',')
            try:
                timestamp = float(record[1])
                if record[0] not in data:
                    data[record[0]] = []
                data[record[0]].append(timestamp)
            except ValueError:
                continue

    deviations = []
    for task in data:
        data[task].sort()
        last_timestamp = 0
        for timestamp in data[task]:
            if last_timestamp == 0:
                last_timestamp = timestamp
                continue
            cur_interval = timestamp - last_timestamp
            last_timestamp = timestamp
            deviations.append(np.fabs(interval - cur_interval))

    print("Total tasks: {}. Total health checks: {}".format(len(data.keys()),
                                                            len(deviations)))
    print("min: {}. max: {}, average: {},"
          " percentile: {}".format(np.min(deviations),
                                   np.max(deviations),
                                   np.average(deviations),
                                   np.percentile(deviations, percentile)))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-f", "--file",
                        help="File to be parsed",
                        required=True)
    parser.add_argument("-i", "--interval",
                        help="Configured health check interval(sec)",
                        required=True)
    parser.add_argument("-p", "--persentile",
                        help="Percentile value [0-100]. Default 95",
                        required=False, default=95.0)
    args = parser.parse_args()

    parse(args.file, float(args.persentile), int(args.interval))
