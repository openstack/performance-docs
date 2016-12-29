.. _Kubernetes_pod_recovery_test_plan:

*********************************
Kubernetes POD recovery test plan
*********************************

:status: **ready**
:version: 1.0

:Abstract:

  This test plan covers scenarios for Kuberneter POD recovery testing.

Test Plan
=========

In Kubernetes "classic" HTTP-based services can be represented with help of
replication controller and service. Replication controller is responsible
for keeping number of PODs constant and in restarts POD in case of failure.
If the POD is deleted, then replication controller creates a new one.
Depending on scheduler settings a new instance of POD can be scheduled
to a different node.

Under service performance we mean the amount of work produced by a service,
for HTTP service this can be measured as number of requests per second.

Test Environment
----------------

Preparation
^^^^^^^^^^^

The test plan is executed against Kubernetes deployed on bare-metal nodes.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The environment description includes hardware specification of servers,
network parameters, operation system and OpenStack deployment characteristics.


Test Case #1: POD restart
-------------------------

Description
^^^^^^^^^^^

In this test case we investigate how POD rescheduling affects service
performance.

Steps:
 * Build Docker image and push it into local registry:
   ``docker build -t localhost:31500/qa/svc code/``
   ``docker push localhost:31500/qa/svc
 * Create Kubernetes Service and Deployments based on files
   :download:`code/svc-dpl.yaml` and :download:`code/svc-svc.yaml`
 * Measure service performance during 20 seconds:
   ``wrk -c 20 -d 10 -t 20 -H "Connection: close" --latency --timeout 10s http://svc.ccp:8000/``
 * While measurement is running delete the pod via
   ``kubectl delete pod -l app=svc``

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: list of test metrics to be collected during this test

  +-------------------------+---------------------------------------------+
  | Parameter               | Description                                 |
  +=========================+=============================================+
  | RPS_BASE                | Base RPS value                              |
  +-------------------------+---------------------------------------------+
  | RPS_WHILE_RESCHEDULING  | RPS measured during rescheduling            |
  +-------------------------+---------------------------------------------+


Reports
=======

Test plan execution reports:
 * :ref:`Kubernetes_pod_recovery_test_report`
