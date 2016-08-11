.. _controlplane_density:

=======================================
OpenStack control plane density testing
=======================================

:status: **ready**
:version: 1.0

:Abstract:

  This document describes a test plan for measuring OpenStack control plane
  performance under with large number of items in terms of ability to handle
  specific amount of objects like VMs, networks, subnets etc.


Test Plan
=========

Test Environment
----------------

This section describes the setup for OpenStack testing.
In these tests basic multi-node setup with OpenStack services comprises 6
physical nodes:
  * Three nodes for a compute node. This node simulates activity which is
    typical for OpenStack compute components.
  * Three nodes for a controller nodes. These node simulate activity which
    is typical for OpenStack control plane services, including running three
    MySQL instances managed by Galera cluster and memcached cluster for
    Keystone caching.

Preparation
^^^^^^^^^^^

**Single node installation**

For single node installation the one can use DevStack_ tool that is targeted
at developers and CI systems to use upstream code. It makes many choices that
are not appropriate for production systems, but for the all-in-one purposes
this can fit ok.


**Multi node installation**

Multi node environment installation depends much on the chosen set of OpenStack
deployment tools.


Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers,
network parameters, operation system and OpenStack deployment characteristics.

.. table:: Amount of servers each role

   +------------+--------------+
   |Role        |Servers count |
   +============+==============+
   |rally       |1             |
   +------------+--------------+
   |controller  |3             |
   +------------+--------------+
   |compute     |176           |
   +------------+--------------+
   |compute-osd |20            |
   +------------+--------------+
   |osd         |0             |
   +------------+--------------+

Hardware configuration of each server
-------------------------------------
All servers have same configuration describing in table below

.. table:: Description of servers hardware

   +-------+----------------+-------------------------------+
   |server |vendor,model    |HP,DL380 Gen9                  |
   +-------+----------------+-------------------------------+
   |CPU    |vendor,model    |Intel,E5-2680 v3               |
   |       +----------------+-------------------------------+
   |       |processor_count |2                              |
   |       +----------------+-------------------------------+
   |       |core_count      |12                             |
   |       +----------------+-------------------------------+
   |       |frequency_MHz   |2500                           |
   +-------+----------------+-------------------------------+
   |RAM    |vendor,model    |HP,752369-081                  |
   |       +----------------+-------------------------------+
   |       |amount_MB       |262144                         |
   +-------+----------------+-------------------------------+
   |NETWORK|interface_name  |p1p1                           |
   |       +----------------+-------------------------------+
   |       |vendor,model    |Intel,X710 Dual Port           |
   |       +----------------+-------------------------------+
   |       |bandwidth       |10G                            |
   +-------+----------------+-------------------------------+
   |STORAGE|dev_name        |/dev/sda                       |
   |       +----------------+-------------------------------+
   |       |vendor,model    | | raid10 - HP P840            |
   |       |                | | 12 disks EH0600JEDHE        |
   |       +----------------+-------------------------------+
   |       |SSD/HDD         |HDD                            |
   |       +----------------+-------------------------------+
   |       |size            | 3,6TB                         |
   +-------+----------------+-------------------------------+

Test Case 1: perform baseline Rally scenarios
---------------------------------------------

Description
^^^^^^^^^^^

1. Create work directory on server. In future we will call it as WORK_DIR
2. Create directory "plugins" in WORK_DIR and copy to the directory
   :download:`nova_density.py <configs/nova_density.py>` plugin.
3. Create directory "scenarios" in WORK_DIR and copy to the directory
   :download:`boot_attach_and_list_with_secgroups.json <configs/boot_attach_and_list_with_secgroups.json>`
   scenario.
4. Create `deployment.json` file in WORK_DIR and fill it with OpenStack
   environment info. Example of how it may look like  is presented below:

   .. code:: json

      {
        "admin": {
          "password": "password",
          "tenant_name": "tenant",
          "username": "user"
        },
        "auth_url": "http://1.2.3.4:5000/v2.0",
        "region_name": "RegionOne",
        "type": "ExistingCloud",
        "endpoint_type": "internal",
        "admin_port": 35357,
        "https_insecure": true
      }

5. Create `job-params.yaml` file in WORK_DIR and fill it with scenarios info.
   Example of how it may look like  is presented below:

   .. code:: yaml

      ---
          concurrency: 5
          compute: 196
          start_cidr: "1.0.0.0/16"
          current_path: "/home/rally/rally-scenarios/heat/"
          floating_ip_amount: 800
          floating_net: "admin_floating_net"
          vlan_amount: 1025
          gre_enabled: false
          http_server_with_glance_images: "1.2.3.4"

6. Perform tests:

   .. code:: bash

      ${WORK_DIR:?}
      DEPLOYMENT_NAME="$(uuidgen)"
      DEPLOYMENT_CONFIG="${WORK_DIR}/deployment.json"
      PLUGIN_PATH="${WORK_DIR}/plugins/nova_scale.py"
      JOB_PARAMS_CONFIG="${WORK_DIR}/job-params.yaml"
      rally deployment create --filename $(DEPLOYMENT_CONFIG) --name $(DEPLOYMENT_NAME)
      SCENARIOS="boot_attach_and_list_with_secgroups.json"
      for scenario in SCENARIOS; do
        rally --plugin-paths ${PLUGINS_PATH} task start --tag ${scenario} --task-args-file ${JOB_PARAMS_CONFIG} ${WORK_DR}/scenarios/${scenario}
      done
      task_list="$(rally task list --uuids-only)"
      rally task report --tasks ${task_list} --out=${WORK_DIR}/rally_report.html

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Foe each component under test define atomic actions made in terms of this test
case. Define what time does it take to perform this specific action (minimum,
maximum, mean and percentiles across all attempts to perform this action).

For example, in case of Cinder testing final measurement for volume creation
may look like:

+---------------+----------------+--------------------+-------------------+-------------+-------------+
| Operation     |      Mean      |        90%ile      |       50%ile      |     Max     |     Min     |
+===============+================+====================+===================+=============+=============+
| create_volume | <mean_numbers> |   <90%ile_numbers> |  <50%ile_numbers> | <max_value> | <min_value> |
+---------------+----------------+--------------------+-------------------+-------------+-------------+
