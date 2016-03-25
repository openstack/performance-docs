
.. _Measuring_performance_of_docker_registry:

***************************************************
Results of measuring performance of Docker Registry
***************************************************

:Abstract:

  This document includes performance test results of `Docker Registry2`_ service
  as a repository of docker images. All test have been performed regarding
  :ref:`Measuring_performance_of_container_repositories`


Environment description
=======================
Hardware configuration of each server
-------------------------------------

.. table:: Description of servers hardware

  +-------+----------------+------------------------+------------------------+
  |server |name            |728998-comp-disk-228    |728998-comp-disk-227    |
  |       +----------------+------------------------+------------------------+
  |       |role            |test_tool               |registry                |
  |       +----------------+------------------------+------------------------+
  |       |vendor,model    |HP,DL380 Gen9           |HP,DL380 Gen9           |
  |       +----------------+------------------------+------------------------+
  |       |operating_system| | 3.13.0-76-generic    | | 3.13.0-76-generic    |
  |       |                | | Ubuntu-trusty        | | Ubuntu-trusty        |
  |       |                | | x86_64               | | x86_64               |
  +-------+----------------+------------------------+------------------------+
  |CPU    |vendor,model    |Intel,E5-2680 v3        |Intel,E5-2680 v3        |
  |       +----------------+------------------------+------------------------+
  |       |processor_count |2                       |2                       |
  |       +----------------+------------------------+------------------------+
  |       |core_count      |12                      |12                      |
  |       +----------------+------------------------+------------------------+
  |       |frequency_MHz   |2500                    |2500                    |
  +-------+----------------+------------------------+------------------------+
  |RAM    |vendor,model    |HP,752369-081           |HP,752369-081           |
  |       +----------------+------------------------+------------------------+
  |       |amount_MB       |262144                  |262144                  |
  +-------+----------------+------------------------+------------------------+
  |NETWORK|interface_name  |p1p1                    |p1p1                    |
  |       +----------------+------------------------+------------------------+
  |       |vendor,model    |Intel,X710 Dual Port    |Intel,X710 Dual Port    |
  |       +----------------+------------------------+------------------------+
  |       |bandwidth       |10G                     |10G                     |
  +-------+----------------+------------------------+------------------------+
  |STORAGE|dev_name        |/dev/sda                |/dev/sda                |
  |       +----------------+------------------------+------------------------+
  |       |vendor,model    | | raid10 - HP P840     | | raid10 - HP P840     |
  |       |                | | 12 disks EH0600JEDHE | | 12 disks EH0600JEDHE |
  |       +----------------+------------------------+------------------------+
  |       |SSD/HDD         |HDD                     |HDD                     |
  |       +----------------+------------------------+------------------------+
  |       |size            | 3,6TB                  | 3,6TB                  |
  +-------+----------------+------------------------+------------------------+

Network scheme and part of configuration of hardware network switches
---------------------------------------------------------------------
Network scheme of the environment:

.. image:: Network_Scheme.png
   :alt: Network Scheme of the environment

Here is the part of switch configuration for each switch port which connected to
p1p1 interface of a server:

.. code:: bash

   switchport mode trunk
   switchport trunk native vlan 600
   switchport trunk allowed vlan 600-602,630-649
   spanning-tree port type edge trunk
   spanning-tree bpduguard enable
   no snmp trap link-status

Software configuration of the DockerRegistry service
----------------------------------------------------
Installation of Registry2:
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: bash

  echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list
  apt-get update && apt-get -y install docker-engine
  service docker restart
  docker run -d -p 5000:5000 --name registry registry:2

.. table:: Versions of some software

  +-----------+------------------+
  |Software   |Version           |
  +===========+==================+
  |Ubuntu     |Ubuntu 14.04.3 LTS|
  +-----------+------------------+
  |Registry   |                  |
  +-----------+------------------+

Operating system configuration:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can find outputs of some commands and /etc folder in the following archive:

:download:`server_description_of_728998-comp-disk-227.tar.gz <configs/server_description_of_728998-comp-disk-227.tar.gz>`

Software configuration of the node with test tool
-------------------------------------------------
Test tool:
^^^^^^^^^^
Firstly we need to install docker-engine:

.. code:: bash

  echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list
  apt-get update && apt-get -y install docker-engine
  echo DOCKER_OPTS=\"--insecure-registry 172.20.9.16:5000\" >> /etc/default/docker
  service docker restart

We use Python2.7 and
:ref:`Script for collecting performance metrics of docker repository` with
:ref:`Proposed docker file` to perform the tests. The image size is a sum of
layers:

.. code:: bash

  IMAGE               CREATED              CREATED BY                                      SIZE                COMMENT
  93333b8ed564        About a minute ago   /bin/sh -c #(nop) CMD ["/bin/sh" "-c" "/usr/s   0 B
  35d8142196c0        About a minute ago   /bin/sh -c #(nop) EXPOSE 80/tcp                 0 B
  3a63f30ab247        About a minute ago   /bin/sh -c apt-get install -y nginx             18.14 MB
  97434d46f197        2 days ago           /bin/sh -c #(nop) CMD ["/bin/bash"]             0 B
  <missing>           2 days ago           /bin/sh -c sed -i 's/^#\s*\(deb.*universe\)$/   1.895 kB
  <missing>           2 days ago           /bin/sh -c set -xe   && echo '#!/bin/sh' > /u   194.5 kB
  <missing>           2 days ago           /bin/sh -c #(nop) ADD file:e01d51d39ea04c8efb   187.8 MB

It means that DATA_SIZE=206.13 MB

.. table:: Versions of some software

  +-----------+------------------+
  |Software   |Version           |
  +===========+==================+
  |Ubuntu     |Ubuntu 14.04.3 LTS|
  +-----------+------------------+
  |Docker     |1.10              |
  +-----------+------------------+

Operating system:
^^^^^^^^^^^^^^^^^
You can find outputs of some commands and /etc folder in the following archive:
:download:`server_description_of_728997-comp-disk-228.tar.gz <configs/server_description_of_728997-comp-disk-228.tar.gz>`

Testing process
===============
1.
  Registry2 was installed on top of 728998-comp-disk-227 server as described in
  `Installation of Registry2:`_ section.

2.
  The values of the variables in test-repo.py script was changed:
  iterations = 1000
  concurrency = 1
  repo_address = "172.20.9.16:5000"

3.
  The following command was executed to perform the tests:

  .. code:: bash

    sudo python test-repo.py

4.
  push_results.csv and pull_results.csv was saved in persistent folder.

5.
  The steps from 1 to 4 was repeated with the following values of the
  concurrency parameters: 1,10,30,50,100

As a result of this part we got the following CSV files:

:download:`PUSH_TIME(CONCURRENCY=1) <./results/registry-1000-1/push_results.csv>`
:download:`PUSH_TIME(CONCURRENCY=10) <./results/registry-1000-10/push_results.csv>`
:download:`PUSH_TIME(CONCURRENCY=30) <./results/registry-1000-30/push_results.csv>`
:download:`PUSH_TIME(CONCURRENCY=50) <./results/registry-1000-50/push_results.csv>`
:download:`PUSH_TIME(CONCURRENCY=100) <./results/registry-1000-100/push_results.csv>`
:download:`PULL_TIME(CONCURRENCY=1) <./results/registry-1000-1/pull_results.csv>`
:download:`PULL_TIME(CONCURRENCY=10) <./results/registry-1000-10/pull_results.csv>`
:download:`PULL_TIME(CONCURRENCY=30) <./results/registry-1000-30/pull_results.csv>`
:download:`PULL_TIME(CONCURRENCY=50) <./results/registry-1000-50/pull_results.csv>`
:download:`PULL_TIME(CONCURRENCY=100) <./results/registry-1000-100/pull_results.csv>`

Results
=======
Push action results
-------------------
PUSH_TIME(ITERATION)
^^^^^^^^^^^^^^^^^^^^
After simple processing results the following plots for push action in depend on
iteration number created (click to expand an image):

+----------------+----------------------------------------------------------+
|Function        |Plot                                                      |
+================+==========================================================+
|PUSH_TIME       |.. image:: results/registry-1000-1/push-1000-1.png        |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=1)              |
|CONCURRENCY=1)  |   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PUSH_TIME       |.. image:: results/registry-1000-10/push-1000-10.png      |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=10)             |
|CONCURRENCY=10) |   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PUSH_TIME       |.. image:: results/registry-1000-30/push-1000-30.png      |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=30)             |
|CONCURRENCY=30) |   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PUSH_TIME       |.. image:: results/registry-1000-50/push-1000-50.png      |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=50)             |
|CONCURRENCY=50) |   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PUSH_TIME       |.. image:: results/registry-1000-100/push-1000-100.png    |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=100)            |
|CONCURRENCY=100)|   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PUSH_TIME       |.. image:: results/registry-push-1000-1_10_30_50_100.png  |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY={1,10,30,50,100}|
|CONCURRENCY={1, |   :scale: 20                                             |
|10,30,50,100}   |                                                          |
+----------------+----------------------------------------------------------+

