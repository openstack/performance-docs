.. _openstack_l3_north_south_dense:

OpenStack L3 North-South Performance within single compute node
***************************************************************

In this scenario Shaker launches pairs of instances on the same compute node.
Instances are connected to different tenant networks, each connected to own
router. Instances in one of networks have floating IPs. The traffic goes from
one network via external network to the other network.

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - double_room
      - density: 8
      - compute_nodes: 1
      template: l3_north_south.hot
    description: In this scenario Shaker launches pairs of instances on the same compute
      node. Instances are connected to different tenant networks, each connected to own
      router. Instances in one of networks have floating IPs. The traffic goes from one
      network via external network to the other network.
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
    file_name: shaker/shaker/scenarios/openstack/dense_l3_north_south.yaml
    title: OpenStack L3 North-South Dense

Bi-directional
==============

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_bidirectional
    title: Bi-directional

.. image:: ef97118d-c610-4779-a3a9-8f79e6a60fe9.*

**Stats**:

===========  =============  =====================  ===================
concurrency  ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===========  =============  =====================  ===================
          1           6.32                1546.04              2158.92
          2          13.34                 848.30              1152.63
          3           3.66                1233.43              1096.07
          4           6.22                1140.33               876.81
          5           3.40                 935.68               860.99
          6           3.25                 521.32               587.13
          7           4.85                 536.31               468.74
          8           5.80                 468.90               301.11
===========  =============  =====================  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-410.domain.tld           6.32                1546.04              2158.92
===================  =============  =====================  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-410.domain.tld          13.57                 812.12              1135.77
node-410.domain.tld          13.10                 884.47              1169.49
===================  =============  =====================  ===================

Concurrency 3
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-410.domain.tld           1.50                1763.03              1076.26
node-410.domain.tld           8.55                 754.86               990.66
node-410.domain.tld           0.93                1182.42              1221.30
===================  =============  =====================  ===================

Concurrency 4
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-410.domain.tld           1.72                1992.45               929.17
node-410.domain.tld          10.82                 698.61               758.42
node-410.domain.tld           1.60                1312.01               884.43
node-410.domain.tld          10.76                 558.26               935.25
===================  =============  =====================  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-410.domain.tld           5.13                 943.98               886.43
node-410.domain.tld           2.34                1052.92               829.42
node-410.domain.tld           5.02                 563.52              1125.07
node-410.domain.tld           2.14                 732.98               913.07
node-410.domain.tld           2.35                1384.99               550.96
===================  =============  =====================  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-410.domain.tld           2.36                 501.11               568.39
node-410.domain.tld           2.22                 632.64               782.23
node-410.domain.tld           2.20                 567.90               349.99
node-410.domain.tld           6.03                 436.01               489.04
node-410.domain.tld           3.99                 472.03               507.83
node-410.domain.tld           2.74                 518.22               825.30
===================  =============  =====================  ===================

Concurrency 7
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-410.domain.tld           4.39                 596.15               450.79
node-410.domain.tld           4.98                 459.32               368.12
node-410.domain.tld           8.22                 503.66               313.17
node-410.domain.tld           3.42                 564.59               644.54
node-410.domain.tld           3.67                 524.89               653.84
node-410.domain.tld           3.56                 671.12               455.48
node-410.domain.tld           5.67                 434.41               395.21
===================  =============  =====================  ===================

Concurrency 8
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-410.domain.tld           8.74                 625.17               186.65
node-410.domain.tld           3.13                 374.05               435.98
node-410.domain.tld           4.60                 453.88               307.88
node-410.domain.tld           8.27                 483.55               178.31
node-410.domain.tld           4.73                 581.72               278.37
node-410.domain.tld           7.39                 322.35               200.09
node-410.domain.tld           4.37                 380.28               340.41
node-410.domain.tld           5.18                 530.20               481.19
===================  =============  =====================  ===================

Download
========

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_download
    title: Download

.. image:: 8f2c9ba1-3990-4de6-8ddd-4acef9132235.*

**Stats**:

===========  =============  =====================
concurrency  ping_icmp, ms  tcp_download, Mbits/s
===========  =============  =====================
          1           1.33                4729.39
          2           1.37                3654.80
          3           1.82                2177.89
          4           1.50                2182.97
          5           2.26                1790.82
          6           2.05                1508.21
          7           1.07                1299.28
          8           1.84                 993.01
