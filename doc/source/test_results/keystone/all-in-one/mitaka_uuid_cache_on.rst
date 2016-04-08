Running profiling against Mitaka Keystone (UUID tokens, cache turned on)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents::

Parameters
~~~~~~~~~~

=========================== ===========
Parameter name              Value
=========================== ===========
OpenStack release           Mitaka
Cache                       on
Token type                  UUID
Environment characteristics Single node
=========================== ===========

Endpoint list request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 36        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 365       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 15        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 158       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 21        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 207       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 19        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 199       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 8         |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.

**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 11                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 17                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 4                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 5                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+

**Keystone cached methods stats**

+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cache** | **Cached operations**          | **args**                                                                                             | **kwargs** | **Times used** |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7fbe19ec8dd0>, u'31d31420a3e349268cd7875aa1825663',    |            | 2              |
|           |                                | u'f1a058ad00364df29cb819a5478e8884'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_token                     | <keystone.token.persistence.core.PersistenceManager object at 0x7fbe18c510d0>,                       |            | 1              |
|           |                                | '4826bf1d6cc04e658316a0135d225f32'                                                                   |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'f1a058ad00364df29cb819a5478e8884'       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7fbe19d8d190>, u'8272f6d8be65464e94d3be094cf35e4c' |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _validate_token                | <keystone.token.provider.Manager object at 0x7fbe19d55090>, '4826bf1d6cc04e658316a0135d225f32'       |            | 8              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7fbe1a0e0950>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_revoke_tree               | <keystone.revoke.core.Manager object at 0x7fbe19d9d950>,                                             |            | 9              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'default'                                |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Server create request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 22        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 225       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 8         |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 115       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 14        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 110       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 12        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 95        |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 15        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 11                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 17                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 24                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 4                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 5                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+

**Keystone cached methods stats**

+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cache** | **Cached operations**          | **args**                                                                                             | **kwargs** | **Times used** |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7fbe19ec8dd0>, u'31d31420a3e349268cd7875aa1825663',    |            | 3              |
|           |                                | u'f1a058ad00364df29cb819a5478e8884'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7fbe19db7090>, u'f1a058ad00364df29cb819a5478e8884'       |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'default'                                |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'f1a058ad00364df29cb819a5478e8884'       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7fbe19d8d190>, u'8272f6d8be65464e94d3be094cf35e4c' |            | 3              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_token                     | <keystone.token.persistence.core.PersistenceManager object at 0x7fbe19c59bd0>,                       |            | 2              |
|           |                                | '428e793676454d04a9ea2fec753c35b1'                                                                   |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user                       | <keystone.identity.core.Manager object at 0x7fbe1a0e0950>, u'31d31420a3e349268cd7875aa1825663'       |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7fbe1a0e0950>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7fbe19db7090>, u'default'                                |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_revoke_tree               | <keystone.revoke.core.Manager object at 0x7fbe19d9d950>,                                             |            | 3              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _validate_token                | <keystone.token.provider.Manager object at 0x7fbe19d55090>, '18d75ba7355d4a8684a5d5658d005f1f'       |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Service list request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 20        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 131       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 7         |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 48        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 13        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 83        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 11        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 74        |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 9         |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.

**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 11                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 17                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 24                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 4                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 5                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+

**Keystone cached methods stats**

+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cache** | **Cached operations**          | **args**                                                                                             | **kwargs** | **Times used** |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7fbe19ec8dd0>, u'31d31420a3e349268cd7875aa1825663',    |            | 2              |
|           |                                | u'f1a058ad00364df29cb819a5478e8884'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_token                     | <keystone.token.persistence.core.PersistenceManager object at 0x7fbe1888aad0>,                       |            | 1              |
|           |                                | '6982459b63f647ed9210bd0ce32f8e95'                                                                   |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'f1a058ad00364df29cb819a5478e8884'       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7fbe19d8d190>, u'8272f6d8be65464e94d3be094cf35e4c' |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7fbe1a0e0950>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_revoke_tree               | <keystone.revoke.core.Manager object at 0x7fbe19d9d950>,                                             |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'default'                                |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Token issue request stats
~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 9         |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 114       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 3         |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 41        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 6         |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 73        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 5         |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 67        |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 1         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 6         |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.

**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 11                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 20                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 24                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 4                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 5                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+

**Keystone cached methods stats**

+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cache** | **Cached operations**          | **args**                                                                                             | **kwargs** | **Times used** |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7fbe19ec8dd0>, u'31d31420a3e349268cd7875aa1825663',    |            | 1              |
|           |                                | u'f1a058ad00364df29cb819a5478e8884'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'f1a058ad00364df29cb819a5478e8884'       |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7fbe19d8d190>, u'8272f6d8be65464e94d3be094cf35e4c' |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7fbe1a0e0950>, u'admin', 'default'                       |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'admin', 'default'                       |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'default'                                |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

User list request stats
~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 30        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 178       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 7         |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 33        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 23        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 145       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 21        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 136       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 9         |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.

**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 9                  |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 4                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user LEFT OUTER JOIN local_user ON user.id = local_user.user_id                                 |                    |
| WHERE local_user.domain_id = %(domain_id_1)s                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 4                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 12                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 10                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 9                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 9                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user LEFT OUTER JOIN local_user ON user.id = local_user.user_id                                 |                    |
| WHERE local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id =    |                    |
| local_user.user_id ORDER BY anon_1.user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 5                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 4                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN federated_user ON anon_1.user_id =                 |                    |
| federated_user.user_id ORDER BY anon_1.user_id                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+

**Keystone cached methods stats**

+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cache** | **Cached operations**          | **args**                                                                                             | **kwargs** | **Times used** |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7fbe19ec8dd0>, u'31d31420a3e349268cd7875aa1825663',    |            | 2              |
|           |                                | u'f1a058ad00364df29cb819a5478e8884'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'default'                                |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'f1a058ad00364df29cb819a5478e8884'       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7fbe19d8d190>, u'8272f6d8be65464e94d3be094cf35e4c' |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7fbe1a0e0950>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7fbe19db6090>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_revoke_tree               | <keystone.revoke.core.Manager object at 0x7fbe19d9d950>,                                             |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_token                     | <keystone.token.persistence.core.PersistenceManager object at 0x7fbe18c53450>,                       |            | 1              |
|           |                                | '6c4b9b6e838c42ff83e6dcfed52f596e'                                                                   |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
