#!/usr/bin/env bash
#==========================================================================
#  Unset quotas for main Nova and Neutron resources for a tenant
#  with name $OS_TENANT_NAME.
#  Neutron quotas: floatingip, network, port, router, security-group,
#  security-group-rule subnet.
#  Nova quotas: cores, instances, ram, server-groups, server-group-members.
#
#  Usage: unset_quotas.sh
#==========================================================================

set -e

NEUTRON_QUOTAS=(floatingip network port router security-group security-group-rule subnet)
NOVA_QUOTAS=(cores instances ram server-groups server-group-members)

OS_TENANT_ID=$(openstack project show $OS_TENANT_NAME -c id -f value)

echo "Unsetting Neutron quotas: ${NEUTRON_QUOTAS[@]}"
for net_quota in ${NEUTRON_QUOTAS[@]}
do
    neutron quota-update --"$net_quota" -1 $OS_TENANT_ID
done

echo "Unsetting Nova quotas: ${NOVA_QUOTAS[@]}"
for nova_quota in ${NOVA_QUOTAS[@]}
do
    nova quota-update --"$nova_quota" -1 $OS_TENANT_ID
done

echo "Successfully unset all quotas"
openstack quota show $OS_TENANT_ID
