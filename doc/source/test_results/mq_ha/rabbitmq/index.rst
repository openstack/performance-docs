.. raw:: pdf

    PageBreak oneColumn

.. _mq_ha_rabbit_report_disabled:

============================================
RabbitMQ HA Test Reports: HA queues disabled
============================================

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

This report is generated for :ref:`message_queue_ha` test plan with
`Oslo.messaging Simulator`_ tool. The data is collected in
:ref:`intel_mirantis_performance_lab_1`.


Software
~~~~~~~~

This section describes installed software.

+-----------------+--------------------------------------------+
| Parameter       | Value                                      |
+-----------------+--------------------------------------------+
| OS              | Ubuntu 14.04.3                             |
+-----------------+--------------------------------------------+
| oslo.messaging  | 4.5.1                                      |
+-----------------+--------------------------------------------+
| MQ Server       | RabbitMQ 3.5.6                             |
+-----------------+--------------------------------------------+
| HA mode         | Pacemaker cluster, HA queues disabled      |
+-----------------+--------------------------------------------+


Reports
^^^^^^^

.. toctree::
    :maxdepth: 2

    cmsm-km/index
    cs1ss1-ks1/index
    cs1ss2-ks2/index
    cmss2-km/index

.. references:

.. _Oslo.messaging Simulator: https://github.com/openstack/oslo.messaging/blob/master/tools/simulator.py
