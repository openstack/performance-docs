.. _Results_of_Measuring_of_API_performance_of_Kubernetes:

*****************************************************
Results of measuring of API performance of Kubernetes
*****************************************************

:Abstract:

  This document includes performance test results of Kubernetes API.
  All tests have been performed regarding
  :ref:`Measuring_of_API_performance_of_Kubernetes`


Environment description
=======================
Hardware configuration of each server
-------------------------------------

.. table:: Description of servers hardware

  +-------+----------------+------------------------+------------------------+
  |server |name            |node-{1..500}, kuber*   |node-{1..355}           |
  |       +----------------+------------------------+------------------------+
  |       |role            |kubernetes cluster      |kubernetes cluster      |
  |       +----------------+------------------------+------------------------+
  |       |vendor,model    |Dell, R630              |Lenovo, RD550-1U        |
  |       +----------------+------------------------+------------------------+
  |       |operating_system| | 4.4.0-36-generic     | | 4.4.0-36-generic     |
  |       |                | | Ubuntu-xenial        | | Ubuntu-xenial        |
  |       |                | | x86_64               | | x86_64               |
  +-------+----------------+------------------------+------------------------+
  |CPU    |vendor,model    |Intel, E5-2680v3        |Intel, E5-2680 v3       |
  |       +----------------+------------------------+------------------------+
  |       |processor_count |2                       |2                       |
  |       +----------------+------------------------+------------------------+
  |       |core_count      |12                      |12                      |
  |       +----------------+------------------------+------------------------+
  |       |frequency_MHz   |2500                    |2500                    |
  +-------+----------------+------------------------+------------------------+
  |RAM    |vendor,model    |Hynix, HMA42GR7MFR4N-TF |IBM,???                 |
  |       +----------------+------------------------+------------------------+
  |       |amount_MB       |262144                  |262144                  |
  +-------+----------------+------------------------+------------------------+
  |NETWORK|interface_name  |bond0                   |bond0                   |
  |       +----------------+------------------------+------------------------+
  |       |vendor,model    |Intel, X710 Dual Port   |Intel, X710 Dual Port   |
  |       +----------------+------------------------+------------------------+
  |       |interfaces_count|2                       |2                       |
  |       +----------------+------------------------+------------------------+
  |       |bandwidth       |10G                     |10G                     |
  +-------+----------------+------------------------+------------------------+
  |STORAGE|dev_name        |/dev/sda                |/dev/sda                |
  |       +----------------+------------------------+------------------------+
  |       |vendor,model    | | raid1 PERC H730P Mini| | raid1 - LSI ????     |
  |       |                | | 2 disks Intel S3610  | | 2 disks Intel S3610  |
  |       +----------------+------------------------+------------------------+
  |       |SSD/HDD         |SSD                     |SSD                     |
  |       +----------------+------------------------+------------------------+
  |       |size            | 800GB                  | 800GB                  |
  +-------+----------------+------------------------+------------------------+

* kuber is a one-node Kubernetes cluster used to run container with test tool

Network scheme and part of configuration of hardware network switches
---------------------------------------------------------------------
Network scheme of the environment:

.. image:: Network_Scheme.png
   :alt: Network Scheme of the environment
   :scale: 65

Here is the piece of switch configuration for each switch port which is a part of
bond0 interface of a server:

.. code:: bash

   switchport mode trunk
   switchport trunk native vlan 600
   switchport trunk allowed vlan 600-602,630-649
   spanning-tree port type edge trunk
   spanning-tree bpduguard enable
   no snmp trap link-status

Software configuration of kubernetes service
--------------------------------------------
Setting up Kubernetes
^^^^^^^^^^^^^^^^^^^^^
Kubernetes was installed using `Kargo`_ deplyment tool.
Kargo operates the following roles:

- master: Calico, Kubernetes API services
- minion: Calico, kubernetetes minion services
- etcd: etcd service

Kargo deploys Kubernetes cluster with the following matching hostnames and
roles:

- node1: minion+master+etcd
- node2: minion+master+etcd
- node3: minion+etcd
- all other nodes: minion

We installed Kargo on top of dedicated node and start deployment (change
ADMIN_IP and SLAVE_IPS variables to addresses of your nodes and SLAVES_COUNT
to nodes count):

