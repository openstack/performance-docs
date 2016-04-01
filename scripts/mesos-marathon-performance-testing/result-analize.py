import argparse
import copy
import json

import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--results",
                    help="File with results",
                    required=True)
args = parser.parse_args()

with open(args.results) as data_file:
    data = json.load(data_file)


# Create empty json for results
tmp_nodes = {}
for nodes in [50, 100, 500]:
    tmp_nodes[nodes] = []
tmp_concur = {}
for concur in [1, 2, 4, 8, 16]:
        tmp_concur[concur] = copy.deepcopy(tmp_nodes)
results_sum = {}
for tests in ["create", "update_cpu", "update_mem", "update_disk",
              "update_instances", "restart", "delete"]:
    results_sum[tests] = copy.deepcopy(tmp_concur)

for i in data:
    for j in i:
        if j["type"] == "summary":
            t_test = j["test"]
            t_concur = int(j["concurrency"])
            t_nodes = int(j["nodes"])
            if j["test"] != "delete":
                results_sum[t_test][t_concur][t_nodes] = [
                    j["app_full_time_min"], j["app_full_time_max"],
                    j["app_full_time_mean"], j["app_full_time_median"]]
            else:
                results_sum[t_test][t_concur][t_nodes] = [
                    j["delete_time_min"], j["delete_time_max"],
                    j["delete_time_mean"], j["delete_time_median"]]

for test in sorted(results_sum):
    graph_string = ""
    test_title = "Test {}".format(test)
    print(test_title)
    print("-" * len(test_title))
    print("+-------------+------------------------------+--------+--------"
          "+---------+--------+\n"
          "| CONCURRENCY | NODES_NUMBER_PER_APPLICATION | "
          "APPLICATION_OPERATION              |\n"
          "|             |                              +--------+--------+"
          "---------+--------+\n"
          "|             |                              |minima  | maxima | "
          "average | median |\n"
          "+=============+==============================+========+========+="
          "========+========+")
    for concurrency in sorted(results_sum[test]):
        graph_max = ()
        graph_min = ()
        graph_mean = ()
        graph_median = ()
        for nodes in sorted(results_sum[test][concurrency]):
            if len(results_sum[test][concurrency][nodes]) > 0:
                print("|{:<13}|{:<30}|{:<8}|{:<8}|{:<9}|{:<8}|".format(
                    concurrency, nodes,
                    results_sum[test][concurrency][nodes][0],
                    results_sum[test][concurrency][nodes][1],
                    results_sum[test][concurrency][nodes][2],
                    results_sum[test][concurrency][nodes][3],
                    ))
                print("+-------------+------------------------------+--------"
                      "+--------+---------+--------+")
                graph_min += (results_sum[test][concurrency][nodes][0],)
                graph_max += (results_sum[test][concurrency][nodes][1],)
                graph_mean += (results_sum[test][concurrency][nodes][2],)
                graph_median += (results_sum[test][concurrency][nodes][3],)

        if (len(graph_max) == 3 and len(graph_min) == 3 and len(graph_mean) and
                len(graph_median) == 3):
            fig, ax = plt.subplots()
            n_groups = 3
            plt.subplot()
            index = np.arange(n_groups)
            bar_width = 0.15
            opacity = 0.4
            plt.bar(index,  graph_min, bar_width,
                    alpha=opacity,
                    color='g',
                    label='Min')
            plt.bar(index + bar_width, graph_mean, bar_width,
                    alpha=opacity,
                    color='y',
                    label='Median')
            plt.bar(index + bar_width*2, graph_median, bar_width,
                    alpha=opacity,
                    color='b',
                    label='Mean')
            plt.bar(index + bar_width*3, graph_max, bar_width,
                    alpha=opacity,
                    color='r',
                    label='Max')

            plt.xlabel('Nodes')
            plt.ylabel('Seconds')
            plt.title('Test {}'.format(test))
            plt.xticks(index + bar_width*2, ('50', '100', '500'))
            plt.legend(loc=0)
            plt.tight_layout()
            pic_file_name = "{}-{}.png".format(test, concurrency)
            plt.savefig(pic_file_name)
            graph_string = ("{0}\nGraph for test {2}, "
                            "concurrency {3}\n"
                            "\n.. image:: {1}\n"
                            "   :alt: Graph for test {2}, "
                            "concurrency {3}\n\n".format(
                                graph_string, pic_file_name,
                                test, concurrency))
            plt.close()
    print(graph_string)
