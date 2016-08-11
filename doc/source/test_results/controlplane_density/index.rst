
.. _Results_of_OpenStack_services_density_testing:

*********************************************
Results of OpenStack Services density testing
*********************************************

:Abstract:

  This document includes density test results of OpenStack
  services. All tests have been performed
  regarding :ref:`controlplane_density`

Environment description
=======================

Environment contains 5 types of servers:

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
All servers have the similar network configuration:

.. image:: configs/Network_Scheme.png
   :alt: Network Scheme of the environment

Here is a part of switch configuration for each switch port which is
connected to ens1f0 interface of a server:

.. code:: bash

   switchport mode trunk
   switchport trunk native vlan 600
   switchport trunk allowed vlan 600-602,630-649
   spanning-tree port type edge trunk
   spanning-tree bpduguard enable
   no snmp trap link-status

Software configuration on servers with controller and compute roles
-------------------------------------------------------------------

.. table:: Services on servers by role

   +------------+---------------------------+
   |Role        |Service name               |
   +============+===========================+
   |controller  || horizon                  |
   |            || keystone                 |
   |            || nova-api                 |
   |            || nava-scheduler           |
   |            || nova-cert                |
   |            || nova-conductor           |
   |            || nova-consoleauth         |
   |            || nova-consoleproxy        |
   |            || cinder-api               |
   |            || cinder-backup            |
   |            || cinder-scheduler         |
   |            || cinder-volume            |
   |            || glance-api               |
   |            || glance-glare             |
   |            || glance-registry          |
   |            || neutron-dhcp-agent       |
   |            || neutron-l3-agent         |
   |            || neutron-metadata-agent   |
   |            || neutron-openvswitch-agent|
   |            || neutron-server           |
   |            || heat-api                 |
   |            || heat-api-cfn             |
   |            || heat-api-cloudwatch      |
   |            || ceph-mon                 |
   |            || rados-gw                 |
   |            || heat-engine              |
   +------------+---------------------------+
   |compute     || nova-compute             |
   |            || neutron-l3-agent         |
   |            || neutron-metadata-agent   |
   |            || neutron-openvswitch-agent|
   +------------+---------------------------+

.. table:: Software version on servers with controller and compute roles

   +------------+-------------------+
   |Software    |Version            |
   +============+===================+
   |OpenStack   |Mitaka             |
   +------------+-------------------+
   |Ceph        |Hammer             |
   +------------+-------------------+
   |Ubuntu      |Ubuntu 14.04.3 LTS |
   +------------+-------------------+

You can find outputs of some commands and /etc folder in the following
archives:

:download:`controller-1.tar.gz <configs/controller-1.tar.gz>`
:download:`controller-2.tar.gz <configs/controller-2.tar.gz>`
:download:`controller-3.tar.gz <configs/controller-3.tar.gz>`
:download:`compute-1.tar.gz <configs/compute-1.tar.gz>`
:download:`compute-osd-1.tar.gz <configs/compute-osd-1.tar.gz>`

Software configuration on servers with Rally role
-------------------------------------------------

Rally should be installed manually on this server. The extended instructions
can be found in `Rally installation documentation`_

.. table:: Software version on server with Rally role

   +------------+-------------------+
   |Software    |Version            |
   +============+===================+
   |Rally       |0.4.0              |
   +------------+-------------------+
   |Ubuntu      |Ubuntu 14.04.3 LTS |
   +------------+-------------------+


Test results
============

As a result of this part we got the following HTML file:

:download:`rally_report.html <results/rally_report.html>`

All results added below are part of this report, all values are presented in
seconds.

Cinder
------
+---------------+---------+----------+----------+---------+---------+
| Operation     |    Mean |   90%ile |   50%ile |     Max |     Min |
+===============+=========+==========+==========+=========+=========+
| create_volume | 2.58966 |   2.7106 |  2.55807 | 3.81035 | 2.40941 |
+---------------+---------+----------+----------+---------+---------+

Neutron
-------
+---------------------------+----------+-----------+----------+-----------+----------+
| Operation                 |     Mean |    90%ile |   50%ile |       Max |      Min |
+===========================+==========+===========+==========+===========+==========+
| create_100_rules          | 90.6873  | 160.768   | 90.1278  | 176.444   | 21.1011  |
+---------------------------+----------+-----------+----------+-----------+----------+
| create_10_security_groups |  9.26443 |  16.6121  |  9.28746 |  21.1762  |  1.23875 |
+---------------------------+----------+-----------+----------+-----------+----------+
| list_security_groups      |  3.34852 |   5.61315 |  3.45464 |   7.33637 |  0.13018 |
+---------------------------+----------+-----------+----------+-----------+----------+

Nova
----
+---------------+----------+----------+----------+----------+-----------+
| Operation     |     Mean |   90%ile |   50%ile |      Max |       Min |
+===============+==========+==========+==========+==========+===========+
| attach_volume |  2.85446 |  3.03082 |  2.74456 |  6.36683 |  2.49666  |
+---------------+----------+----------+----------+----------+-----------+
| boot_server   | 19.064   | 24.7443  | 18.9116  | 28.9823  | 11.2053   |
+---------------+----------+----------+----------+----------+-----------+
| list_servers  |  4.12437 |  7.17804 |  4.11694 |  9.48992 |  0.174039 |
+---------------+----------+----------+----------+----------+-----------+

.. references:

.. _Rally installation documentation: https://rally.readthedocs.io/en/latest/install.html
