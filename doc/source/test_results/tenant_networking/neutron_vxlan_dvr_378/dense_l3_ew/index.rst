.. _openstack_l3_east_west_dense:

OpenStack L3 East-West Performance within single compute node
*************************************************************

In this scenario Shaker launches pairs of instances on the same compute node.
Instances are connected to different tenant networks connected to one router.
The traffic goes from one network to the other (L3 east-west).

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - double_room
      - density: 8
      - compute_nodes: 1
      template: l3_east_west.hot
    description: In this scenario Shaker launches pairs of instances on the same compute
      node. Instances are connected to different tenant networks connected to one router.
      The traffic goes from one network to the other (L3 east-west).
    execution:
      progression: linear
      tests:
      - class: flent
        method: tcp_download
        title: Download
      - class: flent
        method: tcp_upload
        title: Upload
      - class: flent
        method: tcp_bidirectional
        title: Bi-directional
    file_name: shaker/shaker/scenarios/openstack/dense_l3_east_west.yaml
    title: OpenStack L3 East-West Dense

Bi-directional
==============

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_bidirectional
    title: Bi-directional

.. image:: 4e4a93eb-45a9-4036-90ba-e8d012646879.*

**Stats**:

===========  =============  =====================  ===================
concurrency  ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===========  =============  =====================  ===================
          1           1.52                8457.75              8327.69
          2           1.49                8800.78              8801.67
          3           1.62                8043.17              8004.92
          4           1.55                8479.99              8596.77
          5           1.78                7635.20              7622.58
          6           1.90                7069.66              7086.26
          7           2.02                6675.86              6656.08
          8           2.02                6470.81              6446.46
===========  =============  =====================  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-275.domain.tld           1.52                8457.75              8327.69
===================  =============  =====================  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-275.domain.tld           1.39                9440.58              9516.83
node-275.domain.tld           1.59                8160.98              8086.51
===================  =============  =====================  ===================

Concurrency 3
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-275.domain.tld           1.47                8706.72              8862.80
node-275.domain.tld           1.71                7659.76              7527.31
node-275.domain.tld           1.68                7763.02              7624.65
===================  =============  =====================  ===================

Concurrency 4
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-275.domain.tld           1.37                8850.28              9189.17
node-275.domain.tld           1.66                7847.05              7846.57
node-275.domain.tld           1.79                7136.96              7053.48
node-275.domain.tld           1.36               10085.66             10297.87
===================  =============  =====================  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-275.domain.tld           1.36                9686.97              9610.78
node-275.domain.tld           1.89                7059.85              7027.04
node-275.domain.tld           1.67                7987.25              8008.20
node-275.domain.tld           2.18                6139.24              6180.48
node-275.domain.tld           1.77                7302.68              7286.40
===================  =============  =====================  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-275.domain.tld           2.10                6286.37              6188.49
node-275.domain.tld           2.22                5955.32              5843.52
node-275.domain.tld           1.48                9413.73              9623.87
node-275.domain.tld           1.83                7101.78              7238.23
node-275.domain.tld           1.73                7404.99              7383.09
node-275.domain.tld           2.05                6255.81              6240.34
===================  =============  =====================  ===================

Concurrency 7
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-275.domain.tld           2.08                6168.70              6152.67
node-275.domain.tld           1.88                6926.98              6868.13
node-275.domain.tld           2.25                5744.58              5712.43
node-275.domain.tld           1.48                8867.42              8945.64
node-275.domain.tld           2.34                5785.97              5883.03
node-275.domain.tld           1.82                7405.34              7150.14
node-275.domain.tld           2.27                5832.03              5880.53
===================  =============  =====================  ===================

Concurrency 8
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-275.domain.tld           1.77                7084.71              7091.14
node-275.domain.tld           2.33                5679.46              5683.84
node-275.domain.tld           2.15                6087.16              6058.08
node-275.domain.tld           2.21                6017.14              6028.22
node-275.domain.tld           1.99                6576.39              6501.82
node-275.domain.tld           1.84                7010.07              6980.70
node-275.domain.tld           2.06                6302.22              6352.23
node-275.domain.tld           1.82                7009.31              6875.67
===================  =============  =====================  ===================

Download
========

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_download
    title: Download

.. image:: 6e251245-3505-4d8b-b102-c97377ffdf4c.*

**Stats**:

===========  =============  =====================
concurrency  ping_icmp, ms  tcp_download, Mbits/s
===========  =============  =====================
          1           0.78               15881.89
          2           0.75               15510.19
          3           0.73               16571.65
          4           0.79               15301.45
          5           0.86               14437.04
          6           0.87               14113.35
          7           0.98               12694.34
          8           1.00               12262.89
