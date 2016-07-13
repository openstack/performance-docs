.. _openstack_l2_performance:

OpenStack L2 Performance
************************

In this scenario Shaker launches 1 pair of instances in the same tenant
network. Each instance is hosted on a separate compute node. The traffic goes
within the tenant network (L2 domain).

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - single_room
      - compute_nodes: 2
      template: l2.hot
    description: In this scenario Shaker launches 1 pair of instances in the same tenant
      network. Each instance is hosted on a separate compute node. The traffic goes within
      the tenant network (L2 domain).
    execution:
      tests:
      - class: flent
        method: ping
        sla:
        - '[type == ''agent''] >> (stats.ping_icmp.avg < 2.0)'
        time: 10
        title: Ping
      - class: iperf3
        sla:
        - '[type == ''agent''] >> (stats.bandwidth.avg > 5000)'
        - '[type == ''agent''] >> (stats.retransmits.max < 10)'
        title: TCP
      - bandwidth: 0
        class: iperf3
        datagram_size: 32
        sla:
        - '[type == ''agent''] >> (stats.packets.avg > 100000)'
        title: UDP
        udp: true
    file_name: /opt/stack/.venv/local/lib/python2.7/site-packages/shaker/scenarios/openstack/perf_l2.yaml
    title: OpenStack L2 Performance

Ping
====

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: ping
    sla:
    - '[type == ''agent''] >> (stats.ping_icmp.avg < 2.0)'
    time: 10
    title: Ping

.. image:: e16eb203-5cb1-49b9-aed3-6fb87e2f9e08.*

**Stats**:

=============  ========  ========  ========
Metric         Min       Avg       Max
=============  ========  ========  ========
ping_icmp, ms      0.27      0.56      1.55
=============  ========  ========  ========

**SLA**:

=========================  ===========  ==================  ========
Expression                 Concurrency  Node                Result
=========================  ===========  ==================  ========
stats.ping_icmp.avg < 2.0            1  node-25.domain.tld  OK
=========================  ===========  ==================  ========

TCP
===

**Test Specification**:

.. code-block:: yaml

    class: iperf3
    interval: 1
    sla:
    - '[type == ''agent''] >> (stats.bandwidth.avg > 5000)'
    - '[type == ''agent''] >> (stats.retransmits.max < 10)'
    title: TCP

.. image:: 0b79db9b-af16-4471-a525-5c740098a7a7.*

**Stats**:

=================  ========  ========  ========
Metric             Min       Avg       Max
=================  ========  ========  ========
bandwidth, Mbit/s   5559.96   6875.94   7930.98
retransmits                                  26
=================  ========  ========  ========

**SLA**:

==========================  ===========  ==================  ========
Expression                  Concurrency  Node                Result
==========================  ===========  ==================  ========
stats.bandwidth.avg > 5000            1  node-25.domain.tld  OK
stats.retransmits.max < 10            1  node-25.domain.tld  FAIL
==========================  ===========  ==================  ========

UDP
===

**Test Specification**:

.. code-block:: yaml

    bandwidth: 0
    class: iperf3
    datagram_size: 32
    interval: 1
    sla:
    - '[type == ''agent''] >> (stats.packets.avg > 100000)'
    title: UDP
    udp: true

.. image:: 4c1cfdd5-5f8c-41de-ab18-75309778f91f.*

**Stats**:

============  =========  =========  =========
Metric        Min        Avg        Max
============  =========  =========  =========
loss, %                      0.019
jitter, ms                   0.003
packets, pps     184290     206668     223370
============  =========  =========  =========

**SLA**:

==========================  ===========  ==================  ========
Expression                  Concurrency  Node                Result
==========================  ===========  ==================  ========
stats.packets.avg > 100000            1  node-25.domain.tld  OK
==========================  ===========  ==================  ========

