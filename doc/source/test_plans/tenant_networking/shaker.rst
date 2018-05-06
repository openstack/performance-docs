Shaker
------

This section describes how to perform
:ref:`openstack_tenant_networking_test_plan` with `Shaker`_ tool.

Test environment preparation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run tests you will need a machine located outside of the cloud. This machine
must be routable from OpenStack instances and need to have one open port
to accept connections from Shaker agents. See more details in
`Shaker deployment`_ guide.

Shaker is distributed as Python package and available through PyPi
(https://pypi.org/project/pyshaker/).
It is recommended to be installed inside virtualenv.

.. code::

    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install pyshaker

The connection to OpenStack can be configured using standard ``openrc`` file.
(Refer to http://docs.openstack.org/cli-reference/content/cli_openrc.html on
how to retrieve it). Alternatively the configuration can be passed to Shaker
via set of CLI parameters ``--os-tenant-name``, ``--os-username``,
``--os-password``, ``--os-auth-url`` and ``--os-region-name``. Connection to
SSL endpoints is configured by parameters ``--os-cacert`` and
``--os-insecure``. Note that it is highly recommended to run Shaker with admin
user. Use of non-admin user is also possible though, see
`Running Shaker by non-admin user`_.

Before starting tests a master image must be built. The process downloads
Ubuntu cloud image, installs all necessary packages and stores snapshot into
Glance. This snapshot is used by ``shaker`` to boot instances.

.. code::

    $ shaker-image-builder

Running `shaker` tool starts a server that accepts connections from
agents located on instances. In order to work user needs to specify host
address and port number. The result may be stored in raw format (``--json``),
in ReST (``--book``) or as interactive HTML report (``--report``).


Test Case 1: L2 instance-to-instance performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test case specification**: :ref:`openstack_tenant_networking_test_plan_l2`

**Execution**::

    shaker --server-endpoint <host:port> --scenario openstack/perf_l2 --book <report folder>


Test Case 2: L2 concurrent performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test case specification**: :ref:`openstack_tenant_networking_test_plan_l2_concurrent`

**Execution**::


    shaker --server-endpoint <host:port> --scenario openstack/full_l2 --book <report folder>


Test Case 3: L3 east-west instance-to-instance performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test case specification**: :ref:`openstack_tenant_networking_test_plan_l3_east_west`

**Execution**::

    shaker --server-endpoint <host:port> --scenario openstack/perf_l3_east_west --book <report folder>


Test Case 4: L3 east-west concurrent performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test case specification**: :ref:`openstack_tenant_networking_test_plan_l3_east_west_concurrent`

**Execution**::

    shaker --server-endpoint <host:port> --scenario openstack/full_l3_east_west --book <report folder>


Test Case 5: L3 north-south instance-to-instance performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test case specification**: :ref:`openstack_tenant_networking_test_plan_l3_north_south`

**Execution**::

    shaker --server-endpoint <host:port> --scenario openstack/perf_l3_north_south --book <report folder>


Test Case 6: L3 north_south concurrent performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test case specification**: :ref:`openstack_tenant_networking_test_plan_l3_north_south_concurrent`

**Execution**::

    shaker --server-endpoint <host:port> --scenario openstack/full_l3_north_south --book <report folder>


Test Case 7: Neutron QoS testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test case specification**: :ref:`openstack_tenant_networking_test_plan_qos`

**Execution**::

    shaker --server-endpoint <host:port> --scenario openstack/qos/perf_l2 --book <report folder>


.. references:

.. _Shaker: https://pyshaker.readthedocs.io/en/latest/index.html
.. _Shaker deployment: https://pyshaker.readthedocs.io/en/latest/installation.html#openstack-deployment
.. _Running Shaker by non-admin user: https://pyshaker.readthedocs.io/en/latest/installation.html#running-shaker-by-non-admin-user
