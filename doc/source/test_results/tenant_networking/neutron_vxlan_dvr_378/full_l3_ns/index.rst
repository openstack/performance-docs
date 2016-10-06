.. _openstack_l3_north_south:

OpenStack L3 North-South Full
*****************************

In this scenario Shaker launches pairs of instances on different compute nodes.
All available compute nodes are utilized. Instances are in different networks
connected to different routers, master accesses slave by floating ip. The
traffic goes from one network via external network to the other network.

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - single_room
      template: l3_north_south.hot
    description: In this scenario Shaker launches pairs of instances on different compute
      nodes. All available compute nodes are utilized. Instances are in different networks
      connected to different routers, master accesses slave by floating ip. The traffic
      goes from one network via external network to the other network.
    execution:
      progression: quadratic
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
    file_name: shaker/shaker/scenarios/openstack/full_l3_north_south.yaml
    title: OpenStack L3 North-South

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_download 2>&1 | grep "se with" |
        grep -Po '\./\S+'`
      type: script
    concurrency: 92
    executor: flent
    id: 4b8e4a56-42da-427f-9047-8ccca0dd4203
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471049.100292
    stats: {}
    status: lost
    test: Download
    type: agent

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_upload 2>&1 | grep "se with" | grep
        -Po '\./\S+'`
      type: script
    concurrency: 185
    executor: flent
    id: ff8aa237-ee77-455d-b006-89f62fd3df78
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471864.232474
    stats: {}
    status: lost
    test: Upload
    type: agent

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_bidirectional 2>&1 | grep "se with"
        | grep -Po '\./\S+'`
      type: script
    concurrency: 92
    executor: flent
    id: bf47bc47-6f16-44c7-b66c-58fb37e193b4
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472472497.609532
    stats: {}
    status: lost
    test: Bi-directional
    type: agent

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_bidirectional 2>&1 | grep "se with"
        | grep -Po '\./\S+'`
      type: script
    concurrency: 46
    executor: flent
    id: f8f785d2-1dcc-4ded-88dd-caa5c6a737f8
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472472407.102942
    stats: {}
    status: lost
    test: Bi-directional
    type: agent

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_download 2>&1 | grep "se with" |
        grep -Po '\./\S+'`
      type: script
    concurrency: 185
    executor: flent
    id: 1134389b-8f1d-4401-8232-0689d855a283
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471139.837024
    stats: {}
    status: lost
    test: Download
    type: agent

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_upload 2>&1 | grep "se with" | grep
        -Po '\./\S+'`
      type: script
    concurrency: 92
    executor: flent
    id: caad76d9-33ba-4612-bc56-ef26be8d6aae
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471773.72396
    stats: {}
    status: lost
    test: Upload
    type: agent

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_download 2>&1 | grep "se with" |
        grep -Po '\./\S+'`
      type: script
    concurrency: 46
    executor: flent
    id: 09efa63f-40e9-471e-92c8-b79a2842eb1a
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472470890.994513
    stats: {}
    status: lost
    test: Download
    type: agent

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_upload 2>&1 | grep "se with" | grep
        -Po '\./\S+'`
      type: script
    concurrency: 46
    executor: flent
    id: 305577d3-e5d5-4cae-b216-1d589af11578
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471683.220475
    stats: {}
    status: lost
    test: Upload
    type: agent

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_bidirectional 2>&1 | grep "se with"
        | grep -Po '\./\S+'`
      type: script
    concurrency: 185
    executor: flent
    id: 8ee3171a-ef51-40ff-89b4-a3f4ed70640a
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472472630.581052
    stats: {}
    status: lost
    test: Bi-directional
    type: agent

Bi-directional
==============

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_bidirectional
    title: Bi-directional

.. image:: 90471cd9-3e4c-4b1a-a562-90b639e48042.*

**Stats**:

===========  =============  =====================  ===================
concurrency  ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===========  =============  =====================  ===================
          1           0.98                2388.14              4415.22
          2           1.47                1160.43               914.84
          5           1.79                 923.28              1170.83
         11           3.37                 450.76               665.91
         23          17.12                 142.30               475.86
         46          38.88                 100.47               226.09
         92          59.53                  50.56               113.15
        185          64.49                  22.84                58.22
===========  =============  =====================  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-146.domain.tld           0.98                2388.14              4415.22
===================  =============  =====================  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-146.domain.tld           1.67                 869.38               857.18
node-74.domain.tld            1.26                1451.49               972.51
===================  =============  =====================  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-146.domain.tld           1.76                1085.90              1236.02
node-36.domain.tld            2.14                 926.36               810.16
node-49.domain.tld            1.61                1079.81              1736.14
node-65.domain.tld            1.39                 836.65              1062.18
node-74.domain.tld            2.06                 687.70              1009.64
===================  =============  =====================  ===================

Concurrency 11
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-1.domain.tld             4.85                 252.76               407.66
node-146.domain.tld           3.18                 205.84              1000.22
node-36.domain.tld           11.22                 215.06               418.33
node-42.domain.tld            0.70                 171.28               384.23
node-45.domain.tld            1.54                 239.54               386.97
node-46.domain.tld            1.41                 520.82               980.10
node-49.domain.tld            4.46                 178.36               406.68
node-506.domain.tld           1.22                1748.53               407.51
node-65.domain.tld            5.12                 592.20              1022.39
node-68.domain.tld            2.34                 460.86              1716.71
node-74.domain.tld            1.01                 373.12               194.24
===================  =============  =====================  ===================

Concurrency 23
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-1.domain.tld            30.25                  22.23               241.09
node-123.domain.tld           2.34                 130.39               209.06
node-146.domain.tld          21.72                  32.85               246.75
node-334.domain.tld          19.91                  57.62               430.78
node-36.domain.tld           15.63                  63.95               154.80
node-393.domain.tld          55.06                 108.93               132.24
node-404.domain.tld          19.19                 101.42               101.92
node-42.domain.tld           15.47                 121.87               194.50
node-45.domain.tld           16.87                  25.19               237.33
node-46.domain.tld           14.41                  36.02               301.86
node-470.domain.tld          28.05                 146.96               129.34
node-483.domain.tld           2.16                 271.14               436.41
node-484.domain.tld          11.18                  78.27               773.82
node-49.domain.tld           24.20                  22.04               257.51
node-493.domain.tld           2.49                 155.85              2118.84
node-501.domain.tld           6.97                 240.77               516.47
node-505.domain.tld          12.81                 288.11              1536.87
node-506.domain.tld           1.17                 136.50               524.87
node-519.domain.tld          23.54                 343.99               271.63
node-65.domain.tld           15.13                  96.35               145.56
node-68.domain.tld           14.34                   6.78               262.95
node-74.domain.tld           13.86                  28.83               132.10
node-84.domain.tld           27.05                 756.74              1588.06
===================  =============  =====================  ===================

Concurrency 46
--------------

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_bidirectional 2>&1 | grep "se with"
        | grep -Po '\./\S+'`
      type: script
    concurrency: 46
    executor: flent
    id: f8f785d2-1dcc-4ded-88dd-caa5c6a737f8
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472472407.102942
    stats: {}
    status: lost
    test: Bi-directional
    type: agent

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-1.domain.tld            66.40                  51.82                 9.28
node-123.domain.tld           3.49                   8.72               821.00
node-137.domain.tld           3.10                 118.07               289.40
node-146.domain.tld          17.62                  30.78                71.01
node-149.domain.tld         188.71                   4.55               125.47
node-192.domain.tld          21.45                  19.82               105.63
node-195.domain.tld          67.74                 612.24               140.65
node-199.domain.tld          19.45                  76.93               770.26
node-209.domain.tld         114.54                  12.73                36.08
node-211.domain.tld         105.71                  14.86               529.67
node-213.domain.tld           3.09                  34.91               123.43
node-214.domain.tld          55.47                 124.71                34.82
node-224.domain.tld           3.32                 305.87                18.01
node-241.domain.tld           2.66                 106.30                45.01
node-334.domain.tld           1.71                  49.08               114.60
node-335.domain.tld           4.44                  86.22               761.37
node-36.domain.tld           55.57                 483.21                37.85
node-393.domain.tld          17.34                  81.65                33.10
node-404.domain.tld          37.93                  31.80               137.68
node-42.domain.tld          130.68                   8.73                34.76
node-435.domain.tld          21.69                  21.71                35.69
node-436.domain.tld          19.85                  34.54               446.61
node-438.domain.tld          25.76                  52.80                37.47
node-446.domain.tld         101.81                  26.60               459.11
node-447.domain.tld          22.78                  55.60               123.19
node-448.domain.tld          45.01                 252.39                36.61
node-45.domain.tld            3.45                 215.25                36.60
node-458.domain.tld           4.31                  56.97               139.28
node-46.domain.tld            4.52                 427.79                37.03
node-470.domain.tld          15.62                  17.77               213.41
node-474.domain.tld         126.10                  33.82               141.66
node-483.domain.tld           5.76                  34.99                33.20
node-484.domain.tld           3.53                   6.70                29.25
node-49.domain.tld           41.74                 259.52               651.87
node-493.domain.tld           9.03                   4.43               274.52
node-501.domain.tld          25.03                  31.07               122.26
node-505.domain.tld          17.96                  12.72               139.03
node-506.domain.tld           2.67                 165.17                86.46
node-515.domain.tld          46.44                  21.72               992.59
node-516.domain.tld           4.40                  18.97               101.61
node-519.domain.tld          90.50                  42.89               691.80
node-65.domain.tld           17.60                 318.05                15.79
node-68.domain.tld          102.55                  56.40               139.47
node-74.domain.tld            3.65                  59.26               787.13
node-84.domain.tld           67.52                  31.19               163.42
===================  =============  =====================  ===================

