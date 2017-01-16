.. _scale_testing_issues:

======================================
Kubernetes Issues At Scale 900 Minions
======================================

Glossary
========

-  **Kubernetes** is an open-source system for automating deployment,
   scaling, and management of containerized applications.

-  **fuel-ccp**: CCP stands for “Containerized Control Plane”. The goal
   of this project is to make building, running and managing
   production-ready OpenStack containers on top of Kubernetes an
   easy task for operators.

-  **OpenStack** is a cloud operating system that controls large pools
   of compute, storage, and networking resources throughout a
   datacenter, all managed through a dashboard that gives
   administrators control while empowering their users to provision
   resources through a web interface.

-  **Heat** is an OpenStack service to orchestrate composite cloud
   applications using a declarative template format through an
   OpenStack-native REST API.

-  **Slice** is a set of 6 VMs:

   -  1x Yahoo! Benchmark (ycsb)

   -  1x Cassandra

   -  1x Magento

   -  1x Wordpress

   -  2x Idle VM


Setup
=====

We had about 181 bare metal machines, 3 of them were used for Kubernetes
control plane services placement (API servers, ETCD, Kubernetes
scheduler, etc.), others had 5 virtual machines on each node, where
every VM was used as a Kubernetes minion node.

Each bare metal node has the following specifications:

-  HP ProLiant DL380 Gen9

-  **CPU** - 2x Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz

-  **RAM** - 264G

-  **Storage** - 3.0T on RAID on HP Smart Array P840 Controller, HDD -
   12 x HP EH0600JDYTL

-  **Network** - 2x Intel Corporation Ethernet 10G 2P X710

Running OpenStack cluster (from Kubernetes point of view) is represented
with the following numbers:

1. OpenStack control plane services are running within ~80 pods on 6
   nodes

2. ~4500 pods are spread across all remaining nodes, 5 pods on each.

Kubernetes architecture analysis obstacles
==========================================

During the 900 nodes tests we used `Prometheus <https://prometheus.io/>`__
monitoring tool for the
verification of the resources consumption and the load put on core
system, Kubernetes and OpenStack levels services. During one of the
Prometheus configuration optimisations old data from the Prometheus
storage was deleted to improve Prometheus API speed, and this old data
included 900 nodes cluster information, therefore we have only partial
data being available for the post run investigation. This fact,
although, does not influence overall reference architecture analysis, as
all issues, that were observed during the containerized OpenStack setup
testing, were thoughtfully documented and debugged.

To prevent monitoring data loss in future (Q1 2017 timeframe and
further) we need to proceed with the following improvements of the
monitoring setup:

1. Prometheus by default is more optimized to be used as real time
   monitoring / alerting system, and there is an official
   recommendation from Prometheus developers team to keep monitoring
   data retention for about 15 days to keep tool working in quick
   and responsive manner. To keep old data for the post-usage
   analytics purposes external store requires to be configured.

2. We need to reconfigure monitoring tool (Prometheus) to include data
   backup to one of the persistent time series databases (e.g.
   InfluxDB / Cassandra / OpenTSDB) that’s supported as an external
   persistent data store by Prometheus. This will allow us to store
   old data for extended amount of time for post-processing needs.

Observed issues
===============

Huge load on kube-apiserver
---------------------------

Symptoms
~~~~~~~~

Both API servers, running in Kubernetes cluster, were utilising up to
2000% of CPU (up to 45% of total node compute performance capacity)
after we migrated them to hardware nodes. Initial setup with all nodes
(including Kubernetes control plane nodes) running on virtualized
environment was showing not workable API servers at all.

Root cause
~~~~~~~~~~

All services that are placed not on Kubernetes masters (``kubelet``,
``kube-proxy`` on all minions) access ``kube-apiserver`` via local
``ngnix`` proxy.

