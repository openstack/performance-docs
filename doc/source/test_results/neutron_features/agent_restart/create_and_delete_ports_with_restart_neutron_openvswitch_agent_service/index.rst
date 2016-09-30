Ports operations and OVS agent restart
======================================

In this scenario we restart all OVS agents while Neutron creates and deletes
ports.

This report is generated on results collected by execution of the following
Rally scenario:

.. code-block:: yaml

    ---
      NeutronNetworks.create_and_delete_ports:
        -
          args:
            network_create_args: {}
            port_create_args: {}
            ports_per_network: 10
          runner:
            type: "constant_for_duration"
            duration: 300
            concurrency: 4
          context:
            users:
              tenants: 1
              users_per_tenant: 1
            quotas:
              neutron:
                network: -1
                port: -1
          hooks:
            -
              name: fault_injection
              args:
                action: restart neutron-openvswitch-agent service
              trigger:
                name: event
                args:
                  unit: iteration
                  at: [80]
    

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
|        65 |         8.7 |       8.8 |      0.31 |                 9.3 |
+-----------+-------------+-----------+-----------+---------------------+