.. code:: bash

   git clone https://review.openstack.org/openstack/fuel-ccp-installer
   cd fuel-ccp-installer
   cat >> create_env_kargo.sh << EOF
   set -ex

   export ENV_NAME="kargo-test"
   export DEPLOY_METHOD="kargo"
   export WORKSPACE="/root/workspace"
   export ADMIN_USER="vagrant"
   export ADMIN_PASSWORD="kargo"

   # for 10 nodes
   export SLAVES_COUNT=10
   export ADMIN_IP="10.3.58.122"
   export SLAVE_IPS="10.3.58.122 10.3.58.138 10.3.58.145 10.3.58.140 10.3.58.124 10.3.58.126 10.3.58.158 10.3.58.173 10.3.58.151 10.3.58.161"

   export CUSTOM_YAML='docker_version: 1.12
   hyperkube_image_repo: "quay.io/coreos/hyperkube"
   hyperkube_image_tag: "v1.3.5_coreos.0"
   etcd_image_repo: "quay.io/coreos/etcd"
   etcd_image_tag: "v3.0.1"
   calicoctl_image_repo: "calico/ctl"
   #calico_node_image_repo: "calico/node"
   calico_node_image_repo: "l23network/node"
   calico_node_image_tag: "v0.20.0"
   calicoctl_image_tag: "v0.20.0"
   kube_apiserver_insecure_bind_address: "0.0.0.0"

   mkdir -p $WORKSPACE
   echo "Running on $NODE_NAME: $ENV_NAME"
   cd /root/fuel-ccp-installer
   bash "./utils/jenkins/run_k8s_deploy_test.sh"

   EOF
   ./create_env_kargo.sh

.. table:: Versions of some software

  +--------------------+------------------------------------------+
  | Software           | Version                                  |
  +--------------------+------------------------------------------+
  | Ubuntu             | Ubuntu 16.04.1 LTS                       |
  +--------------------+------------------------------------------+
  | Kargo              | 54d64106c74c72433c7c492a8a9a5075e17de35b |
  +--------------------+------------------------------------------+

Operating system configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can find outputs of some commands and /etc folder in the following archive:
:download:`server_description_of_node1 <configs/server_description_of_node1.tar.gz>`
:download:`server_description_of_node3 <configs/server_description_of_node3.tar.gz>`
:download:`server_description_of_node4 <configs/server_description_of_node4.tar.gz>`

Software configuration of Test tool:
------------------------------------
Test tool preparation
^^^^^^^^^^^^^^^^^^^^^
Kubernetes `e2e-tests`_ has been used to collect API latencies during the
tests. We've run the test having Docker container with the tool. To build the
container create e2e-tests directory and copy files from
`Files and scripts to build Docker container with e2e-test tool`_ section to
the directory. Then build the image:

.. code:: bash

  root@kuber:~# cd e2e-tests
  root@kuber:~/e2e-tests# docker build -t k8s_e2e ./

Test tool description
^^^^^^^^^^^^^^^^^^^^^
- The test creates 30 pods per Kubernetes minion.
    - 300 on 10-nodes cluster
    - 1500 on 50-nodes cluster
    - 10650 on 355-nodes cluster
- The test actually spawns replication controllers, not pods directly
- The test spawns three types of replication controllers:
    - small which includes 5 pods
    - medium which includes 30 pods
    - big which includes 250 pods
- After all containers are spawned the test resizes them
- The test performs 10 actions/sec
You can see more from the `load.py`_ code.

.. table:: Versions of some software

  +----------------------------+------------------------------------------+
  | Software                   | Version                                  |
  +----------------------------+------------------------------------------+
  | Ubuntu                     | Ubuntu 14.04 LTS                         |
  +----------------------------+------------------------------------------+
  | e2e-test (kubernetes repo) | v1.3.5                                   |
  +----------------------------+------------------------------------------+
  | Docker                     | 1.11.2, build b9f10c9                    |
  +----------------------------+------------------------------------------+

Operating system configuration:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can find outputs of some commands and /etc folder in the following archive:
:download:`server_description_of_e2e-test_node <configs/server_description_of_kuber.tar.gz>`

Testing process
===============
Preparation
-----------
1.
  Kubernetes was set up on top of 10 nodes as described in
  `Setting up kubernetes`_ section.

