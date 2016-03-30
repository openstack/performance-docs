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
| Total (*) Keystone DB queries count                          | 132       |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 1240      |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 55        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 506       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 77        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 734       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 75        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 722       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 12        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


.. note:: Number of DB queries is much bigger for this request comparing with
          similar Liberty environment. The difference is in
          `keystone_authtoken` middleware (and, more specifically, its cache)
          usage. Although all environments that took part in the research had
          exactly the same `keystone_authtoken` middleware configuration,
          described in the test plan and containing `memcache_servers`
          parameter set up, Mitaka environments profiling shows that all
          OpenStack services that used `keystone_authtoken` middleware did not
          use the external Memcached cached token copy. All of them used
          Keystone API every time REST API request was coming to the OpenStack
          services. This behaviour needs to be investigated separately.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 2                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 4                  |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 24                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 15                 |
| revocation_event_domain_id, revocation_event.project_id AS revocation_event_project_id,              |                    |
| revocation_event.user_id AS revocation_event_user_id, revocation_event.role_id AS                    |                    |
| revocation_event_role_id, revocation_event.trust_id AS revocation_event_trust_id,                    |                    |
| revocation_event.consumer_id AS revocation_event_consumer_id, revocation_event.access_token_id AS    |                    |
| revocation_event_access_token_id, revocation_event.issued_before AS revocation_event_issued_before,  |                    |
| revocation_event.expires_at AS revocation_event_expires_at, revocation_event.revoked_at AS           |                    |
| revocation_event_revoked_at, revocation_event.audit_id AS revocation_event_audit_id,                 |                    |
| revocation_event.audit_chain_id AS revocation_event_audit_chain_id                                   |                    |
| FROM revocation_event ORDER BY revocation_event.revoked_at                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 13                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 17                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 40                 |
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
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 4                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 4                  |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 12                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 7                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 8                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 11                 |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 13                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone cached methods stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f2e5728b9d0>, u'a465ecd9f7004c38b30792a07b363b2c'       |            | 6              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f2e57262350>, u'31c541984f48440ab8753d11d84e58ca' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f2e5728b9d0>, u'default'                                |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Server create request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 1140      |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 9581      |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 451       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 3500      |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 689       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 6081      |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 687       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 6067      |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 14        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


.. note:: Number of DB queries is much bigger for this request comparing with
          similar Liberty environment. The difference is in
          `keystone_authtoken` middleware (and, more specifically, its cache)
          usage. Although all environments that took part in the research had
          exactly the same `keystone_authtoken` middleware configuration,
          described in the test plan and containing `memcache_servers`
          parameter set up, Mitaka environments profiling shows that all
          OpenStack services that used `keystone_authtoken` middleware did not
          use the external Memcached cached token copy. All of them used
          Keystone API every time REST API request was coming to the OpenStack
          services. This behaviour needs to be investigated separately.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 39                 |