===========  =============  =====================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-275.domain.tld           0.78               15881.89
===================  =============  =====================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-275.domain.tld           0.76               15247.03
node-275.domain.tld           0.74               15773.35
===================  =============  =====================

Concurrency 3
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-275.domain.tld           0.70               16886.26
node-275.domain.tld           0.71               17199.99
node-275.domain.tld           0.77               15628.70
===================  =============  =====================

Concurrency 4
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-275.domain.tld           0.70               16376.26
node-275.domain.tld           0.77               15238.86
node-275.domain.tld           0.73               16570.47
node-275.domain.tld           0.96               13020.20
===================  =============  =====================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-275.domain.tld           1.05               12317.70
node-275.domain.tld           0.71               16836.23
node-275.domain.tld           0.82               14478.83
node-275.domain.tld           0.79               15427.59
node-275.domain.tld           0.92               13124.87
===================  =============  =====================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-275.domain.tld           0.89               14133.96
node-275.domain.tld           0.89               13404.21
node-275.domain.tld           1.01               12714.91
node-275.domain.tld           0.91               13516.74
node-275.domain.tld           0.72               16215.22
node-275.domain.tld           0.80               14695.04
===================  =============  =====================

Concurrency 7
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-275.domain.tld           1.01               12526.78
node-275.domain.tld           1.08               12375.26
node-275.domain.tld           1.00               12247.29
node-275.domain.tld           0.85               13329.27
node-275.domain.tld           0.90               13466.65
node-275.domain.tld           1.13               11618.70
node-275.domain.tld           0.94               13296.40
===================  =============  =====================

Concurrency 8
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-275.domain.tld           1.04               12543.69
node-275.domain.tld           1.04               11794.31
node-275.domain.tld           0.96               12560.19
node-275.domain.tld           1.04               11568.23
node-275.domain.tld           0.88               13299.47
node-275.domain.tld           1.04               11703.82
node-275.domain.tld           1.03               12345.28
node-275.domain.tld           1.00               12288.11
===================  =============  =====================

Upload
======

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_upload
    title: Upload

.. image:: a60fb96b-633e-4d80-9570-f3005b582862.*

**Stats**:

===========  =============  ===================
concurrency  ping_icmp, ms  tcp_upload, Mbits/s
===========  =============  ===================
          1           0.84             17167.63
          2           0.72             19966.74
          3           0.83             17006.97
          4           0.87             16349.17
          5           0.98             14671.08
          6           1.06             13574.77
          7           1.07             12967.83
          8           1.14             12481.79
===========  =============  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-275.domain.tld           0.84             17167.63
===================  =============  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-275.domain.tld           0.73             19687.23
node-275.domain.tld           0.71             20246.26
===================  =============  ===================

Concurrency 3
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-275.domain.tld           0.78             18773.29
node-275.domain.tld           0.82             16864.34
node-275.domain.tld           0.90             15383.29
===================  =============  ===================

Concurrency 4
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-275.domain.tld           0.96             14120.73
node-275.domain.tld           0.89             15999.36
node-275.domain.tld           0.78             18222.04
node-275.domain.tld           0.84             17054.53
===================  =============  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-275.domain.tld           0.99             14385.39
node-275.domain.tld           1.13             12955.86
node-275.domain.tld           0.96             14531.94
node-275.domain.tld           1.02             13953.28
node-275.domain.tld           0.81             17528.92
===================  =============  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-275.domain.tld           0.99             14701.80
node-275.domain.tld           1.07             13396.36
node-275.domain.tld           1.00             13535.07
node-275.domain.tld           1.13             12807.53
node-275.domain.tld           0.99             14619.33
node-275.domain.tld           1.19             12388.53
===================  =============  ===================

Concurrency 7
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-275.domain.tld           0.95             15082.15
node-275.domain.tld           1.02             12995.54
node-275.domain.tld           1.03             13800.15
node-275.domain.tld           1.15             11982.45
node-275.domain.tld           1.12             12270.46
node-275.domain.tld           1.12             11981.77
node-275.domain.tld           1.11             12662.30
===================  =============  ===================

Concurrency 8
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-275.domain.tld           1.18             12192.89
node-275.domain.tld           1.27             11128.53
node-275.domain.tld           1.07             12911.47
node-275.domain.tld           0.92             14827.95
node-275.domain.tld           1.24             11961.62
node-275.domain.tld           1.27             11163.74
node-275.domain.tld           1.19             11914.73
node-275.domain.tld           0.98             13753.36
===================  =============  ===================

