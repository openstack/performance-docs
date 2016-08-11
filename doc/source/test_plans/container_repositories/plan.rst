
.. _Measuring_performance_of_container_repositories:

***********************************************
Measuring performance of container repositories
***********************************************

:status: **ready**
:version: 1.0

:Abstract:

  This document describes a test plan for quantifying the performance of
  docker repository as a function of the number of clients of the systems.

:Conventions:
  - **Docker repository** A complete microservices architecture need a some
    repository for images. This repository  should provide  storage for image,
    should can work with image versions, provide HA mode and scalability. There
    are several repositories, such as `Docker Registry2`_, `Sonatype Nexus`_
    or `JFrog Artifactory`_.

  - **Pull from a docker repository** is a process when a client gets some
    docker image from a docker repository.

  - **Push to a docker repository** is a process when a client uploads some
    docker image to a docker repository.

  - **Client** is a software which communicate with a docker repository to
    push/pull a docker image to/from the docker repository. We'll use `Docker`_
    as a client.

List of performance metrics
===========================
The table below shows the list of test metrics which impact to docker
repository system at all:

.. table:: List of performance metrics

  +--------------------+-------------------------------------------------------+
  | Parameter          | Description                                           |
  +====================+=======================================================+
  |PULL_TIME           | | The time which a client spends on reading a data    |
  |                    | | from the docker repository                          |
  +--------------------+-------------------------------------------------------+
  |PUSH_TIME           | | The time which a client spends on writing a data    |
  |                    | | to a docker repository                              |
  +--------------------+-------------------------------------------------------+
  |ITERATIONS_COUNT    | | Numbers of requests or chains of requests from a    |
  |                    | | client to docker repository and corresponding       |
  |                    | | responses from docker repository                    |
  |                    | | to a client wchich perform an action or chain of    |
  |                    | | actions like a pull, push etc.                      |
  +--------------------+-------------------------------------------------------+
  |CONCURRENCY         | | Numbers of clients which pull/push a data from/to a |
  |                    | | data from/to the docker repository at the same time |
  +--------------------+-------------------------------------------------------+
  |DATA_SIZE           | | A size of a data which clients read/write from/to   |
  |                    | | docker repository during one request-response cycle |
  +--------------------+-------------------------------------------------------+

Test Plan
=========
Test Environment
----------------
Preparation
^^^^^^^^^^^
To test docker repository some tool is needed. Here we can propose
`Script for collecting performance metrics`_ which you can find in
`Applications`_ section.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^
Test results MUST include a description of the environment used. The following
items should be included:

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

- **Software configuration of the docker repository system** `sysctl.conf` and
  any other kernel file that is changed from the default should be attached.
  List of installed packages should be attached. Specifications of the
  operating system, network interfaces configuration, and disk partitioning
  configuration should be included. If distributed provisioning systems are
  to be tested then the parts that are distributed need to be described.

- **Software configuration of the client nodes** The operating system, disk
  partitioning scheme, network interface configuration, installed packages and
  other components of client nodes define limits which a client can experience
  during sending requests and getting responses to/from docker repository.

Test Case #1: Uploading to a docker repository.
-----------------------------------------------
Description
^^^^^^^^^^^
This test is aimed at measuring the image uploading (pull action) time.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +---------------------------+-----------------------------------------------+
  | Parameter                 |Description                                    |
  +===========================+===============================================+
  |PUSH_TIME(CONCURRENCY)     | | The time which a client spends on pushing a |
  |                           | | data to the docker repository, as a         |
  |                           | | function of concurrency value               |
  +---------------------------+-----------------------------------------------+

.. table:: list of test metrics to be persistent during this test:

  +--------------------+------------------------------------------------------+
  | Parameter          | Value                                                |
  +====================+======================================================+
  |ITERATIONS_COUNT    | 1000                                                 |
  +--------------------+------------------------------------------------------+
  |DATA_SIZE           | depends on your docker file                          |
  +--------------------+------------------------------------------------------+

Measuring PUSH_TIME(CONCURRENCY) values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.
  Deploy docker repository from scratch. We should be sure that there is no
  data in the docker repository.

2.
  Build 1000 images.

5.
  Run a client in the cycle with ITERATIONS_COUNT iterations and CONCURRENCY
  concurrency value. The client should be able to push the images which we
  created on the step 2 and write a response time to a log/report. You need to
  perform by one cycle per each CONCURRENCY value from the following list:

  * CONCURRENCY=1
  * CONCURRENCY=10
  * CONCURRENCY=30
  * CONCURRENCY=50
  * CONCURRENCY=100

