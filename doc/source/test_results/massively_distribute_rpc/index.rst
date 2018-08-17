Massively Distributed RPCs report
=================================

Below there are the results of the `test plan of massively distributed RPCs`__.

.. _mdrpc: ../../test_plans/massively_distribute_rpc/plan.html

__ mdrpc_

Test Environment
^^^^^^^^^^^^^^^^

Environment Description
=======================

Hardware
--------

Paravance cluster (72 nodes) of Rennes site at `Grid'5000`__ testbed.

.. _grid5000: https://www.grid5000.fr/mediawiki/index.php/Rennes:Hardware#paravance

__ grid5000_


+-------------+------------------------------------------------------------------+
| **Model**   | Dell PowerEdge R630                                              |
+-------------+------------------------------------------------------------------+
| **CPU**     | Intel Xeon E5-2630 v3 Haswell 2.40GHz (2 CPUs/node, 8 cores/CPU) |
+-------------+------------------------------------------------------------------+
| **Memory**  | 128 GB                                                           |
+-------------+------------------------------------------------------------------+
| **Storage** | 558 GB HDD SATA ST600MM0006 (x2)                                 |
|             +------------------------------------------------------------------+
|             | driver: ahci                                                     |
+-------------+------------------------------------------------------------------+
| **Network** | eth0/eno1, Ethernet                                              |
|             +------------------------------------------------------------------+
|             | configured rate: 10 Gbps                                         |
|             +------------------------------------------------------------------+
|             | model: Intel 82599ES 10-Gigabit SFI/SFP+ Network Connection      |
|             +------------------------------------------------------------------+
|             | driver: ixgbe                                                    |
|             +------------------------------------------------------------------+
|             +------------------------------------------------------------------+
|             | eth1/eno2, Ethernet                                              |
|             +------------------------------------------------------------------+
|             | configured rate: 10 Gbps                                         |
|             +------------------------------------------------------------------+
|             | model: Intel 82599ES 10-Gigabit SFI/SFP+ Network Connection      |
|             +------------------------------------------------------------------+
|             | driver: ixgbe                                                    |
+-------------+------------------------------------------------------------------+


Software
--------


+-----------------------+------------------------------+
| **OS**                | Debian 9 "Stretch"           |
+-----------------------+------------------------------+
| **oslo.messaging**    | 5.35.0                       |
+-----------------------+------------------------------+
| **pyngus**            | 2.2.2                        |
+-----------------------+------------------------------+
| **ombt**              | 2.3.0 (a3f0fc7_)             |
+-----------------------+------------------------------+
| **ombt-orchestrator** | 1.x                          |
+-----------------------+------------------------------+
| **broker**            | RabbitMQ server 3.6.x        |
+-----------------------+------------------------------+
| **router**            | QP dispatch server 1.0.1     |
+-----------------------+------------------------------+
| **topology**          | complete_graph (router only) |
+-----------------------+------------------------------+

.. _a3f0fc7: https://github.com/kgiusti/ombt/commit/a3f0fc79502a9219b6417418e31fb7a862254657


Test Case 1
^^^^^^^^^^^

Latency
-------

Driver and Call Type 
~~~~~~~~~~~~~~~~~~~~


.. |bm1l| image:: tc1/latency-1-rabbitmq_rpc-call.png
    :scale: 20

.. |bl1l| image:: tc1/latency-1-rabbitmq_rpc-call-boxplot.png
    :scale: 20

.. |bd1l| image:: tc1/latency-1-rabbitmq_rpc-call-distribution.png
    :scale: 17
            
.. |bm1t| image:: tc1/latency-1-rabbitmq_rpc-cast.png
    :scale: 20

.. |bl1t| image:: tc1/latency-1-rabbitmq_rpc-cast-boxplot.png
    :scale: 20

.. |bd1t| image:: tc1/latency-1-rabbitmq_rpc-cast-distribution.png
    :scale: 17

.. |rm1l| image:: tc1/latency-1-router_rpc-call.png
    :scale: 20

.. |rl1l| image:: tc1/latency-1-router_rpc-call-boxplot.png
    :scale: 20

.. |rd1l| image:: tc1/latency-1-router_rpc-call-distribution.png
    :scale: 17
            
.. |rm1t| image:: tc1/latency-1-router_rpc-cast.png
    :scale: 20

.. |rl1t| image:: tc1/latency-1-router_rpc-cast-boxplot.png
    :scale: 20

.. |rd1t| image:: tc1/latency-1-router_rpc-cast-distribution.png
    :scale: 17

.. |bm3l| image:: tc1/latency-3-rabbitmq_rpc-call.png
    :scale: 20

.. |bl3l| image:: tc1/latency-3-rabbitmq_rpc-call-boxplot.png
    :scale: 20

.. |bd3l| image:: tc1/latency-3-rabbitmq_rpc-call-distribution.png
    :scale: 17
            
.. |bm3t| image:: tc1/latency-3-rabbitmq_rpc-cast.png
    :scale: 20

.. |bl3t| image:: tc1/latency-3-rabbitmq_rpc-cast-boxplot.png
    :scale: 20

.. |bd3t| image:: tc1/latency-3-rabbitmq_rpc-cast-distribution.png
    :scale: 17

.. |rm3l| image:: tc1/latency-3-router_rpc-call.png
    :scale: 20

.. |rl3l| image:: tc1/latency-3-router_rpc-call-boxplot.png
    :scale: 20

.. |rd3l| image:: tc1/latency-3-router_rpc-call-distribution.png
    :scale: 17
            
.. |rm3t| image:: tc1/latency-3-router_rpc-cast.png
    :scale: 20

.. |rl3t| image:: tc1/latency-3-router_rpc-cast-boxplot.png
    :scale: 20

.. |rd3t| image:: tc1/latency-3-router_rpc-cast-distribution.png
    :scale: 17

