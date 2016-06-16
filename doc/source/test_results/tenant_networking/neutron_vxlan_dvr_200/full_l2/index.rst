.. _openstack_l2:

OpenStack L2
************

In this scenario Shaker launches pairs of instances in the same tenant network.
Every instance is hosted on a separate compute node, all available compute
nodes are utilized. The traffic goes within the tenant network (L2 domain).

**Scenario**:

.. code-block:: yaml

    deployment:
      accommodation:
      - pair
      - single_room
      template: l2.hot
    description: In this scenario Shaker launches pairs of instances in the same tenant
      network. Every instance is hosted on a separate compute node, all available compute
      nodes are utilized. The traffic goes within the tenant network (L2 domain).
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
    file_name: /opt/stack/.venv/local/lib/python2.7/site-packages/shaker/scenarios/openstack/full_l2.yaml
    title: OpenStack L2

Bi-directional
==============

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_bidirectional
    title: Bi-directional

.. image:: 31c0c798-db9b-458c-aca5-d0f797a88dc6.*

**Stats**:

===========  =============  =====================  ===================
concurrency  ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===========  =============  =====================  ===================
          1           1.71                5956.48              2510.61
          3           2.61                4207.65              3947.19
          6           2.44                4142.22              3985.50
         12           2.39                4026.37              4196.23
         24           2.70                4011.49              3960.51
         48           2.44                3990.44              4156.30
         97           2.51                4229.79              3901.63
===========  =============  =====================  ===================

Concurrency 1
-------------

**Stats**:

==================  =============  =====================  ===================
node                ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
==================  =============  =====================  ===================
node-63.domain.tld           1.71                5956.48              2510.61
==================  =============  =====================  ===================

Concurrency 3
-------------

**Stats**:

==================  =============  =====================  ===================
node                ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
==================  =============  =====================  ===================
node-33.domain.tld           3.01                4129.71              3906.27
node-60.domain.tld           2.25                4456.15              3575.02
node-63.domain.tld           2.57                4037.07              4360.28
==================  =============  =====================  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-104.domain.tld           2.71                4557.71              3473.93
node-107.domain.tld           2.77                4246.01              3877.41
node-33.domain.tld            2.58                3074.65              5118.81
node-38.domain.tld            2.61                4344.23              3573.11
node-60.domain.tld            1.64                3941.68              4186.79
node-63.domain.tld            2.32                4689.04              3682.96
===================  =============  =====================  ===================

Concurrency 12
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-104.domain.tld           2.83                4457.97              3375.79
node-107.domain.tld           2.73                3308.82              4368.01
node-162.domain.tld           1.80                5882.42              2162.74
node-170.domain.tld           2.47                3013.53              4940.60
node-182.domain.tld           1.91                4167.41              3949.83
node-31.domain.tld            2.83                4108.44              4443.08
node-33.domain.tld            2.30                3720.26              5269.15
node-35.domain.tld            2.24                3505.32              4349.43
node-37.domain.tld            2.39                5186.71              2841.02
node-38.domain.tld            2.31                3078.73              4703.12
node-60.domain.tld            2.71                3764.14              4852.61
node-63.domain.tld            2.21                4122.71              5099.33
===================  =============  =====================  ===================

Concurrency 24
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-104.domain.tld           2.57                4665.06              3145.02
node-107.domain.tld           2.64                3157.12              4621.53
node-118.domain.tld           2.64                3714.97              4564.44
node-162.domain.tld           2.68                3344.19              4560.74
node-170.domain.tld           2.94                4226.89              4370.01
node-173.domain.tld           2.83                4295.00              3993.93
node-175.domain.tld           3.06                3601.95              4129.89
node-182.domain.tld           2.79                3121.31              4373.49
node-183.domain.tld           2.44                4140.35              4141.80
node-186.domain.tld           3.45                3635.65              3806.11
node-31.domain.tld            2.10                5503.74              2518.21
node-33.domain.tld            2.56                3672.80              4477.08
node-35.domain.tld            2.44                4713.80              3153.50
node-37.domain.tld            2.51                4344.58              3238.81
node-38.domain.tld            2.66                4749.48              3375.03
node-6.domain.tld             2.78                3762.59              4306.82
node-60.domain.tld            2.86                4006.11              3932.36
node-63.domain.tld            2.60                4919.35              3401.14
node-64.domain.tld            3.05                3239.95              4193.72
node-66.domain.tld            2.78                3314.05              4712.86
node-69.domain.tld            2.92                4131.92              4050.42
node-80.domain.tld            2.32                2995.16              4871.95
node-83.domain.tld            2.64                4704.35              3281.34
node-85.domain.tld            2.58                4315.29              3832.04
===================  =============  =====================  ===================

