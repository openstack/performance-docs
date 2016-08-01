=====
Tools
=====

In distributed computing systems three basic components of the underlying
telecommunications architecture can be found - **control plane**,
**data plane** and **management plane**, that is commonly considered a subset
of the control plane.

Classically the control plane is defined as the part of a network that carries
signaling traffic and is responsible for routing. Control plane functions
include system configuration and its management. The data plane in this
definition is the part of a network that carries user traffic and, served by
control plane, enables data transfer to and from system clients.

In case of very specific use case - testing of OpenStack clouds - we can treat
these terms in a bit different light.

For cloud technologies and infrastructures (and OpenStack in particular)
we can define control plane as a part of cloud architecture, that is
responsible for cloud resources management, including their on demand
availability, their scheduling, creation, modification and deletion. These
operations are covered by various distributed cloud services, communicating
via their unified APIs. Data plane in general can be considered as all data
operations performed by the workloads on top of OpenStack infrastructure.
In particular, the most common parts are network operations which are
responsible for data transfer over network protocols between running on cloud
VMs or between a VM and the external networks including Internet. Other parts
of Data Plane layer are related to the storage operations which are used by the
workloads to store data on a persistent storage.

All tools listed below are orienting on the cloud-specific definition of
both control plane and data plane layers.

Control Plane (API) testing
===========================

To evaluate cloud control plane performance, it's vital to understand
performance of resource management operations, that are served by cloud APIs.
Therefore, in this section API testing tools will be listed.

JMeter
------

The leader of the pack in awareness is probably **Apache JMeter**. This is an
open-source Java application whose key feature is a powerful and complete GUI
which you use to create test plans. A test plan is composed of test components
which define every piece of the test such as:

* Multiple threads to generate a load
* Parametrizing HTTP requests
* Flexible output results via listeneres interface

This tool is very well established and is probably one of the best tools for
functional load testing. It allows to model complex flows using conditions and
allows to create custom assertions to validate the behavior. It also allows to
simulate non-trivial HTTP scenarios like logging in before the actual HTTP call
to a specific URL or perform file uploads. **JMeter** has a wide and well
established community which produces various plugins to modify and extend the
built-in behaviors. **JMeter** allows to test not only HTTP based API but also
supports various protocols including:

* Web - HTTP and HTTPS
* SOAP and REST API protocols (over HTTP)
* FTP
* Databases via JDBC Java DB interfaces
* LDAP
* Message oriented middleware MOM via JMS • Mail - SMTP, POP3 and IMAP
* MongoDB
* TCP over IP

And last, but not the least, **JMeter** is open source and free. As with every
tool, it has its own limitations and problems. **JMeter** comes with GUI which
has a steep learning curve. It is overloaded with options and concepts which
one should learn before being able to use this tool efficiently. GUI consumes
a lot of compute and memory resources, so, in order to reduce the performance
impact, the GUI can be switched off and tests can be executed in non-GUI mode.
It will require saving the test scenario in an XML formatted file and using CLI
tool to start the test execution. The desired throughput of the requests is
controlled by several parameters of the test scenario and requires fine-tuning
before test execution.

Gatling
-------

**Gatling** is a highly capable load testing tool. It is designed for ease of
use, maintainability, and high performance.

Out of the box, **Gatling** comes with excellent support of the HTTP protocol
that makes it a tool of choice for load testing of any HTTP server (including
OpenStack controllers, as all cloud management processes running on them are
using HTTP APIs to communicate). As the core engine is actually protocol
agnostic, it is perfectly possible to implement support for other protocols.
For example, **Gatling** currently also ships JMS support. Gatling’s
architecture is asynchronous as long as the underlying protocol, such as HTTP,
can be implemented in a non-blocking way. This kind of architecture lets us
implement virtual users as messages instead of dedicated threads, making them
very resource cheap. Thus, running thousands of concurrent virtual users is not
an issue. **Gatling** uses its own DSL for the test scenarios.

Wrk and Apache AB
-----------------

**Wrk** and **Apache AB** are command line tools to test HTTP based resources
written in C. They only provide a command line interface but can generate 
higher HTTP load than tools written in Java or Python.
Apache AB is single threaded and can be extended via plugins (currently plugins for
Kafka and RabbitMQ tests).
`Wrk <https://github.com/wg/wrk>`_ can be multi-threaded and is one of the
most scalable HTTP traffic generator.
`Wrk2 <https://github.com/giltene/wrk2>`_ is a version that has been corrected to
generate very accurate latency measurement.
`A fork of wrk2 <https://github.com/yicwang/wrk2>`_ further provides
compressed latency histograms that are ready to be sent over the network to
any test orchestrator for aggregation.


Rally
-----