| implied_role_implied_role_id                                                                         |                    |
| FROM implied_role                                                                                    |                    |
| WHERE implied_role.prior_role_id = %(prior_role_id_1)s                                               |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 61                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 24                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 27                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 12                 |
| revocation_event_domain_id, revocation_event.project_id AS revocation_event_project_id,              |                    |
| revocation_event.user_id AS revocation_event_user_id, revocation_event.role_id AS                    |                    |
| revocation_event_role_id, revocation_event.trust_id AS revocation_event_trust_id,                    |                    |
| revocation_event.consumer_id AS revocation_event_consumer_id, revocation_event.access_token_id AS    |                    |
| revocation_event_access_token_id, revocation_event.issued_before AS revocation_event_issued_before,  |                    |
| revocation_event.expires_at AS revocation_event_expires_at, revocation_event.revoked_at AS           |                    |
| revocation_event_revoked_at, revocation_event.audit_id AS revocation_event_audit_id,                 |                    |
| revocation_event.audit_chain_id AS revocation_event_audit_chain_id                                   |                    |
| FROM revocation_event ORDER BY revocation_event.revoked_at                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 40                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 8                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %(name_1)s AND project.domain_id = %(domain_id_1)s                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 9                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 18                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 63                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 27                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 9                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 40                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
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
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 22                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 9                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 14                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 28                 |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 12                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 25                 |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 33                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 9                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 9                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 5                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 6                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone cached methods stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_token            | <keystone.token.persistence.core.PersistenceManager object at 0x7f76eae62c10>,                       |            | 6              |
|                       | 'c1613dbf55ac423fb5c0ae8833e4884b'                                                                   |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_revoke_tree      | <keystone.revoke.core.Manager object at 0x7f76ebf9a990>,                                             |            | 66             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f76ebfea850>, u'a7e61cc2e4634e8c9179257bdb8dcb47'       |            | 81             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f76ebf401d0>, u'141ab89993aa4d9fa645540dad1a3e2a' |            | 27             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_token            | <keystone.token.persistence.core.PersistenceManager object at 0x7f76eae62a10>,                       |            | 16             |
|                       | 'c1613dbf55ac423fb5c0ae8833e4884b'                                                                   |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f76ebfea850>, u'default'                                |            | 27             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_token            | <keystone.token.persistence.core.PersistenceManager object at 0x7f76eae629d0>,                       |            | 5              |
|                       | 'c1613dbf55ac423fb5c0ae8833e4884b'                                                                   |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f76ebfe9850>, u'a7e61cc2e4634e8c9179257bdb8dcb47'       |            | 6              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_token            | <keystone.token.persistence.core.PersistenceManager object at 0x7f76eae62a10>,                       |            | 5              |
|                       | 'e9d77e583df44f7ebf84de745882e722'                                                                   |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_token            | <keystone.token.persistence.core.PersistenceManager object at 0x7f76eae62c10>,                       |            | 1              |
|                       | 'e9d77e583df44f7ebf84de745882e722'                                                                   |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _validate_v3_token    | <keystone.token.provider.Manager object at 0x7f76ebf648d0>, {u'tenant': {u'domain': {u'id':          |            | 6              |
|                       | u'default', u'name': u'Default'}, u'id': u'87dfc2348604428590293a3e6ec1c62c', u'name': u'service'},  |            |                |
|                       | 'user_id': u'bb2514e4901d4682a8ebdedc13b8df83', 'expires': datetime.datetime(2016, 3, 29, 21, 26,    |            |                |
|                       | 35), u'token_data': {u'token': {u'methods': [u'password'], u'roles': [{u'id':                        |            |                |
|                       | u'bab7f95dd62e46d68d6aecca9d18c4fd', u'name': u'service'}], u'expires_at':                           |            |                |
|                       | u'2016-03-29T21:26:35.010736Z', u'project': {u'domain': {u'id': u'default', u'name': u'Default'},    |            |                |
|                       | u'id': u'87dfc2348604428590293a3e6ec1c62c', u'name': u'service'}, u'catalog': [{u'endpoints':        |            |                |
|                       | [{u'url': u'http://10.0.2.15:8776/v1/87dfc2348604428590293a3e6ec1c62c', u'interface': u'public',     |            |                |
|                       | u'region': u'RegionOne', u'region_id': u'RegionOne', u'id': u'56205029c0a1478cbd8c4fc075315746'},    |            |                |
|                       | {u'url': u'http://10.0.2.15:8776/v1/87dfc2348604428590293a3e6ec1c62c', u'interface': u'admin',       |            |                |
|                       | u'region': u'RegionOne', u'region_id': u'RegionOne', u'id': u'80de6747b5f14681a14ebcadcd1bfa3c'},    |            |                |
|                       | {u'url': u'http://10.0.2.15:8776/v1/87dfc2348604428590293a3e6ec1c62c', u'interface': u'internal',    |            |                |
|                       | u'region': u'RegionOne', u'region_id': u'RegionOne', u'id': u'cba6f65a146b4973ace876b38b3480b9'}],   |            |                |
|                       | u'type': u'volume', u'id': u'4ebaed7acb634017a6913526311d98e9', u'name': u'cinder'}, {u'endpoints':  |            |                |
|                       | [{u'url': u'http://10.0.2.15:8776/v2/87dfc2348604428590293a3e6ec1c62c', u'interface': u'public',     |            |                |
|                       | u'region': u'RegionOne', u'region_id': u'RegionOne', u'id': u'853305e44f5d4236b081a46e1e9b83af'},    |            |                |
|                       | {u'url': u'http://10.0.2.15:8776/v2/87dfc2348604428590293a3e6ec1c62c', u'interface': u'admin',       |            |                |
|                       | u'region': u'RegionOne', u'region_id': u'RegionOne', u'id': u'89fdb562d14e40e4ba01268ae79910c5'},    |            |                |
|                       | {u'url': u'http://10.0.2.15:8776/v2/87dfc2348604428590293a3e6ec1c62c', u'interface': u'internal',    |            |                |
|                       | u'region': u'RegionOne', u'region_id': u'RegionOne', u'id': u'b27a27f962e44d69939a30ef3cb6b2a3'}],   |            |                |
|                       | u'type': u'volumev2', u'id': u'4f1650e001bb49b1a995755b88812998', u'name': u'cinderv2'},             |            |                |
|                       | {u'endpoints': [{u'url': u'http://10.0.2.15:8774/v2/87dfc2348604428590293a3e6ec1c62c', u'interface': |            |                |
|                       | u'admin', u'region': u'RegionOne', u'region_id': u'RegionOne', u'id':                                |            |                |
|                       | u'605496c2c01549e09e3c3511d5d050c1'}, {u'url':                                                       |            |                |
|                       | u'http://10.0.2.15:8774/v2/87dfc2348604428590293a3e6ec1c62c', u'interface': u'internal', u'region':  |            |                |
|                       | u'RegionOne', u'region_id': u'RegionOne', u'id': u'a359f6aaf80643dd90fd5598f4cf0614'}, {u'url':      |            |                |
|                       | u'http://10.0.2.15:8774/v2/87dfc2348604428590293a3e6ec1c62c', u'interface': u'public', u'region':    |            |                |
|                       | u'RegionOne', u'region_id': u'RegionOne', u'id': u'f552054d19ca4cfe981ca02ff4558595'}], u'type':     |            |                |
|                       | u'compute_legacy', u'id': u'4fb62933662a4017ac2f8beb7239a7c5', u'name': u'nova_legacy'},             |            |                |
|                       | {u'endpoints': [{u'url': u'http://10.0.2.15:8774/v2.1/87dfc2348604428590293a3e6ec1c62c',             |            |                |
|                       | u'interface': u'internal', u'region': u'RegionOne', u'region_id': u'RegionOne', u'id':               |            |                |
|                       | u'21878ce4ff7d48a89f621675d89a0994'}, {u'url':                                                       |            |                |
|                       | u'http://10.0.2.15:8774/v2.1/87dfc2348604428590293a3e6ec1c62c', u'interface': u'public', u'region':  |            |                |
|                       | u'RegionOne', u'region_id': u'RegionOne', u'id': u'645b3a5079ae4ed68c61890659b0af96'}, {u'url':      |            |                |
|                       | u'http://10.0.2.15:8774/v2.1/87dfc2348604428590293a3e6ec1c62c', u'interface': u'admin', u'region':   |            |                |
|                       | u'RegionOne', u'region_id': u'RegionOne', u'id': u'b20358e6f0574a4abbefd7d9fea42d27'}], u'type':     |            |                |
|                       | u'compute', u'id': u'8c04194b75b846618a673b59a0a4bf3c', u'name': u'nova'}, {u'endpoints': [{u'url':  |            |                |
|                       | u'http://10.0.2.15:9292', u'interface': u'admin', u'region': u'RegionOne', u'region_id':             |            |                |
|                       | u'RegionOne', u'id': u'3f4f3c602e0c4b94aaef28d42f3fe1bc'}, {u'url': u'http://10.0.2.15:9292',        |            |                |
|                       | u'interface': u'internal', u'region': u'RegionOne', u'region_id': u'RegionOne', u'id':               |            |                |
|                       | u'610b5a73106b412a992ad987782b7cd0'}, {u'url': u'http://10.0.2.15:9292', u'interface': u'public',    |            |                |
|                       | u'region': u'RegionOne', u'region_id': u'RegionOne', u'id': u'f39bfd16ee7e43b7bc82fd78eb20a9c4'}],   |            |                |
|                       | u'type': u'image', u'id': u'a4d2690b9ad34c4ea4e2eafe12125496', u'name': u'glance'}, {u'endpoints':   |            |                |
|                       | [{u'url': u'http://10.0.2.15:8777', u'interface': u'public', u'region': u'RegionOne', u'region_id':  |            |                |
|                       | u'RegionOne', u'id': u'40f20ee570504169902791abf506a49c'}, {u'url': u'http://10.0.2.15:8777',        |            |                |
|                       | u'interface': u'internal', u'region': u'RegionOne', u'region_id': u'RegionOne', u'id':               |            |                |
|                       | u'49b66e88bdda4e648855b2c0e8b55227'}, {u'url': u'http://10.0.2.15:8777', u'interface': u'admin',     |            |                |
|                       | u'region': u'RegionOne', u'region_id': u'RegionOne', u'id': u'5f2f9f9a58064a04a449a170d176bce4'}],   |            |                |
|                       | u'type': u'metering', u'id': u'ac90aa229d7048adb18219359fbbd437', u'name': u'ceilometer'},           |            |                |
|                       | {u'endpoints': [{u'url': u'http://10.0.2.15:9696/', u'interface': u'public', u'region':              |            |                |
|                       | u'RegionOne', u'region_id': u'RegionOne', u'id': u'12dbac67dfd842929a73cc2da267a585'}, {u'url':      |            |                |
|                       | u'http://10.0.2.15:9696/', u'interface': u'admin', u'region': u'RegionOne', u'region_id':            |            |                |
|                       | u'RegionOne', u'id': u'b6f1f5f59a3649658a1c02c7c9be0e6b'}, {u'url': u'http://10.0.2.15:9696/',       |            |                |
|                       | u'interface': u'internal', u'region': u'RegionOne', u'region_id': u'RegionOne', u'id':               |            |                |
|                       | u'd4f8473ff3bc4ba6ad754c5b9ea6fe11'}], u'type': u'network', u'id':                                   |            |                |
|                       | u'e86e501b77344f35a4877f48f570f86a', u'name': u'neutron'}, {u'endpoints': [{u'url':                  |            |                |
|                       | u'http://10.0.2.15:5000/v2.0', u'interface': u'public', u'region': u'RegionOne', u'region_id':       |            |                |
|                       | u'RegionOne', u'id': u'32eedd79382e42a693ae4ae36104e257'}, {u'url': u'http://10.0.2.15:5000/v2.0',   |            |                |
|                       | u'interface': u'internal', u'region': u'RegionOne', u'region_id': u'RegionOne', u'id':               |            |                |
|                       | u'6c623f00190348aea66a29e86e980449'}, {u'url': u'http://10.0.2.15:35357/v2.0', u'interface':         |            |                |
|                       | u'admin', u'region': u'RegionOne', u'region_id': u'RegionOne', u'id':                                |            |                |
|                       | u'c4f3f0e4a90542e6af07805a9570a91d'}], u'type': u'identity', u'id':                                  |            |                |
|                       | u'f0dc03fd61e84f338abd2b40371a767a', u'name': u'keystone'}], u'user': {u'domain': {u'id':            |            |                |
|                       | u'default', u'name': u'Default'}, u'id': u'bb2514e4901d4682a8ebdedc13b8df83', u'name': u'neutron'},  |            |                |
|                       | u'audit_ids': [u'1rgcCrgFQJqlLiCoeniFUQ'], u'issued_at': u'2016-03-29T20:26:35.010777Z'}}, u'user':  |            |                |
|                       | {u'domain': {u'id': u'default', u'name': u'Default'}, u'id': u'bb2514e4901d4682a8ebdedc13b8df83',    |            |                |
|                       | u'name': u'neutron'}, u'key': u'e9d77e583df44f7ebf84de745882e722', u'token_version': u'v3.0', 'id':  |            |                |
|                       | u'e9d77e583df44f7ebf84de745882e722', 'trust_id': None, u'metadata': {u'roles':                       |            |                |
|                       | [u'bab7f95dd62e46d68d6aecca9d18c4fd']}}                                                              |            |                |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f76ebfbf1d0>, u'141ab89993aa4d9fa645540dad1a3e2a' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f76ebfe9850>, u'default'                                |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Service list request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 84        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 619       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 31        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 207       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 53        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 412       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 51        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 393       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 19        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