Concurrency 48
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-101.domain.tld           2.87                4251.19              3269.25
node-102.domain.tld           2.36                4164.63              3578.38
node-104.domain.tld           2.01                5958.89              2214.36
node-107.domain.tld           2.32                4153.30              4036.82
node-108.domain.tld           1.58                3996.17              4197.52
node-110.domain.tld           2.56                4467.65              3150.08
node-114.domain.tld           2.72                4162.36              4228.18
node-118.domain.tld           3.03                3759.39              4514.61
node-120.domain.tld           2.66                3509.10              4415.32
node-123.domain.tld           2.56                3302.20              4664.05
node-125.domain.tld           1.99                4728.64              4002.22
node-129.domain.tld           2.74                4674.72              3112.51
node-13.domain.tld            2.83                4126.07              4118.59
node-141.domain.tld           2.87                3696.16              4539.40
node-161.domain.tld           2.88                3557.39              4396.53
node-162.domain.tld           2.49                4797.50              3644.98
node-163.domain.tld           2.79                3595.01              4610.81
node-170.domain.tld           2.40                4534.05              4159.80
node-173.domain.tld           2.96                3939.16              4157.27
node-175.domain.tld           2.64                3580.95              4878.67
node-178.domain.tld           2.61                3963.77              4329.12
node-182.domain.tld           2.57                4267.20              3094.15
node-183.domain.tld           2.84                3495.44              4439.85
node-186.domain.tld           2.44                3641.17              4830.28
node-188.domain.tld           2.64                4772.16              3260.39
node-190.domain.tld           2.07                4129.58              3599.28
node-192.domain.tld           2.61                4332.02              4305.94
node-194.domain.tld           0.88                2658.60              5559.53
node-196.domain.tld           1.74                4464.63              3089.16
node-199.domain.tld           2.97                3141.99              4397.00
node-31.domain.tld            3.04                2665.64              4518.71
node-33.domain.tld            2.15                5367.74              3631.90
node-35.domain.tld            1.18                4372.19              3535.23
node-37.domain.tld            2.54                3220.07              4779.35
node-38.domain.tld            2.69                4505.29              4087.21
node-50.domain.tld            1.94                4765.38              4016.25
node-52.domain.tld            2.45                3184.73              5208.71
node-56.domain.tld            2.80                3653.78              4068.01
node-6.domain.tld             2.27                2955.33              5447.90
node-60.domain.tld            2.77                4512.25              3367.93
node-63.domain.tld            1.92                2448.33              6235.23
node-64.domain.tld            2.58                3609.25              4616.87
node-66.domain.tld            2.45                4566.12              4023.97
node-69.domain.tld            2.75                3763.76              4338.62
node-80.domain.tld            2.38                4647.18              4271.45
node-83.domain.tld            2.55                4627.43              3597.77
node-85.domain.tld            3.11                4279.00              3335.27
node-89.domain.tld            0.86                2576.65              5627.99
===================  =============  =====================  ===================

