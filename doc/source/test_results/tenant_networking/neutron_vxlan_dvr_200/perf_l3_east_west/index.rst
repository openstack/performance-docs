.. _openstack_l3_east_west_performance:

OpenStack L3 East-West Performance
**********************************

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
    file_name: /opt/stack/.venv/local/lib/python2.7/site-packages/shaker/scenarios/openstack/perf_l3_east_west.yaml
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

.. image:: 62f33859-d3eb-401f-b002-f77af299090d.*

**Stats**:

=============  ========  ========  ========
Metric         Min       Avg       Max     
=============  ========  ========  ========
ping_icmp, ms      0.54      0.71      1.24
=============  ========  ========  ========

**SLA**:

=========================  ===========  ===================  ========
Expression                 Concurrency  Node                 Result
=========================  ===========  ===================  ========
stats.ping_icmp.avg < 2.0            1  node-164.domain.tld  OK
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

.. image:: 7f38e7b9-498a-4e82-b928-aa0dc5641d7f.*

**Stats**:

=================  ========  ========  ========
Metric             Min       Avg       Max
=================  ========  ========  ========
bandwidth, Mbit/s   5405.46   5812.68   7309.81
retransmits                                  13
=================  ========  ========  ========

**SLA**:

==========================  ===========  ===================  ========
Expression                  Concurrency  Node                 Result
==========================  ===========  ===================  ========
stats.bandwidth.avg > 5000            1  node-164.domain.tld  OK
stats.retransmits.max < 10            1  node-164.domain.tld  FAIL
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

.. image:: 3dcd5b03-943e-44d0-9e8c-3ef79c424d4e.*

**Stats**:

============  =========  =========  =========
Metric        Min        Avg        Max
============  =========  =========  =========
loss, %                      0.005
jitter, ms                   0.004
packets, pps     138870     153702     165970
============  =========  =========  =========

**SLA**:

==========================  ===========  ===================  ========
Expression                  Concurrency  Node                 Result  
==========================  ===========  ===================  ========
stats.packets.avg > 100000            1  node-164.domain.tld  OK
==========================  ===========  ===================  ========

