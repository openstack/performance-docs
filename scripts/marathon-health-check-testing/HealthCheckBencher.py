#!/usr/bin/python


from argparse import ArgumentParser
from datetime import datetime
from hashlib import md5
from marathon import MarathonClient
from marathon.models.container import MarathonContainer
from marathon.models.container import MarathonContainerPortMapping
from marathon.models.container import MarathonDockerContainer
from marathon.models import MarathonApp
from marathon.models import MarathonHealthCheck
from Queue import Empty
from Queue import Queue
from random import random
from threading import Thread
from time import sleep
from urllib2 import urlopen

MEM = 50
CPUS = 1
DISK = 50


class HealthCheckBencher(object):
    def __init__(self, marathon_url, image, tasks):
        self.concurrency = 20
        self.docker_image = image
        self.app_base_name = 'health-check-test-'
        self.total_tasks_cout = int(tasks)
        self.instances_per_app = 50
        if tasks < self.instances_per_app:
            self.instances_per_app = self.total_tasks_cout
            self.app_count = 1
        else:
            self.app_count = self.total_tasks_cout/self.instances_per_app
        self.heath_check_interval = 30
        self.test_duration = 20
        self.marathon_cluster = MarathonClient(marathon_url, timeout=240)
        self.work_queue = Queue()
        self.result_queue = Queue()
        self.app_list_queue = Queue()
        self.action_list = [self.start_collect,
                            'sleep={}'.format(self.test_duration),
                            self.get_stats]

    def remove_apps(self):
        apps = self.marathon_cluster.list_apps()
        for app in apps:
            if app.id.startswith("/"+self.app_base_name):
                self.marathon_cluster.delete_app(app.id)
        active = 0
        while True:
            apps = self.marathon_cluster.list_apps()
            for app in apps:
                if app.id.startswith(self.app_base_name):
                    active += 1
            if active == 0:
                break

    def create_app(self, id):
        port_mapping = MarathonContainerPortMapping(container_port=80,
                                                    protocol="tcp")
        app_docker = MarathonDockerContainer(
            image=self.docker_image,
            network="BRIDGE",
            force_pull_image=True,
            port_mappings=[port_mapping])
        app_container = MarathonContainer(docker=app_docker)
        http_health_check = MarathonHealthCheck(
            protocol="HTTP",
            path="/status",
            grace_period_seconds=300,
            interval_seconds=self.heath_check_interval,
            timeout_seconds=20,
            max_consecutive_failures=0
        )

        app_suffix = str(md5(str(random())).hexdigest())
        app_name = self.app_base_name + app_suffix
        new_app = MarathonApp(cpus=CPUS, mem=MEM, disk=DISK,
                              container=app_container,
                              health_checks=[http_health_check],
                              instances=self.instances_per_app,
                              max_launch_delay_seconds=5)
        print("Creating {}".format(app_name))
        self.marathon_cluster.create_app(app_id=app_name, app=new_app)
        self.app_list_queue.put(app_name)
        return None

    def wait_instances(self, app_name):
        health_ok = 0
        while health_ok < self.instances_per_app:
            health_ok = 0
            tasks = self.marathon_cluster.list_tasks(app_name)
            for task in tasks:
                if task.health_check_results:
                    health_ok += 1

    def start_collect(self, task):
        url = 'http://'+task['host']+':'+str(task['port'])+'/start_collect'
        res = urlopen(url)
        if res.getcode() == 200:
            print(task['id']+': collecter was started')
        else:
            print(task['id']+': failed to start collecter')

    def stop_collect(self, task):
        url = 'http://'+task['host']+':'+str(task['port'])+'/stop_collect'
        res = urlopen(url)
        if res.getcode() == 200:
            print(task['id']+': collecter was stopped')
        else:
            print(task['id']+': failed to stop collecter')

    def clear_stats(self, task):
        url = 'http://'+task['host']+':'+str(task['port'])+'/clear_stats'
        res = urlopen(url)
        if res.getcode() == 200:
            print(task['id']+': stats was dropped')
        else:
            print(task['id']+': stats was dropped')

    def get_stats(self, task):
        url = 'http://'+task['host']+':'+str(task['port'])+'/get_timestamps'
        try:
            res = urlopen(url)
        except Exception:
            print("URL req failed")
            self.result_queue.put({'id': task['id'],
                                   'status': 'Failed',
                                   'data': []})
            return
        if res.getcode() == 200:
            data = res.read()
            timestamps = data.split(',')
            self.result_queue.put({'id': task['id'],
                                   'status': 'ok',
                                   'data': timestamps})
        elif res.getcode() == 202:
            print("Collecting is not enabled")
            self.result_queue.put({'id': task['id'],
                                   'status': 'Collecting is not enabled',
                                   'data': []})
        else:
            print("Unknown response code")
            self.result_queue.put({'id': task['id'],
                                   'status': 'Unknown response code',
                                   'data': []})

    def repeat(self, action):
        while self.work_queue.empty() is False:
            try:
                iteration = self.work_queue.get_nowait()
            except Empty:
                continue
            action(iteration)
            self.work_queue.task_done()

    def fill_queue(self, iterations):
        for iteration in iterations:
            self.work_queue.put(iteration)

    def get_tasks(self):
        res = []
        tasks = self.marathon_cluster.list_tasks()
        for task in tasks:
            if not task.id.startswith('health-check-test-'):
                continue
            res.append({'id': str(task.id),
                        'host': str(task.host),
                        'port': str(task.ports[0])})
        return res

    def create_apps(self):
        self.fill_queue(range(self.app_count))
        for thread_num in range(self.concurrency):
            if self.work_queue.empty() is True:
                break
            worker = Thread(target=self.repeat, args=(self.create_app,))
            worker.start()
        self.work_queue.join()

        while self.app_list_queue.empty() is False:
            try:
                app_name = self.app_list_queue.get_nowait()
            except Empty:
                continue
            self.work_queue.put(app_name)

        for thread_num in range(self.concurrency):
            if self.work_queue.empty() is True:
                break
            worker = Thread(target=self.repeat, args=(self.wait_instances,))
            worker.start()
        self.work_queue.join()

    def start_test(self):
        task_list = self.get_tasks()
        for action in self.action_list:
            if isinstance(action, basestring):
                if action.startswith('sleep='):
                    amount = int(action.split('=')[1])
                    sleep(60*amount)
                continue
            self.fill_queue(task_list)
            for thread_num in range(self.concurrency):
                if self.work_queue.empty() is True:
                    break
                worker = Thread(target=self.repeat, args=(action,))
                worker.start()
            self.work_queue.join()

    def generate_report(self):
        today = datetime.today()
        file_prefix = "{:%Y-%m-%d_%H_%M_%S-}".format(today)
        file_name = (file_prefix +
                     'health_check_result-' +
                     str(self.total_tasks_cout) +
                     'tasks.csv')

        f = open(file_name, "w")
        f.write("Task ID,Health check timestamp")

        while self.result_queue.empty() is False:
            try:
                result = self.result_queue.get_nowait()
            except Empty:
                continue
            for timestamp in result['data']:
                f.write("\n%s,%s" % (result['id'], timestamp))

        f.close()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-m", "--marathon",
                        help="Marathon URL, on example "
                             "http://172.20.8.34:8080/virt-env-2/marathon",
                        required=True)
    parser.add_argument("-t", "--tasks",
                        help="Total tasks count",
                        required=True)
    parser.add_argument("-i", "--image",
                        help="Docker image path",
                        required=True)
    args = parser.parse_args()

    bencher = HealthCheckBencher(args.marathon, args.image, int(args.tasks))

    bencher.create_apps()
    bencher.start_test()
    bencher.remove_apps()
    bencher.generate_report()
