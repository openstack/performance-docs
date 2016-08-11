.. _db_performance:

======================
SQL Database Test Plan
======================

:status: **ready**
:version: 1.0

:Abstract:

  This project will determine best practices for scale and performance of SQL
  database deployments in OpenStack, while maintaining availability or
  preferably ACID properties. The focus will be on MySQL and its variants.
  NoSQL and other database types will not be considered here.
  To avoid complications, like lack of repeatability and complex test
  environments, this testing will be done in isolation from all
  other OpenStack components.
  The first part of the plan will use the tool sysbench to drive simple
  queries. In the second part, a real database will be extracted from a
  production OpenStack deployment along with a set of corresponding queries.
  These queries can then be played back in a repeatable manner to the same
  database using various configurations.

Test Plan
=========

Test Environment
----------------

A cluster of three server hosts will be used for all database tests with
replication. Tests without replication will use one of these servers.
A separate client machine will be used to drive the tests.
All cluster hardware will be documented, including processor model and
frequency, memory size, storage type and capacity, networking interfaces, etc.

Preparation
^^^^^^^^^^^

On all 3 database server hosts:


**MySQL installation**

.. code-block:: none

  sudo apt-get install mysql-server
  add to /etc/apt/sources.list.d/galera.list:
        deb http://releases.galeracluster.com/ubuntu trusty main
  sudo apt-get install software-properties-common
  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv BC19DDBA
  sudo apt-get update
  sudo apt-get install galera-3 galera-arbitrator-3 mysql-wsrep-5.6
  sudo apt-get install libmysqlclient-dev

**MariaDB installation**

.. code-block:: none

  sudo apt-get install software-properties-common
  sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
  sudo add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/10.0/ubuntu trusty main'
  sudo apt-get update
  sudo apt-get install mariadb-server           # stand-alone MariaDB
  sudo apt-get install mariadb-galera-server    # with replication

**Percona Cluster installation**

.. code-block:: none

  wget -O - http://www.percona.com/redir/downloads/RPM-GPG-KEY-percona | gpg --import
  sudo gpg --armor --export 1C4CBDCDCD2EFD2A | sudo apt-key add -
  # Add to /etc/apt/sources.list
         deb http://repo.percona.com/apt trusty main
  sudo apt-get update
  sudo apt-get install percona-xtradb-cluster-56  # or
  sudo apt-get install percona-xtradb-cluster-full-56

**Baseline parameters defined in /etc/mysql/my.cnf:**

.. code-block:: none

  user                            = mysql
  binlog_format                   = ROW
  bind_address                    = 0.0.0.0
  default_storage_engine          = InnoDB
  # Uncomment to NOT use default XtraDB
  #ignore_builtin_innodb
  #plugin_load=innodb=ha_innodb.so
  innodb_autoinc_lock_mode        = 2
  innodb_flush_method             = O_DIRECT
  innodb_log_files_in_group       = 2
  innodb_log_file_size            = 1500M
  innodb_flush_log_at_trx_commit  = 2
  innodb_file_per_table           = 1
  innodb_buffer_pool_size         = 52G
  innodb_log_buffer_size          = 8M
  innodb_write_io_threads         = 4
  innodb_read_io_threads          = 4
  innodb_doublewrite              = ON
  wsrep_provider                  = /usr/lib/libgalera_smm.so
  wsrep_provider_options          = "gcache.size=1G; gcache.page_size=1G"
  wsrep_cluster_name              = "test_cluster"
  wsrep_cluster_address           = "gcomm://10.4.1.115,10.4.1.105,10.4.1.114"
  wsrep_node_name                 = "JP15-3"
  wsrep_node_address              = "10.4.1.114"
  wsrep_sst_method                = rsync
  wsrep_slave_threads             = 24
  max_connections                 = 100
  connect_timeout                 = 5
  wait_timeout                    = 600
  max_allowed_packet              = 16M
  thread_cache_size               = 128
  sort_buffer_size                = 4M
  bulk_insert_buffer_size         = 16M
  tmp_table_size                  = 32M
  max_heap_table_size             = 32M
  max_allowed_packet              = 16M
  max_connect_errors              = 1000000
  query_cache_type                = 0
  query_cache_size                = 0
  open_files_limit                = 65535
  table_definition_cache          = 1024
  table_open_cache                = 2048
  max_prepared_stmt_count         = 100000
  log_warnings                    = 2
  log_error                       = /var/log/mysql/mysqld_error.log
  log_queries_not_using_indexes   = 1
  slow_query_log                  = 1
  slow_query_log_file             = /var/log/mysql/mariadb-slow.log
  log_slow_verbosity              = query_plan
  long_query_time                 = 10
  log_slow_verbosity              = query_plan
  log_bin                         = /var/lib/mysql/mariadb-bin
  log_bin_index                   = /var/lib/mysql/mariadb-bin.index
  sync_binlog                     = 0
  expire_logs_days                = 1
  max_binlog_size                 = 1G

**database user permissions**

.. code-block:: none

  run with ``mysql -u root``:
  CREATE USER 'sbtest'@'%';
  GRANT ALL PRIVILEGES ON *.* TO 'sbtest'@'%' WITH GRANT OPTION;
  CREATE USER 'ubuntu'@'%';
  GRANT ALL PRIVILEGES ON *.* TO 'ubuntu'@'%' WITH GRANT OPTION;
  # extra commands for Percona:
  GRANT ALL PRIVILEGES ON `mysql`.* TO ''@'%' WITH GRANT OPTION;
  GRANT ALL PRIVILEGES ON `sbtest%`.* TO ''@'%' WITH GRANT OPTION;

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