**Rally** is a benchmarking tool that was designed specifically for OpenStack
API testing. To make this possible, **Rally** automates and unifies multi-node
OpenStack deployment, cloud verification, benchmarking & profiling. **Rally**
does it in a generic way, making it possible to check whether OpenStack is
going to work well on, say, a 1k-servers installation under high load. The
actual **Rally** core consists of four main components, listed below in the
order they go into action:

* *Server Providers* provide a unified interface for interaction with different
  virtualization technologies (*LXS*, *Virsh* etc.) and cloud suppliers
  (like *Amazon*): it does so via SSH access and in one L3 network
* *Deploy Engines* either deploy some OpenStack distribution (like *DevStack*,
  *Fuel* or others) or use the existing one before any benchmarking procedures
  take place, using servers retrieved from *Server Providers*
* *Verification* runs *Tempest* (or another subunit-based tool) against the
  deployed cloud to check that it works correctly, collects results and
  presents them in a human readable form
* *Benchmark Engine* allows to write parameterized benchmark tasks & run
  them against the cloud (and in fact, it is the most powerful part of this
  framework, that allows to simulate any kind of usual OpenStack control
  plane load)

*Rally* is written in Python language and can easily be extended with plugins
written in Python.

Data Plane testing
==================

For now there is no 100% ready data plane testing tool for OpenStack, that can
cover all possible data workloads, although, there are still options to use
and to improve, to be able to run complex testing data workloads against the
cloud.

VMTP
----

VMTP_ is a data path performance measurement tool built specifically for
OpenStack clouds. It was written to provide a quick, simple and automated way
to get VM-level or host-level single-flow throughput and latency numbers from
any OpenStack cloud and to take into account various Neutron topologies.

*VMTP* is a small Python application that will automatically perform ping
connectivity, round trip time measurement (latency) and TCP/UDP throughput
measurement for the following East/West flows on any OpenStack deployment:

* VM to VM same network (private fixed IP)
* VM to VM different network using fixed IP (same as intra-tenant L3 fixed IP)
* VM to VM different network using floating IP and NAT (same as floating IP
  inter-tenant L3)

Optionally, when an external Linux host is available for testing North/South
flows:

* External host/VM download and upload throughput/latency (L3/floating IP)


For VM-related flows, *VMTP* will automatically create the necessary OpenStack
resources (router, networks, subnets, key pairs, security groups, test VMs)
using the public OpenStack API, install the test tools, then orchestrate
them to gather the throughput measurements then cleanup all related resources
before exiting.

*VMTP* also supports:

* throughput and latency for VMs using SR-IOV
* provider network

.. _VMTP: https://github.com/openstack/vmtp

`VMTP online documentation <http://vmtp.readthedocs.io/>`_


KloudBuster
-----------

While VMTP_ is a single flow measurement tool, KloudBuster_
can load the data plane or storage infrastructure of any OpenStack cloud at
massive scale and measure how well the cloud behaves under load. The
performance data comes from where it matters: the VMs standpoint where cloud
applications run.

KloudBuster *HTTP traffic load*:

    * Can load the data plane with one OpenStack cloud (single-cloud
      operations for L3 East-West scale) or two OpenStack clouds (dual-cloud
      operations with one cloud hosting the HTTP servers and the other loading
      HTTP traffic for L3 North-South scale testing)

    * Can stage any number of tenants, routers, networks, and HTTP
      servers (as many as your cloud can handle)

    * Uses real HTTP servers (Nginx) running in real Linux images (Ubuntu 14.04)

    * Uses high performance and highly scalable HTTP traffic generators (wrk2) to
      simulate huge number of HTTP users and TCP connections (hundreds of
      thousands to millions of concurrent and active connections)

    * Overall throughput aggregation and loss-less millisecond-precision
      latency aggregation for every single HTTP request (typically millions per
      run)

    * Traffic shaping to specify on which links traffic should flow

    * Supports periodic reporting for real-time monitoring and results
      aggregation

KloudBuster *Storage load*:

   * Can launch any number of VMs accessing storage using FIO running inside VMs

   * Supports VM-level Cinder volume (block storage) or Ephemeral disk file I/O
     performance measurement

   * Supports random and sequential file access mode and any mix of read/write,
     block size and queue depth

   * Returns IOPs, bandwidth and loss-less sub millisecond-precision latency
     aggregations for every IO operation (typically millions per run)

   * Supports user configurable workload sequence

*KloudBuster* supports automated progression runs on the VM count (e.g. measure
load for 10 to 100 Vms, in increment of 10 VMs).

Automatic cleanup is performed upon termination to avoid stale resources
leaving in the cloud under test.

*KloudBuster* is accessible to anybody with basic knowledge of OpenStack,
installs in minutes and runs off the box in a fully automated way with sensible
default workloads. Available to run from CLI, REST or Web User Interface... you
pick what works best for you.

.. _KloudBuster: https://github.com/openstack/kloudbuster

