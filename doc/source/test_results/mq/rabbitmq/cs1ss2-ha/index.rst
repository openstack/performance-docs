RabbitMQ performance (Client -> Slave-1, Server -> Slave-2), HA queues enabled
------------------------------------------------------------------------------

This report contains results of :ref:`message_queue_performance` execution
with `Oslo.messaging Simulator`_. Simulator client and simulator server
are connected to different slave nodes. `RabbitMQ HA queues`_ are enabled.

.. image:: topology_cs1ss2_ha.*

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
     - 286874
     - 286874
     - 286874
     - 0
   *
     - 100
     - 335274
     - 335274
     - 335274
     - 0
   *
     - 250
     - 227804
     - 227830
     - 227804
     - 0
   *
     - 350
     - 238445
     - 238445
     - 238445
     - 0
   *
     - 500
     - 168374
     - 167229
     - 168374
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
     - 2814.8
     - 15.1
     - 1229.4
   *
     - 100
     - 3275.9
     - 29.3
     - 1546.0
   *
     - 250
     - 2253.5
     - 87.7
     - 1981.4
   *
     - 350
     - 2358.5
     - 146.7
     - 1901.1
   *
     - 500
     - 1650.2
     - 238.2
     - 2260.0



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
     - 210.9
     - 659.8
     - 358.8
     - 57.5
     - 170.0
     - 90.0
   *
     - 100
     - 201.4
     - 944.7
     - 399.9
     - 50.9
     - 243.7
     - 95.8
   *
     - 250
     - 182.7
     - 1229.5
     - 569.2
     - 45.2
     - 333.2
     - 142.5
   *
     - 350
     - 172.0
     - 1297.6
     - 431.6
     - 44.0
     - 367.9
     - 107.5
   *
     - 500
     - 157.0
     - 1369.8
     - 733.1
     - 39.6
     - 391.3
     - 195.2



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
     - 481721
     - 481721
     - 0
   *
     - 100
     - 566495
     - 566495
     - 0
   *
     - 250
     - 557957
     - 557957
     - 0
   *
     - 350
     - 420309
     - 420296
     - 13
   *
     - 500
     - 497506
     - 497506
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
     - 4760.2
     - 5.5
     - 896.5
   *
     - 100
     - 5602.8
     - 12.3
     - 1124.2
   *
     - 250
     - 5520.7
     - 12.8
     - 1443.0
   *
     - 350
     - 4157.7
     - 7.5
     - 1448.2
   *
     - 500
     - 4922.2
     - 11.8
     - 1450.0


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
     - 177.5
     - 549.1
     - 169.9
     - 53.8
     - 137.0
     - 44.9
   *
     - 100
     - 177.8
     - 727.4
     - 218.9
     - 50.3
     - 187.1
     - 56.1
   *
     - 250
     - 171.7
     - 1061.9
     - 209.3
     - 46.8
     - 292.8
     - 55.7
   *
     - 350
     - 163.9
     - 1074.6
     - 209.6
     - 43.9
     - 302.0
     - 57.1
   *
     - 500
     - 148.8
     - 1050.9
     - 250.3
     - 39.8
     - 297.5
     - 67.8


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
     - 488810
     - 488810
     - 0
   *
     - 100
     - 481277
     - 481277
     - 0
   *
     - 250
     - 541306
     - 541306
     - 0
   *
     - 350
     - 537552
     - 537552
     - 0
   *
     - 500
     - 483554
     - 483554
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
     - 4830.8
     - 9.7
     - 931.2
   *
     - 100
     - 4761.0
     - 20.4
     - 804.5
   *
     - 250
     - 5356.1
     - 39.0
     - 1249.1
   *
     - 350
     - 5319.3
     - 51.8
     - 1298.8
   *
     - 500
     - 4785.1
     - 38.1
     - 1420.2


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
     - 155.6
     - 542.5
     - 233.1
     - 44.1
     - 138.1
     - 61.5
   *
     - 100
     - 154.8
     - 441.1
     - 208.6
     - 43.1
     - 111.6
     - 53.0
   *
     - 250
     - 152.4
     - 848.6
     - 248.1
     - 40.7
     - 226.1
     - 61.3
   *
     - 350
     - 150.5
     - 902.3
     - 246.0
     - 40.4
     - 240.5
     - 62.5
   *
     - 500
     - 156.4
     - 1020.9
     - 242.9
     - 41.9
     - 287.9
     - 61.0



.. references:

.. _message_queue_performance: http://docs.openstack.org/developer/performance-docs/test_plans/mq/plan.html
.. _Oslo.messaging Simulator: https://github.com/openstack/oslo.messaging/blob/master/tools/simulator.py
.. _RabbitMQ HA queues: https://www.rabbitmq.com/ha.html