.. |bm5l| image:: tc1/latency-5-rabbitmq_rpc-call.png
    :scale: 20

.. |bl5l| image:: tc1/latency-5-rabbitmq_rpc-call-boxplot.png
    :scale: 20

.. |bd5l| image:: tc1/latency-5-rabbitmq_rpc-call-distribution.png
    :scale: 17
            
.. |bm5t| image:: tc1/latency-5-rabbitmq_rpc-cast.png
    :scale: 20

.. |bl5t| image:: tc1/latency-5-rabbitmq_rpc-cast-boxplot.png
    :scale: 20

.. |bd5t| image:: tc1/latency-5-rabbitmq_rpc-cast-distribution.png
    :scale: 17

.. |rm5l| image:: tc1/latency-5-router_rpc-call.png
    :scale: 20

.. |rl5l| image:: tc1/latency-5-router_rpc-call-boxplot.png
    :scale: 20

.. |rd5l| image:: tc1/latency-5-router_rpc-call-distribution.png
    :scale: 17
            
.. |rm5t| image:: tc1/latency-5-router_rpc-cast.png
    :scale: 20

.. |rl5t| image:: tc1/latency-5-router_rpc-cast-boxplot.png
    :scale: 20

.. |rd5t| image:: tc1/latency-5-router_rpc-cast-distribution.png
    :scale: 17

  
+--------+-----------+----------+----------+---------+--------------+
| Driver | Instances | Type     | Messages | Latency | Distribution |
+========+===========+==========+==========+=========+==============+
| broker |         1 | rpc-call |   |bm1l| |  |bl1l| |       |bd1l| |
+--------+-----------+----------+----------+---------+--------------+                                                                                                                        
| broker |         1 | rpc-cast |   |bm1t| |  |bl1t| |       |bd1t| |
+--------+-----------+----------+----------+---------+--------------+                                                                                                                        
| router |         1 | rpc-call |   |rm1l| |  |rl1l| |       |rd1l| |
+--------+-----------+----------+----------+---------+--------------+                                                                                                                        
| router |         1 | rpc-cast |   |rm1t| |  |rl1t| |       |rd1t| |
+--------+-----------+----------+----------+---------+--------------+                                                            
| broker |         3 | rpc-call |   |bm3l| |  |bl3l| |       |bd3l| |
+--------+-----------+----------+----------+---------+--------------+                                                                                                                        
| broker |         3 | rpc-cast |   |bm3t| |  |bl3t| |       |bd3t| |
+--------+-----------+----------+----------+---------+--------------+                                                                                                                        
| router |         3 | rpc-call |   |rm3l| |  |rl3l| |       |rd3l| |
+--------+-----------+----------+----------+---------+--------------+                                                                                                                        
| router |         3 | rpc-cast |   |rm3t| |  |rl3t| |       |rd3t| |
+--------+-----------+----------+----------+---------+--------------+                                                            
| broker |         5 | rpc-call |   |bm5l| |  |bl5l| |       |bd5l| |
+--------+-----------+----------+----------+---------+--------------+                                                                                                                        
| broker |         5 | rpc-cast |   |bm5t| |  |bl5t| |       |bd5t| |
+--------+-----------+----------+----------+---------+--------------+                                                            
| router |         5 | rpc-call |   |rm5l| |  |rl5l| |       |rd5l| |
+--------+-----------+----------+----------+---------+--------------+                                                            
| router |         5 | rpc-cast |   |rm5t| |  |rl5t| |       |rd5t| |
+--------+-----------+----------+----------+---------+--------------+


Driver distribution comparison against number of clients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


+---------+------------------------------------------+------------------------------------------+
| Clients | rpc-call                                 | rpc-cast                                 |
+=========+==========================================+==========================================+
| 1000    |.. image:: tc1/latency-rpc-call_1000.png  |.. image:: tc1/latency-rpc-cast_1000.png  |
|         |   :scale: 35                             |   :scale: 35                             |
+---------+------------------------------------------+------------------------------------------+
| 2000    |.. image:: tc1/latency-rpc-call_2000.png  |.. image:: tc1/latency-rpc-cast_2000.png  |
|         |   :scale: 35                             |   :scale: 35                             |
+---------+------------------------------------------+------------------------------------------+
| 4000    |.. image:: tc1/latency-rpc-call_4000.png  |.. image:: tc1/latency-rpc-cast_4000.png  |
|         |   :scale: 35                             |   :scale: 35                             |
+---------+------------------------------------------+------------------------------------------+
| 6000    |.. image:: tc1/latency-rpc-call_6000.png  |.. image:: tc1/latency-rpc-cast_6000.png  |
|         |   :scale: 35                             |   :scale: 35                             |
+---------+------------------------------------------+------------------------------------------+
| 8000    |.. image:: tc1/latency-rpc-call_8000.png  |.. image:: tc1/latency-rpc-cast_8000.png  |
|         |   :scale: 35                             |   :scale: 35                             |
+---------+------------------------------------------+------------------------------------------+
| 10000   |.. image:: tc1/latency-rpc-call_10000.png |.. image:: tc1/latency-rpc-cast_10000.png |
|         |   :scale: 35                             |   :scale: 35                             |
+---------+------------------------------------------+------------------------------------------+


RPC-CALL metrics
----------------

Metric results show maximum (collected) values for each case.

Memory usage on the bus
~~~~~~~~~~~~~~~~~~~~~~~


.. |bm30l| image:: tc1/usage_mem_bus-3-rabbitmq_0-rpc-call.png
    :scale: 15

.. |bm31l| image:: tc1/usage_mem_bus-3-rabbitmq_1-rpc-call.png
    :scale: 15

.. |bm32l| image:: tc1/usage_mem_bus-3-rabbitmq_2-rpc-call.png
    :scale: 15        

.. |rm30l| image:: tc1/usage_mem_bus-3-router_0-rpc-call.png
    :scale: 15

