.. _keystone_performance:

============================
Keystone Performance testing
============================

:status: **ready**
:version: 1.0

:Abstract:

  This document describes a test plan for measuring OpenStack Identity service
  (Keystone) performance, including primary analysis of database and cache
  operations effectiveness. This test plan assumes to use OSprofiler library
  for cross-project OpenStack requests profiling.

Test Plan
=========

Keystone is an OpenStack project that provides Identity, Token, Catalog and
Policy services for use specifically by projects in the OpenStack family.
It implements OpenStack’s Identity API and is widely used by almost all
OpenStack services, therefore its performance is a key. To evaluate it this
test plan proposes to use OSprofiler.

OSprofiler is an Oslo library that provides Python wrappers to trace
operations on the Python level. It provides several ways to wrap
separated methods, all methods inside one specific class and all methods
encapsulated under Python classes having common ancestor.

For every profiled method, notifications are sent about operation start time
and end time, including information about parent operation. Right now these
notifications are stored as OpenStack Telemetry (Ceilometer) events, so on
high level OpenStack profiling process can be presented as follows:

.. image:: profiling_workflow.png
    :width: 650px

Test Environment
----------------

This section describes the setup for Keystone testing. It can be either
a single (all-in-one) or a multi-node installation.

A single-node setup requires just one node to be up and running. It has
both compute and controller roles and all OpenStack services run on this node.
This setup does not support test cases, related to the performance
measurements, combined with the components HA testing.

A basic multi-node setup with Keystone comprises 4 physical nodes:
  * One node for a compute node. This node simulates activity which is
    typical for OpenStack compute components.
  * Three nodes for a controller nodes. These node simulate activity which
    is typical for OpenStack control plane services, including running three
    MySQL instances managed by Galera cluster and memcached cluster for
    Keystone caching.

Preparation
^^^^^^^^^^^

**Common preparation steps**

No matter if you're running single node or multi node setup, you will require
several steps to be completed before running any profiling tasks:
  * Ensure OSprofiler library_ is installed to all environment nodes to present
    most full information in the trace.
  * OSprofiler requires persistent profiling events storage to be presented in
    the environment. For now, the only supported variant is to use OpenStack
    Telemetry (Ceilometer) project, that will consume profiling events via
    message queue notifications from the affected OpenStack services.
  * OSprofiler integration to the OpenStack projects is ongoing initiative,
    so please ensure that all OpenStack services you would like to profile
    support it in your environment. Here is a project to release mapping that
    can be useful:
      * Cinder OSprofiler support - OpenStack Juno release
      * Glance OSprofiler support - OpenStack Juno release
      * Heat OSprofiler support - OpenStack Juno release
      * Trove OSprofiler support - OpenStack Juno release
      * Nova_ OSprofiler support - [planned] OpenStack Newton release
      * Neutron_ OSprofiler support - [planned] OpenStack Newton release
      * Keystone_ OSprofiler support - [planned] OpenStack Newton release
    At the time of this document composing Nova, Neutron and Keystone changes
    need to be applied manually to trace these projects usage.
  * Please make sure that all OpenStack services are properly configured to
    allow cross-project request profiling. In case of single node installation
    using DevStack this will be automatically managed by OSprofiler DevStack
    plugin, but for multi node environment this needs to be tracked separately.
    Please pay attention to the appropriate subsection under `Multi node
    installation` section.
  * Test cases described in this document suppose to collect information for
    comparison analysis of Keystone database and cache operations
    effectiveness, that requires Keystone reconfiguration depending on if
    caching mechanism is used at the moment or not. This is tracked via
    specialized `keystone.conf` file section::

        [cache]
        enabled = True|False
        backend = oslo_cache.memcache_pool
        memcache_servers = <memcached_host>:<memcached_port>[,<memcached_host>:<memcached_port>]
        expiration_time = 600

**Single node installation**

For single node installation the one can use DevStack_ tool that is targeted
at developers and CI systems to use upstream code. It makes many choices that
are not appropriate for production systems, but for the all-in-one purposes
this can fit ok.

