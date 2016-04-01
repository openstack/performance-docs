import argparse
import hashlib
import json
import logging
import random
import signal
import statistics
import sys
import time


from marathon import MarathonClient
from marathon.models.container import MarathonContainer
from marathon.models.container import MarathonContainerPortMapping
from marathon.models.container import MarathonDockerContainer
from marathon.models import MarathonApp
from marathon.models import MarathonHealthCheck


from multiprocessing import Pool

MEM = 256
CPUS = 1
DISK = 50


def percentage(part, whole):
    return 100 * float(part)/float(whole)


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def is_timeout(start_time, timeout):
    logging.debug("[is_timeout] start timeout is  {}".format(start_time))
    if time.time() - start_time > timeout:
        logging.warning("Timeout")
        return True
    else:
        return False


def check_instances(check, app_instances, app_name, start_time, timeout,
                    ready_tasks=None):
    in_progress = 0
    while in_progress < app_instances:
        in_progress = 0
        tasks = cluster.list_tasks(app_name)
        for task in tasks:
            if check == "task":
                if ready_tasks is not None:
                    app_index = -1
                    for ready_task in ready_tasks:
                        app_index += 1
                        if ready_task.id != task.id:
                            break
                    if (task.started_at is not None and
                            task.started_at !=
                            ready_tasks[app_index].started_at):
                        logging.info("[check_instances] Task started "
                                     "at {}".format(task.started_at))
                        in_progress += 1
                else:
                    if task.started_at is not None:
                        logging.info("[check_instances] Task started "
                                     "at {}".format(task.started_at))
                        in_progress += 1
            elif check == "health":
                if task.health_check_results:
                    in_progress += 1
        if is_timeout(start_time, timeout):
            return in_progress
    return in_progress


def delete_app(app_name, force=False):
    cluster.delete_app(app_id=app_name, force=force)


def calculate_results_per_operation(results):
    return {"app_name": results[0],
            "instances": results[1],
            "successful_instances": results[2],
            "successful_instance_percent": percentage(results[2], results[1]),
            "app_full_time": round(results[3], 2),
            "instances_mean": round(statistics.mean(results[4]), 2),
            "instances_median": round(statistics.median(results[4]), 2),
            "instances_min": round(min(results[4]), 2),
            "instances_max": round(max(results[4]), 2)}


def check_in_deployment(app_name, timeout):
    deployments = 1
    start_time = time.time()
    while deployments != 0 and not is_timeout(start_time, timeout):
        for app in cluster.list_apps():
            if app.id == "/{}".format(app_name):
                deployments = len(app.deployments)
    return None


def check_operation_status(start_time, app_name, app_instances,
                           timeout, ready_tasks=None):
    successful_instances = check_instances(
        "task", app_instances, app_name, start_time, timeout, ready_tasks)
    all_starting = []
    tasks = cluster.list_tasks(app_name)
    for task in tasks:
        logging.info("[check_operation_status] Task started at ="
                     " {}".format(task.started_at))
        logging.debug("[check_operation_status] {} - {} ".format(
            task.started_at, task.staged_at))
        if task.started_at is not None:
            starting = task.started_at - task.staged_at
            all_starting.append(starting.total_seconds())
    if len(all_starting) == 0:
        all_starting = [0]
    check_in_deployment(app_name, timeout)
    logging.debug("[check_operation_status] start time is {}".format(
        start_time))
    app_full_time = time.time() - start_time
    return successful_instances, all_starting, app_full_time


def restart_and_wait_app(app_name):
    timeout = 600
    list_tasks = cluster.list_tasks(app_name)
    app_instances = len(list_tasks)
    start_time = time.time()
    cluster.restart_app(app_id=app_name)
    time.sleep(5)
    successful_instances, all_starting, app_full_time = \
        check_operation_status(start_time, app_name, app_instances,
                               timeout, list_tasks)
    return calculate_results_per_operation([app_name, app_instances,
                                            successful_instances,
                                            app_full_time,
                                            all_starting])


def update_and_wait_cpu(app_name):
    return update_and_wait_app(app_name, "cpu", "2")


def update_and_wait_mem(app_name):
    return update_and_wait_app(app_name, "mem", "2")


def update_and_wait_disk(app_name):
    return update_and_wait_app(app_name, "disk", "2")


def update_and_wait_instances(app_name):
    return update_and_wait_app(app_name, "instances", "2")


def update_and_wait_app(app_name, scale_param, scale, scale_type="*"):
    timeout = 600
    list_tasks = cluster.list_tasks(app_name)
    app_instances = len(list_tasks)
    cpus = CPUS
    mem = MEM
    disk = DISK
    instances = app_instances
    if scale_param == "cpu":
        cpus = eval("{} {} {}".format(cpus, scale_type, scale))
    if scale_param == "mem":
        mem = eval("{} {} {}".format(mem, scale_type, scale))
    if scale_param == "disk":
        disk = eval("{} {} {}".format(disk, scale_type, scale))
    if scale_param == "instances":
        instances = eval("{} {} {}".format(instances, scale_type, scale))

    updated_app = MarathonApp(cpus=cpus, mem=mem, disk=disk,
                              instances=instances)
    start_time = time.time()
    cluster.update_app(app_id=app_name, app=updated_app)
    time.sleep(5)
    successful_instances, all_starting, app_full_time = \
        check_operation_status(start_time, app_name, instances,
                               timeout, list_tasks)
    return calculate_results_per_operation([app_name, app_instances,
                                            successful_instances,
                                            app_full_time,
                                            all_starting])