.. |rm31l| image:: tc1/usage_mem_bus-3-router_1-rpc-call.png
    :scale: 15

.. |rm32l| image:: tc1/usage_mem_bus-3-router_2-rpc-call.png
    :scale: 15

.. |bm50l| image:: tc1/usage_mem_bus-5-rabbitmq_0-rpc-call.png
    :scale: 15

.. |bm51l| image:: tc1/usage_mem_bus-5-rabbitmq_1-rpc-call.png
    :scale: 15

.. |bm52l| image:: tc1/usage_mem_bus-5-rabbitmq_2-rpc-call.png
    :scale: 15        

.. |bm53l| image:: tc1/usage_mem_bus-5-rabbitmq_3-rpc-call.png
    :scale: 15

.. |bm54l| image:: tc1/usage_mem_bus-5-rabbitmq_4-rpc-call.png
    :scale: 15        

.. |rm50l| image:: tc1/usage_mem_bus-5-router_0-rpc-call.png
    :scale: 15

.. |rm51l| image:: tc1/usage_mem_bus-5-router_1-rpc-call.png
    :scale: 15

.. |rm52l| image:: tc1/usage_mem_bus-5-router_2-rpc-call.png
    :scale: 15
            
.. |rm53l| image:: tc1/usage_mem_bus-5-router_3-rpc-call.png
    :scale: 15

.. |rm54l| image:: tc1/usage_mem_bus-5-router_4-rpc-call.png
    :scale: 15


+--------+-----------+-------------------------------------------------------+
| Driver | Instances | Memory                                                |
+========+===========+=======================================================+
| broker |         1 |.. image:: tc1/usage_mem_bus-1-rabbitmq_0-rpc-call.png |
|        |           |   :scale: 15                                          |
+--------+-----------+-------------------------------------------------------+
| router |         1 |.. image:: tc1/usage_mem_bus-1-router_0-rpc-call.png   |
|        |           |   :scale: 15                                          |
+--------+-----------+-------------------------------------------------------+
| broker |         3 |  |bm30l| |bm31l| |bm32l|                              |
+--------+-----------+-------------------------------------------------------+
| router |         3 |  |rm30l| |rm31l| |rm32l|                              |
+--------+-----------+-------------------------------------------------------+
| broker |         5 |  |bm50l| |bm51l| |bm52l| |bm53l| |bm54l|              |
+--------+-----------+-------------------------------------------------------+
| router |         5 |  |rm50l| |rm51l| |rm52l| |rm53l| |rm54l|              |
+--------+-----------+-------------------------------------------------------+


CPU usage on the bus
~~~~~~~~~~~~~~~~~~~~


.. |bc30l| image:: tc1/usage_cpu_percent_bus-3-rabbitmq_0-rpc-call.png
    :scale: 15

.. |bc31l| image:: tc1/usage_cpu_percent_bus-3-rabbitmq_1-rpc-call.png
    :scale: 15

.. |bc32l| image:: tc1/usage_cpu_percent_bus-3-rabbitmq_2-rpc-call.png
    :scale: 15        

.. |rc30l| image:: tc1/usage_cpu_percent_bus-3-router_0-rpc-call.png
    :scale: 15

.. |rc31l| image:: tc1/usage_cpu_percent_bus-3-router_1-rpc-call.png
    :scale: 15

.. |rc32l| image:: tc1/usage_cpu_percent_bus-3-router_2-rpc-call.png
    :scale: 15

.. |bc50l| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_0-rpc-call.png
    :scale: 15

.. |bc51l| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_1-rpc-call.png
    :scale: 15

.. |bc52l| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_2-rpc-call.png
    :scale: 15        

.. |bc53l| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_3-rpc-call.png
    :scale: 15

.. |bc54l| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_4-rpc-call.png
    :scale: 15        

.. |rc50l| image:: tc1/usage_cpu_percent_bus-5-router_0-rpc-call.png
    :scale: 15

.. |rc51l| image:: tc1/usage_cpu_percent_bus-5-router_1-rpc-call.png
    :scale: 15

.. |rc52l| image:: tc1/usage_cpu_percent_bus-5-router_2-rpc-call.png
    :scale: 15
            
.. |rc53l| image:: tc1/usage_cpu_percent_bus-5-router_3-rpc-call.png
    :scale: 15

.. |rc54l| image:: tc1/usage_cpu_percent_bus-5-router_4-rpc-call.png
    :scale: 15


+--------+-----------+---------------------------------------------------------------+
| Driver | Instances | CPU                                                           |
+========+===========+===============================================================+
| broker |         1 |.. image:: tc1/usage_cpu_percent_bus-1-rabbitmq_0-rpc-call.png |
|        |           |   :scale: 15                                                  |
+--------+-----------+---------------------------------------------------------------+
| router |         1 |.. image:: tc1/usage_cpu_percent_bus-1-router_0-rpc-call.png   |
|        |           |   :scale: 15                                                  |
+--------+-----------+---------------------------------------------------------------+
| broker |         3 |  |bc30l| |bc31l| |bc32l|                                      |
+--------+-----------+---------------------------------------------------------------+
| router |         3 |  |rc30l| |rc31l| |rc32l|                                      |
+--------+-----------+---------------------------------------------------------------+
| broker |         5 |  |bc50l| |bc51l| |bc52l| |bc53l| |bc54l|                      |
+--------+-----------+---------------------------------------------------------------+
| router |         5 |  |rc50l| |rc51l| |rc52l| |rc53l| |rc54l|                      |
+--------+-----------+---------------------------------------------------------------+


TCP connections on the bus
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. |bt30l| image:: tc1/tcp_established_bus-3-rabbitmq_0-rpc-call.png 
    :scale: 15

.. |bt31l| image:: tc1/tcp_established_bus-3-rabbitmq_2-rpc-call.png 
    :scale: 15

.. |bt32l| image:: tc1/tcp_established_bus-3-rabbitmq_4-rpc-call.png 
    :scale: 15        

