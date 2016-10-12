MySQL on Kubernetes with volume on host
---------------------------------------

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
         hostPath:
           path: /var/lib/mysql

.. _Sysbench: https://github.com/akopytov/sysbench

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
    - 45929.93
    - 41336.65
    - 2296.42
   *
    - 40
    - 65418.03
    - 58875.32
    - 3270.64
   *
    - 60
    - 71185.91
    - 64063.57
    - 3558.65
   *
    - 80
    - 67894.49
    - 61103.56
    - 3393.92
   *
    - 120
    - 70333.68
    - 63299.39
    - 3515.37
   *
    - 160
    - 70310.28
    - 63276.21
    - 3513.48
   *
    - 200
    - 69755.76
    - 62775.64
    - 3485.03
