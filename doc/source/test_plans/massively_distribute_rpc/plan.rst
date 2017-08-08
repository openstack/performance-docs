.. _message_queue_performance:

==========================
Massively Distributed RPCs
==========================

:status: **draft**
:version: 1.0

:Abstract:

  This document describes a test plan for evaluating the OpenStack message bus
  in the context of a massively distributed cloud architecture. For instance, a
  massively distributed cloud addresses the use case of the Fog or Edge
  computing where the services are geographically distributed accross a large
  area. For the time being, OpenStack inter-service communications rely on
  oslo_messaging which defines a common abstraction to different instantiations
  of the message bus. Historically broker-based implementations (e.g RabbitMQ,
  QPid) competed with brokerless based implementations (e.g ZeroMQ), but with
  the advent of AMQP1.0 in oslo_messaging, `alternative non-broker`_ messaging
  system can be now envisioned. In the latter messages can traverse a set of
  inter-connected agents (broker or routers) before reaching their destination.

  The test plan takes place in the context of a prospective effort to evaluate
  the distribution of the messaging bus using emerging solutions (e.g qpid
  dispatch router) or established ones (e.g Zero-MQ) compared to the
  traditional and centralized solutions (e.g RabbitMQ). Finally the scope of
  the test plan is RPC communication between OpenStack services, thus
  notification is out of the scope of range.

Test Plan
=========

Test Environment
----------------

Most of the following test cases are synthetic tests. Those tests are performed
on top of oslo_messaging in isolation from any OpenStack components. The test
plan is completed by an operational testing. It aims to evaluate the overall
behaviour of Openstack using similar deployment of the messaging middleware.

Preparation
^^^^^^^^^^^

For the synthetic tests tools like `ombt2`_ or `simulator`_ can be used. In the
former case it must be configured to use a separated control bus (e.g RabbitMQ)
different from the message bus under test. This will avoid any unwanted
perturbations in the measurements. Failure injection can leverage `os_faults`_.
Both synthetic and operational experiments can be scripted using `enoslib`_.
Finally operational testing can leverage `rally`_ .

.. include:: environment_description.rst

Test Case 1 : One single large distributed target
-------------------------------------------------

Description
^^^^^^^^^^^

In this test case clients are sending requests to the same Target. Servers are
serving those requests. The goal of this test case is to evaluate how large a
single distributed queue can be in terms of number of clients/servers. Moreover
RPC clients and servers must be distributed evenly across the messaging components

Methodology
^^^^^^^^^^^^

.. code-block:: none

    Start
      * Provision a single RPC server on Target T
      * Provision a single RPC client
      * RPC client issues calls to T using a fixed delay between two messages.
    Repeat:
      * Add additional clients until RPC server CPU utilization reaches >70%
      * Provision another RPC server on T


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following metrics are recorded for each repetition.

========  ==================  =================  ================================
Priority  Value               Measurement Units  Description
========  ==================  =================  ================================
1         Messages rate       msg/sec            Number of calls made by the
                                                 callers per second
                                                 (overall and by client)
2         Latency             ms                 The round-trip latency in
                                                 message processing
2         Latency stddev      ms                 Standard deviation of the latency.
3         Sent                -                  The number of messages sent
                                                 (overall and by client)
3         Processed           -                  The number of messages processed
                                                 (overall and by server)
4         Throughput          bytes/sec          Volume of raw data flowing
                                                 through the bus by unit of time.
========  ==================  =================  ================================

.. note::

    - This test case can be run for RPC call and RPC cast.

    - In the case of RPC *call* tests, throughput and latency should be
      measured from the RPC client (the caller).  For *cast* tests the latency
      and throughput should be measured from the RPC server (since the client
      does not block for ack). More specifically the latency is the time taken
      by a message to reach the server. The throughput will be calculated by
      dividing the total number of messages by the time interval between the
      first message sent by a client and the last message received by a server.

    - Throughput is correlated to the message rate but depends on the actual
      encoding of the message payload. This can be obtained by different means
      e.g: monitoring statistics from the bus itself or estimation based on the
      wired protocol used. This must be specified clearly to allow fair
      comparisons.


