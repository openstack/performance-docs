
.. _Measuring_performance_of_container_cluster_systems:

**************************************************
Measuring performance of container cluster systems
**************************************************

:status: **ready**
:version: 1.0

:Abstract:

  A complete microservices architecture has the ability to manage a large
  number of small applications   which together form a set of services.
  Container technology provides a way to package and run applications
  independent of the underlying operating system.
  Microservice and container technologies are very complimentary and
  usually used in conjunction.
  There are several container management systems, such as Apache Mesos,
  Kubernetes, and Docker Swarm,
  which provide various ways to manage groups of containers.

Test Plan
=========

Test Environment
----------------

Preparation
^^^^^^^^^^^
Typical container frameworks consist of several components:
 * Configuration and Synchronization (Zookeeper)
 * Scheduler (Mesos)
 * Application manager (Marathon)

Environment description
^^^^^^^^^^^^^^^^^^^^^^^
In this document only performance and scaling aspects of the different
frameworks will be covered.
It is expected that existing solutions will be used and that they have had
sufficient functional testing.
Performance aspects should cover elapsed times for operations used in the
framework.

Test Case #1: A new application creation time
---------------------------------------------

Description
^^^^^^^^^^^
This test is aimed at measuring the total elapsed time of the create
application operation.
This metric includes the time of application submission processing,
time of scheduling,
and time of actual all containers spawning on the slaves hosts.


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +------------------------------+----------------------------------------+
  | Parameter                    | Description                            |
  +==============================+========================================+
  | APPLICATION_OPERATION_MAX    |Maximum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MIN    |Minimum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEAN   |Mean execution time of all operations   |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEDIAN |Median execution time of all operations |
  +------------------------------+----------------------------------------+
.. table:: list of test metrics to be persistent during this test:

  +---------------------------------+--------------------------------+
  | Parameter                       | Value                          |
  +=================================+================================+
  | NODES_NUMBER_PER_APPLICATION    |50, 100, 500                    |
  +---------------------------------+--------------------------------+
  | CONCURRENCY                     |1, 2, 4, 8, 16                  |
  +---------------------------------+--------------------------------+

Measuring values
^^^^^^^^^^^^^^^^
1.
  Start to create simultaneously the number of applications equal CONCURRENCY
  with number of instances equal NODES_NUMBER_PER_APPLICATION  in the each
  application through Marathon API. Every instances is docker container with
  nginx from dockerhub. Every instances has 1 CPU, 256M RAM and 50G disk.
2.
  Wait util all application go to state Running
3.
  As a result of the previous step you should be able to provide the amount of
  graphs and tables with the dependencies on an concurrency and instances
  number of a operation time. One table for all results and graphs for every
  concurrency and every nodes number. On this step you need to
  calculate minimum, maxima, average and median of operation time. You need
  to fill the following table with calculated values:

.. table:: results

  +-------------+------------------------------+--------+--------+---------+--------+
  | CONCURRENCY | NODES_NUMBER_PER_APPLICATION | APPLICATION_OPERATION (sec)        |
  |             |                              +--------+--------+---------+--------+
  |             |                              |minimum |maximum | average | median |
  +=============+==============================+========+========+=========+========+
  |1            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+

Test Case #2: A application CPU update time
-------------------------------------------

Description
^^^^^^^^^^^
This test is aimed at measuring the total elapsed time of the update CPU
application operation. This metric includes the time of application submission
processing, time of scheduling, and time of actual all containers updated on
the slaves hosts.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +------------------------------+----------------------------------------+
  | Parameter                    | Description                            |
  +==============================+========================================+
  | APPLICATION_OPERATION_MAX    |Maximum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MIN    |Minimum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEAN   |Mean execution time of all operations   |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEDIAN |Median execution time of all operations |
  +------------------------------+----------------------------------------+