Concurrency 97
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            3.01                3784.46              4247.86
node-101.domain.tld           2.78                3644.44              4288.63
node-102.domain.tld           2.60                4663.32              3186.52
node-104.domain.tld           2.87                4732.23              3279.10
node-107.domain.tld           2.69                4563.19              3338.62
node-108.domain.tld           2.87                3248.04              4518.31
node-110.domain.tld           2.65                3836.26              4319.76
node-114.domain.tld           2.74                4740.47              3385.65
node-116.domain.tld           2.17                4471.76              4474.21
node-118.domain.tld           2.66                3376.53              4483.72
node-119.domain.tld           3.27                4014.88              4044.65
node-120.domain.tld           2.66                4587.78              3772.42
node-123.domain.tld           2.75                4800.29              3517.41
node-125.domain.tld           2.68                4685.76              3387.58
node-127.domain.tld           1.47                5783.08              2571.41
node-129.domain.tld           1.88                6462.18              1919.31
node-13.domain.tld            2.92                4064.11              3978.20
node-131.domain.tld           2.09                2974.15              4875.43
node-133.domain.tld           2.17                5405.83              2660.09
node-135.domain.tld           2.18                4594.88              3769.85
node-137.domain.tld           2.96                3975.07              4059.75
node-139.domain.tld           2.16                3081.38              4994.68
node-14.domain.tld            0.98                3857.65              4188.45
node-140.domain.tld           2.46                3549.88              4595.90
node-141.domain.tld           2.82                4228.06              3496.65
node-144.domain.tld           2.40                4364.03              3421.70
node-145.domain.tld           3.04                3883.49              3879.71
node-146.domain.tld           2.88                4322.72              3366.99
node-148.domain.tld           2.60                3862.99              4805.93
node-15.domain.tld            2.43                4780.95              3126.02
node-151.domain.tld           2.82                3984.93              4046.55
node-152.domain.tld           2.73                3250.06              4082.12
node-154.domain.tld           2.55                4911.06              3561.73
node-156.domain.tld           1.93                5775.91              2912.39
node-158.domain.tld           2.05                3115.60              5308.19
node-161.domain.tld           2.74                3654.17              4361.04
node-162.domain.tld           2.45                3816.78              3824.62
node-163.domain.tld           1.55                5280.00              2775.14
node-166.domain.tld           2.06                4206.54              3784.19
node-168.domain.tld           2.78                3852.40              4341.74
node-170.domain.tld           2.81                4261.48              4118.79
node-173.domain.tld           2.71                2899.53              5078.68
node-175.domain.tld           1.62                3799.67              4577.46
node-178.domain.tld           2.77                4092.21              4114.11
node-182.domain.tld           2.13                5809.24              2448.70
node-183.domain.tld           2.95                3422.82              4444.16
node-185.domain.tld           2.53                5207.60              2526.80
node-186.domain.tld           1.34                4496.03              3685.32
node-188.domain.tld           3.04                3985.29              4073.53
node-19.domain.tld            2.83                4449.34              3950.49
node-190.domain.tld           1.73                4757.46              4046.45
node-192.domain.tld           1.71                5215.04              4532.26
node-194.domain.tld           2.76                3867.15              4232.34
node-196.domain.tld           2.74                3901.38              4278.86
node-199.domain.tld           2.55                4991.48              2990.22
node-2.domain.tld             2.98                3836.36              4238.39
node-21.domain.tld            2.63                4711.88              3251.09
node-23.domain.tld            2.95                3876.75              3938.47
node-26.domain.tld            2.40                4467.60              3508.01
node-27.domain.tld            2.28                4963.79              3019.53
node-28.domain.tld            2.05                5468.37              3457.90
node-31.domain.tld            2.49                3571.49              4303.93
node-33.domain.tld            3.22                3653.08              4047.38
node-35.domain.tld            2.77                4461.08              3406.55
node-37.domain.tld            1.84                6514.03              2322.76
node-38.domain.tld            2.54                4604.07              4237.13
node-42.domain.tld            2.60                4965.79              3306.29
node-43.domain.tld            2.65                3996.08              4062.43
node-46.domain.tld            2.54                4484.54              3770.04
node-47.domain.tld            2.68                3515.58              5128.08
node-5.domain.tld             2.94                4291.20              4111.62
node-50.domain.tld            2.27                2970.70              4972.64
node-52.domain.tld            2.73                3904.29              4542.66
node-56.domain.tld            3.20                3728.67              3906.43
node-57.domain.tld            2.90                4209.49              3294.72
node-58.domain.tld            2.49                3317.37              4382.47
node-6.domain.tld             2.17                4427.66              3824.59
node-60.domain.tld            2.68                3258.19              4769.35
node-63.domain.tld            2.77                3731.96              4207.31
node-64.domain.tld            2.65                3789.39              4472.09
node-66.domain.tld            2.48                4716.09              3673.87
node-69.domain.tld            1.93                3748.97              4300.06
node-71.domain.tld            2.20                3836.30              4062.56
node-73.domain.tld            2.69                4517.85              3405.64
node-76.domain.tld            2.63                3177.62              4889.41
node-77.domain.tld            2.55                4691.12              3879.04
node-79.domain.tld            2.00                4616.56              2925.16
node-80.domain.tld            3.10                3962.14              3838.13
node-82.domain.tld            2.96                4293.39              4168.84
node-83.domain.tld            1.70                4573.02              4222.81
node-85.domain.tld            3.06                3912.16              4020.00
node-87.domain.tld            2.41                3638.33              4224.89
node-89.domain.tld            2.69                3693.57              4577.78
node-91.domain.tld            2.79                4655.91              3239.34
node-93.domain.tld            2.51                3689.37              4487.85
node-96.domain.tld            2.52                4642.74              3587.69
node-99.domain.tld            1.72                3861.85              4422.90
===================  =============  =====================  ===================