.. note:: Number of DB queries is much bigger for this request comparing with
          similar Liberty environment. The difference is in
          `keystone_authtoken` middleware (and, more specifically, its cache)
          usage. Although all environments that took part in the research had
          exactly the same `keystone_authtoken` middleware configuration,
          described in the test plan and containing `memcache_servers`
          parameter set up, Mitaka environments profiling shows that all
          OpenStack services that used `keystone_authtoken` middleware did not
          use the external Memcached cached token copy. All of them used
          Keystone API every time REST API request was coming to the OpenStack
          services. This behaviour needs to be investigated separately.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 9                  |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 40                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 10                 |
| implied_role_implied_role_id                                                                         |                    |
| FROM implied_role                                                                                    |                    |
| WHERE implied_role.prior_role_id = %(prior_role_id_1)s                                               |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 5                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s                        |                    |
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
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 16                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 15                 |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 11                 |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 24                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 12                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 18                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 12                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 9                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %(name_1)s AND project.domain_id = %(domain_id_1)s                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 27                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 4                  |
| revocation_event_domain_id, revocation_event.project_id AS revocation_event_project_id,              |                    |
| revocation_event.user_id AS revocation_event_user_id, revocation_event.role_id AS                    |                    |
| revocation_event_role_id, revocation_event.trust_id AS revocation_event_trust_id,                    |                    |
| revocation_event.consumer_id AS revocation_event_consumer_id, revocation_event.access_token_id AS    |                    |
| revocation_event_access_token_id, revocation_event.issued_before AS revocation_event_issued_before,  |                    |
| revocation_event.expires_at AS revocation_event_expires_at, revocation_event.revoked_at AS           |                    |
| revocation_event_revoked_at, revocation_event.audit_id AS revocation_event_audit_id,                 |                    |
| revocation_event.audit_chain_id AS revocation_event_audit_chain_id                                   |                    |
| FROM revocation_event ORDER BY revocation_event.revoked_at                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 33                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 22                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 9                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 5                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 9                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 12                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 19                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 5                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 9                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 6                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 12                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone cached methods stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f2e5728b9d0>, u'a465ecd9f7004c38b30792a07b363b2c'       |            | 6              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f2e57262350>, u'31c541984f48440ab8753d11d84e58ca' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f2e5728b9d0>, u'default'                                |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Token issue request stats
~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 39        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 448       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 14        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 179       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 25        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 269       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 24        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 263       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 1         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 6         |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


