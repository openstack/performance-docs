Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers, network
parameters and operating system configuration.

Hardware
""""""""

This section contains list of all types of hardware nodes.

+-----------+-------+----------------------------------------------------+
| Parameter | Value | Comments                                           |
+-----------+-------+----------------------------------------------------+
| model     |       | e.g. Supermicro X9SRD-F                            |
+-----------+-------+----------------------------------------------------+
| CPU       |       | e.g. 6 x Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz |
+-----------+-------+----------------------------------------------------+

Network
"""""""

This section contains list of interfaces and network parameters.  In the
context of a cloud massively distributed (e.g across a WAN), the network links
may present different characteristics in terms of latency, bandwidth, packet
loss. These characteristics can be emulated (e.g `tc`_) or be the result of a
real deployment over a large geographical area.  In any cases, link
characteristics must be described.

+------------------+-------+-------------------------+
| Parameter        | Value | Comments                |
+------------------+-------+-------------------------+
| card model       |       | e.g. Intel              |
+------------------+-------+-------------------------+
| driver           |       | e.g. ixgbe              |
+------------------+-------+-------------------------+
| speed            |       | e.g. 10G or 1G          |
+------------------+-------+-------------------------+

Software
""""""""

This section describes installed Operating System and other relevant parameter
(e.g system level) and software.

+-----------------+-------+---------------------------+
| Parameter       | Value | Comments                  |
+-----------------+-------+---------------------------+
| OS              |       | e.g. Ubuntu 14.04.3       |
+-----------------+-------+---------------------------+
| oslo.messaging  |       | e.g 5.30.0                |
+-----------------+-------+---------------------------+

Backend specific versions must be gathered as well as third party tools.

* RabbitMQ backend

+-----------------+-------+---------------------------+
| Parameter       | Value | Comments                  |
+-----------------+-------+---------------------------+
| RMQ server      |       | e.g 3.6.11                |
+-----------------+-------+---------------------------+
| kombu client    |       | e.g 4.10                  |
+-----------------+-------+---------------------------+
| AMQP client     |       | e.g 2.2.1                 |
+-----------------+-------+---------------------------+

* AMQP backend

+----------------------+-------+---------------------------+
| Parameter            | Value | Comments                  |
+----------------------+-------+---------------------------+
| Qpid dispatch router |       | e.g 0.8.0                 |
+----------------------+-------+---------------------------+
| python-qpid-proton   |       | e.g 0.17.0                |
+----------------------+-------+---------------------------+
| pyngus               |       | e.g 2.2.1                 |
+----------------------+-------+---------------------------+

* ZeroMQ backend

+----------------------+-------+---------------------------+
| Parameter            | Value | Comments                  |
+----------------------+-------+---------------------------+
| pyzmq                |       | e.g 17.0.0                |
+----------------------+-------+---------------------------+
| redis-server         |       | e.g 4.0                   |
+----------------------+-------+---------------------------+

* Kafka backend

+----------------------+-------+---------------------------+
| Parameter            | Value | Comments                  |
+----------------------+-------+---------------------------+
| Kafka server         |       | e.g 0.10.2                |
+----------------------+-------+---------------------------+
| Kafka python         |       | e.g 1.3.4                 |
+----------------------+-------+---------------------------+
| Java RE              |       | e.g 8u144                 |
+----------------------+-------+---------------------------+

Messaging middleware topology
"""""""""""""""""""""""""""""

The actual deployment of the messaging middleware. A graph may be used to
illustrate thoroughly the topology of the messaging entities (e.g federated
RabbitMQ clusters, set of qdrouterd daemons)

Openstack version
"""""""""""""""""

For the operational testings, OpenStack version must be specified.
