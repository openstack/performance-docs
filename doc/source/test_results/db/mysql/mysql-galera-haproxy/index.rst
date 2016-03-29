MySQL + Galera + HAproxy performance report
-------------------------------------------

This scenario is executed with `Sysbench`_ tool. There is one instance of
tool per tester node, each running in N threads. Galera cluster is located
behind HAproxy. Tester tools all point to HAProxy endpoint.

.. image:: topology.*


Throughput
^^^^^^^^^^

The following chart shows the number of queries, read queries and transactions
depending on total thread count.

.. image:: throughput.*


.. list-table:: Throughput
   :header-rows: 1

   *
     - threads
     - queries per sec
     - read queries per sec
     - transactions per sec
   *
     - 20
     - 49331.4
     - 32887.6
     - 2349.1
   *
     - 40
     - 56479.8
     - 37653.2
     - 2689.5
   *
     - 60
     - 56265.1
     - 37510.2
     - 2679.2
   *
     - 80
     - 58458.7
     - 38972.5
     - 2783.7
   *
     - 120
     - 55108.4
     - 36739.3
     - 2624.1
   *
     - 160
     - 17298.6
     - 11532.5
     - 823.7
   *
     - 200
     - 11732.2
     - 7821.8
     - 558.5



Throughput and server CPU consumption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following chart shows how DB server CPU consumption depends on number
of concurrent threads and throughput.

.. image:: cpu_consumption.*


.. list-table:: CPU consumption
   :header-rows: 1

   *
     - threads
     - queries per sec
     - CPU, %
   *
     - 20
     - 49331.4
     - 917.4
   *
     - 40
     - 56479.8
     - 1115.2
   *
     - 60
     - 56265.1
     - 1073.0
   *
     - 80
     - 58458.7
     - 1153.9
   *
     - 120
     - 55108.4
     - 1178.3
   *
     - 160
     - 17298.6
     - 2050.1
   *
     - 200
     - 11732.2
     - 2058.9



Operation latency
^^^^^^^^^^^^^^^^^

The following chart shows how operation latency depends on number of 
concurrent threads.

.. image:: latency.*


.. list-table:: Latency
   :header-rows: 1

   *
     - threads
     - min latency, ms
     - avg latency, ms
     - max latency, ms
   *
     - 20
     - 4.8
     - 8.5
     - 23.3
   *
     - 40
     - 6.1
     - 14.9
     - 27.2
   *
     - 60
     - 5.4
     - 22.4
     - 64.8
   *
     - 80
     - 7.3
     - 28.7
     - 78.6
   *
     - 120
     - 9.4
     - 45.7
     - 113.8
   *
     - 160
     - 13.4
     - 194.5
     - 1069.3
   *
     - 200
     - 14.9
     - 358.9
     - 4071.6



.. references:

.. _Sysbench: https://github.com/akopytov/sysbench
