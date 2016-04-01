ZeroMQ performance
------------------

This report contains results of :ref:`message_queue_performance` execution
with `Oslo.messaging Simulator`_.

Simulator is configured with `eventlet` executor running in 10 threads.
The overall number of threads is calculated as multiplication of eventlet
threads and number of processes. All processes are executed on the same
physical host.


Environment description
^^^^^^^^^^^^^^^^^^^^^^^

This report is generated for :ref:`message_queue_performance` test plan with
`Oslo.messaging Simulator`_ tool. The data is collected in
:ref:`intel_mirantis_performance_lab`.

Software
~~~~~~~~

+-----------------+--------------------------------------------+
| Parameter       | Value                                      |
+-----------------+--------------------------------------------+
| OS              | Ubuntu 14.04.3                             |
+-----------------+--------------------------------------------+
| oslo.messaging  | 4.5.1 with ZMQ driver                      |
+-----------------+--------------------------------------------+
| Redis           | 2.8.4                                      |
+-----------------+--------------------------------------------+


Test Case 1: RPC CALL Throughput Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Message processing
~~~~~~~~~~~~~~~~~~

Messages are collected at 3 points: ``sent`` - messages sent by the client,
``received`` - messages received by the server, ``round-trip`` - replies
received by the client. Also the number of lost messages is calculated.
Sizes of messages is based on the distribution of messages collected on
the 100-node cloud.

.. image:: rpc_call_message_count.*


.. list-table:: RPC CALL Message count
   :header-rows: 1

   *
     - threads
     - sent, msg
     - received, msg
     - round-trip, msg
     - lost, msg
   *
     - 10
     - 243452
     - 243452
     - 243452
     - 0
   *
     - 20
     - 493979
     - 493979
     - 493979
     - 0
   *
     - 50
     - 1182805
     - 1182805
     - 1182805
     - 0
   *
     - 70
     - 1461209
     - 1461209
     - 1461209
     - 0
   *
     - 100
     - 1917207
     - 1917207
     - 1917207
     - 0
   *
     - 120
     - 2026038
     - 2026038
     - 2026038
     - 0
   *
     - 150
     - 2462634
     - 2462634
     - 2462634
     - 0
   *
     - 170
     - 2638116
     - 2638116
     - 2638116
     - 0
   *
     - 200
     - 2801776
     - 2801776
     - 2801776
     - 0



The throughput and latency
~~~~~~~~~~~~~~~~~~~~~~~~~~

The chart shows the throughput, latency and CPU utilization by RabbitMQ server
depending on number of concurrent threads.

.. image:: rpc_call_throughput_and_latency_depending_on_thread_count.*


.. list-table:: RPC CALL throughput and latency depending on thread count
   :header-rows: 1

   *
     - threads
     - throughput, msg/sec
     - latency, ms
   *
     - 10
     - 2407.3
     - 3.8
   *
     - 20
     - 4884.5
     - 3.8
   *
     - 50
     - 11695.7
     - 3.9
   *
     - 70
     - 14449.7
     - 4.5
   *
     - 100
     - 18955.8
     - 4.9
   *
     - 120
     - 20022.2
     - 5.5
   *
     - 150
     - 24335.8
     - 5.7
   *
     - 170
     - 26069.3
     - 6.0
   *
     - 200
     - 27680.0
     - 6.6



Test Case 2: RPC CAST Throughput Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Message processing
~~~~~~~~~~~~~~~~~~

Messages are collected at 2 points: ``sent`` - messages sent by the client
and ``received`` - messages received by the server. Also the number of lost
messages is calculated. Sizes of messages is based on the distribution of
messages collected on the 100-node cloud.

.. image:: rpc_cast_message_count.*


.. list-table:: RPC CAST Message count
   :header-rows: 1

   *
     - threads
     - sent, msg
     - received, msg
     - lost, msg
   *
     - 10
     - 194036
     - 194036
     - 0
   *
     - 20
     - 387997
     - 387997
     - 0
   *
     - 50
     - 971124
     - 971124
     - 0
   *
     - 70
     - 1360370
     - 1360370
     - 0
   *
     - 100
     - 1938276
     - 1938276
     - 0
   *
     - 120
     - 2303417
     - 2303417
     - 0
   *
     - 150
     - 2869428
     - 2869428
     - 0
   *
     - 170
     - 3233841
     - 3233841
     - 0
   *
     - 200
     - 2681203
     - 2681203
     - 0



The throughput and latency
~~~~~~~~~~~~~~~~~~~~~~~~~~

The chart shows the throughput, latency and CPU utilization by RabbitMQ server
depending on number of concurrent threads.

.. image:: rpc_cast_throughput_and_latency_depending_on_thread_count.*


.. list-table:: RPC CAST throughput and latency depending on thread count
   :header-rows: 1

   *
     - threads
     - throughput, msg/sec
     - latency, ms
   *
     - 10
     - 1920.0
     - 0.7
   *
     - 20
     - 3839.8
     - 0.7
   *
     - 50
     - 9610.8
     - 0.7
   *
     - 70
     - 13463.1
     - 0.8
   *
     - 100
     - 19181.4
     - 1.0
   *
     - 120
     - 22789.0
     - 1.2
   *
     - 150
     - 28388.6
     - 1.4
   *
     - 170
     - 31993.5
     - 1.5
   *
     - 200
     - 26481.6
     - 385.8


Test Case 3: Notification Throughput Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   The execution of this test case was skipped due to unstable work of
   oslo.messaging simulator with ZMQ driver.


.. references:

.. _Oslo.messaging Simulator: https://github.com/openstack/oslo.messaging/blob/master/tools/simulator.py
