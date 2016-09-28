.. _fuel_ccp_test_plan:

====================================================
Fuel Containerized Control Plane performance testing
====================================================

:status: **ready**
:version: 1.0

:Abstract:

  This test plan aims to provide set of tests to identify OpenStack
  performance against given containerized OpenStack cloud (installed
  on the top of pre-deployed Kubernetes cluster) using simple minimalistic set
  of Rally tests.

Test Plan
=========

This document is inspired by
:ref:`openstack_control_plane_performance_test_plan`, and aims to cover
baseline cloud operations and extend this test suite to verify containerized
deployment approach. As :ref:`openstack_control_plane_performance_test_plan`
this test plan covers basic cloud operations e.g. VMs creation, work with the
security groups, authentication and more, as well as long-running test suites
to verify cloud stability.

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

Test Case 1: Boot and delete server
-----------------------------------

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

Test Case 2: Boot and delete server with security groups
--------------------------------------------------------

Description
^^^^^^^^^^^

The most user-facing control plane operation is new virtual machine creation.
At the same time security groups management is very time consuming operation
in case of lots VMs attached to the same security group, therefore it's vital
to understand these operations performance. Standard Rally scanario is used for
this purpose (comparing with
:ref:`openstack_control_plane_performance_test_plan` fuel-ccp does not support
yet Cinder installation or appropriate Nova configuration to support live
migrations, so there is no need to write separated plugin to cover these
operations).

Parameters
^^^^^^^^^^

+-------------------------+-----------------------------------------+
|Name                     | Description                             |
+=========================+=========================================+
|IMAGE                    | Image from which boot server            |
+-------------------------+-----------------------------------------+
|FLAVOR                   | Flavor type from which boot server      |
+-------------------------+-----------------------------------------+
|SEC_GROUP_COUNT          | Count of security groups                |
|                         | to be created in one iteration          |
+-------------------------+-----------------------------------------+
|RULES_PER_SECURITY_GROUP | Count of rules to be added to           |
|                         | each security group                     |
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

1. Successively create SEC_GROUP_COUNT security groups through Nova API.
   Duration of this step represent time that control plane process
   create_SEC_GROUP_COUNT_security_groups atomic operation.
2. Successively create RULES_PER_SECURITY_GROUP rules for security
   groups through Nova API.
3. Create server with FLAVOR flavor from IMAGE image through Nova API
4. List all security groups through Nova API.
5. Delete server through Nova API.
6. Successively delete SEC_GROUP_COUNT security group through Nova API.

These 6 steps executed successively in CONCURRENCY parallel executors.
One cycle of these 6 steps is called an iteration.

ITERATIONS is a total amount of iterations which was processed by executors.

At the end of this test case you should calculate average, 90% percentile,
50% percentile, minimum and maximum for each step. You need to fill the
following tables with calculated values:

Neutron
-------

+--------------------------+------+--------+--------+-------+-------+
| Operation                | Mean | 90%ile | 50%ile | Max   | Min   |
|                          | (sec)| (sec)  | (sec)  | (sec) | (sec) |
+==========================+======+========+========+=======+=======+
| create_N_security_groups |      |        |        |       |       |
+--------------------------+------+--------+--------+-------+-------+
| delete_N_security_groups |      |        |        |       |       |
+--------------------------+------+--------+--------+-------+-------+
| create_M_rules           |      |        |        |       |       |
+--------------------------+------+--------+--------+-------+-------+
| delete_M_rules           |      |        |        |       |       |
+--------------------------+------+--------+--------+-------+-------+

.. note::
  Change operation name to appropriate regarding SEC_GROUP_COUNT and
  RULES_PER_SECURITY_GROUP values.

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

.. literalinclude:: test_plans/041-nova-boot-and-delete-with-secgroups-baseline.yaml
   :language: bash


Test Case 3: Boot and list servers
----------------------------------

Description
^^^^^^^^^^^

This scenario covers density aspect of server creation control plane
operation and checks how many virtual machines can be booted on top
of containerized OpenStack.

Parameters
^^^^^^^^^^

+-------------------------+-----------------------------------------+
|Name                     | Description                             |
+=========================+=========================================+
|IMAGE                    | Image from which boot server            |
+-------------------------+-----------------------------------------+
|FLAVOR                   | Flavor type from which boot server      |
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
2. List all existing servers through Nova API.

These 2 steps executed successively in CONCURRENCY parallel executors.

One cycle of these 2 steps is called an iteration.
ITERATIONS is a total amount of iterations which was processed by executors.

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
| list_servers  |      |        |        |       |       |
+---------------+------+--------+--------+-------+-------+

Example of Rally scenario configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: test_plans/051-nova-boot-and-list-baseline.yaml
   :language: bash

Test Case 4: Create and delete image
------------------------------------

Description
^^^^^^^^^^^

To cover Glance control plane operations simple create and delete image
scenario can be used.

Parameters
^^^^^^^^^^

