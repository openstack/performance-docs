MySQL + Galera performance report
---------------------------------

This scenario is executed with `Sysbench`_ tool. There is one instance of
tool per tester node, each running in N threads. The tool is configured
to point to one of DB nodes in Galera cluster directly.

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
     - 69112.8
     - 46075.2
     - 3291.1
   *
     - 40
     - 74157.2
     - 49438.2
     - 3531.3
   *
     - 60
     - 67909.4
     - 45273.0
     - 3233.8
   *
     - 80
     - 65218.1
     - 43478.9
     - 3105.6
   *
     - 120
     - 58895.1
     - 39263.7
     - 2804.4
   *
     - 160
     - 57187.0
     - 38125.3
     - 2723.0
   *
     - 200
     - 51120.9
     - 34081.6
     - 2434.0



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
     - 69112.8
     - 1247.3
   *
     - 40
     - 74157.2
     - 1942.5
   *
     - 60
     - 67909.4
     - 2302.5
   *
     - 80
     - 65218.1
     - 2414.2
   *
     - 120
     - 58895.1
     - 2423.0
   *
     - 160
     - 57187.0
     - 2421.0
   *
     - 200
     - 51120.9
     - 2326.0



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
     - 3.2
     - 6.1
     - 19.6
   *
     - 40
     - 3.5
     - 11.4
     - 42.9
   *
     - 60
     - 4.3
     - 18.7
     - 56.5
   *
     - 80
     - 4.1
     - 25.9
     - 155.9
   *
     - 120
     - 4.3
     - 42.8
     - 572.9
   *
     - 160
     - 5.2
     - 58.8
     - 485.3
   *
     - 200
     - 6.6
     - 82.2
     - 745.9



.. references:

.. _Sysbench: https://github.com/akopytov/sysbench
