.. _Measuring_performance_of_provisioning_systems:

=============================================
Measuring performance of provisioning systems
=============================================

:status: **ready**
:version: 1.0

:Abstract:

  This document describes a test plan for quantifying the performance of
  provisioning systems as a function of the number of nodes to be provisioned.
  The plan includes the collection of several resource utilization metrics,
  which will be used to analyze and understand the overall performance of each
  system. In particular, resource bottlenecks will either be fixed, or best
  practices developed for system configuration and hardware requirements.

:Conventions:

  - **Provisioning:** is the entire process of installing and configuring an
    operating system.

  - **Provisioning system:** is a service or a set of services which enables
    the installation of an operating system and performs basic operations such
    as configuring network interfaces and partitioning disks. A preliminary
    `list of provisioning systems`_ can be found below in `Applications`_.
    The provisioning system
    can include configuration management systems like Puppet or Chef, but
    this feature will not be considered in this document. The test plan for
    configuration management systems is described in the
    "Measuring_performance_of_configuration_management_systems" document.

  - **Performance of a provisioning system:** is a set of metrics which
    describes how many nodes can be provisioned at the same time and the
    hardware resources required to do so.

  - **Nodes:** are servers which will be provisioned.

Test Plan
=========

This test plan aims to identify the best provisioning solution for cloud
deployment, using specified list of performance measurements and tools.

Test Environment
----------------

Preparation
^^^^^^^^^^^

1.
  The following package needs to be installed on the provisioning system
  servers to collect performance metrics.

.. table:: Software to be installed

  +--------------+---------+-----------------------------------+
  | package name | version | source                            |
  +==============+=========+===================================+
  | `dstat`_     | 0.7.2   | Ubuntu trusty universe repository |
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

- **Configuration of virtual machines and virtual networks (if used).**
  The configuration files can be attached, along with the mapping of virtual
  machines to host machines.

- **Network scheme.** The plan should show how all hardware is connected and
  how the components communicate. All ethernet/fibrechannel and VLAN channels
  should be included. Each interface of every hardware component should be
  matched with the corresponding L2 channel and IP address.

- **Software configuration of the provisioning system.** `sysctl.conf` and any
  other kernel file that is changed from the default should be attached.
  List of installed packages should be attached. Specifications of the
  operating system, network interfaces configuration, and disk partitioning
  configuration should be included. If distributed provisioning systems are
  to be tested then the parts that are distributed need to be described.

- **Desired software configuration of the provisioned nodes.**
  The operating system, disk partitioning scheme, network interface
  configuration, installed packages and other components of the nodes
  affect the amount of work to be performed by the provisioning system
  and thus its performance.

Test Case
---------

Description
^^^^^^^^^^^

This specific test plan contains only one test case, that needs to be run
step by step on the environments differing list of parameters below.

Parameters
^^^^^^^^^^

=============== =========================================
Parameter name  Value
=============== =========================================
number of nodes 10, 20, 40, 80, 160, 320, 640, 1280, 2000
=============== =========================================

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below shows the list of test metrics to be collected. The priority
is the relative ranking of the importance of each metric in evaluating the
performance of the system.

.. table:: List of performance metrics

  +--------+-------------------+-------------------+------------------------------------------+
  |Priority| Value             | Measurement Units | Description                              |
  +========+===================+===================+==========================================+
  |        |                   |                   || The elapsed time to provision all       |
  | 1      | PROVISIONING_TIME | seconds           || nodes, as a function of the numbers of  |
  |        |                   |                   || nodes                                   |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || Incoming network bandwidth usage as a   |
  | 2      | INGRESS_NET       | Gbit/s            || function of the number of nodes.        |
  |        |                   |                   || Average during provisioning on the host |
  |        |                   |                   || where the provisioning system is        |
  |        |                   |                   || installed.                              |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || Outgoing network bandwidth usage as a   |
  | 2      | EGRESS_NET        | Gbit/s            || function of the number of nodes.        |
  |        |                   |                   || Average during provisioning on the host |
  |        |                   |                   || where the provisioning system is        |
  |        |                   |                   || installed.                              |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || CPU utilization as a function of the    |
  | 3      | CPU               | percentage        || number of nodes. Average during         |
  |        |                   |                   || provisioning on the host where the      |
  |        |                   |                   || provisioning system is installed.       |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || Active memory usage as a function of    |
  | 3      | RAM               | GB                || the number of nodes. Average during     |
  |        |                   |                   || provisioning on the host where the      |
  |        |                   |                   || provisioning system is installed.       |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || Storage read IO bandwidth as a          |
  | 3      | WRITE_IO          | operations/second || function of the number of nodes.        |
  |        |                   |                   || Average during provisioning on the host |
  |        |                   |                   || where the provisioning system is        |
  |        |                   |                   || installed.                              |
  +--------+-------------------+-------------------+------------------------------------------+
  |        |                   |                   || Storage write IO bandwidth as a         |
  | 3      | READ_IO           | operations/second || function of the number of nodes.        |
  |        |                   |                   || Average during provisioning on the host |
  |        |                   |                   || where the provisioning system is        |
  |        |                   |                   || installed.                              |
  +--------+-------------------+-------------------+------------------------------------------+

