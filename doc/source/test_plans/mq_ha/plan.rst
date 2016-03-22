.. _message_queue_ha:

===============================
Message Queue High Availability
===============================

:status: draft
:version: 1

:Abstract:

  This document describes a test plan for analysing high availability of
  OpenStack message bus. The measurement covers message queue and
  oslo.messaging library.


Test Plan
=========

Test Environment
----------------

RabbitMQ is installed on 3 nodes in HA mode. Active monitoring is implemented
with help of pacemaker. The test tool is executed on another host.

Preparation
^^^^^^^^^^^

Setup RabbitMQ cluster, for example by using the setup made by OpenStack Fuel.

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

Network
~~~~~~~

This section contains list of interfaces and network parameters.
For complicated cases this section may include topology diagram and switch
parameters.

+------------------+-------+-------------------------+
| Parameter        | Value | Comments                |
+------------------+-------+-------------------------+
| card model       |       | e.g. Intel              |
+------------------+-------+-------------------------+
| driver           |       | e.g. ixgbe              |
+------------------+-------+-------------------------+
| speed            |       | e.g. 10G or 1G          |
+------------------+-------+-------------------------+

Software
~~~~~~~~

This section describes installed software.

+-----------------+-------+---------------------------+
| Parameter       | Value | Comments                  |
+-----------------+-------+---------------------------+
| OS              |       | e.g. Ubuntu 14.04.3       |
+-----------------+-------+---------------------------+
| oslo.messaging  |       | e.g. 4.0.0                |
+-----------------+-------+---------------------------+
| MQ Server       |       | e.g. RabbitMQ 3.5.6       |
+-----------------+-------+---------------------------+
| HA mode         |       | e.g. Cluster              |
+-----------------+-------+---------------------------+


.. _message_queue_ha_rpc_cmsm_km:

Test Case 1: Client and Server connected to Master, Master fails
----------------------------------------------------------------

.. image:: cmsm-km.*

Description
^^^^^^^^^^^

In this test case both client and server are connected to RabbitMQ master node.
The throughput is measured and at the same time RabbitMQ master process is
terminated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test case result is time series showing message flow between client and server.
It can be shown as chart and/or table. The average throughput and number of
errors are calculated.

========  ==========  =================  =================================
Priority  Value       Measurement Units  Description
========  ==========  =================  =================================
1         Throughput  msg/sec            Number of messages per second
2         Latency     ms                 The latency in message processing
========  ==========  =================  =================================

Options
^^^^^^^

The test case is executed for different types of communication:
 * `RPC call`_
 * `RPC cast`_
 * `Notification`_


.. _message_queue_ha_rpc_cs1ss1_ks1:

Test Case 2: Client and Server connected to Slave 1, Slave 1 fails
------------------------------------------------------------------

.. image:: cs1ss1-ks1.*

Description
^^^^^^^^^^^

In this test case both client and server are connected to the same RabbitMQ
slave node. The throughput is measured and at the same time RabbitMQ slave
process is terminated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test case result is time series showing message flow between client and server.
It can be shown as chart and/or table. The average throughput and number of
errors are calculated.

========  ==========  =================  =================================
Priority  Value       Measurement Units  Description
========  ==========  =================  =================================
1         Throughput  msg/sec            Number of messages per second
2         Latency     ms                 The latency in message processing
========  ==========  =================  =================================

Options
^^^^^^^

The test case is executed for different types of communication:
 * `RPC call`_
 * `RPC cast`_
 * `Notification`_


.. _message_queue_ha_rpc_cs1ss2_ks2:

Test Case 3: Client and Server on different slaves. Client Slave fails
----------------------------------------------------------------------

.. image:: cs1ss2-ks2.*

Description
^^^^^^^^^^^

In this test case client and server are connected to different RabbitMQ
slave node. The throughput is measured and at the same time RabbitMQ slave
process is terminated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test case result is time series showing message flow between client and server.
It can be shown as chart and/or table. The average throughput and number of
errors are calculated.

========  ==========  =================  =================================
Priority  Value       Measurement Units  Description
========  ==========  =================  =================================
1         Throughput  msg/sec            Number of messages per second
2         Latency     ms                 The latency in message processing
========  ==========  =================  =================================

Options
^^^^^^^

The test case is executed for different types of communication:
 * `RPC call`_
 * `RPC cast`_
 * `Notification`_


.. _message_queue_ha_rpc_cmss2_km:

Test Case 4: Client on Master and Server on Slave, Master fails
---------------------------------------------------------------

.. image:: cmss2-km.*

Description
^^^^^^^^^^^

In this test case client and server are connected to different RabbitMQ
slave node: the client to master and server to slave. The throughput is
measured and at the same time RabbitMQ slave process is terminated.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test case result is time series showing message flow between client and server.
It can be shown as chart and/or table. The average throughput and number of
errors are calculated.

========  ==========  =================  =================================
Priority  Value       Measurement Units  Description
========  ==========  =================  =================================
1         Throughput  msg/sec            Number of messages per second
2         Latency     ms                 The latency in message processing
========  ==========  =================  =================================

Options
^^^^^^^

The test case is executed for different types of communication:
 * `RPC call`_
 * `RPC cast`_
 * `Notification`_


Tools
=====

This section contains tools that can be used to perform the test plan.

.. include:: performa.rst


Reports
=======

Test plan execution reports:
 * :ref:`mq_ha_rabbit_report`

.. references:

.. _RPC call: http://docs.openstack.org/developer/oslo.messaging/rpcclient.html#oslo_messaging.RPCClient.call
.. _RPC cast: http://docs.openstack.org/developer/oslo.messaging/rpcclient.html#oslo_messaging.RPCClient.cast
.. _Notification: http://docs.openstack.org/developer/oslo.messaging/notifier.html#notifier
