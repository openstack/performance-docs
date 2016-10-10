.. _neutron_agent_restart_test_report:

=========================================================================
OpenStack Neutron Control Plane Performance and Agent Restart Test Report
=========================================================================

This report is generated for :ref:`neutron_agent_restart_test_plan`.

Environment description
=======================

Cluster description
-------------------
* 3 controllers
* 3 compute nodes

Software versions
-----------------

**OpenStack/System**:
  Fuel/MOS 9.0, Ubuntu 14.04, Linux kernel 3.13, OVS 2.4.1
**Networking**
  Neutron ML2 + OVS plugin, DVR, L2pop, MTU 1500

Hardware configuration of each server
-------------------------------------

Description of servers hardware

**Compute Vendor**:
    HP ProLiant DL380 Gen9,
**CPU**
    2 x Intel(R) Xeon(R) CPU E5-2680 v3 @2.50GHz (48 cores)
**RAM**:
    256 Gb
**NIC**
    2 x Intel Corporation Ethernet 10G 2P X710


Reports
=======

Reports are collected on OpenStack with 100 instances, 100 routers,
100 networks.

.. toctree::
    :glob:
    :maxdepth: 1

    */index
