.. _openstack_l3_north_south_performance:

OpenStack L3 North-South Performance 2 nodes
********************************************

In this scenario Shaker launches 1 pair of instances on different compute
nodes. Instances are in different networks connected to different routers,
master accesses slave by floating ip. The traffic goes from one network via
external network to the other network.

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - single_room
      - compute_nodes: 2
      template: l3_north_south.hot
    description: In this scenario Shaker launches 1 pair of instances on different compute
      nodes. Instances are in different networks connected to different routers, master
      accesses slave by floating ip. The traffic goes from one network via external network
      to the other network.
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
    file_name: /opt/stack/.venv/local/lib/python2.7/site-packages/shaker/scenarios/openstack/perf_l3_north_south.yaml
    title: OpenStack L3 North-South Performance

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

.. image:: f31693a7-4b4d-4ccd-a11a-8089e0d56ede.*

**Stats**:

=============  ========  ========  ========
Metric         Min       Avg       Max     
=============  ========  ========  ========
ping_icmp, ms      0.68      0.91      1.69
=============  ========  ========  ========

**SLA**:

=========================  ===========  =================  ========
Expression                 Concurrency  Node               Result  
=========================  ===========  =================  ========
stats.ping_icmp.avg < 2.0            1  node-9.domain.tld  OK
=========================  ===========  =================  ========

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

.. image:: 7a9de86c-3cf7-449a-991a-0cacb9f6f22c.*

**Stats**:

=================  ========  ========  ========
Metric             Min       Avg       Max     
=================  ========  ========  ========
bandwidth, Mbit/s   4798.81   5321.76   7280.13
retransmits                         9       194
=================  ========  ========  ========

**SLA**:

==========================  ===========  =================  ========
Expression                  Concurrency  Node               Result  
==========================  ===========  =================  ========
stats.bandwidth.avg > 5000            1  node-9.domain.tld  OK
stats.retransmits.max < 10            1  node-9.domain.tld  FAIL
==========================  ===========  =================  ========

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

.. image:: ed64971f-fb42-4526-a7a7-6aecbbdd60e8.*

**Stats**:

============  ========  ========  ========
Metric        Min       Avg       Max     
============  ========  ========  ========
packets, pps    135350    141101    149270
============  ========  ========  ========

**SLA**:

==========================  ===========  =================  ========
Expression                  Concurrency  Node               Result  
==========================  ===========  =================  ========
stats.packets.avg > 100000            1  node-9.domain.tld  OK
==========================  ===========  =================  ========