`KloudBuster online documentation <http://kloudbuster.readthedocs.io/en/latest/>`_

`Examples of KloudBuster results <http://kloudbuster.readthedocs.io/en/latest/gallery.html>`_


Shaker
------

The Shaker_ tool is a tool used and developed by Mirantis to understand the
Data Plane capabilities of an OpenStack deployment. Data Plane testing helps
cloud administrators understand their deployment from the perspective of the
applications that are using the environment. This tool can be used for
deployment planning, environment verification, and troubleshooting.

Today, *Shaker* focuses on network based tests using iperf to drive load across
the network. *Shaker* has future plans to roll out testing to evaluate I/O and
CPU.

*Shaker* utilizes Heat (OpenStack Orchestration) templates to deploy and
execute Data Plane tests. It deploys a number of agents/compute nodes that all
report back to a centralized *Shaker* server.

The server is executed by *shaker* command and is responsible for deployment of
instances, execution of tests as specified in the scenario, for results
processing and report generation. The agent is light-weight and polls tasks
from the server and replies with the results. Agents have connectivity to the
server, but the server does not (so it is easy to keep agents behind NAT).

*Shaker* runs three types of network tests with many different options
(including TCP and UDP). Below is a summary of the tests and their
characteristics:

* type of the test:
  * VMs in the same network (L2)
  * VMs in a different network (L3 East/West)
  * VMs hitting external IP addresses (L3 North/South)
* communication: either floating IPs or SNAT/internal
* number of VMs: from 1 to *N/2*, where *N* is number of compute nodes
  available
* external hosts to use: static hard coded
* VM placement:
  * one VM per compute
  * two VMs per compute
  * two VMs per compute (different networks)

Shaker L2 Segment Topology
~~~~~~~~~~~~~~~~~~~~~~~~~~

With VMs in the same network (L2 network test), *Shaker* deploys two VMs in the
same network using Heat templates, and runs *iperf* between them, measuring the
single stream network performance between.

Shaker L3 East-West Topology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With VMs in different networks (L3 east/west), *Shaker* deploys two VMs in
different networks using Heat templates, and runs *iperf* between them,
measuring the single stream network performance between them. This will
involve routing and will test the performance of the deployed SDN overlay.

Shaker L3 North-South Topology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The last case is about VMs hitting external IP addresses (L3 north/south).
*Shaker* deploys one of the VMs with an external (floating) IP address, and
runs *iperf* between the some given external node and the VM.


.. _Shaker: https://github.com/openstack/shaker

Rally
-----

Although right now *Rally* is used for control plane testing, there is the
approved blueprint_ for it to support various workloads testing, that means
that in future it will be possible to use *Rally* for all data plane testing
as well.

.. _blueprint: https://blueprints.launchpad.net/rally/+spec/vm-workloads-framework

Browbeat
--------

Browbeat_ is a powerful combination of several upstream tools for performance
testing, tuning, comparison and monitoring of an OpenStack cloud. It uses
Ansible to automate deploying infrastructure such as:

    * Graphite: To serve as a store for system performance metrics being pushed
      from the cloud by *Collectd*
    * Grafana: To visualize the system performance data in Graphite and act as a
      means of actively monitoring the cloud real-time to troubleshoot
      performance bottlenecks
    * ELK Stack:

      * Elasticsearch: To act as a storage backend for performance testing data,
        metadata about how the cloud is setup and log data
      * Logstash: To manage the logs
      * Kibana: To Visualize data from Elasticsearch and aid in performance
        comparison

The tool also sets up *Collectd* on the OpenStack environment so that metrics are
reported to Graphite. All the user needs to do is fill in minimal variables such
as IP address, username, password of the infrastructure hosts and *Browbeat*
will setup the infrastructure hosts and transport system metrics form the
OpenStack environment so that the user can actively monitor the cloud through
Grafana. Dashboards that visualize OpenStack related data can be uploaded to
Grafana by simply running a playbook
Playbooks to deploy containerized Graphite/Grafana are also available.
Metrics such as CPU, memory utilization, process/thread counts of
OpenStack processes along with general system metrics are collected.

Other important features of *Browbeat* are:
    * Check Overcloud and Undercloud for common configuration/tuning errors and
      print out a bug report.
    * Run control/data plane workloads from upstream tools such as Rally, Shaker
      and Perfkit by simply passing a configuration file. *Browbeat*
      orchestrates the entire run to include multiple benchmarks at varying
      concurrencies/configurations and creates a result directory for all results
    * Pushes the results to the Elasticsearch Instance configured, along with
      metadata that represents how the cloud is configured(Nova, Neutron,
      Ceilometer, etc.) so that run-to-run, build-to-build and cloud-to-cloud
      comparisons can be done

.. _Browbeat: https://github.com/openstack/browbeat

