Running profiling against Liberty Keystone (Fernet tokens, cache turned on)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents::

Parameters
~~~~~~~~~~

=========================== ===========
Parameter name              Value
=========================== ===========
OpenStack release           Liberty
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
| Total (*) Keystone DB queries count                          | 70        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 466       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 35        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 241       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 35        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 225       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 35        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 225       |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 9                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 8                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 8                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 10                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.type = %s AND assignment.actor_id = %s AND assignment.target_id = %s                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 4                  |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %s                                                             |                    |
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

**Cached operations stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f616845e210>, u'66ad606d34854993a502159d5aeb2220' |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _validate_token       | <keystone.token.provider.Manager object at 0x7f616841f710>, 'gAAAAABW-UBZFYDCk76jI3hJvTg2gRpANGk0J-  |            | 9              |
|                       | QqtTldQ7cCs2dRIPR1kw_BJzDcklb3IAAlPzAalHqPDfTyJUhNN4T0zNuIFf92lMEu-cyVRxZBVw-OLY8hO-                 |            |                |
|                       | nxOgh1FoLBqwe6SZgi0MvFVEdvgb9tfDKynks_CB1ApQtPmi3pkC54obPwHnY'                                       |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_revoke_tree      | <keystone.contrib.revoke.core.Manager object at 0x7f616845f1d0>,                                     |            | 10             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user_by_name      | <keystone.identity.core.Manager object at 0x7f6168728750>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user              | <keystone.identity.core.Manager object at 0x7f6168728750>, '020fbf5e143146c2aa3816a5eb07e65b'        |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f61684a9190>, 'e1ec2c364fa4480c9dd8db33e1de097e'        |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'e1ec2c364fa4480c9dd8db33e1de097e'       |            | 10             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project_by_name   | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f616845f210>, u'66ad606d34854993a502159d5aeb2220' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'default'                                |            | 8              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Server create request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 60        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 980       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 30        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 691       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 30        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 289       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 30        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 289       |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 9                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 16                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 8                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 21                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 18                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.type = %s AND assignment.actor_id = %s AND assignment.target_id = %s                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 4                  |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %s                                                             |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 17                 |
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

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+

**Cached operations stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f616845e210>, u'66ad606d34854993a502159d5aeb2220' |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f61684a9190>, 'e1ec2c364fa4480c9dd8db33e1de097e'        |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_revoke_tree      | <keystone.contrib.revoke.core.Manager object at 0x7f616845f1d0>,                                     |            | 3              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user              | <keystone.identity.core.Manager object at 0x7f6168728750>, '020fbf5e143146c2aa3816a5eb07e65b'        |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _validate_token       | <keystone.token.provider.Manager object at 0x7f616841f710>, 'gAAAAABW-Tn9YF8                         |            | 1              |
|                       | -QHo3fneFWxPDbURkdQ1pFiQ4HwZcr3wilSG17WeilkpuKy16b0tcXvxUC3x7xXw7rVE5bUDhnuXup-                      |            |                |
|                       | EvzKd6k4aNHlPwqwemh0djiEdEmhyjfxXB76_fF0kcQlL2iw2l6MN42BQO_oU1OFYE01-9nTeheFIsii3rBkERAYQ'           |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user_by_name      | <keystone.identity.core.Manager object at 0x7f6168728750>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'e1ec2c364fa4480c9dd8db33e1de097e'       |            | 10             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project_by_name   | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f616845f210>, u'66ad606d34854993a502159d5aeb2220' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'default'                                |            | 10             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Service list request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 54        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 400       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 27        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 190       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 27        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 210       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 27        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 210       |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 9                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 16                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 46                 |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 21                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 18                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.type = %s AND assignment.actor_id = %s AND assignment.target_id = %s                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 15                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %s                                                             |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 11                 |
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

**Cached operations stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f616845e210>, u'66ad606d34854993a502159d5aeb2220' |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_revoke_tree      | <keystone.contrib.revoke.core.Manager object at 0x7f616845f1d0>,                                     |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user_by_name      | <keystone.identity.core.Manager object at 0x7f6168728750>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user              | <keystone.identity.core.Manager object at 0x7f6168728750>, '020fbf5e143146c2aa3816a5eb07e65b'        |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f61684a9190>, 'e1ec2c364fa4480c9dd8db33e1de097e'        |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'e1ec2c364fa4480c9dd8db33e1de097e'       |            | 10             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project_by_name   | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f616845f210>, u'66ad606d34854993a502159d5aeb2220' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'default'                                |            | 7              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+


Token issue request stats
~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 28        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 219       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 14        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 150       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 14        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 69        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 14        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 69        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 9                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 16                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 46                 |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.extra AS role_extra                          | 3                  |
| FROM role                                                                                            |                    |
| WHERE role.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 9                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 6                  |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.type = %s AND assignment.actor_id = %s AND assignment.target_id = %s                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 7                  |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %s                                                             |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 11                 |
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

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+

**Cached operations stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f616845e210>, u'66ad606d34854993a502159d5aeb2220' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'e1ec2c364fa4480c9dd8db33e1de097e'       |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'default'                                |            | 3              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

User list request stats
~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 52        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 332       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 26        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 157       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 26        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 175       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 26        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 175       |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 9                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 16                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 10                 |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.extra AS role_extra                          | 3                  |
| FROM role                                                                                            |                    |
| WHERE role.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 8                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 8                  |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.type = %s AND assignment.actor_id = %s AND assignment.target_id = %s                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 4                  |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %s                                                             |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 9                  |
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

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+

**Keystone cached methods stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f616845e210>, u'66ad606d34854993a502159d5aeb2220' |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_revoke_tree      | <keystone.contrib.revoke.core.Manager object at 0x7f616845f1d0>,                                     |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user_by_name      | <keystone.identity.core.Manager object at 0x7f6168728750>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user              | <keystone.identity.core.Manager object at 0x7f6168728750>, '020fbf5e143146c2aa3816a5eb07e65b'        |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f61684a9190>, 'e1ec2c364fa4480c9dd8db33e1de097e'        |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'e1ec2c364fa4480c9dd8db33e1de097e'       |            | 10             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project_by_name   | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f616845f210>, u'66ad606d34854993a502159d5aeb2220' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f61684a9190>, u'default'                                |            | 8              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
