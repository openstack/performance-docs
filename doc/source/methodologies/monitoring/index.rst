
.. _Methodology_for_Containerized_Openstack_Monitoring:

**************************************************
Methodology for Containerized Openstack Monitoring
**************************************************

:Abstract:

  This document describes one of the Containerized Openstack monitoring solutions
  to provide scalable and comprehensive architecture and obtain all crucial performance
  metrics on each structure layer.


Containerized Openstack Monitoring Architecture
===============================================

  This part of documentation describes required performance metrics in each
  distinguished Containerized Openstack layer.

Containerized Openstack comprises three layers where Monitoring System should
be able to query all necessary counters:
 - OS layer
 - Kubernetes layer
 - Openstack layer

Monitoring instruments must be logically divided in two groups:
 - Monitoring Server Side
 - Node Client Side

Operation System Layer
----------------------

We were using Ubuntu Xenial on top of bare-metal servers for both server and node side.

Baremetal hardware description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We deployed everything at 200 servers environment with following hardware characteristics:

.. table::

  +-------+----------------+------------------------+
  |server |vendor,model    |HP,DL380 Gen9           |
  +-------+----------------+------------------------+
  |CPU    |vendor,model    |Intel,E5-2680 v3        |
  |       +----------------+------------------------+
  |       |processor_count |2                       |
  |       +----------------+------------------------+
  |       |core_count      |12                      |
  |       +----------------+------------------------+
  |       |frequency_MHz   |2500                    |
  +-------+----------------+------------------------+
  |RAM    |vendor,model    |HP,752369-081           |
  |       +----------------+------------------------+
  |       |amount_MB       |262144                  |
  +-------+----------------+------------------------+
  |NETWORK|interface_name  |p1p1                    |
  |       +----------------+------------------------+
  |       |vendor,model    |Intel,X710 Dual Port    |
  |       +----------------+------------------------+
  |       |bandwidth       |10G                     |
  +-------+----------------+------------------------+
  |STORAGE|dev_name        |/dev/sda                |
  |       +----------------+------------------------+
  |       |vendor,model    | | raid10 - HP P840     |
  |       |                | | 12 disks EH0600JEDHE |
  |       +----------------+------------------------+
  |       |SSD/HDD         |HDD                     |
  |       +----------------+------------------------+
  |       |size            | 3,6TB                  |
  +-------+----------------+------------------------+

Operating system configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Baremetal nodes were provisioned with Cobbler with our in-home preseed scripts.
OS versions we used:

.. table:: Versions Operating Systems

  +--------------------+-----------------------------------------+
  |Software            |Version                                  |
  +--------------------+-----------------------------------------+
  |Ubuntu              |Ubuntu 16.04.1 LTS                       |
  +--------------------+-----------------------------------------+
  |Kernel              |4.4.0-47-generic                         |
  +--------------------+-----------------------------------------+

You can find /etc folder contents from the one of the typical system we were using:

:download:`etc_tarball <configs/node1.tar.gz>`

Required system metrics
^^^^^^^^^^^^^^^^^^^^^^^

At this layer we must get this list of processes:

.. table::

  +------------------------+-----------------------------------------+
  |List of processes       |Mariadb                                  |
  |                        +-----------------------------------------+
  |                        |Rabbitmq                                 |
  |                        |-----------------------------------------+
  |                        |Keystone                                 |
  |                        +-----------------------------------------+
  |                        |Glance                                   |
  |                        +-----------------------------------------+
  |                        |Cinder                                   |
  |                        +-----------------------------------------+
  |                        |Nova                                     |
  |                        +-----------------------------------------+
  |                        |Neutron                                  |
  |                        +-----------------------------------------+
  |                        |Openvswitch                              |
  |                        +-----------------------------------------+
  |                        |Kubernetes                               |
  +------------------------+-----------------------------------------+

And following list of metrics:

