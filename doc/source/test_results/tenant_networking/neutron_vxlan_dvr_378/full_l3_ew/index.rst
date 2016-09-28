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
    file_name: shaker/shaker/scenarios/openstack/full_l3_east_west.yaml
    title: OpenStack L3 East-West

Bi-directional
==============

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_bidirectional
    title: Bi-directional

.. image:: 0663aaa1-6404-4f91-89f5-759722b11b9a.*

**Stats**:

===========  =============  =====================  ===================
concurrency  ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===========  =============  =====================  ===================
          1           1.87                6133.72              6239.35
          2           1.90                6351.59              6216.00
          5           1.68                6855.89              6941.04
         11           1.75                6621.63              6679.62
         23           1.96                6104.99              6064.53
         46           1.97                6090.82              6047.78
         92           1.79                5901.71              5627.92
        185           1.24                4670.85              4789.33
===========  =============  =====================  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-241.domain.tld           1.87                6133.72              6239.35
===================  =============  =====================  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-192.domain.tld           1.77                6421.32              6283.28
node-241.domain.tld           2.03                6281.86              6148.73
===================  =============  =====================  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-192.domain.tld           1.54                6899.34              6881.06
node-195.domain.tld           1.72                7420.67              7630.49
node-211.domain.tld           1.90                6382.10              6717.00
node-224.domain.tld           1.60                6784.29              6602.31
node-241.domain.tld           1.66                6793.05              6874.36
===================  =============  =====================  ===================

Concurrency 11
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-149.domain.tld           1.81                6681.41              6747.76
node-192.domain.tld           1.62                6497.66              6578.62
node-195.domain.tld           1.89                6396.81              6532.91
node-199.domain.tld           1.52                7772.98              7476.76
node-209.domain.tld           1.55                7199.33              7345.44
node-211.domain.tld           1.82                6652.37              6490.39
node-213.domain.tld           1.69                6787.36              6960.05
node-214.domain.tld           1.76                6773.23              6811.50
node-224.domain.tld           1.62                6678.62              6795.29
node-241.domain.tld           1.72                6588.50              6762.16
node-391.domain.tld           2.28                4809.64              4974.97
===================  =============  =====================  ===================

Concurrency 23
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            2.00                5453.50              6125.34
node-104.domain.tld           2.38                4531.42              4572.89
node-149.domain.tld           1.80                6700.36              6654.30
node-192.domain.tld           1.79                6444.67              6398.16
node-195.domain.tld           1.88                6177.15              5896.52
node-199.domain.tld           1.96                6652.23              6664.60
node-209.domain.tld           1.52                7158.08              7166.74
node-211.domain.tld           1.52                6995.43              6901.98
node-213.domain.tld           2.07                6176.21              5995.13
node-214.domain.tld           1.65                6932.57              6855.74
node-224.domain.tld           1.78                6267.52              6301.31
node-241.domain.tld           1.64                6715.65              6690.07
node-262.domain.tld           2.12                6519.31              6425.12
node-337.domain.tld           2.80                4380.47              4109.11
node-390.domain.tld           2.25                4641.53              4545.78
node-391.domain.tld           2.22                5040.50              5047.64
node-432.domain.tld           2.41                4763.28              5095.45
node-449.domain.tld           1.93                6451.14              6213.17
node-475.domain.tld           1.88                6671.98              6444.61
node-481.domain.tld           1.74                6991.63              7310.98
node-517.domain.tld           2.30                5825.36              4958.00
node-60.domain.tld            1.67                6731.33              6873.67
node-70.domain.tld            1.86                6193.33              6237.95
===================  =============  =====================  ===================

Concurrency 46
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            2.16                5032.88              4895.23
node-104.domain.tld           2.23                5015.73              4864.01
node-123.domain.tld           2.02                6030.43              6007.91
node-149.domain.tld           1.84                6653.21              6542.01
node-192.domain.tld           1.52                7623.90              7235.22
node-195.domain.tld           1.93                6251.48              6128.25
node-199.domain.tld           1.84                6334.56              6366.78
node-209.domain.tld           1.63                6733.59              6417.51
node-211.domain.tld           1.65                7023.09              6983.55
node-213.domain.tld           2.09                6115.34              6117.95
node-214.domain.tld           1.57                6813.69              6940.05
node-224.domain.tld           1.88                6094.90              6500.20
node-241.domain.tld           1.73                6793.27              6908.45
node-262.domain.tld           1.85                6924.16              6784.27
node-276.domain.tld           2.26                4647.52              4659.42
node-283.domain.tld           2.43                5087.65              4840.09
node-337.domain.tld           2.47                4809.02              4531.80
node-349.domain.tld           2.40                4774.07              4521.18
node-356.domain.tld           1.74                6538.33              6459.38
node-368.domain.tld           1.67                7126.29              6852.57
node-376.domain.tld           1.93                6379.47              6341.59
node-390.domain.tld           2.40                4775.19              4609.30
node-391.domain.tld           2.03                5263.58              5316.08
node-402.domain.tld           1.69                6998.94              7044.76
node-432.domain.tld           2.14                5113.42              5521.78
node-449.domain.tld           2.50                4709.25              4614.82
node-460.domain.tld           1.71                6762.50              6706.57
node-470.domain.tld           1.96                6287.28              6177.81
node-473.domain.tld           1.81                6532.50              6537.99
node-475.domain.tld           1.94                6180.44              6240.05
node-479.domain.tld           2.03                5829.34              6085.68
node-481.domain.tld           1.83                7171.67              7093.15
node-483.domain.tld           1.74                6833.26              7076.82
node-484.domain.tld           1.95                6202.34              6207.79
node-486.domain.tld           1.92                6228.71              6319.51
node-493.domain.tld           1.99                6096.98              6054.48
node-501.domain.tld           2.04                6198.36              6217.78
node-505.domain.tld           2.10                5854.33              5372.37
node-506.domain.tld           2.03                5960.18              5928.25
node-511.domain.tld           1.79                6911.33              6999.07
node-517.domain.tld           1.80                7013.15              6720.11
node-519.domain.tld           1.94                6076.61              5935.22
node-60.domain.tld            2.05                5650.58              5639.89
node-70.domain.tld            2.60                4234.11              4081.71
node-83.domain.tld            1.74                6371.51              6505.99
node-84.domain.tld            1.92                6119.55              6293.39
===================  =============  =====================  ===================

