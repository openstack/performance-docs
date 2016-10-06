.. _openstack_l3_east_west:

OpenStack L3 East-West Full
***************************

In this scenario Shaker launches pairs of instances, each instance on its own
compute node. All available compute nodes are utilized. Instances are connected
to one of 2 tenant networks, which plugged into single router. The traffic goes
from one network to the other (L3 east-west).

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - single_room
      template: l3_east_west.hot
    description: In this scenario Shaker launches pairs of instances, each instance on
      its own compute node. All available compute nodes are utilized. Instances are connected
      to one of 2 tenant networks, which plugged into single router. The traffic goes
      from one network to the other (L3 east-west).
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
    file_name: /opt/stack/.venv/local/lib/python2.7/site-packages/shaker/scenarios/openstack/full_l3_east_west.yaml
    title: OpenStack L3 East-West

Bi-directional
==============

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_bidirectional
    title: Bi-directional

.. image:: 95db663d-ac33-47b9-9ecb-3a73174b13e1.*

**Stats**:

===========  =============  =====================  ===================
concurrency  ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===========  =============  =====================  ===================
          1           2.54                3829.73              3404.94
          3           2.80                3448.17              4575.20
          6           2.70                3782.78              3820.52
         12           2.63                3865.64              3797.17
         24           2.90                3772.18              3875.87
         48           2.87                3767.87              3853.64
         97           2.76                3776.28              3840.64
===========  =============  =====================  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-188.domain.tld           2.54                3829.73              3404.94
===================  =============  =====================  ===================

Concurrency 3
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-158.domain.tld           2.60                3792.91              5040.45
node-188.domain.tld           3.13                3362.84              4339.88
node-46.domain.tld            2.67                3188.77              4345.26
===================  =============  =====================  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-116.domain.tld           2.56                4376.42              2804.18
node-15.domain.tld            2.70                4189.10              3289.12
node-158.domain.tld           2.92                3484.79              3921.57
node-188.domain.tld           3.11                3529.00              4008.41
node-19.domain.tld            2.16                3370.55              4055.43
node-46.domain.tld            2.77                3746.83              4844.43
===================  =============  =====================  ===================

Concurrency 12
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-114.domain.tld           2.83                3598.53              4060.69
node-116.domain.tld           2.38                3297.54              3905.83
node-14.domain.tld            2.58                3869.14              3299.51
node-15.domain.tld            2.90                3175.87              4405.47
node-151.domain.tld           2.87                4212.88              4259.33
node-152.domain.tld           2.85                4503.96              3608.36
node-154.domain.tld           2.48                4324.82              2602.78
node-156.domain.tld           2.75                4518.94              3099.85
node-158.domain.tld           2.90                3564.72              4059.06
node-188.domain.tld           2.79                3250.77              4520.09
node-19.domain.tld            3.09                4201.74              4379.94
node-46.domain.tld            1.09                3868.77              3365.09
===================  =============  =====================  ===================

Concurrency 24
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-114.domain.tld           2.76                4728.68              3158.08
node-116.domain.tld           3.03                3133.45              4354.81
node-119.domain.tld           2.85                3232.89              4500.83
node-14.domain.tld            2.68                3444.33              3963.85
node-140.domain.tld           2.54                3309.74              4061.95
node-144.domain.tld           2.84                4570.68              3746.23
node-145.domain.tld           3.15                4141.58              3035.42
node-146.domain.tld           2.65                3599.27              3957.74
node-148.domain.tld           2.90                2904.43              4671.91
node-15.domain.tld            2.95                3417.05              4391.14
node-151.domain.tld           3.14                3810.02              3812.99
node-152.domain.tld           3.33                3840.51              3583.04
node-154.domain.tld           2.40                3039.43              4023.27
node-156.domain.tld           3.06                4319.49              3129.57
node-158.domain.tld           2.84                4450.73              3348.22
node-188.domain.tld           3.15                3794.73              3896.68
node-19.domain.tld            2.98                3648.63              4032.43
node-190.domain.tld           2.81                3878.38              4205.35
node-192.domain.tld           3.17                3510.62              4043.95
node-42.domain.tld            2.62                3956.85              3827.18
node-43.domain.tld            2.90                3950.13              3970.39
node-46.domain.tld            2.83                3479.40              4474.76
node-5.domain.tld             3.02                4303.17              3186.33
node-87.domain.tld            2.92                4068.09              3644.77
===================  =============  =====================  ===================

