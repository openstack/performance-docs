RabbitMQ performance (Client and Server connected to Master)
------------------------------------------------------------

This report contains results of :ref:`message_queue_performance` execution
with `Oslo.messaging Simulator`_. Both simulator client and simulator server
are connected to Master node. `RabbitMQ HA queues`_ are disabled.

.. image:: topology_cmsm.*

Simulator is configured with `eventlet` executor running in 10 threads.
The overall number of threads is calculated as multiplication of eventlet
threads, number of processes and number of used nodes.


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
     - 50
     - 301010
     - 301010
     - 301010
     - 0
   *
     - 100
     - 426252
     - 426252
     - 426252
     - 0
   *
     - 250
     - 518273
     - 518273
     - 518273
     - 0
   *
     - 350
     - 514594
     - 514594
     - 514594
     - 0
   *
     - 500
     - 405731
     - 405898
     - 405731
     - 0



The throughput, latency and RabbitMQ CPU utilization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The chart shows the throughput, latency and CPU utilization by RabbitMQ server
depending on number of concurrent threads.

.. image:: rpc_call_throughput_latency_and_rabbitmq_cpu_utilization_depending_on_thread_count.*


.. list-table:: RPC CALL throughput, latency and RabbitMQ CPU utilization depending on thread count
   :header-rows: 1

   *
     - threads
     - throughput, msg/sec
     - latency, ms
     - RabbitMQ CPU, %
   *
     - 50
     - 2956.7
     - 13.8
     - 835.8
   *
     - 100
     - 4197.8
     - 21.5
     - 1634.4
   *
     - 250
     - 5122.3
     - 47.5
     - 1511.7
   *
     - 350
     - 5088.6
     - 67.5
     - 1406.3
   *
     - 500
     - 3978.6
     - 98.3
     - 1494.8



Detailed RabbitMQ CPU consumption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thus chart shows statistics on RabbitMQ CPU consumption per nodes.

.. image:: rabbitmq_nodes_cpu_consumption_during_rpc_call_load_test.*


.. list-table:: RabbitMQ nodes CPU consumption during RPC CALL load test
   :header-rows: 1

   *
     - threads
     - Master total, %
     - Slave 1 total, %
     - Slave 2 total, %
     - Master sys, %
     - Slave 1 sys, %
     - Slave 2 sys, %
   *
     - 50
     - 820.6
     - 5.8
     - 9.4
     - 210.8
     - 2.0
     - 2.9
   *
     - 100
     - 1618.2
     - 6.6
     - 9.5
     - 483.2
     - 2.1
     - 2.9
   *
     - 250
     - 1496.4
     - 6.2
     - 9.2
     - 443.8
     - 2.2
     - 2.6
   *
     - 350
     - 1390.6
     - 6.1
     - 9.7
     - 406.2
     - 2.0
     - 2.7
   *
     - 500
     - 1479.2
     - 6.6
     - 9.1
     - 432.0
     - 2.2
     - 2.4




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
     - 50
     - 685704
     - 685704
     - 0
   *
     - 100
     - 948844
     - 948844
     - 0
   *
     - 250
     - 625096
     - 625096
     - 0
   *
     - 350
     - 578176
     - 578176
     - 0
   *
     - 500
     - 565903
     - 565903
     - 0



The throughput, latency and RabbitMQ CPU utilization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The chart shows the throughput, latency and CPU utilization by RabbitMQ server
depending on number of concurrent threads.

.. image:: rpc_cast_throughput_latency_and_rabbitmq_cpu_utilization_depending_on_thread_count.*


.. list-table:: RPC CAST throughput, latency and RabbitMQ CPU utilization depending on thread count
   :header-rows: 1

   *
     - threads
     - throughput, msg/sec
     - latency, ms
     - RabbitMQ CPU consumption, %
   *
     - 50
     - 6754.4
     - 47.2
     - 1131.1
   *
     - 100
     - 9372.1
     - 10.9
     - 1518.3
   *
     - 250
     - 6185.0
     - 40.4
     - 1601.9
   *
     - 350
     - 5721.3
     - 61.0
     - 1451.0
   *
     - 500
     - 5570.7
     - 88.8
     - 1486.6


Detailed RabbitMQ CPU consumption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thus chart shows statistics on RabbitMQ CPU consumption per nodes.