Concurrency 92
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            2.26                5092.78              5265.06
node-103.domain.tld           1.98                6317.81              6205.90
node-104.domain.tld           2.45                4585.77              4605.27
node-121.domain.tld           2.30                4323.30              3291.47
node-123.domain.tld           3.47                3667.31               692.39
node-127.domain.tld           2.04                6281.53              6211.57
node-142.domain.tld           1.38                8314.04              6959.78
node-149.domain.tld           1.29                4985.82              8850.03
node-162.domain.tld           2.03                6110.13              5974.62
node-173.domain.tld           0.60                2829.90              8114.19
node-175.domain.tld           0.53                 987.85              6581.44
node-177.domain.tld           0.42                5782.02              2829.23
node-180.domain.tld           1.82                6515.14              6447.66
node-182.domain.tld           0.45                5056.05              2887.91
node-185.domain.tld           1.18                3384.41              9647.57
node-188.domain.tld           0.76                8956.82              1047.24
node-192.domain.tld           5.32                9626.95              1849.32
node-195.domain.tld           1.66                7557.73              7179.93
node-199.domain.tld           1.11                4027.86              9546.46
node-209.domain.tld           0.96                9359.02              3762.70
node-211.domain.tld           0.96                9027.71              4581.89
node-213.domain.tld           1.57                6953.10              6912.13
node-214.domain.tld           1.07                3556.52              9680.31
node-224.domain.tld           1.20                6602.23              6352.18
node-226.domain.tld           1.99                6257.21              6237.61
node-228.domain.tld           1.49                8678.94              3711.91
node-241.domain.tld           1.61                6931.83              6902.74
node-248.domain.tld           1.32                9833.55               333.65
node-254.domain.tld           0.49                1162.98              5576.16
node-260.domain.tld           2.43                4788.84              4833.24
node-262.domain.tld           0.40                4977.39              3330.75
node-276.domain.tld           2.47                4712.69              4879.94
node-283.domain.tld           2.46                4953.08              4759.69
node-291.domain.tld           1.71                7251.33              7157.80
node-292.domain.tld           1.88                6788.22              6734.88
node-298.domain.tld           1.30                4139.05              8348.95
node-301.domain.tld           1.79                6148.63              6364.80
node-306.domain.tld           2.33                4477.84              5097.89
node-309.domain.tld           1.29                4787.74              7147.75
node-313.domain.tld           1.89                6410.63              6305.58
node-315.domain.tld           1.89                6573.53              6397.89
node-317.domain.tld           1.06                7292.04              5841.09
node-337.domain.tld           2.38                4862.03              4687.11
node-343.domain.tld           2.13                5444.59              5636.66
node-349.domain.tld           2.24                5289.38              4905.25
node-356.domain.tld           1.80                6267.49              6582.08
node-359.domain.tld           2.59                4354.70              4182.13
node-368.domain.tld           1.00                8702.09              3281.02
node-376.domain.tld           1.69                6829.67              6189.79
node-390.domain.tld           2.45                4746.88              4579.71
node-391.domain.tld           2.50                4564.68              4630.23
node-402.domain.tld           1.73                6344.54              6431.46
node-424.domain.tld           2.41                4544.85              4541.80
node-432.domain.tld           2.26                4841.94              5580.44
node-449.domain.tld           2.45                4652.51              4422.01
node-450.domain.tld           1.65                6675.24              6680.93
node-451.domain.tld           2.46                4566.65              4539.61
node-455.domain.tld           2.67                9465.37              3241.36
node-459.domain.tld           6.81                 946.99              2353.14
node-460.domain.tld           0.99                9457.50              4115.67
node-465.domain.tld           1.98                6286.17              6248.98
node-466.domain.tld           1.84                6436.28              6360.76
node-467.domain.tld           1.47                7518.64              6484.19
node-469.domain.tld           0.92                9627.73               813.72
node-470.domain.tld           1.41                3156.95              9160.75
node-473.domain.tld           1.18                4363.96              9120.77
node-475.domain.tld           1.22                8810.80              4092.86
node-479.domain.tld           1.98                6543.23              6323.63
node-481.domain.tld           0.47                6574.88              3855.49
node-483.domain.tld           1.68                6782.93              6820.61
node-484.domain.tld           1.92                6093.32              6057.70
node-485.domain.tld           1.34                8692.10              2939.40
node-486.domain.tld           1.60                4393.29              8326.84
node-489.domain.tld           1.66                4042.06              7997.92
node-490.domain.tld           1.87                6477.11              6244.22
node-493.domain.tld           1.77                6445.02              6597.57
node-501.domain.tld           2.07                6183.75              6022.83
node-503.domain.tld           1.13                6354.69              7005.04
node-505.domain.tld           1.88                6011.79              6409.54
node-506.domain.tld           2.01                5955.92              5945.84
node-507.domain.tld           2.17                3725.89              7443.74
node-508.domain.tld           0.80                1859.54              9424.94
node-511.domain.tld           1.85                6510.35              6813.66
node-517.domain.tld           1.90                6386.40              6084.16
node-519.domain.tld           1.94                5908.51              6230.91
node-522.domain.tld           2.84                1781.58              5558.86
node-60.domain.tld            2.41                4550.57              5130.16
node-70.domain.tld            2.00                6483.57              6099.57
node-83.domain.tld            1.99                6261.41              6191.78
node-84.domain.tld            1.34                8700.56              3175.87
node-96.domain.tld            1.58                7051.19              6387.49
node-99.domain.tld            1.42                8362.84              4380.12
===================  =============  =====================  ===================