Download
========

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_download
    title: Download

.. image:: d0b46684-75af-4d8b-a282-a5336c284c08.*

**Stats**:

===========  =============  =====================
concurrency  ping_icmp, ms  tcp_download, Mbits/s
===========  =============  =====================
          1           2.16                6158.73
          3           1.91                7168.31
          6           2.02                6699.87
         12           1.93                6962.48
         24           1.98                6804.42
         48           1.96                6688.44
         97           1.91                6849.95
===========  =============  =====================

Concurrency 1
-------------

**Stats**:

==================  =============  =====================
node                ping_icmp, ms  tcp_download, Mbits/s
==================  =============  =====================
node-63.domain.tld           2.16                6158.73
==================  =============  =====================

Concurrency 3
-------------

**Stats**:

==================  =============  =====================
node                ping_icmp, ms  tcp_download, Mbits/s
==================  =============  =====================
node-33.domain.tld           1.93                7268.44
node-60.domain.tld           1.70                7667.30
node-63.domain.tld           2.08                6569.19
==================  =============  =====================

Concurrency 6
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-104.domain.tld           2.12                6275.38
node-107.domain.tld           2.06                6502.40
node-33.domain.tld            1.92                6908.32
node-38.domain.tld            1.71                7947.37
node-60.domain.tld            2.14                6137.23
node-63.domain.tld            2.16                6428.51
===================  =============  =====================

Concurrency 12
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-104.domain.tld           1.85                7299.81
node-107.domain.tld           1.74                7804.58
node-162.domain.tld           2.03                6680.64
node-170.domain.tld           1.74                7522.71
node-182.domain.tld           1.93                6904.67
node-31.domain.tld            1.95                6937.16
node-33.domain.tld            1.80                7400.94
node-35.domain.tld            1.99                6457.84
node-37.domain.tld            2.13                6282.90
node-38.domain.tld            2.19                6214.55
node-60.domain.tld            2.08                6643.84
node-63.domain.tld            1.76                7400.05
===================  =============  =====================

Concurrency 24
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-104.domain.tld           1.89                7550.64
node-107.domain.tld           1.72                7896.51
node-118.domain.tld           1.99                6707.18
node-162.domain.tld           1.90                7289.08
node-170.domain.tld           2.14                6237.33
node-173.domain.tld           1.89                7260.93
node-175.domain.tld           1.75                7701.26
node-182.domain.tld           1.93                6962.98
node-183.domain.tld           2.11                6512.16
node-186.domain.tld           2.05                6346.68
node-31.domain.tld            1.92                7101.47
node-33.domain.tld            2.12                6307.38
node-35.domain.tld            1.96                6945.70
node-37.domain.tld            2.02                6676.56
node-38.domain.tld            2.36                5657.73
node-6.domain.tld             1.68                7739.82
node-60.domain.tld            2.22                6071.31
node-63.domain.tld            2.08                6590.70
node-64.domain.tld            1.90                7054.93
node-66.domain.tld            2.05                6238.28
node-69.domain.tld            1.68                7873.55
node-80.domain.tld            2.09                6067.90
node-83.domain.tld            2.04                6309.97
node-85.domain.tld            2.15                6205.97
===================  =============  =====================