Concurrency 92
--------------

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_bidirectional 2>&1 | grep "se with"
        | grep -Po '\./\S+'`
      type: script
    concurrency: 92
    executor: flent
    id: bf47bc47-6f16-44c7-b66c-58fb37e193b4
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472472497.609532
    stats: {}
    status: lost
    test: Bi-directional
    type: agent

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-1.domain.tld           451.75                   3.18               141.82
node-123.domain.tld          39.18                  39.99                50.40
node-129.domain.tld          44.18                 121.30                 4.82
node-130.domain.tld          42.67                  10.20                19.28
node-133.domain.tld          36.63                  20.66                 3.93
node-137.domain.tld          41.54                  14.27               136.16
node-146.domain.tld          48.79                 148.62                43.74
node-149.domain.tld          86.14                  30.46               206.08
node-192.domain.tld          95.37                  48.84                45.52
node-195.domain.tld         462.64                  55.70               486.47
node-199.domain.tld           9.02                  11.58               139.19
node-209.domain.tld          45.10                  42.34               219.72
node-211.domain.tld          23.84                 164.76                48.25
node-213.domain.tld          11.41                  46.16                22.24
node-214.domain.tld          96.40                  39.66               241.68
node-224.domain.tld          63.31                  86.53                29.09
node-24.domain.tld          114.05                  25.45                60.34
node-241.domain.tld          24.36                 153.74                82.83
node-264.domain.tld          24.29                  46.84                42.48
node-268.domain.tld          12.28                  34.91                43.61
node-271.domain.tld          11.76                  24.24               278.73
node-272.domain.tld          64.49                  12.40               109.97
node-28.domain.tld           50.31                   0.23               127.72
node-303.domain.tld          20.45                  33.71               149.68
node-310.domain.tld         111.84                  13.45                61.88
node-319.domain.tld         111.33                   2.08                64.65
node-320.domain.tld          25.85                  20.97                87.29
node-326.domain.tld          35.70                  16.50                56.37
node-334.domain.tld          42.43                   4.79                58.55
node-335.domain.tld          54.28                  22.48                64.53
node-336.domain.tld           9.44                  33.45                99.15
node-339.domain.tld          91.38                  14.11                51.10
node-345.domain.tld          32.59                  73.85                82.88
node-36.domain.tld          176.85                  38.77                59.47
node-366.domain.tld          35.46                   2.88                26.63
node-367.domain.tld          61.60                  86.42                89.28
node-375.domain.tld          32.42                  42.45                60.07
node-381.domain.tld          27.50                  45.39                62.15
node-383.domain.tld          38.38                  51.59               153.12
node-384.domain.tld          36.58                  37.97                40.11
node-387.domain.tld          36.20                  81.53               155.10
node-388.domain.tld          39.32                  42.47                45.30
node-393.domain.tld         135.06                   0.79               127.65
node-404.domain.tld          95.06                   4.18               115.87
node-411.domain.tld         136.88                   1.84                79.47
node-412.domain.tld         100.47                  34.39                77.21
node-415.domain.tld          66.81                  17.71               252.59
node-42.domain.tld           88.80                  15.94                17.20
node-421.domain.tld          55.92                  77.23               825.02
node-422.domain.tld          14.62                  92.73                68.78
node-426.domain.tld          97.65                  26.45               234.63
node-428.domain.tld          15.05                  22.43               156.12
node-435.domain.tld          18.85                  37.68               126.26
node-436.domain.tld           9.78                 442.59               354.16
node-438.domain.tld          41.89                  51.81               139.17
node-446.domain.tld          19.68                  35.01               135.23
node-447.domain.tld          38.23                  39.61                81.06
node-448.domain.tld           7.84                  59.91                18.05
node-45.domain.tld           57.04                  11.44                10.92
node-452.domain.tld          62.08                  14.34                34.38
node-458.domain.tld          12.47                  40.40                75.81
node-46.domain.tld           39.41                  28.15                69.52
node-461.domain.tld          84.71                  20.63               321.62
node-464.domain.tld          68.42                 168.79               145.58
node-468.domain.tld           9.16                  34.33                60.98
node-470.domain.tld         102.88                  11.00               124.37
node-474.domain.tld         104.75                  41.02               118.59
node-483.domain.tld           9.07                  43.24               204.68
node-484.domain.tld          19.44                  49.04               506.27
node-49.domain.tld           80.73                   2.90               137.22
node-491.domain.tld          74.35                  97.63                33.48
node-493.domain.tld          21.46                  44.23                29.33
node-495.domain.tld          57.27                  44.78                14.52
node-499.domain.tld          29.73                  36.90               129.81
node-50.domain.tld           36.78                   0.75               102.83
node-500.domain.tld          64.57                  30.18                40.02
node-501.domain.tld          30.34                  23.58                31.16
node-504.domain.tld          47.21                   5.61               505.08
node-505.domain.tld          73.09                  45.87                56.63
node-506.domain.tld          10.77                  70.63               208.43
node-509.domain.tld          22.28                 124.40               125.61
node-515.domain.tld          21.13                  18.95                15.70
node-516.domain.tld           8.76                  37.78                18.81
node-519.domain.tld          28.23                  20.42                42.41
node-56.domain.tld           36.43                  23.62                10.18
node-58.domain.tld           72.88                  48.74                33.27
node-65.domain.tld           91.70                  13.95                95.98
node-68.domain.tld           47.05                 203.21                14.72
node-73.domain.tld           62.68                  25.09                 3.70
node-74.domain.tld           40.87                 369.40                17.61
node-84.domain.tld           27.85                  42.91                97.64
===================  =============  =====================  ===================

Concurrency 185
---------------

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_bidirectional 2>&1 | grep "se with"
        | grep -Po '\./\S+'`
      type: script
    concurrency: 185
    executor: flent
    id: 8ee3171a-ef51-40ff-89b4-a3f4ed70640a
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472472630.581052
    stats: {}
    status: lost
    test: Bi-directional
    type: agent

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-1.domain.tld           507.55                  41.92                58.55
node-103.domain.tld          11.26                   4.05               118.43
node-117.domain.tld          17.15                  27.21                36.99
node-121.domain.tld          34.45                   3.08                33.24
node-123.domain.tld          40.67                  31.37                19.02
node-127.domain.tld          19.42                   6.28                20.81
node-129.domain.tld           6.57                  36.78                48.83
node-130.domain.tld          65.03                 102.23                83.98
node-133.domain.tld           9.54                   6.75                61.70
node-136.domain.tld          55.77                  26.15                15.65
node-137.domain.tld          31.45                   9.07                19.99
node-138.domain.tld          70.44                   2.81                43.73
node-142.domain.tld          14.07                   3.02                19.72
node-146.domain.tld          17.78                  64.91                33.80
node-149.domain.tld          17.81                   9.87                31.48
node-150.domain.tld          95.66                  12.58                16.06
node-153.domain.tld          30.36                   5.82                73.61
node-158.domain.tld          28.53                  31.03               102.52
node-162.domain.tld          44.52                   3.57                11.28
node-173.domain.tld         530.91                   9.19                15.13
node-175.domain.tld          19.96                   1.90                41.64
node-177.domain.tld          90.09                   6.21                36.21
node-180.domain.tld         128.55                  32.62                98.88
node-182.domain.tld          76.34                   2.92                44.39
node-185.domain.tld          95.28                  13.86                65.65
node-188.domain.tld          41.05                  50.53                62.15
node-192.domain.tld           7.85                   1.45                37.81
node-195.domain.tld         433.77                  17.74                60.35
node-199.domain.tld          11.54                  11.10               171.19
node-201.domain.tld           7.44                  27.05                33.58
node-202.domain.tld         348.39                  51.13                28.18
node-209.domain.tld          28.89                  20.40                72.06
node-211.domain.tld          15.12                  61.39                31.62
node-213.domain.tld           7.54                   9.09                34.50
node-214.domain.tld          36.98                   1.73                91.50
node-224.domain.tld          33.37                   8.24                16.75
node-226.domain.tld          30.77                  10.91                32.92
node-228.domain.tld          44.84                   4.85                23.19
node-233.domain.tld          66.53                   6.19                16.62
node-236.domain.tld          13.53                  46.23                35.24
node-237.domain.tld          35.65                  20.42                65.80
node-24.domain.tld           73.44                  59.55                81.89
node-241.domain.tld          28.52                   6.34                60.39
node-248.domain.tld         529.66                  12.84                86.95
node-254.domain.tld          32.59                   9.78                47.41
node-264.domain.tld          26.80                   5.36                31.52
node-267.domain.tld          16.72                  12.30                13.74
node-268.domain.tld          61.04                  19.37                35.59
node-271.domain.tld          12.39                  17.14                23.31
node-272.domain.tld         116.35                  46.82                16.08
node-275.domain.tld          87.37                   9.56                84.37
node-277.domain.tld           7.75                  58.00                23.27
node-28.domain.tld            5.11                 100.03                61.36
node-280.domain.tld          10.61                  13.17                51.53
node-284.domain.tld          68.06                  41.19                48.58
node-286.domain.tld          20.62                   5.31                87.85
node-288.domain.tld          35.41                   5.74                28.02
node-289.domain.tld          43.05                  12.99                80.04
node-291.domain.tld         521.20                  32.81                94.14
node-292.domain.tld          14.83                  19.18                34.31
node-297.domain.tld         332.01                  90.99                88.12
node-298.domain.tld          16.21                   6.18                60.49
node-303.domain.tld          14.29                  16.94                78.80
node-304.domain.tld           4.45                  29.60                31.98
node-309.domain.tld          30.29                  16.62                68.71
node-310.domain.tld         115.80                   4.35                13.94
node-312.domain.tld          11.37                  28.05                88.71
node-313.domain.tld          16.91                  52.44                15.96
node-315.domain.tld          28.48                   9.97                45.78
node-317.domain.tld          78.80                  20.67                49.06
node-319.domain.tld          21.83                  71.34                49.54
node-320.domain.tld         101.03                   2.19                39.38
node-326.domain.tld          29.14                   9.44                 9.21
node-327.domain.tld          79.20                  16.32                18.69
node-334.domain.tld          30.36                  10.34               204.38
node-335.domain.tld          45.53                  74.03               136.49
node-336.domain.tld          67.32                  34.88                40.04
node-339.domain.tld          16.62                   6.22               197.83
node-341.domain.tld          26.83                  43.47                 6.31
node-344.domain.tld           6.12                  72.06                97.44
node-345.domain.tld          46.88                  11.26                12.14
node-348.domain.tld           6.92                  33.71                75.97
node-351.domain.tld           5.14                  59.28                43.76
node-353.domain.tld          11.27                   8.03                38.93
node-355.domain.tld          26.23                  10.43                 4.96
node-357.domain.tld           3.58                  36.95               131.55
node-36.domain.tld           22.49                   9.17                49.16
node-366.domain.tld          61.46                  46.52                28.20
node-367.domain.tld          40.14                   5.50                38.47
node-370.domain.tld          66.36                  56.30                63.78
node-375.domain.tld          30.44                  26.78               252.07
node-379.domain.tld          16.78                   2.80                18.48
node-38.domain.tld            8.00                  66.61                73.87
node-381.domain.tld          71.04                   4.13                57.88
node-383.domain.tld          29.58                  15.72                41.65
node-384.domain.tld         113.16                   4.22                20.86
node-387.domain.tld          55.57                  46.23                58.80
node-388.domain.tld          75.24                  13.12                87.87
node-389.domain.tld          25.79                  15.76                12.98
node-39.domain.tld           73.75                   6.84               110.27
node-393.domain.tld          79.15                  12.04               123.53
node-400.domain.tld         511.45                  15.81                60.49
node-401.domain.tld          73.21                   9.35                20.55
node-403.domain.tld          15.34                  10.93                18.10
node-404.domain.tld          61.61                  23.87               116.75
node-409.domain.tld          50.04                   5.91               118.88
node-41.domain.tld           71.56                   7.23               209.71
node-410.domain.tld          13.44                  30.03                55.14
node-411.domain.tld          78.20                  48.59               118.44
node-412.domain.tld          75.85                  12.22                41.49
node-413.domain.tld          11.62                   4.74                13.77
node-415.domain.tld          29.27                  97.63                63.78
node-416.domain.tld           7.40                   8.57                19.15
node-42.domain.tld           23.32                  35.20                39.02
node-421.domain.tld          15.73                  14.06                11.33
node-422.domain.tld         115.52                   1.73                14.01
node-423.domain.tld          22.25                   7.32                41.14
node-426.domain.tld          64.12                   6.17               148.98
node-427.domain.tld          64.49                  25.35                61.92
node-428.domain.tld          41.33                  33.99                81.35
node-430.domain.tld          78.41                   9.75               110.89
node-435.domain.tld          18.75                  46.68                24.76
node-436.domain.tld          19.56                  18.10                75.31
node-438.domain.tld          56.54                   4.42                 8.84
node-446.domain.tld          86.70                   8.48                31.46
node-447.domain.tld          53.61                  14.78                16.10
node-448.domain.tld           7.28                   2.72               203.65
node-45.domain.tld           31.91                  21.41                67.03
node-452.domain.tld          26.24                   8.33                31.79
node-453.domain.tld           2.60                  21.69               184.17
node-454.domain.tld          46.57                  54.08               150.44
node-458.domain.tld          67.12                  15.79                57.35
node-46.domain.tld           59.66                  15.24               553.42
node-461.domain.tld          78.88                   8.14                32.85
node-463.domain.tld          17.95                   3.08                60.11
node-464.domain.tld          59.53                  27.18                38.14
node-466.domain.tld          42.90                  62.28                97.40
node-468.domain.tld          17.11                  16.59                63.11
node-470.domain.tld          31.62                  14.16                28.38
node-472.domain.tld          15.73                   4.01                16.29
node-474.domain.tld         101.00                  15.34                13.86
node-476.domain.tld          10.02                  19.45                40.22
node-479.domain.tld          17.01                  24.44                47.09
node-482.domain.tld          62.17                   3.78                21.81
node-483.domain.tld         144.77                  11.14                31.26
node-484.domain.tld          57.43                  11.05                26.65
node-485.domain.tld          10.47                   9.90                68.52
node-486.domain.tld          87.85                   1.32                55.04
node-489.domain.tld          87.84                  16.18               102.68
node-49.domain.tld           57.57                  14.82                69.41
node-491.domain.tld          64.15                   3.92                32.70
node-493.domain.tld          16.86                   3.40                31.95
node-495.domain.tld          35.83                   4.71                18.97
node-496.domain.tld          65.01                  26.61                 7.06
node-499.domain.tld         106.61                  11.01                10.27
node-50.domain.tld            7.04                  19.70                20.83
node-500.domain.tld           9.57                   3.41                18.92
node-501.domain.tld          74.29                  18.30                24.00
node-504.domain.tld         127.92                  15.07                94.55
node-505.domain.tld          29.96                  15.55                34.68
node-506.domain.tld           7.47                   3.81                28.58
node-509.domain.tld          20.37                   4.23                77.27
node-510.domain.tld         347.61                  13.11                65.69
node-511.domain.tld          80.84                  14.84                20.04
node-512.domain.tld          72.32                  12.72                41.30
node-514.domain.tld          65.71                  41.79                21.57
node-515.domain.tld          66.16                   5.82                42.87
node-516.domain.tld          66.11                   2.30                94.12
node-519.domain.tld          45.41                  37.75                 6.77
node-522.domain.tld           8.04                  49.68                 9.30
node-56.domain.tld           58.39                   7.71                83.79
node-57.domain.tld           19.00                   3.16                14.04
node-58.domain.tld           99.21                  85.95                16.65
node-61.domain.tld           14.73                  20.95                59.77
node-62.domain.tld           42.77                 110.98                42.24
node-65.domain.tld           11.89                  88.04                11.34
node-68.domain.tld            5.04                  52.29                94.46
node-73.domain.tld          119.60                  64.95                66.38
node-74.domain.tld           27.13                  16.45               131.27
node-83.domain.tld           46.53                  57.33                55.43
node-84.domain.tld           11.67                  22.09                15.79
node-96.domain.tld          340.29                  19.62                91.58
node-98.domain.tld           51.29                   1.76                62.86
node-99.domain.tld           25.45                   2.81                42.59
===================  =============  =====================  ===================

