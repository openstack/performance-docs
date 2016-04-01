import argparse
import hashlib
import logging
import random
import signal


from marathon import MarathonClient
from marathon.models.constraint import MarathonConstraint
from marathon.models.container import MarathonContainer
from marathon.models.container import MarathonContainerPortMapping
from marathon.models.container import MarathonDockerContainer
from marathon.models import MarathonApp
from marathon.models import MarathonHealthCheck
from multiprocessing import Pool

MEM = 256
CPUS = 1
DISK = 50


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def create_app(app_instances):
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
                                            interval_seconds=30,
                                            timeout_seconds=20,
                                            max_consecutive_failures=3)

    app_name = str(hashlib.md5(str(random.random())).hexdigest())
    logging.debug("Create cluster {}".format(app_name))
    app_constraint = MarathonConstraint(field="hostname", operator="UNIQUE")
    new_app = MarathonApp(cpus=CPUS, mem=MEM, disk=DISK,
                          container=app_container,
                          health_checks=[http_health_check],
                          instances=app_instances,
                          constraints=[app_constraint],
                          max_launch_delay_seconds=5)
    print("Creating {}".format(app_name))
    cluster.create_app(app_id=app_name,
                       app=new_app)
    return None


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
        print("=======  Creating {1} applications with {0} instances, "
              "concurrency is {1} "
              "===============".format(instances, concurrency))
    list_instances = [instances] * concurrency
    return concur_operations("create_app", str(list_instances),
                             concurrency)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--marathon",
                        help="Marathon URL, on example "
                             "http://127.0.0.1:8080/marathon",
                        required=True)
    parser.add_argument("-e", "--execute", help="Operation execute",
                        choices=['delete', 'create'], required=True)
    parser.add_argument("-d", "--delete",
                        help="Delete all applications",
                        action="store_true")
    parser.add_argument("-c", "--concurrency",
                        help="Concurrency")
    parser.add_argument("-n", "--nodes",
                        help="Number of tasks per application")
    parser.add_argument("-s", "--silent",
                        help="Print only results",
                        action="store_true")
    args = parser.parse_args()
    cluster = MarathonClient(args.marathon, timeout=240)

    if args.execute == "delete":
        cluster = MarathonClient(args.marathon)
        all_apps = cluster.list_apps()
        for app in all_apps:
            print("Delete {}".format(app.id))
            cluster.delete_app(app.id, force=True)
    if args.execute == "create":
        concur = 1 if args.concurrency is None else args.concurrency
        nodes = 1 if args.nodes is None else args.nodes
        concur_create_apps(int(concur), int(nodes))
