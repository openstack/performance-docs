Keystone DB / cache operations analysis
---------------------------------------

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

The :ref:`keystone_performance` (test case #1) is executed at the all-in-one
virtual environment, created with Oracle VM VirtualBox Manager.

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

Short summary
^^^^^^^^^^^^^

Detailed information about every topology (out of 8 that were examined) can
be found in the next `Reports` section.

Every topology was examined with 5 different profiled control plane requests to
figure out number and relative time spent on the DB / Memcached caching.

All collected data needs to be deeply examined in future, although several
interesting moments can be highlighted right now to pay special attention to
them further.

Due to the collected profiling information, it can be clearly seen that
Keystone was significantly changed during Mitaka timeframe, and lots of changes
seem to be related to the following:
  * Federation support (introduced more complexity on the DB level)
  * Moving to oslo.cache instead of local `dogpile.cache` usage in Liberty and
    introducing local context cache layer for per-request caching.

Federation support introduced multiple SQL JOINs usage in Keystone and made
the database scheme a bit more complex. In further multinode research it's
planned to check how this is influencing operations DB operations performance
in case, for instance, if Galera cluster is used.

As for the caching layer usage, one specific issue is clearly seen in Mitaka
Keystone operations caching. Although local context cache should reduce number
of calls to Memcache via storing already grabbed data for the specific API
request in local thread, this was not observed (the duplicated function calls
still used Memcache for cache purposes). The `Keystone bug`_ was filed to
investigate this behaviour.

One more interesting moment is also related to the cache usage. If the cache
will be turned off in Keystone configuration explicitly, the profiling still
shows `data being fetched`_ from the Memcache.

.. _Keystone bug: https://bugs.launchpad.net/keystone/+bug/1567403
.. _data being fetched: https://bugs.launchpad.net/keystone/+bug/1567413


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
