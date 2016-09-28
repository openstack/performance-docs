Boot and delete VM with reboot of one of controllers
====================================================

This report is generated on results collected by execution of the following
Rally scenario:

.. code-block:: yaml

    ---
      NovaServers.boot_and_delete_server:
        -
          args:
            flavor:
                name: "m1.micro"
            image:
                name: "(^cirros.*uec$|TestVM)"
            force_delete: false
          runner:
            type: "constant_for_duration"
            duration: 600
            concurrency: 4
          context:
            users:
              tenants: 1
              users_per_tenant: 1
          hooks:
            -
              name: fault_injection
              args:
                action: reboot one node with rabbitmq service
              trigger:
                name: event
                args:
                  unit: iteration
                  at: [50]
    

Summary
-------

In this scenario we reboot one of controllers (in Fuel architecture controller
runs DB, MQ, API services, scheduler). The observed recovery period corresponds
to time needed for a node to reboot, start services and get back to sync state.

+-----------------------+--------------+---------------------------------------+-------------------------------------------+
| Service downtime, s   | MTTR, s      | Absolute performance degradation, s   | Relative performance degradation, ratio   |
+=======================+==============+=======================================+===========================================+
| 8.7 ±1.6              | 286.89 ±0.87 | 14.7 ±4.7                             | 3.85 ±0.91                                |
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
|        36 |         5.1 |       5.2 |      0.63 |                 6.1 |
+-----------+-------------+-----------+-----------+---------------------+


Service downtime
~~~~~~~~~~~~~~~~

The tested service is not available during the following time period(s).

+-----+---------------+
|   # | Downtime, s   |
+=====+===============+
|   1 | 8.7 ±2.5      |
+-----+---------------+



Service performance degradation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tested service has measurable performance degradation during the
following time period(s).

+-----+----------------------+---------------------------+------------------------+
|   # | Time to recover, s   | Absolute degradation, s   | Relative degradation   |
+=====+======================+===========================+========================+
|   1 | 286.89 ±0.76         | 14.7 ±4.7                 | 3.85 ±0.91             |
+-----+----------------------+---------------------------+------------------------+


