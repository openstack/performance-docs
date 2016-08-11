.. _reliability_testing:

=============================
OpenStack reliability testing
=============================

:status: **ready**
:version: 1.0

:Abstract:
  This document describes an abstract methodology for OpenStack cluster
  high-availability testing and analysis. OpenStack data plane testing
  at this moment is out of scope, but will be described in future.

:Conventions:

.. include:: plan_conventions.rst

Test Plan
=========

Test Environment
----------------

This section should contain all information about deployed OpenStack
environment including archive with all information in the ``/etc`` folder from
all nodes.

Preparation
^^^^^^^^^^^

This section should contain all steps to reproduce Openstack environment
deployment and client node. For example: if testing environment is deployed
with DevStack, this section should contain all DevStack configuration files,
DevStack version and all deployment steps.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

This section should contain all cluster hardware information, including
processor model and its frequency, memory size, storage type and its capacity,
network interfaces, and others.
A separate client node must be used to drive the tests.

Hardware
~~~~~~~~

This section should contain a full hardware nodes specification.

.. table:: Description of server hardware

  +--------+----------------+-------+-------+
  |SERVER  |name            |       |       |
  |        +----------------+-------+-------+
  |        |role            |       |       |
  |        +----------------+-------+-------+
  |        |vendor,model    |       |       |
  |        +----------------+-------+-------+
  |        |operating_system|       |       |
  +--------+----------------+-------+-------+
  |CPU     |vendor,model    |       |       |
  |        +----------------+-------+-------+
  |        |processor_count |       |       |
  |        +----------------+-------+-------+
  |        |core_count      |       |       |
  |        +----------------+-------+-------+
  |        |frequency_MHz   |       |       |
  +--------+----------------+-------+-------+
  |RAM     |vendor,model    |       |       |
  |        +----------------+-------+-------+
  |        |amount_MB       |       |       |
  +--------+----------------+-------+-------+
  |NETWORK |interface_name  |       |       |
  |        +----------------+-------+-------+
  |        |vendor,model    |       |       |
  |        +----------------+-------+-------+
  |        |bandwidth       |       |       |
  +--------+----------------+-------+-------+
  |STORAGE |dev_name        |       |       |
  |        +----------------+-------+-------+
  |        |vendor,model    |       |       |
  |        +----------------+-------+-------+
  |        |SSD/HDD         |       |       |
  |        +----------------+-------+-------+
  |        |size            |       |       |
  +--------+----------------+-------+-------+

Networking
~~~~~~~~~~

This section should сontain full description of network equipment used in
OpenStack cluster. Network topology diagram and network hardware
configuration files should be included in this section.

Factors description
-------------------

  Please define here description of used factors during test runs.
  Examples are:

  - **reboot-random-controller:** consist node-crash fault injection on random
  OpenStack controller node.

  - **reboot-random-rabbitmq:** consist node-crash fault injection on master
  RabbitMQ messaging node.

  - **sigstop-random-nova-api:** consist service-hang fault injection on random
  nova-api service.

  - **sigkill-random-mysql:** consist service-crash fault injection on
  random MySQL node.

  - **network-partition-random-mysql:** consist network-partition fault injection on
  random MySQL node.


Test Case 1: NovaServers.boot_and_delete_server
-----------------------------------------------

Description
^^^^^^^^^^^

This Rally scenario boots and deletes virtual instances with injected fault
factors through OpenStack Nova API.

Service-level agreement
^^^^^^^^^^^^^^^^^^^^^^^

In this section, specify SLA values. For example:

=================== ========
Parameter           Value
=================== ========
MTTR (sec)          <=240
Failure rate (%)    <=95
Auto-healing        Yes
=================== ========

Parameters
^^^^^^^^^^

In this section, specify load parameters during the test. For example:

=================== ========
Parameter           Value
=================== ========
Runner              constant
Concurrency         X
Times               Y
Injection-iteration Z
Testing-cycles      N
=================== ========

List of reliability metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ==============  =================  =================================================
Priority  Value           Measurement Units  Description
========  ==============  =================  =================================================
1         SLA             Boolean            Service-level agreement result
2         Auto-healing    Boolean            Is cluster auto-healed after fault-injection
3         Failure rate    Percents           Test iteration failure ratio
4         MTTR (auto)     Seconds            Automatic mean time to repair
5         MTTR (manual)   Seconds            Manual mean time to repair, if Auto MTTR is Inf.
========  ==============  =================  =================================================

Results
^^^^^^^

reboot-random-controller
~~~~~~~~~~~~~~~~~~~~~~~~

