Running profiling against Mitaka Keystone (UUID tokens, cache turned off)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents::

Parameters
~~~~~~~~~~

=========================== ===========
Parameter name              Value
=========================== ===========
OpenStack release           Mitaka
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
| Total (*) Keystone DB queries count                          | 152       |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 1348      |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 65        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 551       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 87        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 797       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 85        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 781       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 16        |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 5                  |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 25                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 13                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 5                  |
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
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 20                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 5                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 43                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 17                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 5                  |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
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
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 3                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
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
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 16                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 14                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
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
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 9                  |
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
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 3                  |
| implied_role_implied_role_id                                                                         |                    |
| FROM implied_role                                                                                    |                    |
| WHERE implied_role.prior_role_id = %(prior_role_id_1)s                                               |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 20                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
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
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 17                 |
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


Server create request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 1670      |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 14784     |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 712       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 5853      |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 958       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 8931      |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 956       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 8908      |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 23        |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 88                 |
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
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 69                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 24                 |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 5                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 75                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 3                  |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 12                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 22                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
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
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 50                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 33                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 16                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 51                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 87                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 22                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 26                 |
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
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 17                 |
| implied_role_implied_role_id                                                                         |                    |
| FROM implied_role                                                                                    |                    |
| WHERE implied_role.prior_role_id = %(prior_role_id_1)s                                               |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 4                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
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
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 12                 |
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


Service list request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 104       |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 945       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 41        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 346       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 63        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 599       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 61        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 588       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 11        |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 13                 |
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
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 69                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 24                 |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 11                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 32                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 5                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 75                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 3                  |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 14                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 11                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
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
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 16                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 15                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 3                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 51                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 87                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 15                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 74                 |
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
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 17                 |
| implied_role_implied_role_id                                                                         |                    |
| FROM implied_role                                                                                    |                    |
| WHERE implied_role.prior_role_id = %(prior_role_id_1)s                                               |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 32                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 31                 |
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
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 14                 |
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


Token issue request stats
~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 49        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 324       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 19        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 121       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 30        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 203       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 29        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 197       |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 13                 |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 10                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 69                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 24                 |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 11                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 32                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 5                  |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 11                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 3                  |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 14                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 14                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
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
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 16                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 15                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 3                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s                        |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 51                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 87                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 15                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 74                 |
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
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 17                 |
| implied_role_implied_role_id                                                                         |                    |
| FROM implied_role                                                                                    |                    |
| WHERE implied_role.prior_role_id = %(prior_role_id_1)s                                               |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 4                  |
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


User list request stats
~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 114       |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 798       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 41        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 267       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 73        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 531       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 71        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 511       |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries count                             | 2         |
+--------------------------------------------------------------+-----------+
| INSERT Keystone DB queries time spent, ms                    | 20        |
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
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 8                  |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 5                  |
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
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 9                  |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 17                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 12                 |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 22                 |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 15                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 32                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 8                  |
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
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 8                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.name = %(name_1)s AND project.domain_id = %(domain_id_1)s                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT token.id AS token_id, token.expires AS token_expires, token.extra AS token_extra, token.valid | 69                 |
| AS token_valid, token.user_id AS token_user_id, token.trust_id AS token_trust_id                     |                    |
| FROM token                                                                                           |                    |
| WHERE token.id = %(param_1)s                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 9                  |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 87                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 3                  |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 11                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 14                 |
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
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 17                 |
| implied_role_implied_role_id                                                                         |                    |
| FROM implied_role                                                                                    |                    |
| WHERE implied_role.prior_role_id = %(prior_role_id_1)s                                               |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+

**Keystone DB queries with multi JOINs inside**

+------------------------------------------------------------------------------------------------------+--------------------+
| **DB query**                                                                                         | **Time spent, ms** |
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