Concurrency 185
---------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            1.31                9160.95              4258.58
node-103.domain.tld           0.60                4324.33              3503.40
node-104.domain.tld           2.40                4545.76              4589.61
node-117.domain.tld           0.77                7115.22              2481.79
node-121.domain.tld           0.65                3044.93              5927.55
node-123.domain.tld           0.70                5029.12              3533.20
node-126.domain.tld           2.30                4706.50              4708.00
node-127.domain.tld           0.84                4085.72              6250.74
node-131.domain.tld           2.51                4902.42              4767.80
node-134.domain.tld           2.69                4250.15              4368.61
node-136.domain.tld           0.57                2794.98              3353.31
node-138.domain.tld           0.67                5134.38              2800.82
node-139.domain.tld           2.22                4273.60              5519.34
node-141.domain.tld           0.82                3183.12              9741.30
node-142.domain.tld           0.58                3038.86              3660.34
node-147.domain.tld           2.64                4474.53              4313.09
node-149.domain.tld           0.63                4992.62              5442.12
node-150.domain.tld           1.28                3798.23              3120.50
node-153.domain.tld           0.49                3924.43              2997.52
node-158.domain.tld           0.58                5864.06              3391.91
node-162.domain.tld           0.59                2964.94              4082.54
node-173.domain.tld           0.58                3476.51              4328.82
node-175.domain.tld           0.54                3021.12              4602.88
node-177.domain.tld           0.61                3654.51              4252.85
node-180.domain.tld           1.77                6547.89              6376.76
node-182.domain.tld           0.70                3146.55              6892.87
node-185.domain.tld           0.64                3632.91              6371.80
node-188.domain.tld           0.59                4565.77              2958.71
node-192.domain.tld           0.48                4008.75              3648.50
node-195.domain.tld           1.80                6634.43              6581.34
node-199.domain.tld           1.16                3592.19              5681.06
node-201.domain.tld           0.49                3323.50              3799.62
node-202.domain.tld           1.64                7046.07              7115.64
node-209.domain.tld           0.57                4091.81              3457.18
node-211.domain.tld           0.71                3190.74              3532.09
node-213.domain.tld           1.58                6870.32              6956.98
node-214.domain.tld           0.60                4562.29              3643.08
node-22.domain.tld            1.56                8024.02              3888.01
node-224.domain.tld           0.71                8724.38              2742.66
node-226.domain.tld           1.83                6625.07              6470.30
node-228.domain.tld           0.59                3641.48              1682.00
node-233.domain.tld           0.78                9722.28              1983.66
node-236.domain.tld           0.58                2842.76              2423.52
node-237.domain.tld           0.58                2300.15              4171.25
node-241.domain.tld           1.76                6791.33              6645.19
node-248.domain.tld           0.50                3082.67              4640.81
node-254.domain.tld           0.45                3147.62              3796.58
node-256.domain.tld           2.38                4745.85              4895.95
node-259.domain.tld           2.30                4616.68              4655.38
node-260.domain.tld           1.62                1541.01              7562.27
node-262.domain.tld           0.61                2035.66              4032.89
node-264.domain.tld           0.60                4106.25              2953.58
node-266.domain.tld           0.57                3890.53              3394.03
node-268.domain.tld           1.98                6063.73              6102.32
node-271.domain.tld           0.51                4467.07              3886.95
node-272.domain.tld           2.00                6048.86              6100.06
node-275.domain.tld           1.60                6593.13              7012.86
node-276.domain.tld           2.51                4609.37              4621.19
node-283.domain.tld           2.91                4330.48              4017.96
node-287.domain.tld           1.81                6322.37              6181.21
node-291.domain.tld           2.05                5979.41              6005.83
node-292.domain.tld           1.90                6399.65              6437.23
node-298.domain.tld           0.46                2789.37              5988.48
node-301.domain.tld           1.63                6633.29              3385.73
node-303.domain.tld           0.63                3791.13              3179.43
node-306.domain.tld           0.82                5288.88              1451.68
node-309.domain.tld           0.87                3279.83              3359.22
node-313.domain.tld           1.99                6221.94              6189.73
node-315.domain.tld           0.55                 853.61              3179.07
node-316.domain.tld           2.06                5078.70              5273.93
node-317.domain.tld           1.27                3518.37              3403.37
node-318.domain.tld           1.34                9051.07              2878.28
node-321.domain.tld           0.61                3821.38              2449.32
node-323.domain.tld           0.65                7181.15              2212.56
node-324.domain.tld           1.54                7309.34              7395.21
node-328.domain.tld           0.49                3268.27              2523.06
node-336.domain.tld           1.70                6637.92              6641.26
node-337.domain.tld           2.62                4662.54              4413.69
node-339.domain.tld           0.55                5257.91              4660.82
node-340.domain.tld           1.55                7309.87              7167.50
node-342.domain.tld           1.16                2250.83              9384.59
node-343.domain.tld           1.92                6504.91              4342.32
node-345.domain.tld           1.80                6804.49              7096.88
node-349.domain.tld           2.18                5293.33              4018.74
node-350.domain.tld           1.85                6927.26              6415.48
node-354.domain.tld           1.96                5840.81              5779.17
node-356.domain.tld           1.89                6090.75              6370.73
node-358.domain.tld           0.62                3956.13              3822.96
node-359.domain.tld           1.65                6812.60              2970.29
node-360.domain.tld           2.88                4248.88              4191.79
node-362.domain.tld           0.48                2240.81              5201.81
node-363.domain.tld           0.65                2246.78              3870.74
node-364.domain.tld           0.48                2288.01              4837.82
node-365.domain.tld           1.67                6253.41              2797.71
node-368.domain.tld           0.56                2196.89              5076.09
node-369.domain.tld           2.48                4493.34              4408.30
node-372.domain.tld           0.83                3961.12              2939.70
node-374.domain.tld           3.71                3611.75               358.64
node-376.domain.tld           0.72                5836.31              4839.79
node-377.domain.tld           0.62                3426.52              4535.41
node-378.domain.tld           0.53                3310.29              3131.30
node-382.domain.tld           1.93                6531.47              6581.50
node-385.domain.tld           0.71                2695.84              7422.80
node-386.domain.tld           0.53                3908.87              2894.03
node-390.domain.tld           2.44                4810.56              4653.45
node-391.domain.tld           2.32                5001.21              4961.16
node-396.domain.tld           2.00                6248.88              5498.53
node-397.domain.tld           0.71                2194.77              3506.69
node-40.domain.tld            1.99                3608.41              6019.82
node-402.domain.tld           1.71                6984.34              6857.53
node-405.domain.tld           1.09                3281.22              9679.92
node-406.domain.tld           1.75                6696.47              6471.83
node-407.domain.tld           0.40                 866.97              3657.25
node-414.domain.tld           1.82                6221.85              6272.24
node-418.domain.tld           2.44                4683.63              4491.79
node-419.domain.tld           2.45                4474.74              4614.93
node-420.domain.tld           0.55                4025.43              2460.38
node-424.domain.tld           2.20                5026.67              4822.23
node-429.domain.tld           0.68                3955.32              5232.17
node-43.domain.tld            2.07                5154.35              4246.60
node-431.domain.tld           0.60                3297.02              4249.60
node-432.domain.tld           1.02                4625.14              3737.89
node-433.domain.tld           0.48                3086.47              6142.08
node-437.domain.tld           1.64                6991.30              6894.49
node-439.domain.tld           0.59                3955.71              4504.93
node-44.domain.tld            1.64                5889.20              3479.44
node-440.domain.tld           0.52                5248.74              3413.48
node-445.domain.tld           0.98                2042.49              9673.59
node-449.domain.tld           1.95                2829.72              5972.37
node-450.domain.tld           0.58                2435.73              4541.80
node-451.domain.tld           3.13                3898.13              3855.32
node-455.domain.tld           0.56                2940.24              4600.83
node-456.domain.tld           0.64                3457.30              5178.14
node-459.domain.tld           3.57                 304.94              3903.71
node-460.domain.tld           0.61                2802.29              6162.24
node-465.domain.tld           0.63                2244.31              4238.16
node-466.domain.tld           1.84                6132.77              5925.87
node-467.domain.tld           0.57                2179.05              7521.71
node-469.domain.tld           0.65                5509.20              3744.88
node-47.domain.tld            1.43                6300.98              4263.72
node-470.domain.tld           0.71                2674.18              7695.30
node-472.domain.tld           0.85                6471.17              4043.88
node-473.domain.tld           0.43                3052.94              5050.62
node-475.domain.tld           0.47                6016.52              3042.94
node-479.domain.tld           0.96                6936.01              4669.43
node-48.domain.tld            2.61                4609.29              4536.65
node-481.domain.tld           0.78                9809.82              1904.89
node-482.domain.tld           0.81                6679.23              3412.12
node-483.domain.tld           0.83                4137.71              7120.43
node-484.domain.tld           1.99                6273.55              6206.45
node-485.domain.tld           0.97                1852.31              9204.67
node-486.domain.tld           0.83                1677.82              7641.08
node-488.domain.tld           0.52                3167.69              2897.74
node-489.domain.tld           1.03                3434.25              8116.51
node-490.domain.tld           1.68                6919.26              6606.39
node-493.domain.tld           1.09                2816.57              4618.48
node-496.domain.tld           0.62                1755.02              6645.42
node-498.domain.tld           0.57                4147.75              5428.78
node-501.domain.tld           0.77                3003.21              7957.93
node-503.domain.tld           0.48                3627.13              2471.14
node-505.domain.tld           0.75                2346.74              3583.45
node-506.domain.tld           1.89                6735.80              6561.02
node-507.domain.tld           0.58                3225.15              4652.98
node-508.domain.tld           0.97                2141.84              6544.16
node-51.domain.tld            2.60                4461.20              4313.68
node-511.domain.tld           1.79                6759.02              6816.20
node-517.domain.tld           1.71                6281.80              6917.68
node-519.domain.tld           0.94                7531.20              3966.92
node-522.domain.tld           1.35                1553.35              5314.45
node-53.domain.tld            1.12                4770.42              4033.20
node-54.domain.tld            1.30                9361.48              4340.16
node-57.domain.tld            0.75                4314.62              6340.40
node-59.domain.tld            0.91                3151.53              8430.10
node-60.domain.tld            1.65                7896.22              3182.65
node-61.domain.tld            0.68                7339.25              2629.02
node-63.domain.tld            0.93                3675.81              7542.79
node-64.domain.tld            1.78                7131.61              3699.91
node-69.domain.tld            1.30                5866.17              3008.98
node-70.domain.tld            1.64                6976.45              3165.68
node-71.domain.tld            0.77                5602.43              2239.15
node-76.domain.tld            1.38                7195.05              2660.11
node-83.domain.tld            0.59                4957.49              2485.38
node-84.domain.tld            0.74                4504.59              4501.20
node-96.domain.tld            0.64                3580.82              3641.97
node-99.domain.tld            0.59                4967.48              2375.64
===================  =============  =====================  ===================

