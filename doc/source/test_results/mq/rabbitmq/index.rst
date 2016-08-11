.. raw:: pdf

    PageBreak oneColumn

.. _mq_rabbit_report:

===========================
RabbitMQ Performance Report
===========================

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

This report is generated for :ref:`message_queue_performance` test plan with
`Oslo.messaging Simulator`_ tool. The data is collected in
:ref:`intel_mirantis_performance_lab`.


Reports
^^^^^^^

.. toctree::
    :maxdepth: 1

    cmsm/index
    cs1ss2/index

    cmsm-ha/index
    cs1ss2-ha/index


High-level performance overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows top throughput achieved on different topologies
with RabbitMQ HA queues enabled and disabled.

.. list-table::
      :header-rows: 1

      *
        - Topology
        - CALL, msg/sec
        - CAST, msg/sec
        - NOTIFY, msg/sec
      *
        - Client -> Master, Server -> Master
        - 5100
        - 9300
        - 9200
      *
        - Client -> Slave-1, Server -> Slave-2
        - 6800
        - 14700
        - 14300
      *
        - Client -> Master, Server -> Master (HA)
        - 2400
        - 6600
        - 6900
      *
        - Client -> Slave-1, Server -> Slave-2 (HA)
        - 3200
        - 5600
        - 5300


.. references:

.. _Oslo.messaging Simulator: https://github.com/openstack/oslo.messaging/blob/master/tools/simulator.py
