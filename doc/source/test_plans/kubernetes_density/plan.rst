.. _Kubernetes_density_test_plan:

**************************
Kubernetes density testing
**************************

:status: **ready**
:version: 1.0

:Abstract:

  This test plan covers scenarios of density testing of Kubernetes

Test Plan
=========

Test Environment
----------------

Preparation
^^^^^^^^^^^

The test plan is executed against Kubernetes deployed on bare-metal nodes.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers,
network parameters, operation system and OpenStack deployment characteristics.


Test Case #1: Maximum pods per node
-----------------------------------

Description
^^^^^^^^^^^
Kubernetes by default limits number of pods running by the node. The value is
chosen by community and since version 1.4 equals to 110 (k8s_max_pods_).

The goal of this test is to investigate system behavior at default limit and
find out whether it can be increased or not. In particular we are interested
in the following metrics: pod startup time during mass start (e.g. when
replication controller is scaled up) and node's average load.

From manual experiments it is observed that pod starts functioning before
Kubernetes API reports it to be in running state. In this test case we are
interested to investigate how long does it takes for Kubernetes to update
pod status.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +-------------------------+---------------------------------------------+
  | Parameter               | Description                                 |
  +=========================+=============================================+
  | POD_COUNT               | Number of pods                              |
  +-------------------------+---------------------------------------------+
  | POD_FIRST_REPORT        | Time taken by pod to start and report       |
  +-------------------------+---------------------------------------------+
  | KUBECTL_RUN             | Time for all pods to be reported as running |
  +-------------------------+---------------------------------------------+
  | KUBECTL_TERMINATE       | Time to terminate all pods                  |
  +-------------------------+---------------------------------------------+


Reports
=======

Test plan execution reports:
 * :ref:`Kubernetes_density_test_report`


.. references:

.. _k8s_max_pods: https://github.com/kubernetes/kubernetes/blob/v1.5.0/pkg/apis/componentconfig/v1alpha1/defaults.go#L290