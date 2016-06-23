# Copyright 2014: Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

#!/bin/bash -xe

# source credentionals
if [ -f /data/rally/rally_plugins/scrappy/scrappy.conf ];
then
    . /data/rally/rally_plugins/scrappy/scrappy.conf
else
    exit -1
fi

#
# Function exetute command over ssh
# Login & password stored in scrappy.conf
#
function ssh_exec() {
    local ssh_node=$1
    local ssh_cmd=$2
    local ssh_options='-oConnectTimeout=5 -oStrictHostKeyChecking=no -oCheckHostIP=no -oUserKnownHostsFile=/dev/null -oRSAAuthentication=no'
    echo "sshpass -p ${SSH_PASS} ssh ${ssh_options} ${SSH_LOGIN}@${ssh_node} ${ssh_cmd}"
    local ssh_result=`sshpass -p ${SSH_PASS} ssh ${ssh_options} ${SSH_LOGIN}@${ssh_node} ${ssh_cmd}`
    echo "$ssh_result"
}

#
# Function return random controller node from Fuel cluster
#
function get_random_controller() {
    local random_controller=${CONTROLLERS[$RANDOM % ${#CONTROLLERS[@]}]}
    echo $random_controller
}

#
# Function return random compute node from Fuel cluster
#
function get_random_compute() {
    local random_compute=${COMPUTES[$RANDOM % ${#COMPUTES[@]}]}
    echo $random_compute
}

#
# Factors
#
function random_controller_kill_rabbitmq() {
    local action=$1
    local controller_node=$(get_random_controller)
    local result=`ssh_exec ${controller_node} "${SCRAPPY_BASE}/scrappy_host.sh send_signal rabbitmq_server -KILL"`
    echo "$result"
}

function random_controller_freeze_process_random_interval() {
    local process_name=$1
    local interval=$2
    local controller_node=$(get_random_controller)
    local result=`ssh_exec ${controller_node} "${SCRAPPY_BASE}/scrappy_host.sh freeze_process_random_interval ${process_name} ${interval}"`
    echo "$result"
}

function random_controller_freeze_process_fixed_interval() {
    local process_name=$1
    local interval=$2
    local controller_node=$(get_random_controller)
    local result=`ssh_exec ${controller_node} "${SCRAPPY_BASE}/scrappy_host.sh freeze_process_fixed_interval ${process_name} ${interval}"`
    echo "$result"
}

function random_controller_reboot() {
    local controller_node=$(get_random_controller)
    local result=`ssh_exec ${controller_node} "${SCRAPPY_BASE}/scrappy_host.sh reboot_node"`
    echo "$result"
}

function usage() {
    echo "usage"
    echo "TODO"
}

#
# Main
#
function main() {
    local factor=$1
    case ${factor} in
    random_controller_kill_rabbitmq)
        random_controller_kill_rabbitmq $2
        ;;
    random_controller_freeze_process_random_interval)
        random_controller_freeze_process_random_interval $2 $3
        ;;
    random_controller_freeze_process_fixed_interval)
        random_controller_freeze_process_fixed_interval $2 $3
        ;;
    random_controller_reboot)
        random_controller_reboot
        ;;
    *)
        usage
        ;;
    esac
}

main "$@"
