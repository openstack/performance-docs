.. _Measuring_performance_of_cinder_with_ceph_backend:

=================================================
Measuring performance of Cinder with Ceph backend
=================================================

:status: **ready**
:version: 1.0

:Abstract:

  This document describes a test plan for quantifying the performance of
  block storage devices provided by OpenStack Cinder with Ceph used as back-end.
  The plan includes the collection of several resource utilization metrics,
  which will be used to analyze and understand the overall performance of used
  storage technologies. In particular, resource bottlenecks will either be
  fixed, or best practices developed for system and hardware requirements.

:Conventions:

  - **Kubernetes:** is an open-source system for automating deployment, scaling,
    and management of containerized applications.

  - **Calico:** is a new approach to virtual networking and network security for
    containers, VMs, and bare metal services, that provides a rich set of
    security enforcement capabilities running on top of a highly scalable and
    efficient virtual network fabric. Calico includes pre-integration with
    Kubernetes and Mesos (as a CNI network plugin), Docker (as a libnetwork
    plugin) and OpenStack (as a Neutron plugin).

  - **fuel-ccp:** CCP stands for "Containerized Control Plane". The goal of this
    project is to make building, running and managing production-ready OpenStack
    containers on top of Kubernetes an easy task for operators.

  - **OpenStack:**  OpenStack is a cloud operating system that controls large
    pools of compute, storage, and networking resources throughout a datacenter,
    all managed through a dashboard that gives administrators control while
    empowering their users to provision resources through a web interface.

  - **Cinder:** The Block Storage service provides block storage devices to
    guest instances. The method in which the storage is provisioned and consumed
    is determined by the Block Storage driver, or drivers in the case of a
    multi-backend configuration. There are a variety of drivers that are
    available: NAS/SAN, NFS, iSCSI, Ceph, and more.

  - **Heat:** Heat is a service to orchestrate composite cloud applications
    using a declarative template format through an OpenStack-native REST API.

  - **Ceph:** Ceph is a massively scalable, open source, distributed storage
    system. It is comprised of an object store, block store, and a
    POSIX-compliant distributed file system. The platform can auto-scale to the
    exabyte level and beyond. It runs on commodity hardware, is self-healing and
    self-managing, and has no single point of failure. Ceph is in the Linux
    kernel and is integrated with the OpenStack cloud operating system.

  - **Nodes:** are servers used for workloads.

  - **IOPS:** Input/output operations per second is a performance measurement
    used to characterize computer storage devices like hard disk drives (HDD),
    solid state drives (SSD), and storage area networks (SAN).

  - **Completion latency:** This is the time that passes between submission to
    the kernel and when the IO is complete, not including submission latency.

Test Plan
=========

This test plan aims to identify Cinder + Ceph storage performance and its
dependency from amount of concurrent attached consumers.

Test Environment
----------------

Preparation
^^^^^^^^^^^

1.
  To be able to run test we need:

  - Ceph cluster installed and configured

  - K8s cluster installed and configured with Calico

  - OpenStack cloud with Heat and Cinder installed on top of K8s cluster

  - Created and uploaded into Glance image with random data which will be used
  for prefilling of Cinder volumes

.. table:: Software to be installed

  +-----------------+------------+------------------------------------------+
  | software        | version    | source                                   |
  +=================+============+==========================================+
  | `Ceph`_         | jewell     | Debian jessie ceph package repository    |
  +-----------------+------------+------------------------------------------+
  | `Kargo`_        | master     | From sources                             |
  +-----------------+------------+------------------------------------------+
  | `Kubernetes`_   | 1.4.3      | quay.io/coreos/hyperkube:v1.4.3_coreos.0 |
  +-----------------+------------+------------------------------------------+
  | `Calico`_       | 0.22.0     | docker hub                               |
  +-----------------+------------+------------------------------------------+
  | `calicoctl`_    | 1.0.0-beta | docker hub                               |
  +-----------------+------------+------------------------------------------+
  | `OpenStack`_    | newton     | From sources                             |
  +-----------------+------------+------------------------------------------+


Environment description
^^^^^^^^^^^^^^^^^^^^^^^

Test results MUST include a description of the environment used. The following
items should be included:

- **Hardware configuration of each server.** If virtual machines are used then
  both physical and virtual hardware should be fully documented.
  An example format is given below:

**Ceph cluster member:**