Download
========

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_download
    title: Download

.. image:: c79bf246-828a-4a7e-af0e-f93193153217.*

**Stats**:

===========  =============  =====================
concurrency  ping_icmp, ms  tcp_download, Mbits/s
===========  =============  =====================
          1           1.03                1462.85
          2           0.92                3263.51
          5           1.44                1505.75
         11           1.86                1003.01
         23           1.79                 588.82
         46           2.15                 261.56
         92           4.37                 104.01
        185           8.81                  67.22
===========  =============  =====================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-146.domain.tld           1.03                1462.85
===================  =============  =====================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-146.domain.tld           1.20                1478.25
node-74.domain.tld            0.64                5048.78
===================  =============  =====================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-146.domain.tld           0.83                2420.71
node-36.domain.tld            1.60                1406.24
node-49.domain.tld            1.67                1178.70
node-65.domain.tld            1.58                1265.11
node-74.domain.tld            1.51                1257.99
===================  =============  =====================

Concurrency 11
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-1.domain.tld             1.82                1063.56
node-146.domain.tld           1.20                 735.49
node-36.domain.tld            2.34                 901.18
node-42.domain.tld            1.14                1111.10
node-45.domain.tld            3.59                 974.88
node-46.domain.tld            1.56                 433.79
node-49.domain.tld            1.94                 879.76
node-506.domain.tld           1.77                2021.62
node-65.domain.tld            3.21                 748.77
node-68.domain.tld            0.87                1391.30
node-74.domain.tld            1.06                 771.63
===================  =============  =====================

