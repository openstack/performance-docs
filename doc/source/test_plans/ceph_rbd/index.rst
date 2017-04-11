.. _ceph_rbd_test_plan:

============================
Ceph RBD performance testing
============================

:status: **ready**
:version: 1.0

:Abstract:

  This test plan aims to provide set of tests to identify Ceph RBD
  performance against given Ceph cluster by using of Wally tests.

Test Plan
=========

The purpose of this document is to describe the environment and performance test plan
for benchmarking Ceph block storage (RBD) performance.

The main goals are:

- Define test approach, methodology and benchmarking toolset for testing Ceph
  block storage performance
- Benchmark Ceph performance for defined scenarios

Preparation
-----------

This test plan is performed against existing Ceph cluster.
Single VM is created for running tests on every compute node.
Before running IO load storage devices are filled with pseudo-random data.

Execution Strategy
------------------

All tests are executed sequentially on all dedicated virtual machines. Number of IO load
threads per VM depends on test phase. Every test starts with 30 second warm-up, which
is not included in test results, followed by 180 second test load phase. At any given time
a single VM per compute node generates IO load with given number of threads.

Block size for small block read/write operation is chosen to be 4K, since using smaller
blocks is not reasonable because a) most modern HDD drives have physical sector size
equal to 4KB and b) default Linux virtual memory page size equals to 4KB too. Larger
block sizes provides no additional information since maximal I/O operations per second
value is constant due to HDD mechanics.

Block size for large block sequential read/write operations has no certain limitations
except being bigger than Ceph block size (4MB), so value of 16MB was chosen.

Test tool
---------

For benchmarking Ceph performance new tool (`Wally`_) was developed. It uses Flexible IO
(fio) as load generator.

Test types
----------

Following load scenarios are selected for Ceph benchmarking:

- Average random read IOPS for small (4KB) blocks as function of thread count
- Average random write IOPS for small (4KB) blocks, both for direct and
  synchronous mode, as function of thread count
- Average linear read throughput for large (16MB) blocks, as function of thread
  count
- Average linear write throughput for large (16MB) blocks, as function of thread
  count
- Maximal synchronous random write IOPS for small (4K) blocks with latency not
  exceeding some predefined value.
- Maximal random read IOPS for small (4K) blocks with latency not exceeding some
  predefined value.
- Maximal amount of threads (virtual machines) can be served from storage with
  given SLA.

Every load scenario is executed for different number of simultaneous threads.

Actual values for scenario parameters are defined in section "Load Description"

Disk operations with small block size shows maximum IO operations rate under
sustained load, moving bottleneck to disks, while sequential operations with large block
sizes allows to estimate system performance when bottleneck is network.

Test Measurements and Metrics
-----------------------------

During every test run raw metrics are collected at least once per second. Collected data
are reported after test run. Report should include median value for a metric, 95%
confidence interval and standard deviation value. Charts can be generated for selected
metrics.

Following metrics are collected on each host for all test scenarios:

- CPU usage per core and total
- RAM utilization
- Network throughput and IOPS on both replication and public interfaces
- Throughput, IOPS and latency per storage device for each participating storage
  devices

Following metrics are additionally collected on test VM depending on test type:

- Random read/write tests:

  - Storage IOPS per thread
  - Storage operations latency

- Sequential read/write tests

  - Storage throughput

Expected Results and Pass/Fail Criteria
---------------------------------------

Pass/Fail Criteria
~~~~~~~~~~~~~~~~~~

A test run is considered as failed if one or more test loads is not completed without
errors.

Expected results
~~~~~~~~~~~~~~~~

No certain expected results are provided since the purpose of this testing effort is to
create benchmarking framework and collect baseline data for described environment.

The only requirement is that pass criteria are fulfilled.

However, results difference between test runs by more than 10% for same test
scenarios should be explained. This value is based on test execution experience (results
variation is about 5%).

Load Description
----------------

- Random write in synchronous mode using 4k block size. 1, 5, 10, 15, 25 and 40
  threads
- Random write in direct mode using 4k block size. 1 thread
- Random read using 4k block size. 1, 5, 10, 15, 25, 40, 80 and 120 threads
- Number of VMs conforming SLA (4K block size, 60 MBps, 100 IOPS for
  read/write, 30 ms latency)
- Sequential read, direct, 16m block size, 1, 3 and 10 threads
- Sequential write, direct, 16m block size, 1, 3 and 10 threads

All test loads should be run with default and optimal size of placement groups.

Test Environment
----------------

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers,
network parameters, operation system and Ceph deployment characteristics.

Hardware
~~~~~~~~

This section contains list of all types of hardware nodes (table below is
an example).

+-----------+-------+----------------------------------------------------+
| Parameter | Value | Comments                                           |
+-----------+-------+----------------------------------------------------+
| model     |       | e.g. Supermicro X9SRD-F                            |
+-----------+-------+----------------------------------------------------+
| CPU       |       | e.g. 6 x Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz |
+-----------+-------+----------------------------------------------------+
| role      |       | e.g. compute or network                            |
+-----------+-------+----------------------------------------------------+

Network
~~~~~~~

This section contains list of interfaces and network parameters. For
complicated cases this section may include topology diagram and switch
parameters (table below is an example).

+------------------+-------+-------------------------+
| Parameter        | Value | Comments                |
+------------------+-------+-------------------------+
| network role     |       | e.g. provider or public |
+------------------+-------+-------------------------+
| card model       |       | e.g. Intel              |
+------------------+-------+-------------------------+
| driver           |       | e.g. ixgbe              |
+------------------+-------+-------------------------+
| speed            |       | e.g. 10G or 1G          |
+------------------+-------+-------------------------+
| MTU              |       | e.g. 9000               |
+------------------+-------+-------------------------+
| offloading modes |       | e.g. default            |
+------------------+-------+-------------------------+

Software
~~~~~~~~

This section describes installed software (table below is an example).

+-----------------+-------+---------------------------+
| Parameter       | Value | Comments                  |
+-----------------+-------+---------------------------+
| OS              |       | e.g. Ubuntu 16.04         |
+-----------------+-------+---------------------------+
| Ceph            |       | e.g. Jewel                |
+-----------------+-------+---------------------------+

Reports
=======

Test plan execution reports:

* :ref:`ceph_rbd_performance_results_50_osd`

.. references:

.. _Wally: https://github.com/Mirantis/disk_perf_test_tool
