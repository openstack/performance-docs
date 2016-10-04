
.. _Measuring_of_API_performance_of_container_cluster_system:

*********************************************************
Measuring of API performance of container cluster systems
*********************************************************

:status: **ready**
:version: 1.0

:Abstract:

  This document describes a test plan for quantifying the API performance of
  container cluster systems.

Test Plan
=========
Test Environment
----------------
Preparation
^^^^^^^^^^^
To test container cluster some tool dedicated to measure CRUD operations
latency is needed. For Kubernetes container cluster system we can propose
"Load test" of `e2e-tests`_ tool.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^
Test results MUST include a description of the environment used. The following
items should be described:

- **Hardware configuration of each server.** If virtual machines are used then
  both physical and virtual hardware should be fully documented.
  An example format is given below:

.. table:: Description of servers hardware

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

- **Configuration of hardware network switches** The configuration file from
  the switch can be downloaded and attached.

- **Configuration of virtual machines and virtual networks (if they are used)**
  The configuration files can be attached, along with the mapping of virtual
  machines to host machines.

- **Network scheme.** The plan should show how all hardware is connected and
  how the components communicate. All ethernet/fibrechannel and VLAN channels
  should be included. Each interface of every hardware component should be
  matched with the corresponding L2 channel and IP address.

- **Software configuration of the container cluster system** `sysctl.conf` and
  any other kernel file that is changed from the default should be attached.
  List of installed packages should be attached. Specifications of the
  operating system, network interfaces configuration, and disk partitioning
  configuration should be included. If distributed provisioning systems are
  to be tested then the parts that are distributed need to be described.

- **Software configuration of the node with test tool** The operating system,
  disk partitioning scheme, network interface configuration, installed packages
  and other components of client nodes define limits which a client can
  experience during sending requests and getting responses to/from docker
  repository.

Test Case #1: API latencies of requests which make actions on containers
------------------------------------------------------------------------
Description
^^^^^^^^^^^
During this test basic actions with containers like start, delete, update
should be performed and API latencies should be measured.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +-----------------------------+---------------------------------------------+
  | Parameter                   |Description                                  |
  +=============================+=============================================+
  || CONTAINER_API_LATENCIES    | | The time which a client spends to get a   |
  || (GET,PUT,POST,DELETE, LIST | | response from container system API to make|
  || types of requests)         | | an action on a docker container           |
  +-----------------------------+---------------------------------------------+

Measuring values of API latencies of requests which make actions on containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.
  Deploy container cluster system from scratch. We should be sure that there is
  no data in the container cluster system.

2.
  Make create, delete, update and any available requests to perform an action
  on container to API of container cluster system and measure latencies of
  the responses. The API client which you use should't crate a big load on the
  cluster system. The load should be spreading over time.

3.
  As a result of the previous step you should be able to provide the table with
  99 percentile of API latencies in depend on type of requests. You need to
  fill the table similar the table bellow with calculated values:

.. table:: API latencies of requests which make actions on containers

  +---------------------------------+-----------------------------------------+
  | Method                          |   Perc99                                |
  +=================================+=========================================+
  | PUT                             |                                         |
  +---------------------------------+-----------------------------------------+
  | GET                             |                                         |
  +---------------------------------+-----------------------------------------+
  | LIST                            |                                         |
  +---------------------------------+-----------------------------------------+
  | DELETE                          |                                         |
  +---------------------------------+-----------------------------------------+
  | POST                            |                                         |
  +---------------------------------+-----------------------------------------+

Test Case #1.5: Container creation startup latency extended measurement
-----------------------------------------------------------------------

Description
^^^^^^^^^^^

The is a specific interest in understanding not only when container cluster
system is reporting that the requested container is up and running, but when
this container really becomes operable in data plane terms. This can be
measured via scheduling and spawning containers, that will report about their
status to some centralized manager. This data needs to be collected and then
carefully analyzed, especially keeping attention to possible regressions (if
huge number of containers is created - either at once or one by one).

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +-----------------------------+---------------------------------------------+
  | Parameter                   |Description                                  |
  +=============================+=============================================+
  |  CONTAINER_STARTUP_LATENCY  | | The time which a container management     |
  |                             | | system needs to spawn workable and fully  |
  |                             | | operable container.                       |
  +-----------------------------+---------------------------------------------+

Test Case #2: API latencies of any other supported requests
-----------------------------------------------------------
Description
^^^^^^^^^^^
In opposite of
`Test Case #1: API latencies of requests which make actions on containers`_ in
in this test case requests different from actions with containers should be
performed and API latencies should be measured. The supported by API of
container cluster system requests depend on the container cluster system. For
example for Kubernetes it can be actions with replicationcontrollers or
namespaces.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +-----------------------------+---------------------------------------------+
  | Parameter                   |Description                                  |
  +=============================+=============================================+
  || API_LATENCIES              | | The time which a client spends to get a   |
  || (GET,PUT,POST,DELETE, LIST | | response from container system API        |
  || types of requests)         | |                                           |
  +-----------------------------+---------------------------------------------+

Measuring values of API latencies of any other supported requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.
  Deploy container cluster system from scratch. We should be sure that there is
  no data in the container cluster system.

2.
  Make available requests to API of container cluster system and measure
  latencies of the responses. The API client which you use should't crate a big
  load on the cluster system. The load should be spreading over time.

3.
  As a result of the previous step you should be able to provide the table with
  99 percentile of API latencies in depend on type of requests. You need to
  fill the table similar the table bellow with calculated values:

.. table:: Table #1 API latencies of requests which make actions on item #1

  +---------------------------------+-----------------------------------------+
  | Method                          |   Perc99                                |
  +=================================+=========================================+
  | PUT                             |                                         |
  +---------------------------------+-----------------------------------------+
  | GET                             |                                         |
  +---------------------------------+-----------------------------------------+
  | LIST                            |                                         |
  +---------------------------------+-----------------------------------------+
  | DELETE                          |                                         |
  +---------------------------------+-----------------------------------------+
  | POST                            |                                         |
  +---------------------------------+-----------------------------------------+

.. table:: Table #2 API latencies of requests which make actions on item #2

  +---------------------------------+-----------------------------------------+
  | Method                          |   Perc99                                |
  +=================================+=========================================+
  | PUT                             |                                         |
  +---------------------------------+-----------------------------------------+
  | GET                             |                                         |
  +---------------------------------+-----------------------------------------+
  | LIST                            |                                         |
  +---------------------------------+-----------------------------------------+
  | DELETE                          |                                         |
  +---------------------------------+-----------------------------------------+
  | POST                            |                                         |
  +---------------------------------+-----------------------------------------+

.. references:

.. _e2e-tests: https://github.com/kubernetes/kubernetes/blob/release-1.4/docs/devel/e2e-tests.md

Reports
=======

Test plan execution reports:
 * :ref:`Results_of_Measuring_of_API_performance_of_Kubernetes`
