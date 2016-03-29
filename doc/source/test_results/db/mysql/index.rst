.. raw:: pdf

    PageBreak oneColumn

===============================
SQL Database performance report
===============================

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

This report is generated for :ref:`db_performance` test plan with
`Sysbench`_ tool. The data is collected in
:ref:`intel_mirantis_performance_lab`.


Software
~~~~~~~~

+-----------------+--------------------------------------------+
| Parameter       | Value                                      |
+-----------------+--------------------------------------------+
| OS              | Ubuntu 14.04.3                             |
+-----------------+--------------------------------------------+
| DB              | MySQL 5.6.28                               |
+-----------------+--------------------------------------------+
| HA              | Galera                                     |
+-----------------+--------------------------------------------+


Reports
^^^^^^^

.. toctree::
    :maxdepth: 2

    mysql-galera-direct/index
    mysql-galera-haproxy/index



.. references:

.. _Sysbench: https://github.com/akopytov/sysbench