.. table:: **Full description of cyclic execution results**

    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | Cycles             | MTTR(sec)     | Failure rate(%)      | Auto-healing     | Performance degradation     |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 1                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 2                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 3                  | X              | Y                   | No               | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 4                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 5                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+

Place here link to rally report file with results of testing this factor.

.. table:: **Testing results summary**

    +--------------------+------------+------------------+
    | Value              | MTTR       | Failure rate     |
    +--------------------+------------+------------------+
    | Min                | X          | Y                |
    +--------------------+------------+------------------+
    | Max                | X          | Y                |
    +--------------------+------------+------------------+
    | SLA                | X          | Y                |
    +--------------------+------------+------------------+

Detailed results description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section, specify detailed description of test results,
including factor impact.

reboot-random-rabbitmq
~~~~~~~~~~~~~~~~~~~~~~

.. table:: **Full description of cyclic execution results**

    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | Cycles             | MTTR(sec)      | Failure rate(%)     | Auto-healing     | Performance degradation     |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 1                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 2                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 3                  | X              | Y                   | No               | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 4                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 5                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+

Place here link to rally report file with results of testing this factor.

.. table:: **Testing results summary**

    +--------------------+------------+------------------+
    | Value              | MTTR       | Failure rate     |
    +--------------------+------------+------------------+
    | Min                | X          | Y                |
    +--------------------+------------+------------------+
    | Max                | X          | Y                |
    +--------------------+------------+------------------+
    | SLA                | X          | Y                |
    +--------------------+------------+------------------+

Detailed results description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section, specify detailed description of test results,
including factor impact.


Test Case 2: GlanceImages.create_and_delete_image
-------------------------------------------------

Description
^^^^^^^^^^^

This Rally scenario creates and deletes images with injected fault
factors through OpenStack Glance API.

Service-level agreement
^^^^^^^^^^^^^^^^^^^^^^^

In this section, specify SLA values. For example:

=================== ========
Parameter           Value
=================== ========
MTTR (sec)          <=120
Failure rate (%)    <=95
Auto-healing        Yes
=================== ========

Parameters
^^^^^^^^^^
In this section, specify load parameters during the test. For example:

=================== ========
Parameter           Value
=================== ========
Runner              constant
Concurrency         X
Times               Y
Injection-iteration Z
Testing-cycles      N
=================== ========

List of reliability metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ==============  =================  =================================================
Priority  Value           Measurement Units  Description
========  ==============  =================  =================================================
1         SLA             Boolean            Service-level agreement result
2         Auto-healing    Boolean            Is cluster auto-healed after fault-injection
3         Failure rate    Percents           Test iteration failure ratio
4         MTTR (auto)     Seconds            Automatic mean time to repair
5         MTTR (manual)   Seconds            Manual mean time to repair, if Auto MTTR is Inf.
========  ==============  =================  =================================================

Results
^^^^^^^

reboot-random-controller
~~~~~~~~~~~~~~~~~~~~~~~~

.. table:: **Full description of cyclic execution results**

    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | Cycles             | MTTR(sec)      | Failure rate(%)     | Auto-healing     | Performance degradation     |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 1                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 2                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 3                  | X              | Y                   | No               | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 4                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 5                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+

Place here link to rally report file with results of testing this factor.

.. table:: **Testing results summary**

    +--------------------+------------+------------------+
    | Value              | MTTR       | Failure rate     |
    +--------------------+------------+------------------+
    | Min                | X          | Y                |
    +--------------------+------------+------------------+
    | Max                | X          | Y                |
    +--------------------+------------+------------------+
    | SLA                | X          | Y                |
    +--------------------+------------+------------------+

Detailed results description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section, specify detailed description of test results,
including factor impact.

reboot-random-rabbitmq
~~~~~~~~~~~~~~~~~~~~~~

.. table:: **Full description of cyclic execution results**

    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | Cycles             | MTTR(sec)      | Failure rate(%)     | Auto-healing     | Performance degradation     |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 1                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 2                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 3                  | X              | Y                   | No               | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 4                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+
    | 5                  | X              | Y                   | Yes              | Yes                         |
    +--------------------+----------------+---------------------+------------------+-----------------------------+

Place here link to rally report file with results of testing this factor.

.. table:: **Testing results summary**

    +--------------------+------------+------------------+
    | Value              | MTTR       | Failure rate     |
    +--------------------+------------+------------------+
    | Min                | X          | Y                |
    +--------------------+------------+------------------+
    | Max                | X          | Y                |
    +--------------------+------------+------------------+
    | SLA                | X          | Y                |
    +--------------------+------------+------------------+

Detailed results description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section, specify detailed description of test results,
including factor impact.
