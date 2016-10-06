.. _openstack_l2_dense:

OpenStack L2 Performance within single compute node
***************************************************

In this scenario Shaker launches several pairs of instances on a single compute
node. Instances are plugged into the same tenant network. The traffic goes
within the tenant network (L2 domain).

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - double_room
      - density: 8
      - compute_nodes: 1
      template: l2.hot
    description: In this scenario Shaker launches several pairs of instances on a single
      compute node. Instances are plugged into the same tenant network. The traffic goes
      within the tenant network (L2 domain).
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
    file_name: shaker/shaker/scenarios/openstack/dense_l2.yaml
    title: OpenStack L2 Dense

Bi-directional
==============

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_bidirectional
    title: Bi-directional

.. image:: 0aa74b7c-f80a-4015-830f-84cde77bc7c1.*

**Stats**:

===========  =============  =====================  ===================
concurrency  ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===========  =============  =====================  ===================
          1           1.47                8932.92              8731.85
          2           1.42                9018.73              9050.41
          3           1.52                8394.38              8367.59
          4           1.38                9170.84              9145.60
          5           1.31               10104.35              9976.37
          6           1.47                8993.65              8909.14
          7           1.57                8222.63              8158.56
          8           1.80                7258.13              7210.99
===========  =============  =====================  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-141.domain.tld           1.47                8932.92              8731.85
===================  =============  =====================  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-141.domain.tld           1.41                9017.37              9067.10
node-141.domain.tld           1.43                9020.09              9033.72
===================  =============  =====================  ===================

Concurrency 3
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-141.domain.tld           1.45                8787.73              8743.41
node-141.domain.tld           1.47                8724.54              8706.40
node-141.domain.tld           1.64                7670.87              7652.98
===================  =============  =====================  ===================

Concurrency 4
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-141.domain.tld           1.42                8678.19              8641.71
node-141.domain.tld           1.75                7710.73              7750.88
node-141.domain.tld           0.98               11529.86             11349.28
node-141.domain.tld           1.39                8764.57              8840.53
===================  =============  =====================  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-141.domain.tld           1.61                8258.34              8172.89
node-141.domain.tld           1.40                9481.39              9450.14
node-141.domain.tld           1.08               11532.37             11445.50
node-141.domain.tld           1.57                8344.98              8230.28
node-141.domain.tld           0.91               12904.68             12583.05
===================  =============  =====================  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-141.domain.tld           1.81                7406.28              7345.23
node-141.domain.tld           1.02               11434.87             11142.51
node-141.domain.tld           1.29                9507.96              9382.82
node-141.domain.tld           1.29               10045.68             10089.79
node-141.domain.tld           1.73                7691.97              7666.05
node-141.domain.tld           1.68                7875.17              7828.46
===================  =============  =====================  ===================

Concurrency 7
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-141.domain.tld           1.61                7989.37              7895.56
node-141.domain.tld           1.52                8237.34              8123.65
node-141.domain.tld           1.53                8538.53              8476.13
node-141.domain.tld           1.89                6885.80              6855.69
node-141.domain.tld           1.24                9843.51              9674.68
node-141.domain.tld           1.65                7604.83              7577.78
node-141.domain.tld           1.55                8459.05              8506.46
===================  =============  =====================  ===================

Concurrency 8
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-141.domain.tld           1.50                8584.58              8455.17
node-141.domain.tld           1.97                6677.43              6619.24
node-141.domain.tld           1.56                8131.01              8136.20
node-141.domain.tld           1.96                6647.47              6640.80
node-141.domain.tld           2.00                6443.56              6425.13
node-141.domain.tld           1.90                6984.43              6871.97
node-141.domain.tld           1.88                6708.52              6693.98
node-141.domain.tld           1.63                7888.02              7845.44
===================  =============  =====================  ===================

Download
========

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_download
    title: Download

.. image:: ed1ea52c-d270-49db-b81c-94511046677b.*

**Stats**:

===========  =============  =====================
concurrency  ping_icmp, ms  tcp_download, Mbits/s
===========  =============  =====================
          1           0.70               17174.86
          2           0.75               16343.71
          3           0.79               15061.77
          4           0.79               15045.57
          5           0.87               13991.47
          6           0.94               13250.97
          7           0.95               13230.50
          8           0.98               12729.51
===========  =============  =====================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-141.domain.tld           0.70               17174.86
===================  =============  =====================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-141.domain.tld           0.75               16354.16
node-141.domain.tld           0.74               16333.25
===================  =============  =====================