Download
========

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_download
    title: Download

.. image:: e0d02623-e9ec-41af-bb11-d42d861769c7.*

**Stats**:

===========  =============  =====================
concurrency  ping_icmp, ms  tcp_download, Mbits/s
===========  =============  =====================
          1           0.39                9836.77
          2           0.42                9835.04
          5           0.43                9836.65
         11           0.50                9756.24
         23           0.68                9506.29
         46           0.65                9608.64
         92           0.66                9067.39
        185           0.70                7745.13
===========  =============  =====================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-241.domain.tld           0.39                9836.77
===================  =============  =====================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-192.domain.tld           0.48                9834.38
node-241.domain.tld           0.36                9835.71
===================  =============  =====================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-192.domain.tld           0.41                9836.19
node-195.domain.tld           0.45                9838.42
node-211.domain.tld           0.39                9837.63
node-224.domain.tld           0.44                9836.86
node-241.domain.tld           0.45                9834.14
===================  =============  =====================

Concurrency 11
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-149.domain.tld           0.40                9838.60
node-192.domain.tld           0.46                9837.95
node-195.domain.tld           0.47                9825.20
node-199.domain.tld           0.50                9835.64
node-209.domain.tld           0.40                9838.43
node-211.domain.tld           0.41                9840.00
node-213.domain.tld           0.49                9839.34
node-214.domain.tld           0.43                9834.84
node-224.domain.tld           0.43                9837.15
node-241.domain.tld           0.39                9837.32
node-391.domain.tld           1.07                8954.12
===================  =============  =====================

Concurrency 23
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            1.33                8591.46
node-104.domain.tld           1.70                6821.78
node-149.domain.tld           0.44                9805.61
node-192.domain.tld           0.41                9839.57
node-195.domain.tld           0.45                9839.87
node-199.domain.tld           0.45                9835.63
node-209.domain.tld           0.39                9838.75
node-211.domain.tld           0.44                9838.68
node-213.domain.tld           0.50                9836.72
node-214.domain.tld           0.43                9832.99
node-224.domain.tld           0.40                9839.53
node-241.domain.tld           0.41                9837.75
node-262.domain.tld           0.48                9826.53
node-337.domain.tld           1.38                8475.17
node-390.domain.tld           1.19                9007.77
node-391.domain.tld           1.11                8750.24
node-432.domain.tld           0.51                9834.08
node-449.domain.tld           0.67                9826.31
node-475.domain.tld           0.50                9835.34
node-481.domain.tld           0.48                9826.17
node-517.domain.tld           0.60                9836.99
node-60.domain.tld            0.75                9830.95
node-70.domain.tld            0.69                9836.82
===================  =============  =====================

Concurrency 46
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            0.57                9837.47
node-104.domain.tld           1.06                9383.50
node-123.domain.tld           0.47                9827.24
node-149.domain.tld           0.41                9831.67
node-192.domain.tld           0.46                9836.24
node-195.domain.tld           0.54                9834.50
node-199.domain.tld           0.52                9832.61
node-209.domain.tld           0.48                9784.59
node-211.domain.tld           0.44                9837.13
node-213.domain.tld           0.43                9838.67
node-214.domain.tld           0.42                9833.96
node-224.domain.tld           0.57                9697.15
node-241.domain.tld           0.43                9834.43
node-262.domain.tld           0.50                9836.56
node-276.domain.tld           1.37                8185.40
node-283.domain.tld           1.02                9400.62
node-337.domain.tld           1.18                8697.10
node-349.domain.tld           0.48                9835.07
node-356.domain.tld           0.39                9839.05
node-368.domain.tld           0.47                9838.96
node-376.domain.tld           0.47                9839.86
node-390.domain.tld           1.16                8546.48
node-391.domain.tld           0.81                9396.65
node-402.domain.tld           0.42                9837.20
node-432.domain.tld           0.54                9837.72
node-449.domain.tld           0.84                9731.74
node-460.domain.tld           0.43                9830.99
node-470.domain.tld           0.54                9816.15
node-473.domain.tld           0.99                9327.95
node-475.domain.tld           0.51                9822.61
node-479.domain.tld           0.51                9816.64
node-481.domain.tld           0.42                9838.43
node-483.domain.tld           0.55                9838.94
node-484.domain.tld           0.69                9831.49
node-486.domain.tld           0.49                9834.96
node-493.domain.tld           0.58                9838.40
node-501.domain.tld           0.44                9838.79
node-505.domain.tld           0.87                9545.73
node-506.domain.tld           1.04                9123.27
node-511.domain.tld           0.49                9833.41
node-517.domain.tld           0.61                9834.19
node-519.domain.tld           0.48                9838.42
node-60.domain.tld            1.41                7811.23
node-70.domain.tld            1.23                8684.95
node-83.domain.tld            0.53                9821.75
node-84.domain.tld            0.50                9837.58
===================  =============  =====================

