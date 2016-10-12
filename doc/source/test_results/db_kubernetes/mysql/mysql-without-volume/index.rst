MySQL on Kubernetes without volume
----------------------------------

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
         volumeMounts:
           - name: mysql-etc
             mountPath: /etc/mysql
         env:
           - name: MYSQL_ROOT_PASSWORD
             value: r00tme
     volumes:
       - name: mysql-etc
         hostPath:
           path: /etc/mysql


Throughput
^^^^^^^^^^

The following chart shows the number of queries, read/write queries
and transactions depending on total thread count.


.. list-table:: Throughput
   :header-rows: 1

   *
     - threads
     - queries per sec
     - read/write queries per sec
     - transactions per sec
   *
    - 20
    - 42389.02
    - 38149.43
    - 2119.32
   *
    - 40
    - 67086.84
    - 60377.59
    - 3354.02
   *
    - 60
    - 64089.24
    - 57679.97
    - 3203.95
   *
    - 80
    - 67831.60
    - 61046.72
    - 3390.72
   *
    - 120
    - 70284.19
    - 63254.38
    - 3512.84
   *
    - 160
    - 71344.12
    - 64209.14
    - 3565.27
   *
    - 200
    - 71300.89
    - 64169.52
    - 3562.46

.. _Sysbench: https://github.com/akopytov/sysbench