.. _neutron_agent_restart_test_plan:

=============================================================
OpenStack Neutron Control Plane Performance and Agent Restart
=============================================================

:status: **draft**
:version: 1.0


Test Plan
=========

Neutron Server is the core of Neutron control plane. It processes requests
from public API and internal RPC API. The latter is used to communicate with
agents. Normally RPC is used to notify agents about updated configuration.
However in case of agent restart or communication failure the agent requests
all data from server and the amount of data may be significant.

The goal of this test plan is to measure how restart of bunch of agents
affect performance of Neutron control plane.


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

Test Case: mass restart of agents
---------------------------------

Description
^^^^^^^^^^^

Measurements can be performed by methodology described in
:ref:`reliability_testing_version_2`. The following metrics need to be 
collected:

.. list-table::
   :header-rows: 1

   *
     - Priority
     - Value
     - Measurement Unit
     - Description
   *
     - 1
     - Service downtime
     - sec
     - How long the service was not available and operations were in error
       state.
   *
     - 1
     - MTTR
     - sec
     - How long does it takes to recover service performance after the failure.
   *
     - 1
     - Operation Degradation
     - sec
     - the mean of difference in operation performance during recovery period
       and operation performance when service operates normally.
   *
     - 1
     - Operation Degradation Ratio
     - sec
     - the ratio between operation performance during recovery period and
       operation performance when service operates normally.


Reports
=======

Test plan execution reports:
 * :ref:`neutron_agent_restart_test_report`
