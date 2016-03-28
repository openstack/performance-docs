RabbitMQ performance (Client and Server connected to Master), HA queues enabled
-------------------------------------------------------------------------------

This report contains results of :ref:`message_queue_performance` execution
with `Oslo.messaging Simulator`_. Both simulator client and simulator server
are connected to Master node. `RabbitMQ HA queues`_ are enabled.

.. image:: topology_cmsm_ha.*

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
     - 244710
     - 244710
     - 244710
     - 0
   *
     - 100
     - 223377
     - 223377
     - 223377
     - 0
   *
     - 250
     - 201327
     - 201327
     - 201327
     - 0
   *
     - 350
     - 200093
     - 200093
     - 200093
     - 0
   *
     - 500
     - 169967
     - 169967
     - 169967
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
     - 2393.8
     - 18.7
     - 1487.0
   *
     - 100
     - 2207.5
     - 44.2
     - 1370.3
   *
     - 250
     - 1987.4
     - 124.1
     - 1725.0
   *
     - 350
     - 1967.3
     - 174.9
     - 1717.3
   *
     - 500
     - 1665.8
     - 294.2
     - 1620.1



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
     - 1255.5
     - 122.1
     - 109.4
     - 353.2
     - 33.0
     - 29.2
   *
     - 100
     - 1142.8
     - 118.2
     - 109.3
     - 319.4
     - 29.9
     - 26.7
   *
     - 250
     - 1475.9
     - 127.6
     - 121.5
     - 416.9
     - 32.6
     - 29.5
   *
     - 350
     - 1459.3
     - 129.9
     - 128.1
     - 416.0
     - 32.7
     - 31.1
   *
     - 500
     - 1358.8
     - 128.5
     - 132.7
     - 396.1
     - 32.1
     - 31.1



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
     - 606121
     - 606121
     - 0
   *
     - 100
     - 674586
     - 674586
     - 0
   *
     - 250
     - 463741
     - 463741
     - 0
   *
     - 350
     - 451210
     - 451210
     - 0
   *
     - 500
     - 444167
     - 444167
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
     - 5982.4
     - 5.9
     - 1308.1
   *
     - 100
     - 6669.4
     - 7.8
     - 1716.1
   *
     - 250
     - 4588.7
     - 38.3
     - 1654.5
   *
     - 350
     - 4458.9
     - 57.7
     - 1499.3
   *
     - 500
     - 4363.8
     - 87.2
     - 1568.4


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
     - 1148.3
     - 88.9
     - 70.9
     - 300.9
     - 22.4
     - 18.3
   *
     - 100
     - 1564.5
     - 83.0
     - 68.5
     - 440.5
     - 20.1
     - 16.3
   *
     - 250
     - 1534.4
     - 61.0
     - 59.0
     - 452.4
     - 14.8
     - 14.3
   *
     - 350
     - 1379.4
     - 57.6
     - 62.3
     - 409.6
     - 13.7
     - 15.5
   *
     - 500
     - 1457.8
     - 52.0
     - 58.6
     - 434.2
     - 12.4
     - 15.4


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
     - 589725
     - 589725
     - 0
   *
     - 100
     - 702420
     - 702420
     - 0
   *
     - 250
     - 484577
     - 484561
     - 16
   *
     - 350
     - 467109
     - 467109
     - 0
   *
     - 500
     - 457309
     - 457309
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
     - 5819.5
     - 5.4
     - 1387.3
   *
     - 100
     - 6943.4
     - 7.5
     - 1693.9
   *
     - 250
     - 4794.8
     - 34.0
     - 1729.7
   *
     - 350
     - 4622.3
     - 54.6
     - 1686.4
   *
     - 500
     - 4525.5
     - 88.6
     - 1644.3


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
     - 1220.5
     - 107.3
     - 59.4
     - 319.5
     - 28.4
     - 16.2
   *
     - 100
     - 1531.8
     - 100.8
     - 61.3
     - 427.4
     - 23.7
     - 15.5
   *
     - 250
     - 1609.9
     - 72.9
     - 46.9
     - 476.1
     - 18.2
     - 12.8
   *
     - 350
     - 1573.8
     - 67.1
     - 45.4
     - 466.8
     - 16.5
     - 12.2
   *
     - 500
     - 1529.6
     - 68.8
     - 45.9
     - 455.8
     - 16.8
     - 12.5



.. references:

.. _message_queue_performance: http://docs.openstack.org/developer/performance-docs/test_plans/mq/plan.html
.. _Oslo.messaging Simulator: https://github.com/openstack/oslo.messaging/blob/master/tools/simulator.py
.. _RabbitMQ HA queues: https://www.rabbitmq.com/ha.html