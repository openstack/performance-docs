.. _telemetry_scale:

===========================================================
Telemetry Services resource consumption/scalability testing
===========================================================

:status: **draft**
:version: 1.0

:Abstract:

  This document describes how scalability and performance testing is conducted
  on an OpenStack Cloud with a focus on OpenStack Telemetry Services. Currently
  this focuses on Telemetry Services collection/processing of metrics, further
  test cases can be added to scale and performance test other aspects of the
  OpenStack Telemetry Services.


Test Plan
=========

Characterize the resource consumption and application performance of OpenStack
Telemetry Services on an OpenStack Cloud as a workload increases over time.
As the workload is increased, measure System Performance Metrics (CPU, Memory,
Disk, IO) and Application Performance Metrics (responsiveness, health,
utilization, functionality) until desired load is reached or system/application
failures.

Test Environment
----------------

Preparation
^^^^^^^^^^^
Ideally this is run on a newly deployed cloud each time for repeatability
purposes.  Cloud deployment should be documented for each test case / run as
deployment will set many configuration values which will impact performance.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^
The environment description includes hardware specs, software versions, tunings
and configuration of the OpenStack Cloud under test.

Hardware
~~~~~~~~
List details of hardware for each node type here.

Deployment node (Undercloud)

+-----------+------------------------------------------------------------+
| Parameter | Value                                                      |
+-----------+------------------------------------------------------------+
| model     | ex. Dell PowerEdge r610                                    |
+-----------+------------------------------------------------------------+
| CPU       | ex. 2xIntel(R) Xeon(R) X5650 @ 2.67GHz (12Cores/24Threads) |
+-----------+------------------------------------------------------------+
| Memory    | ex. 64GiB (@1333MHz)                                       |
+-----------+------------------------------------------------------------+
| Disk      | ex. 4 x 146GiB 15K SAS Drives in RAID 0                    |
+-----------+------------------------------------------------------------+
| Network   | ex. 2x1Gb/s Broadcom, 2x10Gb/s Intel X520                  |
+-----------+------------------------------------------------------------+

Controller

+-----------+------------------------------------------------------------+
| Parameter | Value                                                      |
+-----------+------------------------------------------------------------+
| model     | ex. Dell PowerEdge r610                                    |
+-----------+------------------------------------------------------------+
| CPU       | ex. 2xIntel(R) Xeon(R) X5650 @ 2.67GHz (12Cores/24Threads) |
+-----------+------------------------------------------------------------+
| Memory    | ex. 64GiB (@1333MHz)                                       |
+-----------+------------------------------------------------------------+
| Disk      | ex. 4 x 146GiB 15K SAS Drives in RAID 0                    |
+-----------+------------------------------------------------------------+
| Network   | ex. 2x1Gb/s Broadcom, 2x10Gb/s Intel X520                  |
+-----------+------------------------------------------------------------+

Compute

+-----------+------------------------------------------------------------+
| Parameter | Value                                                      |
+-----------+------------------------------------------------------------+
| model     | ex. Dell PowerEdge r610                                    |
+-----------+------------------------------------------------------------+
| CPU       | ex. 2xIntel(R) Xeon(R) X5650 @ 2.67GHz (12Cores/24Threads) |
+-----------+------------------------------------------------------------+
| Memory    | ex. 64GiB (@1333MHz)                                       |
+-----------+------------------------------------------------------------+
| Disk      | ex. 4 x 146GiB 15K SAS Drives in RAID 0                    |
+-----------+------------------------------------------------------------+
| Network   | ex. 2x1Gb/s Broadcom, 2x10Gb/s Intel X520                  |
+-----------+------------------------------------------------------------+

Additional Hardware for testing/monitoring/results

- Performance Monitoring Host (Carbon/Graphite/Grafana)
- Performance Results Host (ElasticSearch/Kibana)

Software
~~~~~~~~
Record versions of Linux kernel, Base Operating System (ex. Centos 7.3),
OpenStack version (ex. Newton), OpenStack Packages, testing harness/framework
and any other pertinent software.

Tuning/Configuration
~~~~~~~~~~~~~~~~~~~~
Record deployed configuration, including the following but not limited to

- # of Gnocchi-metricd processes
- # api processes/threads
- api deployed in httpd? (If so include httpd configuration options)
- Backend (file, swift, ceph)
- Ceilometer polling interval
- Other Services worker/process counts (Nova, Neutron, ...)

System Performance Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Record System performance metrics into a separate metrics
collection/storage/analysis system. Suggested system would be a separate
machine with Carbon, Graphite, and Grafana with dashboards for monitoring
system resource utilization.  To push metrics into the TSDB, collectd
can/should be installed on all monitored machines. (Deployment, Controllers,
and Computes)

Test Diagram
~~~~~~~~~~~~
Attach test diagram to display test topology.

Test Case 1
-----------

Description
^^^^^^^^^^^

Boot 50 persisting instances every 1200 seconds until 1000 instances booted
and running in OpenStack cloud.

Parameters

#. Amount of Instances to boot per period (ex. 50)
#. Amount of time to wait between booting periods (ex. 1200 seconds)
#. Maximum number of instances desired for test (ex. 1000)

**Depending upon available hardware, the above parameters will need to adjusted**

Stopping/Failure Conditions

- Max number of instances achieved
- Failure to boot instances
- Failure for Telemetry Services to consume metrics
- Other service failures/errors
- System out of Resources (ex. CPU 100% utilized)

Setup
^^^^^^^^

#. Deploy OpenStack Cloud
#. Install testing and monitoring tooling
#. Gather metadata on Cloud
#. Run test

Analysis
^^^^^^^^

Review System performance metrics graphs during test duration to observe for
stopping/failure conditions. Review testing harness output for test failure
conditions.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Performance

- CPU utilization
- Memory utilization
- Disk IO utilization
- Per-Process CPU/Memory/IO (Gnocchi, Ceilometer, Nova, Swift, Ceph ...)
- Time required to Boot Instances
- Responsiveness of Gnocchi/Ceilometer or services

Failure Conditions

- Errors in log files (Gnocchi, Ceilometer, Nova, Swift, ...)
