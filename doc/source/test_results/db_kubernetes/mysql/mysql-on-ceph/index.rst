MySQL on Kubernetes with Ceph performance report
------------------------------------------------

This scenario is executed with `Sysbench`_ tool. There is one instance of
tool per tester node, each running in N threads. The tool is configured
to point to MySQL container directly.

YAML for Kubernetes pod
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

   apiVersion: v1
   kind: Pod
   metadata:
     name: mysql
     labels:
       name: mysql
   spec:
     containers:
       - name: mysql
         image: mysql/mysql-server:5.7
         env:
           - name: MYSQL_ROOT_PASSWORD
             value: r00tme
         volumeMounts:
           - name: mysql-data
             mountPath: /var/lib/mysql
     volumes:
       - name: mysql-data
         rbd:
           monitors:
             - 10.3.58.6:6789
             - 10.3.58.14:6789
             - 10.3.58.18:6789
           pool: rbd
           image: mysql-data
           user: admin
           secretRef:
             name: ceph-secret
           fsType: ext4
           readOnly: false

CEPH status
^^^^^^^^^^^
.. code-block:: none

   cluster 09b06e2e-205d-4bbf-8ad8-37582d00e723
    health HEALTH_OK
    monmap e1: 3 mons at {osscr04r13c26=10.3.58.6:6789/0,osscr04r13c27=10.3.58.14:6789/0,osscr04r13c28=10.3.58.18:6789/0}
           election epoch 6, quorum 0,1,2 osscr04r13c26,osscr04r13c27,osscr04r13c28
    osdmap e14: 3 osds: 3 up, 3 in
     pgmap v8663: 64 pgs, 1 pools, 1630 MB data, 448 objects
           4993 MB used, 2214 GB / 2219 GB avail
                 64 active+clean

/etc/ceph/ceph.conf
^^^^^^^^^^^^^^^^^^^
.. code-block:: none

   [global]
   fsid = 09b06e2e-205d-4bbf-8ad8-37582d00e723
   max open files = 131072
   mon_initial_members = osscr04r13c26,osscr04r13c27,osscr04r13c28
   mon host = 10.3.58.6,10.3.58.14,10.3.58.18
   public_network = 10.3.56.0/21
   cluster_network = 192.168.0.0/24

   [client.libvirt]
   admin socket = /var/run/ceph/$cluster-$type.$id.$pid.$cctid.asok
   log file = /var/log/ceph/qemu-guest-$pid.log

   [osd]
   osd mkfs type = xfs
   osd mkfs options xfs = -f -i size=2048
   osd mount options xfs = noatime,largeio,inode64,swalloc
   osd journal size = 5120

Full output for ``ceph --show-config available`` in
:download:`full_ceph_config.txt <files/full_ceph_config.txt>`

Throughput
^^^^^^^^^^

The following chart shows the number of queries, read/write  queries and
transactions depending on total thread count.


.. list-table:: Throughput
   :header-rows: 1

   *
     - threads
     - queries per sec
     - read/write queries per sec
     - transactions per sec
   *
     - 20
     - 12413.47
     - 11171.73
     - 620.64
   *
     - 40
     - 16843.37
     - 15158.59
     - 842.08
   *
     - 60
     - 19478.55
     - 17524.87
     - 973.53
   *
     - 80
     - 19761.78
     - 17779.89
     - 987.67
   *
     - 120
     - 20047.85
     - 18037.43
     - 1001.96
   *
     - 160
     - 19914.13
     - 17920.40
     - 995.50
   *
     - 200
     - 20229.39
     - 18204.32
     - 1011.27

.. _Sysbench: https://github.com/akopytov/sysbench