At the time of document writing, DevStack's `local.conf` should be looking like
as following to have and all-in-one OpenStack installation with Neutron enabled
and OSprofiler installation included with all needed fixes to the OpenStack
services::

    [[local|localrc]]
    ADMIN_PASSWORD=password
    DATABASE_PASSWORD=$ADMIN_PASSWORD
    RABBIT_PASSWORD=$ADMIN_PASSWORD
    SERVICE_PASSWORD=$ADMIN_PASSWORD

    LIBS_FROM_GIT=osprofiler,python-openstackclient

    NOVA_REPO=https://review.openstack.org/p/openstack/nova
    NOVA_BRANCH=refs/changes/03/254703/39

    KEYSTONE_REPO=https://review.openstack.org/p/openstack/keystone
    KEYSTONE_BRANCH=refs/changes/35/294535/2

    NEUTRON_REPO=https://review.openstack.org/p/openstack/neutron
    NEUTRON_BRANCH=refs/changes/51/273951/12

    disable_service n-net horizon
    enable_service q-svc q-dhcp q-meta q-agt q-l3 neutron

    enable_plugin ceilometer https://git.openstack.org/openstack/ceilometer.git
    enable_plugin osprofiler https://github.com/openstack/osprofiler.git

To add Fernet tokens usage (as for the time of document writing, default token
format for DevStack is still UUID), the next line needs to be added
explicitly::

    KEYSTONE_TOKEN_FORMAT=fernet


Please make sure to have identical cache configuration for Keystone authtoken
middleware. For example, cache might be external (memcached) and appropriate
configuration section will look like this in this case::

    [keystone_authtoken]
    memcache_servers = <memcached_host>:<memcached_port>[,<memcached_host>:<memcached_port>]
    signing_dir = <signing_dir>
    cafile = <cafile.pem>
    auth_uri = <auth_uri>
    project_domain_id = <domain>
    project_name = <service>
    user_domain_id = <domain>
    password = <password>
    username = <project_user_name>
    auth_url = <auth_url>
    auth_plugin = <password>

Sadly there is no simple way to setup specific patches to be applyed on the
python libraries used (OpenStack clients, OSProfiler, etc.) so they require
manual patching in this case:

* `OSprofiler changes`_

**Multi node installation**

Multi node environment installation depends much on the chosen set of OpenStack
deployment tools. Whatever instrument will be used, please consider to ensure
the following patches to be applied against main OpenStack services to be
profiled (Nova, Neutron, Keystone) and the appropriate libraries:

* `OSprofiler changes`_
* Nova_ OSprofiler integration
* Neutron_ OSprofiler integration
* Keystone_ OSprofiler integration

*OpenStack services configuration*

Several OpenStack configuration files need to be modified to enable appropriate
OSprofiler workability.

First of all, the one needs to enable `Ceilometer` profiling events storage via
adding the following lines to the `event_definitions.yaml` file, declaratively
announcing the wish to consume them::

    - event_type: profiler.*
      traits:
        project:
          fields: payload.project
        service:
          fields: payload.service
        name:
          fields: payload.name
        base_id:
          fields: payload.base_id
        trace_id:
          fields: payload.trace_id
        parent_id:
          fields: payload.parent_id
        timestamp:
          fields: payload.timestamp
        host:
          fields: payload.info.host
        path:
          fields: payload.info.request.path
        query:
          fields: payload.info.request.query
        method:
          fields: payload.info.request.method
        scheme:
          fields: payload.info.request.scheme
        db.statement:
          fields: payload.info.db.statement
        db.params:
          fields: payload.info.db.params

Also, for extended tracing information providing it's useful (although, not
mandatory if you need only high-level traces) to add the following lines to the
`ceilometer.conf` configuration file::

    [event]
    store_raw=info

.. note:: Please pay attention to the fact, that the configuration parameter
          defined above will store raw events for **all** `info` level event
          notifications coming to the Ceilometer queue. Please make sure either
          to turn off not needed events in `event_definitions.yaml` or save
          enough place for the Ceilometer storage backend.

Also for every project you would like to trace it's required to enable its
profiling via service configuration files and add the following section::

    [profiler]
    enabled = True
    trace_sqlalchemy = True
    hmac_keys = SECRET_KEY

In this test plan it's supposed to turn profiling on for Cinder, Glance, Nova,
Neutron and Keystone.

.. _library: https://pypi.python.org/pypi/osprofiler
.. _Nova: https://review.openstack.org/#/q/status:open+branch:master+topic:bp/osprofiler-support-in-nova
.. _Neutron: https://review.openstack.org/#/q/status:open++branch:master+topic:bug/1335640
.. _Keystone: https://review.openstack.org/#/q/status:open+branch:master+topic:osprofiler-support-in-keystone
.. _DevStack: http://devstack.org
.. _OSprofiler changes: https://review.openstack.org/#/c/294516/

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers,
network parameters, operation system and OpenStack deployment characteristics.

Hardware
~~~~~~~~

This section contains list of all types of hardware nodes.

+-----------+-------+----------------------------------------------------+
| Parameter | Value | Comments                                           |
+-----------+-------+----------------------------------------------------+
| model     |       | e.g. Supermicro X9SRD-F                            |
+-----------+-------+----------------------------------------------------+
| CPU       |       | e.g. 6 x Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz |
+-----------+-------+----------------------------------------------------+