def delete_and_wait_app(app_name):
    timeout = 600
    start_time = time.time()
    try:
        cluster.delete_app(app_id=app_name)
        while (len(cluster.list_apps()) > 0 and
                time.time() - start_time < timeout):
            time.sleep(0.01)
        logging.debug("[delete_and_wait_app] start time is {}".format(
            start_time))
        end_time = time.time() - start_time
        return {"app_name": app_name,
                "delete_time": round(end_time, 2)
                }
    except BaseException as ex:
        logging.error(ex)
        return {"app_name": app_name,
                "delete_time": None
                }


def create_and_delete_app(app_instances):
    return create_app(app_instances, delete=True)


def create_several_apps(apps_amount, instances_amount):
    all_apps = []
    if not args.silent:
        print("=======  Creating {} applications, with {} instances "
              "===============".format(apps_amount, instances_amount))
        sys.stdout.write('Creating apps: ')
    for count in range(apps_amount):
        if not args.silent:
            if count % 10:
                sys.stdout.write('.')
                sys.stdout.flush()
            else:
                sys.stdout.write(str(count))
                sys.stdout.flush()
        all_apps.append(
            create_app(app_instances=instances_amount,
                       need_statistics=False)["app_name"])
    if not args.silent:
        print(str(apps_amount))
    return all_apps


def create_app(app_instances, delete=False,
               timeout=1200, need_statistics=True):
    port_mapping = MarathonContainerPortMapping(container_port=80,
                                                protocol="tcp")
    app_docker = MarathonDockerContainer(
        image="nginx",
        network="BRIDGE",
        port_mappings=[port_mapping])
    app_container = MarathonContainer(docker=app_docker)
    http_health_check = MarathonHealthCheck(protocol="HTTP",
                                            path="/",
                                            grace_period_seconds=300,
                                            interval_seconds=2,
                                            timeout_seconds=20,
                                            max_consecutive_failures=3)

    app_name = str(hashlib.md5(str(random.random())).hexdigest())
    logging.debug("Create cluster {}".format(app_name))
    new_app = MarathonApp(cpus=CPUS, mem=MEM, disk=DISK,
                          container=app_container,
                          health_checks=[http_health_check],
                          instances=app_instances,
                          max_launch_delay_seconds=5)
    start_time = time.time()
    cluster.create_app(app_id=app_name,
                       app=new_app)
    logging.debug("Get tasks for cluster {}".format(app_name))
    successful_instances, all_starting, app_full_time = \
        check_operation_status(start_time, app_name, app_instances, timeout)
    if delete:
        logging.debug('Delete {}'.format(app_name))
        delete_app(app_name, force=True)
    if need_statistics:
        return {"app_name": app_name,
                "app_full_time": round(app_full_time, 2),
                "instances": app_instances,
                "successful_instances": successful_instances,
                "instances_mean": round(statistics.mean(all_starting), 2),
                "instances_median": round(statistics.median(all_starting), 2),
                "instances_min": round(min(all_starting), 2),
                "instances_max": round(max(all_starting), 2),
                "id_run": id_run}
    else:
        return {"app_name": app_name}


def concur_operations(function, arguments, concurrency):
    pool = Pool(concurrency, init_worker)
    results = []
    try:
        results = eval("pool.map({}, {})".format(function, arguments))
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
        pool.join()
    return results


def concur_create_apps(concurrency, instances):
    if not args.silent:
        print("=======  Creating applications with {} instances, "
              "concurrency is {} "
              "===============".format(instances, concurrency))
    list_instances = [instances] * concurrency
    return concur_operations("create_and_delete_app", str(list_instances),
                             concurrency)


def concur_restart_apps(concurrency, instances):
    apps = create_several_apps(concurrency, instances)
    if not args.silent:
        print("=======  Restart applications with {} instances , "
              "concurrency is {} "
              "===============".format(instances, concurrency))
    results = concur_operations("restart_and_wait_app", str(apps), concurrency)
    for app in apps:
        delete_app(app, True)
    return results


def concur_update_app(update_type, concurrency, instances):
    apps = create_several_apps(concurrency, instances)
    if not args.silent:
        print("=======  Update applications, concurrency is {} "
              "===============".format(concurrency))
    results = []
    if update_type == "cpu":
        results = concur_operations("update_and_wait_cpu", str(apps),
                                    concurrency)
    if update_type == "mem":
        results = concur_operations("update_and_wait_mem", str(apps),
                                    concurrency)
    if update_type == "disk":
        results = concur_operations("update_and_wait_disk", str(apps),
                                    concurrency)
    if update_type == "instances":
        results = concur_operations("update_and_wait_instances", str(apps),
                                    concurrency)
    for app in apps:
        delete_app(app, True)
    return results


