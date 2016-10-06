.. raw:: pdf

    PageBreak oneColumn

.. _tenant_networking_report_vxlan_dvr_378_nodes:

===================================================
Tenant Networking: Neutron DVR + VXLAN at 378 nodes
===================================================

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

This report is generated for :ref:`openstack_tenant_networking_test_plan`
test plan with `Shaker`_ tool. The data is collected in
:ref:`intel_mirantis_performance_lab`.


Software
~~~~~~~~

This section describes installed software.

+---------------+-------------------------------------------------------------+
| Parameter     | Value                                                       |
+---------------+-------------------------------------------------------------+
| OS            | Ubuntu 14.04.3                                              |
+---------------+-------------------------------------------------------------+
| OpenStack     | Mitaka                                                      |
+---------------+-------------------------------------------------------------+
| Networking    | Neutron OVS ML2 plugin, VxLAN, DVR, L2pop, MTU 9000         |
+---------------+-------------------------------------------------------------+
| HW offloading | Tx, Rx checksumming, TSO, GSO, GRO, tx-udp_tnl-segmentation |
+---------------+-------------------------------------------------------------+


Reports
^^^^^^^

.. toctree::
    :maxdepth: 2
    :glob:

    */index

.. _Shaker: http://pyshaker.readthedocs.io/