Concurrency 48
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-101.domain.tld           1.81                7076.48
node-102.domain.tld           1.81                7473.93
node-104.domain.tld           2.11                6396.98
node-107.domain.tld           1.55                7521.83
node-108.domain.tld           2.23                6177.01
node-110.domain.tld           2.07                6531.66
node-114.domain.tld           2.06                6387.91
node-118.domain.tld           2.07                6594.98
node-120.domain.tld           2.16                6159.61
node-123.domain.tld           1.88                7027.73
node-125.domain.tld           2.33                5817.55
node-129.domain.tld           1.70                7945.71
node-13.domain.tld            1.99                6751.68
node-141.domain.tld           2.21                6075.71
node-161.domain.tld           1.81                7401.20
node-162.domain.tld           2.18                6210.56
node-163.domain.tld           1.80                7291.88
node-170.domain.tld           1.86                7239.89
node-173.domain.tld           1.91                7105.21
node-175.domain.tld           1.84                7476.81
node-178.domain.tld           2.03                6448.84
node-182.domain.tld           2.06                6842.47
node-183.domain.tld           1.75                7725.56
node-186.domain.tld           2.01                6609.34
node-188.domain.tld           2.17                6150.33
node-190.domain.tld           2.03                6356.78
node-192.domain.tld           2.26                6119.14
node-194.domain.tld           2.16                6007.97
node-196.domain.tld           1.66                7961.12
node-199.domain.tld           2.06                6508.80
node-31.domain.tld            2.19                6272.22
node-33.domain.tld            1.84                7154.33
node-35.domain.tld            1.83                7300.18
node-37.domain.tld            1.97                6949.31
node-38.domain.tld            2.24                5999.33
node-50.domain.tld            1.84                7490.39
node-52.domain.tld            0.32                2977.88
node-56.domain.tld            2.20                6072.12
node-6.domain.tld             2.18                6189.29
node-60.domain.tld            1.78                7433.55
node-63.domain.tld            1.86                7481.29
node-64.domain.tld            1.98                6687.26
node-66.domain.tld            1.80                7406.09
node-69.domain.tld            1.69                7618.44
node-80.domain.tld            2.20                6064.22
node-83.domain.tld            2.10                6102.73
node-85.domain.tld            2.19                6101.86
node-89.domain.tld            2.12                6349.80
===================  =============  =====================