Concurrency 23
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-1.domain.tld             2.97                 421.58
node-123.domain.tld           2.13                 454.97
node-146.domain.tld           1.62                 718.54
node-334.domain.tld           1.40                 674.25
node-36.domain.tld            0.88                 479.95
node-393.domain.tld           2.16                 567.88
node-404.domain.tld           1.87                 301.70
node-42.domain.tld            1.30                 267.78
node-45.domain.tld            1.10                 233.76
node-46.domain.tld            1.95                 632.05
node-470.domain.tld           3.07                 652.03
node-483.domain.tld           1.11                 567.20
node-484.domain.tld           1.36                 701.03
node-49.domain.tld            3.31                 453.93
node-493.domain.tld           1.65                 878.37
node-501.domain.tld           1.97                 945.63
node-505.domain.tld           1.38                 542.36
node-506.domain.tld           1.44                1347.65
node-519.domain.tld           1.03                 582.21
node-65.domain.tld            1.55                 796.56
node-68.domain.tld            1.79                 415.47
node-74.domain.tld            2.05                 298.38
node-84.domain.tld            2.10                 609.47
===================  =============  =====================

Concurrency 46
--------------

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_download 2>&1 | grep "se with" |
        grep -Po '\./\S+'`
      type: script
    concurrency: 46
    executor: flent
    id: 09efa63f-40e9-471e-92c8-b79a2842eb1a
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472470890.994513
    stats: {}
    status: lost
    test: Download
    type: agent

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-1.domain.tld             4.01                 860.93
node-123.domain.tld           3.04                  99.51
node-137.domain.tld           2.32                 290.17
node-146.domain.tld           3.26                 791.77
node-149.domain.tld           1.90                 128.86
node-192.domain.tld           1.00                 115.95
node-195.domain.tld           6.58                  85.88
node-199.domain.tld           1.76                 271.51
node-209.domain.tld           1.12                  84.74
node-211.domain.tld           1.36                 327.32
node-213.domain.tld           0.97                  55.40
node-214.domain.tld           2.89                  93.54
node-224.domain.tld           1.18                  80.77
node-241.domain.tld           0.97                  95.96
node-334.domain.tld           2.03                 441.93
node-335.domain.tld           2.84                 293.10
node-36.domain.tld            1.56                 749.93
node-393.domain.tld           3.06                 445.17
node-404.domain.tld           0.97                 373.76
node-42.domain.tld            0.97                 205.52
node-435.domain.tld           1.29                  65.20
node-436.domain.tld           1.86                 364.64
node-438.domain.tld           1.53                  35.80
node-446.domain.tld           1.72                 100.35
node-447.domain.tld           1.59                 442.81
node-448.domain.tld           1.65                  85.54
node-45.domain.tld            1.95                 375.44
node-458.domain.tld           2.20                  78.94
node-46.domain.tld            1.05                 325.24
node-470.domain.tld           6.63                  59.20
node-474.domain.tld           1.45                  75.35
node-483.domain.tld           2.48                  85.93
node-484.domain.tld           2.40                 266.26
node-49.domain.tld            4.54                 313.89
node-493.domain.tld           1.90                 360.52
node-501.domain.tld           2.40                  92.51
node-505.domain.tld           1.16                  68.85
node-506.domain.tld           1.20                  64.51
node-515.domain.tld           1.93                  77.93
node-516.domain.tld           2.14                  68.03
node-519.domain.tld           1.26                 106.24
node-65.domain.tld            2.71                 867.31
node-68.domain.tld            2.18                 907.57
node-74.domain.tld            1.73                 450.19
node-84.domain.tld            1.87                 140.29
===================  =============  =====================

Concurrency 92
--------------

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_download 2>&1 | grep "se with" |
        grep -Po '\./\S+'`
      type: script
    concurrency: 92
    executor: flent
    id: 4b8e4a56-42da-427f-9047-8ccca0dd4203
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471049.100292
    stats: {}
    status: lost
    test: Download
    type: agent

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-1.domain.tld             4.04                 156.14
node-123.domain.tld           2.51                  91.04
node-129.domain.tld           0.93                 162.28
node-130.domain.tld          46.47                 194.70
node-133.domain.tld           1.36                 207.33
node-137.domain.tld           1.47                  94.42
node-146.domain.tld           1.62                 101.12
node-149.domain.tld           2.35                  43.25
node-192.domain.tld           0.80                 121.33
node-195.domain.tld           4.01                  88.09
node-199.domain.tld           1.08                  53.35
node-209.domain.tld           0.77                  67.21
node-211.domain.tld           1.36                  71.84
node-213.domain.tld           1.44                  79.41
node-214.domain.tld           2.51                 113.56
node-224.domain.tld           1.26                  95.02
node-24.domain.tld            4.33                 149.19
node-241.domain.tld           1.09                  40.97
node-264.domain.tld           2.25                  62.30
node-268.domain.tld           2.43                  96.37
node-271.domain.tld          91.41                  83.81
node-272.domain.tld           2.78                  41.91
node-28.domain.tld            2.45                  44.79
node-303.domain.tld          91.22                  67.13
node-310.domain.tld           2.61                 148.91
node-319.domain.tld           1.38                 159.97
node-320.domain.tld           3.52                  88.46
node-326.domain.tld           2.83                  48.96
node-334.domain.tld           1.43                 390.80
node-335.domain.tld           1.22                 139.72
node-336.domain.tld           2.06                  46.92
node-339.domain.tld           3.01                  28.49
node-345.domain.tld           1.18                  89.18
node-36.domain.tld            1.71                  64.46
node-366.domain.tld           2.75                  95.39
node-367.domain.tld           1.31                 137.33
node-375.domain.tld           3.32                  60.89
node-381.domain.tld           2.76                  69.62
node-383.domain.tld           2.41                  68.08
node-384.domain.tld           1.46                  30.14
node-387.domain.tld           2.76                  99.38
node-388.domain.tld           2.38                  65.02
node-393.domain.tld           3.10                 190.74
node-404.domain.tld           1.32                 137.31
node-411.domain.tld           3.07                 203.25
node-412.domain.tld           2.92                  74.96
node-415.domain.tld           2.69                 147.17
node-42.domain.tld            0.99                  81.47
node-421.domain.tld           5.06                  53.54
node-422.domain.tld           1.04                 144.88
node-426.domain.tld           2.43                  99.42
node-428.domain.tld           1.10                  63.88
node-435.domain.tld           2.69                  71.39
node-436.domain.tld           1.17                  55.22
node-438.domain.tld           0.96                  53.75
node-446.domain.tld           0.84                  78.22
node-447.domain.tld           1.12                  63.67
node-448.domain.tld           0.67                  61.85
node-45.domain.tld            2.54                  67.75
node-452.domain.tld           2.30                 153.06
node-458.domain.tld           1.04                 100.90
node-46.domain.tld            1.32                 355.63
node-461.domain.tld           2.95                  58.14
node-464.domain.tld           1.04                  83.30
node-468.domain.tld           0.98                  49.48
node-470.domain.tld           2.62                 134.91
node-474.domain.tld           0.80                  52.01
node-483.domain.tld           1.20                  94.46
node-484.domain.tld           1.11                  58.50
node-49.domain.tld            4.19                 155.10
node-491.domain.tld           0.99                  55.59
node-493.domain.tld           2.58                 150.99
node-495.domain.tld           1.09                  40.94
node-499.domain.tld           0.90                 103.48
node-50.domain.tld            1.39                 383.92
node-500.domain.tld           1.16                  92.80
node-501.domain.tld           2.41                  94.22
node-504.domain.tld           2.14                  48.58
node-505.domain.tld           1.78                  75.58
node-506.domain.tld           0.95                  44.99
node-509.domain.tld           0.85                  24.09
node-515.domain.tld           1.08                  89.62
node-516.domain.tld           0.99                  43.22
node-519.domain.tld           1.00                  96.35
node-56.domain.tld            1.14                 164.59
node-58.domain.tld            1.61                 126.88
node-65.domain.tld            1.61                 141.23
node-68.domain.tld            1.34                  72.17
node-73.domain.tld            4.47                 164.28
node-74.domain.tld            1.46                 296.45
node-84.domain.tld            1.06                  52.99
===================  =============  =====================

