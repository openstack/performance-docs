.. _openstack_l2_performance:

OpenStack L2 Performance 2 nodes
********************************

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
    file_name: shaker/shaker/scenarios/openstack/perf_l2.yaml
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

.. image:: 040fbe4a-8b9d-4288-bd53-23133ab0d780.*

**Stats**:

=============  ========  ========  ========
Metric         Min       Avg       Max     
=============  ========  ========  ========
ping_icmp, ms      0.26      0.43      1.12
=============  ========  ========  ========

**SLA**:

=========================  ===========  ===================  ========
Expression                 Concurrency  Node                 Result  
=========================  ===========  ===================  ========
stats.ping_icmp.avg < 2.0            1  node-228.domain.tld  OK
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

.. image:: d4d58e1d-355b-421b-830e-431e97e594b1.*

**Stats**:

=================  ========  ========  ========
Metric             Min       Avg       Max     
=================  ========  ========  ========
bandwidth, Mbit/s   9309.98   9378.30   9390.23
retransmits                         1       104
=================  ========  ========  ========

**SLA**:

==========================  ===========  ===================  ========
Expression                  Concurrency  Node                 Result  
==========================  ===========  ===================  ========
stats.bandwidth.avg > 5000            1  node-228.domain.tld  OK
stats.retransmits.max < 10            1  node-228.domain.tld  FAIL
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

.. image:: e7e6243f-d0ed-43f9-a75c-13874be522a3.*

**Stats**:

============  ========  ========  ========
Metric        Min       Avg       Max     
============  ========  ========  ========
loss, %                     4.09
jitter, ms                  0.01
packets, pps    190320    199583    213660
============  ========  ========  ========

**SLA**:

==========================  ===========  ===================  ========
Expression                  Concurrency  Node                 Result  
==========================  ===========  ===================  ========
stats.packets.avg > 100000            1  node-228.domain.tld  OK
==========================  ===========  ===================  ========