Concurrency 97
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            2.15                6271.69
node-101.domain.tld           1.17                7254.11
node-102.domain.tld           1.78                7605.54
node-104.domain.tld           2.12                6494.07
node-107.domain.tld           1.78                7706.24
node-108.domain.tld           2.15                6182.63
node-110.domain.tld           2.13                6308.67
node-114.domain.tld           1.86                7392.43
node-116.domain.tld           2.02                6249.93
node-118.domain.tld           2.12                6107.34
node-119.domain.tld           2.12                6353.08
node-120.domain.tld           1.80                7447.32
node-123.domain.tld           2.15                6289.15
node-125.domain.tld           2.17                6170.60
node-127.domain.tld           2.06                6413.50
node-129.domain.tld           1.82                7433.55
node-13.domain.tld            2.23                6138.15
node-131.domain.tld           1.67                7692.70
node-133.domain.tld           1.71                7328.75
node-135.domain.tld           2.04                6391.05
node-137.domain.tld           1.96                6916.53
node-139.domain.tld           2.19                6244.69
node-14.domain.tld            2.08                6355.81
node-140.domain.tld           1.86                7096.43
node-141.domain.tld           2.08                6306.10
node-144.domain.tld           2.02                6807.12
node-145.domain.tld           2.28                5931.90
node-146.domain.tld           1.96                6894.59
node-148.domain.tld           1.80                7307.53
node-15.domain.tld            1.81                7582.77
node-151.domain.tld           2.21                5995.43
node-152.domain.tld           2.12                6359.72
node-154.domain.tld           1.77                7384.59
node-156.domain.tld           1.53                6309.03
node-158.domain.tld           2.16                6242.52
node-161.domain.tld           2.10                6534.47
node-162.domain.tld           2.16                6370.40
node-163.domain.tld           1.72                7578.80
node-166.domain.tld           1.95                7098.80
node-168.domain.tld           2.14                6303.41
node-170.domain.tld           2.10                6579.85
node-173.domain.tld           2.18                6326.53
node-175.domain.tld           1.93                7048.81
node-178.domain.tld           2.00                7075.32
node-182.domain.tld           1.76                7641.65
node-183.domain.tld           1.72                7612.63
node-185.domain.tld           2.09                6044.92
node-186.domain.tld           1.73                7400.94
node-188.domain.tld           1.87                7430.09
node-19.domain.tld            2.02                6849.53
node-190.domain.tld           2.14                6291.88
node-192.domain.tld           1.72                7818.09
node-194.domain.tld           1.35                7250.58
node-196.domain.tld           1.67                8130.50
node-199.domain.tld           1.70                7063.20
node-2.domain.tld             1.65                7576.02
node-21.domain.tld            1.55                6708.24
node-23.domain.tld            2.15                6316.56
node-26.domain.tld            2.20                6104.77
node-27.domain.tld            1.65                8021.87
node-28.domain.tld            2.21                6197.98
node-31.domain.tld            1.84                7285.46
node-33.domain.tld            1.78                7493.27
node-35.domain.tld            1.96                6523.79
node-37.domain.tld            1.92                6958.20
node-38.domain.tld            1.82                7298.73
node-42.domain.tld            1.82                7347.38
node-43.domain.tld            2.05                6421.65
node-46.domain.tld            1.92                6926.01
node-47.domain.tld            1.35                7305.80
node-5.domain.tld             2.07                6489.19
node-50.domain.tld            1.82                7424.65
node-52.domain.tld            1.80                7157.00
node-56.domain.tld            1.71                7794.90
node-57.domain.tld            2.07                6460.09
node-58.domain.tld            1.57                8362.34
node-6.domain.tld             2.15                6200.98
node-60.domain.tld            2.12                6241.45
node-63.domain.tld            1.70                7811.28
node-64.domain.tld            2.09                6355.77
node-66.domain.tld            1.79                7293.85
node-69.domain.tld            2.14                5989.40
node-71.domain.tld            2.07                6426.13
node-73.domain.tld            1.54                7431.64
node-76.domain.tld            2.13                6208.68
node-77.domain.tld            1.85                7318.23
node-79.domain.tld            1.59                6157.08
node-80.domain.tld            1.69                7652.52
node-82.domain.tld            2.24                6408.74
node-83.domain.tld            2.11                6170.53
node-85.domain.tld            1.68                6654.28
node-87.domain.tld            1.62                6442.55
node-89.domain.tld            1.79                7711.55
node-91.domain.tld            2.16                6309.05
node-93.domain.tld            2.07                5852.12
node-96.domain.tld            1.62                6447.62
node-99.domain.tld            1.75                7771.68
===================  =============  =====================

Upload
======

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_upload
    title: Upload

.. image:: 40017e10-fbcf-46d6-a652-953d3fffd038.*

**Stats**:

===========  =============  ===================
concurrency  ping_icmp, ms  tcp_upload, Mbits/s
===========  =============  ===================
          1           2.42              5736.11
          3           2.40              6145.09
          6           2.15              6904.19
         12           2.11              7007.88
         24           2.08              7088.64
         48           2.13              6930.26
         97           2.14              6919.27
===========  =============  ===================

Concurrency 1
-------------

**Stats**:

==================  =============  ===================
node                ping_icmp, ms  tcp_upload, Mbits/s
==================  =============  ===================
node-63.domain.tld           2.42              5736.11
==================  =============  ===================

Concurrency 3
-------------

**Stats**:

==================  =============  ===================
node                ping_icmp, ms  tcp_upload, Mbits/s
==================  =============  ===================
node-33.domain.tld           2.27              6541.54
node-60.domain.tld           2.41              6133.55
node-63.domain.tld           2.52              5760.17
==================  =============  ===================

Concurrency 6
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-104.domain.tld           2.02              7183.05
node-107.domain.tld           1.84              7922.05
node-33.domain.tld            2.60              5806.30
node-38.domain.tld            2.30              6429.33
node-60.domain.tld            1.83              7834.27
node-63.domain.tld            2.30              6250.14
===================  =============  ===================

Concurrency 12
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-104.domain.tld           1.88              7829.94
node-107.domain.tld           1.81              8050.55
node-162.domain.tld           1.98              7496.39
node-170.domain.tld           2.26              6487.37
node-182.domain.tld           2.07              7173.40
node-31.domain.tld            1.83              7592.78
node-33.domain.tld            1.96              7389.17
node-35.domain.tld            2.45              6103.92
node-37.domain.tld            1.88              7571.15
node-38.domain.tld            2.35              6172.75
node-60.domain.tld            2.40              6255.05
node-63.domain.tld            2.45              5972.06
===================  =============  ===================

