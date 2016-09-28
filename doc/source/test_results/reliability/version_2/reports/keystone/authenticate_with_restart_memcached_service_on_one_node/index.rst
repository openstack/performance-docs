Keystone authentication with memached restart on one node
=========================================================

This report is generated on results collected by execution of the following
Rally scenario:

.. code-block:: yaml

    ---
    {% set repeat = repeat|default(5) %}
      Authenticate.keystone:
    {% for iteration in range(repeat) %}
        -
          runner:
            type: "constant_for_duration"
            duration: 30
            concurrency: 5
          context:
            users:
              tenants: 1
              users_per_tenant: 1
          hooks:
            -
              name: fault_injection
              args:
                action: restart memcached service on one node
              trigger:
                name: event
                args:
                  unit: iteration
                  at: [100]
    {% endfor %}
    

Summary
-------

In this scenario we restart Memcached service on one of controller nodes.
Memcached is used as caching backend for Keystone, thus it's expected that
Keystone performance may degrade.

+-----------------------+--------------+---------------------------------------+-------------------------------------------+
| Service downtime, s   | MTTR, s      | Absolute performance degradation, s   | Relative performance degradation, ratio   |
+=======================+==============+=======================================+===========================================+
| N/A                   | 0.458 ±0.068 | 0.057 ±0.034                          | 1.46 ±0.27                                |
+-----------------------+--------------+---------------------------------------+-------------------------------------------+

Metrics:
    * `Service downtime` is the time interval between the first and
      the last errors.
    * `MTTR` is the mean time to recover service performance after
      the fault.
    * `Absolute performance degradation` is an absolute difference between
      the mean of operation duration during recovery period and the baseline's.
    * `Relative performance degradation` is the ratio between the mean
      of operation duration during recovery period and the baseline's.

Details
-------

This section contains individual data for particular scenario runs.



Run #1
^^^^^^

.. image:: plot_1.svg

Baseline
~~~~~~~~

Baseline samples are collected before the start of fault injection. They are
used to estimate service performance degradation after the fault.

+-----------+-------------+-----------+-----------+---------------------+
|   Samples |   Median, s |   Mean, s |   Std dev |   95% percentile, s |
+===========+=============+===========+===========+=====================+
|        88 |        0.12 |      0.12 |     0.014 |                0.13 |
+-----------+-------------+-----------+-----------+---------------------+







Run #2
^^^^^^

.. image:: plot_2.svg

Baseline
~~~~~~~~

Baseline samples are collected before the start of fault injection. They are
used to estimate service performance degradation after the fault.

+-----------+-------------+-----------+-----------+---------------------+
|   Samples |   Median, s |   Mean, s |   Std dev |   95% percentile, s |
+===========+=============+===========+===========+=====================+
|        84 |        0.12 |      0.12 |    0.0078 |                0.13 |
+-----------+-------------+-----------+-----------+---------------------+




Service performance degradation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tested service has measurable performance degradation during the
following time period(s).

+-----+----------------------+---------------------------+------------------------+
|   # | Time to recover, s   | Absolute degradation, s   | Relative degradation   |
+=====+======================+===========================+========================+
|   1 | 0.4059 ±0.0027       | 0.069 ±0.030              | 1.57 ±0.25             |
+-----+----------------------+---------------------------+------------------------+




Run #3
^^^^^^

.. image:: plot_3.svg

Baseline
~~~~~~~~

Baseline samples are collected before the start of fault injection. They are
used to estimate service performance degradation after the fault.

+-----------+-------------+-----------+-----------+---------------------+
|   Samples |   Median, s |   Mean, s |   Std dev |   95% percentile, s |
+===========+=============+===========+===========+=====================+
|        88 |        0.12 |      0.13 |     0.017 |                0.15 |
+-----------+-------------+-----------+-----------+---------------------+







Run #4
^^^^^^

.. image:: plot_4.svg

Baseline
~~~~~~~~

Baseline samples are collected before the start of fault injection. They are
used to estimate service performance degradation after the fault.

+-----------+-------------+-----------+-----------+---------------------+
|   Samples |   Median, s |   Mean, s |   Std dev |   95% percentile, s |
+===========+=============+===========+===========+=====================+
|        84 |        0.12 |      0.12 |      0.01 |                0.14 |
+-----------+-------------+-----------+-----------+---------------------+







Run #5
^^^^^^

.. image:: plot_5.svg

Baseline
~~~~~~~~

Baseline samples are collected before the start of fault injection. They are
used to estimate service performance degradation after the fault.

+-----------+-------------+-----------+-----------+---------------------+
|   Samples |   Median, s |   Mean, s |   Std dev |   95% percentile, s |
+===========+=============+===========+===========+=====================+
|        84 |        0.13 |      0.13 |    0.0086 |                0.14 |
+-----------+-------------+-----------+-----------+---------------------+




Service performance degradation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tested service has measurable performance degradation during the
following time period(s).

+-----+----------------------+---------------------------+------------------------+
|   # | Time to recover, s   | Absolute degradation, s   | Relative degradation   |
+=====+======================+===========================+========================+
|   1 | 0.5110 ±0.0037       | 0.045 ±0.037              | 1.35 ±0.29             |
+-----+----------------------+---------------------------+------------------------+


