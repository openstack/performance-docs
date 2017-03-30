import os
import shlex
import subprocess

import jinja2

PODS = 200


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def create(node):
    service_name = "minion-rc-{}".format(node)
    file_name = "{}.yaml".format(service_name)

    # Create YAML file for new service
    template = render("minion-rc.yaml", {"node": node, "replicas": PODS})
    f = open(file_name, "w")
    f.write(template)
    f.close()

    f = open("nodes.txt", 'a')
    f.write("minion-{}\n".format(node))
    f.close()

    cmd = "kubectl create -f {}".format(file_name)
    args = shlex.split(cmd)

    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()

    # Delete YAML file
    os.remove(file_name)


def main():
    # List nodes
    nodes = ["node{}".format(x+1) for x in xrange(20, 430)]
    broken_nodes = ['node16', 'node170', 'node357']
    for n in broken_nodes:
        try:
            nodes.remove(n)
        except ValueError:
            pass

    for n in nodes:
        create(n)


if __name__ == '__main__':
    main()
