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

Contributors
============

The following people have credits for contributing to this
document:

* Dina Belova <dbelova@mirantis.com>

* Yuriy Taraday <ytaraday@mirantis.com>