4.
  As a result of the previous step you should be able to provide the amount of
  graphs and tables with the dependences on an iteration number of a response
  time. One graph and one table per each CONCURRENCY. On this step you need to
  calculate minima, maxima, average and 95% percental of PUSH_TIME parameter
  per each CONCURRENCY value. You need to fill the following table with
  calculated values:

.. table:: PUSH_TIME(CONCURRENCY)

  +-------------+--------+--------+---------+-----+
  | CONCURRENCY | PUSH_TIME                       |
  |             +--------+--------+---------+-----+
  |             | minima | maxima | average | 95% |
  +=============+========+========+=========+=====+
  |             |        |        |         |     |
  +-------------+--------+--------+---------+-----+

Test Case #2: Downloading from a docker repository.
---------------------------------------------------
Description
^^^^^^^^^^^
This test is aimed at measuring the image downloading (pull action) time.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +---------------------------+-----------------------------------------------+
  | Parameter                 |Description                                    |
  +===========================+===============================================+
  |PULL_TIME(CONCURRENCY)     | | The time which a client spends on pulling a |
  |                           | | data from the docker repository, as a       |
  |                           | | function of concurrency value               |
  +---------------------------+-----------------------------------------------+

.. table:: list of test metrics to be persistent during this test:

  +--------------------+------------------------------------------------------+
  | Parameter          | Value                                                |
  +====================+======================================================+
  |ITERATIONS_COUNT    | 1000                                                 |
  +--------------------+------------------------------------------------------+
  |DATA_SIZE           | depends on your docker file                          |
  +--------------------+------------------------------------------------------+

Measuring PULL_TIME(CONCURRENCY) values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.
  Deploy docker repository from scratch. We should be sure that there is no
  data in the docker repository.

2.
  Build 1000 images.

3.
  Upload 1000 images to the docker repository

4.
  Delete created images from a local docker on a machine with test tool where
  docker images was created. After this step created images should be placed in
  the docker repository and they should be removed from the local docker.

5.
  Run a client in the cycle with ITERATIONS_COUNT iterations and CONCURRENCY
  concurrency value. The client should be able to pull the images which we
  uploaded on the step 3 and write a response time to a log/report. You need to
  perform by one cycle per each CONCURRENCY value from the following list:

  * CONCURRENCY=1
  * CONCURRENCY=10
  * CONCURRENCY=30
  * CONCURRENCY=50
  * CONCURRENCY=100

4.
  As a result of the previous step you should be able to provide the amount of
  graphs and tables with the dependences on an iteration number of a response
  time. One graph and one table per each CONCURRENCY. On this step you need to
  calculate minima, maxima, average and 95% percental of PULL_TIME parameter
  per each CONCURRENCY value. You need to fill the following table with
  calculated values:

.. table:: PULL_TIME(CONCURRENCY)

  +-------------+--------+--------+---------+-----+
  | CONCURRENCY | PULL_TIME                       |
  |             +--------+--------+---------+-----+
  |             | minima | maxima | average | 95% |
  +=============+========+========+=========+=====+
  |             |        |        |         |     |
  +-------------+--------+--------+---------+-----+

Applications
============
list of container repositories
------------------------------

+-------------------------------+---------+
| Name of container repositories| Version |
+===============================+=========+
| `Docker Registry2`_           |         |
+-------------------------------+---------+
| `Sonatype Nexus`_             |         |
+-------------------------------+---------+
| `JFrog Artifactory`_          |         |
+-------------------------------+---------+

.. _Script for collecting performance metrics of docker repository:

Script for collecting performance metrics
-----------------------------------------
This script has been tested with Python2.7.
Here is three variables which you need to change:

- **iterations:** - number of images which should be created, uploaded to
  a repository and downloaded from the repository.

- **concurrency:** - number of threads which should work at the same time.

- **repo_address** - address and port of a repository service.

.. literalinclude:: test-repo.py
    :language: python

.. _Proposed docker file:

Proposed docker file
--------------------

.. literalinclude:: containers/nginx/Dockerfile

.. references:

.. _Sonatype Nexus:
  http://www.sonatype.com/nexus/solution-overview/nexus-repository
.. _Docker Registry2: https://docs.docker.com/registry
.. _JFrog Artifactory: https://www.jfrog.com/artifactory
.. _Docker: https://www.docker.com

Reports
=======

Test plan execution reports:
 * :ref:`Measuring_performance_of_Sonatype_Nexus`
 * :ref:`Measuring_performance_of_JFrog_Artifactory_Pro`
 * :ref:`Measuring_performance_of_docker_registry`