.. table:: list of test metrics to be persistent during this test:

  +---------------------------------+--------------------------------+
  | Parameter                       | Value                          |
  +=================================+================================+
  | NODES_NUMBER_PER_APPLICATION    |50, 100, 500                    |
  +---------------------------------+--------------------------------+
  | CONCURRENCY                     |1, 2, 4, 8, 16                  |
  +---------------------------------+--------------------------------+

Measuring values
^^^^^^^^^^^^^^^^
1.
  Start to create simultaneously the number of applications equal CONCURRENCY
  with number of instances equal NODES_NUMBER_PER_APPLICATION  in the each
  application through Marathon API. Every instances is docker container with
  nginx from dockerhub. Every instances has 1 CPU, 256M RAM and 50G disk.
2.
  Wait util all application go to state Running
3.
  Update applications CPU up to 2.
4.
  Wait util all application go to state Running
5.
  As a result of the previous step you should be able to provide the amount of
  graphs and tables with the dependencies on an concurrency and instances
  number of a operation time. One table for all results and graphs for every
  concurrency and every nodes number. On this step you need to
  calculate minimum, maxima, average and median of operation time. You need
  to fill the following table with calculated values:

.. table:: results

  +-------------+------------------------------+--------+--------+---------+--------+
  | CONCURRENCY | NODES_NUMBER_PER_APPLICATION | APPLICATION_OPERATION (sec)        |
  |             |                              +--------+--------+---------+--------+
  |             |                              |minimum |maximum | average | median |
  +=============+==============================+========+========+=========+========+
  |1            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+


Test Case #3: A application memory update time
----------------------------------------------

Description
^^^^^^^^^^^
This test is aimed at measuring the total elapsed time of the update memory
application operation. This metric includes the time of application submission
processing, time of scheduling, and time of actual all containers updated on
the slaves hosts.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +------------------------------+----------------------------------------+
  | Parameter                    | Description                            |
  +==============================+========================================+
  | APPLICATION_OPERATION_MAX    |Maximum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MIN    |Minimum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEAN   |Mean execution time of all operations   |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEDIAN |Median execution time of all operations |
  +------------------------------+----------------------------------------+

.. table:: list of test metrics to be persistent during this test:

  +---------------------------------+--------------------------------+
  | Parameter                       | Value                          |
  +=================================+================================+
  | NODES_NUMBER_PER_APPLICATION    |50, 100, 500                    |
  +---------------------------------+--------------------------------+
  | CONCURRENCY                     |1, 2, 4, 8, 16                  |
  +---------------------------------+--------------------------------+

Measuring values
^^^^^^^^^^^^^^^^
1.
  Start to create simultaneously the number of applications equal CONCURRENCY
  with number of instances equal NODES_NUMBER_PER_APPLICATION  in the each
  application through Marathon API. Every instances is docker container with
  nginx from dockerhub. Every instances has 1 CPU, 256M RAM and 50G disk.
2.
  Wait util all application go to state Running
3.
  Update applications memory up to 512M.
4.
  Wait util all application go to state Running
5.
  As a result of the previous step you should be able to provide the amount of
  graphs and tables with the dependencies on an concurrency and instances
  number of a operation time. One table for all results and graphs for every
  concurrency and every nodes number. On this step you need to
  calculate minimum, maxima, average and median of operation time. You need
  to fill the following table with calculated values:

.. table:: results

  +-------------+------------------------------+--------+--------+---------+--------+
  | CONCURRENCY | NODES_NUMBER_PER_APPLICATION | APPLICATION_OPERATION (sec)        |
  |             |                              +--------+--------+---------+--------+
  |             |                              |minimum |maximum | average | median |
  +=============+==============================+========+========+=========+========+
  |1            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+


Test Case #4: A application disk update time
--------------------------------------------