Concurrency 48
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            2.20                3955.60              3385.58
node-114.domain.tld           2.78                3107.71              4390.13
node-116.domain.tld           2.68                4303.31              3505.80
node-119.domain.tld           3.01                4030.81              3597.93
node-131.domain.tld           3.00                4334.21              3049.39
node-133.domain.tld           3.04                2921.87              4452.05
node-135.domain.tld           3.05                3232.16              4472.28
node-139.domain.tld           3.15                3932.52              3550.26
node-14.domain.tld            2.25                3897.60              3827.66
node-140.domain.tld           2.87                4483.15              3178.79
node-144.domain.tld           3.16                3743.60              3802.05
node-145.domain.tld           3.08                3999.84              3895.32
node-146.domain.tld           2.71                4635.96              3197.34
node-148.domain.tld           3.34                2909.59              4445.99
node-15.domain.tld            3.02                4279.65              2987.62
node-151.domain.tld           2.50                3861.82              4081.58
node-152.domain.tld           2.88                3268.23              4351.51
node-154.domain.tld           2.92                2667.52              4493.55
node-156.domain.tld           3.14                3868.94              3817.54
node-158.domain.tld           1.97                2617.82              5011.16
node-168.domain.tld           2.84                4116.49              3771.96
node-185.domain.tld           2.57                3154.17              4846.73
node-188.domain.tld           3.13                3840.35              3761.67
node-19.domain.tld            3.15                3614.28              3910.89
node-190.domain.tld           2.41                4575.54              2882.15
node-192.domain.tld           2.31                3637.49              4064.02
node-196.domain.tld           2.99                2875.55              4648.21
node-2.domain.tld             2.91                4106.70              3870.42
node-23.domain.tld            3.17                3427.12              4227.15
node-28.domain.tld            2.91                3572.91              4269.11
node-42.domain.tld            3.00                4199.91              3012.25
node-43.domain.tld            2.95                3071.89              4367.16
node-46.domain.tld            2.86                4234.01              2970.43
node-47.domain.tld            3.02                3917.40              3879.64
node-5.domain.tld             3.07                3977.50              3411.82
node-57.domain.tld            3.50                3750.11              3162.88
node-58.domain.tld            2.68                4289.54              2917.29
node-6.domain.tld             2.79                4460.94              3535.01
node-71.domain.tld            3.04                3023.71              4517.11
node-73.domain.tld            2.77                4557.92              2979.38
node-76.domain.tld            3.14                3889.73              3780.79
node-77.domain.tld            2.81                3959.70              3331.71
node-79.domain.tld            3.08                3378.90              4131.34
node-87.domain.tld            3.14                4015.18              3591.28
node-89.domain.tld            2.17                2763.23              5948.63
node-91.domain.tld            3.03                3619.53              4540.80
node-96.domain.tld            2.82                4061.33              3277.16
node-99.domain.tld            2.62                4714.79              3874.02
===================  =============  =====================  ===================

