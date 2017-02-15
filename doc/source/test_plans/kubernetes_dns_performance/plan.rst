.. _Kubernetes_dns_performance_test_plan:

************************************
Kubernetes DNS performance test plan
************************************

:status: **ready**
:version: 1.0

:Abstract:

  This test plan covers scenarios for Kubernetes DNS performance testing.

Test Plan
=========

Kubernetes DNS schedules a DNS Pod and Service on the cluster, and configures
the kubelets to tell individual containers to use the DNS Service's IP to
resolve DNS names.

"Normal" (not headless) Services are assigned a DNS A record for a name of
the form ``my-svc.my-namespace.svc.cluster.local``. This resolves to the
cluster IP of the Service.

Under DNS performance we mean the amount of work produced by a service,
for DNS service this can be measured as number of requests for resolving host
per second.

Test Environment
----------------

Preparation
^^^^^^^^^^^

The test plan is executed against Kubernetes deployed on bare-metal nodes.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers,
network parameters, operation system and OpenStack deployment characteristics.


Test Case #1: Performing DNS queries
------------------------------------

Description
^^^^^^^^^^^

In this test case we investigate how number of queries affects Kubernetes
DNS performance.

Script :download:`code/test_kubedns.py` will create Kubernetes services based
on file :download:`code/template.yaml`. After that, will make request to this
services by host name. Results will show number of failed hosts.

Parameters
^^^^^^^^^^

**Case group 1:**

.. table:

+----------------------+------------------------+
| Parameter name       | Value                  |
+======================+========================+
| number of replicas   | 1, 2, 3                |
+----------------------+------------------------+
| requests per second  | 50, 100, ..., 1000     |
+----------------------+------------------------+
| number of Services   | 1000                   |
+----------------------+------------------------+
| number of attempts   | 1000                   |
+----------------------+------------------------+

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +-------------------------+-----------------------------------------------+
  | Parameter               | Description                                   |
  +=========================+===============================================+
  | FAILED_HOSTS            | Number of hosts, which not be resolved by DNS |
  +-------------------------+-----------------------------------------------+
  | SUCCESS_RATE            | Percentage of successful queries              |
  +-------------------------+-----------------------------------------------+

Reports
=======

Test plan execution reports:
 * :ref:`Kubernetes_dns_performance_test_report`
