#!/bin/bash
set -e
export ANSIBLE_HOST_KEY_CHECKING=False
export SSH_USER="root"
export SSH_PASS="r00tme"
cd $(dirname $(realpath $0))

ENV=${1}
if [ -z "${ENV}" ]; then
   echo "Please provide env number $(basename $0) [1|2|3|4|5|6]"
   exit 1
fi
PROMETHEUS_NODE="172.20.124.25"
KUBE_MAIN_NODE="172.20.8.6${ENV}"
CLUSTER_TAG="env-${ENV}"

# Secret option
ANSIBLE_TAG=$2

SSH_OPTS="-q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

echo "Get clusters nodes"

NODES_TMP=$(sshpass -p ${SSH_PASS} ssh ${SSH_OPTS} ${SSH_USER}@${KUBE_MAIN_NODE} 'kubectl get nodes -o jsonpath='"'"'{.items[*].status.addresses[?(@.type=="InternalIP")].address}'"'"'')
ALL_IP_ON_KUBER_NODE=$(sshpass -p ${SSH_PASS} ssh ${SSH_OPTS} ${SSH_USER}@${KUBE_MAIN_NODE} ip addr | grep 172.20 | awk '{print $2}' | awk -F'/' '{print $1}')
GREP_STRING_TMP=""
for i in $ALL_IP_ON_KUBER_NODE; do
   GREP_STRING_TMP="${GREP_STRING_TMP}${i}|"
done
GREP_STRING=${GREP_STRING_TMP:0:-1}
SSH_AUTH="ansible_ssh_user=${SSH_USER} ansible_ssh_pass=${SSH_PASS}"
echo "[main]" > cluster-hosts
echo "${PROMETHEUS_NODE} ${SSH_AUTH}" >> cluster-hosts
echo "[main-kuber]" >> cluster-hosts
echo "${KUBE_MAIN_NODE} ${SSH_AUTH}" >> cluster-hosts
echo "[cluster-nodes]" >> cluster-hosts
set +e
# Remove IP of kuber node
for i in ${NODES_TMP} ; do
    TMP_VAR=$(echo $i | grep -vE "(${GREP_STRING})")
    NODES="${NODES} ${TMP_VAR}"
done
set -e
for i in ${NODES} ; do
    if [ "$i" != "${KUBE_MAIN_NODE}" ]; then
        echo "${i} ${SSH_AUTH}" >>  cluster-hosts
    fi
done
echo "[all-cluster-nodes:children]" >> cluster-hosts
echo "main-kuber" >> cluster-hosts
echo "cluster-nodes" >> cluster-hosts
LINES=$(wc -l cluster-hosts | awk '{print $1}')
NUM_NODES=$(($LINES - 7))
if [ ${NUM_NODES} -le 0 ]; then
   echo "Something wrong, $NUM_NODES nodes found"
   exit 1
else
   echo "${NUM_NODES} nodes found"
fi

if [ -z "${ANSIBLE_TAG}" ]; then
   ansible-playbook -f 40 -i ./cluster-hosts -e cluster_tag=${CLUSTER_TAG} ./deploy-telegraf.yaml
else
   ansible-playbook -f 40 -i ./cluster-hosts -e cluster_tag=${CLUSTER_TAG} -t ${ANSIBLE_TAG} ./deploy-telegraf.yaml
fi