Concurrency 97
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            3.56                3644.49              3625.08
node-101.domain.tld           1.93                5157.02              2564.25
node-102.domain.tld           2.20                4341.98              3226.50
node-104.domain.tld           3.00                4000.67              3206.50
node-107.domain.tld           2.91                4105.35              3916.00
node-108.domain.tld           3.11                4016.73              3864.51
node-110.domain.tld           2.07                3274.26              4906.62
node-114.domain.tld           2.82                3495.25              4424.98
node-116.domain.tld           2.11                2539.35              5953.22
node-118.domain.tld           2.62                3024.31              5031.01
node-119.domain.tld           3.26                3710.79              3738.67
node-120.domain.tld           2.21                3469.30              3854.07
node-123.domain.tld           3.01                3552.61              4264.33
node-125.domain.tld           3.04                4121.63              3971.52
node-127.domain.tld           3.09                3864.56              3743.97
node-129.domain.tld           2.78                4627.48              2823.81
node-13.domain.tld            3.28                3690.64              3649.56
node-131.domain.tld           3.06                3786.91              3809.25
node-133.domain.tld           2.63                4647.81              3189.70
node-135.domain.tld           3.14                2929.68              4214.94
node-137.domain.tld           2.27                4361.18              2995.60
node-139.domain.tld           3.17                3563.44              4132.09
node-14.domain.tld            3.41                3700.50              3590.20
node-140.domain.tld           2.14                5104.75              2709.92
node-141.domain.tld           3.08                3106.87              4292.16
node-144.domain.tld           2.81                4565.26              3262.16
node-145.domain.tld           2.99                4229.95              3930.42
node-146.domain.tld           3.09                3970.37              3655.63
node-148.domain.tld           2.49                3245.50              4198.52
node-15.domain.tld            2.75                3260.94              4560.70
node-151.domain.tld           2.13                4268.46              3145.34
node-152.domain.tld           2.79                3212.65              4622.42
node-154.domain.tld           2.90                3022.89              4442.57
node-156.domain.tld           3.27                3778.82              3769.81
node-158.domain.tld           2.72                4695.06              2692.23
node-161.domain.tld           3.84                3389.12              3209.04
node-162.domain.tld           2.92                2857.63              4452.69
node-163.domain.tld           2.30                3906.58              3434.61
node-166.domain.tld           2.77                4680.49              3273.71
node-168.domain.tld           2.80                3102.57              3543.31
node-170.domain.tld           2.14                4571.19              3166.99
node-173.domain.tld           2.43                3811.71              3753.30
node-175.domain.tld           1.64                2470.99              5524.28
node-178.domain.tld           2.39                3180.68              4527.98
node-182.domain.tld           2.87                4197.66              3110.27
node-183.domain.tld           1.74                5494.35              2539.13
node-185.domain.tld           2.45                3213.59              4491.23
node-186.domain.tld           1.87                3249.78              4197.29
node-188.domain.tld           3.10                3736.47              3787.75
node-19.domain.tld            2.81                3057.62              4505.88
node-190.domain.tld           3.09                3968.48              4076.37
node-192.domain.tld           2.95                2897.20              4804.81
node-194.domain.tld           2.98                3095.59              4457.10
node-196.domain.tld           3.06                3911.90              3919.74
node-199.domain.tld           2.92                3448.30              4670.83
node-2.domain.tld             2.65                3040.51              4787.20
node-21.domain.tld            3.27                3604.55              3801.87
node-23.domain.tld            3.32                3069.86              3787.92
node-26.domain.tld            3.34                2728.44              3918.46
node-27.domain.tld            1.82                5472.32              3445.85
node-28.domain.tld            3.18                3719.60              3799.42
node-31.domain.tld            2.78                4259.09              3978.02
node-33.domain.tld            3.15                3015.00              4319.10
node-35.domain.tld            2.58                4682.02              2597.64
node-37.domain.tld            3.07                2784.93              4226.12
node-38.domain.tld            2.78                4573.13              3154.77
node-42.domain.tld            3.17                3812.01              3561.86
node-43.domain.tld            2.89                4288.43              3341.44
node-46.domain.tld            2.73                4637.53              3068.83
node-47.domain.tld            3.35                3666.87              3528.49
node-5.domain.tld             2.80                4189.53              3863.84
node-50.domain.tld            1.42                3201.89              3852.00
node-52.domain.tld            2.05                 603.53              5584.20
node-56.domain.tld            2.85                4491.00              3363.86
node-57.domain.tld            2.21                5685.37              2937.98
node-58.domain.tld            2.96                3991.23              3570.12
node-6.domain.tld             2.95                4124.41              3987.80
node-60.domain.tld            3.26                3762.43              3773.11
node-63.domain.tld            2.49                3578.32              4035.75
node-64.domain.tld            2.21                3503.43              3933.21
node-66.domain.tld            2.61                3813.58              4528.92
node-69.domain.tld            2.77                4183.02              4188.57
node-71.domain.tld            2.96                4315.07              2891.64
node-73.domain.tld            3.07                3109.35              4335.67
node-76.domain.tld            3.30                3237.36              4083.93
node-77.domain.tld            2.58                4337.09              3247.45
node-79.domain.tld            2.29                3713.95              3853.34
node-80.domain.tld            2.93                3402.98              4537.19
node-82.domain.tld            2.73                3189.92              4638.36
node-83.domain.tld            3.18                3967.49              4021.89
node-85.domain.tld            2.52                3752.49              3762.45
node-87.domain.tld            2.08                4904.01              3250.67
node-89.domain.tld            3.12                3021.01              3970.13
node-91.domain.tld            2.05                6240.29              1733.52
node-93.domain.tld            3.07                2881.45              4384.39
node-96.domain.tld            3.28                3694.66              3644.13
node-99.domain.tld            3.19                3720.86              3826.71
===================  =============  =====================  ===================