.. table::

  +------------------------+-----------------------------------------+
  |Node load average       |1min                                     |
  |                        +-----------------------------------------+
  |                        |5min                                     |
  |                        |-----------------------------------------+
  |                        |15min                                    |
  +------------------------+-----------------------------------------+
  |Global process stats    |Running                                  |
  |                        +-----------------------------------------+
  |                        |Stopped                                  |
  |                        |-----------------------------------------+
  |                        |Waiting                                  |
  +------------------------+-----------------------------------------+
  |Global CPU Usage        | Steal                                   |
  |                        +-----------------------------------------+
  |                        | Wait                                    |
  |                        +-----------------------------------------+
  |                        | User                                    |
  |                        +-----------------------------------------+
  |                        | System                                  |
  |                        +-----------------------------------------+
  |                        | Interrupt                               |
  |                        +-----------------------------------------+
  |                        | Nice                                    |
  |                        +-----------------------------------------+
  |                        | Idle                                    |
  +------------------------+-----------------------------------------+
  |Per CPU Usage           | User                                    |
  |                        +-----------------------------------------+
  |                        | System                                  |
  +------------------------+-----------------------------------------+
  |Global memory usage     |bandwidth                                |
  |                        +-----------------------------------------+
  |                        |Cached                                   |
  |                        +-----------------------------------------+
  |                        |Buffered                                 |
  |                        +-----------------------------------------+
  |                        |Free                                     |
  |                        +-----------------------------------------+
  |                        |Used                                     |
  |                        +-----------------------------------------+
  |                        |Total                                    |
  +------------------------+-----------------------------------------+
  |Numa monitoring         |Numa_hit                                 |
  |For each node           +-----------------------------------------+
  |                        |Numa_miss                                |
  |                        |-----------------------------------------+
  |                        |Numa_foreign                             |
  |                        +-----------------------------------------+
  |                        |Local_node                               |
  |                        +-----------------------------------------+
  |                        |Other_node                               |
  +------------------------+-----------------------------------------+
  |Numa monitoring         |Huge                                     |
  |For each pid            +-----------------------------------------+
  |                        |Heap                                     |
  |                        |-----------------------------------------+
  |                        |Stack                                    |
  |                        +-----------------------------------------+
  |                        |Private                                  |
  +------------------------+-----------------------------------------+
  |Global IOSTAT \+        |Merge reads /s                           |
  |Per device IOSTAT       +-----------------------------------------+
  |                        |Merge write /s                           |
  |                        +-----------------------------------------+
  |                        |read/s                                   |
  |                        +-----------------------------------------+
  |                        |write/s                                  |
  |                        +-----------------------------------------+
  |                        |Read transfer                            |
  |                        +-----------------------------------------+
  |                        |Write transfer                           |
  |                        +-----------------------------------------+
  |                        |Read latency                             |
  |                        +-----------------------------------------+
  |                        |Write latency                            |
  |                        +-----------------------------------------+
  |                        |Write transfer                           |
  |                        +-----------------------------------------+
  |                        |Queue size                               |
  |                        +-----------------------------------------+
  |                        |Await                                    |
  +------------------------+-----------------------------------------+
  |Network per interface   |Octets /s (in, out)                      |
  |                        +-----------------------------------------+
  |                        |Packet /s (in, out)                      |
  |                        |-----------------------------------------+
  |                        |Dropped /s                               |
  +------------------------+-----------------------------------------+
  |Other system metrics    |Entropy                                  |
  |                        +-----------------------------------------+
  |                        |DF per device                            |
  +------------------------+-----------------------------------------+

Kubernetes Layer
----------------

`Kargo`_ from `Fuel-CCP-installer`_ was our main tool to deploy K8S
 on top of provisioned systems (monitored nodes).

  Kargo sets up Kubernetes in the following way:

  - masters: Calico, Kubernetes API services
  - nodes: Calico, Kubernetes minion services
  - etcd: etcd service

Kargo deployment parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can find Kargo deployment script in `Kargo deployment script`_ section

