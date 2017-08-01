.. _openstack_wan:

===================================
 OpenStack in a WAN Context Testing
===================================

:status: **draft**
:version: 0.1

:Abstract:

   This document describes a test plan for analysing how OpenStack
   behaves under Wide Area Network (WAN) conditions. In particular,
   measuring the effect of high latency, low bandwidth, packet loss
   and link failure.

:Conventions:
   - **WAN** A Wide Area Network (WAN) is a computer network that
     extends over a large geographical distance.
   - **NB_COMPUTES** The number of Computes considered by the tester.
   - **NB_CORES/COMPUTE** The number of cores on a Compute node.


Test Plan
=========

New paradigms like Fog and Edge computing suggest pushing Computes
close to the user. This kind of deployment puts Computes far from
Control services that have to operate through WAN. The current test
plan covers basic cloud operations (VM creations, Security Group
management and IP associations) and communication testing (through
several VMs) under such WAN conditions.


Test Environment
----------------

This section describes the setup for OpenStack testing under WAN
conditions.

Preparation
^^^^^^^^^^^

The current test plan considers a fresh, bare-metal, simple deployment
where Control, Network and Volume services are on the same nodes.
Computes are on dedicated nodes. The tester should fix the number of
Computes depending on the capacity of her testbed. In the rest of this
document, the name *NB_COMPUTES* references the number of Computes.

Regarding network, the following section should describe in details
network settings. In particular, links parameters (latency, bandwidth
and reliability) between OpenStack services. It should also indicate
the use of network emulation functionality (e.g.: `netem`_). In case
of network emulation with netem, netem constraints have to be set up
right after the end of the OpenStack deployment to make tests
reliable.

.. _netem: https://wiki.linuxfoundation.org/networking/netem


Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of
servers, network parameters, operation system and OpenStack deployment
characteristics.

Hardware
~~~~~~~~

This section contains the list of all types of hardware nodes.

+-----------+-------+----------------------------------------------------+
| Parameter | Value | Comments                                           |
+-----------+-------+----------------------------------------------------+
| model     |       | e.g. Supermicro X9SRD-F                            |
+-----------+-------+----------------------------------------------------+
| CPU       |       | e.g. 6 x Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz |
+-----------+-------+----------------------------------------------------+


Network
~~~~~~~

This section contains the list of interfaces and network parameters.
In addition, it should include a topology diagram with latency,
bandwidth and reliability of links between OpenStack services.

+------------------+-------+-------------------------+
| Parameter        | Value | Comments                |
+------------------+-------+-------------------------+
| card model       |       | e.g. Intel              |
+------------------+-------+-------------------------+
| driver           |       | e.g. ixgbe              |
+----------------- +-------+-------------------------+
| speed            |       | e.g.                    |
|                  |       | - *eth0* 10G            |
|                  |       | - *eth1* 10G            |
+----------------- +-------+-------------------------+


Software
~~~~~~~~

This section describes installed software.

+-------------------+--------+---------------------------+
| Parameter         | Value  | Comments                  |
+-------------------+--------+---------------------------+
| OS                |        | e.g. Ubuntu 14.04.3       |
+-------------------+--------+---------------------------+
| DB                |        | e.g. MySQL 5.6            |
+-------------------+--------+---------------------------+
| MQ broker         |        | e.g. RabbitMQ v3.4.25     |
+-------------------+--------+---------------------------+
| OpenStack release |        | e.g. Ocata                |
+-------------------+--------+---------------------------+
| Network emulation |        | e.g. iproute2 4.9.0       |
+-------------------+--------+---------------------------+


Configuration
~~~~~~~~~~~~~

This section describes configuration of OpenStack and core services

+-------------------+-------------------------------+
| Parameter         | File                          |
+-------------------+-------------------------------+
| Keystone          |   ./results/keystone.conf     |
+-------------------+-------------------------------+
| Nova-api          |   ./results/nova-api.conf     |
+-------------------+-------------------------------+
| ...               |                               |
+-------------------+-------------------------------+


Test Case 1: OpenStack control services behaviour under WAN
-----------------------------------------------------------

Description
^^^^^^^^^^^

This test case aims to measure the correct behaviour of OpenStack
under WAN at control plane level. It relies on `Rally`_ that runs
loads on the current OpenStack. Then Rally reports can be used to get
time of operations executions and percent of failure to evaluate
OpenStack. Concretely, this test case considers followings `Rally
scenarios`_ that are known to be sensitive to network performance:

Nova scenarios
  - ``NovaServers.boot_and_delete_multiple_servers``
  - ``NovaServers.boot_and_associate_floating_ip``
  - ``NovaServers.pause_and_unpause_server``
  - ``NovaSecGroup.boot_server_and_add_secgroups``

Neutron scenarios
  - ``NeutronNetworks.create_and_delete_networks``
  - ``NeutronNetworks.create_and_delete_ports``
  - ``NeutronNetworks.create_and_delete_routers``
  - ``NeutronNetworks.create_and_delete_subnets``
  - ``NeutronSecurityGroup.create_and_delete_security_groups``

Glance scenario
  - ``GlanceImages.create_and_delete_image``

Other scenarios such as live migration, VM snapshoting and telemetry
may also be considered.

