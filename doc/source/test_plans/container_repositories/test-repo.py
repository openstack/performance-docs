#!/usr/bin/python

from subprocess import Popen, PIPE
from time import time
from threading import Thread
from Queue import Queue
import os
import argparse

iterations = 1000
concurrency = 30
repo_address = "172.20.9.16:5000"

repo_ref = "/test-1"
repo_url = repo_address + repo_ref
container_name = "nginx"
container_tag = "latest"
work_dir = "containers/nginx"
build_results_file = "build_results.csv"
push_results_file = "push_results.csv"
pull_results_file = "pull_results.csv"
delete_local_results_file = "delete_local_results.csv"

results_files = [build_results_file, push_results_file, pull_results_file, delete_local_results_file]
for results_file in results_files:
    outfile = open(results_file, 'w')
    outfile.write("iteration,spent_time")
    outfile.close()

work_queue = Queue()


def build_container(iteration):
    start_time = time()
    build_command = Popen(['docker', 'build', '--no-cache=true', '-t', repo_url + '/' + container_name + '-' + str(iteration) + ':' + container_tag, '--file=' + work_dir + '/Dockerfile', work_dir])
    build_command.wait()
    end_time = time()
    action_time = end_time - start_time
    print "Iteration", iteration, "has been done in", action_time
    outfile = open(build_results_file, 'a')
    outfile.write('\n' + str(iteration) + "," + str(action_time))
    outfile.close()


def push_container(iteration):
    start_time = time()
    build_command = Popen(['docker', 'push', repo_url + '/' + container_name + '-' + str(iteration)])
    build_command.wait()
    end_time = time()
    action_time = end_time - start_time
    print "Iteration", iteration, "has been done in", action_time
    outfile = open(push_results_file, 'a')
    outfile.write('\n' + str(iteration) + "," + str(action_time))
    outfile.close()


def delete_local_images(iteration):
    start_time = time()
    delete_local_images_command = Popen(['docker', 'rmi', repo_url + '/' + container_name + '-' + str(iteration)])
    delete_local_images_command.wait()
    end_time = time()
    action_time = end_time - start_time
    print "Iteration", iteration, "has been done in", action_time
    outfile = open(delete_local_results_file, 'a')
    outfile.write('\n' + str(iteration) + "," + str(action_time))
    outfile.close()


def pull_container(iteration):
    start_time = time()
    build_command = Popen(['docker', 'pull', repo_url + '/' + container_name + '-' + str(iteration)])
    build_command.wait()
    end_time = time()
    action_time = end_time - start_time
    print "Iteration", iteration, "has been done in", action_time
    outfile = open(pull_results_file, 'a')
    outfile.write('\n' + str(iteration) + "," + str(action_time))
    outfile.close()


def repeat():
    while work_queue.empty() is False:
        iteration = work_queue.get_nowait()
        container_action(iteration)
        work_queue.task_done()


def fill_queue(iterations):
    for iteration in range(1, (iterations + 1)):
        work_queue.put(iteration)

container_actions = [build_container, push_container, delete_local_images, pull_container]
for container_action in container_actions:
    fill_queue(iterations)
    for thread_num in range(1, (concurrency + 1)):
        if work_queue.empty() is True:
            break
        worker = Thread(target=repeat)
        worker.start()
    work_queue.join()