Download
========

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_download
    title: Download

.. image:: abfc32d9-d8d3-4be8-a2f5-c8a49338fe4e.*

**Stats**:

===========  =============  =====================
concurrency  ping_icmp, ms  tcp_download, Mbits/s
===========  =============  =====================
          1           2.27                5902.55
          3           1.95                6801.81
          6           2.07                6574.14
         12           2.12                6453.51
         24           2.05                6391.87
         48           2.03                6587.61
         97           2.01                6479.25
===========  =============  =====================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-188.domain.tld           2.27                5902.55
===================  =============  =====================

Concurrency 3
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-158.domain.tld           2.05                6247.44
node-188.domain.tld           1.95                7044.62
node-46.domain.tld            1.87                7113.38
===================  =============  =====================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-116.domain.tld           2.39                5593.59
node-15.domain.tld            2.24                6210.29
node-158.domain.tld           1.80                7473.06
node-188.domain.tld           1.83                7272.86
node-19.domain.tld            2.43                5456.29
node-46.domain.tld            1.75                7438.74
===================  =============  =====================

Concurrency 12
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-114.domain.tld           2.00                6864.24
node-116.domain.tld           2.26                5973.92
node-14.domain.tld            2.19                6309.52
node-15.domain.tld            1.89                6933.29
node-151.domain.tld           1.84                7561.24
node-152.domain.tld           2.32                5978.38
node-154.domain.tld           2.27                6050.74
node-156.domain.tld           2.26                5902.87
node-158.domain.tld           1.77                7403.94
node-188.domain.tld           2.32                5934.60
node-19.domain.tld            2.31                5784.72
node-46.domain.tld            2.00                6744.66
===================  =============  =====================

Concurrency 24
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-114.domain.tld           2.08                6492.21
node-116.domain.tld           2.26                5918.35
node-119.domain.tld           1.88                7101.19
node-14.domain.tld            2.20                6146.34
node-140.domain.tld           1.09                5261.00
node-144.domain.tld           1.94                6934.47
node-145.domain.tld           2.29                5720.99
node-146.domain.tld           2.07                6389.76
node-148.domain.tld           1.78                7463.79
node-15.domain.tld            2.10                6137.54
node-151.domain.tld           2.15                6234.62
node-152.domain.tld           2.32                5792.87
node-154.domain.tld           2.22                6246.42
node-156.domain.tld           2.16                6317.80
node-158.domain.tld           1.76                7382.17
node-188.domain.tld           2.42                5517.11
node-19.domain.tld            2.22                5931.53
node-190.domain.tld           1.90                6950.73
node-192.domain.tld           1.80                7219.77
node-42.domain.tld            2.10                6527.91
node-43.domain.tld            2.18                6185.22
node-46.domain.tld            2.06                6488.41
node-5.domain.tld             2.22                6046.32
node-87.domain.tld            1.88                6998.32
===================  =============  =====================

