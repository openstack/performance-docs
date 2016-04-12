MariaDB + Galera performance report
-----------------------------------

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
     - 76531.6
     - 51021.1
     - 3644.3
   *
     - 40
     - 115498.7
     - 76999.3
     - 5499.9
   *
     - 60
     - 119388.4
     - 79592.3
     - 5685.1
   *
     - 80
     - 119065.8
     - 79377.4
     - 5669.7
   *
     - 120
     - 123311.9
     - 82208.2
     - 5871.9
   *
     - 160
     - 103132.3
     - 68755.2
     - 4910.9
   *
     - 200
     - 93633.2
     - 62422.7
     - 4458.5



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
     - 76531.6
     - 660.5
   *
     - 40
     - 115498.7
     - 1170.9
   *
     - 60
     - 119388.4
     - 1555.3
   *
     - 80
     - 119065.8
     - 1775.3
   *
     - 120
     - 123311.9
     - 1959.7
   *
     - 160
     - 103132.3
     - 2128.0
   *
     - 200
     - 93633.2
     - 2170.7



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
     - 3.3
     - 5.5
     - 148.4
   *
     - 40
     - 3.3
     - 7.3
     - 182.4
   *
     - 60
     - 3.5
     - 10.6
     - 349.2
   *
     - 80
     - 3.7
     - 14.1
     - 212.5
   *
     - 120
     - 4.0
     - 20.6
     - 312.5
   *
     - 160
     - 4.4
     - 32.7
     - 284.3
   *
     - 200
     - 3.9
     - 45.1
     - 942.5



.. references:

.. _Sysbench: https://github.com/akopytov/sysbench