.. _Kubernetes_proxy_performance_test_plan:

**************************************
Kubernetes proxy performance test plan
**************************************

:status: **ready**
:version: 1.0

:Abstract:

  This test plan covers scenarios for Kubernetes proxy performance testing.

Test Plan
=========

Kube-proxy(starting with k8s version 1.4) by default works in 'iptables' mode
and does not proxy the traffic. Old 'userspace' mode is left for backward
compatibility only. There is opinion, that even most recent version of
kube-proxy is not as effective, as it can be due ip-tables mode has its own
disadvantages and possible lack of performance. We want to check it.

Test Environment
----------------

Preparation
^^^^^^^^^^^

The test plan is executed against Kubernetes deployed on bare-metal nodes.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers,
network parameters, operation system and OpenStack deployment characteristics.


Test Case #1: Performing kube-proxy
-----------------------------------

Description
^^^^^^^^^^^

In this test case we investigate how number of services affects Kubernetes
proxy performance.

Script :download:`code/kubeproxy/test_kubeproxy.py` will create Kubernetes
services based on file :download:`code/kubeproxy/service.yaml`. After that,
will make request to this services using Locust_ (
:download:`code/locustfile.py`). Results will show response time.

Parameters
^^^^^^^^^^

**Case group 1:**

.. table:

+----------------------+------------------------+
| Parameter name       | Value                  |
+======================+========================+
| number of Services   | 100, 200, ..., 1400    |
+----------------------+------------------------+

**Case group 2:**

.. table:

+----------------------+------------------------+
| Parameter name       | Value                  |
+======================+========================+
| number of Services   | 10, 50                 |
+----------------------+------------------------+
| number of Pods       | 1, 3, 5                |
+----------------------+------------------------+

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +-------------------------+-----------------------------------------------+
  | Parameter               | Description                                   |
  +=========================+===============================================+
  | MIN_RESPONSE            | time in ms                                    |
  +-------------------------+-----------------------------------------------+
  | MAX_RESPONSE            | time in ms                                    |
  +-------------------------+-----------------------------------------------+
  | AVERAGE_RESPONSE        | time in ms                                    |
  +-------------------------+-----------------------------------------------+

Reports
=======

Test plan execution reports:
 * :ref:`Kubernetes_proxy_performance_test_report`


.. references:

.. _Locust: http://locust.io/