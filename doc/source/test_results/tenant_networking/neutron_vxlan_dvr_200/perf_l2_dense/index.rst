.. _openstack_l2_performance_dense:

OpenStack L2 Performance within single compute node
***************************************************

In this scenario Shaker launches 1 pair of instances in the same tenant
network. Both instances are hosted on the same compute node. The traffic goes
within the tenant network (L2 domain).

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - double_room
      - compute_nodes: 1
      template: l2.hot
    description: In this scenario Shaker launches 1 pair of instances in the same tenant
      network. Both instances are hosted on the same compute node. The traffic goes within
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

.. image:: 23d521f3-d5eb-444a-9dc2-d05ee6e9461d.*

**Stats**:

=============  =========  =========  =========
Metric         Min        Avg        Max
=============  =========  =========  =========
ping_icmp, ms      0.200      0.317      0.666
=============  =========  =========  =========

**SLA**:

=========================  ===========  ==================  =========
Expression                 Concurrency  Node                Result
=========================  ===========  ==================  =========
stats.ping_icmp.avg < 2.0            1  node-17.domain.tld  OK
=========================  ===========  ==================  =========

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

.. image:: 94599950-242d-4c96-8c5b-cd725edf1970.*

**Stats**:

=================  =========  =========  =========
Metric             Min        Avg        Max
=================  =========  =========  =========
bandwidth, Mbit/s  13009.930  16494.578  24087.429
retransmits
=================  =========  =========  =========

**SLA**:

==========================  ===========  ==================  =========
Expression                  Concurrency  Node                Result
==========================  ===========  ==================  =========
stats.bandwidth.avg > 5000            1  node-17.domain.tld  OK
stats.retransmits.max < 10            1  node-17.domain.tld  OK
==========================  ===========  ==================  =========

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

.. image:: 4f806542-e1fc-4d45-a23f-9c10e77270b3.*

**Stats**:

============  =========  =========  =========
Metric        Min        Avg        Max
============  =========  =========  =========
loss, %                      0.000
jitter, ms                   0.004
packets, pps     160720     166747     179430
============  =========  =========  =========

**SLA**:

==========================  ===========  ==================  =========
Expression                  Concurrency  Node                Result
==========================  ===========  ==================  =========
stats.packets.avg > 100000            1  node-17.domain.tld  OK
==========================  ===========  ==================  =========