Concurrency 92
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            1.19                8594.24
node-103.domain.tld           0.64                9756.06
node-104.domain.tld           1.32                8673.47
node-121.domain.tld           0.44                7610.87
node-123.domain.tld           0.82                9740.27
node-127.domain.tld           0.34                7116.74
node-142.domain.tld           0.69                9806.34
node-149.domain.tld           0.67                9831.02
node-162.domain.tld           0.42                9822.91
node-173.domain.tld           0.61                8462.15
node-175.domain.tld           0.45                7171.50
node-177.domain.tld           0.50                8021.89
node-180.domain.tld           0.45                9839.11
node-182.domain.tld           0.50                8301.87
node-185.domain.tld           0.56                9814.31
node-188.domain.tld           0.56                9735.14
node-192.domain.tld           0.52                9831.62
node-195.domain.tld           0.45                9838.60
node-199.domain.tld           0.61                9836.58
node-209.domain.tld           0.66                9806.76
node-211.domain.tld           0.60                9832.24
node-213.domain.tld           0.46                9837.41
node-214.domain.tld           0.52                9790.48
node-224.domain.tld           0.53                9839.81
node-226.domain.tld           0.40                9837.93
node-228.domain.tld           0.56                9833.08
node-241.domain.tld           0.52                9824.24
node-248.domain.tld           0.72                9720.00
node-254.domain.tld           0.70                9799.96
node-260.domain.tld           1.12                9466.82
node-262.domain.tld           0.50                8436.40
node-276.domain.tld           1.34                7830.72
node-283.domain.tld           1.49                7700.81
node-291.domain.tld           0.49                9834.74
node-292.domain.tld           0.41                9837.60
node-298.domain.tld           0.60                9835.58
node-301.domain.tld           0.95                9367.67
node-306.domain.tld           0.57                9837.65
node-309.domain.tld           0.94                9453.63
node-313.domain.tld           0.47                9836.65
node-315.domain.tld           0.52                9748.08
node-317.domain.tld           0.57                9832.31
node-337.domain.tld           1.44                8227.76
node-343.domain.tld           0.99                8893.12
node-349.domain.tld           0.53                9836.82
node-356.domain.tld           0.45                9836.97
node-359.domain.tld           1.24                9144.30
node-368.domain.tld           0.50                7065.35
node-376.domain.tld           0.47                9827.17
node-390.domain.tld           1.22                8170.48
node-391.domain.tld           1.17                8117.60
node-402.domain.tld           0.41                9839.32
node-424.domain.tld           1.23                8788.81
node-432.domain.tld           0.47                9836.56
node-449.domain.tld           0.55                9836.16
node-450.domain.tld           0.39                5242.63
node-451.domain.tld           1.04                9286.44
node-455.domain.tld           0.58                5912.64
node-459.domain.tld           1.32                8423.13
node-460.domain.tld           0.42                9839.87
node-465.domain.tld           0.49                6813.07
node-466.domain.tld           0.51                9825.39
node-467.domain.tld           0.46                6730.79
node-469.domain.tld           0.69                9823.38
node-470.domain.tld           0.64                9836.19
node-473.domain.tld           0.47                9829.55
node-475.domain.tld           0.40                9837.32
node-479.domain.tld           0.45                9759.44
node-481.domain.tld           0.63                9837.32
node-483.domain.tld           0.62                9739.01
node-484.domain.tld           0.58                9830.23
node-485.domain.tld           0.47                8272.38
node-486.domain.tld           0.33                6513.32
node-489.domain.tld           0.71                9830.54
node-490.domain.tld           0.40                9838.73
node-493.domain.tld           0.44                9787.61
node-501.domain.tld           0.54                9833.88
node-503.domain.tld           0.78                9809.38
node-505.domain.tld           0.83                9583.85
node-506.domain.tld           0.64                9824.27
node-507.domain.tld           0.57                5500.90
node-508.domain.tld           0.66                5629.01
node-511.domain.tld           0.51                9825.26
node-517.domain.tld           0.62                9807.62
node-519.domain.tld           0.71                9438.90
node-522.domain.tld           1.30                7558.53
node-60.domain.tld            0.72                9811.26
node-70.domain.tld            0.69                9832.05
node-83.domain.tld            0.45                9811.61
node-84.domain.tld            0.86                9828.10
node-96.domain.tld            0.45                5211.20
node-99.domain.tld            0.41                9718.99
===================  =============  =====================

Concurrency 185
---------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            1.35                8516.69
node-103.domain.tld           0.48                4005.80
node-104.domain.tld           1.68                6980.02
node-117.domain.tld           0.70                9827.14
node-121.domain.tld           0.55                6417.92
node-123.domain.tld           0.89                9836.77
node-126.domain.tld           1.39                7716.34
node-127.domain.tld           0.48                5214.30
node-131.domain.tld           1.08                8816.53
node-134.domain.tld           1.62                7053.96
node-136.domain.tld           0.62                5834.57
node-138.domain.tld           0.45                7337.85
node-139.domain.tld           1.30                9539.57
node-141.domain.tld           0.33                6735.84
node-142.domain.tld           0.48                7775.44
node-147.domain.tld           1.30                8119.73
node-149.domain.tld           0.60                4086.47
node-150.domain.tld           0.61                5369.15
node-153.domain.tld           0.59                6978.49
node-158.domain.tld           0.66                3976.53
node-162.domain.tld           0.49                6758.80
node-173.domain.tld           0.46                8444.66
node-175.domain.tld           0.48                7695.07
node-177.domain.tld           0.64                5541.19
node-180.domain.tld           0.52                9838.38
node-182.domain.tld           0.62                5987.04
node-185.domain.tld           0.55                9839.59
node-188.domain.tld           0.58                9837.10
node-192.domain.tld           0.62                9777.34
node-195.domain.tld           0.51                9839.00
node-199.domain.tld           0.61                9788.70
node-201.domain.tld           0.60                9839.57
node-202.domain.tld           0.38                9839.66
node-209.domain.tld           0.62                3765.23
node-211.domain.tld           0.64                3948.72
node-213.domain.tld           0.40                9838.99
node-214.domain.tld           0.60                9835.73
node-22.domain.tld            0.51                7141.61
node-224.domain.tld           0.38                6303.49
node-226.domain.tld           0.43                9829.97
node-228.domain.tld           0.58                9837.66
node-233.domain.tld           0.62                9825.73
node-236.domain.tld           0.61                3983.49
node-237.domain.tld           0.60                4178.08
node-241.domain.tld           0.55                9833.81
node-248.domain.tld           1.50                9830.54
node-254.domain.tld           0.58                6045.22
node-256.domain.tld           1.16                9166.57
node-259.domain.tld           0.61                9831.62
node-260.domain.tld           0.59                5276.34
node-262.domain.tld           0.65                5704.01
node-264.domain.tld           0.45                7796.76
node-266.domain.tld           0.55                9614.06
node-268.domain.tld           0.41                9839.97
node-271.domain.tld           0.57                4242.32
node-272.domain.tld           0.44                9834.27
node-275.domain.tld           0.45                9838.97
node-276.domain.tld           1.45                7669.38
node-283.domain.tld           1.17                8111.61
node-287.domain.tld           0.40                9839.52
node-291.domain.tld           0.47                9839.52
node-292.domain.tld           0.41                9836.44
node-298.domain.tld           0.67                9832.09
node-301.domain.tld           0.51                6880.65
node-303.domain.tld           0.62                9839.47
node-306.domain.tld           0.68                9835.11
node-309.domain.tld           0.58                3712.91
node-313.domain.tld           0.48                9834.37
node-315.domain.tld           0.38                3929.74
node-316.domain.tld           1.54                7315.10
node-317.domain.tld           0.62                7068.96
node-318.domain.tld           0.74                9834.27
node-321.domain.tld           0.60                7316.79
node-323.domain.tld           0.82                9650.40
node-324.domain.tld           0.39                9834.10
node-328.domain.tld           0.72                9837.21
node-336.domain.tld           0.44                9835.74
node-337.domain.tld           1.00                9169.30
node-339.domain.tld           0.45                9839.02
node-340.domain.tld           0.42                9839.47
node-342.domain.tld           0.50                3895.47
node-343.domain.tld           1.34                8135.19
node-345.domain.tld           0.41                9836.22
node-349.domain.tld           0.41                9837.37
node-350.domain.tld           0.95                9644.86
node-354.domain.tld           0.47                9836.36
node-356.domain.tld           0.42                9836.59
node-358.domain.tld           0.44                5181.84
node-359.domain.tld           0.73                9831.31
node-360.domain.tld           1.17                8148.65
node-362.domain.tld           0.39                7814.16
node-363.domain.tld           0.63                4475.70
node-364.domain.tld           0.44                7113.02
node-365.domain.tld           1.33                8198.22
node-368.domain.tld           0.51                7214.30
node-369.domain.tld           1.06                9068.16
node-372.domain.tld           0.62                4108.46
node-374.domain.tld           3.48                4017.07
node-376.domain.tld           0.64                7609.62
node-377.domain.tld           0.39                4183.57
node-378.domain.tld           0.66                7817.73
node-382.domain.tld           0.41                9839.38
node-385.domain.tld           0.46                6321.27
node-386.domain.tld           0.84                9779.41
node-390.domain.tld           1.44                7800.60
node-391.domain.tld           1.24                8217.63
node-396.domain.tld           0.86                9720.70
node-397.domain.tld           0.48                2625.12
node-40.domain.tld            0.96                9739.85
node-402.domain.tld           0.41                9839.64
node-405.domain.tld           0.46                9320.06
node-406.domain.tld           0.44                9834.37
node-407.domain.tld           0.58                2972.29
node-414.domain.tld           0.47                9833.53
node-418.domain.tld           1.31                8455.09
node-419.domain.tld           1.50                7336.27
node-420.domain.tld           0.78                9791.62
node-424.domain.tld           1.24                8309.88
node-429.domain.tld           0.65                7133.78
node-43.domain.tld            0.99                8902.09
node-431.domain.tld           0.62                3803.29
node-432.domain.tld           1.26                8089.79
node-433.domain.tld           0.52                7751.60
node-437.domain.tld           0.69                9836.95
node-439.domain.tld           0.45                9382.55
node-44.domain.tld            1.35                8139.42
node-440.domain.tld           0.60                9836.88
node-445.domain.tld           0.70                9792.53
node-449.domain.tld           1.13                8222.14
node-450.domain.tld           0.41                5330.90
node-451.domain.tld           1.37                7869.75
node-455.domain.tld           0.50                7218.55
node-456.domain.tld           0.44                6628.73
node-459.domain.tld           0.68                3721.89
node-460.domain.tld           0.41                7881.53
node-465.domain.tld           0.61                3994.55
node-466.domain.tld           0.47                9839.27
node-467.domain.tld           0.58                4158.11
node-469.domain.tld           1.93                6753.99
node-47.domain.tld            0.53                8578.68
node-470.domain.tld           0.64                9809.97
node-472.domain.tld           0.77                9827.16
node-473.domain.tld           0.58                6781.95
node-475.domain.tld           0.43                8102.89
node-479.domain.tld           0.35                9321.91
node-48.domain.tld            1.29                8086.63
node-481.domain.tld           0.47                6793.63
node-482.domain.tld           0.63                9837.50
node-483.domain.tld           0.50                4123.88
node-484.domain.tld           0.44                9834.57
node-485.domain.tld           0.47                4941.81
node-486.domain.tld           0.49                7078.77
node-488.domain.tld           0.63                4310.95
node-489.domain.tld           0.71                4359.13
node-490.domain.tld           0.40                9838.24
node-493.domain.tld           0.40                3867.39
node-496.domain.tld           0.47                2699.20
node-498.domain.tld           0.49                5342.83
node-501.domain.tld           0.51                6833.76
node-503.domain.tld           0.56                5265.84
node-505.domain.tld           0.40                6139.03
node-506.domain.tld           0.53                9830.50
node-507.domain.tld           0.46                6906.99
node-508.domain.tld           0.66                5728.86
node-51.domain.tld            1.53                7612.73
node-511.domain.tld           0.57                9833.89
node-517.domain.tld           0.51                9834.37
node-519.domain.tld           0.36                8992.93
node-522.domain.tld           0.49                6172.99
node-53.domain.tld            0.68                8574.63
node-54.domain.tld            0.70                6208.53
node-57.domain.tld            0.70                7018.02
node-59.domain.tld            0.73                9827.07
node-60.domain.tld            0.40                8037.23
node-61.domain.tld            0.64                9837.89
node-63.domain.tld            0.36                7015.77
node-64.domain.tld            1.32                8613.60
node-69.domain.tld            0.94                9393.52
node-70.domain.tld            1.30                8030.08
node-71.domain.tld            0.81                7433.92
node-76.domain.tld            0.33                6586.56
node-83.domain.tld            0.50                9825.94
node-84.domain.tld            0.74                6648.85
node-96.domain.tld            0.61                6232.01
node-99.domain.tld            0.62                9838.02
===================  =============  =====================

