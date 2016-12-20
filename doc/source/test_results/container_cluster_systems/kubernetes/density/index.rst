.. _Kubernetes_density_test_report:

******************************
Kubernetes density test report
******************************

:Abstract:

  This document is the report for :ref:`Kubernetes_density_test_plan`


Environment description
=======================

This report is collected on the hardware described in
:ref:`intel_mirantis_performance_lab_1`.


Software
~~~~~~~~

Kubernetes is installed using :ref:`Kargo` deployment tool on Ubuntu 16.04.1.

Node roles:
 - node1: minion+master+etcd
 - node2: minion+master+etcd
 - node3: minion+etcd
 - node4: minion

Software versions:
 - OS: Ubuntu 16.04.1 LTS (Xenial Xerus)
 - Kernel: 4.4.0-47
 - Docker: 1.12.1
 - Kubernetes: 1.4.3

Reports
=======

Test Case #1: Maximum pods per node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pod startup time is measured with help of
`MMM(MySQL/Master/Minions) testing suite`_. To schedule all pods on a single
node the original replication controller for minions is updated with scheduler
hint. To do this add the following lines into template's spec section:

.. code-block:: yaml

      nodeSelector:
        kubernetes.io/hostname: node4

Pod status from Kubernetes point of view is retrieved from kubectl tool.
The process is automated with
:download:`kubectl_mon.py <kubectl-mon/kubectl_mon.py>`, which produces
output in CSV format. Charts are created by
:download:`pod_stats.py <kubectl-mon/pod_stats.py>` script.

Every measurement starts with empty namespace. Then Kubernetes replication
controller is created with specified number of pods. We collect pod's report
time and kubectl stats. The summary data is presented below.

.. image:: summary.png

.. list-table:: POD stats
    :header-rows: 1

    *
      - POD_COUNT
      - POD_FIRST_REPORT, s
      - KUBECTL_RUN, s
      - KUBECTL_TERMINATE, s
    *
      - 50
      - 12
      - 44
      - 30
    *
      - 100
      - 27
      - 131
      - 87
    *
      - 200
      - 61
      - 450
      - 153
    *
      - 400
      - 208
      - ∞ (not finished)
      - 390



Detailed Stats
--------------

50 pods
^^^^^^^

Start replication controller with 50 pods

.. image:: 50-start.svg
    :width: 100%

Terminate replication controller with 50 pods

.. image:: 50-term.svg
    :width: 100%

100 pods
^^^^^^^^

Start replication controller with 100 pods

.. image:: 100-start.svg
    :width: 100%

Terminate replication controller with 100 pods

.. image:: 100-term.svg
    :width: 100%

200 pods
^^^^^^^^

Start replication controller with 200 pods

.. image:: 200-start.svg
    :width: 100%

Terminate replication controller with 200 pods

.. image:: 200-term.svg
    :width: 100%

400 pods
^^^^^^^^

Start replication controller with 400 pods.

Note: In this experiment all pods successfully reported, however from Kubernetes API
point of view less than 60 pods were in running state. The number of pods
reported as running was slowly increasing over the time, but the speed was very
low to treat the process as succeed.

.. image:: 400-start.svg
    :width: 100%

Terminate replication controller with 400 pods.

.. image:: 400-term.svg
    :width: 100%

Scale by 100 pods steps
^^^^^^^^^^^^^^^^^^^^^^^

In this experiment we scale replication controller up by steps of 100 pods.
Scaling process is invoked after all pods are reported as running. On step 3
(201-300 pods) the process has become significantly slower and we've started
scaling replication controller down. The full cycle is visualized below.

.. image:: N-start-term.svg
    :width: 100%

System metrics from API nodes and minion are below

.. image:: N-cpu-user.png

.. image:: N-cpu-system.png

.. image:: N-mem-used.png

.. image:: N-disk-io.png

Full `Kubernetes stats`_ are available online.


.. references:

.. _Kargo: https://github.com/kubespray/kargo
.. _MMM(MySQL/Master/Minions) testing suite: https://github.com/AleksandrNull/MMM
.. _Kubernetes stats: https://snapshot.raintank.io/dashboard/snapshot/YCtAh7jHhYpmWk8nsfda0EAIRRnG4TV9