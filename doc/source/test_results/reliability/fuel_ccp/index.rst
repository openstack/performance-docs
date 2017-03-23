.. _reliability_test_results_version_2_containerized:

===========================================
Containerized OpenStack reliability testing
===========================================

Test results
============

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

This report contains results for :ref:`reliability_testing_version_2`
test plan. The data is collected in :ref:`intel_mirantis_performance_lab_1`.


Software
~~~~~~~~

This section describes installed software.

+-----------------+--------------------------------------------+
| Parameter       | Value                                      |
+-----------------+--------------------------------------------+
| OS              | Ubuntu 16.04.2                             |
+-----------------+--------------------------------------------+
| Docker          | 1.13                                       |
+-----------------+--------------------------------------------+
| Kubernetes      | 1.5.3                                      |
+-----------------+--------------------------------------------+
| OpenStack       | Fuel-CCP (Newton)                          |
+-----------------+--------------------------------------------+
| Networking      | Neutron OVS ML2 plugin with VxLAN, non-DVR |
+-----------------+--------------------------------------------+

Configs
~~~~~~~

    * Fuel-CCP: :download:`configs/configs.yaml`,
      :download:`configs/topology.yaml`, :download:`configs/repos.yaml`,
      :download:`configs/versions.yaml`
    * Rally: :download:`configs/deployment.yaml`
    * OS-Faults: :download:`configs/os-faults.yaml`

Reports
^^^^^^^

.. toctree::
    :maxdepth: 1
    :glob:

    reports/*/*/index

Reports are calculated on :download:`Raw Rally data <raw/raw_data.tar.xz>`