Upload
======

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_upload
    title: Upload

.. image:: 296ad9f9-22d5-4974-b662-fff6cf57f989.*

**Stats**:

===========  =============  ===================
concurrency  ping_icmp, ms  tcp_upload, Mbits/s
===========  =============  ===================
          1           0.45              9837.88
          2           0.45              9838.32
          5           0.49              9833.13
         11           0.57              9692.34
         23           0.74              9488.95
         46           0.79              9452.69
         92           0.83              8913.08
        185           0.78              7987.85
===========  =============  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-241.domain.tld           0.45              9837.88
===================  =============  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-192.domain.tld           0.48              9837.99
node-241.domain.tld           0.42              9838.65
===================  =============  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-192.domain.tld           0.44              9817.92
node-195.domain.tld           0.65              9838.20
node-211.domain.tld           0.47              9831.95
node-224.domain.tld           0.41              9839.65
node-241.domain.tld           0.46              9837.91
===================  =============  ===================

Concurrency 11
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-149.domain.tld           0.43              9840.45
node-192.domain.tld           0.63              9837.79
node-195.domain.tld           0.62              9831.45
node-199.domain.tld           0.44              9838.36
node-209.domain.tld           0.38              9839.46
node-211.domain.tld           0.42              9839.59
node-213.domain.tld           0.51              9840.59
node-214.domain.tld           0.45              9839.39
node-224.domain.tld           0.46              9839.58
node-241.domain.tld           0.52              9833.79
node-391.domain.tld           1.44              8235.33
===================  =============  ===================

Concurrency 23
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            0.58              9830.48
node-104.domain.tld           1.56              8017.32
node-149.domain.tld           0.45              9839.27
node-192.domain.tld           0.42              9835.47
node-195.domain.tld           0.47              9838.40
node-199.domain.tld           0.45              9840.51
node-209.domain.tld           0.39              9839.91
node-211.domain.tld           0.45              9838.74
node-213.domain.tld           0.50              9836.81
node-214.domain.tld           0.45              9837.43
node-224.domain.tld           0.38              9837.10
node-241.domain.tld           0.61              9819.02
node-262.domain.tld           0.50              9834.56
node-337.domain.tld           1.29              9019.53
node-390.domain.tld           1.28              7882.32
node-391.domain.tld           1.56              7816.92
node-432.domain.tld           0.53              9838.57
node-449.domain.tld           1.51              8459.77
node-475.domain.tld           0.46              9840.51
node-481.domain.tld           0.49              9832.85
node-517.domain.tld           0.53              9839.48
node-60.domain.tld            0.76              9833.75
node-70.domain.tld            1.40              9837.04
===================  =============  ===================

