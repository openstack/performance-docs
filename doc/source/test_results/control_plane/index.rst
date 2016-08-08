
.. _openstack_control_plane_performance_report:

******************************************
OpenStack control plane performance report
******************************************

:Abstract:

  This document includes OpenStack control plane performance test results.
  All tests have been performed regarding
  :ref:`openstack_control_plane_performance_test_plan`


Environment description
=======================

Environment contains 4 types of servers:

- rally node
- controller node
- compute-osd node
- compute node

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

Network configuration of each server
------------------------------------

All servers have same network configuration:

.. image:: configs/Network_Scheme.png
   :alt: Network Scheme of the environment

Here is the part of switch configuration for each switch port which connected to
ens1f0 interface of a server:

.. code:: bash

   switchport mode trunk
   switchport trunk native vlan 600
   switchport trunk allowed vlan 600-602,630-649
   spanning-tree port type edge trunk
   spanning-tree bpduguard enable
   no snmp trap link-status

Software configuration on servers with controller, compute and compute-osd roles
--------------------------------------------------------------------------------

.. table:: Services on servers by role

   +------------+----------------------------+
   |Role        |Service name                |
   +============+============================+
   |controller  || horizon                   |
   |            || keystone                  |
   |            || nova-api                  |
   |            || nava-scheduler            |
   |            || nova-cert                 |
   |            || nova-conductor            |
   |            || nova-consoleauth          |
   |            || nova-consoleproxy         |
   |            || cinder-api                |
   |            || cinder-backup             |
   |            || cinder-scheduler          |
   |            || cinder-volume             |
   |            || glance-api                |
   |            || glance-glare              |
   |            || glance-registry           |
   |            || neutron-dhcp-agent        |
   |            || neutron-l3-agent          |
   |            || neutron-metadata-agent    |
   |            || neutron-openvswitch-agent |
   |            || neutron-server            |
   |            || heat-api                  |
   |            || heat-api-cfn              |
   |            || heat-api-cloudwatch       |
   |            || ceph-mon                  |
   |            || rados-gw                  |
   |            || memcached                 |
   |            || rabbitmq_server           |
   |            || mysqld                    |
   |            || galera                    |
   |            || corosync                  |
   |            || pacemaker                 |
   |            || haproxy                   |
   +------------+----------------------------+
   |compute     || nova-compute              |
   |            || neutron-l3-agent          |
   |            || neutron-metadata-agent    |
   |            || neutron-openvswitch-agent |
   +------------+----------------------------+
   |compute-osd || nova-compute              |
   |            || neutron-l3-agent          |
   |            || neutron-metadata-agent    |
   |            || neutron-openvswitch-agent |
   |            || ceph-osd                  |
   +------------+----------------------------+

.. table:: Software version on servers with controller, compute and compute-osd roles

   +------------+-------------------+
   |Software    |Version            |
   +============+===================+
   |OpenStack   |Mitaka             |
   +------------+-------------------+
   |Ceph        |Hammer             |
   +------------+-------------------+
   |Ubuntu      |Ubuntu 14.04.3 LTS |
   +------------+-------------------+

You can find outputs of some commands and /etc folder in the following archives:

| :download:`controller-1.tar.gz <configs/controller-1.tar.gz>`
| :download:`controller-2.tar.gz <configs/controller-2.tar.gz>`
| :download:`controller-3.tar.gz <configs/controller-3.tar.gz>`
| :download:`compute-1.tar.gz <configs/compute-1.tar.gz>`
| :download:`compute-osd-1.tar.gz <configs/compute-osd-1.tar.gz>`

Software configuration on servers with rally role
-------------------------------------------------

On this server should be installed Rally. How to do it you can find in
`Rally installation documentation`_

.. table:: Software version on server with rally role

   +------------+-------------------+
   |Software    |Version            |
   +============+===================+
   |Rally       |0.4.0              |
   +------------+-------------------+
   |Ubuntu      |Ubuntu 14.04.3 LTS |
   +------------+-------------------+

Testing process
===============

.. table:: Some test parameters

   +--------------------------------+--------+
   |Name                            |Value   |
   +================================+========+
   |Volume size to create in Cinder |1GB     |
   +--------------------------------+--------+
   |Flavor to create VM from        |m1.tiny |
   +--------------------------------+--------+
   |Image name to create VM from    |cirros  |
   +--------------------------------+--------+

1. Create work directory on server with Rally role. In future we will call that directory as WORK_DIR
2. Create directory "plugins" in WORK_DIR and copy to that directory
   :download:`nova_performance.py <../../test_plans/control_plane/plugins/nova_performance.py>` plugin.