.. image:: rabbitmq_nodes_cpu_consumption_during_rpc_cast_load_test.*


.. list-table:: RabbitMQ nodes CPU consumption during RPC CAST load test
   :header-rows: 1

   *
     - threads
     - Master total, %
     - Slave 1 total, %
     - Slave 2 total, %
     - Master sys, %
     - Slave 1 sys, %
     - Slave 2 sys, %
   *
     - 50
     - 1114.4
     - 6.5
     - 10.2
     - 293.6
     - 2.3
     - 2.2
   *
     - 100
     - 1502.3
     - 7.2
     - 8.9
     - 428.2
     - 2.3
     - 2.5
   *
     - 250
     - 1586.1
     - 6.8
     - 9.0
     - 466.0
     - 2.1
     - 2.7
   *
     - 350
     - 1434.9
     - 6.6
     - 9.5
     - 422.2
     - 2.2
     - 3.0
   *
     - 500
     - 1470.8
     - 6.1
     - 9.7
     - 438.0
     - 2.0
     - 3.0



Test Case 3: Notification Throughput Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Message processing
~~~~~~~~~~~~~~~~~~

Messages are collected at 2 points: ``sent`` - messages sent by the client
and ``received`` - messages received by the server. Also the number of lost
messages is calculated. Sizes of messages is based on the distribution of
messages collected on the 100-node cloud.

.. image:: notify_message_count.*


.. list-table:: NOTIFY Message count
   :header-rows: 1

   *
     - threads
     - sent, msg
     - received, msg
     - lost, msg
   *
     - 50
     - 652649
     - 652649
     - 0
   *
     - 100
     - 937191
     - 937191
     - 0
   *
     - 250
     - 622106
     - 622106
     - 0
   *
     - 350
     - 583574
     - 583574
     - 0
   *
     - 500
     - 573813
     - 573813
     - 0



The throughput, latency and RabbitMQ CPU utilization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The chart shows the throughput, latency and CPU utilization by RabbitMQ server
depending on number of concurrent threads.

.. image:: notify_throughput_latency_and_rabbitmq_cpu_utilization_depending_on_thread_count.*


.. list-table:: NOTIFY throughput, latency and RabbitMQ CPU utilization depending on thread count
   :header-rows: 1

   *
     - threads
     - throughput, msg/sec
     - latency, ms
     - RabbitMQ CPU consumption, %
   *
     - 50
     - 6425.6
     - 51.8
     - 1047.9
   *
     - 100
     - 9251.9
     - 10.6
     - 1434.0
   *
     - 250
     - 6155.4
     - 40.5
     - 1625.7
   *
     - 350
     - 5774.5
     - 60.3
     - 1451.2
   *
     - 500
     - 5674.8
     - 87.5
     - 1460.3


Detailed RabbitMQ CPU consumption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thus chart shows statistics on RabbitMQ CPU consumption per nodes.

.. image:: rabbitmq_nodes_cpu_consumption_during_notify_load_test.*


.. list-table:: RabbitMQ nodes CPU consumption during NOTIFY load test
   :header-rows: 1

   *
     - threads
     - Master total, %
     - Slave 1 total, %
     - Slave 2 total, %
     - Master sys, %
     - Slave 1 sys, %
     - Slave 2 sys, %
   *
     - 50
     - 1032.2
     - 6.1
     - 9.6
     - 268.3
     - 2.0
     - 3.0
   *
     - 100
     - 1418.0
     - 6.1
     - 9.9
     - 400.8
     - 2.1
     - 2.9
   *
     - 250
     - 1610.3
     - 6.4
     - 9.1
     - 475.5
     - 2.0
     - 2.8
   *
     - 350
     - 1436.1
     - 6.1
     - 9.0
     - 425.4
     - 1.9
     - 2.6
   *
     - 500
     - 1443.6
     - 6.6
     - 10.1
     - 430.8
     - 2.2
     - 2.9



.. references:

.. _message_queue_performance: http://docs.openstack.org/developer/performance-docs/test_plans/mq/plan.html
.. _Oslo.messaging Simulator: https://github.com/openstack/oslo.messaging/blob/master/tools/simulator.py
.. _RabbitMQ HA queues: https://www.rabbitmq.com/ha.html