Concurrency 24
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-104.domain.tld           1.83              7855.21
node-107.domain.tld           2.40              6279.43
node-118.domain.tld           1.74              8128.61
node-162.domain.tld           1.95              7365.63
node-170.domain.tld           2.27              6805.82
node-173.domain.tld           1.81              7889.94
node-175.domain.tld           2.38              6406.78
node-182.domain.tld           2.40              6107.22
node-183.domain.tld           2.24              6847.47
node-186.domain.tld           2.04              6983.52
node-31.domain.tld            1.77              8050.89
node-33.domain.tld            1.84              7564.47
node-35.domain.tld            2.14              5897.26
node-37.domain.tld            1.87              7831.94
node-38.domain.tld            1.87              7611.12
node-6.domain.tld             1.87              7934.42
node-60.domain.tld            1.83              8043.81
node-63.domain.tld            2.47              5853.63
node-64.domain.tld            2.38              6178.55
node-66.domain.tld            1.88              7904.73
node-69.domain.tld            2.26              6343.36
node-80.domain.tld            1.84              7915.54
node-83.domain.tld            2.53              6183.71
node-85.domain.tld            2.38              6144.35
===================  =============  ===================

Concurrency 48
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-101.domain.tld           2.39              6224.35
node-102.domain.tld           2.09              7068.28
node-104.domain.tld           1.85              7853.71
node-107.domain.tld           1.83              8236.92
node-108.domain.tld           2.28              6211.24
node-110.domain.tld           1.96              7387.10
node-114.domain.tld           1.97              7402.35
node-118.domain.tld           2.31              6275.21
node-120.domain.tld           2.30              6422.86
node-123.domain.tld           2.32              6358.91
node-125.domain.tld           1.97              7514.45
node-129.domain.tld           1.87              7871.76
node-13.domain.tld            2.15              6724.65
node-141.domain.tld           2.44              6013.55
node-161.domain.tld           1.91              7619.43
node-162.domain.tld           2.43              6069.52
node-163.domain.tld           2.41              6196.49
node-170.domain.tld           2.11              7111.69
node-173.domain.tld           2.23              6536.13
node-175.domain.tld           2.27              6741.28
node-178.domain.tld           2.18              6724.81
node-182.domain.tld           2.09              7285.57
node-183.domain.tld           2.26              6486.64
node-186.domain.tld           2.40              6022.67
node-188.domain.tld           2.53              5940.53
node-190.domain.tld           1.93              7449.46
node-192.domain.tld           2.22              6742.75
node-194.domain.tld           1.92              7367.92
node-196.domain.tld           2.11              6693.30
node-199.domain.tld           2.26              6580.84
node-31.domain.tld            1.77              8020.08
node-33.domain.tld            1.89              7835.22
node-35.domain.tld            2.41              6005.63
node-37.domain.tld            1.73              7855.55
node-38.domain.tld            2.33              6376.93
node-50.domain.tld            1.98              7470.82
node-52.domain.tld            2.36              6202.68
node-56.domain.tld            1.97              7436.52
node-6.domain.tld             1.87              7620.21
node-60.domain.tld            2.38              6281.14
node-63.domain.tld            2.49              5867.09
node-64.domain.tld            1.87              7910.78
node-66.domain.tld            2.37              6121.72
node-69.domain.tld            1.84              7702.03
node-80.domain.tld            1.81              7762.21
node-83.domain.tld            2.04              7301.27
node-85.domain.tld            1.80              7642.28
node-89.domain.tld            2.46              6106.13
===================  =============  ===================

