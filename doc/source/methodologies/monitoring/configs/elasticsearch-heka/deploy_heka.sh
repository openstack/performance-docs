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
# elastic for k8s at rackspace as default
ELASTICSEARCH_NODE=${ELASTICSEARCH_NODE:-172.20.9.3}
# heka 0.10.0 as default
HEKA_PACKAGE_URL=${HEKA_PACKAGE_URL:-https://github.com/mozilla-services/heka/releases/download/v0.10.0/heka_0.10.0_amd64.deb}
KUBE_MAIN_NODE="172.20.8.6${ENV}"
SSH_OPTS="-q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

echo "Get clusters nodes ..."
NODES_TMP=$(sshpass -p ${SSH_PASS} ssh ${SSH_OPTS} ${SSH_USER}@${KUBE_MAIN_NODE} 'kubectl get nodes -o jsonpath='"'"'{.items[*].status.addresses[?(@.type=="InternalIP")].address}'"'"'')
ALL_IP_ON_KUBER_NODE=$(sshpass -p ${SSH_PASS} ssh ${SSH_OPTS} ${SSH_USER}@${KUBE_MAIN_NODE} ip addr | grep 172.20 | awk '{print $2}' | awk -F'/' '{print $1}')
GREP_STRING_TMP=""
for i in $ALL_IP_ON_KUBER_NODE; do
   GREP_STRING_TMP="${GREP_STRING_TMP}${i}|"
done
GREP_STRING=${GREP_STRING_TMP:0:-1}
SSH_AUTH="ansible_ssh_user=${SSH_USER} ansible_ssh_pass=${SSH_PASS}"
echo "[main-kuber]" > cluster-hosts
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

# Calculate parallel ansible execution
NODES_IPS=( $NODES )
if [[ "${#NODES_IPS[@]}" -lt 50 ]] && [[ "${#NODES_IPS[@]}" -gt 5 ]]; then
    ANSIBLE_FORKS="${#NODES_IPS[@]}"
elif [[ "${#NODES_IPS[@]}" -ge 50 ]]; then
    ANSIBLE_FORKS=50
else
    ANSIBLE_FORKS=10
fi

echo "Starting ansible ..."
ansible-playbook -v --ssh-extra-args "-o\ StrictHostKeyChecking=no" -f ${ANSIBLE_FORKS} -i ./cluster-hosts -e env_num=${ENV} -e elasticsearch_node="${ELASTICSEARCH_NODE}" -e heka_package_url=${HEKA_PACKAGE_URL} ./deploy-heka.yaml --diff

