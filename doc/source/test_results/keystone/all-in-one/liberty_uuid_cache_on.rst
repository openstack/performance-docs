Running profiling against Liberty Keystone (UUID tokens, cache turned on)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents::

Parameters
~~~~~~~~~~

=========================== ===========
Parameter name              Value
=========================== ===========
OpenStack release           Liberty
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
| Total (*) Keystone DB queries count                          | 44        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 465       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 22        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 230       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 22        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 235       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 20        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 204       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 31        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 5                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
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
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 15                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 25                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 13                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
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
| _validate_token       | <keystone.token.provider.Manager object at 0x7ff1cde3f710>, '0038b99a5d8b4888b54b41d5799f56a2'       |            | 9              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user_by_name      | <keystone.identity.core.Manager object at 0x7ff1ce146750>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_token            | <keystone.token.persistence.core.PersistenceManager object at 0x7ff1cc023210>,                       |            | 1              |
|                       | '0038b99a5d8b4888b54b41d5799f56a2'                                                                   |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_revoke_tree      | <keystone.contrib.revoke.core.Manager object at 0x7ff1cde7e1d0>,                                     |            | 10             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7ff1cde7d210>, u'68e61c80e05244f2ab9af0a9e2e0320a' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'741271ef2a554242af037d66d6682e3f'       |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'default'                                |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project_by_name   | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Server create request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: This control plane request numbers were not collected yet due to
          environmental issues.


Service list request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 36        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 227       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 18        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 101       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 18        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 126       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 16        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 108       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 18        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 13                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 12                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %s AND project.domain_id = %s                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 5                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 16                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 13                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %s                                                             |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 15                 |
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
| get_user_by_name      | <keystone.identity.core.Manager object at 0x7ff1ce146750>, u'admin', 'default'                       |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project_by_name   | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'admin', 'default'                       |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_revoke_tree      | <keystone.contrib.revoke.core.Manager object at 0x7ff1cde7e1d0>,                                     |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_token            | <keystone.token.persistence.core.PersistenceManager object at 0x7ff1cc0cb890>,                       |            | 1              |
|                       | '1c61ea5b4b4c4583aa9c394631cf458b'                                                                   |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7ff1cde7d210>, u'68e61c80e05244f2ab9af0a9e2e0320a' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'741271ef2a554242af037d66d6682e3f'       |            | 3              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'default'                                |            | 3              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Token issue request stats
~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 22        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 107       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 11        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 45        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 11        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 62        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 10        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 55        |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 1         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 7         |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 13                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 12                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %s AND project.domain_id = %s                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 5                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 16                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 13                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %s                                                             |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 15                 |
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

+-----------------------+------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                       | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'741271ef2a554242af037d66d6682e3f' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'default'                          |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------+------------+----------------+

User list request stats
~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 26        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 165       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 13        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 61        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 13        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 104       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 11        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 90        |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 14        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 13                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 12                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %s AND project.domain_id = %s                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 22                 |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 16                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 13                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %s                                                             |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 15                 |
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
| get_user_by_name      | <keystone.identity.core.Manager object at 0x7ff1ce146750>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project_by_name   | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'admin', 'default'                       |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_revoke_tree      | <keystone.contrib.revoke.core.Manager object at 0x7ff1cde7e1d0>,                                     |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_token            | <keystone.token.persistence.core.PersistenceManager object at 0x7ff1d7b6df90>,                       |            | 1              |
|                       | 'b7cf92a4467145c888974097112c2c3d'                                                                   |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7ff1cde7d210>, u'68e61c80e05244f2ab9af0a9e2e0320a' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'741271ef2a554242af037d66d6682e3f'       |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7ff1cdeca190>, u'default'                                |            | 4              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
