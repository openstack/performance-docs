.. _neutron_resource_density_test_plan:

============================================
OpenStack Neutron Resource Density Test Plan
============================================

:status: **draft**
:version: 1.0

:Abstract:
  Is data-plane performance affected by existence of other OpenStack resources?



Test Plan
=========

The goal of this test plan is to investigate whether existing OpenStack
resources affect data-plane performance.

Out of all resources the following may theoretically affect performance:
  * instances running on the same compute host - because of CPU consumption,
    additional network namespaces, iptables, OVS ports and flows;
  * routers - because of Linux network and OVS resources;
  * security groups and rules - because of iptables rules.


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
| virtual routers |       | HA                        |
+-----------------+-------+---------------------------+

Test Case: Data-plane performance measurements
----------------------------------------------

Description
^^^^^^^^^^^

Measurements are performed between 2 instances running on different compute
nodes. One of instances has floating IP assigned and thus is reachable from
outside. We are interested in following metrics: TCP max throughput and
UDP top packets throughput (for 64-byte packets).

TCP throughput is measured with `flent`_::

    flent -H <destination> -f stats tcp_download

UDP throughput is measured with `iperf3`_::

    iperf3 -c <destination> -u -l 64 -b 0 -t 20

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ===============  =================  ======================================
Priority  Value            Measurement Units  Description
========  ===============  =================  ======================================
1         Latency          ms                 The network latency
1         TCP bandwidth    Mbits/s            TCP network bandwidth
1         UDP bandwidth    packets per sec    Number of UDP packets of 32 bytes size
========  ===============  =================  ======================================

Reports
=======

Test plan execution reports:
 * :ref:`neutron_neutron_resource_test_report`

.. references:

.. _flent: http://flent.org/
.. _iperf3: http://iperf.fr/