Concurrency 48
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            1.96                5527.49
node-114.domain.tld           2.21                6054.69
node-116.domain.tld           2.18                6025.94
node-119.domain.tld           1.86                6955.53
node-131.domain.tld           1.80                7474.50
node-133.domain.tld           2.19                6247.52
node-135.domain.tld           1.92                6895.67
node-139.domain.tld           2.28                5829.31
node-14.domain.tld            1.87                7312.13
node-140.domain.tld           2.00                6735.65
node-144.domain.tld           2.14                6425.96
node-145.domain.tld           1.78                7572.63
node-146.domain.tld           2.23                6125.20
node-148.domain.tld           1.87                7210.65
node-15.domain.tld            2.15                6513.33
node-151.domain.tld           2.18                5968.76
node-152.domain.tld           2.39                5738.16
node-154.domain.tld           2.30                5902.93
node-156.domain.tld           1.95                6248.62
node-158.domain.tld           2.35                5782.87
node-168.domain.tld           1.56                6757.41
node-185.domain.tld           1.86                7197.16
node-188.domain.tld           2.38                5738.12
node-19.domain.tld            2.24                6103.58
node-190.domain.tld           1.84                7249.50
node-192.domain.tld           2.20                6067.51
node-196.domain.tld           2.02                6910.94
node-2.domain.tld             2.09                6786.16
node-23.domain.tld            1.88                7313.82
node-28.domain.tld            2.21                6200.44
node-42.domain.tld            1.94                6807.50
node-43.domain.tld            1.82                7345.06
node-46.domain.tld            2.05                6463.71
node-47.domain.tld            1.95                6957.97
node-5.domain.tld             1.82                7349.38
node-57.domain.tld            1.84                7214.61
node-58.domain.tld            2.12                6334.81
node-6.domain.tld             2.06                6767.26
node-71.domain.tld            1.85                5638.37
node-73.domain.tld            1.89                7098.23
node-76.domain.tld            1.95                6930.11
node-77.domain.tld            1.88                7201.53
node-79.domain.tld            2.22                6004.54
node-87.domain.tld            1.92                6885.06
node-89.domain.tld            2.33                5833.80
node-91.domain.tld            1.96                6714.76
node-96.domain.tld            2.24                6042.57
node-99.domain.tld            1.69                7743.71
===================  =============  =====================

