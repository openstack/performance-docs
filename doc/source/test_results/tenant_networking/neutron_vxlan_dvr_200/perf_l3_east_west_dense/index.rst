.. _openstack_l3_east_west_performance_dense:

OpenStack L3 East-West Performance within single compute node
*************************************************************

In this scenario Shaker launches 1 pair of instances, both are hosted on the
same compute node.  Instances are connected to one of 2 tenant networks, which
plugged into single router. The traffic goes from one network to the other (L3
east-west).

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - double_room
      - compute_nodes: 1
      template: l3_east_west.hot
    description: In this scenario Shaker launches 1 pair of instances, both are hosted on the
      same compute node. Instances are connected to one of 2 tenant networks, which
      plugged into single router. The traffic goes from one network to the other (L3 east-west).
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
    title: OpenStack L3 East-West Performance

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

.. image:: 42f40fed-1f50-41cb-9bf7-8f7043164832.*

**Stats**:

=============  =========  =========  =========
Metric         Min        Avg        Max
=============  =========  =========  =========
ping_icmp, ms      0.215      0.346      0.582
=============  =========  =========  =========

**SLA**:

=========================  ===========  =================  =========
Expression                 Concurrency  Node               Result
=========================  ===========  =================  =========
stats.ping_icmp.avg < 2.0            1  node-7.domain.tld  OK
=========================  ===========  =================  =========

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

.. image:: c83bcfac-5181-4dd7-a808-250f230e144b.*

**Stats**:

=================  =========  =========  =========
Metric             Min        Avg        Max      
=================  =========  =========  =========
bandwidth, Mbit/s  12611.771  16735.987  20540.142
retransmits
=================  =========  =========  =========

**SLA**:

==========================  ===========  =================  =========
Expression                  Concurrency  Node               Result   
==========================  ===========  =================  =========
stats.bandwidth.avg > 5000            1  node-7.domain.tld  OK
stats.retransmits.max < 10            1  node-7.domain.tld  OK
==========================  ===========  =================  =========

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

.. image:: 81bd6b54-c9ef-46b8-8325-b13004b9d651.*

**Stats**:

============  =========  =========  =========
Metric        Min        Avg        Max
============  =========  =========  =========
loss, %                      0.000
jitter, ms                   0.007
packets, pps     121030     131170     136500
============  =========  =========  =========

**SLA**:

==========================  ===========  =================  =========
Expression                  Concurrency  Node               Result
==========================  ===========  =================  =========
stats.packets.avg > 100000            1  node-7.domain.tld  OK
==========================  ===========  =================  =========

