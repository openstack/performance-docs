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

In this scenario we kill one of running RabbitMQ servers. Once killed RabbitMQ
gets restarted automatically by Pacemaker.

The cloud stays stable, no errors, nor significant performance degradation
observed. Oslo.messaging library handles the loss of connection to RabbitMQ
and reconnects to one of other servers automatically::

    AMQP server on 10.43.0.3:5673 is unreachable: timed out. Trying again in
    1 seconds.
    ...
    Reconnected to AMQP server on 10.43.0.6:5673 via [amqp] client


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
|        45 |         5.8 |       5.8 |       0.3 |                 6.1 |
+-----------+-------------+-----------+-----------+---------------------+





