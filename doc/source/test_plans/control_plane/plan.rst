.. _openstack_control_plane_performance_test_plan:

=============================================
OpenStack control plane performance test plan
=============================================

:status: **ready**
:version: 1.0

:Abstract:

  This test plan aims to provide set of tests to identify Control Plane
  performance against given OpenStack cloud using simple minimalistic set of
  Rally tests.

Test Plan
=========
This test plan describes several test cases
that can cover almost all most important in terms of performance basic cloud
operations e.g. VMs creation, work with the security groups, authentication
and other operations.

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

Test Case 1: Boot, attach, migrate and delete server with security groups
-------------------------------------------------------------------------

Description
^^^^^^^^^^^

The most user-facing control plane operation is new virtual machine creation.
At the same time security groups management is very time consuming operation
in case of lots VMs attached to the same security group, therefore it's vital
to understand these operations performance. Special Rally plugin can be written
for this purpose.

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
|VOLUME_SIZE size         | Size of volume to be created in Cinder  |
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
4. Create VOLUME_SIZE GB size volume through Cinder API.
5. Attach created volume to server.
6. Migrate server to pre-chosen host through Nova API.
7. List all security groups through Nova API.
8. Detach volume from server through Nova API.
9. Delete server through Nova API.
10. Delete volume through Cinder API.
11. Successively delete SEC_GROUP_COUNT security group through Nova API.

This 11 steps executed successively in CONCURRENCY parallel executors.
One cycle of this 11 steps is called as iteration.
ITERATIONS is a total amount of iterations which was processed by executors.

At the end of this test case you should calculate average, 90% percentile,
50% percentile, minimum and maximum for each step. You need to fill the
following tables with calculated values:

Cinder
------

+---------------+-------+--------+--------+-------+-------+
| Operation     | Mean  | 90%ile | 50%ile | Max   | Min   |
|               | (sec) | (sec)  | (sec)  | (sec) | (sec) |
+===============+=======+========+========+=======+=======+
| create_volume |       |        |        |       |       |
+---------------+-------+--------+--------+-------+-------+
| delete_volume |       |        |        |       |       |
+---------------+-------+--------+--------+-------+-------+

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
| attach_volume |      |        |        |       |       |
+---------------+------+--------+--------+-------+-------+
| live_migrate  |      |        |        |       |       |
+---------------+------+--------+--------+-------+-------+
| detach_volume |      |        |        |       |       |
+---------------+------+--------+--------+-------+-------+
| delete_server |      |        |        |       |       |
+---------------+------+--------+--------+-------+-------+

Example of Rally scenario configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: test_plans/boot_attach_migrate_delete_server_with_sec_groups.json
   :language: bash

This scenario use custom Rally plugin: :download:`nova_performance.py <plugins/nova_performance.py>`

Test Case 2: Create and delete image
------------------------------------

Description
^^^^^^^^^^^

To cover Glance control plane operations simple crete and delete image scenario
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
2. Delete image from Glance through Glance API.

This 2 steps executed successively in CONCURRENCY parallel executors.
One cycle of this 2 steps is called as iteration.
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

.. literalinclude:: test_plans/create_and_delete_image.json
   :language: bash

Test case 3: Keystone authentication
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

This step executed in parallel on multiple executors to generate
RPS load.
Execution of this step is called as iteration.
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

.. literalinclude:: test_plans/keystone_authenticate.json
   :language: bash

Reports
=======

Test plan execution reports:
 * :ref:`openstack_control_plane_performance_report_200_nodes`
 * :ref:`openstack_control_plane_performance_report_400_nodes`
