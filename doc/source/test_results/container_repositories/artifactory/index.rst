
.. _Measuring_performance_of_JFrog_Artifactory_Pro:

*********************************************************
Results of measuring performance of JFrog Artifactory Pro
*********************************************************

:Abstract:

  This document includes performance test results of `JFrog Artifactory Pro`_
  service as a repository of docker images. All test have been performed
  regarding :ref:`Measuring_performance_of_container_repositories`


Environment description
=======================
Hardware configuration of each server
-------------------------------------

.. table:: Description of servers hardware

  +-------+----------------+------------------------+------------------------+
  |server |name            |728998-comp-disk-228    |728998-comp-disk-227    |
  |       +----------------+------------------------+------------------------+
  |       |role            |test_tool               |artifactory             |
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

Software configuration of the Artifactory service
-------------------------------------------------
Installation of Artifactory:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: bash

  # Install Java
  apt-get install software-properties-common
  sudo add-apt-repository ppa:webupd8team/java
  apt-get update
  sudo apt-get install oracle-java8-installer # Interactive java installer
  # Install ArtifactoryPro
  echo "deb https://jfrog.bintray.com/artifactory-pro-debs trusty main" > /etc/apt/sources.list.d/artifactory.list
  apt-get update
  apt-get install jfrog-artifactory-pro
  # Install Nginx as a reverse proxy
  # https://www.jfrog.com/confluence/display/RTF/Configuring+NGINX
  apt-get install nginx

You can find nginx configuration file here
:download:`nginx.conf <configs/nginx.conf>`

Here is the all config files of Artifactory
:download:`artifactory_etc.tar.gz <configs/artifactory_etc.tar.gz>`

After installation all default repositories was removed from Artifactory and
"docker-local" hosted repository was created. You can find full configuration of
the Artifactory installation here:
:download:`config_descriptor.xml <configs/config_descriptor.xml>`
:download:`security_descriptor.xml <configs/security_descriptor.xml>`

.. table:: Versions of some software

  +-----------+------------------+
  |Software   |Version           |
  +===========+==================+
  |Ubuntu     |Ubuntu 14.04.3 LTS|
  +-----------+------------------+
  |Artifactory|4.5.2 rev 40121   |
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
  Artifactory was installed on top of 728998-comp-disk-227 server as described in
  `Installation of Artifactory:`_ section.

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

5. Clean up docker repository in Artifactory via Web UI

6.
  The steps from 2 to 5 was repeated with the following values of the
  concurrency parameters: 1,10,30,50,100

As a result of this part we got the following CSV files:

:download:`PUSH_TIME(CONCURRENCY=1) <./results/artifactory-1000-1/push_results.csv>`
:download:`PUSH_TIME(CONCURRENCY=10) <./results/artifactory-1000-10/push_results.csv>`
:download:`PUSH_TIME(CONCURRENCY=30) <./results/artifactory-1000-30/push_results.csv>`
:download:`PUSH_TIME(CONCURRENCY=50) <./results/artifactory-1000-50/push_results.csv>`
:download:`PUSH_TIME(CONCURRENCY=100) <./results/artifactory-1000-100/push_results.csv>`
:download:`PULL_TIME(CONCURRENCY=1) <./results/artifactory-1000-1/pull_results.csv>`
:download:`PULL_TIME(CONCURRENCY=10) <./results/artifactory-1000-10/pull_results.csv>`
:download:`PULL_TIME(CONCURRENCY=30) <./results/artifactory-1000-30/pull_results.csv>`
:download:`PULL_TIME(CONCURRENCY=50) <./results/artifactory-1000-50/pull_results.csv>`
:download:`PULL_TIME(CONCURRENCY=100) <./results/artifactory-1000-100/pull_results.csv>`

Results
=======
Push action results
-------------------
PUSH_TIME(ITERATION)
^^^^^^^^^^^^^^^^^^^^
After simple processing results the following plots for push action in depend on
iteration number created (click to expand an image):

