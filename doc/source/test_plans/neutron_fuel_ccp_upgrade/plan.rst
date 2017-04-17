.. _neutron_fuel_ccp_upgrade_test_plans:

=============================================================
OpenStack Neutron Testing During Open Stack Upgrade Test Plan
=============================================================

:status: **ready**
:version: 1.0

:Abstract:

  This test plan aims to provide set of tests to identify OpenStack
  performance against given containerized OpenStack cloud (installed
  on the top of pre-deployed Kubernetes cluster) using simple minimalistic set
  of Shaker tests during upgrade from Mitaka to Newton.

:Conventions:

    - **Shaker** - Data plane performance testing tool
    - **iperf** - Commonly-used network testing tool


Test Plan
=========

The purpose of this section is to describe scenarios for testing Open Stack
networking during upgrade from Mitaka to Newton.


Test Environment
----------------

Preparation
^^^^^^^^^^^

This test plan is performed against existing OpenStack cloud installed on top
of pre-deployed Kubernetes cluster with `fuel-ccp`_ tool with pre-installed Rally
framework.

.. _fuel-ccp: http://fuel-ccp.readthedocs.io/en/latest/

Environment description
^^^^^^^^^^^^^^^^^^^^^^^
The environment description includes hardware specification of servers,
network parameters, operation system and OpenStack deployment characteristics.

Hardware
~~~~~~~~

This section contains list of all types of hardware nodes (table below is
an example).

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

This section contains list of interfaces and network parameters. For
complicated cases this section may include topology diagram and switch
parameters (table below is an example).

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

This section describes installed software (table below is an example).

+-----------------+-------+---------------------------+
| Parameter       | Value | Comments                  |
+-----------------+-------+---------------------------+
| OS              |       | e.g. Ubuntu 14.04.3       |
+-----------------+-------+---------------------------+
| OpenStack       |       | e.g. Mitaka               |
+-----------------+-------+---------------------------+
| Hypervisor      |       | e.g. KVM                  |
+-----------------+-------+---------------------------+
| Neutron plugin  |       | e.g. ML2 + OVS            |
+-----------------+-------+---------------------------+
| L2 segmentation |       | e.g. VLAN / VxLAN / GRE   |
+-----------------+-------+---------------------------+
| virtual routers |       | e.g. HA / DVR             |
+-----------------+-------+---------------------------+

Test tool
---------

Shaker wraps around popular system network testing tools like iperf, iperf3
and netperf (with help of flent). Shaker is able to deploy OpenStack instances
and networks in different topologies. Shaker scenario specifies the deployment
and list of tests to execute. Additionally tests may be tuned dynamically
in command-line.

Test Case 1: Analysis of L2 metrics during Open Stack upgrade
-------------------------------------------------------------

Description
^^^^^^^^^^^

`Shaker <http://pyshaker.readthedocs.org/en/latest/index.html>`__ is
able to deploy OpenStack instances and networks in different topologies.


The following steps should be executed:

1. Deploy Kubernetes cluster
2. Deploy Open Stack cluster
3. Run full_l2 shaker's scenario and wait successfully stack heats deployment
4. Start Open Stack upgrade



List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. table:: Shaker metrics

========  ===============  =================  ======================================
Priority  Value            Measurement Units  Description
========  ===============  =================  ======================================
1         Errors           times              Number of errors during testing
1         Lost             times              Number of lost results during testing
1         Latency          ms                 The network latency
1         TCP bandwidth    Mbits/s            TCP network bandwidth
2         UDP bandwidth    packets per sec    Number of UDP packets of 32 bytes size
2         TCP retransmits  packets per sec    Number of retransmitted TCP packets
========  ===============  =================  ======================================

Test Case 2: Analysis of L3 metrics during Open Stack upgrade
-------------------------------------------------------------

Description
^^^^^^^^^^^

`Shaker <http://pyshaker.readthedocs.org/en/latest/index.html>`__ is
able to deploy OpenStack instances and networks in different topologies.


The following steps should be executed:

1. Deploy Kubernetes cluster
2. Deploy Open Stack cluster
3. Run full_l3_east_west shaker's scenario and wait successfully stack heats
   deployment
4. Start Open Stack upgrade



List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. table:: Shaker metrics

========  ===============  =================  ======================================
Priority  Value            Measurement Units  Description
========  ===============  =================  ======================================
1         Errors           times              Number of errors during testing
1         Lost             times              Number of lost results during testing
1         Latency          ms                 The network latency
1         TCP bandwidth    Mbits/s            TCP network bandwidth
2         UDP bandwidth    packets per sec    Number of UDP packets of 32 bytes size
2         TCP retransmits  packets per sec    Number of retransmitted TCP packets
========  ===============  =================  ======================================

Reports
=======

Test plan execution reports:
 * :ref:`neutron_fuel_ccp_upgrade_report`
