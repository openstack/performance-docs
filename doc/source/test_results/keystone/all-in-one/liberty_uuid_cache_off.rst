Running profiling against Liberty Keystone (UUID tokens, cache turned off)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents::

Parameters
~~~~~~~~~~

=========================== ===========
Parameter name              Value
=========================== ===========
OpenStack release           Liberty
Cache                       off
Token type                  UUID
Environment characteristics Single node
=========================== ===========

Endpoint list request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 92        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 534       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 46        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 259       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 46        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 275       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 44        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 266       |
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
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 9                  |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %s                                                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 8                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 7                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.extra AS role_extra                          | 24                 |
| FROM role                                                                                            |                    |
| WHERE role.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 10                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT domain.id AS domain_id, domain.name AS domain_name, domain.enabled AS domain_enabled,         | 9                  |
| domain.extra AS domain_extra                                                                         |                    |
| FROM domain                                                                                          |                    |
| WHERE domain.id = %s                                                                                 |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 8                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 16                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+


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
| Total (*) Keystone DB queries count                          | 56        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 369       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 28        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 177       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 28        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 192       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 26        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 174       |
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
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 14                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %s                                                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 8                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 4                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %s AND project.domain_id = %s                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 4                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.name = %s AND user.domain_id = %s                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 4                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.extra AS role_extra                          | 9                  |
| FROM role                                                                                            |                    |
| WHERE role.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 11                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT domain.id AS domain_id, domain.name AS domain_name, domain.enabled AS domain_enabled,         | 9                  |
| domain.extra AS domain_extra                                                                         |                    |
| FROM domain                                                                                          |                    |
| WHERE domain.id = %s                                                                                 |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 8                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 17                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

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
| Total (*) Keystone DB queries count                          | 26        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 174       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 13        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 91        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 13        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 83        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 12        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 79        |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 1         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 4         |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 14                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %s                                                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 8                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 10                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %s AND project.domain_id = %s                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 4                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.name = %s AND user.domain_id = %s                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 4                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.extra AS role_extra                          | 9                  |
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
| SELECT domain.id AS domain_id, domain.name AS domain_name, domain.enabled AS domain_enabled,         | 9                  |
| domain.extra AS domain_extra                                                                         |                    |
| FROM domain                                                                                          |                    |
| WHERE domain.id = %s                                                                                 |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 8                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 9                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+


User list request stats
~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 56        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 360       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 28        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 212       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 28        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 148       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 26        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 139       |
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
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 14                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %s                                                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 8                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 10                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %s AND project.domain_id = %s                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 3                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.name = %s AND user.domain_id = %s                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.name AS user_name, user.domain_id AS user_domain_id, user.password   | 4                  |
| AS user_password, user.enabled AS user_enabled, user.extra AS user_extra, user.default_project_id AS |                    |
| user_default_project_id                                                                              |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.extra AS role_extra                          | 9                  |
| FROM role                                                                                            |                    |
| WHERE role.id = %s                                                                                   |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 13                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT domain.id AS domain_id, domain.name AS domain_name, domain.enabled AS domain_enabled,         | 3                  |
| domain.extra AS domain_extra                                                                         |                    |
| FROM domain                                                                                          |                    |
| WHERE domain.id = %s                                                                                 |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 8                  |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 9                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %s                                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+--------------+--------------------+
| **DB query** | **Time spent, ms** |
+--------------+--------------------+