Description
^^^^^^^^^^^
This test is aimed at measuring the total elapsed time of the update disk
application operation. This metric includes the time of application submission
processing, time of scheduling,
and time of actual all containers updated on the slaves hosts.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +------------------------------+----------------------------------------+
  | Parameter                    | Description                            |
  +==============================+========================================+
  | APPLICATION_OPERATION_MAX    |Maximum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MIN    |Minimum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEAN   |Mean execution time of all operations   |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEDIAN |Median execution time of all operations |
  +------------------------------+----------------------------------------+

.. table:: list of test metrics to be persistent during this test:

  +---------------------------------+--------------------------------+
  | Parameter                       | Value                          |
  +=================================+================================+
  | NODES_NUMBER_PER_APPLICATION    |50, 100, 500                    |
  +---------------------------------+--------------------------------+
  | CONCURRENCY                     |1, 2, 4, 8, 16                  |
  +---------------------------------+--------------------------------+

Measuring values
^^^^^^^^^^^^^^^^
1.
  Start to create simultaneously the number of applications equal CONCURRENCY
  with number of instances equal NODES_NUMBER_PER_APPLICATION  in the each
  application through Marathon API. Every instances is docker container with
  nginx from dockerhub. Every instances has 1 CPU, 256M RAM and 50G disk.
2.
  Wait util all application go to state Running
3.
  Update applications disk up to 100G.
4.
  Wait util all application go to state Running
5.
  As a result of the previous step you should be able to provide the amount of
  graphs and tables with the dependencies on an concurrency and instances
  number of a operation time. One table for all results and graphs for every
  concurrency and every nodes number. On this step you need to
  calculate minimum, maxima, average and median of operation time. You need
  to fill the following table with calculated values:

.. table:: results

  +-------------+------------------------------+--------+--------+---------+--------+
  | CONCURRENCY | NODES_NUMBER_PER_APPLICATION | APPLICATION_OPERATION (sec)        |
  |             |                              +--------+--------+---------+--------+
  |             |                              |minimum |maximum | average | median |
  +=============+==============================+========+========+=========+========+
  |1            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+


Test Case #5: A application instances update time
-------------------------------------------------

Description
^^^^^^^^^^^
This test is aimed at measuring the total elapsed time of the update number of
instances application operation.
This metric includes the time of application submission processing, time of
scheduling, and time of actual all containers updated on the slaves hosts.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +------------------------------+----------------------------------------+
  | Parameter                    | Description                            |
  +==============================+========================================+
  | APPLICATION_OPERATION_MAX    |Maximum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MIN    |Minimum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEAN   |Mean execution time of all operations   |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEDIAN |Median execution time of all operations |
  +------------------------------+----------------------------------------+

.. table:: list of test metrics to be persistent during this test:

  +---------------------------------+--------------------------------+
  | Parameter                       | Value                          |
  +=================================+================================+
  | NODES_NUMBER_PER_APPLICATION    |50, 100, 500                    |
  +---------------------------------+--------------------------------+
  | CONCURRENCY                     |1, 2, 4, 8, 16                  |
  +---------------------------------+--------------------------------+

Measuring values
^^^^^^^^^^^^^^^^
1.
  Start to create simultaneously the number of applications equal CONCURRENCY
  with number of instances equal NODES_NUMBER_PER_APPLICATION  in the each
  application through Marathon API. Every instances is docker container with
  nginx from dockerhub. Every instances has 1 CPU, 256M RAM and 50G disk.
2.
  Wait util all application go to state Running
3.
  Update instances up to twice in the each application.
4.
  Wait util all application go to state Running
5.
  As a result of the previous step you should be able to provide the amount of
  graphs and tables with the dependencies on an concurrency and instances
  number of a operation time. One table for all results and graphs for every
  concurrency and every nodes number. On this step you need to
  calculate minimum, maxima, average and median of operation time. You need
  to fill the following table with calculated values:

.. table:: results

  +-------------+------------------------------+--------+--------+---------+--------+
  | CONCURRENCY | NODES_NUMBER_PER_APPLICATION | APPLICATION_OPERATION (sec)        |
  |             |                              +--------+--------+---------+--------+
  |             |                              |minimum |maximum | average | median |
  +=============+==============================+========+========+=========+========+
  |1            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+

Test Case #6: A application restart time
----------------------------------------

Description
^^^^^^^^^^^
This test is aimed at measuring the total elapsed time of the restart
application operation. This metric includes the time of application submission
processing, time of scheduling, and time of actual all containers restarted on
the slaves hosts.


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +------------------------------+----------------------------------------+
  | Parameter                    | Description                            |
  +==============================+========================================+
  | APPLICATION_OPERATION_MAX    |Maximum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MIN    |Minimum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEAN   |Mean execution time of all operations   |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEDIAN |Median execution time of all operations |
  +------------------------------+----------------------------------------+

.. table:: list of test metrics to be persistent during this test:

  +---------------------------------+--------------------------------+
  | Parameter                       | Value                          |
  +=================================+================================+
  | NODES_NUMBER_PER_APPLICATION    |50, 100, 500                    |
  +---------------------------------+--------------------------------+
  | CONCURRENCY                     |1, 2, 4, 8, 16                  |
  +---------------------------------+--------------------------------+

Measuring values
^^^^^^^^^^^^^^^^
1.
  Start to create simultaneously the number of applications equal CONCURRENCY
  with number of instances equal NODES_NUMBER_PER_APPLICATION  in the each
  application through Marathon API. Every instances is docker container with
  nginx from dockerhub. Every instances has 1 CPU, 256M RAM and 50G disk.
2.
  Wait util all application go to state Running
3.
  Restart all applications.
4.
  Wait util all application go to state Running
5.
  As a result of the previous step you should be able to provide the amount of
  graphs and tables with the dependencies on an concurrency and instances
  number of a operation time. One table for all results and graphs for every
  concurrency and every nodes number. On this step you need to
  calculate minimum, maxima, average and median of operation time. You need
  to fill the following table with calculated values:

.. table:: results

  +-------------+------------------------------+--------+--------+---------+--------+
  | CONCURRENCY | NODES_NUMBER_PER_APPLICATION | APPLICATION_OPERATION (sec)        |
  |             |                              +--------+--------+---------+--------+
  |             |                              |minimum |maximum | average | median |
  +=============+==============================+========+========+=========+========+
  |1            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+

Test Case #7: A application delete time
---------------------------------------

Description
^^^^^^^^^^^
This test is aimed at measuring the total elapsed time of the delete
application operation. This metric includes the time of application submission
processing, time of scheduling, and time of actual all containers deleted on
the slaves hosts.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +------------------------------+----------------------------------------+
  | Parameter                    | Description                            |
  +==============================+========================================+
  | APPLICATION_OPERATION_MAX    |Maximum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MIN    |Minimum execution time of one operation |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEAN   |Mean execution time of all operations   |
  +------------------------------+----------------------------------------+
  | APPLICATION_OPERATION_MEDIAN |Median execution time of all operations |
  +------------------------------+----------------------------------------+

.. table:: list of test metrics to be persistent during this test:

  +---------------------------------+--------------------------------+
  | Parameter                       | Value                          |
  +=================================+================================+
  | NODES_NUMBER_PER_APPLICATION    |50, 100, 500                    |
  +---------------------------------+--------------------------------+
  | CONCURRENCY                     |1, 2, 4, 8, 16                  |
  +---------------------------------+--------------------------------+

Measuring values
^^^^^^^^^^^^^^^^
1.
  Start to create simultaneously the number of applications equal CONCURRENCY
  with number of instances equal NODES_NUMBER_PER_APPLICATION  in the each
  application through Marathon API. Every instances is docker container with
  nginx from dockerhub. Every instances has 1 CPU, 256M RAM and 50G disk.
2.
  Wait util all application go to state Running
3.
  Delete all applications.
4.
  Wait util list of application return empty list.