3. Create directory "scenarios" in WORK_DIR and copy to that directory
   :download:`boot_attach_live_migrate_and_delete_server_with_secgroups.json
   <rally_scenarios/boot_attach_live_migrate_and_delete_server_with_secgroups.json>`,
   :download:`create-and-delete-image.json <rally_scenarios/create-and-delete-image.json>`
   and :download:`keystone.json <rally_scenarios/keystone.json>` scenarios.
4. Create deployment.json file in WORK_DIR and fill it with OpenStack environment info.
   It should looks like this:

   .. literalinclude:: configs/deployment.json
      :language: bash

5. Create job-params.yaml file in WORK_DIR and fill it with scenarios info.
   It should looks like this:

   .. literalinclude:: configs/job-params.yaml
      :language: bash

6. Perform tests:

   .. literalinclude:: configs/run_test_script.sh
      :language: bash

As a result of this part we got the following HTML file:

:download:`rally_report.html <configs/rally_report.html>`

Test results
============

All values in tables below are in seconds.

Cinder
------

+---------------+---------+----------+----------+---------+---------+
| Operation     |   Mean  |   90%ile |   50%ile |   Max   |   Min   |
|               |   (sec) |   (sec)  |   (sec)  |   (sec) |   (sec) |
+===============+=========+==========+==========+=========+=========+
| create_volume | 2.619   | 2.754    | 2.593    | 2.988   | 2.453   |
+---------------+---------+----------+----------+---------+---------+
| delete_volume | 2.339   | 2.449    | 2.323    | 2.666   | 2.200   |
+---------------+---------+----------+----------+---------+---------+

Glance
------

+--------------+----------+----------+----------+----------+-----------+
| Operation    |    Mean  |   90%ile |   50%ile |   Max    |   Min     |
|              |    (sec) |   (sec)  |   (sec)  |   (sec)  |   (sec)   |
+==============+==========+==========+==========+==========+===========+
| create_image | 44.204   | 56.243   | 43.835   | 74.826   | 22.382    |
+--------------+----------+----------+----------+----------+-----------+
| delete_image | 1.579    | 2.049    | 1.540    | 3.846    | 0.718     |
+--------------+----------+----------+----------+----------+-----------+

Keystone
--------

+--------------+-----------+----------+-----------+----------+-----------+
| Operation    |     Mean  |   90%ile |    50%ile |   Max    |   Min     |
|              |     (sec) |   (sec)  |    (sec)  |   (sec)  |   (sec)   |
+==============+===========+==========+===========+==========+===========+
| authenticate | 0.099     | 0.135    | 0.093     | 0.718    | 0.054     |
+--------------+-----------+----------+-----------+----------+-----------+

Neutron
-------

+--------------------------+----------+----------+----------+----------+----------+
| Operation                |   Mean   |   90%ile |   50%ile |   Max    |   Min    |
|                          |   (sec)  |   (sec)  |   (sec)  |   (sec)  |   (sec)  |
+==========================+==========+==========+==========+==========+==========+
| create_20_rules          | 4.535    | 4.883    | 4.515    | 5.577    | 3.873    |
+--------------------------+----------+----------+----------+----------+----------+
| create_2_security_groups | 0.412    | 0.477    | 0.401    | 0.670    | 0.292    |
+--------------------------+----------+----------+----------+----------+----------+
| delete_2_security_groups | 0.380    | 0.480    | 0.371    | 0.771    | 0.234    |
+--------------------------+----------+----------+----------+----------+----------+

Nova
----

+----------------------+-----------+-----------+-----------+-----------+-----------+
| Operation            |     Mean  |    90%ile |    50%ile |   Max     |   Min     |
|                      |     (sec) |    (sec)  |    (sec)  |   (sec)   |   (sec)   |
+======================+===========+===========+===========+===========+===========+
| attach_volume        | 2.806     | 2.985     | 2.781     | 3.294     | 2.563     |
+----------------------+-----------+-----------+-----------+-----------+-----------+
| boot_server          | 11.989    | 12.937    | 11.953    | 14.265    | 9.482     |
+----------------------+-----------+-----------+-----------+-----------+-----------+
| delete_server        | 2.531     | 2.670     | 2.467     | 4.817     | 2.348     |
+----------------------+-----------+-----------+-----------+-----------+-----------+
| detach_volume        | 2.701     | 2.861     | 2.684     | 3.201     | 2.464     |
+----------------------+-----------+-----------+-----------+-----------+-----------+
| find_host_to_migrate | 0.554     | 0.682     | 0.520     | 0.954     | 0.419     |
+----------------------+-----------+-----------+-----------+-----------+-----------+
| live_migrate         | 15.351    | 15.715    | 15.221    | 28.692    | 12.623    |
+----------------------+-----------+-----------+-----------+-----------+-----------+

.. references:

.. _Rally installation documentation: https://rally.readthedocs.io/en/latest/install.html