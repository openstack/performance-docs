#!/bin/bash
CLUSTER=${1}
TMP_YAML=$(mktemp -u)

export ANSIBLE_HOST_KEY_CHECKING=False
export SSH_USER="root"
export SSH_PASS="r00tme"
cd $(dirname $(realpath $0))

ENV=${1}
if [ -z "${ENV}" ]; then
   echo "Please provide env number $(basename $0) [1|2|3|4|5|6]"
   exit 1
fi
PROMETHEUS_HOST="172.20.9.115"
KUBE_MAIN_NODE="172.20.8.6${ENV}"
CLUSTER_TAG="env-${ENV}"

ETCD=""

SSH_OPTS="-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"


TARGETS=$(sshpass -p ${SSH_PASS} ssh ${SSH_OPTS} ${SSH_USER}@${KUBE_MAIN_NODE} curl -ks https://127.0.0.1:2379/v2/members | python -m json.tool | grep 2379)

if [ -z "$TARGETS" ]; then
  echo "No etcd found"
  exit 1
fi

for i in ${TARGETS}; do
  TEMP_TARGET=${i#\"https://}
  ETCD="$ETCD ${TEMP_TARGET%\"}"
done

echo "- targets:" > ${TMP_YAML}
for i in ${ETCD}; do
  echo "  - $i" >> ${TMP_YAML}
done
echo "  labels:" >> ${TMP_YAML}
echo "    env: ${CLUSTER_TAG}" >> ${TMP_YAML}

echo "Targets file is ready"
cat ${TMP_YAML}
sshpass -p ${SSH_PASS} scp ${SSH_OPTS} ${TMP_YAML} root@${PROMETHEUS_HOST}:/var/lib/prometheus/etcd-env-${1}.yml
rm ${TMP_YAML}
