#!/usr/bin/python

import json
import logging
import sys

from tabulate import tabulate


def cut_json_data(file_with_results):
    json_data = "{"
    start = False
    end = False
    with open(file_with_results) as f:
        for line in f:
            end = end or "Finish:Performance" in line
            if end:
                break
            if start:
                json_data += line
            start = start or "Result:Performance" in line
    data = json.loads(json_data)
    return data


def get_resources_and_request_types(data):
    resources = {}
    for data_item in data["dataItems"]:
        resource = data_item["labels"]["Resource"]
        if resource not in resources:
            resources[resource] = {}
        type_of_request = data_item["labels"]["Verb"]
        resources[resource][type_of_request] = data_item["data"]
    return resources


def create_rst_tables(resource):
    headers = ["Method"]
    data = []
    for method, perc in resource.iteritems():
        headers += perc.keys()
        data.append([method] + perc.values())
    tables = tabulate(data, headers=headers, tablefmt="grid")
    return tables


def put_tables_to_file(file_with_results):
    rst_file = file_with_results.split(".")[0] + ".rst"
    data = cut_json_data(file_with_results)
    with open(rst_file, 'w') as f:
        for resource, data in \
                get_resources_and_request_types(data).iteritems():
            table_head = "\n" + resource + "\n"
            table_head_underline = ""
            for character in resource:
                table_head_underline += "^"
            table_head += table_head_underline + "\n"
            f.write(table_head + create_rst_tables(data))


def main(file_with_results):
    put_tables_to_file(file_with_results)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[1])
