#!/bin/bash

DNS_DOMAIN="cobbler-test.local"
PROFILE="ubuntu14-x86_64"
ENV_NAME="cobbler-test"
INTERFACE_1="p1p1"
IP_RANGE_1="10.50.11.1 10.50.20.254"
NETMASK_1="255.255.0.0"
GATEWAY_1="10.50.0.10"
DNS1="10.50.0.10"

SYSTEM_IPMI_USER="root"
SYSTEM_IPMI_PASS="calvincalvin"

SYSTEMS_LIST_FILE="systems.list"
SYSTEMS_COUNT=`wc -l ${SYSTEMS_LIST_FILE} | awk '{print $1}'`

for EXISTED_SYSTEM in `cobbler system list`
do
  EXISTED_IP_ADDRESSES=(`cobbler system dumpvars --name=${EXISTED_SYSTEM} | grep ^ip_address | awk -F": " '{print $2}'`)
done

IP_ADDRESSES=(`prips ${IP_RANGE_1}`)

for IP in ${EXISTED_IP_ADDRESSES[@]}
do
  for ARRAY_ELEMENT_NUM in $(seq 0 ${#IP_ADDRESSES[@]})
  do
    if [ "${IP_ADDRESSES[${ARRAY_ELEMENT_NUM}]}" == "${IP}" ]
    then
       unset IP_ADDRESSES[${ARRAY_ELEMENT_NUM}] && IP_ADDRESSES=(${IP_ADDRESSES[@]})
    fi
  done
done


for SYSTEM_NUM in $(seq 1 ${SYSTEMS_COUNT})
do
  SYSTEM_NAME=`awk -F"," '{print $1}' ${SYSTEMS_LIST_FILE} | head -${SYSTEM_NUM} | tail -1`
  SYSTEM_MAC=`awk -F"," '{print $3}' ${SYSTEMS_LIST_FILE} | head -${SYSTEM_NUM} | tail -1`
  SYSTEM_IPMI_ADDRESS=`awk -F"," '{print $2}' ${SYSTEMS_LIST_FILE} | head -${SYSTEM_NUM} | tail -1`
  NODE_IP_1=${IP_ADDRESSES[${SYSTEM_NUM}]}
  cobbler system add --name=${SYSTEM_NAME} \
                     --hostname=${SYSTEM_NAME} \
                     --dns-name=${SYSTEM_NAME}.${DNS_DOMAIN} \
                     --name-servers-search=${DNS_DOMAIN} \
                     --profile=${PROFILE} \
                     --comment=${ENV_NAME}\
                     --netboot-enabled=yes \
                     --interface=${INTERFACE_1} \
                     --mac-address=${SYSTEM_MAC} \
                     --ip-address=${NODE_IP_1} \
                     --netmask=${NETMASK_1} \
                     --virt-bridge=pxe \
                     --virt-file-size=100 \
                     --power-type=ipmilan \
                     --power-address=${SYSTEM_IPMI_ADDRESS} \
                     --power-user=${SYSTEM_IPMI_USER} \
                     --power-pass=${SYSTEM_IPMI_PASS} \
                     --power-id=lanplus \
                     --kickstart=/var/lib/cobbler/kickstarts/sample.seed
done
