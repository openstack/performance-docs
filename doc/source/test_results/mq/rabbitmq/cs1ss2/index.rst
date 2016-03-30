RabbitMQ performance (Client -> Slave-1, Server -> Slave-2)
-----------------------------------------------------------

This report contains results of :ref:`message_queue_performance` execution
with `Oslo.messaging Simulator`_. Simulator client and simulator server
are connected to different slave nodes. `RabbitMQ HA queues`_ are enabled.

.. image:: topology_cs1ss2.*

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
     - 303108
     - 303108
     - 303108
     - 0
   *
     - 100
     - 530183
     - 530183
     - 530183
     - 0
   *
     - 250
     - 590627
     - 590627
     - 590627
     - 0
   *
     - 350
     - 612468
     - 612468
     - 612468
     - 0
   *
     - 500
     - 687218
     - 687218
     - 687218
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
     - 2992.2
     - 13.6
     - 477.6
   *
     - 100
     - 5219.0
     - 16.2
     - 1432.7
   *
     - 250
     - 5838.8
     - 41.9
     - 1969.2
   *
     - 350
     - 6057.5
     - 56.9
     - 2037.3
   *
     - 500
     - 6798.0
     - 72.6
     - 2216.4



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
     - 59.1
     - 262.2
     - 156.3
     - 16.7
     - 75.1
     - 47.2
   *
     - 100
     - 76.6
     - 1050.6
     - 305.5
     - 20.8
     - 288.4
     - 83.2
   *
     - 250
     - 78.0
     - 1422.6
     - 468.7
     - 21.2
     - 417.0
     - 122.8
   *
     - 350
     - 78.0
     - 1462.2
     - 497.1
     - 20.7
     - 424.5
     - 127.9
   *
     - 500
     - 80.5
     - 1509.7
     - 626.1
     - 21.4
     - 429.2
     - 161.9




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
     - 740756
     - 740756
     - 0
   *
     - 100
     - 981647
     - 981647
     - 0
   *
     - 250
     - 1265226
     - 1265226
     - 0
   *
     - 350
     - 1362716
     - 1362716
     - 0
   *
     - 500
     - 1487540
     - 1487540
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
     - 7293.3
     - 65.0
     - 778.3
   *
     - 100
     - 9691.4
     - 8.3
     - 1530.6
   *
     - 250
     - 12510.6
     - 16.0
     - 1728.8
   *
     - 350
     - 13478.8
     - 21.3
     - 1835.4
   *
     - 500
     - 14713.0
     - 23.8
     - 1712.8


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
     - 110.3
     - 552.9
     - 115.0
     - 31.9
     - 145.8
     - 36.5
   *
     - 100
     - 101.4
     - 1268.7
     - 160.4
     - 25.6
     - 367.8
     - 50.1
   *
     - 250
     - 114.7
     - 1377.1
     - 237.0
     - 29.1
     - 431.5
     - 69.6
   *
     - 350
     - 119.3
     - 1438.2
     - 277.9
     - 32.3
     - 447.6
     - 80.9
   *
     - 500
     - 143.1
     - 1286.0
     - 283.7
     - 39.5
     - 397.7
     - 82.5



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
     - 704253
     - 704253
     - 0
   *
     - 100
     - 965920
     - 965920
     - 0
   *
     - 250
     - 1228602
     - 1228602
     - 0
   *
     - 350
     - 1366766
     - 1366766
     - 0
   *
     - 500
     - 1453842
     - 1453842
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
     - 6932.9
     - 5.0
     - 750.1
   *
     - 100
     - 9532.6
     - 8.1
     - 1548.2
   *
     - 250
     - 12147.7
     - 15.7
     - 1773.8
   *
     - 350
     - 13517.9
     - 19.8
     - 1768.2
   *
     - 500
     - 14378.9
     - 21.7
     - 1799.2


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
     - 99.7
     - 545.0
     - 105.5
     - 27.8
     - 144.0
     - 33.9
   *
     - 100
     - 102.9
     - 1268.6
     - 176.7
     - 29.1
     - 366.7
     - 55.0
   *
     - 250
     - 109.0
     - 1401.5
     - 263.2
     - 30.4
     - 439.0
     - 79.0
   *
     - 350
     - 124.2
     - 1334.0
     - 309.9
     - 34.3
     - 416.0
     - 89.1
   *
     - 500
     - 136.7
     - 1330.6
     - 332.0
     - 37.6
     - 411.1
     - 93.3



.. references:

.. _Oslo.messaging Simulator: https://github.com/openstack/oslo.messaging/blob/master/tools/simulator.py
.. _RabbitMQ HA queues: https://www.rabbitmq.com/ha.html