Concurrency 97
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            1.86                7200.43
node-101.domain.tld           2.05                6720.63
node-102.domain.tld           1.87                7324.68
node-104.domain.tld           2.42                5471.49
node-107.domain.tld           2.22                6137.11
node-108.domain.tld           2.41                5672.17
node-110.domain.tld           1.95                6755.94
node-114.domain.tld           2.23                6022.19
node-116.domain.tld           2.22                6023.31
node-118.domain.tld           1.99                7015.25
node-119.domain.tld           2.18                6223.06
node-120.domain.tld           2.27                5724.72
node-123.domain.tld           2.00                6886.38
node-125.domain.tld           1.66                6413.79
node-127.domain.tld           1.92                6994.11
node-129.domain.tld           2.35                5760.15
node-13.domain.tld            2.32                5653.53
node-131.domain.tld           2.27                6027.74
node-133.domain.tld           2.30                5937.12
node-135.domain.tld           1.74                7601.24
node-137.domain.tld           1.93                6964.69
node-139.domain.tld           2.06                6460.11
node-14.domain.tld            2.27                5822.25
node-140.domain.tld           0.42                6142.95
node-141.domain.tld           1.99                6801.74
node-144.domain.tld           2.18                6192.67
node-145.domain.tld           2.19                6177.41
node-146.domain.tld           2.17                6079.10
node-148.domain.tld           1.88                7438.60
node-15.domain.tld            1.93                7075.15
node-151.domain.tld           2.26                5909.79
node-152.domain.tld           1.90                7295.63
node-154.domain.tld           1.86                7328.16
node-156.domain.tld           1.91                6948.84
node-158.domain.tld           2.22                5969.20
node-161.domain.tld           1.98                6711.85
node-162.domain.tld           2.01                6664.69
node-163.domain.tld           1.84                6971.20
node-166.domain.tld           1.79                7503.57
node-168.domain.tld           2.14                6191.77
node-170.domain.tld           1.97                5525.65
node-173.domain.tld           2.09                6503.91
node-175.domain.tld           1.80                7360.15
node-178.domain.tld           1.92                6774.50
node-182.domain.tld           1.80                7368.10
node-183.domain.tld           2.12                6449.54
node-185.domain.tld           2.06                6526.84
node-186.domain.tld           2.16                6344.44
node-188.domain.tld           1.56                6751.05
node-19.domain.tld            2.21                6057.97
node-190.domain.tld           1.82                7230.44
node-192.domain.tld           2.27                5912.98
node-194.domain.tld           2.06                6639.94
node-196.domain.tld           2.21                5938.73
node-199.domain.tld           2.34                5628.39
node-2.domain.tld             2.28                5943.00
node-21.domain.tld            2.01                6606.07
node-23.domain.tld            2.23                5929.13
node-26.domain.tld            1.86                6965.93
node-27.domain.tld            1.96                6799.68
node-28.domain.tld            1.82                7136.58
node-31.domain.tld            1.88                7093.38
node-33.domain.tld            2.09                6611.83
node-35.domain.tld            1.90                6922.87
node-37.domain.tld            2.06                6650.42
node-38.domain.tld            1.78                7350.52
node-42.domain.tld            1.88                7117.24
node-43.domain.tld            2.29                5960.63
node-46.domain.tld            2.17                6397.26
node-47.domain.tld            1.68                7530.22
node-5.domain.tld             2.02                6062.07
node-50.domain.tld            1.95                6844.94
node-52.domain.tld            0.36                3416.53
node-56.domain.tld            2.20                5997.07
node-57.domain.tld            2.38                5676.79
node-58.domain.tld            1.89                6680.84
node-6.domain.tld             1.85                7309.77
node-60.domain.tld            2.28                5856.11
node-63.domain.tld            2.34                5872.58
node-64.domain.tld            2.18                6182.03
node-66.domain.tld            1.90                6795.11
node-69.domain.tld            2.26                6020.50
node-71.domain.tld            2.13                6409.57
node-73.domain.tld            1.98                6681.53
node-76.domain.tld            1.67                7772.81
node-77.domain.tld            2.31                5760.71
node-79.domain.tld            1.86                7116.69
node-80.domain.tld            2.19                6135.54
node-82.domain.tld            2.41                5694.44
node-83.domain.tld            1.67                6514.05
node-85.domain.tld            2.34                5593.16
node-87.domain.tld            2.17                6101.81
node-89.domain.tld            1.92                6084.46
node-91.domain.tld            1.92                6935.84
node-93.domain.tld            1.89                7045.85
node-96.domain.tld            2.02                6477.02
node-99.domain.tld            1.83                7207.48
===================  =============  =====================

Upload
======

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_upload
    title: Upload

.. image:: 6601eee3-e47f-44fe-9b61-336e3d94272b.*

**Stats**:

===========  =============  ===================
concurrency  ping_icmp, ms  tcp_upload, Mbits/s
===========  =============  ===================
          1           2.50              5743.06
          3           2.23              6714.78
          6           2.37              6301.22
         12           2.26              6574.76
         24           2.23              6594.05
         48           2.26              6516.15
         97           2.24              6552.61
===========  =============  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-188.domain.tld           2.50              5743.06
===================  =============  ===================

Concurrency 3
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-158.domain.tld           2.26              6525.46
node-188.domain.tld           1.86              7909.73
node-46.domain.tld            2.58              5709.15
===================  =============  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-116.domain.tld           2.31              6166.56
node-15.domain.tld            2.60              5639.22
node-158.domain.tld           2.34              6307.41
node-188.domain.tld           2.62              5780.88
node-19.domain.tld            2.45              6124.09
node-46.domain.tld            1.92              7789.20
===================  =============  ===================

Concurrency 12
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-114.domain.tld           2.03              7246.20
node-116.domain.tld           2.01              7255.39
node-14.domain.tld            2.48              5888.11
node-15.domain.tld            2.45              6171.54
node-151.domain.tld           2.37              6275.57
node-152.domain.tld           2.09              7122.02
node-154.domain.tld           2.44              5993.20
node-156.domain.tld           1.95              7351.63
node-158.domain.tld           2.12              7098.95
node-188.domain.tld           2.60              5654.91
node-19.domain.tld            2.13              6967.21
node-46.domain.tld            2.50              5872.43
===================  =============  ===================