5.
  As a result of the previous step you should be able to provide the amount of
  graphs and tables with the dependencies on an concurrency and instances
  number of a operation time. One table for all results and graphs for every
  concurrency and every nodes number. On this step you need to
  calculate minimum, maxima, average and median of operation time. You need
  to fill the following table with calculated values:

.. table:: results

  +-------------+------------------------------+--------+--------+---------+--------+
  | CONCURRENCY | NODES_NUMBER_PER_APPLICATION | APPLICATION_OPERATION (sec)        |
  |             |                              +--------+--------+---------+--------+
  |             |                              |minimum |maximum | average | median |
  +=============+==============================+========+========+=========+========+
  |1            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |1            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |2            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |4            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |8            | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 50                           |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 100                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+
  |16           | 500                          |        |        |         |        |
  +-------------+------------------------------+--------+--------+---------+--------+


Test Case #8: Health check Performance
--------------------------------------

Description
^^^^^^^^^^^
This test is aimed at validating the response time of a health check when many
health checks are configured.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +---------------------------------------------------+----------------------------------------+
  | Parameter                                         | Description                            |
  +===================================================+========================================+
  | HEALTH_CHECK_INTERVAL_DEVIATION(CONTAINERS_COUNT) | | Difference between real health check |
  |                                                   | | interval and configured value        |
  +---------------------------------------------------+----------------------------------------+

.. table:: list of test metrics to be persistent during this test:

  +---------------------------------+--------------------------------+
  | Parameter                       | Value                          |
  +=================================+================================+
  | HEALTH_CHECK_TEST_DURATION      | 20                             |
  +---------------------------------+--------------------------------+
  | HEALTH_CHECK_INTERVAL           | 30                             |
  +---------------------------------+--------------------------------+

Measuring REAL_INTERVAL(TASK_COUNT) values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.
  Deploy Marathon cluster from scratch.
2.
  Run CONTAINERS_COUNT containers in container cluster system. Setup health
  check for those containers in container cluster system with health check
  interval is set to HEALTH_CHECK_INTERVAL seconds.
3.
  Gather HEALTH_CHECK_INTERVAL_DEVIATION from containers during
  HEALTH_CHECK_TEST_DURATION minutes.
4.
  You need to perform step 2 and step 3 per each CONTAINERS_COUNT value from
  the following list:

  * CONTAINERS_COUNT=2500
  * CONTAINERS_COUNT=5000
  * CONTAINERS_COUNT=7500
  * CONTAINERS_COUNT=10000
  * CONTAINERS_COUNT=12500
  * CONTAINERS_COUNT=15000
  * CONTAINERS_COUNT=17500
  * CONTAINERS_COUNT=20000

3.
    As a result of the previous step you should be able to provide table with
    the dependences on an health check interval deviation of a containers
    count. You need to calculate minimuml, maximal, average and 95% percental
    of HEALTH_CHECK_INTERVAL_DEVIATION parameter per each CONTAINERS_COUNT
    value. You need to fill the following table with calculated values:

  .. table:: PUSH_TIME(CONCURRENCY)

    +------------------+---------+---------+---------+-----+
    | CONTAINERS_COUNT | HEALTH_CHECK_INTERVAL_DEVIATION   |
    |                  +---------+---------+---------+-----+
    |                  | minimum | maximal | average | 95% |
    +==================+=========+=========+=========+=====+
    |                  |         |         |         |     |
    +------------------+---------+---------+---------+-----+

Applications
============

list of container platforms
---------------------------

+-----------------------------+---------+
| Name of container platform  | Version |
+=============================+=========+
| Apache Mesos                |         |
+-----------------------------+---------+
| Marathon                    |         |
+-----------------------------+---------+
| Docker                      |         |
+-----------------------------+---------+

Reports
=======

Test plan execution reports:
 * :ref:`Results_of_measuring_performance_of_Mesos_Marathon`
