Performa omsimulator
--------------------

This section describes how to perform
:ref:`message_queue_ha` with `Performa`_
tool.

Test environment preparation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To perform the test plan you will need to install performa toolkit.
The toolkit uses MongoDB for stats processing and reporting.

.. code::

    $ pip install performa

The execution requires the following parameters to be set:
  * ``mongo-address`` - The host where MongoDB is installed
  * ``remote-user`` - The user that can connect to remote host in OpenStack
    cloud
  * ``tester-hosts`` - List of hosts were omsimulator will be executed
  * ``rabbit-url`` - RabbitMQ address, it has the form of
    `rabbit://{<user>:<password>@<host>:<port>[,]}/`
  * ``report`` - folder where to store the report



Execution
^^^^^^^^^

RPC CALL measurements::

    $ performa --mongo-url <mongo-address> --mongo-db performa
      --scenario mq/omsimulator-ha-call --remote-user <remote-user>
      --vars "{tester_hosts: [<tester-hosts>], rabbit_url: \"<rabbit-url>\"}"
      --book <report>

example:
    ``$ performa --mongo-url 172.20.9.20 --mongo-db performa --scenario mq/omsimulator-ha-call --remote-user root --vars "{rabbit_hosts: [node-123, node-111, node-58], tester_hosts: [node-144], rabbit_url: \"rabbit://nova:tGAPNtjHh8yvvkR69MooN1eD@node-58:5673,nova:tGAPNtjHh8yvvkR69MooN1eD@node-111:5673,nova:tGAPNtjHh8yvvkR69MooN1eD@node-123:5673/\"}" --book books/omsimulator-ha-call-cmsm-km``


RPC CAST measurements::

    $ performa --mongo-url <mongo-address> --mongo-db performa
      --scenario mq/omsimulator-ha-cast --remote-user <remote-user>
      --vars "{tester_hosts: [<tester-hosts>], rabbit_url: \"<rabbit-url>\"}"
      --book <report>

example:
    ``$ performa --mongo-url 172.20.9.20 --mongo-db performa --scenario mq/omsimulator-ha-cast --remote-user root --vars "{rabbit_hosts: [node-123, node-111, node-58], tester_hosts: [node-144], rabbit_url: \"rabbit://nova:tGAPNtjHh8yvvkR69MooN1eD@node-58:5673,nova:tGAPNtjHh8yvvkR69MooN1eD@node-111:5673,nova:tGAPNtjHh8yvvkR69MooN1eD@node-123:5673/\"}" --book books/omsimulator-ha-cast-cmsm-km``


NOTIFY measurements::

    $ performa --mongo-url <mongo-address> --mongo-db performa
      --scenario mq/omsimulator-ha-notify --remote-user <remote-user>
      --vars "{tester_hosts: [<tester-hosts>], rabbit_url: \"<rabbit-url>\"}"
      --book <report>

example:
    ``$ performa --mongo-url 172.20.9.20 --mongo-db performa --scenario mq/omsimulator-ha-notify --remote-user root --vars "{rabbit_hosts: [node-123, node-111, node-58], tester_hosts: [node-144], rabbit_url: \"rabbit://nova:tGAPNtjHh8yvvkR69MooN1eD@node-58:5673,nova:tGAPNtjHh8yvvkR69MooN1eD@node-111:5673,nova:tGAPNtjHh8yvvkR69MooN1eD@node-123:5673/\"}" --book books/omsimulator-ha-notify-cmsm-km``


.. references:

.. _Performa: https://github.com/shakhat/performa