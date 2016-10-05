
.. _openstack_control_plane_performance_report_1000_nodes:

*********************************************************
OpenStack control plane performance report for 1000 nodes
*********************************************************

:Abstract:

  This document includes OpenStack control plane performance test results for
  1000 compute nodes cluster.
  All tests have been performed regarding
  :ref:`openstack_control_plane_performance_test_plan`


Environment description
=======================

Environment contains 4 types of servers:

- rally node
- controller node
- osd node
- hypervisor
- compute node

.. table:: Amount of servers each role

   +------------+--------------+------------+
   |Role        |Servers count |Server Type |
   +============+==============+============+
   |rally       |1             |bare-metal  |
   +------------+--------------+------------+
   |controller  |3             |bare-metal  |
   +------------+--------------+------------+
   |osd         |20            |bare-metal  |
   +------------+--------------+------------+
   |compute     |1000          |virtual     |
   +------------+--------------+------------+

Hardware configuration of each server
-------------------------------------

All bare-metal servers have the same configuration describing in table below

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

All virtual servers has the same configuration. QEMU-KVM used as hypervisor.
For datailed info about VM configuration look into sample
:download:`domain.xml <configs/domain.xml>`.

Network configuration of each server
------------------------------------

Lab network configuration you can find in scheme below:

.. image:: configs/Network_Scheme.png
   :alt: Network Scheme of the environment

Here is the part of switch configuration for each switch port which connected to
p1p1 interface of a bare-metal server:

.. code:: bash

   switchport mode trunk
   switchport trunk native vlan 600
   switchport trunk allowed vlan 600-602,630-649
   spanning-tree port type edge trunk
   spanning-tree bpduguard enable
   no snmp trap link-status

Software configuration on servers with controller, osd and compute roles
------------------------------------------------------------------------

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
   |osd         || ceph-osd                  |
   +------------+----------------------------+
   |compute     || nova-compute              |
   |            || neutron-l3-agent          |
   |            || neutron-metadata-agent    |
   |            || neutron-openvswitch-agent |
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
| :download:`osd-1.tar.gz <configs/osd-1.tar.gz>`

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
| Operation     |    Mean |   90%ile |   50%ile |     Max |     Min |
+===============+=========+==========+==========+=========+=========+
| create_volume | 2.59589 |  2.72586 |  2.57214 | 3.05174 | 2.40753 |
+---------------+---------+----------+----------+---------+---------+
| delete_volume | 2.31282 |  2.42514 |  2.30285 | 2.77269 | 0.4474  |
+---------------+---------+----------+----------+---------+---------+

Glance
------

+--------------+----------+----------+----------+----------+-----------+
| Operation    |     Mean |   90%ile |   50%ile |      Max |       Min |
+==============+==========+==========+==========+==========+===========+
| create_image | 44.797   | 59.5237  | 43.129   | 73.7454  | 26.3647   |
+--------------+----------+----------+----------+----------+-----------+
| delete_image |  1.51749 |  1.98148 |  1.51694 |  2.93414 |  0.649655 |
+--------------+----------+----------+----------+----------+-----------+

Keystone
--------

+-------------+-----------+----------+----------+----------+-----------+
| Operation   |      Mean |   90%ile |   50%ile |      Max |       Min |
+=============+===========+==========+==========+==========+===========+
| keystone    | 0.0772378 |  0.10375 | 0.071027 | 0.624643 | 0.0493538 |
+-------------+-----------+----------+----------+----------+-----------+

Neutron
-------

+--------------------------+----------+----------+----------+----------+----------+
| Operation                |     Mean |   90%ile |   50%ile |      Max |      Min |
+==========================+==========+==========+==========+==========+==========+
| create_20_rules          | 4.45449  | 4.75529  | 4.4336   | 5.72318  | 3.71847  |
+--------------------------+----------+----------+----------+----------+----------+
| create_2_security_groups | 0.358809 | 0.405863 | 0.350541 | 1.10707  | 0.261818 |
+--------------------------+----------+----------+----------+----------+----------+
| delete_2_security_groups | 0.314609 | 0.397726 | 0.308533 | 0.602876 | 0.191209 |
+--------------------------+----------+----------+----------+----------+----------+

Nova
----

+----------------------+----------+----------+----------+----------+-----------+
| Operation            |     Mean |   90%ile |   50%ile |      Max |       Min |
+======================+==========+==========+==========+==========+===========+
| attach_volume        |  2.77096 |  2.93019 |  2.753   |  3.5367  |  2.50419  |
+----------------------+----------+----------+----------+----------+-----------+
| boot_server          | 13.1012  | 14.1159  | 12.9169  | 17.6851  | 11.2657   |
+----------------------+----------+----------+----------+----------+-----------+
| delete_server        |  2.4879  |  2.62365 |  2.42707 |  4.98843 |  2.32484  |
+----------------------+----------+----------+----------+----------+-----------+
| detach_volume        |  2.64998 |  2.80518 |  2.62848 |  3.30333 |  2.39798  |
+----------------------+----------+----------+----------+----------+-----------+
| find_host_to_migrate |  1.19893 |  1.36617 |  1.21302 |  1.77083 |  0.896176 |
+----------------------+----------+----------+----------+----------+-----------+
| live_migrate         | 14.6121  | 15.3808  | 14.9722  | 26.7783  | 12.3919   |
+----------------------+----------+----------+----------+----------+-----------+

Issues which have been found during the tests
=============================================

.. table:: Issues which have been found during the tests

 +---------------------------------+-----------------------------+-------------+----------+
 |Issue description                |Root cause, Link             | Link to bug | Is fixed |
 +=================================+=============================+=============+==========+
 || Live migration failure.        || Qemu and nova use the same || 1627476_   | Yes      |
 || Port range intersection.       || port range.                ||            |          |
 +---------------------------------+-----------------------------+-------------+----------+

Test result from run where bug mentioned above was not fixed: :download:`rally_report.html <configs/rally_report_last.html>`

.. references:

.. _Rally installation documentation: https://rally.readthedocs.io/en/latest/install.html

.. _1628652: https://bugs.launchpad.net/mos/+bug/1628652

.. _1627476: https://bugs.launchpad.net/mos/+bug/1627476