.. note:: Number of DB queries is much bigger for this request comparing with
          similar Liberty environment. The difference is in
          `keystone_authtoken` middleware (and, more specifically, its cache)
          usage. Although all environments that took part in the research had
          exactly the same `keystone_authtoken` middleware configuration,
          described in the test plan and containing `memcache_servers`
          parameter set up, Mitaka environments profiling shows that all
          OpenStack services that used `keystone_authtoken` middleware did not
          use the external Memcached cached token copy. All of them used
          Keystone API every time REST API request was coming to the OpenStack
          services. This behaviour needs to be investigated separately.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 20                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 40                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 15                 |
| implied_role_implied_role_id                                                                         |                    |
| FROM implied_role                                                                                    |                    |
| WHERE implied_role.prior_role_id = %(prior_role_id_1)s                                               |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 5                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s                        |                    |
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
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 16                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 15                 |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 11                 |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 24                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 12                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 18                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 27                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 9                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %(name_1)s AND project.domain_id = %(domain_id_1)s                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 27                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 4                  |
| revocation_event_domain_id, revocation_event.project_id AS revocation_event_project_id,              |                    |
| revocation_event.user_id AS revocation_event_user_id, revocation_event.role_id AS                    |                    |
| revocation_event_role_id, revocation_event.trust_id AS revocation_event_trust_id,                    |                    |
| revocation_event.consumer_id AS revocation_event_consumer_id, revocation_event.access_token_id AS    |                    |
| revocation_event_access_token_id, revocation_event.issued_before AS revocation_event_issued_before,  |                    |
| revocation_event.expires_at AS revocation_event_expires_at, revocation_event.revoked_at AS           |                    |
| revocation_event_revoked_at, revocation_event.audit_id AS revocation_event_audit_id,                 |                    |
| revocation_event.audit_chain_id AS revocation_event_audit_chain_id                                   |                    |
| FROM revocation_event ORDER BY revocation_event.revoked_at                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 33                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 22                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 9                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 5                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 9                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 12                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 19                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 5                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 10                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone cached methods stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f2e5728b9d0>, u'a465ecd9f7004c38b30792a07b363b2c'       |            | 3              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f2e57262350>, u'31c541984f48440ab8753d11d84e58ca' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f2e5728b9d0>, u'default'                                |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