.. code:: bash

  docker_options: "--insecure-registry 172.20.8.35:5000 -D"
  upstream_dns_servers: [172.20.8.34, 8.8.4.4]
  nameservers: [172.20.8.34, 8.8.4.4]
  kube_service_addresses: 10.224.0.0/12
  kube_pods_subnet: 10.240.0.0/12
  kube_network_node_prefix: 22
  kube_apiserver_insecure_bind_address: "0.0.0.0"
  dns_replicas: 3
  dns_cpu_limit: "100m"
  dns_memory_limit: "512Mi"
  dns_cpu_requests: "70m"
  dns_memory_requests: "70Mi"
  deploy_netchecker: false

.. table::

  +----------------------+-----------------------------------------+
  |Software              |Version                                  |
  +----------------------+-----------------------------------------+
  |`Fuel-CCP-Installer`_ |6fd81252cb2d2c804f388337aa67d4403700f094 |
  |                      |                                         |
  +----------------------+-----------------------------------------+
  |`Kargo`_              |2c23027794d7851ee31363c5b6594180741ee923 |
  +----------------------+-----------------------------------------+

Required K8S metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here we should get K8S health
metrics and ETCD performance metrics:

.. table::

  +------------------------+-----------------------------------------+
  |ETCD performance metrics|members count / states                   |
  |                        +-----------------------------------------+
  |                        |numbers of keys in a cluster             |
  |                        |-----------------------------------------+
  |                        |Size of data set                         |
  |                        +-----------------------------------------+
  |                        |Avg. latency from leader to followers    |
  |                        +-----------------------------------------+
  |                        |Bandwidth rate, send/receive             |
  |                        +-----------------------------------------+
  |                        |Create store success/fail                |
  |                        +-----------------------------------------+
  |                        |Get success/fail                         |
  |                        +-----------------------------------------+
  |                        |Set success/fail                         |
  |                        +-----------------------------------------+
  |                        |Package rate, send/receive               |
  |                        +-----------------------------------------+
  |                        |Expire count                             |
  |                        +-----------------------------------------+
  |                        |Update success/fail                      |
  |                        +-----------------------------------------+
  |                        |Compare-and-swap success/fail            |
  |                        +-----------------------------------------+
  |                        |Watchers                                 |
  |                        +-----------------------------------------+
  |                        |Delete success/fail                      |
  |                        +-----------------------------------------+
  |                        |Compare-and-delete success/fail          |
  |                        +-----------------------------------------+
  |                        |Append req, send/ receive                |
  +------------------------+-----------------------------------------+
  |K8S health metrics      |Number of node in each state             |
  |                        +-----------------------------------------+
  |                        |Total number of namespaces               |
  |                        +-----------------------------------------+
  |                        |Total number of PODs per cluster,node,ns |
  |                        +-----------------------------------------+
  |                        |Total of number of services              |
  |                        +-----------------------------------------+
  |                        |Endpoints in each service                |
  |                        +-----------------------------------------+
  |                        |Number of API service instances          |
  |                        +-----------------------------------------+
  |                        |Number of controller instances           |
  |                        +-----------------------------------------+
  |                        |Number of scheduler instances            |
  |                        +-----------------------------------------+
  |                        |Cluster resources, scheduler view        |
  +------------------------+-----------------------------------------+
  |K8S API log analysis    |Number of responses (per each HTTP code) |
  |                        +-----------------------------------------+
  |                        |Response Time                            |
  +------------------------+-----------------------------------------+

For last two metrics we should utilize log collector to store and parse all
log records within K8S environments.

Openstack Layer
-----------------

CCP stands for "Containerized Control Plane". CCP aims to build, run and manage
production-ready OpenStack containers on top of Kubernetes cluster.

.. table::

  +--------------------+-----------------------------------------+
  |Software            |Version                                  |
  +--------------------+-----------------------------------------+
  |`Fuel-CCP`_         |8570d0e0e512bd16f8449f0a10b1e3900fd09b2d |
  +--------------------+-----------------------------------------+


CCP configuration
^^^^^^^^^^^^^^^^^

CCP was deployed on top of 200 nodes K8S cluster in the following configuration:

.. code-block:: yaml

  node[1-3]: Kubernetes
  node([4-6])$: # 4-6
    roles:
      - controller
      - openvswitch
  node[7-9]$: # 7-9
    roles:
      - rabbitmq
  node10$: # 10
    roles:
      - galera
  node11$: # 11
    roles:
      - heat
  node(1[2-9])$: # 12-19
    roles:
      - compute
      - openvswitch
  node[2-9][0-9]$: # 20-99
    roles:
      - compute
      - openvswitch
  node(1[0-9][0-9])$: # 100-199
    roles:
      - compute
      - openvswitch
  node200$:
    roles:
      - backup


CCP Openstack services list ( `versions.yaml`_ ):


.. code-block:: yaml

  openstack/cinder:
    git_ref: stable/newton
    git_url: https://github.com/openstack/cinder.git
  openstack/glance:
    git_ref: stable/newton
    git_url: https://github.com/openstack/glance.git
  openstack/heat:
    git_ref: stable/newton
    git_url: https://github.com/openstack/heat.git
  openstack/horizon:
    git_ref: stable/newton
    git_url: https://github.com/openstack/horizon.git
  openstack/keystone:
    git_ref: stable/newton
    git_url: https://github.com/openstack/keystone.git
  openstack/neutron:
    git_ref: stable/newton
    git_url: https://github.com/openstack/neutron.git
  openstack/nova:
    git_ref: stable/newton
    git_url: https://github.com/openstack/nova.git
  openstack/requirements:
    git_ref: stable/newton
    git_url: https://git.openstack.org/openstack/requirements.git
  openstack/sahara-dashboard:
    git_ref: stable/newton
    git_url: https://git.openstack.org/openstack/sahara-dashboard.git


`K8S Ingress Resources`_ rules were enabled during CCP deployment to expose Openstack services
endpoints to external routable network.


See CCP deployment script and configuration files in the
`CCP deployment and configuration files`_ section.

Required Openstack-related metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this layer we should get openstack environment metrics,
API and resources utilization metrics.

.. table:: Versions of CCP-related software

  +------------------------+-----------------------------------------+
  |Openstack metrics       |Total number of controller nodes         |
  |                        +-----------------------------------------+
  |                        |Total number of services                 |
  |                        |-----------------------------------------+
  |                        |Total number of compute nodes            |
  |                        +-----------------------------------------+
  |                        |Total number of nodes                    |
  |                        +-----------------------------------------+
  |                        |Total number of VMs                      |
  |                        +-----------------------------------------+
  |                        |Number of VMs per tenant, per node       |
  |                        +-----------------------------------------+
  |                        |Resource utilization per project,service |
  |                        +-----------------------------------------+
  |                        |Total number of tenants                  |
  |                        +-----------------------------------------+
  |                        |API request time                         |
  |                        +-----------------------------------------+
  |                        |Mean time to spawn VM                    |
  +------------------------+-----------------------------------------+

Implementation
==============

This part of documentation describes Monitoring System implementation.
Here is software list that we chose to realize all required tasks:

.. table::

  +-----------------------------------------+-----------------------------------------+
  |Monitoring Node Server Side              |Monitored Node Client Side               |
  +--------------------+--------------------+--------------------+--------------------+
  |Metrics server      |Log storage         |Metrics agent       |Log collector       |
  |                    |                    |                    |                    |
  +--------------------+--------------------+--------------------+--------------------+
  |  `Prometheus`_ \+  | `ElasticSearch`_   |`Telegraf`_         | `Heka`_            |
  |  `Grafana`_        | \+ `Kibana`_       |                    |                    |
  +--------------------+--------------------+--------------------+--------------------+

Server Side Software
---------------------

Prometheus
^^^^^^^^^^

.. table::

  +--------------------+-----------------------------------------+
  |Software            |Version                                  |
  +--------------------+-----------------------------------------+
  |`Prometheus GitHub`_|7e369b9318a4d5d97a004586a99f10fa51a46b26 |
  +--------------------+-----------------------------------------+