===========  =============  =====================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-410.domain.tld           1.33                4729.39
===================  =============  =====================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-410.domain.tld           1.46                3637.35
node-410.domain.tld           1.28                3672.26
===================  =============  =====================

Concurrency 3
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-410.domain.tld           1.72                1879.20
node-410.domain.tld           1.41                3216.68
node-410.domain.tld           2.34                1437.80
===================  =============  =====================

Concurrency 4
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-410.domain.tld           3.38                2436.53
node-410.domain.tld           0.83                2329.07
node-410.domain.tld           0.88                2144.68
node-410.domain.tld           0.91                1821.59
===================  =============  =====================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-410.domain.tld           2.08                1452.92
node-410.domain.tld           1.32                2404.24
node-410.domain.tld           2.48                1391.38
node-410.domain.tld           1.52                1826.32
node-410.domain.tld           3.90                1879.26
===================  =============  =====================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-410.domain.tld           1.21                1962.90
node-410.domain.tld           1.21                1054.63
node-410.domain.tld           1.67                2020.94
node-410.domain.tld           5.66                1240.59
node-410.domain.tld           1.08                1384.27
node-410.domain.tld           1.48                1385.92
===================  =============  =====================

Concurrency 7
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-410.domain.tld           1.10                1430.96
node-410.domain.tld           1.26                 966.16
node-410.domain.tld           1.11                1338.35
node-410.domain.tld           1.00                1594.95
node-410.domain.tld           1.15                1473.48
node-410.domain.tld           0.84                 931.41
node-410.domain.tld           1.04                1359.67
===================  =============  =====================

Concurrency 8
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-410.domain.tld           1.26                 995.66
node-410.domain.tld           2.36                 760.26
node-410.domain.tld           2.42                1212.19
node-410.domain.tld           1.76                1147.19
node-410.domain.tld           2.03                 993.95
node-410.domain.tld           1.39                 987.38
node-410.domain.tld           1.90                 808.68
node-410.domain.tld           1.56                1038.74
===================  =============  =====================

Upload
======

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_upload
    title: Upload

.. image:: ad7218a9-06cc-49c3-b695-05c8f926056c.*

**Stats**:

===========  =============  ===================
concurrency  ping_icmp, ms  tcp_upload, Mbits/s
===========  =============  ===================
          1           5.12              2898.77
          2           5.68              1999.00
          3           7.00              1878.53
          4           2.88              1819.38
          5           2.32              1209.07
          6           1.24              1242.51
          7           1.83              1021.09
          8           1.71               805.24
===========  =============  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-410.domain.tld           5.12              2898.77
===================  =============  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-410.domain.tld           4.70              2198.43
node-410.domain.tld           6.66              1799.57
===================  =============  ===================

Concurrency 3
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-410.domain.tld           1.84              2370.90
node-410.domain.tld           8.19              1852.47
node-410.domain.tld          10.97              1412.22
===================  =============  ===================

Concurrency 4
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-410.domain.tld           2.60              2198.87
node-410.domain.tld           1.21              2410.40
node-410.domain.tld           3.38              1442.20
node-410.domain.tld           4.34              1226.04
===================  =============  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-410.domain.tld           2.13              1673.02
node-410.domain.tld           1.82              1256.90
node-410.domain.tld           2.44               982.50
node-410.domain.tld           2.27              1266.84
node-410.domain.tld           2.93               866.08
===================  =============  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-410.domain.tld           1.07              1502.23
node-410.domain.tld           1.17              1541.96
node-410.domain.tld           1.29               908.99
node-410.domain.tld           1.54              1007.39
node-410.domain.tld           1.15              1562.41
node-410.domain.tld           1.20               932.07
===================  =============  ===================

Concurrency 7
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-410.domain.tld           2.16               858.05
node-410.domain.tld           1.92              1068.49
node-410.domain.tld           1.68              1153.24
node-410.domain.tld           2.52               888.18
node-410.domain.tld           1.48               934.01
node-410.domain.tld           1.44              1124.57
node-410.domain.tld           1.64              1121.10
===================  =============  ===================

Concurrency 8
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-410.domain.tld           1.42               827.88
node-410.domain.tld           1.92               722.71
node-410.domain.tld           1.61               943.77
node-410.domain.tld           2.25               649.87
node-410.domain.tld           1.49               874.17
node-410.domain.tld           1.43              1046.07
node-410.domain.tld           1.65               657.74
node-410.domain.tld           1.89               719.70
===================  =============  ===================

