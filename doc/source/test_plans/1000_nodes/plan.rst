.. _1000_nodes:

===========================================================
1000 Compute nodes resource consumption/scalability testing
===========================================================

:status: **ready**
:version: 1.0

:Abstract:

  This document describes a test plan for measuring OpenStack services
  resources consumption along with scalability potential. It also provides
  a results which could be used to find bottlenecks and/or potential pain
  points for scaling standalone OpenStack services and OpenStack cloud itself.

Test Plan
=========

Most of current OpenStack users wonder how it will behave on scale with a lot
of compute nodes. This is a valid concern because OpenStack have a lot of
services whose have different load and resources consumptions patterns.
Most of the cloud operations are related to the two things: workloads placement
and simple control/data plane management for them.
So the main idea of this test plan is to create simple workloads (10-30k of
VMs) and observe how core services working with them and what is resources
consumption during active workloads placement and some time after that.

Test Environment
----------------

Test assumes that each and every service will be monitored separately for
resources consuption using known techniques like atop/nagios/containerization
and any other toolkits/solutions which will allow to:

1. Measure CPU/RAM consumption of process/set of processes.
2. Separate services and provide them as much as possible resources available
   to fulfill their needs.

List of mandatory services for OpenStack testing:
  nova-api
  nova-scheduler
  nova-conductor
  nova-compute
  glance-api
  glance-registry
  neutron-server
  keystone-all

List of replaceable but still mandatory services:
  neutron-dhcp-agent
  neutron-ovs-agent
  rabbitmq
  libvirtd
  mysqld
  openvswitch-vswitch

List of optional service which may be omitted with performance decrease:
  memcached

List of optional service which may be omitted:
  horizon

Rally fits here as a pretty stable and reliable load runner. Monitoring could be
done by any suitable software which will be able to provide a results in a form
which allow to build graphs/visualize resources consumption to analyze them or
do the analysis automatically.

Preparation
^^^^^^^^^^^

**Common preparation steps**

To begin testing environment should have all the OpenStack services up and
running. Of course they should be configured accordingly to the recommended
settings from release and/or for your specific environment or use case.
To have real world RPS/TPS/etc metrics all the services (including compute
nodes) should be on the separate physical servers but again it depends on
setup and requirements. For simplicity and testing only control plane the
Fake compute driver could be used.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers,
network parameters, operation system and OpenStack deployment characteristics.

Hardware
~~~~~~~~

This section contains list of all types of hardware nodes.

+-----------+-------+----------------------------------------------------+
| Parameter | Value | Comments                                           |
+-----------+-------+----------------------------------------------------+
| model     |       | e.g. Supermicro X9SRD-F                            |
+-----------+-------+----------------------------------------------------+
| CPU       |       | e.g. 6 x Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz |
+-----------+-------+----------------------------------------------------+

Network
~~~~~~~

This section contains list of interfaces and network parameters.
For complicated cases this section may include topology diagram and switch
parameters.

+------------------+-------+-------------------------+
| Parameter        | Value | Comments                |
+------------------+-------+-------------------------+
| card model       |       | e.g. Intel              |
+------------------+-------+-------------------------+
| driver           |       | e.g. ixgbe              |
+------------------+-------+-------------------------+
| speed            |       | e.g. 10G or 1G          |
+------------------+-------+-------------------------+

Software
~~~~~~~~

This section describes installed software.

+-------------------+--------+---------------------------+
| Parameter         | Value  | Comments                  |
+-------------------+--------+---------------------------+
| OS                |        | e.g. Ubuntu 14.04.3       |
+-------------------+--------+---------------------------+
| DB                |        | e.g. MySQL 5.6            |
+-------------------+--------+---------------------------+
| MQ broker         |        | e.g. RabbitMQ v3.4.25     |
+-------------------+--------+---------------------------+
| OpenStack release |        | e.g. Liberty              |
+-------------------+--------+---------------------------+


Configuration
~~~~~~~~~~~~~

This section describes configuration of OpenStack and core services

+-------------------+-------------------------------+
| Parameter         | File                          |
+-------------------+-------------------------------+
| Keystone          |   ./results/keystone.conf     |
+-------------------+-------------------------------+
| Nova-api          |   ./results/nova-api.conf     |
+-------------------+-------------------------------+
| ...               +                               |
+-------------------+-------------------------------+



Test Case 1: Resources consumption under severe load
----------------------------------------------------


Description
^^^^^^^^^^^

This test should spawn a number of instances in n parallel threads and along
with that record all CPU/RAM metrics from all the OpenStack and core services
like MQ brokers and DB server. As test itself is pretty long there is no need
in very high test resolution. 1 measure per 5 seconds should be more than
enough.

Rally scenario that creates load of 50 parallel threads spawning VMs and
calling for VMs list can be found in test plan folder and can be used for
testing purposes. It could be modified to fit specific deployment needs.


Parameters
^^^^^^^^^^

============================  ====================================================
Parameter name                Value
============================  ====================================================
OpenStack release             Liberty, Mitaka

Compute nodes amount          50,100,200,500,1000,2000,5000,10000

Services configurations       Configuration for each OpenStack and core service
============================  ====================================================

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test case result is presented as a weighted tree structure with operations
as nodes and time spent on them as node weights for every control plane
operation under the test. This information is automatically gathered in
Ceilometer and can be gracefully transformed to the human-friendly report via
OSprofiler.

========  ===============  =================  =================================
Priority  Value            Measurement Units  Description
========  ===============  =================  =================================
1         CPU load         Mhz                CPU load for each OpenStack
                                              service
2         RAM consumption  Gb                 RAM consumption for each
                                              OpenStack service
3         Instances amnt   Amount             Max number of instances spawned
4         Operation time   milliseconds       Time spent for every instance
                                              spawn
========  ===============  =================  =================================

Reports
=======

Test plan execution reports:
 * :ref:`1000_nodes_report`