Due to high load rate we faced an issue with Prometheus performance at metrics count up to 15 millions.
We split Prometheus setup in 2 standalone nodes. First node - to poll API metrics from K8S-related services
that natively available at `/metrics` uri and exposed by K8S API and ETCD API by default.
Second node - to store all other metrics that should be collected and calculated locally on environment
servers via Telegraf.

Prometheus nodes deployments scripts and configuration files could be found at `Prometheus deployment and configuration files`_ section

Grafana
^^^^^^^

.. table::

  +--------------------+-----------------------------------------+
  |Software            |Version                                  |
  +--------------------+-----------------------------------------+
  |`Grafana`_          |v4.0.1                                   |
  +--------------------+-----------------------------------------+

Grafana was used as a metrics visualizer with several dashboards for each metrics group.
Separate individual dashboards were built for each group of metrics:

- System nodes metrics
- Kubernetes metrics
- ETCD metrics
- Openstack metrics

You can find their setting at `Grafana dashboards configuration`_

Grafana server deployment script:

.. code-block:: bash

  #!/bin/bash
  ansible-playbook -i ./hosts ./deploy-graf-prom.yaml --tags "grafana"

It uses the same yaml configuration file `deploy-graf-prom.yaml`_ from `Prometheus deployment and configuration files`_ section.

ElasticSearch
^^^^^^^^^^^^^

.. table::

  +--------------------+-----------------------------------------+
  |Software            |Version                                  |
  +--------------------+-----------------------------------------+
  |`ElasticSearch`_    |2.4.2                                    |
  +--------------------+-----------------------------------------+

ElasticSearch is well-known proven log storage and we used it as a standalone
node for collecting Kubernetes API logs and all other logs from containers across environment.
For appropriate performance at 200 nodes lab we increased `ES_HEAP_SIZE` from default 1G to 10G
in /etc/default/elasticsearch configuration file.

Elastic search and Kibana dashboard were installed with
`deploy_elasticsearch_kibana.sh`_ deployment script.

Kibana
^^^^^^

.. table::

  +--------------------+-----------------------------------------+
  |Software            |Version                                  |
  +--------------------+-----------------------------------------+
  |`Kibana`_           |4.5.4                                    |
  +--------------------+-----------------------------------------+

We used Kibana as a main visualization tool for Elastic Search. We were able to create chart
graphs based on K8S API logs analysis. Kibana was installed on a single separate node
with a single dashboard representing K8S API Response time graph.

Dashboard settings:

:download:`Kibana_dashboard.json <configs/dashboards/Kibana_dashboard.json>`

Client side Software
--------------------

Telegraf
^^^^^^^^

.. table::

  +--------------------+-----------------------------------------+
  |Software            |Version                                  |
  +--------------------+-----------------------------------------+
  |`Telegraf`_         |v1.0.0-beta2-235-gbc14ac5                |
  |                    |git: openstack_stats                     |
  |                    |bc14ac5b9475a59504b463ad8f82ed810feed3ec |
  +--------------------+-----------------------------------------+

Telegraf was chosen as client-side metrics agent. It provides multiple ways to poll and calculate from variety of
different sources. With regard to its plugin-driven nature, it takes data from different inputs and
exposes calculated metrics in Prometheus format. We used forked version of Telegraf with custom patches to
be able to utilize custom Openstack-input plugin:

- `GitHub Telegraf Fork`_
- `Go SDK for OpenStack`_

Following automation scripts and configuration files were used to start Telegraf agent
across environment nodes.

`Telegraf deployment and configuration files`_

Below you can see which plugins were used to obtain metrics.

Standart Plugins
""""""""""""""""

.. code:: bash

  inputs.cpu  CPU
  inputs.disk
  inputs.diskio
  inputs.kernel
  inputs.mem
  inputs.processes
  inputs.swap
  inputs.system
  inputs.kernel_vmstat
  inputs.net
  inputs.netstat
  inputs.exec

Openstack input plugin
""""""""""""""""""""""
`inputs.openstack` custom plugin was used to gather the most of required Openstack-related metrics.

settings:

.. code:: bash

  interval = '40s'
  identity_endpoint = "http://keystone.ccp.svc.cluster.local:5000/v3"
  domain = "default"
  project = "admin"
  username = "admin"
  password = "password"


`System.exec` plugin
""""""""""""""""""""
`system.exec` plugin was used to trigger scripts to poll
and calculate all non-standard metrics.

common settings:

.. code:: bash

  interval = "15s"
  timeout = "30s"
  data_format = "influx"

commands:

.. code:: bash

  "/opt/telegraf/bin/list_openstack_processes.sh"
  "/opt/telegraf/bin/per_process_cpu_usage.sh"
  "/opt/telegraf/bin/numa_stat_per_pid.sh"
  "/opt/telegraf/bin/iostat_per_device.sh"
  "/opt/telegraf/bin/memory_bandwidth.sh"
  "/opt/telegraf/bin/network_tcp_queue.sh"
  "/opt/telegraf/bin/etcd_get_metrics.sh"
  "/opt/telegraf/bin/k8s_get_metrics.sh"
  "/opt/telegraf/bin/vmtime.sh"
  "/opt/telegraf/bin/osapitime.sh"

You can see full Telegraf configuration file and its custom input scripts in the
section `Telegraf deployment and configuration files`_.

Heka
^^^^

.. table::

  +--------------------+-----------------------------------------+
  |Software            |Version                                  |
  +--------------------+-----------------------------------------+
  |`Heka`_             |0.10.0                                   |
  +--------------------+-----------------------------------------+

We chose Heka as log collecting agent for its wide variety of inputs
(possibility to feed data from Docker socket), filters (custom shorthand SandBox filters in LUA language)
and possibility to encode data for ElasticSearch.

With Heka agent started across environment servers we were able to send containers' logs to ElasticSearch
server. With custom LUA filter we extracted K8S API data and convert it in appropriate format to
visualize API timing counters (Average Response Time).

Heka deployment scripts and configuration file with LUA custom filter are in
`Heka deployment and configuration`_ section.

Applications
============

Kargo deployment script
-----------------------

deploy_k8s_using_kargo.sh
^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: configs/deploy_k8s_using_kargo.sh
   :language: bash

CCP deployment and configuration files
---------------------------------------

deploy-ccp.sh
^^^^^^^^^^^^^

.. literalinclude:: configs/ccp/deploy-ccp.sh
    :language: bash

ccp.yaml
^^^^^^^^

.. literalinclude:: configs/ccp/ccp.yaml
    :language: yaml

configs.yaml
^^^^^^^^^^^^

.. literalinclude:: configs/ccp/configs.yaml
    :language: yaml

topology.yaml
^^^^^^^^^^^^^

.. literalinclude:: configs/ccp/topology.yaml
    :language: yaml

repos.yaml
^^^^^^^^^^

.. literalinclude:: configs/ccp/repos.yaml
    :language: yaml

versions.yaml
^^^^^^^^^^^^^

.. literalinclude:: configs/ccp/versions.yaml
    :language: yaml

Prometheus deployment and configuration files
---------------------------------------------

Deployment scripts
^^^^^^^^^^^^^^^^^^

deploy_prometheus.sh
""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/deploy_prometheus.sh
    :language: bash

deploy-graf-prom.yaml
"""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/deploy-graf-prom.yaml
    :language: yaml

docker_prometheus.yaml
""""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/docker_prometheus.yaml
    :language: yaml

deploy_etcd_collect.sh
""""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/deploy_etcd_collect.sh
    :language: bash

Configuration files
^^^^^^^^^^^^^^^^^^^

prometheus-kuber.yml.j2
"""""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/prometheus/prometheus-kuber.yml.j2
    :language: bash

prometheus-system.yml.j2
""""""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/prometheus/prometheus-system.yml.j2
    :language: bash

targets.yml.j2
""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/prometheus/targets.yml.j2
    :language: bash

Grafana dashboards configuration
--------------------------------

:download:`Systems_nodes_statistics.json <configs/dashboards/Systems_nodes_statistics.json>`

