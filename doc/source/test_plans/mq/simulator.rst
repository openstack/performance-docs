Oslo.messaging Simulator
------------------------

This section describes how to perform
:ref:`message_queue_performance` with `Oslo.messaging Simulator`_
tool.

Test environment preparation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To perform the test plan you will need to install oslo.messaging simulator.

The simulator tool depends on SciPy library which requires some mathematical
packages to be installed into system.

To install on CentOS 7::

    # yum install lapack-devel

To install on Ubuntu 14.04::

    # apt-get install liblapack-dev gfortran


The simulator is distributed as part of library sources. It is recommended
to be installed within virtual environment.

.. code::

    $ git clone https://git.openstack.org/openstack/oslo.messaging
    $ cd oslo.messaging/
    $ virtualenv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ python setup.py install
    $ pip install scipy
    $ cd tools/


Test Case 1: RPC Call Throughput Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test case specification**: :ref:`message_queue_performance_rpc_call`

**Execution**:

Start the server::

    $ python simulator.py --url rabbit://<username>:<password>@<host>:<port>/ rpc-server

example: ``python simulator.py --url rabbit://nova:DUoqsyrq@192.168.0.4:5673/ --debug true rpc-server``

Start the client::

    $ python simulator.py --url rabbit://<username>:<password>@<host>:<port>/ rpc-client -p <threads> -m <messages>

example: ``python simulator.py --url rabbit://nova:DUoqsyrq@192.168.0.4:5673/ rpc-client -p 10 -m 100``


Test Case 2: RPC Cast Throughput Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test case specification**: :ref:`message_queue_performance_rpc_cast`

**Execution**:

Start the server::

    $ python simulator.py --url rabbit://<username>:<password>@<host>:<port>/ rpc-server

example: ``python simulator.py --url rabbit://nova:DUoqsyrq@192.168.0.4:5673/ --debug true rpc-server``

Start the client::

    $ python simulator.py --url rabbit://<username>:<password>@<host>:<port>/ rpc-client --is-cast true -p <threads> -m <messages>

example: ``python simulator.py --url rabbit://nova:DUoqsyrq@192.168.0.4:5673/ rpc-client --is-cast true -p 10 -m 100``


Test Case 3: Notification Throughput Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    Version at least 2.9 is required to run this test case.

**Test case specification**: :ref:`message_queue_performance_notification`

**Execution**:

Start the server::

    $ python simulator.py --url rabbit://<username>:<password>@<host>:<port>/ notify-server

examples:: ``python simulator.py --url rabbit://nova:DUoqsyrq@192.168.0.4:5673/ notify-server``

Start the client::

    $ python simulator.py --url rabbit://<username>:<password>@<host>:<port>/ notify-client -p <threads> -m <messages>

example: ``python simulator.py --url rabbit://nova:DUoqsyrq@192.168.0.4:5673/ notify-client -p 10 -m 100``



.. references:

.. _Oslo.messaging Simulator: https://github.com/openstack/oslo.messaging/blob/master/tools/simulator.py