**Hardware**

Minimum hardware to run these tests follows. The actual hardware used needs
to be fully documented.

  * 2 socket servers with recent Intel processors
  * 64 GB memory
  * 10 GbE NICs
  * SSD storage
  * 10 GbE network switch

**Software**

Actual software used to be fully documented.

  * Ubuntu 14.04
      */etc/ssh/sshd_config:*

      .. code-block:: none

         PermitRootLogin yes
         PasswordAuthentication yes

  * Recent versions of MySQL, MariaDB, Percona, sysbench

**Sysbench on 3 hosts**

  * Build sysbench from source, requires mysql 5.6.27
  * SIZE = 5000000
  * 10 tables per db
  * Either 1 or 3 dbs on cluster
  * Replication=1 (no replication) uses innodb-flush-log-at-trx-commit=1
  * Replication=3 (Galera) uses innodb-flush-log-at-trx-commit=2 for
    comparable durability

**Example sysbench commands**

*Preparation*

.. code-block:: none

  SIZE=50000000
  for HOST in 115 105 114; do
    sysbench --test=oltp --mysql-host=10.4.8.$HOST --mysql-db=sbtest$HOST \
      --oltp-table-name=sbtest$HOST --oltp-table-size=$SIZE \
      --oltp-auto-inc=off --db-driver=mysql --mysql-table-engine=innodb \
      prepare &
  done

*Run*

.. code-block:: none

  SIZE=50000000
  THREADS=80
  for HOST in 115 105 114; do
    sysbench --num-threads=$THREADS --max-time=600 --max-requests=0 \
      --test=oltp --mysql-host=10.4.8.$HOST --mysql-db=sbtest$HOST \
      --oltp-table-name=sbtest$HOST --oltp-table-size=$SIZE \
      --oltp-auto-inc=off --oltp-read-only=off --db-driver=mysql \
      --mysql-table-engine=innodb --mysql-engine-trx=yes --oltp-num-tables=10 \
      run &
  done

Test Case 1: sysbench
---------------------

Description
^^^^^^^^^^^

This set of tests will quantify generic database query performance.
The load is controlled by the number of threads. The performance difference
due to replication will be measured.

Parameters
^^^^^^^^^^

=================  ========================
Parameter          Value
=================  ========================
Database	   MySQL, MariaDB, Percona
Number of threads  10, 20, 30, 60, 120, 180
Replication        1, 3
=================  ========================

Database configurations

  * MySQL/InnoDB with Galera
  * MariaDB/XtraDB with Galera
  * MariaDB/InnoDB with Galera
  * Percona Cluster/XtraDB with Galera
  * MySQL with NDB
  * PostgreSQL

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ===========  =================  ======================================
Priority  Value        Measurement Units  Description
========  ===========  =================  ======================================
1         throughput   tps                transactions/sec, measured by the tool
1         query lat    millisec           query latency, measured by MySQL
2         CPU util     percent            Average CPU utilization on db server
2         Rx BW        MB/sec             Average Network receive bandwidth
2         Tx BW        MB/sec             Average Network transmit bandwidth
2         Read BW      MB/sec             Average storage read bandwidth
2         Write BW     MB/sec             Average storage write bandwidth
2         Storage lat  millisec           Average storage latency
========  ===========  =================  ======================================

Test Case 2: Database Testing Tool
----------------------------------

Description
^^^^^^^^^^^

This set of tests will quantify, as realistically as possible,
database query performance with an actual OpenStack database and
corresponding queries.
The goal is to develop a portable tool to test databases.
A backup will be taken of the database from Mirantis' 200-node cluster,
which can then be imported into different databases. Corresponding queries
will be collected as well. These queries will then be played back using
Percona Playback, or a similar tool.
Database configurations will be similar to above.
Some of the ultimate goals of the testing tool are to identify:

  * which software is best for OpenStack
  * how to best configure database parameters
  * which OpenStack queries consume the most resources and are therefore the
    best candidates for optimization

Parameters
^^^^^^^^^^

=================  ========================
Parameter          Value
=================  ========================
Database           MySQL, MariaDB, Percona
Number of threads  10, 20, 30, 60, 120, 180
Replication        1, 3
=================  ========================

Database configurations will be chosen from among the best of the
sysbench tests.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ===========  =================  ======================================
Priority  Value        Measurement Units  Description
========  ===========  =================  ======================================
1         throughput   tps                transactions/sec, measured by the tool
1         query lat    millisec           query latency, measured by the tool
2         CPU util     percent            Average CPU utilization on db server
2         Memory util  MB                 Memory used on the server
2         Rx BW        MB/sec             Average Network receive bandwidth
2         Tx BW        MB/sec             Average Network transmit bandwidth
2         Read BW      MB/sec             Average storage read bandwidth
2         Write BW     MB/sec             Average storage write bandwidth
2         Storage lat  millisec           Average storage latency
========  ===========  =================  ======================================

CPU utilization, network and storage throughputs, and storage latency will
be obtained from standard Linux performance tools like sar and mpstat.

Elapsed time or latency for high-level OpenStack operations like virtual
machine creation or network configuration may involve many database queries.
The maximum query throughput the database layer can process with
reasonable latency determines the maximum cluster size that can be supported.
