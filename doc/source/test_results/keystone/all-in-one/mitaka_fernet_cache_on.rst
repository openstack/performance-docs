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
| Total (*) Keystone DB queries count                          | 398       |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 4107      |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 152       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 1477      |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 246       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 2630      |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 246       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 2630      |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 29                 |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 18                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 42                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 19                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 4                  |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 12                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 24                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 29                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 52                 |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 24                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 19                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
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
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 29                 |
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
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 15                 |
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
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 4                  |
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

**Keystone cached methods stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f48552a1350>, u'4ed859be7342465c945448395bac826f' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f48552a2350>, u'4ed859be7342465c945448395bac826f' |            | 9              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f48552ca9d0>, u'default'                                |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f48552cb9d0>, u'default'                                |            | 9              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f48552cb9d0>, '267e50e2487c46cdb60c1ec82adce5f9'        |            | 27             |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f48552ca9d0>, u'267e50e2487c46cdb60c1ec82adce5f9'       |            | 6              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Server create request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 2108      |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 19003     |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 807       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 6813      |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 1301      |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 12190     |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 1301      |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 12190     |
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
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 16                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user INNER JOIN local_user ON user.id = local_user.user_id                                      |                    |
| WHERE local_user.name = %(name_1)s AND local_user.domain_id = %(domain_id_1)s) AS anon_1 INNER JOIN  |                    |
| local_user ON anon_1.user_id = local_user.user_id ORDER BY anon_1.user_id                            |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 27                 |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 27                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 18                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 26                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 26                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 4                  |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 12                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 23                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 26                 |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 196                |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 50                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 18                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 18                 |
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
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 18                 |
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
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 16                 |
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

**Keystone cached methods stats**

+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations**          | **args**                                                                                             | **kwargs** | **Times used** |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain                     | <keystone.resource.core.Manager object at 0x7f45a5f18850>, u'default'                                |            | 2              |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| _get_revoke_tree               | <keystone.revoke.core.Manager object at 0x7f45a5ec9990>,                                             |            | 64             |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project                    | <keystone.resource.core.Manager object at 0x7f45a5f19850>, '2dc93f73479940d0b39ce2e4c52c108c'        |            | 106            |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain                     | <keystone.resource.core.Manager object at 0x7f45a5f19850>, u'default'                                |            | 160            |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role                       | <keystone.assignment.core.RoleManager object at 0x7f45a5e6f1d0>, u'c76d7947edb44079b7fca0b376674315' |            | 36             |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role                       | <keystone.assignment.core.RoleManager object at 0x7f45a5eee1d0>, u'3481c11394a64189bafc60551e1ee25c' |            | 2              |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project                    | <keystone.resource.core.Manager object at 0x7f45a5f18850>, u'1f093e18f4ab4318bdb2876a03d81811'       |            | 6              |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project                    | <keystone.resource.core.Manager object at 0x7f45a5f19850>, '1f093e18f4ab4318bdb2876a03d81811'        |            | 108            |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user                       | <keystone.identity.core.Manager object at 0x7f45a6217a50>, 'a74255d40f634b9d8c83e7fb0959c082'        |            | 10             |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7f45a6001610>, 'a74255d40f634b9d8c83e7fb0959c082',     |            | 10             |
|                                | '2dc93f73479940d0b39ce2e4c52c108c'                                                                   |            |                |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_roles_for_user_and_project | <keystone.assignment.core.Manager object at 0x7f45a6001610>, 'b4a6b5f09b9c4b57a582b16537f4a976',     |            | 27             |
|                                | '1f093e18f4ab4318bdb2876a03d81811'                                                                   |            |                |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role                       | <keystone.assignment.core.RoleManager object at 0x7f45a5e6f1d0>, u'3481c11394a64189bafc60551e1ee25c' |            | 66             |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_user                       | <keystone.identity.core.Manager object at 0x7f45a6217a50>, 'b4a6b5f09b9c4b57a582b16537f4a976'        |            | 27             |
+--------------------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Service list request stats
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 110       |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 1048      |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 40        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 389       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 70        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 659       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 70        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 659       |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 4                  |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 27                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 18                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 5                  |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 17                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 4                  |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 12                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 23                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 5                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 4                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
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
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 16                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 13                 |
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
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f48552a1350>, u'4ed859be7342465c945448395bac826f' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f48552a2350>, u'4ed859be7342465c945448395bac826f' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f48552ca9d0>, u'default'                                |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f48552cb9d0>, u'default'                                |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f48552cb9d0>, '267e50e2487c46cdb60c1ec82adce5f9'        |            | 3              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f48552ca9d0>, u'267e50e2487c46cdb60c1ec82adce5f9'       |            | 6              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

Token issue request stats
~~~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 37        |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 308       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 13        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 120       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 24        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 188       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 24        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 188       |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 9                  |
| password.password AS password_password                                                               |                    |
| FROM password                                                                                        |                    |
| WHERE %(param_1)s = password.local_user_id                                                           |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 27                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = false                                     |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT revocation_event.id AS revocation_event_id, revocation_event.domain_id AS                     | 18                 |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 8                  |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 17                 |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 4                  |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 12                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 23                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
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
| SELECT project.id AS project_id, project.name AS project_name, project.domain_id AS                  | 9                  |
| project_domain_id, project.description AS project_description, project.enabled AS project_enabled,   |                    |
| project.extra AS project_extra, project.parent_id AS project_parent_id, project.is_domain AS         |                    |
| project_is_domain                                                                                    |                    |
| FROM project                                                                                         |                    |
| WHERE project.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 8                  |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
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
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 16                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 10                 |
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
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 19                 |
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
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f48552a1350>, u'4ed859be7342465c945448395bac826f' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f48552ca9d0>, u'267e50e2487c46cdb60c1ec82adce5f9'       |            | 3              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f48552ca9d0>, u'default'                                |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+

