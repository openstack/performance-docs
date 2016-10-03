.. _openstack_neutron_control_plane_performance_test_plan:

==================================================================
OpenStack Networking (Neutron) control plane performance test plan
==================================================================

:status: **ready**
:version: 1.0

:Abstract:

  This test plan aims to provide set of tests to identify OpenStack Networking
  (aka Neutron) Control Plane performance against given OpenStack cloud using
  Rally tests.

Test Plan
=========
This test plan describes several Rally test cases that can cover almost
all most important in terms of networking performance basic cloud
operations e.g. routers, security groups and other objects management.

Test Environment
----------------

Preparation
^^^^^^^^^^^

This test plan is performed either against existing OpenStack cloud with
pre-installed Rally framework or can be executed via Rally from very beginning
including deployment of the OpenStack cloud. As an option verification (Tempest
testing) can be run prior the benchmarking (scenarios to be described in this
document).

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

**Rally** is a benchmarking tool that was designed specifically for OpenStack
API testing. To make this possible, **Rally** automates and unifies multi-node
OpenStack deployment, cloud verification, benchmarking & profiling. This is a
simple way to check cloud workability and performance of control plane
operations running on it.

Test Case 1: Basic Neutron test suite
-------------------------------------

Description
^^^^^^^^^^^

This test suite is combined from default Rally Neutron test cases with `default
configuration`_. It is most useful for validating cloud operability. The
following Rally test scenarios need to be executed:

* create-and-list-floating-ips
* create-and-list-networks
* create-and-list-ports
* create-and-list-routers
* create-and-list-security-groups
* create-and-list-subnets
* create-and-delete-floating-ips
* create-and-delete-networks
* create-and-delete-ports
* create-and-delete-routers
* create-and-delete-security-groups
* create-and-delete-subnets
* create-and-update-networks
* create-and-update-ports
* create-and-update-routers
* create-and-update-security-groups
* create-and-update-subnets

.. _default configuration: https://github.com/openstack/rally/tree/master/samples/tasks/scenarios/neutron

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+-------------------+---------------------------+
| Priority | Value | Measurement Units | Description               |
+==========+=======+===================+===========================+
| 1        |       | sec               | Time of atomic operations |
+----------+-------+-------------------+---------------------------+

Test Case 2: Stressful Neutron test suite
-----------------------------------------

Description
^^^^^^^^^^^

This test case the same set of scenarios that were mentioned in
`Test Case 1: Basic Neutron test suite`_ can be used, the difference is in
increased number of iterations and concurrency that create sufficient load on
Neutron control plane. To stress OpenStack networking control plane 50-100
concurrency can be used with 2000-5000 iterations in total. We can advice to
focus on the following Rally test cases (that cover most interesting and most
stressed parts of OpenStack Networking):

* create-and-list-networks
* create-and-list-ports
* create-and-list-routers
* create-and-list-security-groups
* create-and-list-subnets
* boot-and-list-server
* boot-and-delete-server-with-secgroups
* boot-runcommand-delete

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+-------------------+---------------------------+
| Priority | Value | Measurement Units | Description               |
+==========+=======+===================+===========================+
| 1        |       | sec               | Time of atomic operations |
+----------+-------+-------------------+---------------------------+

Test case 3: Neutron scalability test with many networks
--------------------------------------------------------

Description
^^^^^^^^^^^

The aim of this test is to create a large number of networks, subnets, routers
and security groups with rules per tenant. Each network has a single VM. For
example 100 networks (each with a subnet, router and a VM) can be created per
each iteration (up to 20 iterations in total).

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+-------------------+---------------------------+
| Priority | Value | Measurement Units | Description               |
+==========+=======+===================+===========================+
| 1        |       | sec               | Time of atomic operations |
+----------+-------+-------------------+---------------------------+

Test case 4: Neutron scalability test with many servers
-------------------------------------------------------

The outline of this test is almost the same as of
`Test case 3: Neutron scalability test with many networks`_. The main
difference is that during each scenario iteration this test creates huge enough
number of VMs (e.g. 100) per a single network, hence it is possible to check
the case with many number of ports per subnet.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+-------------------+---------------------------+
| Priority | Value | Measurement Units | Description               |
+==========+=======+===================+===========================+
| 1        |       | sec               | Time of atomic operations |
+----------+-------+-------------------+---------------------------+

Reports
=======

Test plan execution reports:
 * :ref:`openstack_neutron_control_plane_performance_report`