Concurrency 3
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-141.domain.tld           0.94               13407.88
node-141.domain.tld           0.74               15494.12
node-141.domain.tld           0.70               16283.32
===================  =============  =====================

Concurrency 4
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-141.domain.tld           0.75               15354.06
node-141.domain.tld           0.89               12873.12
node-141.domain.tld           0.75               15783.54
node-141.domain.tld           0.76               16171.55
===================  =============  =====================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-141.domain.tld           0.79               14708.10
node-141.domain.tld           0.96               12132.16
node-141.domain.tld           0.87               14437.94
node-141.domain.tld           0.88               14437.93
node-141.domain.tld           0.82               14241.21
===================  =============  =====================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-141.domain.tld           0.77               15037.82
node-141.domain.tld           1.01               12723.78
node-141.domain.tld           0.91               13645.23
node-141.domain.tld           0.80               14589.91
node-141.domain.tld           1.08               12021.81
node-141.domain.tld           1.09               11487.27
===================  =============  =====================

Concurrency 7
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-141.domain.tld           0.83               14182.20
node-141.domain.tld           0.97               12545.83
node-141.domain.tld           0.94               12665.17
node-141.domain.tld           1.14               11937.60
node-141.domain.tld           0.87               15161.94
node-141.domain.tld           0.87               13544.19
node-141.domain.tld           1.02               12576.59
===================  =============  =====================

Concurrency 8
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-141.domain.tld           1.06               11766.60
node-141.domain.tld           1.06               11854.18
node-141.domain.tld           0.93               13082.38
node-141.domain.tld           1.00               12669.54
node-141.domain.tld           1.13               10735.65
node-141.domain.tld           0.80               15464.54
node-141.domain.tld           1.01               12574.11
node-141.domain.tld           0.90               13689.09
===================  =============  =====================

Upload
======

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_upload
    title: Upload

.. image:: 65b31bdf-ec3f-4017-9a9a-5f8913d6e249.*

**Stats**:

===========  =============  ===================
concurrency  ping_icmp, ms  tcp_upload, Mbits/s
===========  =============  ===================
          1           0.90             15985.96
          2           0.83             16971.57
          3           0.91             15858.46
          4           0.79             17651.69
          5           0.84             16438.54
          6           0.89             15655.78
          7           0.99             14351.86
          8           1.01             14213.86
===========  =============  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-141.domain.tld           0.90             15985.96
===================  =============  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-141.domain.tld           0.74             18265.24
node-141.domain.tld           0.92             15677.91
===================  =============  ===================

Concurrency 3
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-141.domain.tld           0.96             14825.99
node-141.domain.tld           0.93             14878.60
node-141.domain.tld           0.84             17870.81
===================  =============  ===================

Concurrency 4
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-141.domain.tld           0.94             15110.30
node-141.domain.tld           0.79             17212.34
node-141.domain.tld           0.89             16294.36
node-141.domain.tld           0.56             21989.74
===================  =============  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-141.domain.tld           0.70             19377.28
node-141.domain.tld           0.93             14911.98
node-141.domain.tld           0.86             15314.42
node-141.domain.tld           0.90             15643.99
node-141.domain.tld           0.82             16945.03
===================  =============  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-141.domain.tld           0.95             14825.44
node-141.domain.tld           0.73             19108.33
node-141.domain.tld           0.88             15285.79
node-141.domain.tld           0.89             15682.64
node-141.domain.tld           0.88             15163.88
node-141.domain.tld           1.01             13868.61
===================  =============  ===================

Concurrency 7
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-141.domain.tld           1.09             13067.09
node-141.domain.tld           0.98             14422.92
node-141.domain.tld           1.02             13441.86
node-141.domain.tld           0.86             15986.76
node-141.domain.tld           1.06             13036.66
node-141.domain.tld           0.85             16705.04
node-141.domain.tld           1.04             13802.73
===================  =============  ===================

Concurrency 8
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-141.domain.tld           0.88             16555.03
node-141.domain.tld           1.05             13632.18
node-141.domain.tld           1.03             13332.33
node-141.domain.tld           0.90             15874.93
node-141.domain.tld           1.01             13767.51
node-141.domain.tld           1.03             14362.50
node-141.domain.tld           1.06             13227.78
node-141.domain.tld           1.11             12958.61
===================  =============  ===================