2.
  e2e-test container was running on top of infrastructure one-node Kubernetes
  cluster called "kuber". You can find k8s_e2e.yaml in
  `Files and scripts to run Docker container with e2e-test tool`_. You need to
  change "${API_SERVER}" to URI of Kubernetes API (for example
  http://10.3.58.66:8080). Also you need to specify filder where results will
  be stored. For 10-nodes cluster we created
  "/var/lib/volumes/e2e-test/10_nodes" filder. This folder will be mounted to
  the container as a volume.

.. code:: bash

  root@kuber:~/e2e-tests# mkdir -p /var/lib/volumes/e2e-test/10_nodes
  # set API URI and volume folder:
  root@kuber:~/e2e-tests# vim k8s_e2e.yaml
  root@kuber:~/e2e-tests# kubectl create -f k8s_e2e.yaml
  # To store log to a file:
  root@kuber:~/e2e-tests# kubectl attach k8s-e2e 2>&1 | tee -a /var/lib/volumes/e2e-test/10_nodes/k8s-e2e.log

3.
  After that we have a log file which includes JSON with Kubernetes API
  latency. We can use simple Python script from
  `Script to convert JSON from log file to RST table`_ to create rst tables
  from the log file.

.. code:: bash

  root@kuber:~/e2e-tests# python create_rst_table_from_k8s_e2e_log.py /var/lib/volumes/e2e-test/10_nodes/k8s-e2e.log

Now we have /var/lib/volumes/e2e-test/10_nodes/k8s-e2e.rst file with rst
tables.

We performed the steps from 1 to 3 for Kubernetes cluster on top of 10, 50 and
355 nodes.

Results
=======
10-nodes cluster
----------------

.. include:: results/10_nodes_results.rst

50-nodes cluster
----------------

.. include:: results/50_nodes_results.rst

355-nodes cluster
-----------------

.. include:: results/355_nodes_results.rst

Comparation
-----------
Here is you can see results comparation from 10, 50 and 355 nodes clusters.
Please note, that numbers of pods and other items depend on numbers of nodes.

-
  300 pods will be spawned on 10-nodes cluster
-
  1500 pods will be spawned on 50-nodes cluster
-
  10650 pods will be spawned on 355-nodes cluster

+---------------------------------------------+-------------------------------+
|.. image:: results/replicationcontrollers.png|.. image:: results/pods.png    |
|   :alt: replicationcontrollers latency      |   :alt: pods latency          |
|   :scale: 50                                |   :scale: 50                  |
+---------------------------------------------+-------------------------------+
|.. image:: results/endpoints.png             |.. image:: results/nodes.png   |
|   :alt: endpoints latency                   |   :alt: nodes latency         |
|   :scale: 50                                |   :scale: 50                  |
+---------------------------------------------+-------------------------------+
|.. image:: results/resourcequotas.png        |.. image:: results/secrets.png |
|   :alt: resourcequotas.png latency          |   :alt: secrets latency       |
|   :scale: 50                                |   :scale: 50                  |
+---------------------------------------------+-------------------------------+

Applications
============
Files and scripts to build Docker container with e2e-test tool
--------------------------------------------------------------
e2e-tests/Dockerfile:

.. literalinclude:: e2e-tests/Dockerfile
    :language: dockerfile

e2e-tests/entrypoint.sh:

.. literalinclude:: e2e-tests/entrypoint.sh
    :language: bash

Files and scripts to run Docker container with e2e-test tool
------------------------------------------------------------
e2e-tests/k8s-e2e.yaml:

.. literalinclude:: e2e-tests/k8s-e2e.yaml
    :language: yaml

Script to convert JSON from log file to RST table
-------------------------------------------------
e2e-tests/create_rst_table_from_k8s_e2e_log.py:

.. literalinclude:: e2e-tests/create_rst_table_from_k8s_e2e_log.py
    :language: python


.. references:

.. _Kargo: https://github.com/kubespray/kargo
.. _e2e-tests: https://github.com/kubernetes/kubernetes/blob/release-1.4/docs/devel/e2e-tests.md
.. _load.py: https://github.com/kubernetes/kubernetes/blob/master/test/e2e/load.go