.. |rt30l| image:: tc1/tcp_established_bus-3-router_0-rpc-call.png
    :scale: 15

.. |rt31l| image:: tc1/tcp_established_bus-3-router_2-rpc-call.png
    :scale: 15

.. |rt32l| image:: tc1/tcp_established_bus-3-router_4-rpc-call.png
    :scale: 15

.. |bt50l| image:: tc1/tcp_established_bus-5-rabbitmq_0-rpc-call.png 
    :scale: 15

.. |bt51l| image:: tc1/tcp_established_bus-5-rabbitmq_1-rpc-call.png 
    :scale: 15

.. |bt52l| image:: tc1/tcp_established_bus-5-rabbitmq_2-rpc-call.png 
    :scale: 15        

.. |bt53l| image:: tc1/tcp_established_bus-5-rabbitmq_3-rpc-call.png 
    :scale: 15

.. |bt54l| image:: tc1/tcp_established_bus-5-rabbitmq_4-rpc-call.png 
    :scale: 15        

.. |rt50l| image:: tc1/tcp_established_bus-5-router_0-rpc-call.png
    :scale: 15

.. |rt51l| image:: tc1/tcp_established_bus-5-router_1-rpc-call.png
    :scale: 15

.. |rt52l| image:: tc1/tcp_established_bus-5-router_2-rpc-call.png
    :scale: 15
            
.. |rt53l| image:: tc1/tcp_established_bus-5-router_3-rpc-call.png
    :scale: 15

.. |rt54l| image:: tc1/tcp_established_bus-5-router_4-rpc-call.png
    :scale: 15


+--------+-----------+-------------------------------------------------------------+
| Driver | Instances | TCP connections                                             |
+========+===========+=============================================================+
| broker |         1 |.. image:: tc1/tcp_established_bus-1-rabbitmq_4-rpc-call.png |
|        |           |   :scale: 15                                                |
+--------+-----------+-------------------------------------------------------------+
| router |         1 |.. image:: tc1/tcp_established_bus-1-router_4-rpc-call.png   |
|        |           |   :scale: 15                                                |
+--------+-----------+-------------------------------------------------------------+
| broker |         3 |  |bt30l| |bt31l| |bt32l|                                    |
+--------+-----------+-------------------------------------------------------------+
| router |         3 |  |rt30l| |rt31l| |rt32l|                                    |
+--------+-----------+-------------------------------------------------------------+
| broker |         5 |  |bt50l| |bt51l| |bt52l| |bt53l| |bt54l|                    |
+--------+-----------+-------------------------------------------------------------+
| router |         5 |  |rt50l| |rt51l| |rt52l| |rt53l| |rt54l|                    |
+--------+-----------+-------------------------------------------------------------+


Network traffic on the bus
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. |bo30l| image:: tc1/net_sent_bus-3-rabbitmq_2-rpc-call.png
    :scale: 15

.. |bo31l| image:: tc1/net_sent_bus-3-rabbitmq_3-rpc-call.png
    :scale: 15

.. |bo32l| image:: tc1/net_sent_bus-3-rabbitmq_4-rpc-call.png
    :scale: 15         

.. |ro30l| image:: tc1/net_sent_bus-3-router_2-rpc-call.png
    :scale: 15

.. |ro31l| image:: tc1/net_sent_bus-3-router_3-rpc-call.png
    :scale: 15

.. |ro32l| image:: tc1/net_sent_bus-3-router_4-rpc-call.png
    :scale: 15

.. |bo50l| image:: tc1/net_sent_bus-5-rabbitmq_0-rpc-call.png
    :scale: 15

.. |bo51l| image:: tc1/net_sent_bus-5-rabbitmq_1-rpc-call.png
    :scale: 15

.. |bo52l| image:: tc1/net_sent_bus-5-rabbitmq_2-rpc-call.png
    :scale: 15         

.. |bo53l| image:: tc1/net_sent_bus-5-rabbitmq_3-rpc-call.png
    :scale: 15

.. |bo54l| image:: tc1/net_sent_bus-5-rabbitmq_4-rpc-call.png
    :scale: 15         

.. |ro50l| image:: tc1/net_sent_bus-5-router_0-rpc-call.png
    :scale: 15

.. |ro51l| image:: tc1/net_sent_bus-5-router_1-rpc-call.png
    :scale: 15

.. |ro52l| image:: tc1/net_sent_bus-5-router_2-rpc-call.png
    :scale: 15
            
.. |ro53l| image:: tc1/net_sent_bus-5-router_3-rpc-call.png
    :scale: 15

.. |ro54l| image:: tc1/net_sent_bus-5-router_4-rpc-call.png
    :scale: 15

.. |bi30l| image:: tc1/net_recv_bus-3-rabbitmq_2-rpc-call.png
    :scale: 15                                               
                                                             
.. |bi31l| image:: tc1/net_recv_bus-3-rabbitmq_3-rpc-call.png
    :scale: 15                                               
                                                             
.. |bi32l| image:: tc1/net_recv_bus-3-rabbitmq_4-rpc-call.png
    :scale: 15         

.. |ri30l| image:: tc1/net_recv_bus-3-router_2-rpc-call.png
    :scale: 15

.. |ri31l| image:: tc1/net_recv_bus-3-router_3-rpc-call.png
    :scale: 15

.. |ri32l| image:: tc1/net_recv_bus-3-router_4-rpc-call.png
    :scale: 15

.. |bi50l| image:: tc1/net_recv_bus-5-rabbitmq_0-rpc-call.png
    :scale: 15                                               
                                                             
.. |bi51l| image:: tc1/net_recv_bus-5-rabbitmq_1-rpc-call.png
    :scale: 15                                               
                                                             
.. |bi52l| image:: tc1/net_recv_bus-5-rabbitmq_2-rpc-call.png
    :scale: 15                                               
                                                             
