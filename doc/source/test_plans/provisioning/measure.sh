#!/bin/bash

# Need to install the required packages on provisioning system servers:
if (("`dpkg -l | grep dstat | grep ^ii > /dev/null; echo $?` == 1"))
then
  apt-get -y install dstat
fi

# Need to prepare the following script on provisioning system server to collect
# values of CPU,RAM,NET and IO loads per second. You need to change "INTERFACE"
# variable regarding the interface which connected to nodes to communicare with
# them during provisioning process. As a result of this command we'll get
# running in backgroud dstat programm which collecting needed parametes in CSV
# format into /var/log/dstat.log file.:
INTERFACE=eth0
OUTPUT_FILE=/var/log/dstat.csv
dstat --nocolor --time --cpu --mem --net -N ${INTERFACE} --io --output ${OUTPUT_FILE} > /dev/null &

# Need to prepare script which starts provisioning process and gets the time when
# provisioning started and when provisioning ended ( when all nodes reachable via
# ssh). We'll analyze results collected during this time window. For getting
# start time we can add "date" command before API call or CLI command and forward
# the output of the command to some log file. Here is example for cobbler:
ENV_NAME=env-1
start_time=`date +%s.%N`
echo "Provisioning started at "`date` > /var/log/provisioning.log
for SYSTEM in `cobbler system find --comment=${ENV_NAME}`
do
  cobbler system reboot --name=$i &
done

# For getting end-time we can use the script below. This script tries to reach
# nodes via ssh and write "Provisioning finished at <date/time>" into
# /var/log/provisioning.log file. You'll need to provide ip addresses of the
# nodes (from file nodes_ips.list, where IPs listed one per line) and
# creadentials (SSH_PASSWORD and SSH_USER variables):
SSH_OPTIONS="StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
SSH_PASSWORD="r00tme"
SSH_USER="root"
NODE_IPS=(`cat nodes_ips.list`)
TIMER=0
TIMEOUT=20
while (("${TIMER}" < "${TIMEOUT}"))
do
     for NODE_IP in ${NODE_IPS[@]}
     do
             SSH_CMD="sshpass -p ${SSH_PASSWORD} ssh -o ${SSH_OPTIONS} ${SSH_USER}@${NODE_IP}"
             ${SSH_CMD} "hostname" && UNHAPPY_SSH=0 || UNHAPPY_SSH=1
             if (("${UNHAPPY_SSH}" == "0"))
             then
                     echo "Node with ip "${NODE_IP}" is reachable via ssh"
                     NODE_IPS=(${NODE_IPS[@]/${NODE_IP}})
             else
                     echo "Node with ip "${NODE_IP}" is still unreachable via ssh"
             fi
      done
      TIMER=$((${TIMER} + 1))
      if (("${TIMER}" == "${TIMEOUT}"))
      then
              echo "The following "${#NODE_IPS[@]}" are unreachable"
              echo ${NODE_IPS[@]}
              exit 1
      fi
      if ((${#NODE_IPS[@]} == 0 ))
      then
              break
      fi
      # Check that nodes are reachable once per 1 seconds
      sleep 1
done
echo "Provisioning finished at "`date` > /var/log/provisioning.log

end_time=`date +%s.%N`
elapsed_time=$(echo "$end_time - $start_time" | bc -l)
echo "Total elapsed time for provisioning: $elapsed_time seconds" > /var/log/provisioning.log

# Stop dstat command
killall dstat

# Delete excess values and convert to needed metrics. So, we'll get the
# following csv format:
# time,cpu_usage,ram_usage,net_recv,net_send,net_all,dsk_io_read,dsk_io_writ,dsk_all
awk -F "," 'BEGIN {getline;getline;getline;getline;getline;getline;getline;
                   print "time,cpu_usage,ram_usage,net_recv,net_send,net_all,dsk_io_read,dsk_io_writ,dsk_all"}
            {print $1","100-$4","$8/1048576","$12/131072","$13/131072","($12+$13)/131072","$14","$15","$14+$15}' \
$OUTPUT_FILE > /var/log/10_nodes.csv
