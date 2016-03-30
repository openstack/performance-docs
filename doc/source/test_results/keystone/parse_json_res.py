import argparse
import collections
import copy
import itertools
import json
import numpy as np
import os
import prettytable


NODES_TEMPLATE = {
    "DB queries": {
        "total": 0,
        "total_time_spent": 0,
        "select1": 0,
        "select1_time_spent": 0,
        "real": 0,
        "real_time_spent": 0,
        "SELECT": {
            "total": 0,
            "INNER JOIN": 0,
            "LEFT JOIN": 0,
            "RIGHT JOIN": 0,
            "FULL JOIN": 0,
            "time_spent": collections.OrderedDict(),
        },
        "INSERT": {
            "total": 0,
            "time_spent": collections.OrderedDict(),
        },
        "UPDATE": {
            "total": 0,
            "time_spent": collections.OrderedDict(),
        },
        "DELETE": {
            "total": 0,
            "time_spent": collections.OrderedDict(),
        },
        "red_flag": {
            "2joins": {
                "total": 0,
                "queries": [],
                "time_spent": collections.OrderedDict(),
            },
            "3+joins": {
                "total": 0,
                "queries": [],
                "time_spent": collections.OrderedDict(),
            }
        }
    },
    "Cached operations": {},
    "Cached time spent": collections.OrderedDict(),
}

NODES = copy.deepcopy(NODES_TEMPLATE)
OUTLIER_QUERIES = {}


def define_node(node):
    if node["info"]["project"] != "keystone":
        return

    if node["info"]["name"] not in ["db", "cache"]:
        return

    time_spent = node["info"]["finished"] - node["info"]["started"]

    if node["info"]["name"] == "db":
        process_db_calls(node, time_spent)
    elif node["info"]["name"] == "cache":
        if not node["children"]:
            process_cache_calls(node, time_spent)
        else:
            for child in node["children"]:
                define_node(child)


def process_cache_calls(node, time_spent):
    cache_info = node["info"]["meta.raw_payload.cache-start"][
        "info"]["fn_info"]
    if not NODES["Cached operations"].get(cache_info):
        NODES["Cached operations"][cache_info] = 0
    NODES["Cached operations"][cache_info] += 1
    if not NODES["Cached time spent"].get(time_spent):
        NODES["Cached time spent"][time_spent] = []
    NODES["Cached time spent"][time_spent].append(cache_info)


def process_db_calls(node, time_spent):
    NODES["DB queries"]["total"] += 1
    NODES["DB queries"]["total_time_spent"] += time_spent
    statement = node[
        "info"]["meta.raw_payload.db-start"]["info"]["db"]["statement"]
    if statement.startswith("SELECT 1"):
        NODES["DB queries"]["select1"] += 1
        NODES["DB queries"]["select1_time_spent"] += time_spent
    else:
        NODES["DB queries"]["real"] += 1
        NODES["DB queries"]["real_time_spent"] += time_spent

        if statement.startswith("SELECT"):
            process_selects(statement, time_spent)
        elif statement.startswith("UPDATE"):
            process_base_db_calls("UPDATE", statement, time_spent)
        elif statement.startswith("INSERT"):
            process_base_db_calls("INSERT", statement, time_spent)
        elif statement.startswith("DELETE"):
            process_base_db_calls("DELETE", statement, time_spent)


def process_base_db_calls(command, statement, time_spent):
    NODES["DB queries"][command]["total"] += 1
    if not NODES["DB queries"][command]["time_spent"].get(time_spent):
        NODES["DB queries"][command]["time_spent"][time_spent] = []
    NODES["DB queries"][command]["time_spent"][time_spent].append(
        statement)


def process_selects(statement, time_spent):
    process_base_db_calls("SELECT", statement, time_spent)

    ij = statement.count("INNER JOIN")
    lj = statement.count("LEFT JOIN")
    rj = statement.count("RIGHT JOIN")
    fj = statement.count("FULL JOIN")
    NODES["DB queries"]["SELECT"]["INNER JOIN"] += ij
    NODES["DB queries"]["SELECT"]["LEFT JOIN"] += lj
    NODES["DB queries"]["SELECT"]["RIGHT JOIN"] += rj
    NODES["DB queries"]["SELECT"]["FULL JOIN"] += fj

    # raise red flags if too many JOINS met
    if ij + lj + rj + fj == 2:
        NODES["DB queries"]["red_flag"]["2joins"]["total"] += 1
        NODES["DB queries"]["red_flag"]["2joins"][
            "queries"].append(statement)
        if not NODES["DB queries"]["red_flag"]["2joins"][
                "time_spent"].get(time_spent):
            NODES["DB queries"]["red_flag"]["2joins"]["time_spent"][
                time_spent] = []
        NODES["DB queries"]["red_flag"]["2joins"]["time_spent"][
            time_spent].append(statement)
    elif ij + lj + rj + fj >= 3:
        NODES["DB queries"]["red_flag"]["3+joins"]["total"] += 1
        NODES["DB queries"]["red_flag"]["3+joins"][
            "queries"].append(statement)
        if not NODES["DB queries"]["red_flag"]["3+joins"][
                "time_spent"].get(time_spent):
            NODES["DB queries"]["red_flag"]["3+joins"]["time_spent"][
                time_spent] = []
        NODES["DB queries"]["red_flag"]["3+joins"]["time_spent"][
            time_spent].append(statement)


def define_nodes(data):
    for child in data["children"]:
        if not child["children"]:
            define_node(child)
        else:
            define_nodes(child)