.. |bi53l| image:: tc1/net_recv_bus-5-rabbitmq_3-rpc-call.png
    :scale: 15                                               
                                                             
.. |bi54l| image:: tc1/net_recv_bus-5-rabbitmq_4-rpc-call.png
    :scale: 15         

.. |ri50l| image:: tc1/net_recv_bus-5-router_0-rpc-call.png
    :scale: 15

.. |ri51l| image:: tc1/net_recv_bus-5-router_1-rpc-call.png
    :scale: 15

.. |ri52l| image:: tc1/net_recv_bus-5-router_1-rpc-call.png
    :scale: 15
            
.. |ri53l| image:: tc1/net_recv_bus-5-router_2-rpc-call.png
    :scale: 15

.. |ri54l| image:: tc1/net_recv_bus-5-router_3-rpc-call.png
    :scale: 15

            
+--------+-----------+------+------------------------------------------------------+
| Driver | Instances | Type | TCP connections                                      |
+========+===========+======+======================================================+
| broker |         1 | Sent |.. image:: tc1/net_sent_bus-1-rabbitmq_2-rpc-call.png |
|        |           |      |   :scale: 15                                         |
+--------+-----------+------+------------------------------------------------------+
| broker |         1 | Recv |.. image:: tc1/net_recv_bus-1-rabbitmq_2-rpc-call.png |
|        |           |      |   :scale: 15                                         |
+--------+-----------+------+------------------------------------------------------+
| router |         1 | Sent |.. image:: tc1/net_sent_bus-1-router_2-rpc-call.png   |
|        |           |      |   :scale: 15                                         |
+--------+-----------+------+------------------------------------------------------+
| router |         1 | Recv |.. image:: tc1/net_recv_bus-1-router_2-rpc-call.png   |
|        |           |      |   :scale: 15                                         |
+--------+-----------+------+------------------------------------------------------+
| broker |         3 | Sent | |bo30l| |bo31l| |bo32l|                              |
+--------+-----------+------+------------------------------------------------------+
| broker |         3 | Recv | |bi30l| |bi31l| |bi32l|                              |
+--------+-----------+------+------------------------------------------------------+
| router |         3 | Sent | |ro30l| |ro31l| |ro32l|                              |
+--------+-----------+------+------------------------------------------------------+
| router |         3 | Recv | |ri30l| |ri31l| |ri32l|                              |
+--------+-----------+------+------------------------------------------------------+
| broker |         5 | Sent | |bo50l| |bo51l| |bo52l| |bo53l| |bo54l|              |
+--------+-----------+------+------------------------------------------------------+
| broker |         5 | Recv | |bi50l| |bi51l| |bi52l| |bi53l| |bi54l|              |
+--------+-----------+------+------------------------------------------------------+
| router |         5 | Sent | |ro50l| |ro51l| |ro52l| |ro53l| |ro54l|              |
+--------+-----------+------+------------------------------------------------------+
| router |         5 | Recv | |ri50l| |ri51l| |ri52l| |ri53l| |ri54l|              |
+--------+-----------+------+------------------------------------------------------+


..
   Metrics of the Ombt server
   ~~~~~~~~~~~~~~~~~~~~~~~~~~

   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | Driver | Instances | Memory                                               | CPU                                                   |
   +========+===========+======================================================+=======================================================+
   | broker |         1 |.. image:: tc1/mem-ombt-serv-broker-1_call.png | .. image:: tc1/cpu-ombt-serv-broker-1_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | router |         1 |.. image:: tc1/mem-ombt-serv-router-1_call.png | .. image:: tc1/cpu-ombt-serv-broker-1_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | broker |         3 |.. image:: tc1/mem-ombt-serv-broker-3_call.png | .. image:: tc1/cpu-ombt-serv-broker-3_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | router |         3 |.. image:: tc1/mem-ombt-serv-router-3_call.png | .. image:: tc1/cpu-ombt-serv-broker-3_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | broker |         5 |.. image:: tc1/mem-ombt-serv-broker-5_call.png | .. image:: tc1/cpu-ombt-serv-broker-5_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | router |         5 |.. image:: tc1/mem-ombt-serv-router-5_call.png | .. image:: tc1/cpu-ombt-serv-broker-5_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+

   Metrics of the Ombt client
   ~~~~~~~~~~~~~~~~~~~~~~~~~~

   +--------+-----------+--------------------------------------------------------+---------------------------------------------------------+
   | Driver | Instances | Memory                                                 | CPU                                                     |
   +========+===========+========================================================+=========================================================+
   | broker |         1 |.. image:: tc1/mem-ombt-client-broker-1_call.png | .. image:: tc1/cpu-ombt-client-broker-1_call.png |
   |        |           |   :scale: 20                                           |    :scale: 20                                           |
   +--------+-----------+--------------------------------------------------------+---------------------------------------------------------+
   | router |         1 |.. image:: tc1/mem-ombt-client-router-1_call.png | .. image:: tc1/cpu-ombt-client-broker-1_call.png |
   |        |           |   :scale: 20                                           |    :scale: 20                                           |
   +--------+-----------+--------------------------------------------------------+---------------------------------------------------------+
   | broker |         3 |.. image:: tc1/mem-ombt-client-broker-3_call.png | .. image:: tc1/cpu-ombt-client-broker-3_call.png |
   |        |           |   :scale: 20                                           |    :scale: 20                                           |
   +--------+-----------+--------------------------------------------------------+---------------------------------------------------------+
   | router |         3 |.. image:: tc1/mem-ombt-client-router-3_call.png | .. image:: tc1/cpu-ombt-client-broker-3_call.png |
   |        |           |   :scale: 20                                           |    :scale: 20                                           |
   +--------+-----------+--------------------------------------------------------+---------------------------------------------------------+
   | broker |         5 |.. image:: tc1/mem-ombt-client-broker-5_call.png | .. image:: tc1/cpu-ombt-client-broker-5_call.png |
   |        |           |   :scale: 20                                           |    :scale: 20                                           |
   +--------+-----------+--------------------------------------------------------+---------------------------------------------------------+
   | router |         5 |.. image:: tc1/mem-ombt-client-router-5_call.png | .. image:: tc1/cpu-ombt-client-broker-5_call.png |
   |        |           |   :scale: 20                                           |    :scale: 20                                           |
   +--------+-----------+--------------------------------------------------------+---------------------------------------------------------+

   Metrics of the Ombt controller
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | Driver | Instances | Memory                                               | CPU                                                   |
   +========+===========+======================================================+=======================================================+
   | broker |         1 |.. image:: tc1/mem-ombt-ctrl-broker-1_call.png | .. image:: tc1/cpu-ombt-ctrl-broker-1_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | router |         1 |.. image:: tc1/mem-ombt-ctrl-router-1_call.png | .. image:: tc1/cpu-ombt-ctrl-broker-1_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | broker |         3 |.. image:: tc1/mem-ombt-ctrl-broker-3_call.png | .. image:: tc1/cpu-ombt-ctrl-broker-3_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | router |         3 |.. image:: tc1/mem-ombt-ctrl-router-3_call.png | .. image:: tc1/cpu-ombt-ctrl-broker-3_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | broker |         5 |.. image:: tc1/mem-ombt-ctrl-broker-5_call.png | .. image:: tc1/cpu-ombt-ctrl-broker-5_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+
   | router |         5 |.. image:: tc1/mem-ombt-ctrl-router-5_call.png | .. image:: tc1/cpu-ombt-ctrl-broker-5_call.png |
   |        |           |   :scale: 20                                         |    :scale: 20                                         |
   +--------+-----------+------------------------------------------------------+-------------------------------------------------------+