def concur_delete_apps(concurrency, instances):
    apps = create_several_apps(concurrency, instances)
    if not args.silent:
        print("=======  Delete applications with {}, concurrency is {} "
              "===============".format(instances, concurrency))
    results = concur_operations("delete_and_wait_app", str(apps), concurrency)
    return results


def calculate_summary(results):
    if len(results[0]) == 10:
        max_tmp = []
        min_tmp = []
        successful_tmp = []
        mean_tmp = []
        median_tmp = []
        app_full_time_tmp = []
        for result in results:
            max_tmp.append(result["instances_max"])
            min_tmp.append(result["instances_min"])
            successful_tmp.append(result["successful_instances"])
            mean_tmp.append(result["instances_mean"])
            median_tmp.append(result["instances_median"])
            app_full_time_tmp.append(result["app_full_time"])
        sum_result = {
            "type": "summary",
            "instances_max": max(max_tmp),
            "instances_min": min(min_tmp),
            "instances_mean": round(statistics.mean(mean_tmp), 2),
            "instances_median": statistics.median(median_tmp),
            "app_full_time_max": max(app_full_time_tmp),
            "app_full_time_min": min(app_full_time_tmp),
            "app_full_time_mean": round(statistics.mean(app_full_time_tmp), 2),
            "app_full_time_median": statistics.median(app_full_time_tmp),
            "test": args.tests,
            "concurrency": args.concurrency,
            "nodes": args.nodes,
            "id_run": id_run
        }
    else:
        time_tmp = []
        delete_fails = 0
        for result in results:
            if result["delete_time"] is not None:
                time_tmp.append(result["delete_time"])
            else:
                delete_fails += 1
        sum_result = {
            "type": "summary",
            "delete_time_max": max(time_tmp),
            "delete_time_min": min(time_tmp),
            "delete_time_mean": round(statistics.mean(time_tmp), 2),
            "delete_time_median": round(statistics.median(time_tmp), 2),
            "delete_fails": delete_fails,
            "test": args.tests,
            "concurrency": args.concurrency,
            "nodes": args.nodes,
            "id_run": id_run
        }

    return sum_result


def print_results(results):
    full_results = []
    for result in results:
        result["type"] = "single"
        full_results.append(result)
    full_results.append(calculate_summary(results))
    if args.only_summary:
        for result in full_results:
            if result["type"] == "summary":
                full_results = [result]
    if args.pretty_output:
        print(json.dumps(full_results, sort_keys=True,
                         indent=4, separators=(',', ': ')))
    else:
        print("{},".format(json.dumps(full_results, sort_keys=True)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tests", help="Tests",
                        choices=['all', 'create', 'update_cpu',
                                 'update_mem', 'update_disk',
                                 'update_instances',
                                 'restart', 'delete'], required=True)
    parser.add_argument("-m", "--marathon",
                        help="Marathon URL, on example "
                             "http://172.20.8.34:8080/virt-env-2/marathon",
                        required=True)
    parser.add_argument("-c", "--concurrency",
                        help="Concurrency",
                        required=True)
    parser.add_argument("-n", "--nodes",
                        help="Number of tasks per application",
                        required=True)
    parser.add_argument("-l", "--log_level", help="logging level",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR',
                                 'CRITICAL'])
    parser.add_argument("-s", "--silent",
                        help="Print only results",
                        action="store_true")
    parser.add_argument("-o", "--only_summary",
                        help="Print only summary results",
                        action="store_true")
    parser.add_argument("-p", "--pretty_output",
                        help="Pretty json outpur",
                        action="store_true")
    args = parser.parse_args()

    cluster = MarathonClient(args.marathon)
    id_run = str(hashlib.md5(str(random.random())).hexdigest())

    if args.log_level is None:
        log_level = logging.DEBUG
    else:
        log_level = eval("logging.{}".format(args.log_level))
    logging.basicConfig(
        filename="tests-debug.log",
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if args.tests == "create":
        print_results(concur_create_apps(int(args.concurrency),
                                         int(args.nodes)))

    if args.tests == "restart":
        print_results(concur_restart_apps(int(args.concurrency),
                                          int(args.nodes)))
    if args.tests == "update_cpu":
        print_results(concur_update_app("cpu",
                                        int(args.concurrency),
                                        int(args.nodes)))

    if args.tests == "update_mem":
        print_results(concur_update_app("mem",
                                        int(args.concurrency),
                                        int(args.nodes)))

    if args.tests == "update_disk":
        print_results(concur_update_app("disk",
                                        int(args.concurrency),
                                        int(args.nodes)))
    if args.tests == "update_instances":
        print_results(concur_update_app("instances",
                                        int(args.concurrency),
                                        int(args.nodes)))

    if args.tests == "delete":
        print_results(concur_delete_apps(int(args.concurrency),
                                         int(args.nodes)))
