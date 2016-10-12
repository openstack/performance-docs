
.. _Measuring_performance_of_Kargo:

=============================================
Measuring performance of Kargo
=============================================

:status: **ready**
:version: 1.0

:Abstract:

  This document describes a test plan for quantifying the performance of
  Kargo as a one of the Kubernetes deployment solutions. Kargo comes with
  Fuel Containerized Control Plane installer and intended to be fast,
  scalable and reliable K8S deployment tool. Its code mostly implemented
  as a set of ansible playbooks with some bash launcher scripts.
  

Test Plan
=========

This test plan aims to get overall performance, timing and resource
utilization during K8S deployment with Kargo on a different number of
nodes, using specified list of performance measurements and tools.

Test Environment
----------------

Preparation
^^^^^^^^^^^

1.
  The following package needs to be installed on the first node in the
  planned K8S cluster in order to collect performance metrics.

.. table:: Software to be installed

  +--------------+---------+-----------------------------------+
  | package name | version | source                            |
  +==============+=========+===================================+
  | `dstat`_     | 0.7.2   | Ubuntu xenial universe repository |
  +--------------+---------+-----------------------------------+

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

Test results MUST include a description of the environment used. The following
items should be included:

- **Hardware configuration of each server.** If virtual machines are used then
  both physical and virtual hardware should be fully documented.
  An example format is given below:

.. table:: Description of server hardware

  +-------+----------------+-------+-------+
  |server |name            |       |       |
  |       +----------------+-------+-------+
  |       |role            |       |       |
  |       +----------------+-------+-------+
  |       |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |operating_system|       |       |
  +-------+----------------+-------+-------+
  |CPU    |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |processor_count |       |       |
  |       +----------------+-------+-------+
  |       |core_count      |       |       |
  |       +----------------+-------+-------+
  |       |frequency_MHz   |       |       |
  +-------+----------------+-------+-------+
  |RAM    |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |amount_MB       |       |       |
  +-------+----------------+-------+-------+
  |NETWORK|interface_name  |       |       |
  |       +----------------+-------+-------+
  |       |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |bandwidth       |       |       |
  +-------+----------------+-------+-------+
  |STORAGE|dev_name        |       |       |
  |       +----------------+-------+-------+
  |       |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |SSD/HDD         |       |       |
  |       +----------------+-------+-------+
  |       |size            |       |       |
  +-------+----------------+-------+-------+

- **Configuration of hardware network switches.** The configuration file from
  the switch can be downloaded and attached.


- **Network scheme.** The plan should show how all hardware is connected and
  how the components communicate. All ethernet/fibrechannel and VLAN channels
  should be included. Each interface of every hardware component should be
  matched with the corresponding L2 channel and IP address.

Test Case
---------

Description
^^^^^^^^^^^

This specific test plan contains only one test case, that needs to be run
step by step on the environments differing list of parameters below.

Parameters
^^^^^^^^^^

=============== ===============
Parameter name  Value
=============== ===============
number of nodes 50, 150, 350
=============== ===============

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below shows the list of test metrics to be collected. The priority
is the relative ranking of the importance of each metric in evaluating the
performance of the system.

.. table:: List of performance metrics

  +--------+-------------------+-------------------+------------------------------------------+
  |Priority| Value             | Measurement Units | Description                              |
  +========+===================+===================+==========================================+
  |        |                   |                   || The elapsed time deploy ready K8S       |
  | 1      | DEPLOYMENT_TIME   | seconds           || cluster on a different number of nodes. |
  |        |                   |                   ||                                         |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || Total incoming/outgoing network         |
  | 2      | NET_ALL           | bit/s             || bandwidth usage as a function of the    |
  |        |                   |                   || number of nodes.                        |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || CPU utilization as a function of the    |
  | 3      | CPU               | percentage        || number of nodes.                        |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || Active memory usage as a function of    |
  | 3      | RAM               | MB                || the number of nodes.                    |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || Storage total read/write IO bandwidth   |
  | 3      | DISK_ALL          | operations/second || as a function of the number of nodes.   |
  +--------+-------------------+-------------------+------------------------------------------+
  