RPC-CAST metrics
----------------

Metric results show maximum (collected) values for each case as previous case.


Note that the max of Y range is not the same as metrics of RPC-CALL.

Memory usage on the bus
~~~~~~~~~~~~~~~~~~~~~~~


.. |bm30t| image:: tc1/usage_mem_bus-3-rabbitmq_0-rpc-cast.png
    :scale: 15

.. |bm31t| image:: tc1/usage_mem_bus-3-rabbitmq_1-rpc-cast.png
    :scale: 15

.. |bm32t| image:: tc1/usage_mem_bus-3-rabbitmq_2-rpc-cast.png
    :scale: 15        

.. |rm30t| image:: tc1/usage_mem_bus-3-router_0-rpc-cast.png
    :scale: 15

.. |rm31t| image:: tc1/usage_mem_bus-3-router_1-rpc-cast.png
    :scale: 15

.. |rm32t| image:: tc1/usage_mem_bus-3-router_2-rpc-cast.png
    :scale: 15

.. |bm50t| image:: tc1/usage_mem_bus-5-rabbitmq_0-rpc-cast.png
    :scale: 15

.. |bm51t| image:: tc1/usage_mem_bus-5-rabbitmq_1-rpc-cast.png
    :scale: 15

.. |bm52t| image:: tc1/usage_mem_bus-5-rabbitmq_2-rpc-cast.png
    :scale: 15        

.. |bm53t| image:: tc1/usage_mem_bus-5-rabbitmq_3-rpc-cast.png
    :scale: 15

.. |bm54t| image:: tc1/usage_mem_bus-5-rabbitmq_4-rpc-cast.png
    :scale: 15        

.. |rm50t| image:: tc1/usage_mem_bus-5-router_0-rpc-cast.png
    :scale: 15

.. |rm51t| image:: tc1/usage_mem_bus-5-router_1-rpc-cast.png
    :scale: 15

.. |rm52t| image:: tc1/usage_mem_bus-5-router_2-rpc-cast.png
    :scale: 15
            
.. |rm53t| image:: tc1/usage_mem_bus-5-router_3-rpc-cast.png
    :scale: 15

.. |rm54t| image:: tc1/usage_mem_bus-5-router_4-rpc-cast.png
    :scale: 15


+--------+-----------+-------------------------------------------------------+
| Driver | Instances | Memory                                                |
+========+===========+=======================================================+
| broker |         1 |.. image:: tc1/usage_mem_bus-1-rabbitmq_0-rpc-cast.png |
|        |           |   :scale: 15                                          |
+--------+-----------+-------------------------------------------------------+
| router |         1 |.. image:: tc1/usage_mem_bus-1-router_0-rpc-cast.png   |
|        |           |   :scale: 15                                          |
+--------+-----------+-------------------------------------------------------+
| broker |         3 |  |bm30t| |bm31t| |bm32t|                              |
+--------+-----------+-------------------------------------------------------+
| router |         3 |  |rm30t| |rm31t| |rm32t|                              |
+--------+-----------+-------------------------------------------------------+
| broker |         5 |  |bm50t| |bm51t| |bm52t| |bm53t| |bm54t|              |
+--------+-----------+-------------------------------------------------------+
| router |         5 |  |rm50t| |rm51t| |rm52t| |rm53t| |rm54t|              |
+--------+-----------+-------------------------------------------------------+


CPU usage on the bus
~~~~~~~~~~~~~~~~~~~~


.. |bc30t| image:: tc1/usage_cpu_percent_bus-3-rabbitmq_0-rpc-cast.png
    :scale: 15

.. |bc31t| image:: tc1/usage_cpu_percent_bus-3-rabbitmq_1-rpc-cast.png
    :scale: 15

.. |bc32t| image:: tc1/usage_cpu_percent_bus-3-rabbitmq_2-rpc-cast.png
    :scale: 15        

.. |rc30t| image:: tc1/usage_cpu_percent_bus-3-router_0-rpc-cast.png
    :scale: 15

.. |rc31t| image:: tc1/usage_cpu_percent_bus-3-router_1-rpc-cast.png
    :scale: 15

