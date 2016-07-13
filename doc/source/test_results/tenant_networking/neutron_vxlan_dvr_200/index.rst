.. raw:: pdf

    PageBreak oneColumn

.. _mq_ha_rabbit_report:

===================================================
Tenant Networking: Neutron DVR + VXLAN at 200 nodes
===================================================

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

This report is generated for :ref:`openstack_tenant_networking_test_plan`
test plan with `Shaker`_ tool. The data is collected in
:ref:`intel_mirantis_performance_lab`.


Software
~~~~~~~~

This section describes installed software.

+-----------------+--------------------------------------------+
| Parameter       | Value                                      |
+-----------------+--------------------------------------------+
| OS              | Ubuntu 14.04.3                             |
+-----------------+--------------------------------------------+
| OpenStack       | Mitaka                                     |
+-----------------+--------------------------------------------+
| Networking      | Neutron OVS ML2 plugin with VxLAN and DVR  |
+-----------------+--------------------------------------------+


Reports
^^^^^^^

.. toctree::
    :maxdepth: 2

    perf_l2_dense/index
    perf_l2/index
    full_l2/index
    perf_l3_east_west_dense/index
    perf_l3_east_west/index
    full_l3_east_west/index
    perf_l3_north_south/index
    full_l3_north_south/index

.. _Shaker: http://pyshaker.readthedocs.org/en/latest/index.html
