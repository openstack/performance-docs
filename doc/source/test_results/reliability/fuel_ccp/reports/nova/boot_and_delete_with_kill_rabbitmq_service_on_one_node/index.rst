Boot and delete VM with kill of RabbitMQ on one of nodes
========================================================

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
            duration: 240
            concurrency: 4
          context:
            users:
              tenants: 1
              users_per_tenant: 1
          hooks:
            -
              name: fault_injection
              args:
                action: kill rabbitmq service on one node
              trigger:
                name: event
                args:
                  unit: iteration
                  at: [60]
    

Summary
-------



No errors nor performance degradation observed.



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
|        47 |         7.3 |       7.3 |      0.86 |                 8.8 |
+-----------+-------------+-----------+-----------+---------------------+