.. |rc32t| image:: tc1/usage_cpu_percent_bus-3-router_2-rpc-cast.png
    :scale: 15

.. |bc50t| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_0-rpc-cast.png
    :scale: 15

.. |bc51t| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_1-rpc-cast.png
    :scale: 15

.. |bc52t| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_2-rpc-cast.png
    :scale: 15        

.. |bc53t| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_3-rpc-cast.png
    :scale: 15

.. |bc54t| image:: tc1/usage_cpu_percent_bus-5-rabbitmq_4-rpc-cast.png
    :scale: 15        

.. |rc50t| image:: tc1/usage_cpu_percent_bus-5-router_0-rpc-cast.png
    :scale: 15

.. |rc51t| image:: tc1/usage_cpu_percent_bus-5-router_1-rpc-cast.png
    :scale: 15

.. |rc52t| image:: tc1/usage_cpu_percent_bus-5-router_2-rpc-cast.png
    :scale: 15
            
.. |rc53t| image:: tc1/usage_cpu_percent_bus-5-router_3-rpc-cast.png
    :scale: 15

.. |rc54t| image:: tc1/usage_cpu_percent_bus-5-router_4-rpc-cast.png
    :scale: 15


+--------+-----------+---------------------------------------------------------------+
| Driver | Instances | CPU                                                           |
+========+===========+===============================================================+
| broker |         1 |.. image:: tc1/usage_cpu_percent_bus-1-rabbitmq_0-rpc-cast.png |
|        |           |   :scale: 15                                                  |
+--------+-----------+---------------------------------------------------------------+
| router |         1 |.. image:: tc1/usage_cpu_percent_bus-1-router_0-rpc-cast.png   |
|        |           |   :scale: 15                                                  |
+--------+-----------+---------------------------------------------------------------+
| broker |         3 |  |bc30t| |bc31t| |bc32t|                                      |
+--------+-----------+---------------------------------------------------------------+
| router |         3 |  |rc30t| |rc31t| |rc32t|                                      |
+--------+-----------+---------------------------------------------------------------+
| broker |         5 |  |bc50t| |bc51t| |bc52t| |bc53t| |bc54t|                      |
+--------+-----------+---------------------------------------------------------------+
| router |         5 |  |rc50t| |rc51t| |rc52t| |rc53t| |rc54t|                      |
+--------+-----------+---------------------------------------------------------------+


TCP connections on the bus
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. |bt30t| image:: tc1/tcp_established_bus-3-rabbitmq_0-rpc-cast.png 
    :scale: 15

.. |bt31t| image:: tc1/tcp_established_bus-3-rabbitmq_1-rpc-cast.png 
    :scale: 15

.. |bt32t| image:: tc1/tcp_established_bus-3-rabbitmq_3-rpc-cast.png 
    :scale: 15        

.. |rt30t| image:: tc1/tcp_established_bus-3-router_0-rpc-cast.png
    :scale: 15

.. |rt31t| image:: tc1/tcp_established_bus-3-router_1-rpc-cast.png
    :scale: 15

.. |rt32t| image:: tc1/tcp_established_bus-3-router_3-rpc-cast.png
    :scale: 15

.. |bt50t| image:: tc1/tcp_established_bus-5-rabbitmq_0-rpc-cast.png 
    :scale: 15

.. |bt51t| image:: tc1/tcp_established_bus-5-rabbitmq_1-rpc-cast.png 
    :scale: 15

.. |bt52t| image:: tc1/tcp_established_bus-5-rabbitmq_2-rpc-cast.png 
    :scale: 15        

.. |bt53t| image:: tc1/tcp_established_bus-5-rabbitmq_3-rpc-cast.png 
    :scale: 15

.. |bt54t| image:: tc1/tcp_established_bus-5-rabbitmq_4-rpc-cast.png 
    :scale: 15        

.. |rt50t| image:: tc1/tcp_established_bus-5-router_0-rpc-cast.png
    :scale: 15

.. |rt51t| image:: tc1/tcp_established_bus-5-router_1-rpc-cast.png
    :scale: 15

.. |rt52t| image:: tc1/tcp_established_bus-5-router_2-rpc-cast.png
    :scale: 15
            
.. |rt53t| image:: tc1/tcp_established_bus-5-router_3-rpc-cast.png
    :scale: 15

.. |rt54t| image:: tc1/tcp_established_bus-5-router_4-rpc-cast.png
    :scale: 15


+--------+-----------+-------------------------------------------------------------+
| Driver | Instances | TCP connections                                             |
+========+===========+=============================================================+
| broker |         1 |.. image:: tc1/tcp_established_bus-1-rabbitmq_4-rpc-cast.png |
|        |           |   :scale: 15                                                |
+--------+-----------+-------------------------------------------------------------+
| router |         1 |.. image:: tc1/tcp_established_bus-1-router_4-rpc-cast.png   |
|        |           |   :scale: 15                                                |
+--------+-----------+-------------------------------------------------------------+
| broker |         3 |  |bt30t| |bt31t| |bt32t|                                    |
+--------+-----------+-------------------------------------------------------------+
| router |         3 |  |rt30t| |rt31t| |rt32t|                                    |
+--------+-----------+-------------------------------------------------------------+
| broker |         5 |  |bt50t| |bt51t| |bt52t| |bt53t| |bt54t|                    |
+--------+-----------+-------------------------------------------------------------+
| router |         5 |  |rt50t| |rt51t| |rt52t| |rt53t| |rt54t|                    |
+--------+-----------+-------------------------------------------------------------+


Network traffic on the bus
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. |bo30t| image:: tc1/net_sent_bus-3-rabbitmq_0-rpc-cast.png
    :scale: 15

.. |bo31t| image:: tc1/net_sent_bus-3-rabbitmq_3-rpc-cast.png
    :scale: 15

.. |bo32t| image:: tc1/net_sent_bus-3-rabbitmq_4-rpc-cast.png
    :scale: 15         