Concurrency 185
---------------

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_download 2>&1 | grep "se with" |
        grep -Po '\./\S+'`
      type: script
    concurrency: 185
    executor: flent
    id: 1134389b-8f1d-4401-8232-0689d855a283
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471139.837024
    stats: {}
    status: lost
    test: Download
    type: agent

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-1.domain.tld            85.70                  84.63
node-103.domain.tld           1.66                  22.04
node-117.domain.tld           1.71                  44.85
node-121.domain.tld          10.48                   6.63
node-123.domain.tld          13.82                  13.66
node-127.domain.tld           1.47                   6.18
node-129.domain.tld           3.31                  55.08
node-130.domain.tld           2.05                  27.26
node-133.domain.tld           1.50                  50.67
node-136.domain.tld           6.32                   6.68
node-137.domain.tld           4.00                  15.03
node-138.domain.tld           3.06                   6.49
node-142.domain.tld           5.70                  84.60
node-146.domain.tld           1.16                  28.97
node-149.domain.tld           1.58                 260.86
node-150.domain.tld           1.11                 275.91
node-153.domain.tld           3.14                 188.96
node-158.domain.tld           1.77                   5.66
node-162.domain.tld           1.61                 101.46
node-173.domain.tld          84.48                  12.39
node-175.domain.tld           5.64                 258.51
node-177.domain.tld           1.87                  16.94
node-180.domain.tld           6.25                   5.83
node-182.domain.tld          16.49                  10.75
node-185.domain.tld           7.67                   9.03
node-188.domain.tld           1.24                  52.30
node-192.domain.tld           1.46                   7.39
node-195.domain.tld          66.45                 127.21
node-199.domain.tld           1.48                 322.59
node-201.domain.tld           3.01                   6.84
node-202.domain.tld          56.10                   8.34
node-209.domain.tld           1.45                   8.01
node-211.domain.tld           1.34                 123.24
node-213.domain.tld           1.61                   6.37
node-214.domain.tld          13.11                 294.16
node-224.domain.tld           1.77                  12.60
node-226.domain.tld           4.97                  11.48
node-228.domain.tld           1.64                 160.20
node-233.domain.tld           2.98                  14.38
node-236.domain.tld           2.06                   2.95
node-237.domain.tld          19.35                  12.98
node-24.domain.tld            7.66                  21.26
node-241.domain.tld           4.65                   8.69
node-248.domain.tld          86.53                 222.02
node-254.domain.tld           3.91                 298.39
node-264.domain.tld           4.94                   6.56
node-267.domain.tld           1.56                 145.89
node-268.domain.tld           5.29                   6.09
node-271.domain.tld           2.24                  10.00
node-272.domain.tld           7.17                   3.55
node-275.domain.tld           1.55                  13.51
node-277.domain.tld           2.93                  36.34
node-28.domain.tld            3.63                  23.98
node-280.domain.tld           1.59                  12.36
node-284.domain.tld           3.06                  20.90
node-286.domain.tld           7.65                  40.41
node-288.domain.tld           5.34                 197.91
node-289.domain.tld           1.58                  49.75
node-291.domain.tld          81.96                  40.90
node-292.domain.tld           1.32                  42.32
node-297.domain.tld          60.07                  27.88
node-298.domain.tld           1.90                   0.90
node-303.domain.tld          19.94                 171.06
node-304.domain.tld           1.60                  61.91
node-309.domain.tld          18.84                  45.61
node-310.domain.tld          15.74                  46.97
node-312.domain.tld           1.02                  47.97
node-313.domain.tld           1.51                   0.46
node-315.domain.tld           8.98                  12.79
node-317.domain.tld          19.23                   9.62
node-319.domain.tld           1.42                  66.59
node-320.domain.tld          10.62                  10.17
node-326.domain.tld           4.70                   8.38
node-327.domain.tld           1.86                   6.22
node-334.domain.tld           3.64                  29.00
node-335.domain.tld          21.60                  20.53
node-336.domain.tld           2.50                 266.68
node-339.domain.tld           6.33                   5.25
node-341.domain.tld           5.19                   8.81
node-344.domain.tld           7.00                 137.66
node-345.domain.tld          17.20                  13.23
node-348.domain.tld           3.57                  26.96
node-351.domain.tld           1.33                 254.91
node-353.domain.tld           1.42                 189.98
node-355.domain.tld           1.40                   6.31
node-357.domain.tld           3.22                  19.70
node-36.domain.tld            2.70                 145.28
node-366.domain.tld           6.16                 292.49
node-367.domain.tld           2.64                  39.04
node-370.domain.tld           1.52                  10.25
node-375.domain.tld           6.80                   4.34
node-379.domain.tld           1.70                  12.81
node-38.domain.tld           14.52                  69.02
node-381.domain.tld           6.68                  10.32
node-383.domain.tld           6.55                  10.97
node-384.domain.tld           1.81                  11.81
node-387.domain.tld          11.61                  19.62
node-388.domain.tld           5.93                   9.34
node-389.domain.tld           6.83                   7.49
node-39.domain.tld            2.34                 191.63
node-393.domain.tld          10.38                  57.41
node-400.domain.tld          83.91                   9.71
node-401.domain.tld           4.71                 182.49
node-403.domain.tld           1.30                  19.59
node-404.domain.tld           3.69                  17.41
node-409.domain.tld           1.84                 348.31
node-41.domain.tld            1.70                  77.85
node-410.domain.tld           1.71                   0.99
node-411.domain.tld           4.92                  59.71
node-412.domain.tld           4.97                  21.36
node-413.domain.tld           3.52                 174.26
node-415.domain.tld           6.55                   3.09
node-416.domain.tld           1.58                  13.72
node-42.domain.tld           18.39                  30.28
node-421.domain.tld           4.96                   5.24
node-422.domain.tld           3.14                  58.60
node-423.domain.tld           5.89                  43.68
node-426.domain.tld           5.49                  15.49
node-427.domain.tld           4.33                 166.82
node-428.domain.tld           1.15                   9.94
node-430.domain.tld           6.76                 234.16
node-435.domain.tld           1.28                  90.39
node-436.domain.tld           2.67                  14.21
node-438.domain.tld           6.56                  12.53
node-446.domain.tld           6.32                   7.12
node-447.domain.tld           2.61                  10.85
node-448.domain.tld           1.32                 197.27
node-45.domain.tld           28.40                  52.98
node-452.domain.tld           3.88                  11.63
node-453.domain.tld           3.22                  48.66
node-454.domain.tld           4.68                  60.36
node-458.domain.tld           1.19                 277.73
node-46.domain.tld            1.42                  12.74
node-461.domain.tld          13.77                   4.27
node-463.domain.tld           1.34                  18.19
node-464.domain.tld           1.61                 113.24
node-466.domain.tld           1.82                  19.21
node-468.domain.tld           3.68                   3.73
node-470.domain.tld           9.46                   4.33
node-472.domain.tld           1.28                  11.82
node-474.domain.tld           2.08                  99.75
node-476.domain.tld           1.48                 144.82
node-479.domain.tld           1.51                  10.45
node-482.domain.tld           2.29                 218.52
node-483.domain.tld           1.40                   9.19
node-484.domain.tld          10.93                   3.22
node-485.domain.tld           2.40                 228.55
node-486.domain.tld          22.40                   2.73
node-489.domain.tld           1.52                  14.16
node-49.domain.tld           16.95                 432.44
node-491.domain.tld           4.13                  12.81
node-493.domain.tld          12.56                   7.43
node-495.domain.tld           3.76                 166.54
node-496.domain.tld          16.15                 102.19
node-499.domain.tld           1.27                  10.04
node-50.domain.tld            1.50                 239.21
node-500.domain.tld           1.09                 104.61
node-501.domain.tld           4.80                  19.59
node-504.domain.tld           5.86                 220.82
node-505.domain.tld           3.54                  17.09
node-506.domain.tld           3.28                   9.97
node-509.domain.tld           1.61                  11.33
node-510.domain.tld          58.91                 176.35
node-511.domain.tld           5.58                   4.63
node-512.domain.tld           6.87                   1.80
node-514.domain.tld           6.06                 148.72
node-515.domain.tld           3.62                   6.90
node-516.domain.tld           3.37                  14.19
node-519.domain.tld           1.52                 115.34
node-522.domain.tld           1.56                  83.53
node-56.domain.tld            1.13                  55.43
node-57.domain.tld            5.27                 172.23
node-58.domain.tld            1.51                 203.10
node-61.domain.tld            1.79                  10.85
node-62.domain.tld           22.72                  28.79
node-65.domain.tld            3.64                   6.69
node-68.domain.tld            1.06                  95.43
node-73.domain.tld           11.27                 131.91
node-74.domain.tld            3.31                  34.23
node-83.domain.tld            5.01                  56.24
node-84.domain.tld            1.63                  10.80
node-96.domain.tld           56.12                   8.24
node-98.domain.tld            4.72                  76.73
node-99.domain.tld            6.62                  17.79
===================  =============  =====================

Upload
======

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_upload
    title: Upload

.. image:: e93831b5-66d4-4904-aad2-0e2de0eca604.*

**Stats**:

===========  =============  ===================
concurrency  ping_icmp, ms  tcp_upload, Mbits/s
===========  =============  ===================
          1           1.37              5557.25
          2           0.80              3278.07
          5           1.00              2162.87
         11           1.71              1228.62
         23           5.69               621.19
         46          11.69               325.27
         92          37.26               173.37
        185          73.29                84.08
===========  =============  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-146.domain.tld           1.37              5557.25
===================  =============  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-146.domain.tld           0.93              5016.40
node-74.domain.tld            0.68              1539.75
===================  =============  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-146.domain.tld           0.96              3094.53
node-36.domain.tld            1.08              1183.78
node-49.domain.tld            1.04              4144.43
node-65.domain.tld            0.84              1148.94
node-74.domain.tld            1.06              1242.66
===================  =============  ===================

Concurrency 11
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-1.domain.tld             2.55               817.07
node-146.domain.tld           1.56               843.80
node-36.domain.tld            1.56              1116.51
node-42.domain.tld            1.04               475.66
node-45.domain.tld            1.24               965.57
node-46.domain.tld            3.24              1195.12
node-49.domain.tld            2.67               506.62
node-506.domain.tld           1.49              1516.70
node-65.domain.tld            1.32              1091.91
node-68.domain.tld            0.73              2011.56
node-74.domain.tld            1.41              2974.36
===================  =============  ===================

Concurrency 23
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-1.domain.tld            12.34               371.11
node-123.domain.tld           1.96               871.15
node-146.domain.tld           7.36               346.90
node-334.domain.tld           7.90               503.90
node-36.domain.tld            7.21               405.28
node-393.domain.tld           9.74               521.13
node-404.domain.tld           6.28               426.49
node-42.domain.tld            6.64               445.97
node-45.domain.tld            7.33               313.78
node-46.domain.tld            7.28               723.02
node-470.domain.tld           4.26              1672.57
node-483.domain.tld           3.19               184.64
node-484.domain.tld           2.82               417.57
node-49.domain.tld           11.79               405.55
node-493.domain.tld           2.87               317.19
node-501.domain.tld           4.19               506.50
node-505.domain.tld           1.14              1246.60
node-506.domain.tld           0.87              1420.48
node-519.domain.tld           3.20              1231.67
node-65.domain.tld            6.86               634.84
node-68.domain.tld            6.78               539.71
node-74.domain.tld            6.51               397.32
node-84.domain.tld            2.29               383.93
===================  =============  ===================

Concurrency 46
--------------

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_upload 2>&1 | grep "se with" | grep
        -Po '\./\S+'`
      type: script
    concurrency: 46
    executor: flent
    id: 305577d3-e5d5-4cae-b216-1d589af11578
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471683.220475
    stats: {}
    status: lost
    test: Upload
    type: agent

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-1.domain.tld            17.50               572.52
node-123.domain.tld           6.59              1091.09
node-137.domain.tld          33.09               128.10
node-146.domain.tld           3.60               104.53
node-149.domain.tld           5.13               558.55
node-192.domain.tld          13.85               154.73
node-195.domain.tld          23.82               103.49
node-199.domain.tld           1.86               255.00
node-209.domain.tld          34.75               262.65
node-211.domain.tld           1.64                25.01
node-213.domain.tld           1.36               138.79
node-214.domain.tld           4.17               366.21
node-224.domain.tld          21.42               457.10
node-241.domain.tld          24.75               151.62
node-334.domain.tld          32.71               101.91
node-335.domain.tld          24.93               132.98
node-36.domain.tld           27.04               102.43
node-393.domain.tld          40.51               575.46
node-404.domain.tld           6.73               371.89
node-42.domain.tld            7.65               346.91
node-435.domain.tld           4.45              1165.31
node-436.domain.tld           5.46               103.32
node-438.domain.tld           5.11               490.91
node-446.domain.tld           3.53               149.74
node-447.domain.tld           2.30              1050.48
node-448.domain.tld           1.62               389.33
node-45.domain.tld            4.57                83.10
node-458.domain.tld           5.31               228.03
node-46.domain.tld            2.37               749.29
node-470.domain.tld           8.80                64.51
node-474.domain.tld           5.21               397.70
node-483.domain.tld           6.38               430.33
node-484.domain.tld          25.63               117.61
node-49.domain.tld           42.58               240.98
node-493.domain.tld           5.06               259.86
node-501.domain.tld          12.48               210.71
node-505.domain.tld           9.07               397.62
node-506.domain.tld           1.24               106.78
node-515.domain.tld          13.94               433.48
node-516.domain.tld           6.47                85.43
node-519.domain.tld           8.82               426.75
node-65.domain.tld            3.72               124.13
node-68.domain.tld            1.70               380.11
node-74.domain.tld            3.20               105.11
node-84.domain.tld            3.96               445.49
===================  =============  ===================