.. table:: Description of server hardware

  +-------+----------------+-------+-------+
  |server |name            |       |       |
  |       +----------------+-------+-------+
  |       |role            |       |       |
  |       +----------------+-------+-------+
  |       |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |operating_system|       |       |
  +-------+----------------+-------+-------+
  |CPU    |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |processor_count |       |       |
  |       +----------------+-------+-------+
  |       |core_count      |       |       |
  |       +----------------+-------+-------+
  |       |frequency_MHz   |       |       |
  +-------+----------------+-------+-------+
  |RAM    |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |amount_MB       |       |       |
  +-------+----------------+-------+-------+
  |NETWORK|interface_name  |       |       |
  |       +----------------+-------+-------+
  |       |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |bandwidth       |       |       |
  +-------+----------------+-------+-------+
  |STORAGE|dev_name        |       |       |
  |       +----------------+-------+-------+
  |       |vendor,model    |       |       |
  |       +----------------+-------+-------+
  |       |SSD/HDD         |       |       |
  |       +----------------+-------+-------+
  |       |size            |       |       |
  +-------+----------------+-------+-------+

- **Configuration of physical network.** The description of phisical and logical
  connectivities.

- **Configuration of virtual machines and virtual networks (if used).**
  The configuration files can be attached, along with the mapping of virtual
  machines to host machines.

- **Ceph cluster configuration** Deployment scheme and configuration of
  ceph components.

 #) ceph nodes configuration and roles

 #) amount of ceph monitor nodes

 #) amount of ceph OSD and placement groups

- **Kubernetes + Calico configuration** Deployment scheme and configuration of
  servers used within testing environment.

 #) k8s nodes configuration and roles

 #) k8s networking configuration (Calico)

- **OpenStack deployment configuration used by fuel-ccp.**
  OpenStack services configuration and topology used by fuel-ccp.

 #) OpenStack services and roles topology

 #) OpenStack cinder + ceph configuration

Test Cases
----------

- Case group 1 - average time of creation, attachment and deletion of Cinder
  volumes
- Case group 2 - amount of concurrent read, write and simultaneous read, write
  IOPS depending on amount of VMs

Description
^^^^^^^^^^^

This specific test plan contains test cases, that needs to be run
on the environments differing list of parameters below. Here we have 2 kinds of
metrics to be measured.

- OpenStack control plane side tests of Cinder with Ceph back-end like
  execution time for basic functionality of cinder.

- Load tests of VM storage subsystem provided by Cinder with Ceph back-end.
  This tests will show dependency of IOPS from amount of consumers and disk
  operations types.

Parameters
^^^^^^^^^^

Parameters depend on ceph and OpenStack configurations.

**Case group 1:**

.. table:

+------------------+------------------------+
| Parameter name   | Value                  |
+==================+========================+
| vms + volumes    | 30, 60, 90             |
+------------------+------------------------+
| concurrency      | 10, 20, 30             |
+------------------+------------------------+
| operation        | create, attach, delete |
+------------------+------------------------+


**Case group 2:**

.. table:

+------------------+---------------------+
| Parameter name   | Value               |
+==================+=====================+
| VMs per rw mode  | 1, 2, 5, 10, 20     |
+------------------+---------------------+
| read/write mode  | randread, randwrite |
+------------------+---------------------+
| block size       | 4k - constant       |
+------------------+---------------------+
| io depth (queue) | 64                  |
+------------------+---------------------+
| test duration in | 600                 |
| seconds          |                     |
+------------------+---------------------+
| filesize         | 40G                 |
+------------------+---------------------+


List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The tables below show the list of test metrics to be collected. The priority
is the relative ranking of the importance of each metric in evaluating the
performance of the system.


**Case group 1:**

.. table:: List of performance metrics for cinder functionality

  +-------------------+-------------------+------------------------------------------+
  | Value             | Measurement Units | Description                              |
  +===================+===================+==========================================+
  | Time              | seconds           || time spent on requested operation       |
  +-------------------+-------------------+------------------------------------------+

**Case group 2:**

.. table:: List of performance metrics for storage subsystem

  +-------------------+-------------------+------------------------------------------+
  | Value             | Measurement Units | Description                              |
  +===================+===================+==========================================+
  |                   |                   || amount of input/output operations per   |
  | READ_IO           | operations/second || second during random read from storage  |
  |                   |                   || subsystem                               |
  |                   |                   ||                                         |
  +-------------------+-------------------+------------------------------------------+
  |                   |                   || amount of input/output operations per   |
  | WRITE_IO          | operations/second || second during random read from storage  |
  |                   |                   || subsystem                               |
  |                   |                   ||                                         |
  +-------------------+-------------------+------------------------------------------+
  |                   |                   || time that passes between submission to  |
  | READ_LATENCY      | milliseconds      || the kernel and when the IO is complete  |
  |                   |                   ||                                         |
  |                   |                   ||                                         |
  +-------------------+-------------------+------------------------------------------+
  |                   |                   || time that passes between submission to  |
  | WRITE_LATENCY     | milliseconds      || the kernel and when the IO is complete  |
  |                   |                   ||                                         |
  |                   |                   ||                                         |
  +-------------------+-------------------+------------------------------------------+
  |                   |                   || amount of simultaneously launched VMs   |
  | VMs_COUNT         | number            || with attached cinder volumes producing  |
  |                   |                   || storage loads                           |
  |                   |                   ||                                         |
  +-------------------+-------------------+------------------------------------------+