Test Case 2: Multiple distributed targets
-----------------------------------------

Description
^^^^^^^^^^^

The objective of the test case is to evaluate how many queues can be
simultaneously active and managed by the messaging middleware.


Methodology
^^^^^^^^^^^^

.. code-block:: none

    Start:
      * Provision a single RPC server on Target T
      * Provision a single RPC client
      * RPC client issues calls to T using a fixed delay between two messages.
    Repeat:
      * Add additional couple (client, server) on another Target.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following metrics are recorded for each repetition.


========  ==================  =================  ================================
Priority  Value               Measurement Units  Description
========  ==================  =================  ================================
1         Messages rate       msg/sec            Number of calls made by the
                                                 callers per second
                                                 (overall and by client)
2         Latency             ms                 The round-trip latency in
                                                 message processing
2         Latency stddev      ms                 Standard deviation of the latency.
3         Sent                -                  The number of messages sent
                                                 (overall and by client)
3         Processed           -                  The number of messages processed
                                                 (overall and by server)
4         Throughput          bytes/sec          Volume of raw data flowing
                                                 through the bus by unit of time.
========  ==================  =================  ================================

.. note::

    This test case can be run for RPC call and RPC cast.

    Note that throughput is less interesting in the case of cast
    messages since it can be artificially high due to the lack of ack.


Test Case 3 : one single large distributed fanout
-------------------------------------------------

Description
^^^^^^^^^^^

The goal of this test case is to evaluate the ability of the message bus to
handle large fanout.

Methodology
^^^^^^^^^^^

.. code-block:: none

    Start:
      * Provision a single RPC server on Target T
      * Provision a single RPC client
      * RPC client issues fanout cast to T:
        - 1 cast every second
        - n messages
    Repeat:
      * Add additional RPC server on T

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following metrics are recorded for each repetition.

========  ==================  =================  ================================
Priority  Value               Measurement Units  Description
========  ==================  =================  ================================
1         Latency             ms                 Latency
2         Sent                -                  The number of messages sent
                                                 (overall and by client)
2         Processed           -                  The number of messages processed
                                                 (overall and by server)
========  ==================  =================  ================================

.. note::

    In case of fanout cast, no ack are sent to the sender. The latency will be the
    time interval between the message is sent and the message is received by all the
    servers.

Test Case 4 : multiple distributed fanouts
------------------------------------------

Description
^^^^^^^^^^^

The goal of this test case is to scale the number of fanouts handled by the
message bus.

Methodology
^^^^^^^^^^^

.. code-block:: none

    Start:
      * Provision n RPC servers on Target T
      * Provision a single RPC client
      * RPC client issues fanout cast to T:
        - 1 cast every second
        - m messages
    Repeat:
      * Add (n RPC servers, 1 RPC client) on another Target

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following metrics are recorded for each repetition.

========  ==================  =================  ================================
Priority  Value               Measurement Units  Description
========  ==================  =================  ================================
1         Latency             ms                 Latency
2         Sent                -                  The number of messages sent
                                                 (overall and by client)
2         Processed           -                  The number of messages processed
                                                 (overall and by server)
========  ==================  =================  ================================


.. note::

    In case of fanout cast, no ack are sent to the sender. The latency will be the
    time interval between the message is sent and the message is received by all the
    servers.

Test Case 5 : Resilience
------------------------

Description
^^^^^^^^^^^

Usual centralized solutions offer some solution to increase their scalability
while providing high-availability (e.g RabbitMQ clustering, mirroring). This
kind of solution fit well the one-datacenter case but doesn't cope with the
distributed case where high latency between communicating entities can be
observed. In a massively distributed case, communicating entities may fail more
often (link down, hardware failure). The goal of this test case is to evaluate
the resiliency of the messaging layer to failures.

Methodology
^^^^^^^^^^^

The messaging infrastructure must be configured in such a way as to ensure
functionality can be preserved in the case of loss of any one messaging
component (e.g. three rabbit brokers in a cluster, two alternate paths across a
router mesh, etc.)  Each messaging client must be configured with a fail-over
address for re-connecting to the message bus should its primary connection fail
(see the oslo.messaging documentation for `TransportURL`_ addresses).