User list request stats
~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 94        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 700       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 31        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 240       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 63        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 460       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 61        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 450       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 10        |
+--------------------------------------------------------------+-----------+

.. note:: (*) OSprofiler uses specific SQLalchemy cursor events to track
          what's going on with the DB layer. This number includes non-real
          DB requests "SELECT 1", processed by SQLalchemy itself to make
          sure that connection to the database is still in place.


.. note:: Number of DB queries is much bigger for this request comparing with
          similar Liberty environment. The difference is in
          `keystone_authtoken` middleware (and, more specifically, its cache)
          usage. Although all environments that took part in the research had
          exactly the same `keystone_authtoken` middleware configuration,
          described in the test plan and containing `memcache_servers`
          parameter set up, Mitaka environments profiling shows that all
          OpenStack services that used `keystone_authtoken` middleware did not
          use the external Memcached cached token copy. All of them used
          Keystone API every time REST API request was coming to the OpenStack
          services. This behaviour needs to be investigated separately.


**Keystone DB queries outliers**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 20                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 40                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 15                 |
| implied_role_implied_role_id                                                                         |                    |
| FROM implied_role                                                                                    |                    |
| WHERE implied_role.prior_role_id = %(prior_role_id_1)s                                               |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 5                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s                        |                    |
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
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 16                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 16                 |
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
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 11                 |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 11                 |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 24                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 12                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 18                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 13                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 9                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %(name_1)s AND project.domain_id = %(domain_id_1)s                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 27                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 4                  |
| revocation_event_domain_id, revocation_event.project_id AS revocation_event_project_id,              |                    |
| revocation_event.user_id AS revocation_event_user_id, revocation_event.role_id AS                    |                    |
| revocation_event_role_id, revocation_event.trust_id AS revocation_event_trust_id,                    |                    |
| revocation_event.consumer_id AS revocation_event_consumer_id, revocation_event.access_token_id AS    |                    |
| revocation_event_access_token_id, revocation_event.issued_before AS revocation_event_issued_before,  |                    |
| revocation_event.expires_at AS revocation_event_expires_at, revocation_event.revoked_at AS           |                    |
| revocation_event_revoked_at, revocation_event.audit_id AS revocation_event_audit_id,                 |                    |
| revocation_event.audit_chain_id AS revocation_event_audit_chain_id                                   |                    |
| FROM revocation_event ORDER BY revocation_event.revoked_at                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 33                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 22                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 9                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 5                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 18                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 12                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra                                                   |                    |
| FROM endpoint                                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT endpoint.id AS endpoint_id, endpoint.legacy_endpoint_id AS endpoint_legacy_endpoint_id,       | 19                 |
| endpoint.interface AS endpoint_interface, endpoint.region_id AS endpoint_region_id,                  |                    |
| endpoint.service_id AS endpoint_service_id, endpoint.url AS endpoint_url, endpoint.enabled AS        |                    |
| endpoint_enabled, endpoint.extra AS endpoint_extra, service_1.id AS service_1_id, service_1.type AS  |                    |
| service_1_type, service_1.enabled AS service_1_enabled, service_1.extra AS service_1_extra           |                    |
| FROM endpoint LEFT OUTER JOIN service AS service_1 ON service_1.id = endpoint.service_id             |                    |
| WHERE endpoint.enabled = true                                                                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 6                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 7                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 9                  |
| federated_user.idp_id AS federated_user_idp_id, federated_user.protocol_id AS                        |                    |
| federated_user_protocol_id, federated_user.unique_id AS federated_user_unique_id,                    |                    |
| federated_user.display_name AS federated_user_display_name, anon_1.user_id AS anon_1_user_id         |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| federated_user ON anon_1.user_id = federated_user.user_id ORDER BY anon_1.user_id                    |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 5                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone cached methods stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f2e5728b9d0>, u'a465ecd9f7004c38b30792a07b363b2c'       |            | 6              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f2e57262350>, u'31c541984f48440ab8753d11d84e58ca' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f2e5728b9d0>, u'default'                                |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