Most of those requests are watch requests that stay mostly idle after
they are initiated (most timeouts on them are defined to be about 5-10
minutes). ``nginx`` was configured to cut idle connections in 3 seconds,
which makes all clients to reconnect and (the worst) restart aborted SSL
session. On the server side it makes ``kube-apiserver`` consume up to 2000%
CPU resources and other requests become very slow.

Solution
~~~~~~~~

Set ``proxy_timeout`` parameter to 10 minutes in ``nginx.conf`` config
file, which should be more than enough not to cut SSL connections before
requests time out by themselves. After this fix was applied, one
api-server became to consume 100% of CPU (about 2% of total node compute
performance capacity), the second one about 200% (about 4% of total node
compute performance capacity) of CPU (with average response time 200-400
ms).

Upstream issue (fixed)
~~~~~~~~~~~~~~~~~~~~~~

Make Kargo deployment tool set ``proxy_timeout`` to 10 minutes:
`issue <https://github.com/kubernetes-incubator/kargo/issues/655>`__
fixed with `pull request <https://github.com/kubernetes-incubator/kargo/pull/656>`__
by Fuel CCP team.

KubeDNS cannot handle big cluster load with default settings
------------------------------------------------------------

Symptoms
~~~~~~~~

When deploying OpenStack cluster on this scale, ``kubedns`` becomes
unresponsive because of high load. This end up with very often error
appearing in logs of ``dnsmasq`` container in ``kubedns`` pod::

    Maximum number of concurrent DNS queries reached.

Also ``dnsmasq`` containers sometimes get restarted due to hitting high
memory limit.

Root cause
~~~~~~~~~~

First of all, ``kubedns`` seems to fail often on high load (or even without
load), during the experiment we observed continuous kubedns container
restarts even on empty (but big enough) Kubernetes cluster. Restarts
are caused by liveness check failing, although nothing notable is
observed in any logs.

Second, ``dnsmasq`` should have taken load off ``kubedns``, but it needs some
tuning to behave as expected for big load, otherwise it is useless.

Solution
~~~~~~~~

This requires several levels of fixing:

1. Set higher limits for ``dnsmasq`` containers: they take on most of the
   load.

2. Add more replicas to ``kubedns`` replication controller (we decided to
   stop on 6 replicas, as it solved the observed issue - for bigger
   clusters it might be needed to increase this number even more).

3. Increase number of parallel connections ``dnsmasq`` should handle (we
   used ``--dns-forward-max=1000`` which is recommendaed parameter setup
   in ``dnsmasq`` manuals)

4. Increase size of cache in ``dnsmasq``: it has hard limit of 10000 cache
   entries which seems to be reasonable amount.

5. Fix ``kubedns`` to handle this behaviour in proper way.

