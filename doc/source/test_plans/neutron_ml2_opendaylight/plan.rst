.. _neutron_ml2_opendaylight:

===================================
Neutron ML2/ODL Performance testing
===================================

:status: **draft**
:version: 1.0

:Abstract:

  This document describes how control plane and network data plane performance
  testing is conducted on an OpenStack Cloud using the Neutron ML2/ODL plugin.
  The control plane performance is going to be  analyzed in terms of response time
  and the parameters used to characterize the data plane performance are throughput
  in Mbps and latency in milliseconds and number of Request-Response Transactions.



Test Plan
=========

Characterize the resource consumption, control plane response time and
network performance of an OpenStack Cloud using the Neutron ML2/ODL Plugin.
Control plane response time is measured when creating and listing common Neutron
resources as well as during actions that require interaction between Neutron and
other OpenStack services such as Nova. Network plane performance is measured for
both TCP and UDP protocols, with throughput, latency and Request-Response
benchmarks for TCP and Packets Per Second (PPS) and loss for UDP.


Test Environment
----------------

Preparation
^^^^^^^^^^^
TripleO is the vehicle used for deploying OpenStack with the ML2/ODL Neutron
Plugin.

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
| model     | Dell PowerEdge r630                                        |
+-----------+------------------------------------------------------------+
| CPU       | 2xIntel(R) Xeon(R) E5-2683(28Cores/56Threads)              |
+-----------+------------------------------------------------------------+
| Memory    | 126 GB                                                     |
+-----------+------------------------------------------------------------+
| Disk      | 2 x 1TB SATA                                               |
+-----------+------------------------------------------------------------+
| Network   | 1 x Intel X710 Quad Port 10G                               |
+-----------+------------------------------------------------------------+

Controller

+-----------+------------------------------------------------------------+
| Parameter | Value                                                      |
+-----------+------------------------------------------------------------+
| model     | Dell PowerEdge r630                                        |
+-----------+------------------------------------------------------------+
| CPU       | 2xIntel(R) Xeon(R) E5-2683(28Cores/56Threads)              |
+-----------+------------------------------------------------------------+
| Memory    | 126 GB                                                     |
+-----------+------------------------------------------------------------+
| Disk      | 2 x 1TB SATA                                               |
+-----------+------------------------------------------------------------+
| Network   | 1 x Intel X710 Quad Port 10G                               |
+-----------+------------------------------------------------------------+

Compute

+-----------+------------------------------------------------------------+
| Parameter | Value                                                      |
+-----------+------------------------------------------------------------+
| model     | Dell PowerEdge r630                                        |
+-----------+------------------------------------------------------------+
| CPU       | 2xIntel(R) Xeon(R) E5-2683(28Cores/56Threads)              |
+-----------+------------------------------------------------------------+
| Memory    | 126 GB                                                     |
+-----------+------------------------------------------------------------+
| Disk      | 2 x 1TB SATA                                               |
+-----------+------------------------------------------------------------+
| Network   | 1 x Intel X710 Quad Port 10G                               |
+-----------+------------------------------------------------------------+



Additional Hardware for testing/monitoring/results

- Performance Monitoring Host (Carbon/Graphite/Grafana)
- Performance Results Host (ElasticSearch/Kibana)

Software
~~~~~~~~
+-----------------+------------+
| Parameter       | Value      |
+-----------------+------------+
| OS              | RHEL 7.3   |
+-----------------+------------+
| OpenStack       | Newton     |
+-----------------+------------+
| Hypervisor      | KVM        |
+-----------------+------------+
| Neutron plugin  | ML2/OVS    |
+-----------------+------------+
| L2 segmentation | VxLAN      |
+-----------------+------------+

System Performance Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Record System performance metrics into a separate metrics
collection/storage/analysis system. Suggested system would be a separate
machine with Carbon, Graphite, and Grafana with dashboards for monitoring
system resource utilization.  To push metrics into the TSDB, collectd
can/should be installed on all monitored machines. (Deployment, Controllers,
and Computes)

Test Case 1
-----------

Description
^^^^^^^^^^^
Create and list Neutron resources such as networks, routers etc and measure the
response time of the API.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ===============  ====================== ===================
Priority  Value            Measurement Units       Description
========  ===============  ====================== ===================
1         Reponse Time            seconds         Time taken for API
                                                  to respond
========  ===============  ====================== ===================

Test Case 2
-----------

Description
^^^^^^^^^^^
Create and list servers on a subnet and compare time taken for server
to go into ACTIVE. This is an important test case as ML2/OVS and
ML2/ODL have both take different approaches when notifying NOVA that
the network is ready.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ===============  ===================== ===================
Priority  Value            Measurement Units       Description
========  ===============  ===================== ===================
1         Reponse Time            seconds         Time taken for API
                                                  to respond
=======  ===============   ===================== ===================


Test Case 3
-----------

Description
^^^^^^^^^^^
Using Browbeat_ to run Shaker_, measure Latency of UDP small packets, TCP
throughput and Request-responses in each of L2, L3-East-West and L3-North-South
Scenarios.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ===============  ===================== ===================
Priority  Value            Measurement Units       Description
========  ===============  ===================== ===================
1         Throughput/       Mbps/Transactions/    Network Performance
          RR/Latency        Seconds
=======  ================  ===================== ===================


Tools
-----
Browbeat_ is used to orchestrate several Rally_ and Shaker_ scenarios and
results are pushed to Elasticsearch for easy visualization through Kibana.

Setup
^^^^^^^^

#. Deploy OpenStack Cloud using TripleO
#. Install testing and monitoring tooling
#. Gather metadata on Cloud
#. Run tests

Analysis
^^^^^^^^

Review System performance metrics graphs during test duration to observe for
stopping/failure conditions. Review testing harness output for test failure
conditions. API response time and several statistics associated with it such as
percentiles can be obtained from Rally and Shaker output. Compare ML2/OVS with
ML2/ODL.

.. references:

.. _Rally: https://github.com/openstack/rally
.. _Shaker: https://github.com/openstack/shaker
.. _Browbeat: https://github.com/openstack/browbeat