Concurrency 92
--------------

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_upload 2>&1 | grep "se with" | grep
        -Po '\./\S+'`
      type: script
    concurrency: 92
    executor: flent
    id: caad76d9-33ba-4612-bc56-ef26be8d6aae
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471773.72396
    stats: {}
    status: lost
    test: Upload
    type: agent

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-1.domain.tld           498.82               259.43
node-123.domain.tld          35.06                84.64
node-129.domain.tld          25.25               114.61
node-130.domain.tld          23.70               386.75
node-133.domain.tld           9.71                59.17
node-137.domain.tld          10.41               219.81
node-146.domain.tld          14.82              1112.21
node-149.domain.tld           2.14                49.86
node-192.domain.tld          16.78               228.60
node-195.domain.tld         401.70               169.85
node-199.domain.tld          27.48                29.53
node-209.domain.tld           3.62               321.71
node-211.domain.tld           8.40               145.68
node-213.domain.tld           1.83                65.37
node-214.domain.tld          15.48               174.73
node-224.domain.tld           1.67               206.35
node-24.domain.tld           37.53                41.49
node-241.domain.tld           9.80                38.11
node-264.domain.tld          34.95                98.71
node-268.domain.tld          22.30               186.56
node-271.domain.tld           6.41               228.94
node-272.domain.tld          32.53               282.89
node-28.domain.tld           15.93               163.13
node-303.domain.tld           5.88               179.16
node-310.domain.tld          65.22               199.36
node-319.domain.tld           5.80               179.02
node-320.domain.tld          18.61               270.60
node-326.domain.tld           8.20                58.26
node-334.domain.tld          32.19               419.45
node-335.domain.tld          18.52                81.93
node-336.domain.tld          12.79                22.60
node-339.domain.tld          13.74               220.73
node-345.domain.tld           9.65                58.32
node-36.domain.tld            7.58               274.84
node-366.domain.tld          15.92                28.76
node-367.domain.tld          71.65                78.17
node-375.domain.tld           3.60               267.89
node-381.domain.tld          14.38                 5.15
node-383.domain.tld          12.93               114.71
node-384.domain.tld          48.60                73.92
node-387.domain.tld          32.34                53.40
node-388.domain.tld          68.10                88.14
node-393.domain.tld          18.81                49.03
node-404.domain.tld          15.87                 3.88
node-411.domain.tld          23.59                21.24
node-412.domain.tld          22.22               131.32
node-415.domain.tld          37.54               266.81
node-42.domain.tld            7.19                71.95
node-421.domain.tld           9.71               243.34
node-422.domain.tld          48.13               270.73
node-426.domain.tld          80.46               534.58
node-428.domain.tld          80.30               326.23
node-435.domain.tld          24.47                37.51
node-436.domain.tld          11.38                89.97
node-438.domain.tld          13.52               348.64
node-446.domain.tld          64.89                10.78
node-447.domain.tld          68.67                25.92
node-448.domain.tld           7.37               356.56
node-45.domain.tld           29.64                17.52
node-452.domain.tld           7.30               154.51
node-458.domain.tld          21.30                80.77
node-46.domain.tld           13.70                18.48
node-461.domain.tld          59.28                58.81
node-464.domain.tld          19.42                78.07
node-468.domain.tld           9.85               564.93
node-470.domain.tld          10.38                65.98
node-474.domain.tld          75.21               375.68
node-483.domain.tld          66.07                20.97
node-484.domain.tld          80.99                11.71
node-49.domain.tld          119.71                13.88
node-491.domain.tld          10.93               222.79
node-493.domain.tld          16.81               688.89
node-495.domain.tld          25.27               143.72
node-499.domain.tld         138.10               231.17
node-50.domain.tld            5.61               125.30
node-500.domain.tld           1.74               101.37
node-501.domain.tld          18.37               478.90
node-504.domain.tld          65.09                18.69
node-505.domain.tld          10.82                54.11
node-506.domain.tld          16.91               222.50
node-509.domain.tld           4.10                88.93
node-515.domain.tld           5.27               308.76
node-516.domain.tld          19.48               118.27
node-519.domain.tld          13.91               162.03
node-56.domain.tld           69.26                21.96
node-58.domain.tld           66.64                15.69
node-65.domain.tld           66.29               160.15
node-68.domain.tld            6.68               429.74
node-73.domain.tld           32.36                50.55
node-74.domain.tld           19.24               303.47
node-84.domain.tld            9.09               237.63
===================  =============  ===================

Concurrency 185
---------------

**Errors**:

.. code-block:: yaml

    agent: shaker_ukdaep_master_180
    command:
      data: zcat `flent -H 10.3.62.190 -l 60 -s 1 tcp_upload 2>&1 | grep "se with" | grep
        -Po '\./\S+'`
      type: script
    concurrency: 185
    executor: flent
    id: ff8aa237-ee77-455d-b006-89f62fd3df78
    node: node-523.domain.tld
    scenario: OpenStack L3 North-South
    schedule: 1472471864.232474
    stats: {}
    status: lost
    test: Upload
    type: agent

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-1.domain.tld           266.67                75.78
node-103.domain.tld          14.74                68.02
node-117.domain.tld          35.06                81.60
node-121.domain.tld         127.47                35.07
node-123.domain.tld          49.45               153.52
node-127.domain.tld          19.06                84.53
node-129.domain.tld         210.15                 6.97
node-130.domain.tld          77.84               122.62
node-133.domain.tld          54.83                 7.69
node-136.domain.tld          62.06                50.98
node-137.domain.tld          46.65                26.57
node-138.domain.tld         119.76               127.71
node-142.domain.tld          52.47                57.26
node-146.domain.tld          38.67                 5.12
node-149.domain.tld           2.68               192.03
node-150.domain.tld         206.19                32.77
node-153.domain.tld         102.77               173.95
node-158.domain.tld          24.87                17.70
node-162.domain.tld         222.30               154.28
node-173.domain.tld         312.48                12.92
node-175.domain.tld          36.22                75.82
node-177.domain.tld         110.11                81.89
node-180.domain.tld          40.98                24.11
node-182.domain.tld         121.64                33.26
node-185.domain.tld          57.63                17.35
node-188.domain.tld          45.78                67.32
node-192.domain.tld          14.37               332.22
node-195.domain.tld         209.09               323.34
node-199.domain.tld           9.04                64.06
node-201.domain.tld          18.38                76.90
node-202.domain.tld         233.36                27.44
node-209.domain.tld           3.01                28.57
node-211.domain.tld          42.31                 8.46
node-213.domain.tld           2.97                96.65
node-214.domain.tld           3.94                54.29
node-224.domain.tld         107.24                45.28
node-226.domain.tld          30.79                31.22
node-228.domain.tld         132.43               190.20
node-233.domain.tld          71.26                79.79
node-236.domain.tld          23.45                76.82
node-237.domain.tld          48.00               322.61
node-24.domain.tld          142.15                 8.08
node-241.domain.tld           2.62               138.83
node-248.domain.tld         330.88                81.35
node-254.domain.tld           2.03                86.63
node-264.domain.tld         136.52                78.82
node-267.domain.tld          97.96                43.00
node-268.domain.tld          46.56                13.69
node-271.domain.tld           5.12               406.64
node-272.domain.tld         132.88                39.96
node-275.domain.tld          37.31               295.81
node-277.domain.tld          37.18                24.50
node-28.domain.tld           33.50                15.34
node-280.domain.tld           1.94                20.77
node-284.domain.tld          38.36               835.30
node-286.domain.tld         200.73                67.06
node-288.domain.tld          85.20               206.82
node-289.domain.tld         107.16                46.20
node-291.domain.tld         241.07                29.53
node-292.domain.tld          16.41               136.47
node-297.domain.tld         181.65                21.39
node-298.domain.tld          16.37                54.22
node-303.domain.tld           3.94                37.71
node-304.domain.tld          34.64                29.44
node-309.domain.tld           3.98                38.36
node-310.domain.tld          55.22                20.73
node-312.domain.tld          42.16                48.92
node-313.domain.tld           5.68                29.31
node-315.domain.tld          44.70                43.84
node-317.domain.tld          33.22               171.08
node-319.domain.tld         102.83                20.72
node-320.domain.tld         179.84                81.55
node-326.domain.tld           3.14               272.73
node-327.domain.tld          87.79                13.32
node-334.domain.tld          36.53                14.22
node-335.domain.tld          29.08               170.72
node-336.domain.tld           3.55                45.51
node-339.domain.tld         107.53               103.67
node-341.domain.tld          96.08                89.75
node-344.domain.tld          81.46                28.62
node-345.domain.tld          41.58               119.61
node-348.domain.tld          50.39                 2.25
node-351.domain.tld          94.98                33.09
node-353.domain.tld          24.87                12.91
node-355.domain.tld          66.93                30.81
node-357.domain.tld          70.16               139.48
node-36.domain.tld           28.87                84.41
node-366.domain.tld         107.89                19.75
node-367.domain.tld         127.32                16.42
node-370.domain.tld          54.70               174.65
node-375.domain.tld           3.74                53.26
node-379.domain.tld         129.71                19.71
node-38.domain.tld           43.07                78.73
node-381.domain.tld          26.29                53.79
node-383.domain.tld          66.88                47.53
node-384.domain.tld          13.88               196.60
node-387.domain.tld         107.22                 8.64
node-388.domain.tld         104.57                18.09
node-389.domain.tld         119.48                29.77
node-39.domain.tld          115.89                33.08
node-393.domain.tld         121.17                78.53
node-400.domain.tld         227.95                23.13
node-401.domain.tld         126.62               217.04
node-403.domain.tld           2.29                23.92
node-404.domain.tld          70.64                15.37
node-409.domain.tld          58.73               280.79
node-41.domain.tld          160.86                20.15
node-410.domain.tld          49.16               108.03
node-411.domain.tld         137.91                41.97
node-412.domain.tld         118.99              1250.50
node-413.domain.tld          42.66               193.23
node-415.domain.tld          76.88                 5.29
node-416.domain.tld           4.46                31.77
node-42.domain.tld           28.49                10.69
node-421.domain.tld          97.32                13.88
node-422.domain.tld          14.39                70.33
node-423.domain.tld          45.59                36.87
node-426.domain.tld          78.94                77.24
node-427.domain.tld         166.87                38.38
node-428.domain.tld          57.14                44.07
node-430.domain.tld         171.82                50.87
node-435.domain.tld           9.21                 3.49
node-436.domain.tld          20.77                29.66
node-438.domain.tld          56.50               318.86
node-446.domain.tld          80.38               269.54
node-447.domain.tld          49.91                38.65
node-448.domain.tld          97.24                 7.23
node-45.domain.tld           31.22                27.37
node-452.domain.tld           7.55               108.13
node-453.domain.tld          36.15                 5.53
node-454.domain.tld          71.14               130.01
node-458.domain.tld          54.72                49.87
node-46.domain.tld           77.47                32.40
node-461.domain.tld          37.75                36.26
node-463.domain.tld           9.54                43.90
node-464.domain.tld          17.75                57.66
node-466.domain.tld          49.49                77.33
node-468.domain.tld          18.23                 6.49
node-470.domain.tld         219.32                81.64
node-472.domain.tld          13.06                48.85
node-474.domain.tld          23.49               108.80
node-476.domain.tld          16.74                33.60
node-479.domain.tld           2.35               186.85
node-482.domain.tld          19.43               157.12
node-483.domain.tld          47.74                30.40
node-484.domain.tld         214.53                25.96
node-485.domain.tld           6.47               130.46
node-486.domain.tld         115.38                45.30
node-489.domain.tld          57.06                84.31
node-49.domain.tld          229.01                 3.18
node-491.domain.tld           6.68                 8.86
node-493.domain.tld           4.13                50.20
node-495.domain.tld          23.24                42.81
node-496.domain.tld          56.05               227.88
node-499.domain.tld          50.02                73.16
node-50.domain.tld           49.10                34.60
node-500.domain.tld         105.67                69.43
node-501.domain.tld         105.27                80.72
node-504.domain.tld          56.45               213.83
node-505.domain.tld          31.64                52.75
node-506.domain.tld         147.13                25.03
node-509.domain.tld           2.69                12.00
node-510.domain.tld         202.99                70.21
node-511.domain.tld          28.98               105.03
node-512.domain.tld          25.46                62.35
node-514.domain.tld         166.21                20.18
node-515.domain.tld          17.10                17.11
node-516.domain.tld          91.34                 7.87
node-519.domain.tld          38.38                 7.25
node-522.domain.tld           5.53                85.77
node-56.domain.tld           52.48                    0
node-57.domain.tld           42.88                61.64
node-58.domain.tld          133.74                20.97
node-61.domain.tld           14.79               201.78
node-62.domain.tld           47.68                12.52
node-65.domain.tld           52.47                 5.59
node-68.domain.tld           25.97               103.41
node-73.domain.tld          223.85                29.63
node-74.domain.tld           77.86                27.39
node-83.domain.tld           90.07                85.72
node-84.domain.tld           55.58                60.24
node-96.domain.tld          165.56                51.23
node-98.domain.tld           27.80                38.47
node-99.domain.tld           60.87                65.51
===================  =============  ===================