:download:`Kubernetes_statistics.json <configs/dashboards/Kubernetes_statistics.json>`

:download:`ETCD.json <configs/dashboards/ETCD.json>`

:download:`OpenStack.json <configs/dashboards/OpenStack.json>`

ElasticSearch deployment script
-------------------------------

deploy_elasticsearch_kibana.sh
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: configs/elasticsearch-heka/deploy_elasticsearch_kibana.sh
    :language: bash

Telegraf deployment and configuration files
-------------------------------------------

deploy_telegraf.sh
^^^^^^^^^^^^^^^^^^

.. literalinclude:: configs/prometheus-grafana-telegraf/deploy_telegraf.sh
    :language: bash

deploy-telegraf.yaml
^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: configs/prometheus-grafana-telegraf/deploy-telegraf.yaml
    :language: yaml

Telegraf system
^^^^^^^^^^^^^^^

telegraf-sys.conf
"""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/telegraf-sys.conf
    :language: bash

Telegraf  openstack
^^^^^^^^^^^^^^^^^^^

telegraf-openstack.conf.j2
""""""""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/telegraf-openstack.conf.j2
    :language: bash

Telegraf inputs scripts
^^^^^^^^^^^^^^^^^^^^^^^

list_openstack_processes.sh
"""""""""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/list_openstack_processes.sh
    :language: bash

per_process_cpu_usage.sh
""""""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/per_process_cpu_usage.sh
    :language: bash

numa_stat_per_pid.sh
""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/numa_stat_per_pid.sh
    :language: bash

iostat_per_device.sh
""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/iostat_per_device.sh
    :language: bash

memory_bandwidth.sh
"""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/memory_bandwidth.sh
    :language: bash

network_tcp_queue.sh
""""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/network_tcp_queue.sh
    :language: bash

etcd_get_metrics.sh
"""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/etcd_get_metrics.sh
    :language: bash

k8s_get_metrics.sh
""""""""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/k8s_get_metrics.sh
    :language: bash

vmtime.sh
"""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/vmtime.sh
    :language: bash

osapitime.sh
""""""""""""

.. literalinclude:: configs/prometheus-grafana-telegraf/telegraf/scripts/osapitime.sh
    :language: bash

Heka deployment and configuration
---------------------------------

Deployment
^^^^^^^^^^

deploy_heka.sh
""""""""""""""

.. literalinclude:: configs/elasticsearch-heka/deploy_heka.sh
    :language: bash

deploy-heka.yaml
""""""""""""""""

.. literalinclude:: configs/elasticsearch-heka/deploy-heka.yaml
    :language: yaml

Configuration
^^^^^^^^^^^^^

00-hekad.toml.j2
""""""""""""""""

.. literalinclude:: configs/elasticsearch-heka/heka/00-hekad.toml.j2
    :language: bash

kubeapi_to_int.lua.j2
"""""""""""""""""""""

.. literalinclude:: configs/elasticsearch-heka/heka/kubeapi_to_int.lua.j2
    :language: bash


.. references:

.. _Fuel-CCP-Installer: https://github.com/openstack/fuel-ccp-installer
.. _Kargo: https://github.com/kubernetes-incubator/kargo.git
.. _Fuel-CCP: https://github.com/openstack/fuel-ccp
.. _Prometheus: https://prometheus.io/
.. _Prometheus GitHub: https://github.com/prometheus/prometheus
.. _Grafana: http://grafana.org/
.. _ElasticSearch: https://www.elastic.co/products/elasticsearch
.. _Kibana: https://www.elastic.co/products/kibana
.. _Telegraf: https://www.influxdata.com/time-series-platform/telegraf/
.. _GitHub Telegraf Fork: https://github.com/spjmurray/telegraf/tree/openstack_stats/plugins/inputs/openstack
.. _Go SDK for OpenStack: https://github.com/rackspace/gophercloud/
.. _Heka: https://hekad.readthedocs.io/en/v0.10.0/
.. _K8S Ingress Resources: http://kubernetes.io/docs/user-guide/ingress/


