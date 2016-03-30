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
  * Moving to oslo.cache instead of local `dogpile.cache` usage in Liberty.

Federation support introduced multiple SQL JOINs usage in Keystone and made
the database scheme a bit more complex. As for the caching layer usage, one
specific issue is clearly seen in Mitaka keystone operations caching. Although
all Liberty and Mitaka environments had identical caching layer configuration,
from HTML reports it can be clearly seen that on Liberty all possible methods
were successfully cached and while their calling cached copy was always used.
On Mitaka OpenStack for some reason cached copy was not used sometimes and the
DB requests were processed.

One more interesting moment is related to the `keystone_authtoken` middleware
(and, more specifically, its cache) usage. Although all environments that took
part in the research had exactly the same `keystone_authtoken` middleware
configuration, described in the test plan and containing `memcache_servers`
parameter set up, Mitaka environments profiling shows that all OpenStack
services that used `keystone_authtoken` middleware did not use the external
Memcached cached token copy. All of them used Keystone API every time REST API
request was coming to the OpenStack services. This behaviour needs to be
investigated separately.

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