+----------------+-------------------------------------------------------------+
|Function        |Plot                                                         |
+================+=============================================================+
|PUSH_TIME       |.. image:: results/artifactory-1000-1/push-1000-1.png        |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=1)                 |
|CONCURRENCY=1)  |   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PUSH_TIME       |.. image:: results/artifactory-1000-10/push-1000-10.png      |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=10)                |
|CONCURRENCY=10) |   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PUSH_TIME       |.. image:: results/artifactory-1000-30/push-1000-30.png      |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=30)                |
|CONCURRENCY=30) |   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PUSH_TIME       |.. image:: results/artifactory-1000-50/push-1000-50.png      |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=50)                |
|CONCURRENCY=50) |   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PUSH_TIME       |.. image:: results/artifactory-1000-100/push-1000-100.png    |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY=100)               |
|CONCURRENCY=100)|   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PUSH_TIME       |.. image:: results/artifactory-push-1000-1_10_30_50_100.png  |
|(ITERATION,     |   :alt: PUSH_TIME(ITERATION, CONCURRENCY={1,10,30,50,100}   |
|CONCURRENCY={1, |   :scale: 20                                                |
|10,30,50,100}   |                                                             |
+----------------+-------------------------------------------------------------+

PUSH_TIME(CONCURRENCY)
^^^^^^^^^^^^^^^^^^^^^^
The following table and graph show how PUSH_TIME parameter depend on CONCURRENCY
parameter.

.. table:: Maximum, Minimum, Average and Percentile 90% of PUSH_TIME values in
           depend on CONCURRENCY parameter.

  +-----------+-----------+-----------+-----------+--------------+
  |Concurrency|Maximum    |Minimum    |Average    |Percentile 90%|
  +===========+===========+===========+===========+==============+
  +-----------+-----------+-----------+-----------+--------------+
  |1          |20.45173717|18.13562512|18.45595757|18.70360937   |
  +-----------+-----------+-----------+-----------+--------------+
  |10         |52.81749606|21.4737699 |47.39192888|47.92230422   |
  +-----------+-----------+-----------+-----------+--------------+
  |30         |147.2520959|21.35128784|140.8133277|143.3592351   |
  +-----------+-----------+-----------+-----------+--------------+
  |50         |242.0436599|21.53936005|232.1077632|238.6817375   |
  +-----------+-----------+-----------+-----------+--------------+
  |100        |474.1983588|21.41779709|447.7350837|471.5060248   |
  +-----------+-----------+-----------+-----------+--------------+

.. image:: results/artifactory-push.png
   :alt: PUSH_TIME
   :scale: 100

Pull action results
-------------------
PULL_TIME(ITERATION)
^^^^^^^^^^^^^^^^^^^^
After simple processing results the following plots for pull action in depend on
iteration number created (click to expand an image):

+----------------+-------------------------------------------------------------+
|Function        |Plot                                                         |
+================+=============================================================+
|PULL_TIME       |.. image:: results/artifactory-1000-1/pull-1000-1.png        |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=1)                 |
|CONCURRENCY=1)  |   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PULL_TIME       |.. image:: results/artifactory-1000-10/pull-1000-10.png      |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=10)                |
|CONCURRENCY=10) |   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PULL_TIME       |.. image:: results/artifactory-1000-30/pull-1000-30.png      |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=30)                |
|CONCURRENCY=30) |   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PULL_TIME       |.. image:: results/artifactory-1000-50/pull-1000-50.png      |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=50)                |
|CONCURRENCY=50) |   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PULL_TIME       |.. image:: results/artifactory-1000-100/pull-1000-100.png    |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY=100)               |
|CONCURRENCY=100)|   :scale: 20                                                |
+----------------+-------------------------------------------------------------+
|PULL_TIME       |.. image:: results/artifactory-pull-1000-1_10_30_50_100.png  |
|(ITERATION,     |   :alt: PULL_TIME(ITERATION, CONCURRENCY={1,10,30,50,100}   |
|CONCURRENCY={1, |   :scale: 20                                                |
|10,30,50,100}   |                                                             |
+----------------+-------------------------------------------------------------+

PULL_TIME(CONCURRENCY)
^^^^^^^^^^^^^^^^^^^^^^
The following table and graph show how PUSH_TIME parameter depend on CONCURRENCY
parameter.

.. table:: Maximum, Minimum, Average and Percentile 90% of PULL_TIME values in
           depend on CONCURRENCY parameter.

  +-----------+------------+-------------+------------+--------------+
  |Concurrency|Maximum     |Minimum      |Average     |Percentile 90%|
  +===========+============+=============+============+==============+
  |1          |1.023168087 |0.09103393555|0.7067174957|0.7760614157  |
  +-----------+------------+-------------+------------+--------------+
  |10         |1.87360692  |0.08845591545|1.127708118 |1.361271906   |
  +-----------+------------+-------------+------------+--------------+
  |30         |4.27976203  |0.1920921803 |2.644113734 |2.870757174   |
  +-----------+------------+-------------+------------+--------------+
  |50         |6.287320852 |0.2292528152 |4.416184656 |4.711911416   |
  +-----------+------------+-------------+------------+--------------+
  |100        |10.30138803 |0.167137146  |8.50843117  |9.09850688    |
  +-----------+------------+-------------+------------+--------------+

.. image:: results/artifactory-pull.png
   :alt: PULL_TIME
   :scale: 100

Issues which have been found during the tests
=============================================

.. table:: Issues which have been found during the tests

  +-------------------------------+---------------------------------------------+
  |Issue description              |Root cause, Link                             |
  +===============================+=============================================+
  || Artifactory allows re-pushing|https://www.jfrog.com/jira/browse/RTFACT-9591|
  || existed docker layers instead|                                             |
  || of answer with               |                                             |
  || "already exists" message     |                                             |
  +-------------------------------+---------------------------------------------+
  || only 5 images can be uploaded|| Root cause of the issue haven't found yet  |
  || to Artifactory at the        ||                                            |
  || same time                    ||                                            |
  +-------------------------------+---------------------------------------------+

.. references:

.. _JFrog Artifactory Pro: https://www.jfrog.com/artifactory
