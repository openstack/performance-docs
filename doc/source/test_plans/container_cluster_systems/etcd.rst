
.. _ETCD_health_tests:

==============================
ETCD health research test plan
==============================

:status: **ready**
:version: 1.0

:Abstract:

  This document is a test plan for ETCD health research that should
  determine a process of getting the dependency between Kubernetes
  cluster under load and ETCD cluster health state.

Test Plan
=========

We should obtain the test results by collecting crucial system
metrics that provided natively by ETCD/Kubernetes API, compare and
normalize them and plot dependency graphs.

Test Environment
----------------

Preparation
^^^^^^^^^^^

1.
  Monitoring system must be set up and working, basing on the
  `Monitoring`_ methodology documentation.

2.
  K8S cluster should be deployed using `Kargo`_ on top of the
  430 nodes with preinstalled Ubuntu Xenial.
3.
  On the one of the K8S master we should check/install the
  following packages/tools:


.. table:: Software to be installed

  +--------------+---------+-----------------------------------+
  | package name | version | source                            |
  +==============+=========+===================================+
  | `curl`_      | latest  | Ubuntu xenial universe repository |
  +--------------+---------+-----------------------------------+
  | `jq`_        | latest  | Ubuntu xenial universe repository |
  +--------------+---------+-----------------------------------+
  | `paste`_     | latest  | Ubuntu xenial universe repository |
  +--------------+---------+-----------------------------------+
  | `MMM`_       | latest  | GitHub                            |
  +--------------+---------+-----------------------------------+
  | `Hoseproxy`_ | latest  | Github                            |
  +--------------+---------+-----------------------------------+

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

Test results MUST include a description of the environment used. The following
items should be included:

- **Hardware configuration of each server.** If virtual machines are used then
  both physical and virtual hardware should be fully documented.
  An example format is given below:

.. table:: Description of server hardware

  +-------+----------------+-------+-------+
  |server |name            |       |       |
  |       +----------------+-------+-------+
  |       |role            |       |       |
  |       +----------------+-------+-------+
  |       |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |operating_system|       |       |
  +-------+----------------+-------+-------+
  |CPU    |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |processor_count |       |       |
  |       +----------------+-------+-------+
  |       |core_count      |       |       |
  |       +----------------+-------+-------+
  |       |frequency_MHz   |       |       |
  +-------+----------------+-------+-------+
  |RAM    |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |amount_MB       |       |       |
  +-------+----------------+-------+-------+
  |NETWORK|interface_name  |       |       |
  |       +----------------+-------+-------+
  |       |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |bandwidth       |       |       |
  +-------+----------------+-------+-------+
  |STORAGE|dev_name        |       |       |
  |       +----------------+-------+-------+
  |       |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |SSD/HDD         |       |       |
  |       +----------------+-------+-------+
  |       |size            |       |       |
  +-------+----------------+-------+-------+

- **Configuration of hardware network switches.** The configuration file from
  the switch can be downloaded and attached.


- **Network scheme.** The plan should show how all hardware is connected and
  how the components communicate. All ethernet/fibrechannel and VLAN channels
  should be included. Each interface of every hardware component should be
  matched with the corresponding L2 channel and IP address.

Test Cases
----------

Description
^^^^^^^^^^^

There are two specific cases that should be conducted.

1.
  Load K8S with as much big as possible number of pods per each node.
  Stop when either of K8S or ETCD degrades or existing limits are reached.

2.
  Load K8S with as much big as possible number of services.
  Stop when either of K8S or ETCD degrades or existing limits are reached.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Basing on `CoreOS ETCD`_ documentation, we collected a list of key metrics
that define ETCD cluster health state:


.. table:: List of performance metrics

  +------------------------------------------------------------+------------------------------------------+
  | Metrics                                                    | Short description                        |
  +============================================================+==========================================+
  |                                                            || Resident memory size in bytes.          |
  | process_resident_memory_bytes                              ||                                         |
  |                                                            ||                                         |
  +------------------------------------------------------------+------------------------------------------+
  |                                                            || The total latency distributions of save |
  | etcd_debugging_snap_save_total_duration_seconds_bucket     || called by snapshot.                     |
  |                                                            ||                                         |
  +------------------------------------------------------------+------------------------------------------+
  |                                                            || The latency distributions of commit     |
  | etcd_disk_backend_commit_duration_seconds_bucket           || called by backend.                      |
  |                                                            ||                                         |
  +------------------------------------------------------------+------------------------------------------+
  |                                                            || Counter of handle failures of requests  |
  | etcd_http_failed_total                                     || (non-watches), by method (GET/PUT etc.) |
  |                                                            || and code (400, 500 etc.).               |
  +------------------------------------------------------------+------------------------------------------+
  |                                                            || The total number of bytes received/sent |
  | etcd_network_peer_(received|sent)_bytes_total              || from/to peers.                          |
  |                                                            ||                                         |
  +------------------------------------------------------------+------------------------------------------+
  |                                                            || Current number of proposals pending/    |
  | etcd_server_proposals_(pending|committed|applied|failed)   || committed/applied/failed.               |
  |                                                            ||                                         |
  +------------------------------------------------------------+------------------------------------------+

K8S-sided metrics should only define total number of pods/services in the cluster
for each moment of time within testing period.

Collecting metrics
^^^^^^^^^^^^^^^^^^

Each required metric could be gathered through `Prometheus API`_ using
curl and jq to extract json objects and strip off extra data. For
example, let say we need to get `<metric_a>` values within period
starting from `<start>` and finishing at `<stop>` with a time step
= `<step>`. Prometheus IP address is `<prometheus_server>`. Resulted
query will look like:

.. code:: bash

  curl -q 'http://<prometheus_server>/api/v1/query_range?query=<metric_a>&start=<start>&end=<end>&step=<step>'

Plotting 'K8S vs ETCD dependency'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After obtaining metrics for each case, we need to make plots showing
dependency between K8S pods/services number and corresponding metric.
It's better to merge collected metrics in two csv files (for each case)
in order to make plots easily using third-party instruments like
`Google sheets`_ or `Plotly`_.

Reports
=======

Resulted report page:
* :ref:`Results_of_the_ETCD_health_tests`

.. references:

.. _Kargo: https://github.com/kubernetes-incubator/kargo.git
.. _Monitoring: https://docs.openstack.org/developer/performance-docs/methodologies/monitoring/index.html
.. _curl: https://curl.haxx.se/
.. _jq: https://stedolan.github.io/jq/
.. _paste: https://linux.die.net/man/1/paste
.. _MMM: https://github.com/AleksandrNull/MMM
.. _Hoseproxy: https://github.com/ivan4th/hoseproxy
.. _CoreOS ETCD: https://coreos.com/etcd/docs/latest/metrics.html
.. _Prometheus API: https://prometheus.io/docs/querying/api/
.. _Google sheets: https://docs.google.com/spreadsheets/
.. _Plotly: https://plot.ly/