The test environment is the same as that for Test Case 1 : One single large
distributed queue, with the caveat that each process comprising the message bus
maintains a steady state CPU load of approximately 50%.  In other words the
test traffic should maintain a reasonable and consistent load on the message
bus without overloading it. Additionally test will be based on RPC call
traffic.  RPC cast traffic is sent "least effort" - cast messages are more
likely to be dropped than calls since there is no return ACKs in the case of
cast.

.. code-block:: none

    Start:
      * Provision the test environment as described above
    Phase 1:
      * reboot one component of the message bus (e.g. a single rabbit broker in
        the cluster)
      * wait until the component recovers and the message bus returns to steady state
    Repeat:
      * Phase 1 for each component of the message bus

    Phase 2:
      * force the failure of one of the TCP connections linking two components
        of the message bus (e.g. the connection between two rabbit brokers in a
        cluster).
      * wait 60 seconds
      * restore the connection
      * wait until message bus stabilizes
    Repeat:
      * Phase 2 for each TCP connection connecting any two message bus
        components.

    Phase 3:
      * force the failure of one of the TCP connections linking one client and
        its connected endpoint
      * wait until client reconnects using one fail-over address
      * restore the connection
    Repeat:
      * Phase 3 for each TCP connection connecting one client and the bus

.. note::

  Message bus backend are likely to offer specific ways to know when a steady
  state is reached after the recovery of one agent (e.g polling RabbitMQ API for
  the cluster status). This must be clearly stated in the test resut.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ===================  =================  ===============================
Priority  Value                Measurement Units  Description
========  ===================  =================  ===============================
1         Call failures        -                  Total number of RPC call
                                                  operations that failed grouped
                                                  by exception type.
2         Reboot recovery      seconds            The average time between a
                                                  component reboot and recovery
                                                  of the message bus
2         Reconnect recovery   seconds            The average time between the
                                                  restoration of an internal
                                                  TCP connection and the recovery
                                                  of the message bus
3         Message duplication  -                  Total number of duplicated
                                                  messages received by the servers.
========  ===================  =================  ===============================

Common metrics to all test cases
--------------------------------

For each agent involved in the communication middleware, metrics about their
resource consumption under load must be gathered.


========  =================  =================  ================================
Priority  Value              Measurement Units  Description
========  =================  =================  ================================
1         CPU load           Mhz                CPU load
2         RAM consumption    Gb                 RAM consumption
3         Opened Connection                     Number of TCP sockets opened
========  =================  =================  ================================


Test Case 6 : Operational testing
----------------------------------

Description
^^^^^^^^^^^

Operational testing intends to evaluate the correct behaviour of a running
OpenStack on top of a specific deployment of the messaging middleware.
This test case aims to measure the correct behaviour of OpenStack
under WAN at messaging plane level. It relies on `rally`_ that runs
loads on the current OpenStack. Then Rally reports can be used to get
time of operations executions and percent of failure to evaluate
OpenStack. The chosen Rally scenarios and those known to be intensive on the
messaging layer (e.g `Neutron scenarios`_ and `Nova scenarios`_).


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since `rally`_ is used, the performance metrics are those reported by the
framework.

.. references:
.. _alternative non-broker: https://review.openstack.org/#/c/314603
.. _ombt2: https://github.com/kgiusti/ombt
.. _simulator: https://github.com/openstack/oslo.messaging/blob/master/tools/simulator.py
.. _enoslib: https://github.com/BeyondTheClouds/enoslib
.. _rally: https://github.com/openstack/rally
.. _Neutron scenarios: https://github.com/openstack/rally/tree/0aa2f58e43ff143a27880b5fa527b09c7670d5f7/samples/tasks/scenarios/neutron
.. _Nova scenarios: https://github.com/openstack/rally/tree/0aa2f58e43ff143a27880b5fa527b09c7670d5f7/samples/tasks/scenarios/nova
.. _TransportURL: https://docs.openstack.org/oslo.messaging/latest/reference/transport.html
.. _tc: http://www.tldp.org/HOWTO/html_single/Traffic-Control-HOWTO/
.. _os_faults: https://github.com/openstack/os-faults


Reports
=======