.. _Rally: https://rally.readthedocs.io/en/latest/
.. _Rally scenarios: https://github.com/openstack/rally/tree/2cb0097bda2b0a04d89834ab2859c83d7013239f/rally/plugins/openstack/scenarios

Parameters
^^^^^^^^^^

+-----------------------------------+------------------------------------------------------+
| Parameter name                    | Value                                                |
+===================================+======================================================+
| RTT latency (ms)                  | LAN, 20, 50, 100, 200                                |
+-----------------------------------+------------------------------------------------------+
| Traffic shaping (% loss)          | 0, 0.1, 1, 10, 25                                    |
+-----------------------------------+------------------------------------------------------+
| Number of VMs (for ``NovaServers. | 1, *NB_COMPUTES*, *NB_COMPUTES* * *NB_CORES/COMPUTE* |
| boot_and_delete_multiple          |                                                      |
| _servers``)                       |                                                      |
+-----------------------------------+------------------------------------------------------+
| Rally concurrency                 | 1, *NB_COMPUTES*, *NB_COMPUTES* * *NB_CORES/COMPUTE* |
+-----------------------------------+------------------------------------------------------+
| VM image                          | CirrOS (~15MB), Alpine (~100MB),                     |
|                                   | Ubuntu-16.04-server (~800MB)                         |
+-----------------------------------+------------------------------------------------------+

The `netem`_ application can help to achieve WAN simulation by
applying network constraints (RTT latency and packet loss) between the
Control node and Computes. The tester may refer to the `Test tool`_
section for such purpose scripts.

Rally ``times`` parameter should be configured properly to produce
accurate results. Furthermore, the tester may choose to execute
scenarios in cold- or hot-cache.


Further parameters
^^^^^^^^^^^^^^^^^^

WAN conditions often lead to link failures and so should be tested. A
link failure should appear at a specific point in the workflow of a
Rally scenario. For instance, just after the
``nova.compute.manager.ComputeManager.build_and_run_instance`` `RPC
call`_ in the case of ``NovaServers.boot_and_delete_multiple_servers``
Rally scenario. The duration of link failure is another important
parameter. However, to the best of our knowledge, there are no tools
to automatically inject such failure at a specific point of an
OpenStack workflow (something more convenient than modifying the
OpenStack source code).

.. _RPC call: https://github.com/openstack/nova/blob/bf34d5f25ca6f4650777a5eb4e3316c5af8ba54d/nova/compute/manager.py#L1720


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

=========  ===============  =================  ===================================
Priority   Value            Measurement Units  Description
=========  ===============  =================  ===================================
1                           sec                Time of operation execution
1                           percentage         Operation execution failure
=========  ===============  =================  ===================================


Test Case 2: OpenStack data plane behaviour under WAN
-----------------------------------------------------

Description
^^^^^^^^^^^

This test case aims to measure the correct behaviour of OpenStack
under WAN at data plane level. It relies on `Shaker`_ that starts VMs
and runs network test on the current OpenStack. Then Shaker reports
can be used to get throughput and round-trip time between VMs in order
to evaluate OpenStack. Expectation here is that Neutron configuration
has a strong impact on data plane, e.g.: going with `DVR`_ or
`Dragonflow`_. This test case considers followings `Shaker
scenarios`_:

- ``openstack/full_l2``
- ``openstack/dense_l3_east_west``
- ``openstack/full_l3_east_west``

Note that a Shaker test requires Heat service to be running.

.. _Shaker: https://pyshaker.readthedocs.io/en/latest/
.. _DVR: https://wiki.openstack.org/wiki/Neutron/DVR
.. _Dragonflow: https://wiki.openstack.org/wiki/Dragonflow
.. _Shaker scenarios: https://github.com/openstack/shaker/tree/4f5005c7798312072b9b14117f45682ff9301c44/shaker/scenarios/openstack


Parameters
^^^^^^^^^^

============================  ====================================================
Parameter name                Value
============================  ====================================================
RTT latency (ms)              LAN, 20, 50, 100, 200
Traffic shaping (% loss)      0, 0.1, 1, 10, 25
Shaker concurrency            1, *NB_COMPUTES*, *NB_COMPUTES* * *NB_CORES/COMPUTE*
============================  ====================================================


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

=========  ===============  =================  ===================================
Priority   Value            Measurement Units  Description
=========  ===============  =================  ===================================
1                           ms                 Ping
2                           Mbits/s            TCP download
2                           Mbits/s            TCP upload
=========  ===============  =================  ===================================

Test tool
---------

The tester can use `EnOS`_ to conduct the current test plan. EnOS is a
tool that helps tester to (1) easily get testbed resources, (2)
deploys and initialises OpenStack over these resources, (3) set
network constraints, (4) invokes benchmarks and provides test reports.
EnOS comes with a set of `testing scenarios`_ including `some for the
current test plan`_.

.. _EnOS: https://enos.readthedocs.io/en/latest/
.. _testing scenarios: https://github.com/BeyondTheClouds/enos-scenarios
.. _some for the current test plan: https://github.com/BeyondTheClouds/enos-scenarios/tree/1c2edd70ce02fd8a3062193120032e848dd9561f/wan
