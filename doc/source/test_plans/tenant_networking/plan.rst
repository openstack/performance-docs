.. _openstack_tenant_networking_test_plan:

=======================================
OpenStack tenant networking performance
=======================================

:status: **ready**
:version: 1.0

:Abstract:

  This document describes test plan for measuring performance of tenant
  networking of the OpenStack cloud.

:Conventions:

  - **Topology** is how instances are plugged into tenant network

  - **L2 topology** is tenant network topology when instances located in the
    same L2 domain

  - **L3 east-west topology** is tenant network topology when instances
    located in different L2 domains connected to the same Neutron router

  - **L3 north-south topology** is tenant network topology when instances
    located in different L2 domains connected to different Neutron routers,
    thus the traffic goes outside of the cloud and back

Test Plan
=========

This test plan covers base topologies (L2, L3 east-west and L3 north-south)
and collection of common network parameters like bandwidth and latency.

Test Environment
----------------

Preparation
^^^^^^^^^^^

This test plan is performed against existing OpenStack cloud.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers,
network parameters, operation system and OpenStack deployment characteristics.

Hardware
~~~~~~~~

This section contains list of all types of hardware nodes.

+-----------+-------+----------------------------------------------------+
| Parameter | Value | Comments                                           |
+-----------+-------+----------------------------------------------------+
| model     |       | e.g. Supermicro X9SRD-F                            |
+-----------+-------+----------------------------------------------------+
| CPU       |       | e.g. 6 x Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz |
+-----------+-------+----------------------------------------------------+
| role      |       | e.g. compute or network                            |
+-----------+-------+----------------------------------------------------+

Network
~~~~~~~

This section contains list of interfaces and network parameters.
For complicated cases this section may include topology diagram and switch
parameters.

+------------------+-------+-------------------------+
| Parameter        | Value | Comments                |
+------------------+-------+-------------------------+
| network role     |       | e.g. provider or public |
+------------------+-------+-------------------------+
| card model       |       | e.g. Intel              |
+------------------+-------+-------------------------+
| driver           |       | e.g. ixgbe              |
+------------------+-------+-------------------------+
| speed            |       | e.g. 10G or 1G          |
+------------------+-------+-------------------------+
| MTU              |       | e.g. 9000               |
+------------------+-------+-------------------------+
| offloading modes |       | e.g. default            |
+------------------+-------+-------------------------+

Software
~~~~~~~~

This section describes installed software.

+-----------------+-------+---------------------------+
| Parameter       | Value | Comments                  |
+-----------------+-------+---------------------------+
| OS              |       | e.g. Ubuntu 14.04.3       |
+-----------------+-------+---------------------------+
| OpenStack       |       | e.g. Liberty              |
+-----------------+-------+---------------------------+
| Hypervisor      |       | e.g. KVM                  |
+-----------------+-------+---------------------------+
| Neutron plugin  |       | e.g. ML2 + OVS            |
+-----------------+-------+---------------------------+
| L2 segmentation |       | e.g. VLAN or VxLAN or GRE |
+-----------------+-------+---------------------------+
| virtual routers |       | e.g. legacy or HA or DVR  |
+-----------------+-------+---------------------------+

.. _openstack_tenant_networking_test_plan_l2_dense:

Test Case 1: single node L2 instance-to-instance performance
------------------------------------------------------------

Description
^^^^^^^^^^^

This test case is executed on a single pair of instances launched on *one
compute node* and plugged into the same tenant network. The measurement is
done during 60 seconds, average values are calculated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================


.. _openstack_tenant_networking_test_plan_l2:

Test Case 2: L2 instance-to-instance performance
------------------------------------------------

Description
^^^^^^^^^^^

This test case is executed on a single pair of instances launched on *different
compute nodes* and plugged into the same tenant network. The measurement is
done during 60 seconds, average values are calculated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================


.. _openstack_tenant_networking_test_plan_l2_concurrent:

Test Case 3: L2 concurrent performance
--------------------------------------

Description
^^^^^^^^^^^

This test case is executed on pairs of instances. Every instance is deployed
on a different compute nodes (one instance per node). All instances are
plugged into the same tenant network. The measurement is run simultaneously
on different number of instances, starting with one pair and increasing in
geometric progression until all pairs are involved. On every iteration
the measurement is run during 60 seconds, then average numbers are stored.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test case result is series of following measurements done at different
levels of concurrency. The output may be shown in table form and/or as chart
showing dependency of parameters from concurrency.

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================


