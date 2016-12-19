.. _openstack_api_workers:

======================================================================
OpenStack API worker performance and scalability testing with Browbeat
======================================================================

:status: **draft**
:version: 1.0

:Abstract:

  The work described in this test plan is to evaluate changes
  that can occure upstream like [1][2], and review the impact of
  API response times due to these changes. This test plan will also seek
  to determine a possible os_worker default that performs close to the
  previous os_worker count.

[1] http://lists.openstack.org/pipermail/openstack-dev/2016-September/104819.html
[2] https://github.com/openstack/puppet-openstacklib/blob/master/lib/facter/os_workers.rb

Test Plan
=========

Test Environment
----------------

Preparation
^^^^^^^^^^^
Ideally this is run on a newly deployed cloud each time for repeatability
purposes. Cloud deployment should be documented for each test case / run as
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
| model     | e.g. Dell PowerEdge r620                                   |
+-----------+------------------------------------------------------------+
| CPU       | e.g. 2xIntel(R) Xeon(R) E2620 @ 2GHz    (12Cores/24Threads)|
+-----------+------------------------------------------------------------+
| Memory    | e.g. 64GiB (@1333MHz)                                      |
+-----------+------------------------------------------------------------+
| Network   | e.g. 2x10Gb/s Intel X520                                   |
+-----------+------------------------------------------------------------+

Controller

+-----------+------------------------------------------------------------+
| Parameter | Value                                                      |
+-----------+------------------------------------------------------------+
| model     | e.g. Dell PowerEdge r620                                   |
+-----------+------------------------------------------------------------+
| CPU       | e.g. 2xIntel(R) Xeon(R) E2620 @ 2GHz    (12Cores/24Threads)|
+-----------+------------------------------------------------------------+
| Memory    | e.g. 64GiB (@1333MHz)                                      |
+-----------+------------------------------------------------------------+
| Network   | e.g. 2x10Gb/s Intel X520                                   |
+-----------+------------------------------------------------------------+

Compute (7)

+-----------+------------------------------------------------------------+
| Parameter | Value                                                      |
+-----------+------------------------------------------------------------+
| model     | e.g. Dell PowerEdge r620                                   |
+-----------+------------------------------------------------------------+
| CPU       | e.g. 2xIntel(R) Xeon(R) E2620 @ 2GHz    (12Cores/24Threads)|
+-----------+------------------------------------------------------------+
| Memory    | e.g. 64GiB (@1333MHz)                                      |
+-----------+------------------------------------------------------------+
| Network   | e.g. 2x10Gb/s Intel X520                                   |
+-----------+------------------------------------------------------------+

Software
~~~~~~~~
Record versions of Linux kernel, Base Operating System (RHEL 7.3),
OpenStack version 10 (Newton), OpenStack Packages, testing harness/framework
and any other pertinent software.

Tuning/Configuration
~~~~~~~~~~~~~~~~~~~~
With TripleO we can use an extra configuration file that explicitly sets the
worker count for us. However with these templates we cannot do simple
calculations based on the $::processorcount. However we can use it to statically
set our deployment to a known number of workers. This tuning file was used for
this work to set the number of workers per-service.

**Example of tunings.yaml**

.. code-block:: none

  parameter_defaults:
    controllerExtraConfig:
        keystone::wsgi::apache::workers: 24
        keystone::wsgi::apache::threads: 1

Test Diagram
~~~~~~~~~~~~
Using OpenStack Browbeat execute the same test scenarios[1]  across different
os_worker counts within the overcloud. Our SUT is equipped with Intel Westmere
CPUs (dual socket), so we have a total of 24 logical cores to work with. Based
on the current upstream calculation, os_worker count will be 6.

.. code-block:: none

  os_worker_count = (((processor_count/4),2).max,8).min
  os_worker_count = (((24/4),2).max,8).min

This testing will run with the following number of os_workers: 6, 8, 12 and 24
to determine if the current default performs favorably, or if we should suggest
changing it.

We will use TripleO to deploy the SUT OpenStack cloud. We will vary the os_worker
count using the tunings.yaml script described above.

Each OpenStack Rally scenario defined in [1] will execute 3 times per os_worker
environment. Our results will show the Min, Max, Average and 95%tile per atomic action.

[1] https://gist.github.com/jtaleric/fcc8d0d0d989d7a593a6e8c595252150

Test Case 1: Keystone
----------------------

Description
^^^^^^^^^^^
Each Rally scenario below was executed until they reach 1500 times, at 32 and 64 concurrencies.

**Scenarios**
  * Authenticate-keystone
  * Authenticate-neutron
  * Authenticate-nova

Setup
^^^^^^
#. Deploy OpenStack Cloud
#. Install testing and monitoring tooling
#. Gather metadata on Cloud
#. Run test

Analysis
^^^^^^^^^
Review Rally scenario results, noting the API response times at different concurrencies.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Performance

- Service API response times

Test Case 2: Neutron
----------------------

Description
^^^^^^^^^^^
Each Rally scenario below will until they reach 500 times, at 32 and 64 concurrencies.

**Scenarios**
  * Create-list-network
  * Create-list-port
  * Create-list-router
  * Create-list-security-group
  * Create-list-subnet

Setup
^^^^^^
#. Deploy OpenStack Cloud
#. Install testing and monitoring tooling
#. Gather metadata on Cloud
#. Run test

Analysis
^^^^^^^^^
Review Rally scenario results, noting the API response times at different concurrencies.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Performance

- Service API response times