Network
~~~~~~~

This section contains list of interfaces and network parameters.
For complicated cases this section may include topology diagram and switch
parameters.

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
~~~~~~~~

This section describes installed software.

+-----------------+--------+---------------------------+
| Parameter       | Value  | Comments                  |
+-----------------+--------+---------------------------+
| OS              |        | e.g. Ubuntu 14.04.3       |
+-----------------+--------+---------------------------+
| Keystone DB     |        | e.g. MySQL 5.6            |
+-----------------+--------+---------------------------+
| Keystone Cache  | on/off | e.g. memcached v1.4.25    |
+-----------------+--------+---------------------------+
| HA mode         |        | e.g. Cluster              |
+-----------------+--------+---------------------------+

Test Case 1: Keystone DB / cache operations analysis
----------------------------------------------------

Description
^^^^^^^^^^^

This test records all HTTP, RPC and DB calls happening during selected list of
OpenStack control plane operations, including Keystone operations and their
duration via OSprofiler. Human-readable report would be automatically generated
to evaluate overall number of DB / cache calls, as well as raw information
ported to the JSON format.

Let's focus on the following control plane operations:

* Keystone token get (token issue)
* Keystone user list
* Keystone endpoint list
* Keystone service list
* Nova instance boot (server create)

OSprofiler adds an opportunity to call CLI command, generating report on the
profiled control plane operation  in one of the chosen formats - either JSON
or HTML.

To initiate OpenStack request tracing `--profile <HMAC_KEY>` option needs to
be added to the CLI command, triggering this specific action. This key needs
to present one of the secret keys defined in <project>.conf configuration file
with `hmac_keys` option under the `[profiler]` configuration section. In case
if all OpenStack projects have shared HMAC_KEY defined in their configuration
files, it will be possible to generate a report, containing tracing points from
all services taking part in the request processing.

To initiate VM creation tracing the following command should be used from the
CLI::

    openstack --profile SECRET_KEY server create --image <image> --flavor <flavor> <server-name>

Without `--profile SECRET_KEY` option trace generation won't be triggered even
if it's enabled in the OpenStack services configuration files.

At the end of output there will be message printed with <trace_id>, and to
plot nice HTML graphs the following command should be used::

    osprofiler trace show <trace_id> --html --out result.html

 All other chosen control plane operations request can be traced via similar
 approach.

Parameters
^^^^^^^^^^

=========================== ====================================================
Parameter name              Value
=========================== ====================================================
OpenStack release           Liberty, Mitaka
Cache                       on, off
Token type                  UUID, fernet
Environment characteristics Single node, multi node (clusterized DB / memcached)
=========================== ====================================================

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test case result is presented as a weighted tree structure with operations
as nodes and time spent on them as node weights for every control plane
operation under the test. This information is automatically gathered in
Ceilometer and can be gracefully transformed to the human-friendly report via
OSprofiler.

========  ==============  =================  =========================================
Priority  Value           Measurement Units  Description
========  ==============  =================  =========================================
1         Operation time  milliseconds       Time spent on every HTTP/RPC/DB operation
========  ==============  =================  =========================================

.. note:: Please keep in mind that OSprofiler uses python code and libraries
          to listen on specific events to happen - in common case that will be
          `before method starts` and `after method starts` via Python
          decorators usage, therefore time it collects includes time spent on
          Python operations inside. For DB calls tracing OSprofiler uses
          `before_cursor_execute` and `after_cursor_execute` events defined in
          SQLAlchemy library.

Test Case 2: Keystone DB / cache operations analysis (HA version)
-----------------------------------------------------------------

Description
^^^^^^^^^^^

This test case  should provide almost the same analysis as the previous one,
the difference is in adding failover testing component to the research. First
test run assumes to be the same as for previous case, the second one should
happen after turning off one of the distributed components used by Keystone,
e.g. stop one of memcached instances and run the same control plane operations
tracing.

Parameters
^^^^^^^^^^

=========================== ====================================================
Parameter name              Value
=========================== ====================================================
OpenStack release           Liberty, Mitaka
Cache                       on, off
Token type                  UUID, fernet
Environment characteristics Single node, multi node (clusterized DB / memcached)
Memcached cluster status    3 nodes, 2 nodes, 1 node
Galera cluster status       3 nodes, 2 nodes
=========================== ====================================================

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ==============  =================  =========================================
Priority  Value           Measurement Units  Description
========  ==============  =================  =========================================
1         Operation time  milliseconds       Time spent on every HTTP/RPC/DB operation
========  ==============  =================  =========================================
