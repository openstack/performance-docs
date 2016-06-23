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

LOG_FILE="/var/log/scrappy.log"

#
# Logging function
#
function log() {
    echo "`date -u` scrappy_host: $1" >> ${LOG_FILE}
}

#
# This is function send specified signal
# to all processes with given name
#
function send_signal() {
    local process_name=$1
    local signal=$2
    local pids=`ps -ef | grep $process_name | grep -v grep | grep -v scrappy_host | awk '{print $2}'`
    for each_pid in ${pids};
    do
        log "sending signal: ${signal} to ${process_name} with pid:$each_pid"
        kill ${signal} ${each_pid}
    done
}

#
# This is function control services
#
function service_control() {
    local service_name=$1
    local service_action=$2
    log "service control: $service_name action: $service_action"
    service $service_name $service_action
}

#
# This is function reboot node
#
function reboot_node() {
    log "reboot"
    shutdown -r now
}

#
# This factor freeze specifid process
#
function freeze_process_random_interval {
    local process_name=$1
    local max_interval=$2
    local interval=$(( ($RANDOM % ${max_interval}) + 1))
    log "freeze_process_random_interval: freezing process ${process_name} freeze interval ${interval}"
    send_signal ${process_name} '-STOP'
    sleep ${interval}
    log "freeze_process_random_interval: unfreezing process ${process_name}"
    send_signal ${process_name} '-CONT'
}

#
# This factor freeze specifid process
#
function freeze_process_fixed_interval {
    local process_name=$1
    local interval=$2
    log "freeze_process_fixed_interval: freezing process ${process_name} freeze interval ${interval}"
    send_signal ${process_name} '-STOP'
    sleep ${interval}
    log "freeze_process_fixed_interval: unfreezing process ${process_name}"
    send_signal ${process_name} '-CONT'
}

#
# Show usage
#
function usage() {
    echo "scrappy_host usage:"
    echo "scrappy_host commands:"
    echo -e "\t send_signal process_name signal"
    echo -e "\t service_control service_name action"
    echo -e "\t freeze_process_random_interval process max_interval"
    echo -e "\t freeze_process_fixed_interval process interval"
    echo -e "\t reboot_node"
}

#
# main
#
function main() {
    local command=$1
    case $command in
        send_signal)
            send_signal $2 $3
            ;;
        service_control)
            service_control $2 $3
            ;;
        reboot_node)
            reboot_node
            ;;
        freeze_process_random_interval)
            set +xe
            freeze_process_random_interval $2 $3 &
            set -xe
            ;;
        freeze_process_fixed_interval)
            set +xe
            freeze_process_fixed_interval $2 $3 &
            set -xe
            ;;
        *)
            usage
            exit -1
            ;;
    esac
}

main "$@"