Measuring performance values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Case group 1:**

"Control plane" test will be executed using OpenStack `Rally`_ scenarios.

.. table:: Maximum values of performance metrics from Rally

  +----------------------+-----------+--------------+--------------+--------------+-----------+-----------+---------+-------+
  | Action               | Min (sec) | Median (sec) | 90%ile (sec) | 95%ile (sec) | Max (sec) | Avg (sec) | Success | Count |
  +----------------------+-----------+--------------+--------------+--------------+-----------+-----------+---------+-------+
  |                      |           |              |              |              |           |           |         |       |
  +----------------------+-----------+--------------+--------------+--------------+-----------+-----------+---------+-------+

Where:

- operation will be one of create, attach or delete
- volume size is also matters and all operations mentioned above
  will be repeated for each groups of volumes

**Case group 2:**

Storage performance testing will be based on test scripts which will be
delivered and launched inside VMs using OpenStack Heat templates.

`Heat templates`_ could be laucnhed with different set of paramteters. These
parameters are serving for 2 porpuses:

- 1.Parameters for OpenStack environment:

  #) *key_name* - SSH key name that will be injected into instances

  #) *flavor* - flavor to be used for instances

  #) *image* - image to be used for instances

  #) *network_name* - internal network to be used for instances

  #) *volume_size* - volume size to be created and attached to instance

  #) *vm_count* - amount of VMs with volumes to be spawned

- 2.Parameters for test script:

  #) *test_mode* - condition of test (time or disk)

  #) *test_rw* - read or write mode (randread, randwrite, randrw)

  #) *test_runtime* - amount of time in seconds (default 600)

  #) *test_filesize* - amount of data size (default 4G)

  #) *test_iodepth* - IO queue size generated by test (default 64)

.. table:: Average values of performance metrics from cinder + ceph

  +-------+----------------+----------+----------+---------+-----------+
  || nodes|| test duration || average || average || average|| average  |
  || count|| time in sec   || IOPS    || IOPS    || latency|| latency  |
  ||      ||               || READ    || WRITE   || READ   || WRITE    |
  +=======+================+==========+==========+=========+===========+
  | 2     |                |          |          |         |           |
  +-------+----------------+----------+----------+---------+-----------+
  | 4     |                |          |          |         |           |
  +-------+----------------+----------+----------+---------+-----------+
  | 10    |                |          |          |         |           |
  +-------+----------------+----------+----------+---------+-----------+
  | 20    |                |          |          |         |           |
  +-------+----------------+----------+----------+---------+-----------+
  | 40    |                |          |          |         |           |
  +-------+----------------+----------+----------+---------+-----------+

.. table:: Summary values of performance metrics from cinder + ceph

  +-------+----------------+----------+----------+
  || nodes|| test duration || SUM     || SUM     |
  || count|| time in sec   || IOPS    || IOPS    |
  ||      ||               || READ    || WRITE   |
  +=======+================+==========+==========+
  | 2     |                |          |          |
  +-------+----------------+----------+----------+
  | 4     |                |          |          |
  +-------+----------------+----------+----------+
  | 10    |                |          |          |
  +-------+----------------+----------+----------+
  | 20    |                |          |          |
  +-------+----------------+----------+----------+
  | 40    |                |          |          |
  +-------+----------------+----------+----------+

Applications
============

Rally jobs templates:
--------------------
.. literalinclude:: rally/cinder30.yaml
  :language: yaml

.. literalinclude:: rally/cinder60.yaml
  :language: yaml

.. literalinclude:: rally/cinder120.yaml
  :language: yaml

Heat templates
--------------
.. literalinclude:: heat/main.yaml
  :language: yaml

.. literalinclude:: heat/vm-with-vol.yaml
  :language: yaml

Test script for heat
--------------------

.. literalinclude:: heat/vmScript.sh
    :language: bash

.. references:

.. _Ceph: http://ceph.com/
.. _Kargo: https://github.com/kubernetes-incubator/kargo
.. _Kubernetes: http://kubernetes.io/
.. _Calico: https://github.com/projectcalico/calico-containers/releases/tag/v0.22.0
.. _calicoctl: https://github.com/projectcalico/calico-containers/releases/tag/v1.0.0-beta
.. _OpenStack: http://www.openstack.org/
.. _fuel-ccp: http://fuel-ccp.readthedocs.io/
.. _fio: https://github.com/axboe/fio
.. _Rally: https://rally.readthedocs.io/en/latest/index.html

Reports
=======

Test plan execution reports:
 * :ref:`Measuring_performance_of_cinder_ceph`