PUSH_TIME(CONCURRENCY)
^^^^^^^^^^^^^^^^^^^^^^
The following table and graph show how PUSH_TIME parameter depend on CONCURRENCY
parameter.

.. table:: Maximum, Minimum, Average and Percentile 90% of PUSH_TIME values in
           depend on CONCURRENCY parameter.

  +-----------+-----------+-----------+-----------+--------------+
  |Concurrency|Maximum    |Minimum    |Average    |Percentile 90%|
  +===========+===========+===========+===========+==============+
  |1          |18.23183703|2.014497995|2.852927562|2.120845795   |
  +-----------+-----------+-----------+-----------+--------------+
  |10         |51.36455989|4.625913858|6.886669915|4.924576068   |
  +-----------+-----------+-----------+-----------+--------------+
  |30         |143.376904 |14.23889208|20.4385057 |14.57682798   |
  +-----------+-----------+-----------+-----------+--------------+
  |50         |45.15124679|21.27197409|24.59056571|24.24201851   |
  +-----------+-----------+-----------+-----------+--------------+
  |100        |254.9175169|20.78799295|66.44495539|133.36117     |
  +-----------+-----------+-----------+-----------+--------------+

.. image:: results/registry-push.png
   :alt: PUSH_TIME
   :scale: 100

Pull action results
-------------------
PULL_TIME(ITERATION)
^^^^^^^^^^^^^^^^^^^^
After simple processing results the following plots for pull action in depend on
iteration number created (click to expand an image):

+----------------+----------------------------------------------------------+
|Function        |Plot                                                      |
+================+==========================================================+
|PULL_TIME       |.. image:: results/registry-1000-1/pull-1000-1.png        |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=1)              |
|CONCURRENCY=1)  |   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PULL_TIME       |.. image:: results/registry-1000-10/pull-1000-10.png      |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=10)             |
|CONCURRENCY=10) |   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PULL_TIME       |.. image:: results/registry-1000-30/pull-1000-30.png      |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=30)             |
|CONCURRENCY=30) |   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PULL_TIME       |.. image:: results/registry-1000-50/pull-1000-50.png      |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=50)             |
|CONCURRENCY=50) |   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PULL_TIME       |.. image:: results/registry-1000-100/pull-1000-100.png    |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=100)            |
|CONCURRENCY=100)|   :scale: 20                                             |
+----------------+----------------------------------------------------------+
|PULL_TIME       |.. image:: results/registry-pull-1000-1_10_30_50_100.png  |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY={1,10,30,50,100}|
|CONCURRENCY={1, |   :scale: 20                                             |
|10,30,50,100}   |                                                          |
+----------------+----------------------------------------------------------+

PULL_TIME(CONCURRENCY)
^^^^^^^^^^^^^^^^^^^^^^
The following table and graph show how PUSH_TIME parameter depend on CONCURRENCY
parameter.

.. table:: Maximum, Minimum, Average and Percentile 90% of PULL_TIME values in
           depend on CONCURRENCY parameter.

  +-----------+------------+-------------+------------+--------------+
  |Concurrency|Maximum     |Minimum      |Average     |Percentile 90%|
  +===========+============+=============+============+==============+
  |1          |0.7883470058|0.05074381828|0.6775195916|0.7058973074  |
  +-----------+------------+-------------+------------+--------------+
  |10         |1.59649086  |0.05712890625|1.113002464 |1.204397488   |
  +-----------+------------+-------------+------------+--------------+
  |30         |4.239136934 |0.1007189751 |2.70093091  |2.899113488   |
  +-----------+------------+-------------+------------+--------------+
  |50         |6.978290081 |0.131428957  |4.493998793 |4.860594058   |
  +-----------+------------+-------------+------------+--------------+
  |100        |13.00426912 |0.152477026  |8.819601912 |9.696622682   |
  +-----------+------------+-------------+------------+--------------+

.. image:: results/registry-pull.png
   :alt: PULL_TIME
   :scale: 100

Issues which have been found during the tests
=============================================

.. table:: Issues which have been found during the tests

 +-------------------------------+---------------------------------------------+
 |Issue description              |Root cause, Link                             |
 +===============================+=============================================+
 || only 5 images can be uploaded|| Root cause of the issue haven't found yet  |
 || to Registry at the           ||                                            |
 || same time                    ||                                            |
 +-------------------------------+---------------------------------------------+

.. references:

.. _Docker Registry2: https://docs.docker.com/registry
