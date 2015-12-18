Test Cases
==========

Test Case 1: Message Queue Throughput Test
------------------------------------------

**Description**

This test measures the aggregate throughput of a MQ layer by using the oslo.messaging
simulator tool. Either RabbitMQ, ActiveMQ, or ZeroMQ can be used as the MQ layer.
Throughput is calculated as the sum
over the MQ clients of the throughput for each client. For each test the number of
clients/threads is configured to one of the specific values defined in the test case
parameters section. The full set of tests will cover all the "Threads count" values shown,
plus additional values as needed to quantify the dependence of MQ throughput on load, and
to find the maximum throughput.

**Parameters**

======================= =====
Parameter name          Value
======================= =====
oslo.messaging version  2.5.0
simulator.py version    1.0
Threads count           50, 70, 100
======================= =====

**Measurements**

==========  ================  ===========
Value       Measurment Units  Description
==========  ================  ===========
Throughput  msg/sec           Directly measured by simulator tool
==========  ================  ===========

**Result Type**

================  =======================  =========================
Result type       Measurement Units        Description
================  =======================  =========================
Throughput Value  msg/sec                  Table of numerical values
Throughput Graph  msg/sec vs # of threads  Graph
================  =======================  =========================

**Additional Measurements**

=========== ======= =============================
Measurement Units   Description
=========== ======= =============================
Variance    msg/sec Throughput variance over time
=========== ======= =============================

Test Case 2: OMGBenchmark Rally test
------------------------------------

**Description**

OMGBenchmark is a rally plugin for benchmarking oslo.messaging.
The plugin and installation instructions are available on github:
https://github.com/Yulya/omgbenchmark

**Parameters**

================================= =============== =====
Parameter name                    Rally name      Value
================================= =============== =====
oslo.messaging version                            2.5.0
Number of iterations              times           50, 100, 500
Threads count                     concurrency     40, 70, 100
Number of RPC servers             num_servers     10
Number of RPC clients             num_clients     10
Number of topics                  num_topics      5
Number of messages per iteration  num_messages    100
Message size                      msg_length_file 900-12000 bytes
================================= =============== =====

**Measurements**

======= ================= ==========================================
Name    Measurement Units Description
======= ================= ==========================================
min     sec               Minimal execution time of one iteration
median  sec               Median execution time
90%ile  sec               90th percentile execution time
95%ile  sec               95th percentile execution time
max     sec               Maximal execution time of one iteration
avg     sec               Average execution time
success none              Number of successfully finished iterations
count   none              Number of executed iterations
======= ================= ==========================================

**Result Type**

=================  =======================  =========================
Result type        Measurement Units        Description
=================  =======================  =========================
Throughput Graph   msg size vs median       Graph
Concurrency Graph  concurrency vs median    Graph
=================  =======================  =========================