Concurrency 24
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-114.domain.tld           2.30              6450.69
node-116.domain.tld           2.02              7366.88
node-119.domain.tld           2.58              5930.50
node-14.domain.tld            1.96              7298.93
node-140.domain.tld           2.43              6075.75
node-144.domain.tld           2.00              7332.07
node-145.domain.tld           2.54              5788.22
node-146.domain.tld           2.47              6010.65
node-148.domain.tld           1.89              7575.88
node-15.domain.tld            2.50              5821.75
node-151.domain.tld           2.56              5829.82
node-152.domain.tld           2.02              7168.01
node-154.domain.tld           2.02              7380.84
node-156.domain.tld           2.57              5755.93
node-158.domain.tld           2.34              6449.16
node-188.domain.tld           2.51              5849.72
node-19.domain.tld            2.50              5969.71
node-190.domain.tld           1.66              6651.22
node-192.domain.tld           2.08              7020.42
node-42.domain.tld            1.99              7346.77
node-43.domain.tld            2.10              7183.56
node-46.domain.tld            1.95              7485.22
node-5.domain.tld             2.47              5920.22
node-87.domain.tld            2.03              6595.18
===================  =============  ===================

Concurrency 48
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            2.60              5786.34
node-114.domain.tld           1.73              7059.47
node-116.domain.tld           2.59              5744.92
node-119.domain.tld           1.94              7392.09
node-131.domain.tld           2.47              5800.00
node-133.domain.tld           1.94              7688.60
node-135.domain.tld           1.99              7351.60
node-139.domain.tld           2.52              5752.69
node-14.domain.tld            2.51              5805.85
node-140.domain.tld           2.08              7262.55
node-144.domain.tld           2.55              5797.13
node-145.domain.tld           1.95              7382.77
node-146.domain.tld           2.02              7405.41
node-148.domain.tld           1.83              7563.77
node-15.domain.tld            2.57              5761.98
node-151.domain.tld           2.41              6063.17
node-152.domain.tld           2.50              5945.75
node-154.domain.tld           2.44              5934.44
node-156.domain.tld           2.44              5889.50
node-158.domain.tld           2.37              6166.36
node-168.domain.tld           2.46              5925.35
node-185.domain.tld           2.01              7298.73
node-188.domain.tld           2.08              7072.22
node-19.domain.tld            2.49              5835.38
node-190.domain.tld           2.06              7119.05
node-192.domain.tld           2.18              7058.46
node-196.domain.tld           2.32              6134.65
node-2.domain.tld             2.49              6253.85
node-23.domain.tld            1.81              7702.19
node-28.domain.tld            2.48              6104.63
node-42.domain.tld            2.35              6148.89
node-43.domain.tld            2.10              7029.65
node-46.domain.tld            1.98              7297.95
node-47.domain.tld            2.56              5911.44
node-5.domain.tld             1.95              7556.69
node-57.domain.tld            2.61              5680.22
node-58.domain.tld            2.07              7068.15
node-6.domain.tld             2.45              5987.26
node-71.domain.tld            1.86              7334.29
node-73.domain.tld            2.44              6352.80
node-76.domain.tld            1.92              7311.81
node-77.domain.tld            2.62              5521.77
node-79.domain.tld            2.05              7239.52
node-87.domain.tld            2.62              5590.22
node-89.domain.tld            1.89              5865.64
node-91.domain.tld            2.45              5782.48
node-96.domain.tld            2.50              5779.70
node-99.domain.tld            2.08              7257.95
===================  =============  ===================

