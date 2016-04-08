Running profiling against Mitaka Keystone (Fernet tokens, cache turned on)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents::

Parameters
~~~~~~~~~~

=========================== ===========
Parameter name              Value
=========================== ===========
OpenStack release           Mitaka
Cache                       on
Token type                  Fernet
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
| Total (*) Keystone DB queries time spent, ms                 | 203       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 15        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 82        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 21        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 121       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 21        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 121       |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 3                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 8                  |
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
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 7                  |
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
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 9                  |
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
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7ff335d08e10>, u'default'                                |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7ff335d08e10>, '1f093e18f4ab4318bdb2876a03d81811'        |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7ff335cbdf90>, u'3481c11394a64189bafc60551e1ee25c' |            | 3              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7ff335e09c10>, u'b4a6b5f09b9c4b57a582b16537f4a976',    |            | 2              |
|           |                                | u'1f093e18f4ab4318bdb2876a03d81811'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'default'                                |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7ff336019d90>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_revoke_tree               | <keystone.revoke.core.Manager object at 0x7ff335cdf790>,                                             |            | 9              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _validate_token                | <keystone.token.provider.Manager object at 0x7ff335c8be90>, 'gAAAAABXBnVbEtemCkqIkBAri3f0P5C2s3z-    |            | 8              |
|           |                                | ZzP5MCkHMCHVGuLdwaJsxuw9k731LHrIuKE9krW-                                                             |            |                |
|           |                                | 2bU7ToROLD9oPTZA38kOU4jy5kqJWzBj7O5VpoQDSi_3VerUdQytO31d47N6v-dYmLtatUKPAHJmMGvRikjhBN4laTh8gay-     |            |                |
|           |                                | LEPId9yhdeA'                                                                                         |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7ff335e09c10>, 'b4a6b5f09b9c4b57a582b16537f4a976',     |            | 1              |
|           |                                | '1f093e18f4ab4318bdb2876a03d81811'                                                                   |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'1f093e18f4ab4318bdb2876a03d81811'       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user                       | <keystone.identity.core.Manager object at 0x7ff336019d90>, 'b4a6b5f09b9c4b57a582b16537f4a976'        |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Server create request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 22        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 213       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 8         |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 77        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 14        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 136       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 14        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 136       |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 14                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 8                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 23                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 3                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 13                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 9                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 7                  |
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
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7ff335d08e10>, u'default'                                |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _validate_token                | <keystone.token.provider.Manager object at 0x7ff335c8be90>,                                          |            | 1              |
|           |                                | 'gAAAAABXBmrRWacx2eWnMbEUxvtXGHLKT3SQfT56J-61d7WyHqAAHH7KN5jv1EFuCusKWBtTZ2KmoXhRN6-u0NdLlgBHYvSwho- |            |                |
|           |                                | sOmmnD1IhHkHr0ZTml39hLZXhM0HmkAy3tSbq76aLvVYGDqE9BHjjVlU4W-P_gXwad6ZhdH9XkoOCkzmWJR4'                |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7ff335d08e10>, '1f093e18f4ab4318bdb2876a03d81811'        |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7ff335cbdf90>, u'3481c11394a64189bafc60551e1ee25c' |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7ff335e09c10>, u'b4a6b5f09b9c4b57a582b16537f4a976',    |            | 2              |
|           |                                | u'1f093e18f4ab4318bdb2876a03d81811'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'default'                                |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7ff336019d90>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_revoke_tree               | <keystone.revoke.core.Manager object at 0x7ff335cdf790>,                                             |            | 3              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7ff335e09c10>, 'b4a6b5f09b9c4b57a582b16537f4a976',     |            | 2              |
|           |                                | '1f093e18f4ab4318bdb2876a03d81811'                                                                   |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'1f093e18f4ab4318bdb2876a03d81811'       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user                       | <keystone.identity.core.Manager object at 0x7ff336019d90>, 'b4a6b5f09b9c4b57a582b16537f4a976'        |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Service list request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 20        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 126       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 7         |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 38        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 13        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 88        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 13        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 88        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 4                  |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 14                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 8                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 23                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 4                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 13                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 9                  |
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
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7ff335d08e10>, u'default'                                |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7ff335d08e10>, '1f093e18f4ab4318bdb2876a03d81811'        |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7ff335cbdf90>, u'3481c11394a64189bafc60551e1ee25c' |            | 3              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7ff335e09c10>, u'b4a6b5f09b9c4b57a582b16537f4a976',    |            | 2              |
|           |                                | u'1f093e18f4ab4318bdb2876a03d81811'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'default'                                |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7ff336019d90>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_revoke_tree               | <keystone.revoke.core.Manager object at 0x7ff335cdf790>,                                             |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7ff335e09c10>, 'b4a6b5f09b9c4b57a582b16537f4a976',     |            | 1              |
|           |                                | '1f093e18f4ab4318bdb2876a03d81811'                                                                   |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'1f093e18f4ab4318bdb2876a03d81811'       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user                       | <keystone.identity.core.Manager object at 0x7ff336019d90>, 'b4a6b5f09b9c4b57a582b16537f4a976'        |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Token issue request stats
~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 7         |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 49        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 2         |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 14        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 5         |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 35        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 5         |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 35        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.

**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 4                  |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 14                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 8                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 23                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 4                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 13                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 9                  |
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
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7ff335cbdf90>, u'3481c11394a64189bafc60551e1ee25c' |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'admin', 'default'                       |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7ff336019d90>, u'admin', 'default'                       |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7ff335e09c10>, u'b4a6b5f09b9c4b57a582b16537f4a976',    |            | 1              |
|           |                                | u'1f093e18f4ab4318bdb2876a03d81811'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'1f093e18f4ab4318bdb2876a03d81811'       |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'default'                                |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

User list request stats
~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 30        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 306       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 7         |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 70        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 23        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 236       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 23        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 236       |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.

**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 14                 |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 23                 |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user LEFT OUTER JOIN local_user ON user.id = local_user.user_id                                 |                    |
| WHERE local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN federated_user ON anon_1.user_id  |                    |
| = federated_user.user_id ORDER BY anon_1.user_id                                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 21                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 14                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 8                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 23                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 4                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 13                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 9                  |
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
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7ff335d08e10>, u'default'                                |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7ff335d08e10>, '1f093e18f4ab4318bdb2876a03d81811'        |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_role                       | <keystone.assignment.core.RoleManager object at 0x7ff335cbdf90>, u'3481c11394a64189bafc60551e1ee25c' |            | 3              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7ff335e09c10>, u'b4a6b5f09b9c4b57a582b16537f4a976',    |            | 2              |
|           |                                | u'1f093e18f4ab4318bdb2876a03d81811'                                                                  |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project_by_name            | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_domain                     | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'default'                                |            | 4              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user_by_name               | <keystone.identity.core.Manager object at 0x7ff336019d90>, u'admin', 'default'                       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | _get_revoke_tree               | <keystone.revoke.core.Manager object at 0x7ff335cdf790>,                                             |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7ff335e09c10>, 'b4a6b5f09b9c4b57a582b16537f4a976',     |            | 1              |
|           |                                | '1f093e18f4ab4318bdb2876a03d81811'                                                                   |            |                |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_project                    | <keystone.resource.core.Manager object at 0x7ff335d07e10>, u'1f093e18f4ab4318bdb2876a03d81811'       |            | 2              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| Memcache  | get_user                       | <keystone.identity.core.Manager object at 0x7ff336019d90>, 'b4a6b5f09b9c4b57a582b16537f4a976'        |            | 1              |
+-----------+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
