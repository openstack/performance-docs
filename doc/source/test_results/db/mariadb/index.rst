.. raw:: pdf

    PageBreak oneColumn

.. _db_performance_mariadb:

===================================
MariaDB Database performance report
===================================

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

This report is generated for :ref:`db_performance` test plan with
`Sysbench`_ tool. The data is collected in
:ref:`intel_mirantis_performance_lab_1`.


Software
~~~~~~~~

+-----------------+--------------------------------------------+
| Parameter       | Value                                      |
+-----------------+--------------------------------------------+
| OS              | Ubuntu 14.04.3                             |
+-----------------+--------------------------------------------+
| DB              | MariaDB                                    |
+-----------------+--------------------------------------------+
| HA              | Galera                                     |
+-----------------+--------------------------------------------+


Reports
^^^^^^^

.. toctree::
    :maxdepth: 2

    mariadb-galera-direct/index

.. references:

.. _Sysbench: https://github.com/akopytov/sysbench