.. _openstack_tenant_networking_test_plan_l3_east_west_dense:

Test Case 4: single node L3 east-west instance-to-instance performance
----------------------------------------------------------------------

Description
^^^^^^^^^^^

This test case is executed on a single pair of instances launched on *one
compute node* and plugged into different tenant networks. Networks are
connected by a single router. The measurement is done during 60 seconds,
average values are calculated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================


.. _openstack_tenant_networking_test_plan_l3_east_west:

Test Case 5: L3 east-west instance-to-instance performance
----------------------------------------------------------

Description
^^^^^^^^^^^

This test case is executed on a single pair of instances launched on *different
compute nodes* and plugged into different tenant networks. Networks are
connected by a single router. The measurement is done during 60 seconds,
average values are calculated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================


.. _openstack_tenant_networking_test_plan_l3_east_west_concurrent:

Test Case 6: L3 east-west concurrent performance
------------------------------------------------

Description
^^^^^^^^^^^

This test case is executed on pairs of instances. Every instance is deployed
on a different compute nodes (one instance per node). All instances are
grouped by pairs, one member is plugged in tenant network A, the other into
tenant network B. Networks A and B are plugged into a single router.
The measurement is run simultaneously on different number of instances,
starting with one pair and increasing in geometric progression until all
pairs are involved. On every iteration the measurement is run during 60
seconds, then average numbers are stored.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test case result is series of following measurements done at different
levels of concurrency. The output may be shown in table form and/or as chart
showing dependency of parameters from concurrency.

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================


.. _openstack_tenant_networking_test_plan_l3_north_south_dense:

Test Case 7: single node L3 north-south instance-to-instance performance
------------------------------------------------------------------------

Description
^^^^^^^^^^^

This test case is executed on a single pair of instances launched on *one
compute node* and plugged into different tenant networks. Each networks is
connected to own router, thus traffic goes via external network. The
destination instance is reached by floating IP.
The measurement is done during 60 seconds, average values are calculated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================


.. _openstack_tenant_networking_test_plan_l3_north_south:

Test Case 8: L3 north-south instance-to-instance performance
------------------------------------------------------------

Description
^^^^^^^^^^^

This test case is executed on a single pair of instances launched on *different
compute nodes* and plugged into different tenant networks. Each networks is
connected to own router, thus traffic goes via external network. The
destination instance is reached by floating IP.
The measurement is done during 60 seconds, average values are calculated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================


.. _openstack_tenant_networking_test_plan_l3_north_south_concurrent:

Test Case 9: L3 north-south concurrent performance
--------------------------------------------------

Description
^^^^^^^^^^^

This test case is executed on pairs of instances. Every instance is deployed
on a different compute nodes (one instance per node). All instances are
grouped by pairs, one member is plugged into tenant network A, the other into
tenant network B. Networks A and B are plugged into different routers.
Instances from network B are reached via floating IP.
The measurement is run simultaneously on different number of instances,
starting with one pair and increasing in geometric progression until all
pairs are involved. On every iteration the measurement is run during 60
seconds, then average numbers are stored.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test case result is series of following measurements done at different
levels of concurrency. The output may be shown in table form and/or as chart
showing dependency of parameters from concurrency.

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================


.. _openstack_tenant_networking_test_plan_qos:

Test Case 10: Neutron QoS testing
---------------------------------

Description
^^^^^^^^^^^

This test case is used to verify Neutron QoS feature as scale. The feature
allows to limit the traffic bandwidth in a particular network. To simplify
testing instances are deployed in the same network (L2 domain). The target
bandwidth is specified in kBits/s.

.. note::

  In order to work Neutron QoS extension must be installed and properly
  configured.


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ================  =================  ===========================================
Priority  Value             Measurement Units  Description
========  ================  =================  ===========================================
1         Latency           ms                 The network latency
1         TCP bandwidth     Mbits/s            TCP network bandwidth
1         UDP bandwidth     packets per sec    Number of UDP packets with 32 bytes payload
2         UDP delay jitter  ms                 Packet delay variation
2         UDP packet loss   %                  Percentage of lost UDP packets
2         TCP retransmits   packets per sec    Number of retransmitted TCP packets
========  ================  =================  ===========================================

It's expected that achieved TCP bandwidth is not higher that the one set in
Neutron QoS policy.


Tools
=====

This section contains tools that can be used to perform the test plan.

.. include:: shaker.rst

Reports
=======

Test plan execution reports:
 * :ref:`tenant_networking_report_vxlan_dvr_200_nodes`