Upstream issues (partially fixed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#1 and #2 are fixed by making them configurable in Kargo by Kubernetes
team:
`issue <https://github.com/kubernetes-incubator/kargo/issues/643>`__,
`pull request <https://github.com/kubernetes-incubator/kargo/pull/652>`__.

Other fixes are still being implemented as of time of this publication.

Kubernetes scheduler is ineffective with pod antiaffinity
---------------------------------------------------------

Symptoms
~~~~~~~~

It takes significant amount of time for scheduler to process pods with
pod antiaffinity rules specified on them. It is spending about **2-3
seconds** on each pod which makes time needed to deploy OpenStack
cluster on 900 nodes unexpectedly long (about 3h for just scheduling).
Antiaffinity rules are required to be used for OpenStack deployment to
prevent several OpenStack compute nodes to be mixed and messed to one
Kubernetes Minion node.

Root cause
~~~~~~~~~~

According to profiling results, most of the time is spent on creating
new Selectors to match existing pods against them, which triggers
validation step. Basically we have O(N^2) unnecessary validation steps
(N - number of pods), even if we have just 5 deployments entities
covering most of the nodes.

Solution
~~~~~~~~

Specific optimization that speeds up scheduling time up to about 300
ms/pod was required in this case. It’s still slow in terms of common
sense (about 30m spent just on pods scheduling for 900 nodes OpenStack
cluster), but is close to be reasonable. This solution lowers number of
very expensive operations to O(N), which is better, but still depends on
number of pods instead of deployments, so there is space for future
improvement.

Upstream issues
~~~~~~~~~~~~~~~

Optimization merged into master: `pull
request <https://github.com/kubernetes/kubernetes/pull/37691>`__;
backported to 1.5 branch (will release in 1.5.2 release): `pull
request <https://github.com/kubernetes/kubernetes/pull/38693>`__.

Kubernetes scheduler needs to be deployed on separate node
----------------------------------------------------------

Symptoms
~~~~~~~~

During huge OpenStack cluster deployment against pre-deployed
Kubernetes ``scheduler``, ``controller-manager`` and ``apiserver`` start
competing for CPU cycles as all of them get big load. Scheduler is more
resource-hungry (see next problem), so we need a way to deploy it
separately.

Root Cause
~~~~~~~~~~

The same problem with Kubsernetes scheduler efficiency at scale of about
1000 nodes as in the issue above.

Solution
~~~~~~~~

Kubernetes scheduler was moved to a separate node manually, all other
schedulers were manually killed to prevent them from moving to other
nodes.

Upstream issues
~~~~~~~~~~~~~~~

`Issue <https://github.com/kubernetes-incubator/kargo/issues/834>`__
created in Kargo installer Github repository.

kube-apiserver have low default rate limit
------------------------------------------

Symptoms
~~~~~~~~

Different services start receiving “429 Rate Limit Exceeded” HTTP error
even though ``kube-apiservers`` can take more load. It is linked to a
scheduler bug (see below).

Solution
~~~~~~~~

Raise rate limit for ``kube-apiserver process`` via ``--max-requests-inflight``
option. It defaults to 400, in our case it became workable at 2000. This
number should be configurable in Kargo deployment tool, as for bigger
deployments it might be required to increase it accordingly.

Upstream issues
~~~~~~~~~~~~~~~

Upstream issue or pull request was not created for this issue.

Kubernetes scheduler can schedule wrongly
-----------------------------------------

Symptoms
~~~~~~~~

When many pods are being created (~4500 in our case of OpenStack
deployment) and faced with 429 error from ``kube-apiserver`` (see above),
the scheduler can schedule several pods of the same deployment on one node
in violation of pod antiaffinity rule on them.

Root cause
~~~~~~~~~~

This issue arises due to scheduler cache being evicted before the pod
actually processed.

Upstream issues
~~~~~~~~~~~~~~~

`Pull
request <https://github.com/kubernetes/kubernetes/pull/38503>`__ accepted
in Kubernetes upstream.

Docker become unresponsive at random
------------------------------------

Symptoms
~~~~~~~~

Docker process sometimes hangs on several nodes, which results in
timeouts in ``kubelet`` logs and pods cannot be spawned or terminated
successfully on the affected minion node. Although bunch of similar
issues has been fixed in Docker since 1.11, we still are observing those
symptoms.

Workaround
~~~~~~~~~~

Docker daemon logs does not contain any notable information, so we had
to restart docker service on the affected node (during those experiments
we used Docker 1.12.3, but we have observed similar symptoms in 1.13
as well).

Calico start up time is too long
--------------------------------

Symptoms
~~~~~~~~

If we have to kill a Kubernetes node, Calico requires ~5 minutes to
reestablish all mesh connections.

Root cause
~~~~~~~~~~

Calico uses BGP, so without route reflector it has to do full-mesh
between all nodes in cluster.

Solution
~~~~~~~~

We need to switch to using route reflectors in our clusters. Then every
node needs only to establish connections to all reflectors.

Upstream Issues
~~~~~~~~~~~~~~~

None. For production use, architecutre of Calico network should be
adjusted to use route reflectors set up on selected nodes or on
switching fabric hardware. This will reduce the number of BGP
connections per node and speed up the Calico startup.

===========================================
OpenStack Issues At Scale 200 Compute Nodes
===========================================

Workloads testing approach
==========================

The goal of this test was to investigate OpenStack and Kubernetes
behavior under load. This load needs to emulate end-user traffic running
on OpenStack servers (guest systems) with different types of
applications running against cloud system. We were interested in the
following metrics: CPU usage, Disk statistics, Network load, Memory used
and IO stats on each controller nodes and chosen set of the compute
nodes.

Testing preparation steps
-------------------------

To preare for testing, several steps should be made:

-  [0] Pre-deploy Kubernetes + OpenStack Newton environment (Kargo +
   fuel-ccp tools)

-  [1] Establish advanced monitoring of the testing environment (on
   all three layers - system, Kubernetes and OpenStack)

-  [2] Prepare to automatically deploy slices against OpenStack and
   configure applications running within them

-  [3] Prepare to run workloads against applications running within
   slices

[1] was achieved through configuring Prometheus monitoring and alerting
tool with Collectd and Telegraf collectors. Separated monitoring
document is under preparation to present significant effort spent on
this task.

[2] was automated by using Heat OpenStack orchestration service
`templates <https://github.com/ayasakov/hot-ansible-templates>`__.

[3] was automated mostly through generating HTTP trafic native for the
applications under test using Locust.IO tool
`templates <https://github.com/ayasakov/locustio-workloads>`__.
Cassandra VM workload was automated through Yahoo! Benchmark (ycsb)
running on neighbour VM of the same slice.

Step [1] was tested against 900 nodes Kubernetes cluster described in
section above and later against all test environments we had, steps [2] and
[3] were verified against small (20 nodes) testing environment in
parallel with finalizing step [1] workability. During this verification
several issues with recently introduced Heat support to fuel-ccp were
observed and fixed. Later all of those steps were assumed to be run
against 200 bare metal nodes lab, but bunch of issues was observed
during step [2] that blocked finishing the testing. All of those issues
(including those found during small environment verification) are listed
below.

Heat/fuel-ccp integration issues
================================

Lack of Heat domain configuration
---------------------------------

Symptoms
~~~~~~~~

Authentication errors during Heat stacks (representing workloads testing
slices on each compute node) creation.

Root cause
~~~~~~~~~~

During OpenStack Newton timeframe Orchestration has started to require
additional information in the Identity service to manage stacks - in
particular, configuration of heat domain that would contain stacks
projects and users, creating of ``heat_domain_admin`` user to manage
projects and users in the heat domain and adding the admin role to the
``heat_domain_admin`` user in the heat domain to enable administrative
stack management privileges by the ``heat_domain_admin`` user. Please take
a look on `OpenStack Newton configuration
guide <http://docs.openstack.org/project-install-guide/orchestration/newton/install-ubuntu.html>`__
for more information.

Solution
~~~~~~~~

Set up needed configuration steps in ``fuel-ccp``:

-  `Patch #1 <https://review.openstack.org/#/c/400846/>`__

-  `Patch #2 <https://review.openstack.org/#/c/402045/>`__

Lack of heat-api-cfn service configuration in fuel-ccp
------------------------------------------------------

Symptoms
~~~~~~~~

Applications configured in Heat templates are not receiving their
configurations and data required for the succeeded applications
workability.

Root cause
~~~~~~~~~~

Initial Heat support in ``fuel-ccp`` did not include ``heat-api-cfn``
service, which is used by Heat for some config transports. This service is
necessary to support default ``user_data_format`` (``HEAT_CFNTOOLS``), used
for most applications-related Heat templates.

Solution
~~~~~~~~

Add new ``heat-api-cfn`` image, which will be used to create new service and
configure all necessary endpoints for it in ``fuel-ccp`` tool. Patches to
``fuel-ccp``:

-  `Patch #1 <https://review.openstack.org/#/c/401138/>`__

-  `Patch #2 <https://review.openstack.org/#/c/401174/>`__

Heat endpoint not reachable from virtual machines
-------------------------------------------------

Symptoms
~~~~~~~~

Heat API and Heat API CFN are not reachable from OpenStack VM, even
though some of the applications configurations require such access.

Root cause
~~~~~~~~~~

Fuel CCP deploys Heat services with default configuration and changes
``endpoint_type`` from ``publicURL`` to ``internalURL``. However,
such configuration in Kubernetes cluster is not enough for several types
of Heat stack resources like ``OS::Heat::Waitcondition`` and 
``OS::Heat::SoftwareDeployment``, which require callbacks to Heat API
or Heat API CFN. Due to Kubernetes  architecture, it's not possible to
do such callback on the default port value (for ``heat-api`` it's - 8004
and 8000 for ``heat-api-cfn``).

Solution
~~~~~~~~

There are two ways to fix described above issues:

-  Out of the box, which requires just adding some data to .ccp.yaml
   configuration file. This workaround can be used prior OpenStack
   cluster deployment during future OpenStack cluster description.

-  Second which requires some manual actions and can be processed when
   Openstack is already deployed and cloud administrator can change
   only one component configuration.

Both of those solutions are described in the `patch to Fuel CCP
Documentation <https://review.openstack.org/#/c/404114>`__. Please
notice that additionally `patch to Fuel CCP
codebase <https://review.openstack.org/#/c/405263/>`__ need to be
applied to make some of the Kubernetes options configurable.

Glance+Heat authentication misconfiguration
-------------------------------------------

Symptoms
~~~~~~~~

During Heat stacks (representing workloads testing slices) creation,
random Glance authentication errors were observed.

Root cause
~~~~~~~~~~

Service-specific users should have admin role in "service" project and
should not belong to user-facing admin project. Initially Fuel-CCP
contained Glance and Heat services misconfigured and several patches
were required to fix it.

Solution
~~~~~~~~

-  `Patch #1 <https://review.openstack.org/#/c/409033/>`__

-  `Patch #2 <https://review.openstack.org/#/c/409037/>`__

Workloads Testing Issues
========================

Random loss of connection to MySQL
----------------------------------

Symptoms
~~~~~~~~

During Heat stacks (representing slices) creation some of the stacks are
moved to ERROR state with the following traceback being found in the
Heat logs::

    2016-12-11 16:59:22.220 1165 ERROR nova.api.openstack.extensions
    DBConnectionError: (pymysql.err.OperationalError) (2003, "Can't
    connect to MySQL server on 'galera.ccp.svc.cluster.local' ([Errno
    -2] Name or service not known)")

Root cause
~~~~~~~~~~

This turned out to be exactly the same issue with KubeDNS being unable
to handle high loads as described in Kubernetes Issues section above.

First of all, ``kubedns`` seems to fail often on high load (or even without
load), during the experiment we observed continuous kubedns container
restarts even on empty (but big enough) Kubernetes cluster. Restarts
are caused by liveness check failing, although nothing notable is
observed in any logs.

Second, ``dnsmasq`` should have taken load off ``kubedns``, but it needs some
tuning to behave as expected for big load, otherwise it is useless.

Solution
~~~~~~~~

See above in Kubernetes Issues section.

Slow Heat API requests (`Bug 1653088 <https://bugs.launchpad.net/fuel-ccp/+bug/1653088>`__)
-----------------------------------------------------------------------------------------

Symptoms
~~~~~~~~

Requests to the Heat API for regular requests took more than a minute of
time. Example of such request can be presented with `this
traceback <http://paste.openstack.org/show/593132/>`__ showing time
needed for listing details of the specific stack

Root cause
~~~~~~~~~~

Fuel-ccp team proposed that it might be a hidden race condition between
multiple Heat workers, and it's not yet clear where is this race
happening. This is still under debug

Workaround
~~~~~~~~~~

Set up number of Heat workers to 1 until real cause of this issue will
be found.

OpenStack VMs cannot fetch required metadata
--------------------------------------------

Symptoms
~~~~~~~~

OpenStack servers do not receive metadata with applications-specific
information. There is a following
`trace <http://paste.openstack.org/show/593337/>`__ in Heat logs.

Root cause
~~~~~~~~~~

Prior pushing metadata to OpenStack VMs, Heat is storing information
about stack under creation to its own database. Starting with OpenStack
Newton Heat works in so-called “convergence” mode by default, making
sure that Heat engine process several requests at one time. This
parallel task processing might end up with race conditions during DB
access.

Workaround
~~~~~~~~~~

Turn off Heat convergence engine::

    convergence_engine=False

RPC timeouts during Heat resources validation
---------------------------------------------

Symptoms
~~~~~~~~

During Heat resources validation, this process is failed with the
following `trace <http://paste.openstack.org/show/593112/>`__ being
caught.

Root cause
~~~~~~~~~~

Initial assumption was that there might be too small
``rpc_response_timeout`` parameter being set up in Heat configuration
file. This parameter was set up to 10 minutes exactly like that was used
in MOS::

    rpc_response_timeout = 600

After that was done, no more RPC timeouts were observed.

Solution
~~~~~~~~

Set up ``rpc_response_timeout = 600`` as that’s tested value for
generations of MOS releases.

Overloaded Memcache service (`Bug 1653089 <https://bugs.launchpad.net/fuel-ccp/+bug/1653089>`__)
----------------------------------------------------------------------------------------------

Symptoms
~~~~~~~~

On 200 nodes with workloads deploying OpenStack is actively using cache
(``memcached``). At some point of time requests to ``memcached`` begin to be
processed really slow.

Root cause
~~~~~~~~~~

Memcache size is 256 MB by default in Fuel CCP, which is really small
size. That was a reason for great amount of retransmissions being
processed.

Solution
~~~~~~~~

Increase cache size up to 30G in ``fuel-ccp`` configuration file for huge or
loaded deployments::

    configs:
        memcached:
            address: 0.0.0.0
            port:
            cont: 11211
            ram: 30720

Incorrect status information for Neutron agents
-----------------------------------------------

Symptoms
~~~~~~~~

While asking for Neutron agents status through OpenStack client, all of
them are displayed in down state, although due to the environment
behaviour it does not seem to be true.

Root cause
~~~~~~~~~~

The root cause of this issue is hidden in OpenStackSDK refactoring that
caused various OSC networking commands to fail. The full discussion
regarding this issue can be found in `upstream
bug <https://bugs.launchpad.net/python-openstackclient/+bug/1652317>`__.

Workaround
~~~~~~~~~~

Use Neutron client directly to gather Neutron services statuses until
`bug <https://bugs.launchpad.net/python-openstackclient/+bug/1652317>`__
will be fixed.

Nova client not working (`Bug 1653075 <https://bugs.launchpad.net/fuel-ccp/+bug/1653075>`__)
------------------------------------------------------------------------------------------

Symptoms
~~~~~~~~

All commands running through Nova client end up with the `stack
trace <http://paste.openstack.org/show/593531/>`__.

Root cause
~~~~~~~~~~

In debug mode it’s seen that client tries to use HTTP protocol for the
Nova requests, e.g. http://compute.ccp.external:8443/v2.1/, although
HTTPS protocol is required for this client-server conversation.

Solution
~~~~~~~~

Add the following lines to
``ccp-repos/fuel-ccp-nova/service/files/nova.conf.j2`` file::

    [DEFAULT]

    secure_proxy_ssl_header = HTTP_X_FORWARDED_PROTO

Neutron server timeouts (`Bug 1653077 <https://bugs.launchpad.net/fuel-ccp/+bug/1653077>`__)
------------------------------------------------------------------------------------------

Symptoms
~~~~~~~~

Neutron server is not able to process requests to it with the following
error being caught in the Neutron logs:
`trace <http://paste.openstack.org/show/593483/>`__

Root cause
~~~~~~~~~~

Default values (that are used in ``fuel-ccp``) for the Neutron database pool
size, as well as max overflow parameter are not enough for the
environment with big enough load on Neutron API.

Solution
~~~~~~~~

Modify ``ccp-repos/fuel-ccp-neutron/service/files/neutron.conf.j2`` file to
contain the following configuration parameters::

    [database]

    max_pool_size = 30

    max_overflow = 60

No access to OpenStack VM from tenant network
---------------------------------------------

Symptoms
~~~~~~~~

Some of the VMs representing the slices are not reachable via tenant
network. For example::

    | 93b95c73-f849-4ffb-9108-63cf262d3a9f | cassandra_vm_0 |
    ACTIVE | slice0-node162-net=11.62.0.8, 10.144.1.35 |
    ubuntu-software-config-last |

    root@node1:~# ssh -i .ssh/slace ubuntu@10.144.1.35
    Connection closed by 10.144.1.35 port 22

It is unreachable from tenant network as well. For example from instance
``b1946719-b401-447d-8103-cc43b03b1481`` which has been spawned by the same
Heat stack on the same compute node (``node162``):
`http://paste.openstack.org/show/593486/ <http://paste.openstack.org/show/593486/>`__

Root cause and solution
~~~~~~~~~~~~~~~~~~~~~~~

Still under investigation. Root cause not clear yet. **This issue is blocking
running workloads against deployed slices.**

OpenStack services don’t handle PXC pseudo-deadlocks
----------------------------------------------------

Symptoms
~~~~~~~~

When run in parallel, create operations of lots of resources were
failing with DBError saying that Percona Xtradb Cluster identified a
deadlock and transaction should be restarted.

Root cause
~~~~~~~~~~

oslo.db is responsible for wrapping errors received from DB into proper
classes so that services can restart transactions if similar errors
occur, but it didn’t expect error in format that is being sent by
Percona. After we fixed this, we still experienced similar errors
because not all transactions that could be restarted were properly
decorated in Nova code.

Upstream issues
~~~~~~~~~~~~~~~

`Bug <https://bugs.launchpad.net/oslo.db/+bug/1648818>`__ has been
fixed by Roman Podolyaka’s
`CR <https://review.openstack.org/409194>`__ and
`backported <https://review.openstack.org/409679>`__ to Newton. It
fixes Percona deadlock error detection, but there’s at least one place
in Nova to be fixed (TBD)

Live migration failed with live_migration_uri configuration
-------------------------------------------------------------

Symptoms
~~~~~~~~

With ``live_migration_uri`` configuration, live migrations fails because
one compute host can’t connect to a libvirt on another host.

Root cause
~~~~~~~~~~

We can’t specify which IP address to use in template in
``live_migration_uri``, so it was trying to use address from first
interface which happened to be in PXE network while libvirt listens in
private network. We couldn’t use ``live_migration_inbound_addr`` which
would solve this problem because of a problem in upstream Nova.

Upstream issues
~~~~~~~~~~~~~~~

A `bug <https://bugs.launchpad.net/nova/+bug/1638625>`__ in Nova has
been `fixed <https://review.openstack.org/398956>`__ and
`backported <https://review.openstack.org/404810>`__ to Newton. We
`switched <https://review.openstack.org/407708>`__ to using
``live_migration_inbound_addr`` after that.

Contributors
============

The following people have credits for contributing to this
document:

* Dina Belova <dbelova@mirantis.com>

* Yuriy Taraday <ytaraday@mirantis.com>