def sort_dicts(dictionary):
    new_nodes = copy.deepcopy(dictionary)
    for key in ["SELECT", "INSERT", "DELETE", "UPDATE"]:
        new_nodes["DB queries"][key]["time_spent"] = \
            sum([k*len(v) for k, v
                 in dictionary["DB queries"][key]["time_spent"].iteritems()])
    for key in ["2joins", "3+joins"]:
        new_nodes["DB queries"]["red_flag"][key]["time_spent"] = \
            sum([k*len(v) for k, v
                 in dictionary["DB queries"]["red_flag"][key][
                     "time_spent"].iteritems()])
    new_nodes["Cached time spent"] = \
        sum([k*len(v) for k, v
             in dictionary["Cached time spent"].iteritems()])
    return new_nodes


def detect_outliers(data, m=2.):
    full_time_set = list(itertools.chain(*[[k] * len(v) for k, v
                                           in data.iteritems()]))
    dat = np.abs(full_time_set - np.median(full_time_set))
    mdev = np.median(dat)
    sss = dat/mdev if mdev else 0.
    if mdev:
        for idx, val in enumerate((sss < m).tolist()):
            if not val:
                for query in data[full_time_set[idx]]:
                    OUTLIER_QUERIES[query] = full_time_set[idx]


def prepare_tables(nodes):
    # prepare table with common information
    common_info_table = prettytable.PrettyTable(["**Metric**", "**Value**"])
    common_info_table.align["**Metric**"] = "l"
    common_info_table.align["**Value**"] = "l"
    common_info_table.padding_width = 1
    common_info_table.max_width = 100
    common_info_table.header = True
    common_info_table.hrules = prettytable.ALL

    common_info_table.add_row(["Total (*) Keystone DB queries count",
                               nodes["DB queries"]["total"]])
    common_info_table.add_row(["Total (*) Keystone DB queries time spent, ms",
                               nodes["DB queries"]["total_time_spent"]])
    common_info_table.add_row([
        "Infrastructure (SELECT 1) Keystone DB queries count",
        nodes["DB queries"]["select1"]])
    common_info_table.add_row([
        "Infrastructure (SELECT 1) Keystone DB queries time spent, ms",
        nodes["DB queries"]["select1_time_spent"]])
    common_info_table.add_row(["Real Keystone DB queries count",
                               nodes["DB queries"]["real"]])
    common_info_table.add_row(["Real Keystone DB queries time spent, ms",
                               nodes["DB queries"]["real_time_spent"]])

    db_query_tmpl = "%s\n\n|"

    for key in ["SELECT", "INSERT", "DELETE", "UPDATE"]:
        if nodes["DB queries"][key]["total"]:
            common_info_table.add_row([
                "%s Keystone DB queries count" % key,
                nodes["DB queries"][key]["total"]])
            common_info_table.add_row([
                "%s Keystone DB queries time spent, ms" % key,
                nodes["DB queries"][key]["time_spent"]])
        detect_outliers(NODES["DB queries"][key]["time_spent"])

    # prepare table with outliers information
    outliers_table = prettytable.PrettyTable(["**DB query**",
                                              "**Time spent, ms**"])
    outliers_table.align["**DB query**"] = "l"
    outliers_table.align["**Time spent, ms**"] = "l"
    outliers_table.max_width = 100
    outliers_table.header = True
    outliers_table.hrules = prettytable.ALL

    for query in OUTLIER_QUERIES:
        outliers_table.add_row([db_query_tmpl % query, OUTLIER_QUERIES[query]])

    # prepare table with information about DB requests containing multiple
    # JOIN statements inside
    multi_join_queries = prettytable.PrettyTable(["**DB query**",
                                                  "**Time spent, ms**"])
    multi_join_queries.align["**DB query**"] = "l"
    multi_join_queries.align["**Time spent, ms**"] = "l"
    multi_join_queries.max_width = 100
    multi_join_queries.header = True
    multi_join_queries.hrules = prettytable.ALL

    for key in ["2joins", "3+joins"]:
        for ts in NODES["DB queries"]["red_flag"][key]["time_spent"]:
            for query in NODES["DB queries"]["red_flag"][key][
                    "time_spent"][ts]:
                multi_join_queries.add_row([db_query_tmpl % query, ts])
    return common_info_table, multi_join_queries, outliers_table


def main():
    parser = argparse.ArgumentParser(description='Process JSON file with '
                                                 'OSprofiler output.')
    parser.add_argument('path', type=str,
                        help='Path to the JSON file / directory with list of '
                             'JSON files with OSprofiler output')

    args = parser.parse_args()
    global NODES
    if os.path.isfile(args.path):
        with open(args.path) as data_file:
            data = json.load(data_file)
            define_nodes(data)
            nodes = sort_dicts(NODES)
            common_info_table, multi_join_queries, outliers_table = \
                prepare_tables(nodes)
            print(common_info_table)
            print(outliers_table)
            print(multi_join_queries)
    elif os.path.isdir(args.path):
        for item in os.listdir(args.path):
            if item.endswith(".txt"):
                with open(os.path.join(args.path, item)) as data_file:
                    data = json.load(data_file)
                    NODES = copy.deepcopy(NODES_TEMPLATE)
                    define_nodes(data)
                    nodes = sort_dicts(NODES)
                    common_info_table, multi_join_queries, outliers_table = \
                        prepare_tables(nodes)
                    item_name = \
                        item.split(".")[0].replace("_", " ").capitalize() + \
                        " request stats"
                    print(item_name)
                    print(len(item_name) * "~" + "\n")
                    print("**%s**\n" % "Control plane request overlook")
                    print(common_info_table)
                    print("\n**%s**\n" % "Keystone DB queries outliers")
                    print(outliers_table)
                    print("\n**%s**\n" % "Keystone DB queries with multi "
                                         "JOINs inside")
                    print(multi_join_queries)
                    print("\n")


if __name__ == "__main__":
    main()
