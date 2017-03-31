import os
import random
import shlex
import string
import subprocess

import jinja2

SERVICES = 100  # amount of services, > len(NODES)
REPLICAS = 1
NODES = ['node2', 'node3', 'node4', 'node5', 'node6']


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def id_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_svc(node='node1'):
    service_name = "minion-{}".format(id_generator())
    file_name = "{}.yaml".format(service_name)

    # Create YAML file for new service
    template = render("service.yaml", {"name": service_name})
    f = open(file_name, "w")
    f.write(template)
    f.close()

    cmd = "kubectl -n minions create -f {}".format(file_name)
    args = shlex.split(cmd)

    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()

    # Delete YAML file
    os.remove(file_name)

    if not err:
        return True

    print err
    return False


def main():
    service_per_node = int(SERVICES / len(NODES))
    for node in NODES:
        for i in range(0, service_per_node):
            success = create_svc(node=node)

if __name__ == "__main__":
    main()