Measuring performance values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The script
`Full script for collecting performance metrics`_
can be used for the first five of the following steps.

.. note::
  If a distributed provisioning system is used, the values need to be
  measured on each provisioning system instance.

1.
  Start the collection of CPU, memory, network, and storage metrics during the
  provisioning process. Use the dstat programm which can collect all of these
  metrics in CSV format into a log file.
2.
  Start the provisioning process for the first node and record the wall time.
3.
  Wait until the provisioning process has finished (when all nodes are
  reachable via ssh) and record the wall time.
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

  * "net/eth0"[recv] receive bandwidth on the NIC. It is converted to Megabits
    per second by dividing by 1024*1024/8=131072.

  * "net/eth0"[send] send bandwidth on the NIC. It is converted to Megabits
    per second by dividing by 1024*1024/8=131072.

  * "net/eth0"[recv]+"net/eth0"[send]. The total receive and transmit bandwidth
    on the NIC. dstat provides these values in Bytes per second. They are
    converted to Megabits per second by dividing by 1024*1024/8=131072.

  * "io/total"[read] storage read IO bandwidth.

  * "io/total"[writ] storage write IO bandwidth.

  * "io/total"[read]+"io/total"[writ]. The total read and write storage IO
    bandwidth.

  These values will be graphed and maximum values reported.

  Additional tests will be performed if some anomalous behaviour is found.
  These may require the collection of additional performance metrics.

6.
  The result of this part of test will be:

* to provide the following graphs, one for each number of provisioned nodes:

  #) Three dependencies on one graph.

     * INGRESS_NET(TIME) Dependence on time of incoming network bandwidth
       usage.
     * EGRESS_NET(TIME)  Dependence on time of outgoing network bandwidth
       usage.
     * ALL_NET(TIME)     Dependence on time of total network bandwidth usage.

  #) One dependence on one graph.

     * CPU(TIME)         Dependence on time of CPU utilization.

  #) One dependence on one graph.

     * RAM(TIME)         Dependence on time of active memory usage.

  #) Three dependencies on one graph.

     * WRITE_IO(TIME)    Dependence on time of storage write IO bandwidth.
     * READ_IO(TIME)     Dependence on time of storage read IO bandwidth.
     * ALL_IO(TIME)      Dependence on time of total storage IO bandwidth.

.. note::
  If a distributed provisioning system is used, the above graphs should be
  provided for each provisioning system instance.

* to fill in the following table for maximum values:

The resource metrics are obtained from the maxima of the corresponding graphs
above. The provisioning time is the elapsed time for all nodes to be
provisioned. One set of metrics will be given for each number of provisioned
nodes.

.. table:: Maximum values of performance metrics

  +-------+--------------+---------+---------+---------+---------+
  || nodes|| provisioning|| maximum|| maximum|| maximum|| maximum|
  || count|| time        || CPU    || RAM    || NET    || IO     |
  |       |              || usage  || usage  || usage  || usage  |
  +=======+==============+=========+=========+=========+=========+
  | 10    |              |         |         |         |         |
  +-------+--------------+---------+---------+---------+---------+
  | 20    |              |         |         |         |         |
  +-------+--------------+---------+---------+---------+---------+
  | 40    |              |         |         |         |         |
  +-------+--------------+---------+---------+---------+---------+
  | 80    |              |         |         |         |         |
  +-------+--------------+---------+---------+---------+---------+
  | 160   |              |         |         |         |         |
  +-------+--------------+---------+---------+---------+---------+
  | 320   |              |         |         |         |         |
  +-------+--------------+---------+---------+---------+---------+
  | 640   |              |         |         |         |         |
  +-------+--------------+---------+---------+---------+---------+
  | 1280  |              |         |         |         |         |
  +-------+--------------+---------+---------+---------+---------+
  | 2000  |              |         |         |         |         |
  +-------+--------------+---------+---------+---------+---------+

Applications
============

List of provisioning systems
----------------------------

.. table:: list of provisioning systems

  +-----------------------------+---------+
  | Name of provisioning system | Version |
  +=============================+=========+
  | `Cobbler`_                  | 2.4     |
  +-----------------------------+---------+
  | `Razor`_                    | 0.13    |
  +-----------------------------+---------+
  | Image based provisioning    |         |
  | via downloading images with | -       |
  | bittorrent protocol         |         |
  +-----------------------------+---------+

Full script for collecting performance metrics
==============================================

.. literalinclude:: measure.sh
    :language: bash

.. references:

.. _dstat: http://dag.wiee.rs/home-made/dstat/
.. _Cobbler: http://cobbler.github.io/
.. _Razor: https://github.com/puppetlabs/razor-server

Reports
=======

Test plan execution reports:
 * :ref:`Measuring_performance_of_Cobbler`
