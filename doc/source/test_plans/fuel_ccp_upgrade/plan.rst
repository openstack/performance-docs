.. _fuel_ccp_upgrade_test_plan:

==================================================================
Fuel Containerized Control Plane upgradability performance testing
==================================================================

:status: **ready**
:version: 1.0

:Abstract:

  This test plan aims to provide set of tests to identify OpenStack
  performance against given containerized OpenStack cloud (installed
  on the top of pre-deployed Kubernetes cluster) using simple minimalistic set
  of Rally tests during upgrade from Mitaka to Newton.

Test Plan
=========

This test plan covers basic network performance with long-running test suites
to verify cloud network stability and performance during update Open Stack
from Mitaka to Newton.

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

**Rally** is a benchmarking tool that was designed specifically for OpenStack
API testing. To make this possible, **Rally** automates and unifies multi-node
OpenStack deployment, cloud verification, benchmarking & profiling. This is a
simple way to check cloud workability and performance of control plane
operations running on it.

Test Case 1: Boot and delete server during Open Stack update
------------------------------------------------------------

Description
^^^^^^^^^^^

The most user-facing control plane operation is new virtual machine creation.
This scenario covers the most basic OpenStack server creation to present the
baseline numbers for Nova (OpenStack Compute) control plane.

Parameters
^^^^^^^^^^

+-------------------------+-----------------------------------------+
|Name                     | Description                             |
+=========================+=========================================+
|IMAGE                    | Image from which boot server            |
+-------------------------+-----------------------------------------+
|FLAVOR                   | Flavor type from which boot server      |
+-------------------------+-----------------------------------------+
|ASSIGN_NIC               | Bool, whether or not to auto assign     |
|                         | NICs in Rally scenario                  |
+-------------------------+-----------------------------------------+
|CONCURRENCY              | Amount of parallel executors            |
+-------------------------+-----------------------------------------+
|ITERATIONS               | Total amount of iterations processed by |
|                         | all executors                           |
+-------------------------+-----------------------------------------+


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+-------------------+---------------------------+
| Priority | Value | Measurement Units | Description               |
+==========+=======+===================+===========================+
| 1        |       | sec               | Time of atomic operations |
+----------+-------+-------------------+---------------------------+

Measuring performance values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create server with FLAVOR flavor from IMAGE image through Nova API
2. Delete server through Nova API.

These 2 steps executed successively in CONCURRENCY parallel executors.
ASSIGN_NIC parameter reflects Rally scenario configuration whether to assign
NIC to the booted server in automatic fashion.

One cycle of these 2 steps is called an iteration.
ITERATIONS is a total amount of iterations which was processed by executors.

During this testing

At the end of this test case you should calculate average, 90% percentile,
50% percentile, minimum and maximum for each step. You need to fill the
following tables with calculated values:


Nova
----

+---------------+------+--------+--------+-------+-------+
| Operation     | Mean | 90%ile | 50%ile | Max   | Min   |
|               | (sec)| (sec)  | (sec)  | (sec) | (sec) |
+===============+======+========+========+=======+=======+
| create_server |      |        |        |       |       |
+---------------+------+--------+--------+-------+-------+
| delete_server |      |        |        |       |       |
+---------------+------+--------+--------+-------+-------+

Example of Rally scenario configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: test_plans/021-nova-boot-and-delete-baseline.yaml
   :language: bash