.. |ro30t| image:: tc1/net_sent_bus-3-router_0-rpc-cast.png
    :scale: 15

.. |ro31t| image:: tc1/net_sent_bus-3-router_3-rpc-cast.png
    :scale: 15

.. |ro32t| image:: tc1/net_sent_bus-3-router_4-rpc-cast.png
    :scale: 15

.. |bo50t| image:: tc1/net_sent_bus-5-rabbitmq_0-rpc-cast.png
    :scale: 15

.. |bo51t| image:: tc1/net_sent_bus-5-rabbitmq_1-rpc-cast.png
    :scale: 15

.. |bo52t| image:: tc1/net_sent_bus-5-rabbitmq_2-rpc-cast.png
    :scale: 15         

.. |bo53t| image:: tc1/net_sent_bus-5-rabbitmq_3-rpc-cast.png
    :scale: 15

.. |bo54t| image:: tc1/net_sent_bus-5-rabbitmq_4-rpc-cast.png
    :scale: 15         

.. |ro50t| image:: tc1/net_sent_bus-5-router_0-rpc-cast.png
    :scale: 15

.. |ro51t| image:: tc1/net_sent_bus-5-router_1-rpc-cast.png
    :scale: 15

.. |ro52t| image:: tc1/net_sent_bus-5-router_2-rpc-cast.png
    :scale: 15
            
.. |ro53t| image:: tc1/net_sent_bus-5-router_3-rpc-cast.png
    :scale: 15

.. |ro54t| image:: tc1/net_sent_bus-5-router_4-rpc-cast.png
    :scale: 15

.. |bi30t| image:: tc1/net_recv_bus-3-rabbitmq_0-rpc-cast.png
    :scale: 15                                               
                                                             
.. |bi31t| image:: tc1/net_recv_bus-3-rabbitmq_3-rpc-cast.png
    :scale: 15                                               
                                                             
.. |bi32t| image:: tc1/net_recv_bus-3-rabbitmq_4-rpc-cast.png
    :scale: 15         

.. |ri30t| image:: tc1/net_recv_bus-3-router_0-rpc-cast.png
    :scale: 15

.. |ri31t| image:: tc1/net_recv_bus-3-router_3-rpc-cast.png
    :scale: 15

.. |ri32t| image:: tc1/net_recv_bus-3-router_4-rpc-cast.png
    :scale: 15

.. |bi50t| image:: tc1/net_recv_bus-5-rabbitmq_0-rpc-cast.png
    :scale: 15                                               
                                                             
.. |bi51t| image:: tc1/net_recv_bus-5-rabbitmq_1-rpc-cast.png
    :scale: 15                                               
                                                             
.. |bi52t| image:: tc1/net_recv_bus-5-rabbitmq_2-rpc-cast.png
    :scale: 15                                               
                                                             
.. |bi53t| image:: tc1/net_recv_bus-5-rabbitmq_3-rpc-cast.png
    :scale: 15                                               
                                                             
.. |bi54t| image:: tc1/net_recv_bus-5-rabbitmq_4-rpc-cast.png
    :scale: 15         

.. |ri50t| image:: tc1/net_recv_bus-5-router_0-rpc-cast.png
    :scale: 15

.. |ri51t| image:: tc1/net_recv_bus-5-router_1-rpc-cast.png
    :scale: 15

.. |ri52t| image:: tc1/net_recv_bus-5-router_1-rpc-cast.png
    :scale: 15
            
.. |ri53t| image:: tc1/net_recv_bus-5-router_2-rpc-cast.png
    :scale: 15

.. |ri54t| image:: tc1/net_recv_bus-5-router_3-rpc-cast.png
    :scale: 15

            
+--------+-----------+------+------------------------------------------------------+
| Driver | Instances | Type | TCP connections                                      |
+========+===========+======+======================================================+
| broker |         1 | Sent |.. image:: tc1/net_sent_bus-1-rabbitmq_2-rpc-cast.png |
|        |           |      |   :scale: 15                                         |
+--------+-----------+------+------------------------------------------------------+
| broker |         1 | Recv |.. image:: tc1/net_recv_bus-1-rabbitmq_2-rpc-cast.png |
|        |           |      |   :scale: 15                                         |
+--------+-----------+------+------------------------------------------------------+
| router |         1 | Sent |.. image:: tc1/net_sent_bus-1-router_2-rpc-cast.png   |
|        |           |      |   :scale: 15                                         |
+--------+-----------+------+------------------------------------------------------+
| router |         1 | Recv |.. image:: tc1/net_recv_bus-1-router_2-rpc-cast.png   |
|        |           |      |   :scale: 15                                         |
+--------+-----------+------+------------------------------------------------------+
| broker |         3 | Sent | |bo30t| |bo31t| |bo32t|                              |
+--------+-----------+------+------------------------------------------------------+
| broker |         3 | Recv | |bi30t| |bi31t| |bi32t|                              |
+--------+-----------+------+------------------------------------------------------+
| router |         3 | Sent | |ro30t| |ro31t| |ro32t|                              |
+--------+-----------+------+------------------------------------------------------+
| router |         3 | Recv | |ri30t| |ri31t| |ri32t|                              |
+--------+-----------+------+------------------------------------------------------+
| broker |         5 | Sent | |bo50t| |bo51t| |bo52t| |bo53t| |bo54t|              |
+--------+-----------+------+------------------------------------------------------+
| broker |         5 | Recv | |bi50t| |bi51t| |bi52t| |bi53t| |bi54t|              |
+--------+-----------+------+------------------------------------------------------+
| router |         5 | Sent | |ro50t| |ro51t| |ro52t| |ro53t| |ro54t|              |
+--------+-----------+------+------------------------------------------------------+
| router |         5 | Recv | |ri50t| |ri51t| |ri52t| |ri53t| |ri54t|              |
+--------+-----------+------+------------------------------------------------------+

