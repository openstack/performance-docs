Keystone DB / cache operations analysis
---------------------------------------

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The test plan (test case #1) is executed at the all-in-one virtual environment,
created with Oracle VM VirtualBox Manager.

Hardware
~~~~~~~~

All-in-one installation on virtual environment.

+-----------+------------------------------------------------------------+
| Parameter | Value                                                      |
+-----------+------------------------------------------------------------+
| CPU       | 4 CPU out of 8 (2,7 GHz Intel Core i5)                     |
+-----------+------------------------------------------------------------+
| RAM       | 4 Gb                                                       |
+-----------+------------------------------------------------------------+

Software
~~~~~~~~

This section describes installed software.

+-----------------+--------------------------------------------+
| Parameter       | Value                                      |
+-----------------+--------------------------------------------+
| OS              | Ubuntu 15.04                               |
+-----------------+--------------------------------------------+

Execution
^^^^^^^^^

To process all control plane requests against the environment the following
set of commands need to be processed::

    openstack --profile SECRET_KEY token issue
    openstack --profile SECRET_KEY user list
    openstack --profile SECRET_KEY endpoint list
    openstack --profile SECRET_KEY service list
    openstack --profile SECRET_KEY server create --image <image_id> --flavor <flavor_id> <server_name>

Reports
^^^^^^^

.. toctree::
    :maxdepth: 1

    liberty_fernet_cache_off
    liberty_fernet_cache_on
    liberty_uuid_cache_off
    liberty_uuid_cache_on
    mitaka_fernet_cache_off
    mitaka_fernet_cache_on
    mitaka_uuid_cache_off
    mitaka_uuid_cache_on