Concurrency 46
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            1.59              7747.56
node-104.domain.tld           1.29              8911.03
node-123.domain.tld           1.36              9763.93
node-149.domain.tld           0.48              9838.84
node-192.domain.tld           0.41              9836.32
node-195.domain.tld           0.47              9833.61
node-199.domain.tld           0.44              9840.38
node-209.domain.tld           0.38              9837.21
node-211.domain.tld           0.52              9730.26
node-213.domain.tld           0.46              9839.59
node-214.domain.tld           0.45              9838.12
node-224.domain.tld           0.42              9839.75
node-241.domain.tld           1.02              9138.02
node-262.domain.tld           0.54              9836.16
node-276.domain.tld           1.29              8640.90
node-283.domain.tld           1.90              6411.27
node-337.domain.tld           1.24              8701.58
node-349.domain.tld           0.48              9839.58
node-356.domain.tld           0.47              9825.64
node-368.domain.tld           0.52              9838.15
node-376.domain.tld           0.49              9839.97
node-390.domain.tld           1.30              8690.74
node-391.domain.tld           1.35              8502.89
node-402.domain.tld           0.47              9834.96
node-432.domain.tld           0.85              9606.52
node-449.domain.tld           1.41              8690.84
node-460.domain.tld           0.50              9837.79
node-470.domain.tld           0.57              9837.89
node-473.domain.tld           0.50              9838.90
node-475.domain.tld           0.48              9837.54
node-479.domain.tld           0.61              9809.47
node-481.domain.tld           0.47              9839.55
node-483.domain.tld           0.79              9742.72
node-484.domain.tld           0.51              9839.03
node-486.domain.tld           0.49              9794.22
node-493.domain.tld           1.47              9833.51
node-501.domain.tld           0.60              9772.19
node-505.domain.tld           0.58              9829.26
node-506.domain.tld           0.50              9833.98
node-511.domain.tld           0.57              9831.07
node-517.domain.tld           1.38              8774.13
node-519.domain.tld           0.64              9752.04
node-60.domain.tld            1.76              7162.55
node-70.domain.tld            1.42              9838.76
node-83.domain.tld            0.45              9792.26
node-84.domain.tld            0.47              9773.01
===================  =============  ===================

Concurrency 92
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            0.57              9828.85
node-103.domain.tld           0.60              9839.15
node-104.domain.tld           1.54              7937.54
node-121.domain.tld           0.96              9840.37
node-123.domain.tld           0.98              4300.12
node-127.domain.tld           0.68              7111.37
node-142.domain.tld           0.38              7462.98
node-149.domain.tld           0.45              9836.22
node-162.domain.tld           0.67              9797.99
node-173.domain.tld           0.78              9741.96
node-175.domain.tld           1.02              9524.97
node-177.domain.tld           0.53              9840.23
node-180.domain.tld           0.63              9821.84
node-182.domain.tld           0.48              9838.44
node-185.domain.tld           0.64              9838.93
node-188.domain.tld           0.58              4840.28
node-192.domain.tld           0.51              7422.90
node-195.domain.tld           0.81              9837.79
node-199.domain.tld           0.57              9840.48
node-209.domain.tld           0.65              9794.68
node-211.domain.tld           0.57              9840.38
node-213.domain.tld           0.49              9838.40
node-214.domain.tld           0.61              9838.29
node-224.domain.tld           0.41              9840.31
node-226.domain.tld           0.49              9839.26
node-228.domain.tld           0.43              9818.79
node-241.domain.tld           0.49              9835.22
node-248.domain.tld           0.47              9839.48
node-254.domain.tld           0.49              7602.29
node-260.domain.tld           1.25              8698.35
node-262.domain.tld           0.56              9824.55
node-276.domain.tld           1.32              8228.36
node-283.domain.tld           1.39              8201.67
node-291.domain.tld           0.55              9804.76
node-292.domain.tld           0.48              9821.57
node-298.domain.tld           0.60              9809.21
node-301.domain.tld           1.84              7120.09
node-306.domain.tld           1.83              6947.38
node-309.domain.tld           1.45              9049.83
node-313.domain.tld           0.51              9840.44
node-315.domain.tld           0.50              9834.35
node-317.domain.tld           0.43              9441.15
node-337.domain.tld           1.25              8869.57
node-343.domain.tld           1.29              8659.46
node-349.domain.tld           0.49              9840.05
node-356.domain.tld           0.41              9838.02
node-359.domain.tld           1.61              7274.26
node-368.domain.tld           0.65              9725.33
node-376.domain.tld           0.48              9840.15
node-390.domain.tld           1.39              8603.87
node-391.domain.tld           1.47              7952.52
node-402.domain.tld           0.39              9840.05
node-424.domain.tld           1.53              7651.39
node-432.domain.tld           1.34              8658.34
node-449.domain.tld           1.67              7502.06
node-450.domain.tld           0.72              9813.99
node-451.domain.tld           1.81              7044.94
node-455.domain.tld           0.77              9690.79
node-459.domain.tld           5.46              2567.62
node-460.domain.tld           0.40              9790.66
node-465.domain.tld           0.53              9839.61
node-466.domain.tld           0.46              9837.28
node-467.domain.tld           0.46              9837.50
node-469.domain.tld           0.70              9835.51
node-470.domain.tld           0.52              6651.37
node-473.domain.tld           0.47              9839.02
node-475.domain.tld           0.65              9832.25
node-479.domain.tld           0.64              9832.62
node-481.domain.tld           0.43              7556.53
node-483.domain.tld           0.79              5522.63
node-484.domain.tld           0.54              9836.25
node-485.domain.tld           0.47              9819.84
node-486.domain.tld           0.34              6584.91
node-489.domain.tld           0.43              9838.67
node-490.domain.tld           0.50              9820.67
node-493.domain.tld           0.55              9830.68
node-501.domain.tld           0.34              7046.39
node-503.domain.tld           0.44              9839.76
node-505.domain.tld           0.59              9822.70
node-506.domain.tld           0.57              9837.00
node-507.domain.tld           0.72              9825.07
node-508.domain.tld           0.79              9618.42
node-511.domain.tld           0.46              9839.10
node-517.domain.tld           0.62              9828.25
node-519.domain.tld           0.40              6760.53
node-522.domain.tld           2.99              5798.53
node-60.domain.tld            1.62              7646.33
node-70.domain.tld            1.55              8223.70
node-83.domain.tld            0.50              9839.67
node-84.domain.tld            0.70              9832.87
node-96.domain.tld            0.55              9716.26
node-99.domain.tld            0.54              9838.77
===================  =============  ===================

