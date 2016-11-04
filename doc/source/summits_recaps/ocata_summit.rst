Ocata OpenStack summit recap
============================

During OpenStack Ocata Summit at Barcelona our team had several sessions and
cross-teams discussions. This page contains links to the resources and
related sessions recordings, that might be interesting for Performance Team
members and newcomers.

Chasing 1000 nodes scale
------------------------

This session is dedicated to our 1000 nodes emulation experiment we have done
during Newton development cycle time frame. This test case aims to gain
information about what resources and configuration are necessary for OpenStack
control plane on large enough scale.

Useful links:

* :ref:`1000_nodes`
* :ref:`1000_nodes_report`
* :ref:`1000_nodes_fake_driver_report`
* `Chasing 1000 nodes scale summit video`_

What Has Been Done During Newton Cycle and Ocata Planning
---------------------------------------------------------

Results sharing / future planning session. All results and plans are logged to
the `Newton results / Ocata planning etherpad`_. Plans for Ocata development
timeframe includes Mirantis, Inria, IBM and Red Hat participation.

OpenStack Scale and Performance Testing with Browbeat
-----------------------------------------------------

Scalability and performance testing toolkit presentation by Red Hat. In this
talk core Browbeat developers share how you can leverage Browbeat tool for your
OpenStack deployment along with a demonstration showcasing some of the useful
features. You can go through this presentation with `Browbeat session summit
video`_.

Massively Distributed Clouds Working Group
------------------------------------------

This is recently created WG dedicated to solve questions regarding the distributed
OpenStack clouds - including questions about what performance and scalability
the operator could expect from such deployments. All information about this
group can be found using the following links:

* `MDC Wiki page`_
* `MDC summit etherpad`_

Large Deployments Team meetup
-----------------------------

During LDT working group summit meetup we collected a feedback from
operators (listed in the `LDT session etherpad`_).

Architecture Working Group
--------------------------

Architecture WG is a new group dedicated to be recognized forum of expertise
on the design and architecture of OpenStack and to provide guidance and resources
to the Technical Committee and the entire OpenStack community on architectural
matters. This group is going to use similar methodologies with Performance Team
help for architectural concepts verification and testing, as well as results
presentation.

Useful links:

* `Architecture WG summit etherpad`_
* `Architecture WG proposal`_

QA: destructive testing
-----------------------

During the design summit there was a separated QA session dedicated to
destructive testing, and tool developed originally under Performance Team
umbrella (os-faults library) was assumed to be #1 solution for those types
of tests.

* `Destructive testing summit etherpad`_
* `OS-faults documentation`_

Cross Project Workshops: Rolling Upgrades, and the Road to Zero-Downtime
------------------------------------------------------------------------

During this cross-project session Performance Team's testing approach for
reliability testing (when we're injecting the destructive hooks) was mentioned
as one of the opportunities for upgrades testing (when we're injecting the
upgrades process in the middle of testing and calculate exactly the same
metrics we collected for reliability testing - mean time to recover, service
downtime, performance degradation, etc.): `upgrades summit etherpad`_.

.. _Chasing 1000 nodes scale summit video: https://www.youtube.com/watch?v=XURkQ3biF6w
.. _Newton results / Ocata planning etherpad: https://etherpad.openstack.org/p/ocata-performance-team
.. _Browbeat session summit video: https://www.youtube.com/watch?v=ch_rCyGQhYM
.. _MDC Wiki page: https://wiki.openstack.org/wiki/Massively_Distributed_Clouds
.. _MDC summit etherpad: https://etherpad.openstack.org/p/massively_distribute-barcelona_working_sessions
.. _LDT session etherpad: https://etherpad.openstack.org/p/BCN-Large-Deployments-Team
.. _Architecture WG summit etherpad: https://etherpad.openstack.org/p/BCN-architecture-wg
.. _Architecture WG proposal: https://etherpad.openstack.org/p/arch-wg-draft
.. _Destructive testing summit etherpad: https://etherpad.openstack.org/p/ocata-qa-destructive-testing
.. _OS-faults documentation: http://os-faults.readthedocs.io/en/latest/usage.html
.. _upgrades summit etherpad: https://etherpad.openstack.org/p/ocata-xp-upgrades
