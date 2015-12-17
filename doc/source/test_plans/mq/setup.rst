Test Setup
----------

This section describes the setup for message queue testing. It can be either
a single (all-in-one) or a multi-node installation.

A single-node setup requires just one node to be up and running. It has
both compute and controller roles and all OpenStack services run on this node.
This setup does not support hardware scaling or workload distribution tests.

A basic multi-node setup with RabbitMQ or ActiveMQ comprises 5 physical nodes:
  * One node for a compute node. This node simulates activity which is
    typical for OpenStack compute components.
  * One node for a controller node. This node simulates activity which
    is typical for OpenStack control plane services.
  * Three nodes are allocated for the MQ cluster.

When using ZeroMQ, the basic multi-node setup can be reduced to two physical nodes.
  * One node for a compute node as above.
  * One node for a controller node. This node also acts as a Redis host
    for match making purposes.


RabbitMQ Installation and Configuration
---------------------------------------

  * Install RabbitMQ server package:
    ``sudo apt-get install rabbitmq-server``
  * Configure RabbitMQ on each node ``/etc/rabbitmq/rabbitmq.config``:

.. literalinclude:: rabbitmq.config
    :language: erlang

..

  * Stop RabbitMQ on nodes 2 and 3:
    ``sudo service rabbitmq-server stop``
  * Make Erlang cookies on nodes 2 and 3 the same as on node 1:
    ``/var/lib/rabbitmq/.erlang.cookie``
  * Start RabbitMQ server:
    ``sudo service rabbitmq-server start``
  * Stop RabbitMQ services, but leave Erlang:
    ``sudo rabbitmqctl stop_app``
  * Join nodes 2 and 3 nodes to node 1:
    ``rabbitmqctl join_cluster rabbit@node-1``
  * Start app on nodes 2 and 3:
    ``sudo rabbitmqctl start_app``
  * Add needed user:

    ``sudo rabbitmqctl add_user stackrabbit password``
    ``sudo rabbitmqctl set_permissions stackrabbit ".*" ".*" ".*"``


ActiveMQ Installation and Configuration
---------------------------------------

This section describes installation and configuration steps for an ActiveMQ
message queue implementation. ActiveMQ is based on Java technologies so it
requires a Java runtime. Actual performance will depend on the Java
version as well as the hardware specification. The following steps should be
performed for an ActiveMQ installation:


  * Install Java on nodes node-1, node-2 and node-3:
    ``sudo apt-get install default-jre``
  * Download the latest ActiveMQ binary:
    ``wget http://www.eu.apache.org/dist/activemq/5.12.0/apache-activemq-5.12.0-bin.tar.gz``
  * Unzip the archive:
    ``tar zxvf apache-activemq-5.12.0-bin.tar.gz``
  * Install everything needed for ZooKeeper:

    * download ZK binaries: ``wget http://www.eu.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz``
    * unzip the archive: ``tar zxvf zookeeper-3.4.6.tar.gz``
    * create ``/home/ubuntu/zookeeper-3.4.6/conf/zoo.cfg`` file:

.. literalinclude:: zoo.cfg
    :language: ini

.. note::

    Here 10.4.1.x are the IP addresses of the ZooKeeper nodes where ZK is
    installed. ZK will be run in cluster mode with majority voting, so at least 3 nodes
    are required.

.. code-block:: none

    tickTime=2000
    dataDir=/home/ubuntu/zookeeper-3.4.6/data
    dataLogDir=/home/ubuntu/zookeeper-3.4.6/logs
    clientPort=2181
    initLimit=10
    syncLimit=5
    server.1=10.4.1.107:2888:3888
    server.2=10.4.1.119:2888:3888
    server.3=10.4.1.111:2888:3888

    * create dataDir and dataLogDir directories
    * for each MQ node create a myid file in dataDir with the id of the
          server and nothing else. For node-1 the file will contain one line with 1,
          node-2 with 2, and node-3 with 3.
    * start ZooKeeper (on each node): \textbf{./zkServer.sh start}
    * check ZK status with: \textbf{./zkServer.sh status}
  * Configure ActiveMQ (apache-activemq-5.12.0/conf/activemq.xml file - set
        the hostname parameter to the node address)

.. code-block:: none

    <broker brokerName="broker" ... >
    ...
        <persistenceAdapter>
            <replicatedLevelDB
                directory="activemq-data"
                replicas="3"
                bind="tcp://0.0.0.0:0"
                zkAddress="10.4.1.107:2181,10.4.1.111:2181,10.4.1.119:2181"
                zkPassword="password"
                zkPath="/activemq/leveldb-stores"
                hostname="10.4.1.107"
            />
        </persistenceAdapter>

        <plugins>
            <simpleAuthenticationPlugin>
                <users>
                    <authenticationUser username="stackrabbit" password="password"
                     groups="users,guests,admins"/>
                </users>
            </simpleAuthenticationPlugin>
        </plugins>
    ...
    </broker>