Measuring performance values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.
  Start the collection of CPU, memory, network, and storage metrics on the
  first K8S cluster node. Use the dstat program which can collect all of
  these metrics in CSV format into a log file.
2.
  Launch Kargo which will begin K8S deployment.
3.
  Wait until the deployment process get finished.
4.
  Stop the dstat program.
5.
  Prepare collected data for analysis. dstat provides a large amount of
  information, which can be pruned by saving only the following:

  * "system"[time]. Save as given.

  * 100-"total cpu usage"[idl]. dstat provides only the idle CPU value. CPU
    utilization is calculated by subtracting the idle value from 100%.

  * "memory usage"[used]. dstat provides this value in Bytes.
    This is converted it to Megabytes by dividing by 1024*1024=1048576.

  * "net/total"[send/recv] The total receive and transmit bandwidth
    on the NIC. dstat provides these values in Bytes per second. They are
    converted to Bits per second dividing by 8.

  * "io/total"[read]+"io/total"[writ]. The total read and write storage IO
    bandwidth.

  These values will be graphed and maximum values reported.

  Additional tests will be performed if some anomalous behavior is found.
  These may require the collection of additional performance metrics.

6.
  The result of this part of test will be:

* to provide the following graphs, one for each number of provisioned nodes:

  #) One dependence on one graph.

     * ALL_NET(TIME)     Dependence on time of total network bandwidth usage.

  #) One dependence on one graph.

     * CPU(TIME)         Dependence on time of CPU utilization.

  #) One dependence on one graph.

     * RAM(TIME)         Dependence on time of active memory usage.

  #) One dependence on one graph.

     * ALL_IO(TIME)      Dependence on time of total storage IO bandwidth.


* to calculate following values and describe they in the table with dependency
 to the certain number of nodes:

.. table:: Maximum values of performance metrics

+-----------------------+-----+-----+-----+
| number of nodes       | 50  | 150 | 350 |
+=======================+=====+=====+=====+
| deployment time       |     |     |     |
+-----------------------+-----+-----+-----+
| cpu_usage_max         |     |     |     |
+-----------------------+-----+-----+-----+
| cpu_usage_min         |     |     |     |
+-----------------------+-----+-----+-----+
| cpu_usage_average     |     |     |     |
+-----------------------+-----+-----+-----+
| cpu_usage_percentile  |     |     |     |
| 90%                   |     |     |     |
+-----------------------+-----+-----+-----+
| ram_usage_max         |     |     |     |
+-----------------------+-----+-----+-----+
| ram_usage_min         |     |     |     |
+-----------------------+-----+-----+-----+
| ram_usage_average     |     |     |     |
+-----------------------+-----+-----+-----+
| ram_usage_percentile  |     |     |     |
| 90%                   |     |     |     |
+-----------------------+-----+-----+-----+
| net_all_max           |     |     |     |
+-----------------------+-----+-----+-----+
| net_all_min           |     |     |     |
+-----------------------+-----+-----+-----+
| net_all_average       |     |     |     |
+-----------------------+-----+-----+-----+
| net_all_percentile    |     |     |     |
| 90%                   |     |     |     |
+-----------------------+-----+-----+-----+
| dsk_io_all_max        |     |     |     |
+-----------------------+-----+-----+-----+
| dsk_io_all_min        |     |     |     |
+-----------------------+-----+-----+-----+
| dsk_io_all_average    |     |     |     |
+-----------------------+-----+-----+-----+
| dsk_io_all_percentile |     |     |     |
| 90%                   |     |     |     |
+-----------------------+-----+-----+-----+

.. references:

.. _dstat: http://dag.wiee.rs/home-made/dstat/


Reports
=======

Test plan execution reports:
 * :ref:`Results_of_measuring_performance_of_Kargo`
