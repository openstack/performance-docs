.. _openstack_load_test_plan:

======================
OpenStack load testing
======================

:status: **ready**
:version: 1.0

:Abstract:

  This test plan describes a set of scenarios to measure maximum number
  of requests per second for a particular OpenStack API service.

:Conventions:
  - **RPS** Requests-per-second - number of requests send to an API endpoint
    per second

Test Plan
=========


**Rally** is a benchmarking tool that was designed specifically for OpenStack
API testing. To make this possible, **Rally** automates and unifies multi-node
OpenStack deployment, cloud verification, benchmarking & profiling. This is a
simple way to check cloud workability and performance of control plane
operations running on it. This test plan describes several Rally scenarios
that can cover almost all most important in perms of performance basic cloud
operations e.g. VMs creation, work with the security groups, authentication
and other operations.

Test Environment
----------------

Preparation
^^^^^^^^^^^

This test plan can be executed with help of Rally tool.

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

Test Case 1: Neutron Load Testing
---------------------------------

Description
^^^^^^^^^^^

In this scenario Neutron API is loaded with constant flow of requests. The
number of requests per second is tuned to keep success rate at 100%.
Duration of operations is collected and stats are calculated. The result
is presented in table format.


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+-------------------+-----------------------------------+
| Priority | Value | Measurement Units | Description                       |
+==========+=======+===================+===================================+
| 1        |       | RPS               | Number of API requests per second |
+----------+-------+-------------------+-----------------------------------+


Tools
=====

This test plan can be executed with help of Rally. Following is the list
of Rally scenarios.

Create Neutron networks
-----------------------

In this scenario Rally creates networks at constant rate. The single
iteration includes the following operations:

  #. create network

.. literalinclude:: rally_scenarios/neutron_create_networks.json



Create Neutron network with 1 port
----------------------------------

In this scenario Rally creates Neutron network with one port at constant rate.
The single iteration includes the following operations:

   #. create network
   #. create one port

.. literalinclude:: rally_scenarios/neutron_create_network_with_port.json


Create Neutron ports
--------------------

In this scenario Rally creates Neutron network and ports at constant rate.
The single iteration includes the following operations:

   #. create network
   #. create 20 ports in each of network
   #. list all ports

.. literalinclude:: rally_scenarios/neutron_create_and_list_ports.json


Create Cinder volumes
---------------------

In this scenario Rally creates volumes at constant rate. The single
iteration includes the following operations:

   #. create volume

.. literalinclude:: rally_scenarios/cinder_create_volumes.json


Boot Nova servers
-----------------

In this scenario Rally boots Nova servers at constant rate:

   #. boot server

.. literalinclude:: rally_scenarios/nova_boot_servers.json

Reports
=======

Test plan execution reports:
 * :ref:`openstack_load_report`
