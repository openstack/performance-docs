import os
import random
import shlex
import socket
import string
import subprocess
import threading
import time

import jinja2


LIST_SVC_SUCCESS = []
LIST_SVC_FAILED = []
RESULTS_FAILED = []

INTERVAL = 1  # in seconds
SERVICES = 1000  # amount of services
REQUESTS = 1000  # amount of requests


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def id_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_svc():
    service_name = "test-service-{}".format(id_generator())
    file_name = "{}.yaml".format(service_name)

    # Create YAML file for new service
    template = render("template.yaml", {"name": service_name})
    f = open(file_name, "w")
    f.write(template)
    f.close()

    cmd = "kubectl create -f {}".format(file_name)
    args = shlex.split(cmd)

    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()

    # Delete YAML file
    os.remove(file_name)

    if not err:
        print out
        LIST_SVC_SUCCESS.append(service_name)
        return True

    print err
    LIST_SVC_FAILED.append(service_name)
    return False


def delete_svc(service_name):
    cmd = "kubectl delete service {}".format(service_name)
    args = shlex.split(cmd)

    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()

    if not err:
        print out
        return True

    print err
    return False


def request_to_host(service_name):
    host = "{}.default.svc.cluster.local".format(service_name)
    try:
        print socket.gethostbyname(host)
    except socket.gaierror:
        return False

    return True


def multi_requests():
    for i in range(0, REQUESTS):
        num_service = random.randint(0, len(LIST_SVC_SUCCESS) - 1)
        service_name = LIST_SVC_SUCCESS[num_service]
        if not request_to_host(service_name):
            RESULTS_FAILED.append(service_name)
        time.sleep(INTERVAL)


def clean_up():
    for svc in LIST_SVC_SUCCESS:
        delete_svc(svc)


def test_case(threads=50):
    query = []
    del RESULTS_FAILED[:]

    for i in range(0, threads):
        query.append(threading.Thread(target=multi_requests, args=()))

    for t in query:
        t.start()

    for t in query:
        t.join()

    return len(RESULTS_FAILED)


if __name__ == "__main__":
    # Create services
    for i in range(0, SERVICES):
        success = create_svc()

    # Run test case
    for i in range(1, 21):
        print "{} rps".format(i * 50)
        result = test_case(i * 50)
        print "Wasn't resolve {} host(s)".format(result)

        with open("result.txt", "a") as f:
            f.write("{} rps - wasn't resolve {} host(s)\n".format(
                i * 50, result))

    # Delete created service
    clean_up()
