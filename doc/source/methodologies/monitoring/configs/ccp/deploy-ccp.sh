#!/bin/bash
set -ex
if [ -z "$1" ]; then
   echo "Please set number of env as argument"
   exit 1
fi

DEPLOY_TIMEOUT=1200
export SSH_USER="root"
export SSH_PASS="r00tme"
cd $(dirname $(realpath $0))

NODE1="172.20.8.6${1}"

SSH_OPTS="-q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
SSH_CMD="sshpass -p ${SSH_PASS} ssh ${SSH_OPTS} ${SSH_USER}@${NODE1}"
SCP_CMD="sshpass -p ${SSH_PASS} scp ${SSH_OPTS}"

if [ ! -d ./env-${1} ]; then
  echo "Yaml files for env-${1} is not found"
  echo "Please, create and commit deployment/ccp/rackspace/env-${1}/configs with correct yaml files"
  echo "Main file should be deployment/ccp/rackspace/env-${1}/configs/ccp.yaml"
  exit 1
fi


$SCP_CMD ./env-${1}/configs/ccp.yaml ${SSH_USER}@${NODE1}:/root/.ccp.yaml
for i in $(ls -1 ./env-${1}/configs/ | grep -v ccp.yaml ); do
  $SCP_CMD ./env-${1}/configs/${i} ${SSH_USER}@${NODE1}:/root/
done

$SSH_CMD "rm -rf /root/fuel-ccp; cd /root; git clone https://git.openstack.org/openstack/fuel-ccp"
$SSH_CMD "apt-get -y install python-pip"
$SSH_CMD "/usr/bin/pip install --upgrade pip"
$SSH_CMD "/usr/bin/pip install /root/fuel-ccp/"

CCP_STATUS=$($SSH_CMD "/usr/local/bin/ccp status")
if [ -n "$CCP_STATUS" ]; then
  echo "Active deployment was found"
  echo "$CCP_STATUS"
  echo "Please execute 'ccp cleanup' and 'rm -rf /var/lib/mysql/*' on the ${NODE1} manually"
  exit 1
fi

$SSH_CMD "echo '172.20.8.6${1} cloudformation.ccp.external console.ccp.external identity.ccp.external object-store.ccp.external compute.ccp.external orchestration.ccp.external network.ccp.external image.ccp.external volume.ccp.external horizon.ccp.external' >> /etc/hosts"
# $SSH_CMD kubectl delete configmaps traefik-conf -n kube-system
# $SSH_CMD kubectl delete service traefik -n kube-system
# $SSH_CMD kubectl delete secret traefik-cert -n kube-system
# $SSH_CMD kubectl delete deployment traefik -n kube-system
$SSH_CMD "/root/fuel-ccp/tools/ingress/deploy-ingress-controller.sh -i 172.20.8.6${1}" || echo "Already configured"
$SSH_CMD "echo 172.20.8.6${1} \$(ccp domains list -f value) >> /etc/hosts"
$SSH_CMD "openssl s_client -status -connect identity.ccp.external:8443 < /dev/null 2>&1 | awk 'BEGIN {pr=0;} /-----BEGIN CERTIFICATE-----/ {pr=1;} {if (pr) print;} /-----END CERTIFICATE-----/ {exit;}' >> /usr/local/lib/python2.7/dist-packages/requests/cacert.pem"
$SSH_CMD "openssl s_client -status -connect identity.ccp.external:8443 < /dev/null 2>&1 | awk 'BEGIN {pr=0;} /-----BEGIN CERTIFICATE-----/ {pr=1;} {if (pr) print;} /-----END CERTIFICATE-----/ {exit;}' > /usr/share/ca-certificates/ingress.crt"
$SSH_CMD "cp /usr/share/ca-certificates/ingress.crt /usr/local/share/ca-certificates/"
$SSH_CMD "update-ca-certificates"
if [ $($SSH_CMD "curl -s 'https://identity.ccp.external:8443/' > /dev/null; echo \$?") != 0 ]
then
  echo "keystone is unreachable check https://identity.ccp.external:8443"
  exit 1
fi

#$SSH_CMD "/root/fuel-ccp/tools/registry/deploy-registry.sh" &&
$SSH_CMD "/usr/local/bin/ccp fetch"
$SSH_CMD "/usr/local/bin/ccp build"
$SSH_CMD "/usr/local/bin/ccp deploy"

DEPLOY_TIME=0
while [ "$($SSH_CMD '/usr/local/bin/ccp status -s -f value' 2>/dev/null)" != "ok" ]
do
  sleep 5
  DEPLOY_TIME=$((${DEPLOY_TIME} + 5))
  if [ $DEPLOY_TIME -ge $DEPLOY_TIMEOUT ]; then
      echo "Deployment timeout"
      exit 1
  fi
done

$SSH_CMD "/usr/local/bin/ccp status"
