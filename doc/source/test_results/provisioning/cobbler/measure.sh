#!/bin/bash -ex

REQUESTED_NODES=$1
ENV_NAME=cobbler-test
INTERFACE=p1p1
DSTAT_OUTPUT_FILE=/var/log/dstat.csv
RESULTS_FILE=/var/log/results.csv

# Need to install the required packages on provisioning system servers:
if (("`dpkg -l | grep dstat | grep ^ii > /dev/null; echo $?` == 1"))
then
  apt-get -y install dstat bc
fi

# Release all nodes from the environment and disable net booting
for SYSTEM in `cobbler system find --comment=${ENV_NAME}`
do
  cobbler system edit --name ${SYSTEM} --comment= --netboot-enabled=no
done

# Check if we have anought nodes
if [ `cobbler system find --comment= | wc -l` < ${REQUESTED_NODES} ]
then
  echo "You have less nodes then requested" | tee -a ${RESULTS_FILE}
  exit 1
fi

# Add requested number of nodes to the env and enable net booting
for SYSTEM in `cobbler system find --comment= | head -${REQUESTED_NODES}`
do
  cobbler system edit --name=${SYSTEM} --comment=${ENV_NAME} --netboot-enabled=yes
done
cobbler sync

# Need to prepare the following script on provisioning system server to collect
# values of CPU,RAM,NET and IO loads per second. You need to change "INTERFACE"
# variable regarding the interface which connected to nodes to communicare with
# them during provisioning process. As a result of this command we'll get
# running in backgroud dstat programm which collecting needed parametes in CSV
# format into /var/log/dstat.log file.:
rm -f ${DSTAT_OUTPUT_FILE}
dstat --nocolor --time --cpu --mem --net -N ${INTERFACE} --io --output ${DSTAT_OUTPUT_FILE} > /dev/null &

# Need to prepare script which starts provisioning process and gets the time when
# provisioning started and when provisioning ended ( when all nodes reachable via
# ssh). We'll analyze results collected during this time window. For getting
# start time we can add "date" command before API call or CLI command and forward
# the output of the command to some log file. Here is example for cobbler:
start_time=`date +%s.%N`
echo "Provisioning started at "`date` > ${RESULTS_FILE}
for SYSTEM in `cobbler system find --comment=${ENV_NAME}`
do
  cobbler system reboot --name=${SYSTEM} &
done

# For getting end-time we can use the script below. This script tries to reach
# nodes via ssh and write "Provisioning finished at <date/time>" into
# /var/log/provisioning.log file. You'll need to provide ip addresses of the
# nodes (from file nodes_ips.list, where IPs listed one per line) and
# creadentials (SSH_PASSWORD and SSH_USER variables):
SSH_OPTIONS="StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
SSH_PASSWORD="r00tme"
SSH_USER="root"
unset NODE_IPS[@]
NODE_IPS=()
for SYSTEM in `cobbler system find --comment=cobbler-test`
do
  NODE_IPS+=(`cobbler system dumpvars --name=${SYSTEM} | grep -w ip_address_${INTERFACE} | awk -F": " '{print $2}'`)
done
TIMER=0
TIMEOUT=50
while (("${TIMER}" < "${TIMEOUT}"))
do
     sleep 10
     for ARRAY_ELEMENT_NUM in $(seq 0 ${#NODE_IPS[@]})
     do
             SSH_CMD="sshpass -p ${SSH_PASSWORD} ssh -o ${SSH_OPTIONS} ${SSH_USER}@${NODE_IPS[${ARRAY_ELEMENT_NUM}]}"
             ${SSH_CMD} "hostname" && UNHAPPY_SSH=0 || UNHAPPY_SSH=1
             if (("${UNHAPPY_SSH}" == "0"))
             then
                     echo "Node with ip "${NODE_IPS[${ARRAY_ELEMENT_NUM}]}" is reachable via ssh"
                     unset NODE_IPS[${ARRAY_ELEMENT_NUM}] && NODE_IPS=(${NODE_IPS[@]})
             else
                     echo "Node with ip "${NODE_IPS[${ARRAY_ELEMENT_NUM}]}" is still unreachable via ssh"
             fi
      done
      TIMER=$((${TIMER} + 1))
      if (("${TIMER}" == "${TIMEOUT}"))
      then
              echo "The following "${#NODE_IPS[@]}" are unreachable" | tee -a ${RESULTS_FILE}
              echo ${NODE_IPS[@]} | tee -a ${RESULTS_FILE}
              break
      fi
      if ((${#NODE_IPS[@]} == 0 ))
      then
              break
      fi
      # Check that nodes are reachable once per 1 seconds
      sleep 1
done
echo "Provisioning finished at "`date` >> ${RESULTS_FILE}

end_time=`date +%s.%N`
elapsed_time=$(echo "$end_time - $start_time" | bc -l)
echo "Total elapsed time for provisioning: $elapsed_time seconds" >> ${RESULTS_FILE}

# Stop dstat command
kill `ps aux | grep dstat | grep python | awk '{print $2}'`

# Delete excess values and convert to needed metrics. So, we'll get the
# following csv format:
# time,cpu_usage,ram_usage,net_recv,net_send,net_all,dsk_io_read,dsk_io_writ,dsk_all
awk -F "," 'BEGIN {getline;getline;getline;getline;getline;getline;getline;
                   print "time,cpu_usage,ram_usage,net_recv,net_send,net_all,dsk_io_read,dsk_io_writ,dsk_all"}
            {print $1","100-$4","$8/1048576","$12/131072","$13/131072","($12+$13)/131072","$14","$15","$14+$15}' \
$DSTAT_OUTPUT_FILE >> ${RESULTS_FILE}
