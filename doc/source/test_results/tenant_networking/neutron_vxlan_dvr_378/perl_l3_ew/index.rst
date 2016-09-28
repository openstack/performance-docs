.. _openstack_l3_east_west_performance:

OpenStack L3 East-West Performance 2 nodes
******************************************

In this scenario Shaker launches 1 pair of instances, each instance on its own
compute node. Instances are connected to one of 2 tenant networks, which
plugged into single router. The traffic goes from one network to the other (L3
east-west).

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - single_room
      - compute_nodes: 2
      template: l3_east_west.hot
    description: In this scenario Shaker launches 1 pair of instances, each instance on
      its own compute node. Instances are connected to one of 2 tenant networks, which
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
    file_name: shaker/shaker/scenarios/openstack/perf_l3_east_west.yaml
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

.. image:: 52751a66-4acd-4ecd-80ec-2722692dd601.*

**Stats**:

=============  ========  ========  ========
Metric         Min       Avg       Max     
=============  ========  ========  ========
ping_icmp, ms      0.26      0.51      0.90
=============  ========  ========  ========

**SLA**:

=========================  ===========  ===================  ========
Expression                 Concurrency  Node                 Result  
=========================  ===========  ===================  ========
stats.ping_icmp.avg < 2.0            1  node-248.domain.tld  OK
=========================  ===========  ===================  ========

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

.. image:: eba8ca00-5402-44ab-93d3-2bc0a32baad5.*

**Stats**:

=================  ========  ========  ========
Metric             Min       Avg       Max     
=================  ========  ========  ========
bandwidth, Mbit/s   9309.96   9376.98   9389.82
retransmits                         1        98
=================  ========  ========  ========

**SLA**:

==========================  ===========  ===================  ========
Expression                  Concurrency  Node                 Result  
==========================  ===========  ===================  ========
stats.bandwidth.avg > 5000            1  node-248.domain.tld  OK
stats.retransmits.max < 10            1  node-248.domain.tld  FAIL
==========================  ===========  ===================  ========

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

.. image:: 0c603cc9-dfa2-4ccd-8e9f-3c167bdd27b7.*

**Stats**:

============  ========  ========  ========
Metric        Min       Avg       Max     
============  ========  ========  ========
loss, %                     0.00
jitter, ms                  0.00
packets, pps    134550    142620    150010
============  ========  ========  ========

**SLA**:

==========================  ===========  ===================  ========
Expression                  Concurrency  Node                 Result  
==========================  ===========  ===================  ========
stats.packets.avg > 100000            1  node-248.domain.tld  OK
==========================  ===========  ===================  ========