Concurrency 185
---------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            0.54              9839.34
node-103.domain.tld           0.62              9828.74
node-104.domain.tld           1.60              7801.65
node-117.domain.tld           0.79              7737.47
node-121.domain.tld           0.61              6621.75
node-123.domain.tld           0.53              8324.07
node-126.domain.tld           1.76              7219.96
node-127.domain.tld           0.68              9684.55
node-131.domain.tld           1.42              8327.28
node-134.domain.tld           1.21              9036.81
node-136.domain.tld           0.54              7955.72
node-138.domain.tld           0.71              4094.88
node-139.domain.tld           0.37              7398.33
node-141.domain.tld           0.43              7363.56
node-142.domain.tld           0.65              4363.36
node-147.domain.tld           1.59              7230.65
node-149.domain.tld           0.41              4374.65
node-150.domain.tld           1.28              2120.77
node-153.domain.tld           0.56              5348.45
node-158.domain.tld           0.65              9514.46
node-162.domain.tld           0.64              6165.04
node-173.domain.tld           0.64              4940.32
node-175.domain.tld           0.63              4936.72
node-177.domain.tld           0.50              7592.07
node-180.domain.tld           0.69              9838.49
node-182.domain.tld           0.51              7183.68
node-185.domain.tld           0.67              7730.67
node-188.domain.tld           0.63              4337.96
node-192.domain.tld           0.64              7469.35
node-195.domain.tld           0.46              9836.48
node-199.domain.tld           0.47              9837.77
node-201.domain.tld           0.60              9045.68
node-202.domain.tld           0.50              9838.98
node-209.domain.tld           0.40              7877.09
node-211.domain.tld           0.47              3421.72
node-213.domain.tld           0.47              9836.97
node-214.domain.tld           0.82              9798.76
node-22.domain.tld            0.31              5165.48
node-224.domain.tld           0.57              9688.48
node-226.domain.tld           0.45              9834.82
node-228.domain.tld           0.44              8500.31
node-233.domain.tld           0.52              8885.65
node-236.domain.tld           0.69              6855.66
node-237.domain.tld           0.74              9795.37
node-241.domain.tld           0.48              9834.46
node-248.domain.tld           0.61              4414.33
node-254.domain.tld           0.66              7732.07
node-256.domain.tld           1.28              8959.34
node-259.domain.tld           1.46              7936.07
node-260.domain.tld           0.43              4917.78
node-262.domain.tld           0.72              6248.86
node-264.domain.tld           0.44              4168.05
node-266.domain.tld           0.70              9159.53
node-268.domain.tld           1.35              9840.50
node-271.domain.tld           0.46              6902.72
node-272.domain.tld           0.54              9837.16
node-275.domain.tld           0.42              9840.37
node-276.domain.tld           1.26              8995.47
node-283.domain.tld           1.48              8246.03
node-287.domain.tld           0.43              9838.33
node-291.domain.tld           0.60              9825.97
node-292.domain.tld           0.47              9834.94
node-298.domain.tld           0.61              6760.10
node-301.domain.tld           0.64              9834.16
node-303.domain.tld           0.70              9829.58
node-306.domain.tld           2.26              9738.90
node-309.domain.tld           0.86              7626.57
node-313.domain.tld           0.45              9839.43
node-315.domain.tld           0.49              5718.58
node-316.domain.tld           1.28              8818.07
node-317.domain.tld           0.58              6748.51
node-318.domain.tld           0.81              9533.56
node-321.domain.tld           0.86              9828.03
node-323.domain.tld           0.70              9819.60
node-324.domain.tld           0.48              9836.61
node-328.domain.tld           0.46              6553.82
node-336.domain.tld           0.45              9834.32
node-337.domain.tld           1.84              6846.51
node-339.domain.tld           0.47              7084.33
node-340.domain.tld           0.42              9838.27
node-342.domain.tld           0.48              9840.32
node-343.domain.tld           0.76              9814.99
node-345.domain.tld           0.46              9838.28
node-349.domain.tld           1.32              8511.60
node-350.domain.tld           0.59              9816.01
node-354.domain.tld           0.51              9838.07
node-356.domain.tld           0.55              9832.99
node-358.domain.tld           0.72              5003.24
node-359.domain.tld           1.61              8276.35
node-360.domain.tld           1.52              7966.42
node-362.domain.tld           0.44              7252.46
node-363.domain.tld           0.65              4455.22
node-364.domain.tld           0.49              6607.82
node-365.domain.tld           0.68              9831.52
node-368.domain.tld           0.50              5216.47
node-369.domain.tld           1.60              7728.40
node-372.domain.tld           0.57              6311.60
node-374.domain.tld           0.81              3439.84
node-376.domain.tld           0.67              4381.37
node-377.domain.tld           0.58              5827.00
node-378.domain.tld           0.67              6947.66
node-382.domain.tld           1.17              9109.60
node-385.domain.tld           0.59              8841.08
node-386.domain.tld           0.84              6796.82
node-390.domain.tld           1.41              8316.41
node-391.domain.tld           1.39              8391.28
node-396.domain.tld           0.69              9778.50
node-397.domain.tld           0.62              6694.48
node-40.domain.tld            1.50              8065.08
node-402.domain.tld           0.44              9840.88
node-405.domain.tld           0.61              9836.57
node-406.domain.tld           0.42              9838.93
node-407.domain.tld           0.53              8458.08
node-414.domain.tld           0.45              9835.97
node-418.domain.tld           1.69              7132.99
node-419.domain.tld           1.18              9095.00
node-420.domain.tld           0.31              6960.58
node-424.domain.tld           1.51              7936.16
node-429.domain.tld           0.32              6099.40
node-43.domain.tld            0.65              9811.76
node-431.domain.tld           0.64              4481.53
node-432.domain.tld           0.87              9592.19
node-433.domain.tld           0.73              9839.76
node-437.domain.tld           0.51              9816.23
node-439.domain.tld           0.66              7268.11
node-44.domain.tld            1.58              7810.43
node-440.domain.tld           0.46              8621.55
node-445.domain.tld           0.72              9839.12
node-449.domain.tld           1.55              7433.86
node-450.domain.tld           0.58              7347.09
node-451.domain.tld           1.32              8859.11
node-455.domain.tld           0.61              4899.80
node-456.domain.tld           2.06              9836.55
node-459.domain.tld           1.22              4042.81
node-460.domain.tld           0.63              8144.80
node-465.domain.tld           0.35              7570.59
node-466.domain.tld           0.54              9827.63
node-467.domain.tld           0.42              7617.90
node-469.domain.tld           0.44              5737.06
node-47.domain.tld            1.19              9125.70
node-470.domain.tld           0.62              6184.18
node-472.domain.tld           0.56              9835.35
node-473.domain.tld           0.76              9840.08
node-475.domain.tld           0.74              9839.77
node-479.domain.tld           0.89              7728.77
node-48.domain.tld            0.62              9836.71
node-481.domain.tld           0.53              6079.57
node-482.domain.tld           0.80              9696.84
node-483.domain.tld           0.53              9835.96
node-484.domain.tld           0.47              9831.53
node-485.domain.tld           0.94              9744.39
node-486.domain.tld           0.73              6230.93
node-488.domain.tld           0.42              3543.22
node-489.domain.tld           0.69              9813.57
node-490.domain.tld           0.46              9833.57
node-493.domain.tld           0.91              9826.61
node-496.domain.tld           0.83              9818.02
node-498.domain.tld           0.48              8911.72
node-501.domain.tld           0.77              5884.07
node-503.domain.tld           0.35              4480.67
node-505.domain.tld           1.17              9749.55
node-506.domain.tld           0.63              9836.04
node-507.domain.tld           0.64              5505.26
node-508.domain.tld           0.66              9839.70
node-51.domain.tld            1.53              7985.91
node-511.domain.tld           0.59              9828.95
node-517.domain.tld           1.26              8613.80
node-519.domain.tld           0.92              7711.48
node-522.domain.tld           0.48              5958.20
node-53.domain.tld            0.66              9808.04
node-54.domain.tld            0.44              9838.02
node-57.domain.tld            0.35              9012.14
node-59.domain.tld            1.75              7575.98
node-60.domain.tld            1.26              8552.54
node-61.domain.tld            0.83              6094.16
node-63.domain.tld            1.67              7804.34
node-64.domain.tld            0.51              5013.23
node-69.domain.tld            0.63              9809.55
node-70.domain.tld            1.39              9813.35
node-71.domain.tld            1.27              8321.95
node-76.domain.tld            2.66              8744.11
node-83.domain.tld            0.71              3871.70
node-84.domain.tld            0.54              9833.32
node-96.domain.tld            0.67              7168.18
node-99.domain.tld            0.62              6157.10
===================  =============  ===================

