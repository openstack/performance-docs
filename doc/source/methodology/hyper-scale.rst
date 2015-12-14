
Methodology for testing Hyper-Scale
===================================

What is meant by Hyper-Scale?
-----------------------------

For this section, hyper-scale is defined as being able to achieve 100K of
something in an OpenStack cloud. Initially this may be VMs, but could be
hypervisors, projects, etc. Because of the open-endnesses of this definition,
it is necessary to identify all places where operations show linear (or
even worse...) execution time as the number of items that the operation deals
with scales up. For example, if execution time of an operation is order of
10 microseconds per item that operation is dealing with, that means that at
100K, a second has been added to agent execution time.

How is linearity defined in this context?
-----------------------------------------

To determine linearity, one measures the execution time of each operation
over a sample the has increasing scale and then performance a least squares
fit [#]_ to the raw data. Such a fit looks to map a straight line (y=mx+b) to
the sample data, where

* x == the number of items being scaled,
* m == the slope of the fit,
* b == the vertical intercept, and
* y == the operation's execution time

In addition to finding m and b, the fit will also generate a correlation
coefficient (r) which provides a measurement of how random the sample data was.
As an initial filter, fits with a correlation coefficient above a certain
threshold can be considered as candidates for improvement. Once an operation
is considered a candidate for improvement, then the execution time of all of
its sub-operations are measured and a least squares fit performed on them.
When looking at sub-operations, of interest are the slope and the ratio of
the vertical intercept to the slope (the "doubling scale" of the operation).
These together determine the "long pole in the test" (the sub-operation that
should be analyzed first), with the slope determining the order and the
"doubling scale" acting as a tie breaker.

How Should Code be Instrumented When Looking for Hyper-Scale?
-------------------------------------------------------------

Today, instrumentation is a very manual process: after running devstack,
debug LOG statements are added into the code base to indicate the entrance
and exit of each routine that should be timed. These debug log statements
can be tagged with strings like "instrument:" or "instrument2:" to allow
multiple levels of instrumentation to be applied during a single test run.
Then restart the agent that is being instrumented via the screen that is
created by devstack.

Note: as this ends up to be an iterative process as one looks to isolate
the code that shows linear execution time, for subsequent restacks, it
usually makes sense to not reclone (unless you want to repeat the by hand
editing afterwards).

It is hoped that the osprofiler sub-project of oslo [#]_ will be extended to
allow for method decoration to replace the use of by hand editing.

Setup Considerations
--------------------

There are two ways to go about looking for potential hyper-scale issues.
The first is to use a brute force method where one actually builds a
hyper-scale cloud and tests. Another route is to build a cloud using the
slowest, smallest, simplest components one has on hand. The idea behind this
approach is that by slowing down the hardware, the slope and intercept of
the least squares fit are both scaled up, making linearity issues easier to
find with lower numbers of instances. However, this makes comparing raw values
from the least squares fits between different setups difficult - one can
never be 100% sure that the comparison is "apples-to-apples" and that
hardware effects are completely isolated. The choice above of using the
correlation coefficient and "doubling scale" above are intended to use values
that are more independent of the test cloud design.

An Example: Neutron L3 Scheduling
---------------------------------

The rest of this section presents an example of this methodology in action
(In fact, this example was what led to the methodology being developed).
This example uses a four node cloud, configured as a controller, a network
node, and two compute nodes.

To determine what parts of L3 scheduling needed scaling improvements the
following experiment was used.  This test can certainly be automated via
Rally and should be (once instrumentation no longer requires manual decoration
and/or code manipulation):

#. Create the external network and subnet with:

.. code-block:: bash

  neutron net-create test-external --router:external --provider:physical_network default --provider:network_type flat
  neutron subnet-create --name test-external-subnet --disable-dhcp test-external 172.18.128.0/20

#. Create X number of projects

#. For each project, perform the following steps (in fhe following,
   $i is the tenant index and $id is the tenant UUID, $net is the UUID of
   the tenant network created in the first step below, and $port is the
   interface port UUID reported by nova):

.. code-block:: bash

  neutron net-create network-$i --tenant-id $id
  neutron subnet-create network-$i 192.168.18.0/24 --name subnet-$i --tenant-id $id
  neutron router-create router-$i --tenant-id $id
  neutron router-interface-add router-$i subnet-$i
  neutron router-gateway-set router-$i test-external
  keystone user-role-add --user=admin --tenant=tenant-$i --role=admin
  nova --os-tenant-name tenant-$i boot --flavor m1.nano --image cirros-0.3.4-x86_64-uec --nic net-id=$net instance-tenant-$i
  (once the instance's interface port is shown as active by nova):
  neutron floatingip-create --tenant-id $id --port-id $port test-external

#. For each project, perform the following steps:

.. code-block:: bash

  neutron floatingip-delete <floatingip-uuid>
  nova --os-tenant-name tenant-$i stop instance-tenant-$i
  neutron router-gateway-clear <router-uuid> test-external
  neutron router-interface-delete router-$i subnet-$i
  neutron router-delete router-$i
  neutron subnet-delete subnet-$i
  neutron net-delete network-$i

This provides testing of both the paths that create and delete Neutron routers
and the attributes that make them usuable.

Extracting Execution Time
~~~~~~~~~~~~~~~~~~~~~~~~~

Once one has instrumented logs (or instrumentation records), extracting
execution time becomes a matter of filtering via one's favorite language.
One approach is to filter to a comma separate value (csv) file and then
import that into a spreadsheet program that has the least squares function
built in to find the fit and correlation coefficient.

Legacy Results Using Neutron Master as of 11/6/15 - Adding Routers/FIPs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+------------+---------------+-----------------+
| Function        | Corelation | Slope         | Doubling        |
|                 | Coeficient | (msec/router) | Scale (routers) |
+=================+============+===============+=================+
| Interface Add   | 0.302      | 1.56          | 1211            |
+-----------------+------------+---------------+-----------------+
| Set Gateway     | 0.260      |               |                 |
+-----------------+------------+---------------+-----------------+
| Add FIP         | 2.46E-05   |               |                 |
+-----------------+------------+---------------+-----------------+

Thus, the interface add operation is a candidate for further evaluation.
Looking at the largest contributers to the slope, we find the following
methods at successively deeper levels of code:

* _process_router_if_compatible (1.34 msec/router)

  * _process_added_router (1.31 msec/router)

    * _router_added (0.226 msec/router)

    * _process (0.998 msec/router)

      * process_internal_ports (0.888 msec/router)

        * ovs add-port (0.505 msec/router)

This last time is outside of Neutron: it needs to be addressed from
within the OVS code itself (this is being tracked by [#]_)

Legacy Results Using Neutron Master as of 11/6/15 - Removing Routers/FIPs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+------------+---------------+-----------------+
| Function         | Corelation | Slope         | Doubling        |
|                  | Coeficient | (msec/router) | Scale (routers) |
+==================+============+===============+=================+
| Clear FIP        | 0.389      | 1.503         | 401.5           |
+------------------+------------+---------------+-----------------+
| Clear Gateway    | 0.535      | 1.733         | 289.3           |
+------------------+------------+---------------+-----------------+
| Remove Interface | 0.390      | 1.425         | 302.6           |
+------------------+------------+---------------+-----------------+
| Remove Router    | 0.526      | 1.5           | 252.8           |
+------------------+------------+---------------+-----------------+

Each of these operations is a candidate for improvement.  Looking more
deeply at each operation, we find the following contributors to the slope:

* Clear FIP

  * get_routers (9.667 usec/router)

  * _process_routers_if_compatible (1.496 msec/router)

    * _process_updated_router (1.455 msec/router)

      * process (1.454 msec/router)

        * process_internal_ports (151 usec/router)

        * process_external (1.304 msec/router)

          * iptables apply time: slope (0.513 msec/router)

          * process_external_gateway (0.207 msec/router)

          * FIP cleanup (0.551 msec/router)

* Clear Gateway

  * get_routers (25.8 usec/router)

  * _process_routers_if_compatible (1.714 msec/router)

    * _process_update_router (1.700 msec/router)

      * process (1.700 msec/router)

        * process_internal_ports (92 usec/router)

        * process_external (0.99 msec/router)

          * process_external_gateway (0.99 msec/router)

            * unplug (0.857 msec/router)

      * iptables apply time: slope (0.614 msec/router)

* Remove Interface

  * _process_routers_if_compatible (1.398 msec/router)

    * _process_update_router (1.372 msec/router)

      * process (1.372 msec/router)

        * process_internal_ports (0.685 sec/router)

          * old_ports_loop (0.586 msec/router)

        * iptables apply time: slope (0.538 msec/router)

* Remove Router

  * _safe_router_removed (1.5 msec/router)

    * before_delete_callback (0.482 msec/router)

    * delete (1.055 msec/router)

      * process (0.865 msec/router)

        * process_internal_ports (0.168 msec/router)

        * process_external (0.200 msec/router)

        * iptables apply time: slope (0.496 msec/router)

      * namespace delete (0.195 msec/router)

As can be seen, improving execution time for iptables will impact a lot of
operations (and this is a known issue).  In addition there are several other
functions to be dug into further to see what improvements can be made.

References
----------

.. [#] http://mathworld.wolfram.com/LeastSquaresFitting.html
.. [#] https://review.openstack.org/#/c/103825/
.. [#]  https://bugs.launchpad.net/neutron/+bug/1494959