After ActiveMQ is installed and configured it can be started with the command:
:command:./activemq start or ``./activemq console`` for a foreground process.


Oslo.messaging ActiveMQ Driver
------------------------------

All OpenStack changes (in the oslo.messaging library) to support ActiveMQ are already
merged to the upstream repository. The relevant changes can be found in the
amqp10-driver-implementation topic.
To run ActiveMQ even on the most basic all-in-one topology deployment the
following requirements need to be satisfied:

  * Java JRE must be installed in the system. The Java version can be checked with the
    command ``java -version``. If java is not installed an error message will
    appear. Java can be installed with the following command:
    ``sudo apt-get install default-jre``

  * ActiveMQ binaries should be installed in the system. See
    http://activemq.apache.org/getting-started.html for installation instructions.
    The latest stable version is currently
    http://apache-mirror.rbc.ru/pub/apache/activemq/5.12.0/apache-activemq-5.12.0-bin.tar.gz.

  * To use the OpenStack oslo.messaging amqp 1.0 driver, the following Python libraries
    need to be installed:
    ``pip install "pyngus$>=$1.0.0,$<$2.0.0"``
    ``pip install python-qpid-proton``

  * All OpenStack projects configuration files containing the line
    ``rpc_backend = rabbit`` need to be modified to replace this line with
    ``rpc_backend = amqp``, and then all the services need to be restarted.

ZeroMQ Installation
-------------------

This section describes installation steps for ZeroMQ. ZeroMQ (also ZMQ or 0MQ)
is an embeddable networking library but acts like a concurrency framework.
Unlike other AMQP-based drivers, such as RabbitMQ, ZeroMQ doesn’t have any central brokers in
oslo.messaging. Instead, each host (running OpenStack services) is both a ZeroMQ client and
a server. As a result, each host needs to listen to a certain TCP port for incoming connections
and directly connect to other hosts simultaneously.

To set up ZeroMQ, only one step needs to be performed.

  * Install python bindings for ZeroMQ. All necessary packages will be installed as dependencies:
    ``sudo apt-get install python-zmq``

  .. note::

     python-zmq version should be at least 14.0.1

  .. code-block:: none

   python-zmq
     Depends: <python:any>
       python
     Depends: python
     Depends: python
     Depends: libc6
     Depends: libzmq3

Oslo.messaging ZeroMQ Driver
----------------------------
All OpenStack changes (in the oslo.messaging library) to support ZeroMQ are already
merged to the upstream repository. You can find the relevant changes in the
zmq-patterns-usage topic.
To run ZeroMQ on the most basic all-in-one topology deployment the
following requirements need to be satisfied:

  * Python ZeroMQ bindings must be installed in the system.

  * Redis binaries should be installed in the system. See
    http://redis.io/download for instructions and details.

  .. note::

     The following changes need to be applied to all OpenStack project configuration files.

  * To enable the driver, in the section [DEFAULT] of each configuration file, the ‘rpc_backend’
    flag must be set to ‘zmq’ and the ‘rpc_zmq_host’ flag must be set to the hostname
    of the node.

  .. code-block:: none

   [DEFAULT]
   rpc_backend = zmq
   rpc_zmq_host = myopenstackserver.example.com


  * Set Redis as a match making service.

  .. code-block:: none

   [DEFAULT]
   rpc_zmq_matchmaker = redis

   [matchmaker_redis]
   host = 127.0.0.1
   port = 6379
   password = None

Running ZeroMQ on a multi-node setup
------------------------------------
The process of setting up oslo.messaging with ZeroMQ on a multi-node environment is very similar
to the all-in-one installation.

  * On each node ``rpc_zmq_host`` should be set to its FQDN.
  * Redis-server should be up and running on a controller node or a separate host.
    Redis can be used with master-slave replication enabled, but currently the oslo.messaging ZeroMQ driver
    does not support Redis Sentinel, so it is not yet possible to achieve high availability, automatic failover,
    and fault tolerance.

    The ``host`` parameter in section ``[matchmaker_redis]`` should be set to the IP address of a host which runs
    a master Redis instance, e.g.

    .. code-block:: none

       [matchmaker_redis]
       host = 10.0.0.3
       port = 6379
       password = None
