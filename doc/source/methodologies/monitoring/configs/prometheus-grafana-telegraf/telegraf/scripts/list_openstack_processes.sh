#!/bin/bash
export LANG=C
PS_ALL=$(ps --no-headers -A -o command | grep -vE '(sh|bash)')
M_NAME=system_openstack_list

MARIADB=$(echo "${PS_ALL}" | grep 'mariadb' | wc -l)
RABBITMQ=$(echo "${PS_ALL}" | grep 'rabbitmq' | wc -l)
KEYSTONE=$(echo "${PS_ALL}" | grep 'keystone' | wc -l)
GLANCE=$(echo "${PS_ALL}" | grep -E '(glance-api|glance-registry)' | wc -l)
CINDER=$(echo "${PS_ALL}" | grep 'cinder' | wc -l)
NOVA=$(echo "${PS_ALL}" | grep -E '(nova-api|nova-conductor|nova-consoleauth|nova-scheduler)' | wc -l)
NEUTRON=$(echo "${PS_ALL}" | grep -E '(neutron-server|neutron-metadata-agent|neutron-dhcp-agent|neutron-l3-agent|neutron-openvswitch-agent)' | wc -l)
OPENVSWITCH=$(echo "${PS_ALL}" | grep -E '(ovsdb-server|ovs-vswitchd|ovsdb-client)' | wc -l)

echo "${M_NAME} mariadb=${MARIADB},rabbitmq=${RABBITMQ},keystone=${KEYSTONE},glance=${GLANCE},cinder=${CINDER},nova=${NOVA},neutron=${NEUTRON},openvswitch=${OPENVSWITCH}"