Concurrency 97
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            1.95              7432.90
node-101.domain.tld           2.65              5509.30
node-102.domain.tld           2.24              6835.88
node-104.domain.tld           1.96              7410.15
node-107.domain.tld           2.56              5878.37
node-108.domain.tld           2.44              6084.09
node-110.domain.tld           2.00              7286.68
node-114.domain.tld           2.52              5849.75
node-116.domain.tld           2.07              7055.14
node-118.domain.tld           2.19              7185.75
node-119.domain.tld           2.46              5755.86
node-120.domain.tld           2.55              5715.31
node-123.domain.tld           2.03              7460.46
node-125.domain.tld           2.04              7139.30
node-127.domain.tld           2.03              7437.30
node-129.domain.tld           2.44              6019.61
node-13.domain.tld            2.44              6048.37
node-131.domain.tld           2.44              6105.37
node-133.domain.tld           2.50              6051.52
node-135.domain.tld           2.10              6912.15
node-137.domain.tld           2.37              6063.28
node-139.domain.tld           2.56              5794.68
node-14.domain.tld            2.55              5712.05
node-140.domain.tld           1.23              5471.74
node-141.domain.tld           1.70              6756.99
node-144.domain.tld           2.75              5411.18
node-145.domain.tld           2.42              6002.78
node-146.domain.tld           1.85              7758.71
node-148.domain.tld           2.39              6032.32
node-15.domain.tld            2.02              6967.55
node-151.domain.tld           2.41              6135.82
node-152.domain.tld           2.29              6172.00
node-154.domain.tld           2.00              6979.94
node-156.domain.tld           2.51              6001.03
node-158.domain.tld           2.36              6093.43
node-161.domain.tld           2.43              6154.97
node-162.domain.tld           2.48              5854.59
node-163.domain.tld           2.61              5712.27
node-166.domain.tld           2.43              6046.18
node-168.domain.tld           1.87              7368.61
node-170.domain.tld           1.97              7400.34
node-173.domain.tld           2.55              5901.24
node-175.domain.tld           2.00              7352.43
node-178.domain.tld           2.15              6819.78
node-182.domain.tld           2.38              6247.72
node-183.domain.tld           2.64              5620.82
node-185.domain.tld           2.38              6637.41
node-186.domain.tld           2.01              7345.83
node-188.domain.tld           2.04              7384.29
node-19.domain.tld            2.08              7222.57
node-190.domain.tld           2.11              7039.02
node-192.domain.tld           1.67              6990.21
node-194.domain.tld           2.00              7493.55
node-196.domain.tld           2.47              6053.05
node-199.domain.tld           2.48              6072.87
node-2.domain.tld             2.06              7352.02
node-21.domain.tld            2.17              6340.85
node-23.domain.tld            2.41              5998.32
node-26.domain.tld            2.11              7215.91
node-27.domain.tld            2.07              7319.42
node-28.domain.tld            2.47              6022.73
node-31.domain.tld            2.47              5902.14
node-33.domain.tld            2.31              6515.58
node-35.domain.tld            2.32              6211.83
node-37.domain.tld            2.47              5812.14
node-38.domain.tld            2.30              6122.45
node-42.domain.tld            2.47              5931.77
node-43.domain.tld            2.59              5742.61
node-46.domain.tld            1.96              7694.87
node-47.domain.tld            2.05              7363.24
node-5.domain.tld             1.94              7406.43
node-50.domain.tld            2.12              7077.62
node-52.domain.tld            2.30              6534.05
node-56.domain.tld            2.02              6930.86
node-57.domain.tld            2.63              5600.35
node-58.domain.tld            2.50              5867.37
node-6.domain.tld             2.27              6571.48
node-60.domain.tld            2.59              5721.26
node-63.domain.tld            2.01              7477.51
node-64.domain.tld            2.09              7028.36
node-66.domain.tld            2.17              7076.57
node-69.domain.tld            1.97              7583.99
node-71.domain.tld            1.90              7622.31
node-73.domain.tld            2.52              5766.52
node-76.domain.tld            2.46              5879.88
node-77.domain.tld            1.90              7630.46
node-79.domain.tld            2.12              5506.09
node-80.domain.tld            2.39              6100.22
node-82.domain.tld            2.18              6876.84
node-83.domain.tld            2.01              7301.80
node-85.domain.tld            2.11              6969.93
node-87.domain.tld            2.08              6973.86
node-89.domain.tld            1.89              7586.34
node-91.domain.tld            2.40              6420.68
node-93.domain.tld            2.30              6536.81
node-96.domain.tld            2.54              5634.68
node-99.domain.tld            2.16              7130.14
===================  =============  ===================