User list request stats
~~~~~~~~~~~~~~~~~~~~~~~

**Control plane request overlook**

+--------------------------------------------------------------+-----------+
| **Metric**                                                   | **Value** |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries count                          | 120       |
+--------------------------------------------------------------+-----------+
| Total (*) Keystone DB queries time spent, ms                 | 906       |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries count          | 40        |
+--------------------------------------------------------------+-----------+
| Infrastructure (SELECT 1) Keystone DB queries time spent, ms | 270       |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries count                               | 80        |
+--------------------------------------------------------------+-----------+
| Real Keystone DB queries time spent, ms                      | 636       |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries count                             | 80        |
+--------------------------------------------------------------+-----------+
| SELECT Keystone DB queries time spent, ms                    | 636       |
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
| SELECT password.id AS password_id, password.local_user_id AS password_local_user_id,                 | 14                 |
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
| SELECT federated_user.id AS federated_user_id, federated_user.user_id AS federated_user_user_id,     | 9                  |
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
| SELECT `group`.id AS group_id, `group`.name AS group_name, `group`.domain_id AS group_domain_id,     | 11                 |
| `group`.description AS group_description, `group`.extra AS group_extra                               |                    |
| FROM `group` INNER JOIN user_group_membership ON `group`.id = user_group_membership.group_id         |                    |
| WHERE user_group_membership.user_id = %(user_id_1)s                                                  |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT assignment.type AS assignment_type, assignment.actor_id AS assignment_actor_id,               | 4                  |
| assignment.target_id AS assignment_target_id, assignment.role_id AS assignment_role_id,              |                    |
| assignment.inherited AS assignment_inherited                                                         |                    |
| FROM assignment                                                                                      |                    |
| WHERE assignment.actor_id IN (%(actor_id_1)s) AND assignment.target_id IN (%(target_id_1)s) AND      |                    |
| assignment.type IN (%(type_1)s) AND assignment.inherited = true                                      |                    |
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
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 12                 |
| service.extra AS service_extra                                                                       |                    |
| FROM service                                                                                         |                    |
| WHERE service.id = %(param_1)s                                                                       |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service_provider.id AS service_provider_id, service_provider.enabled AS                       | 23                 |
| service_provider_enabled, service_provider.description AS service_provider_description,              |                    |
| service_provider.auth_url AS service_provider_auth_url, service_provider.sp_url AS                   |                    |
| service_provider_sp_url, service_provider.relay_state_prefix AS service_provider_relay_state_prefix  |                    |
| FROM service_provider                                                                                |                    |
| WHERE service_provider.enabled = true                                                                |                    |
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
| SELECT local_user.id AS local_user_id, local_user.user_id AS local_user_user_id,                     | 5                  |
| local_user.domain_id AS local_user_domain_id, local_user.name AS local_user_name, anon_1.user_id AS  |                    |
| anon_1_user_id                                                                                       |                    |
| FROM (SELECT user.id AS user_id                                                                      |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s) AS anon_1 INNER JOIN local_user ON anon_1.user_id = local_user.user_id  |                    |
| ORDER BY anon_1.user_id                                                                              |                    |
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
| SELECT role.id AS role_id, role.name AS role_name, role.domain_id AS role_domain_id, role.extra AS   | 14                 |
| role_extra                                                                                           |                    |
| FROM role                                                                                            |                    |
| WHERE role.id = %(param_1)s                                                                          |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT service.id AS service_id, service.type AS service_type, service.enabled AS service_enabled,   | 11                 |
| service.extra AS service_extra, endpoint_1.id AS endpoint_1_id, endpoint_1.legacy_endpoint_id AS     |                    |
| endpoint_1_legacy_endpoint_id, endpoint_1.interface AS endpoint_1_interface, endpoint_1.region_id AS |                    |
| endpoint_1_region_id, endpoint_1.service_id AS endpoint_1_service_id, endpoint_1.url AS              |                    |
| endpoint_1_url, endpoint_1.enabled AS endpoint_1_enabled, endpoint_1.extra AS endpoint_1_extra       |                    |
| FROM service LEFT OUTER JOIN endpoint AS endpoint_1 ON service.id = endpoint_1.service_id            |                    |
| WHERE service.enabled = true                                                                         |                    |
|                                                                                                      |                    |
| |                                                                                                    |                    |
+------------------------------------------------------------------------------------------------------+--------------------+
| SELECT user.id AS user_id, user.enabled AS user_enabled, user.extra AS user_extra,                   | 24                 |
| user.default_project_id AS user_default_project_id                                                   |                    |
| FROM user                                                                                            |                    |
| WHERE user.id = %(param_1)s                                                                          |                    |
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
| SELECT implied_role.prior_role_id AS implied_role_prior_role_id, implied_role.implied_role_id AS     | 4                  |
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

**Keystone cached methods stats**

+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| **Cached operations** | **args**                                                                                             | **kwargs** | **Times used** |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f48552a1350>, u'4ed859be7342465c945448395bac826f' |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_role              | <keystone.assignment.core.RoleManager object at 0x7f48552a2350>, u'4ed859be7342465c945448395bac826f' |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f48552ca9d0>, u'default'                                |            | 2              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_domain            | <keystone.resource.core.Manager object at 0x7f48552cb9d0>, u'default'                                |            | 1              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f48552cb9d0>, '267e50e2487c46cdb60c1ec82adce5f9'        |            | 3              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
| get_project           | <keystone.resource.core.Manager object at 0x7f48552ca9d0>, u'267e50e2487c46cdb60c1ec82adce5f9'       |            | 6              |
+-----------------------+------------------------------------------------------------------------------------------------------+------------+----------------+