+-----------------+-----------------------------------------+
|Name             | Description                             |
+=================+=========================================+
|IMAGE            | Image to upload to glance               |
+-----------------+-----------------------------------------+
|CONTAINER_FORMAT | Container format to create              |
+-----------------+-----------------------------------------+
|DISK_FORMAT      | Disk format to create                   |
+-----------------+-----------------------------------------+
|CONCURRENCY      | Amount of parallel executors            |
+-----------------+-----------------------------------------+
|ITERATIONS       | Total amount of iterations processed by |
|                 | all executors                           |
+-----------------+-----------------------------------------+

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+-------------------+---------------------------+
| Priority | Value | Measurement Units | Description               |
+==========+=======+===================+===========================+
| 1        |       | sec               | Time of atomic operations |
+----------+-------+-------------------+---------------------------+

Measuring performance values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create image from IMAGE with CONTAINER_FORMAT container format and
   DISK_FORMAT disk format through Glance API.
2. Delete image from Glance through Glance API.

These 2 steps executed successively in CONCURRENCY parallel executors.
One cycle of thee 2 steps is called an iteration.

ITERATIONS is a total amount of iterations which was processed by executors.

At the end of this test case you should calculate average, 90% percentile,
50% percentile, minimum and maximum for each step. You need to fill the
following tables with calculated values:

Glance
------

+--------------+------+--------+--------+-------+-------+
| Operation    | Mean | 90%ile | 50%ile | Max   | Min   |
|              | (sec)| (sec)  | (sec)  | (sec) | (sec) |
+==============+======+========+========+=======+=======+
| create_image |      |        |        |       |       |
+--------------+------+--------+--------+-------+-------+
| delete_image |      |        |        |       |       |
+--------------+------+--------+--------+-------+-------+

Example of Rally scenario configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: test_plans/011-glance-create-and-delete-1g-image.yaml
   :language: bash

Test Case 5: Create and list images
-----------------------------------

Description
^^^^^^^^^^^

To cover Glance control plane operations simple create and list images scenario
can be used.

Parameters
^^^^^^^^^^

+-----------------+-----------------------------------------+
|Name             | Description                             |
+=================+=========================================+
|IMAGE            | Image to upload to glance               |
+-----------------+-----------------------------------------+
|CONTAINER_FORMAT | Container format to create              |
+-----------------+-----------------------------------------+
|DISK_FORMAT      | Disk format to create                   |
+-----------------+-----------------------------------------+
|CONCURRENCY      | Amount of parallel executors            |
+-----------------+-----------------------------------------+
|ITERATIONS       | Total amount of iterations processed by |
|                 | all executors                           |
+-----------------+-----------------------------------------+

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+-------------------+---------------------------+
| Priority | Value | Measurement Units | Description               |
+==========+=======+===================+===========================+
| 1        |       | sec               | Time of atomic operations |
+----------+-------+-------------------+---------------------------+

Measuring performance values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create image from IMAGE with CONTAINER_FORMAT container format and
   DISK_FORMAT disk format through Glance API.
2. List existing images through Glance API.

These 2 steps executed successively in CONCURRENCY parallel executors.
One cycle of thee 2 steps is called an iteration.

ITERATIONS is a total amount of iterations which was processed by executors.

At the end of this test case you should calculate average, 90% percentile,
50% percentile, minimum and maximum for each step. You need to fill the
following tables with calculated values:

Glance
------

+--------------+------+--------+--------+-------+-------+
| Operation    | Mean | 90%ile | 50%ile | Max   | Min   |
|              | (sec)| (sec)  | (sec)  | (sec) | (sec) |
+==============+======+========+========+=======+=======+
| create_image |      |        |        |       |       |
+--------------+------+--------+--------+-------+-------+
| list_images  |      |        |        |       |       |
+--------------+------+--------+--------+-------+-------+

Example of Rally scenario configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: test_plans/012-glance-create-and-list-image.yaml
   :language: bash

Test case 6: Keystone authentication
------------------------------------

Description
^^^^^^^^^^^

To cover Keystone control plane operations simple authenticate
scenario can be used.

Parameters
^^^^^^^^^^

+------------------+-----------------------------------------+
| Name             | Description                             |
+==================+=========================================+
| RPS              | Generated load                          |
+------------------+-----------------------------------------+
| ITERATIONS       | Total amount of iterations processed by |
|                  | all executors                           |
+------------------+-----------------------------------------+

Measuring performance values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Authenticate in Keystone through Keystone API.

This step is executed in parallel on multiple executors to generate
RPS load.

Execution of this step is called an iteration.

ITERATIONS is a total amount of iterations which was processed by executors.

At the end of this test case you should calculate average, 90% percentile,
50% percentile, minimum and maximum for each step. You need to fill the
following tables with calculated values:

Keystone
--------

+--------------+------+--------+--------+-------+-------+
| Operation    | Mean | 90%ile | 50%ile | Max   | Min   |
|              | (sec)| (sec)  | (sec)  | (sec) | (sec) |
+==============+======+========+========+=======+=======+
| authenticate |      |        |        |       |       |
+--------------+------+--------+--------+-------+-------+

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+-------------------+---------------------------+
| Priority | Value | Measurement Units | Description               |
+==========+=======+===================+===========================+
| 1        |       | sec               | Time of atomic operations |
+----------+-------+-------------------+---------------------------+

Example of Rally scenario configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: test_plans/001-keystone-authenticate-90-rps.yaml
   :language: bash

Reports
=======

Test plan execution reports:

* :ref:`fuel_ccp_test_report`
