#!/usr/bin/env bash

: ${DB_CONNECTION_STRING:?"You need to specify DB_CONNECTION_STRING parameter"}
: ${ENV_NAME:?"You need to specify ENV_NAME parameter"}

: ${MANAGEMENT_INTERFACE:="p1p1.602"}
: ${COBBLER_ADDRESS:="172.20.8.34"}
: ${CUSTOM_YAML}
: ${KARGO_REPO}
: ${KARGO_COMMIT}
: ${FUEL_CCP_COMMIT}
: ${ADMIN_USER}
: ${ADMIN_PASSWORD}
: ${ADMIN_NODE_CLEANUP}
DEPLOY_METHOD="kargo"
WORKSPACE="~/kargo_workspace_${ENV_NAME}"
SSH_OPTIONS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"

get_env_nodes ()
{
  ENV_NODES_NAMES=$(echo $(psql ${DB_CONNECTION_STRING} -c "select name from servers where environment_id in (select id from environments where name='${ENV_NAME}')" -P format=unaligned -t))
  if [ -z "${ENV_NODES_NAMES}" ]
  then
    echo "No nodes in environment with name ${ENV_NAME}"
    exit 1
  fi
}

get_env_nodes_ips ()
{
  ENV_NODES_IPS=$(echo $(ssh ${SSH_OPTIONS} root@${COBBLER_ADDRESS} bash -ex << EOF
  for COBBLER_SYSTEM_NAME in ${ENV_NODES_NAMES}
  do
    NODE_IP=\$(cobbler system dumpvars --name=\${COBBLER_SYSTEM_NAME} | grep ^ip_address_${MANAGEMENT_INTERFACE} | awk '{print \$3}')
    NODE_IPS+=\${NODE_IP}" "
  done
  echo \${NODE_IPS}
EOF
  ))
}

main ()
{
  get_env_nodes
  get_env_nodes_ips
  export ADMIN_IP=$(echo ${ENV_NODES_IPS} | awk '{print $1}')
  export SLAVE_IPS=$(echo ${ENV_NODES_IPS})

#  for SLAVE_IP in ${SLAVE_IPS}
#  do
#    ssh ${SSH_OPTIONS} root@${SLAVE_IP} bash -ex << EOF
#echo "deb https://apt.dockerproject.org/repo ubuntu-\$(grep DISTRIB_CODENAME /etc/lsb-release | awk -F"=" '{print \$2}') main" >> /etc/apt/sources.list
#apt-get update && apt-get install -y --allow-unauthenticated -o Dpkg::Options::="--force-confdef" docker-engine
#EOF
#  done

  if [ -d "$WORKSPACE" ] ; then
      rm -rf $WORKSPACE
  fi
  mkdir -p $WORKSPACE
  cd $WORKSPACE

  if [ -d './fuel-ccp-installer' ] ; then
      rm -rf ./fuel-ccp-installer
  fi
  git clone https://review.openstack.org/openstack/fuel-ccp-installer
  cd ./fuel-ccp-installer

  if [ "$FUEL_CCP_COMMIT" ]; then
      git fetch git://git.openstack.org/openstack/fuel-ccp-installer $FUEL_CCP_COMMIT && git checkout FETCH_HEAD
  fi

  echo "Running on $NODE_NAME: $ENV_NAME"

  bash -xe "./utils/jenkins/run_k8s_deploy_test.sh"
}
main