Concurrency 97
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            2.16              7086.80
node-101.domain.tld           2.29              6377.29
node-102.domain.tld           1.91              7437.30
node-104.domain.tld           1.83              7926.08
node-107.domain.tld           2.37              6368.36
node-108.domain.tld           2.36              6146.99
node-110.domain.tld           2.20              7073.77
node-114.domain.tld           1.89              7927.43
node-116.domain.tld           1.97              7599.34
node-118.domain.tld           2.54              5862.40
node-119.domain.tld           2.47              6079.37
node-120.domain.tld           2.02              7368.22
node-123.domain.tld           2.31              6367.33
node-125.domain.tld           1.99              7281.10
node-127.domain.tld           2.02              7257.33
node-129.domain.tld           1.91              7600.53
node-13.domain.tld            2.25              6487.05
node-131.domain.tld           2.24              6393.11
node-133.domain.tld           2.19              7078.86
node-135.domain.tld           2.31              6154.54
node-137.domain.tld           2.12              6844.44
node-139.domain.tld           2.17              6736.65
node-14.domain.tld            1.85              7620.85
node-140.domain.tld           2.24              6770.58
node-141.domain.tld           2.43              6078.84
node-144.domain.tld           1.91              7712.92
node-145.domain.tld           1.99              7104.05
node-146.domain.tld           1.96              7684.36
node-148.domain.tld           1.84              7470.18
node-15.domain.tld            2.32              6356.18
node-151.domain.tld           2.01              7388.88
node-152.domain.tld           1.83              7662.53
node-154.domain.tld           2.39              6359.06
node-156.domain.tld           2.31              6470.02
node-158.domain.tld           2.39              6145.61
node-161.domain.tld           2.38              6076.91
node-162.domain.tld           1.82              7796.89
node-163.domain.tld           1.84              7622.43
node-166.domain.tld           2.17              6901.96
node-168.domain.tld           1.87              7822.04
node-170.domain.tld           2.00              7580.97
node-173.domain.tld           2.45              5933.53
node-175.domain.tld           1.92              7360.78
node-178.domain.tld           2.16              6793.26
node-182.domain.tld           2.58              5860.38
node-183.domain.tld           2.14              7271.37
node-185.domain.tld           2.22              6530.54
node-186.domain.tld           2.25              6625.85
node-188.domain.tld           2.44              6297.71
node-19.domain.tld            2.22              6675.59
node-190.domain.tld           1.94              7573.03
node-192.domain.tld           2.18              6835.22
node-194.domain.tld           2.18              6627.49
node-196.domain.tld           2.15              7071.06
node-199.domain.tld           1.86              7919.52
node-2.domain.tld             1.92              7600.47
node-21.domain.tld            1.85              7890.73
node-23.domain.tld            2.27              6606.12
node-26.domain.tld            1.95              7573.56
node-27.domain.tld            2.36              6373.93
node-28.domain.tld            2.29              6542.26
node-31.domain.tld            1.85              7624.65
node-33.domain.tld            2.37              6087.56
node-35.domain.tld            2.29              6304.19
node-37.domain.tld            2.40              6192.03
node-38.domain.tld            1.81              7564.09
node-42.domain.tld            2.41              6173.61
node-43.domain.tld            2.31              6445.34
node-46.domain.tld            1.92              7482.00
node-47.domain.tld            1.98              7605.16
node-5.domain.tld             1.93              7530.01
node-50.domain.tld            1.90              7521.39
node-52.domain.tld            2.14              7045.94
node-56.domain.tld            1.92              7488.06
node-57.domain.tld            1.89              7584.44
node-58.domain.tld            2.30              6400.75
node-6.domain.tld             2.46              5926.02
node-60.domain.tld            2.48              5801.62
node-63.domain.tld            2.35              6205.54
node-64.domain.tld            2.31              6281.44
node-66.domain.tld            1.92              7736.11
node-69.domain.tld            2.45              6055.67
node-71.domain.tld            1.96              7690.57
node-73.domain.tld            2.31              6551.94
node-76.domain.tld            1.91              7545.96
node-77.domain.tld            2.17              6582.52
node-79.domain.tld            2.40              6107.38
node-80.domain.tld            2.44              6063.29
node-82.domain.tld            1.96              7354.60
node-83.domain.tld            2.12              7089.25
node-85.domain.tld            2.26              6250.53
node-87.domain.tld            1.97              7676.71
node-89.domain.tld            1.90              7842.22
node-91.domain.tld            2.01              7572.32
node-93.domain.tld            1.99              7130.99
node-96.domain.tld            2.34              6355.15
node-99.domain.tld            2.45              6258.08
===================  =============  ===================

