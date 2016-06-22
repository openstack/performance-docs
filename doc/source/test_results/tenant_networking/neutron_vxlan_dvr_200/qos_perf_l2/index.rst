.. _openstack_l2_qos_performance:

OpenStack L2 QoS Performance
****************************

In this scenario Shaker launches 1 pair of instances in the same tenant
network. Each instance is hosted on a separate compute node. The traffic goes
within the tenant network (L2 domain). Neutron QoS feature is used to limit
traffic throughput to 10 Mbit/s.

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - single_room
      - compute_nodes: 2
      template: l2_qos.hot
    description: In this scenario Shaker launches 1 pair of instances in the same tenant
      network. Each instance is hosted on a separate compute node. The traffic goes within
      the tenant network (L2 domain). Neutron QoS feature is used to limit traffic throughput
      to 10 Mbit/s.
    execution:
      tests:
      - class: flent
        method: ping
        time: 10
        title: Ping
      - class: iperf3
        title: TCP
      - bandwidth: 0
        class: iperf3
        datagram_size: 32
        title: UDP
        udp: true
    title: OpenStack L2 QoS Performance

Ping
====

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: ping
    time: 10
    title: Ping

.. image:: 4b80944c-2ec8-45a0-8d9e-f67d9c631f8a.*

**Stats**:

=============  ========  ========  ========
Metric         Min       Avg       Max     
=============  ========  ========  ========
ping_icmp, ms      0.31      0.55      1.26
=============  ========  ========  ========

TCP
===

**Test Specification**:

.. code-block:: yaml

    class: iperf3
    interval: 1
    title: TCP

.. image:: 3b6ce92f-9aca-40a4-8eeb-f7ba6fc5bea1.*

**Stats**:

=================  ========  ========  ========
Metric             Min       Avg       Max     
=================  ========  ========  ========
bandwidth, Mbit/s      8.13     10.69     91.39
retransmits              58        90       424
=================  ========  ========  ========

UDP
===

**Test Specification**:

.. code-block:: yaml

    bandwidth: 0
    class: iperf3
    datagram_size: 32
    interval: 1
    title: UDP
    udp: true

.. image:: d3e16faa-71c6-4742-8202-71302b1492da.*

**Stats**:

============  ========  ========  ========
Metric        Min       Avg       Max     
============  ========  ========  ========
packets, pps    238180    388859    427170
============  ========  ========  ========
