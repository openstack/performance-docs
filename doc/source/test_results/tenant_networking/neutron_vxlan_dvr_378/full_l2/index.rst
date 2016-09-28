.. _openstack_l2:

OpenStack L2 Full
*****************

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
    file_name: shaker/shaker/scenarios/openstack/full_l2.yaml
    title: OpenStack L2

Bi-directional
==============

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_bidirectional
    title: Bi-directional

.. image:: fbbe3f55-12f3-4e9a-ac2a-d28daae3451b.*

**Stats**:

===========  =============  =====================  ===================
concurrency  ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===========  =============  =====================  ===================
          1           1.46                7479.58              7944.63
          2           1.73                6790.19              6918.99
          5           1.59                7097.44              7268.58
         11           1.68                7000.33              7006.15
         23           1.69                6855.75              6521.45
         46           1.74                6638.69              6595.22
         92           1.31                6281.66              6061.87
        185           1.13                4868.10              5068.92
===========  =============  =====================  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-228.domain.tld           1.46                7479.58              7944.63
===================  =============  =====================  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-188.domain.tld           1.76                6749.34              6837.78
node-228.domain.tld           1.71                6831.04              7000.20
===================  =============  =====================  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-173.domain.tld           1.68                6797.87              6877.63
node-175.domain.tld           1.56                6985.78              6999.42
node-177.domain.tld           1.56                7238.25              7453.24
node-188.domain.tld           1.68                6834.26              6952.56
node-228.domain.tld           1.48                7631.04              8060.04
===================  =============  =====================  ===================

Concurrency 11
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-173.domain.tld           1.55                7823.58              8257.63
node-175.domain.tld           1.55                7731.82              7502.64
node-177.domain.tld           1.51                7626.03              7381.82
node-180.domain.tld           1.71                7524.49              7420.09
node-182.domain.tld           1.71                6477.69              6541.88
node-185.domain.tld           1.76                6560.40              6578.21
node-188.domain.tld           1.68                6692.63              6724.67
node-228.domain.tld           1.91                6054.56              6344.92
node-248.domain.tld           1.66                6715.31              6552.30
node-254.domain.tld           1.88                6531.69              6356.44
node-61.domain.tld            1.52                7265.39              7407.08
===================  =============  =====================  ===================

Concurrency 23
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            1.81                6251.53              5457.05
node-104.domain.tld           2.23                5114.00              5204.83
node-173.domain.tld           1.01                8058.90              5772.72
node-175.domain.tld           1.87                8574.30              6119.13
node-177.domain.tld           1.50                6956.01              7297.78
node-180.domain.tld           1.69                6902.23              6807.91
node-182.domain.tld           1.61                6546.72              6612.81
node-185.domain.tld           1.52                7636.57              7723.47
node-188.domain.tld           1.27                5545.17              7616.71
node-228.domain.tld           1.75                6683.13              6740.87
node-248.domain.tld           1.45                8137.27              5511.47
node-254.domain.tld           1.75                6719.28              7052.35
node-262.domain.tld           1.51                6813.13              6909.23
node-377.domain.tld           1.76                6426.84              6441.72
node-460.domain.tld           1.65                7577.07              7549.02
node-473.domain.tld           1.34                8016.68              8409.88
node-475.domain.tld           1.79                6801.44              6665.50
node-481.domain.tld           1.13                9308.49              6873.02
node-511.domain.tld           1.70                6954.48              6874.42
node-517.domain.tld           1.55                6606.89              6734.16
node-60.domain.tld            2.59                4764.86              4687.58
node-61.domain.tld            1.74                6868.63              6477.01
node-70.domain.tld            2.58                4418.67              4454.73
===================  =============  =====================  ===================

Concurrency 46
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            2.08                5654.19              5153.74
node-104.domain.tld           2.37                4711.48              4643.65
node-173.domain.tld           1.28                5850.43              8571.24
node-175.domain.tld           1.66                6705.22              6870.94
node-177.domain.tld           1.34                6605.60              8313.82
node-180.domain.tld           1.65                6793.09              6909.96
node-182.domain.tld           1.18                6550.44              8765.56
node-185.domain.tld           1.66                7567.46              6328.58
node-188.domain.tld           1.32                8557.21              5647.08
node-228.domain.tld           1.44                6769.07              8037.07
node-248.domain.tld           2.07                6269.90              6018.47
node-254.domain.tld           1.58                6246.06              6968.21
node-260.domain.tld           1.81                6602.60              6688.31
node-262.domain.tld           1.68                6787.03              6905.07
node-276.domain.tld           2.35                4633.40              4556.74
node-283.domain.tld           2.44                4673.68              4613.53
node-301.domain.tld           1.89                6171.08              6239.05
node-306.domain.tld           2.22                4894.27              5586.15
node-343.domain.tld           2.38                5394.16              4876.00
node-349.domain.tld           2.07                5736.07              5078.53
node-350.domain.tld           1.98                7002.07              6468.44
node-354.domain.tld           1.39                7814.85              7880.38
node-359.domain.tld           2.60                4504.72              4523.91
node-362.domain.tld           1.79                7214.76              7221.33
node-363.domain.tld           1.40                8495.01              5733.77
node-364.domain.tld           1.67                7179.62              7275.68
node-372.domain.tld           1.52                8172.89              7981.41
node-377.domain.tld           1.71                6719.20              6945.85
node-382.domain.tld           1.47                7581.62              7674.07
node-385.domain.tld           1.35                6769.91              8257.10
node-386.domain.tld           1.77                6077.65              6464.57
node-407.domain.tld           1.34                8468.39              7238.68
node-420.domain.tld           1.41                7814.16              7656.19
node-424.domain.tld           2.33                4742.73              4765.62
node-429.domain.tld           1.45                6441.37              8239.67
node-451.domain.tld           2.23                4859.95              4820.92
node-460.domain.tld           1.67                7041.44              6996.18
node-473.domain.tld           1.32                8206.35              7349.06
node-475.domain.tld           1.61                6957.07              7061.22
node-481.domain.tld           1.35                8424.98              8231.09
node-496.domain.tld           1.66                6548.48              6644.30
node-511.domain.tld           1.60                7110.58              7209.76
node-517.domain.tld           1.50                7587.71              7260.02
node-60.domain.tld            2.23                4825.96              5257.60
node-61.domain.tld            1.23                9166.29              5163.13
node-70.domain.tld            1.82                6479.61              6288.63
===================  =============  =====================  ===================

Concurrency 92
--------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            1.57                7100.33              6786.78
node-104.domain.tld           2.45                4431.05              4255.62
node-141.domain.tld           1.67                6827.50              6551.89
node-147.domain.tld           2.07                5159.79              5132.74
node-149.domain.tld           0.57                5566.06              4103.81
node-150.domain.tld           0.45                4374.60              4611.52
node-153.domain.tld           0.70                4031.79              8211.36
node-158.domain.tld           0.49                5151.46              5379.21
node-173.domain.tld           0.63                7011.48              5466.52
node-175.domain.tld           0.61                6517.61              6184.61
node-177.domain.tld           0.75                6824.64              6678.69
node-180.domain.tld           1.58                7060.21              6921.36
node-182.domain.tld           0.73                4742.09              7981.62
node-185.domain.tld           1.30                9579.09              3416.01
node-188.domain.tld           0.59                6702.06              5658.17
node-192.domain.tld           0.70                7352.05              6534.80
node-195.domain.tld           1.47                7545.31              7831.58
node-199.domain.tld           0.96                5003.92              9722.62
node-202.domain.tld           1.42                7786.88              7625.12
node-209.domain.tld           0.71                5298.42              7575.91
node-211.domain.tld           2.20                6027.33              1970.69
node-213.domain.tld           1.42                6984.71              7051.73
node-214.domain.tld           0.46                7530.85              4325.51
node-224.domain.tld           0.54                5546.90              5395.41
node-228.domain.tld           0.67                5341.41              4342.25
node-233.domain.tld           0.89                9579.78              2243.24
node-236.domain.tld           0.36                5565.68              4938.01
node-237.domain.tld           1.02                2575.09              9719.48
node-241.domain.tld           1.74                6916.22              6776.30
node-248.domain.tld           0.75                4215.08              7572.26
node-254.domain.tld           1.21                9698.31              2915.09
node-260.domain.tld           2.16                5759.26              5940.77
node-262.domain.tld           0.44                7534.41              3668.10
node-266.domain.tld           1.13                9601.94              2252.18
node-276.domain.tld           2.59                4219.50              4140.23
node-283.domain.tld           2.11                5297.74              5142.19
node-287.domain.tld           1.69                7108.82              7034.54
node-301.domain.tld           2.29                4723.60              4728.09
node-306.domain.tld           1.97                6531.30              6548.43
node-324.domain.tld           1.24                8204.00              8157.27
node-328.domain.tld           0.87                2708.21              9777.89
node-340.domain.tld           1.46                8208.49              7955.19
node-342.domain.tld           1.25                5204.09              9277.04
node-343.domain.tld           2.48                4622.36              4538.05
node-349.domain.tld           1.58                5964.99              7919.99
node-350.domain.tld           2.04                6403.67              6144.06
node-354.domain.tld           1.36                7932.43              7949.85
node-356.domain.tld           1.61                7187.55              7282.74
node-359.domain.tld           1.83                4763.05              5613.24
node-362.domain.tld           0.93                9601.83              3945.51
node-363.domain.tld           0.64                5182.54              6599.37
node-364.domain.tld           0.70                4619.06              8332.99
node-368.domain.tld           0.88                3848.30              9811.42
node-372.domain.tld           1.33                5223.55              7763.90
node-374.domain.tld           0.58                4687.94              5375.08
node-376.domain.tld           0.93                9811.71              2447.93
node-377.domain.tld           1.29                6327.47              6638.94
node-378.domain.tld           0.99                6158.54              5658.34
node-382.domain.tld           1.71                6904.65              7160.02
node-385.domain.tld           0.84                3036.52              9534.81
node-386.domain.tld           1.21                8506.09              3614.86
node-396.domain.tld           1.75                7131.21              6698.63
node-397.domain.tld           1.43                2437.45              8948.56
node-40.domain.tld            2.31                5354.77              4486.58
node-402.domain.tld           1.73                6632.01              6544.29
node-405.domain.tld           0.47                4807.02              4771.63
node-406.domain.tld           1.81                7029.38              6720.07
node-407.domain.tld           0.71                9624.84              3659.27
node-414.domain.tld           1.53                6831.42              6820.96
node-420.domain.tld           0.65                9778.77              3638.17
node-424.domain.tld           2.13                5192.08              5349.68
node-429.domain.tld           0.79                9803.73              3531.56
node-43.domain.tld            1.79                4840.99              6156.82
node-44.domain.tld            1.67                6853.16              6654.97
node-451.domain.tld           2.28                5318.62              5230.05
node-460.domain.tld           1.11                3518.16              8564.03
node-47.domain.tld            2.36                4892.60              5375.03
node-473.domain.tld           0.64                3599.09              9485.48
node-475.domain.tld           0.43                5608.91              4345.27
node-48.domain.tld            1.60                6639.21              4912.76
node-481.domain.tld           0.89                9733.14              4051.05
node-482.domain.tld           1.78                6687.10              6442.80
node-496.domain.tld           1.10                4344.37              9683.30
node-511.domain.tld           1.76                6651.04              7073.87
node-517.domain.tld           1.60                6892.79              6821.30
node-57.domain.tld            1.00                9341.13              3354.59
node-60.domain.tld            1.85                6435.71              6799.34
node-61.domain.tld            0.97                9750.62              3981.72
node-63.domain.tld            2.24                5085.63              5011.31
node-64.domain.tld            1.72                6431.02              6250.19
node-70.domain.tld            2.38                3961.22              4850.19
node-76.domain.tld            1.59                6774.08              6645.42
===================  =============  =====================  ===================

Concurrency 185
---------------

**Stats**:

===================  =============  =====================  ===================
node                 ping_icmp, ms  tcp_download, Mbits/s  tcp_upload, Mbits/s
===================  =============  =====================  ===================
node-10.domain.tld            1.28                3413.34              6922.29
node-103.domain.tld           0.63                3620.52              7159.17
node-104.domain.tld           2.40                4673.90              4689.40
node-117.domain.tld           0.71                7855.76              2650.99
node-121.domain.tld           0.58                3687.62              3637.40
node-123.domain.tld           0.61                5469.91              1647.23
node-126.domain.tld           2.08                4646.19              4728.11
node-127.domain.tld           0.72                2802.08              6084.78
node-131.domain.tld           2.41                4860.91              4533.52
node-134.domain.tld           2.48                4835.32              4639.45
node-136.domain.tld           0.60                3006.76              3890.99
node-138.domain.tld           0.99                4244.90              3009.64
node-139.domain.tld           1.71                6470.84              6541.54
node-141.domain.tld           1.67                7094.69              6888.21
node-142.domain.tld           0.68                5805.31              2822.77
node-147.domain.tld           2.04                5336.97              5201.47
node-149.domain.tld           0.54                3079.10              2848.58
node-150.domain.tld           0.65                3149.64              7553.54
node-153.domain.tld           0.49                3921.20              2724.41
node-158.domain.tld           0.57                3558.82              3926.47
node-162.domain.tld           0.61                2951.22              4743.57
node-173.domain.tld           0.60                3480.34              5146.84
node-175.domain.tld           0.52                3421.56              4290.33
node-177.domain.tld           0.74                3092.35              3735.70
node-180.domain.tld           1.62                7045.35              7016.79
node-182.domain.tld           0.69                2584.05              4290.80
node-185.domain.tld           0.57                4732.81              4271.65
node-188.domain.tld           0.64                4723.95              3270.23
node-192.domain.tld           0.58                6479.91              3242.92
node-195.domain.tld           1.46                7714.79              7843.23
node-199.domain.tld           0.59                3530.65              6554.90
node-201.domain.tld           0.53                7111.45              3312.70
node-202.domain.tld           1.54                7750.04              7528.39
node-209.domain.tld           0.51                3013.67              4052.28
node-211.domain.tld           0.59                2960.55              3302.89
node-213.domain.tld           1.61                7206.98              7018.87
node-214.domain.tld           0.49                4531.20              3064.92
node-22.domain.tld            1.94                2348.25              5929.57
node-224.domain.tld           0.49                2311.55              4770.46
node-226.domain.tld           1.62                7347.24              7060.70
node-228.domain.tld           0.53                2359.83              3878.13
node-233.domain.tld           0.51                4881.33              3054.06
node-236.domain.tld           0.66                3094.12              3069.88
node-237.domain.tld           0.70                3261.00              4084.75
node-241.domain.tld           1.40                8150.88              8057.64
node-248.domain.tld           0.57                3476.36              3696.77
node-254.domain.tld           0.52                3070.00              4228.83
node-256.domain.tld           2.29                5230.74              5204.46
node-259.domain.tld           1.87                6338.97              5901.98
node-260.domain.tld           0.66                2544.93              8530.98
node-262.domain.tld           0.48                3285.30              3188.25
node-264.domain.tld           0.69                4855.96              6818.05
node-266.domain.tld           0.47                3190.57              2823.67
node-268.domain.tld           1.67                7533.75              7641.16
node-271.domain.tld           0.53                3055.75              2928.54
node-272.domain.tld           1.73                6816.87              6645.80
node-275.domain.tld           1.79                6597.83              6717.74
node-276.domain.tld           2.64                4517.11              4481.98
node-283.domain.tld           2.39                4578.21              4428.87
node-287.domain.tld           1.67                7093.73              7008.60
node-291.domain.tld           1.64                6663.43              6445.59
node-292.domain.tld           1.64                6686.00              6819.47
node-298.domain.tld           0.56                3613.76              4697.77
node-301.domain.tld           1.29                1805.05              7327.86
node-303.domain.tld           0.67                2492.36              7753.39
node-306.domain.tld           0.92                9591.60              3039.95
node-309.domain.tld           0.84                3029.19              2225.41
node-313.domain.tld           1.53                7950.23              7840.37
node-315.domain.tld           0.57                2950.59              7879.06
node-316.domain.tld           2.44                4584.03              4695.12
node-317.domain.tld           0.47                2624.31              2558.23
node-318.domain.tld           1.16                9722.13              3013.57
node-321.domain.tld           0.52                6115.29              2924.24
node-323.domain.tld           0.55                4729.13              3211.18
node-324.domain.tld           1.53                7507.90              7432.85
node-328.domain.tld           0.44                2854.11              2827.59
node-336.domain.tld           1.66                7341.86              7211.63
node-337.domain.tld           2.20                4813.20              4877.48
node-339.domain.tld           0.58                6408.65              3711.03
node-340.domain.tld           1.55                7593.12              7636.73
node-342.domain.tld           0.63                2976.31              7567.19
node-343.domain.tld           1.82                6116.84              2611.02
node-345.domain.tld           1.61                7579.73              7472.77
node-349.domain.tld           2.18                5043.15              4934.48
node-350.domain.tld           1.76                6860.76              6356.60
node-354.domain.tld           1.46                7682.00              7321.12
node-356.domain.tld           1.77                7189.29              7453.74
node-358.domain.tld           0.56                2860.07              4905.24
node-359.domain.tld           1.84                6409.14              6520.24
node-360.domain.tld           2.19                5091.19              5157.87
node-362.domain.tld           0.59                2964.33              4484.29
node-363.domain.tld           0.58                2794.65              4088.75
node-364.domain.tld           0.52                2959.59              5039.99
node-365.domain.tld           2.05                6012.71              5471.66
node-368.domain.tld           0.56                3597.43              4519.81
node-369.domain.tld           2.56                4660.16              4783.31
node-372.domain.tld           0.51                3793.13              3092.03
node-374.domain.tld           0.68                5645.36              5957.32
node-376.domain.tld           0.60                5251.43              2979.17
node-377.domain.tld           0.46                3619.62              2725.64
node-378.domain.tld           0.59                3177.83              5690.48
node-382.domain.tld           1.58                7573.43              7849.68
node-385.domain.tld           0.60                7137.18              2619.33
node-386.domain.tld           0.58                4245.15              2537.51
node-390.domain.tld           2.34                4905.62              4867.03
node-391.domain.tld           2.42                4576.76              4610.38
node-396.domain.tld           1.72                7235.61              6679.08
node-397.domain.tld           0.74                2461.38              3357.65
node-40.domain.tld            1.94                5472.92              6155.92
node-402.domain.tld           1.85                6527.47              6712.26
node-405.domain.tld           0.52                2710.68              3643.63
node-406.domain.tld           1.88                6304.63              6155.31
node-407.domain.tld           0.57                3363.35              3649.45
node-414.domain.tld           1.58                6800.48              6827.58
node-418.domain.tld           1.93                5898.08              5625.75
node-419.domain.tld           2.52                4395.16              4344.36
node-420.domain.tld           0.53                4452.04              3556.43
node-424.domain.tld           2.34                4749.17              4865.69
node-429.domain.tld           0.54                4710.68              3390.31
node-43.domain.tld            1.72                6936.13              3812.44
node-431.domain.tld           0.64                3993.32              2741.25
node-432.domain.tld           2.20                5056.41              5285.74
node-433.domain.tld           0.62                7157.60              3799.13
node-437.domain.tld           1.36                7704.31              7540.56
node-439.domain.tld           0.56                5888.26              4010.16
node-44.domain.tld            1.00                4605.30              8265.01
node-440.domain.tld           0.88                6591.76              2755.47
node-445.domain.tld           0.65                4195.27              6332.93
node-449.domain.tld           1.66                4820.06              6031.76
node-450.domain.tld           0.64                3501.10              5308.62
node-451.domain.tld           2.39                4843.60              4680.01
node-455.domain.tld           0.60                3095.22              4356.35
node-456.domain.tld           0.89                2952.37              4602.72
node-459.domain.tld           0.52                2435.97              2338.25
node-460.domain.tld           0.61                6542.84              3832.03
node-465.domain.tld           0.64                3143.64              6235.62
node-466.domain.tld           1.80                7207.80              7171.55
node-467.domain.tld           0.50                3558.90              2550.56
node-469.domain.tld           0.52                6250.37              3779.60
node-47.domain.tld            1.13                4127.02              8756.52
node-470.domain.tld           0.77                3071.39              7878.57
node-472.domain.tld           0.94                8076.25              3527.42
node-473.domain.tld           0.56                3061.87              6060.48
node-475.domain.tld           0.58                2382.04              3666.84
node-479.domain.tld           0.86                3742.73              6113.73
node-48.domain.tld            1.55                4629.55              7598.89
node-481.domain.tld           0.61                6850.37              2975.81
node-482.domain.tld           0.87                5057.50              4201.82
node-483.domain.tld           0.69                3176.55              6174.97
node-484.domain.tld           1.68                6590.30              6707.75
node-485.domain.tld           0.65                1648.01              5278.99
node-486.domain.tld           0.72                3015.89              6001.27
node-488.domain.tld           0.54                3908.68              4147.96
node-489.domain.tld           0.71                3043.85              5385.23
node-490.domain.tld           1.58                7604.04              7352.52
node-493.domain.tld           0.69                3474.98              5140.86
node-496.domain.tld           0.66                3613.05              4909.25
node-498.domain.tld           0.58                3313.08              7362.91
node-501.domain.tld           0.80                3019.09              7473.65
node-503.domain.tld           0.51                2988.60              3184.74
node-505.domain.tld           0.68                2405.44              3713.55
node-506.domain.tld           1.71                6538.66              6530.20
node-507.domain.tld           0.59                3091.25              4602.38
node-508.domain.tld           0.51                2387.30              3464.05
node-51.domain.tld            2.18                4974.14              5152.83
node-511.domain.tld           1.60                7077.97              6809.52
node-517.domain.tld           2.12                5624.07              5082.41
node-519.domain.tld           0.83                3438.90              7806.16
node-522.domain.tld           1.10                3020.01              3834.46
node-53.domain.tld            1.75                4146.69              7600.10
node-54.domain.tld            0.98                2725.94              9429.52
node-57.domain.tld            0.88                9215.84              3328.95
node-59.domain.tld            1.31                1926.59              7497.09
node-60.domain.tld            1.07                3756.77              6329.08
node-61.domain.tld            0.64                6020.62              2790.75
node-63.domain.tld            1.66                2160.29              6809.74
node-64.domain.tld            1.82                3851.91              6995.89
node-69.domain.tld            1.48                7615.24              5062.94
node-70.domain.tld            2.20                6020.54              5263.41
node-71.domain.tld            1.23                9309.62              3216.89
node-76.domain.tld            1.12                7306.60              3906.77
node-83.domain.tld            0.86                9444.11              1936.94
node-84.domain.tld            0.84                9387.14              2989.43
node-96.domain.tld            0.49                3118.69              3253.40
node-99.domain.tld            0.61                4473.49              3366.91
===================  =============  =====================  ===================

Download
========

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_download
    title: Download

.. image:: b10e7391-0b1c-4a48-86d1-2d291cf361e5.*

**Stats**:

===========  =============  =====================
concurrency  ping_icmp, ms  tcp_download, Mbits/s
===========  =============  =====================
          1           0.39                9838.36
          2           0.47                9837.31
          5           0.52                9837.85
         11           0.56                9837.84
         23           0.55                9685.34
         46           0.60                9615.75
         92           0.64                9428.83
        185           0.64                7867.68
===========  =============  =====================

Concurrency 1
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-228.domain.tld           0.39                9838.36
===================  =============  =====================

Concurrency 2
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-188.domain.tld           0.46                9837.64
node-228.domain.tld           0.49                9836.98
===================  =============  =====================

Concurrency 5
-------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-173.domain.tld           0.60                9836.67
node-175.domain.tld           0.51                9837.81
node-177.domain.tld           0.48                9838.71
node-188.domain.tld           0.58                9837.56
node-228.domain.tld           0.44                9838.50
===================  =============  =====================

Concurrency 11
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-173.domain.tld           0.54                9833.38
node-175.domain.tld           0.51                9839.29
node-177.domain.tld           0.43                9838.02
node-180.domain.tld           0.58                9839.49
node-182.domain.tld           0.51                9838.78
node-185.domain.tld           0.40                9839.55
node-188.domain.tld           0.50                9836.10
node-228.domain.tld           0.40                9838.79
node-248.domain.tld           1.33                9834.65
node-254.domain.tld           0.53                9838.21
node-61.domain.tld            0.46                9839.95
===================  =============  =====================

Concurrency 23
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            1.02                8816.15
node-104.domain.tld           1.23                7697.47
node-173.domain.tld           0.44                9837.21
node-175.domain.tld           0.53                9835.07
node-177.domain.tld           0.56                9836.73
node-180.domain.tld           0.45                9821.38
node-182.domain.tld           0.55                9838.87
node-185.domain.tld           0.40                9834.52
node-188.domain.tld           0.44                9837.01
node-228.domain.tld           0.40                9737.74
node-248.domain.tld           0.44                9746.13
node-254.domain.tld           0.43                9772.12
node-262.domain.tld           0.45                9839.64
node-377.domain.tld           0.50                9839.16
node-460.domain.tld           0.48                9839.73
node-473.domain.tld           0.58                9796.71
node-475.domain.tld           0.65                9838.19
node-481.domain.tld           0.44                9835.73
node-511.domain.tld           0.47                9836.10
node-517.domain.tld           0.46                9836.53
node-60.domain.tld            0.60                9814.66
node-61.domain.tld            0.50                9838.47
node-70.domain.tld            0.61                9837.52
===================  =============  =====================

Concurrency 46
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            1.08                8308.76
node-104.domain.tld           1.01                8886.89
node-173.domain.tld           0.35                9689.13
node-175.domain.tld           0.48                9835.32
node-177.domain.tld           0.40                9714.10
node-180.domain.tld           0.45                9834.72
node-182.domain.tld           0.56                9765.93
node-185.domain.tld           0.47                9839.10
node-188.domain.tld           0.61                9838.12
node-228.domain.tld           0.39                9787.21
node-248.domain.tld           0.55                9611.67
node-254.domain.tld           0.48                9813.95
node-260.domain.tld           0.55                9831.80
node-262.domain.tld           0.34                9742.84
node-276.domain.tld           1.02                8854.10
node-283.domain.tld           0.90                9288.16
node-301.domain.tld           1.40                7578.46
node-306.domain.tld           0.50                9833.56
node-343.domain.tld           0.54                9838.98
node-349.domain.tld           0.49                9839.97
node-350.domain.tld           0.69                9731.15
node-354.domain.tld           0.43                9838.47
node-359.domain.tld           0.52                9832.37
node-362.domain.tld           0.59                9723.81
node-363.domain.tld           0.48                9839.93
node-364.domain.tld           0.47                9838.74
node-372.domain.tld           0.45                9839.22
node-377.domain.tld           0.44                9838.65
node-382.domain.tld           0.46                9838.63
node-385.domain.tld           0.43                9837.25
node-386.domain.tld           0.59                9833.75
node-407.domain.tld           0.61                9839.80
node-420.domain.tld           0.58                9833.77
node-424.domain.tld           0.64                9794.67
node-429.domain.tld           0.43                9838.91
node-451.domain.tld           0.85                9397.91
node-460.domain.tld           0.42                9836.39
node-473.domain.tld           0.50                9812.88
node-475.domain.tld           0.68                9837.84
node-481.domain.tld           0.59                9838.11
node-496.domain.tld           0.45                9839.16
node-511.domain.tld           0.53                9826.30
node-517.domain.tld           0.50                9836.59
node-60.domain.tld            1.23                8623.98
node-61.domain.tld            0.51                9839.68
node-70.domain.tld            1.08                8603.78
===================  =============  =====================

Concurrency 92
--------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            1.02                8743.89
node-104.domain.tld           0.94                8926.00
node-141.domain.tld           0.61                9829.53
node-147.domain.tld           0.72                9680.84
node-149.domain.tld           0.69                9837.16
node-150.domain.tld           0.51                9839.07
node-153.domain.tld           0.63                9839.19
node-158.domain.tld           1.24                9786.32
node-173.domain.tld           0.57                9750.27
node-175.domain.tld           0.66                9779.96
node-177.domain.tld           0.65                9836.45
node-180.domain.tld           0.43                9835.22
node-182.domain.tld           0.38                9805.19
node-185.domain.tld           0.42                9838.78
node-188.domain.tld           0.50                9837.00
node-192.domain.tld           0.67                9837.46
node-195.domain.tld           0.43                9838.69
node-199.domain.tld           0.54                9833.09
node-202.domain.tld           0.44                9797.86
node-209.domain.tld           0.54                9836.31
node-211.domain.tld           0.60                9835.51
node-213.domain.tld           0.56                9839.62
node-214.domain.tld           2.06                9795.50
node-224.domain.tld           0.47                9803.14
node-228.domain.tld           0.44                9760.24
node-233.domain.tld           0.53                9833.12
node-236.domain.tld           0.42                9837.21
node-237.domain.tld           0.49                9838.42
node-241.domain.tld           0.45                9838.64
node-248.domain.tld           0.83                9810.54
node-254.domain.tld           0.85                9748.95
node-260.domain.tld           1.14                8632.65
node-262.domain.tld           0.72                9720.77
node-266.domain.tld           0.56                9801.76
node-276.domain.tld           1.06                8709.94
node-283.domain.tld           1.33                7619.82
node-287.domain.tld           0.43                9839.20
node-301.domain.tld           0.62                9832.59
node-306.domain.tld           1.26                8731.21
node-324.domain.tld           0.67                9700.30
node-328.domain.tld           0.44                9838.10
node-340.domain.tld           0.40                9839.54
node-342.domain.tld           0.55                9792.87
node-343.domain.tld           0.87                9140.56
node-349.domain.tld           0.58                9837.08
node-350.domain.tld           0.66                9763.90
node-354.domain.tld           0.41                9834.00
node-356.domain.tld           0.44                9838.37
node-359.domain.tld           0.64                9832.38
node-362.domain.tld           0.32                6566.10
node-363.domain.tld           0.40                9837.16
node-364.domain.tld           0.26                6651.80
node-368.domain.tld           0.32                6556.36
node-372.domain.tld           0.44                6702.14
node-374.domain.tld           0.84                8190.30
node-376.domain.tld           0.48                9839.77
node-377.domain.tld           0.42                6484.85
node-378.domain.tld           0.44                9834.30
node-382.domain.tld           0.46                9831.14
node-385.domain.tld           0.49                9818.46
node-386.domain.tld           0.48                6461.89
node-396.domain.tld           0.76                9772.15
node-397.domain.tld           0.82                9793.55
node-40.domain.tld            0.85                9319.32
node-402.domain.tld           0.48                9838.14
node-405.domain.tld           0.60                9835.59
node-406.domain.tld           0.51                9830.68
node-407.domain.tld           0.55                9695.73
node-414.domain.tld           0.41                9839.54
node-420.domain.tld           0.54                9837.92
node-424.domain.tld           0.77                9464.28
node-429.domain.tld           0.39                9837.14
node-43.domain.tld            0.98                8605.22
node-44.domain.tld            0.63                9836.06
node-451.domain.tld           1.02                8915.78
node-460.domain.tld           0.56                9839.31
node-47.domain.tld            0.54                9838.95
node-473.domain.tld           0.41                9837.68
node-475.domain.tld           0.53                9837.53
node-48.domain.tld            0.88                9218.85
node-481.domain.tld           0.41                9838.96
node-482.domain.tld           0.58                9819.35
node-496.domain.tld           0.51                9778.06
node-511.domain.tld           0.59                9832.06
node-517.domain.tld           0.57                9832.98
node-57.domain.tld            0.43                9838.29
node-60.domain.tld            0.57                9836.51
node-61.domain.tld            0.72                9830.21
node-63.domain.tld            1.32                7929.86
node-64.domain.tld            1.00                9109.90
node-70.domain.tld            0.62                9837.27
node-76.domain.tld            0.76                9646.99
===================  =============  =====================

Concurrency 185
---------------

**Stats**:

===================  =============  =====================
node                 ping_icmp, ms  tcp_download, Mbits/s
===================  =============  =====================
node-10.domain.tld            0.56                8782.27
node-103.domain.tld           0.59                5069.28
node-104.domain.tld           1.46                7281.46
node-117.domain.tld           0.72                9839.21
node-121.domain.tld           0.37                3686.45
node-123.domain.tld           0.49                9745.03
node-126.domain.tld           1.09                8902.22
node-127.domain.tld           0.50                9670.44
node-131.domain.tld           1.17                8042.17
node-134.domain.tld           1.32                7691.06
node-136.domain.tld           0.49                4966.76
node-138.domain.tld           0.65                9700.54
node-139.domain.tld           0.61                9834.96
node-141.domain.tld           0.54                6937.78
node-142.domain.tld           0.82                9782.84
node-147.domain.tld           0.89                8706.04
node-149.domain.tld           0.53                4920.15
node-150.domain.tld           0.62                3983.72
node-153.domain.tld           0.69                3589.04
node-158.domain.tld           0.53                3581.37
node-162.domain.tld           0.47                5644.59
node-173.domain.tld           0.27                4953.94
node-175.domain.tld           0.38                9836.30
node-177.domain.tld           0.64                9838.23
node-180.domain.tld           0.50                9837.83
node-182.domain.tld           0.61                3531.93
node-185.domain.tld           0.53                9838.57
node-188.domain.tld           0.64                9835.03
node-192.domain.tld           0.45                6588.67
node-195.domain.tld           0.48                9835.52
node-199.domain.tld           0.59                4386.50
node-201.domain.tld           0.77                9761.65
node-202.domain.tld           0.43                9838.16
node-209.domain.tld           0.61                4379.42
node-211.domain.tld           0.60                4489.49
node-213.domain.tld           0.42                9838.85
node-214.domain.tld           0.65                9834.58
node-22.domain.tld            0.35                6494.35
node-224.domain.tld           0.66                7902.37
node-226.domain.tld           0.40                9839.44
node-228.domain.tld           0.62                6329.11
node-233.domain.tld           0.76                9789.25
node-236.domain.tld           0.57                4925.95
node-237.domain.tld           0.60                3586.32
node-241.domain.tld           0.46                9835.31
node-248.domain.tld           0.65                9256.01
node-254.domain.tld           0.55                9012.22
node-256.domain.tld           1.11                8723.69
node-259.domain.tld           0.54                9822.80
node-260.domain.tld           0.54                7050.17
node-262.domain.tld           0.42                3569.05
node-264.domain.tld           0.67                9709.53
node-266.domain.tld           0.47                4708.21
node-268.domain.tld           0.47                9837.89
node-271.domain.tld           0.52                3444.70
node-272.domain.tld           0.46                9839.50
node-275.domain.tld           0.44                9836.14
node-276.domain.tld           1.13                8790.27
node-283.domain.tld           0.84                9262.05
node-287.domain.tld           0.42                9838.90
node-291.domain.tld           0.44                9837.96
node-292.domain.tld           0.45                9838.55
node-298.domain.tld           0.45                9558.76
node-301.domain.tld           1.32                7583.61
node-303.domain.tld           0.61                9837.23
node-306.domain.tld           0.49                9832.22
node-309.domain.tld           0.74                3537.28
node-313.domain.tld           0.46                9837.42
node-315.domain.tld           0.56                4976.00
node-316.domain.tld           1.13                9089.13
node-317.domain.tld           0.60                5943.86
node-318.domain.tld           0.66                9837.51
node-321.domain.tld           0.63                7938.21
node-323.domain.tld           0.69                9774.98
node-324.domain.tld           0.44                9838.31
node-328.domain.tld           0.59                9838.33
node-336.domain.tld           0.43                9839.44
node-337.domain.tld           1.21                8306.84
node-339.domain.tld           0.61                9838.96
node-340.domain.tld           0.48                9825.69
node-342.domain.tld           0.62                4721.93
node-343.domain.tld           0.60                9838.72
node-345.domain.tld           0.47                9837.10
node-349.domain.tld           0.67                9767.41
node-350.domain.tld           0.95                9367.73
node-354.domain.tld           0.51                9829.10
node-356.domain.tld           0.47                9836.47
node-358.domain.tld           0.46                5647.64
node-359.domain.tld           0.65                9552.95
node-360.domain.tld           0.73                8984.36
node-362.domain.tld           0.47                4806.11
node-363.domain.tld           0.57                3114.26
node-364.domain.tld           0.47                9589.04
node-365.domain.tld           0.54                9796.63
node-368.domain.tld           0.44                4660.02
node-369.domain.tld           1.49                7746.93
node-372.domain.tld           0.45                5606.06
node-374.domain.tld           0.45                7553.75
node-376.domain.tld           0.52                9718.90
node-377.domain.tld           0.48                6658.03
node-378.domain.tld           0.65                4069.30
node-382.domain.tld           0.50                9831.59
node-385.domain.tld           0.77                8344.12
node-386.domain.tld           0.49                6216.86
node-390.domain.tld           1.22                7695.44
node-391.domain.tld           1.20                7526.30
node-396.domain.tld           0.81                9789.28
node-397.domain.tld           0.69                4515.94
node-40.domain.tld            1.00                8948.58
node-402.domain.tld           0.41                9839.96
node-405.domain.tld           0.62                9716.04
node-406.domain.tld           0.79                9714.01
node-407.domain.tld           0.56                5495.85
node-414.domain.tld           0.50                9837.09
node-418.domain.tld           0.74                9689.44
node-419.domain.tld           1.33                8423.15
node-420.domain.tld           0.59                8018.19
node-424.domain.tld           0.63                9708.14
node-429.domain.tld           0.60                7244.63
node-43.domain.tld            0.41                9801.91
node-431.domain.tld           0.59                4611.16
node-432.domain.tld           0.65                9836.19
node-433.domain.tld           0.50                7138.97
node-437.domain.tld           0.49                9837.98
node-439.domain.tld           0.39                9315.56
node-44.domain.tld            1.26                8708.63
node-440.domain.tld           0.83                9834.76
node-445.domain.tld           0.52                9787.53
node-449.domain.tld           1.21                8817.73
node-450.domain.tld           0.44                4360.63
node-451.domain.tld           0.89                9305.38
node-455.domain.tld           0.31                4452.45
node-456.domain.tld           0.61                7575.01
node-459.domain.tld           0.64                4253.77
node-460.domain.tld           0.63                9764.46
node-465.domain.tld           0.57                4255.17
node-466.domain.tld           0.48                9836.75
node-467.domain.tld           0.45                5661.11
node-469.domain.tld           0.79                9761.87
node-47.domain.tld            0.75                6562.45
node-470.domain.tld           0.49                6244.78
node-472.domain.tld           0.62                9830.73
node-473.domain.tld           0.50                8843.67
node-475.domain.tld           0.71                9835.97
node-479.domain.tld           0.42                9827.30
node-48.domain.tld            0.57                9826.71
node-481.domain.tld           0.63                9732.23
node-482.domain.tld           0.62                9773.39
node-483.domain.tld           0.45                7186.63
node-484.domain.tld           0.56                9835.10
node-485.domain.tld           0.60                4197.97
node-486.domain.tld           0.53                9264.11
node-488.domain.tld           0.60                5440.98
node-489.domain.tld           0.41                3327.42
node-490.domain.tld           0.38                9838.43
node-493.domain.tld           0.48                3750.77
node-496.domain.tld           0.43                6012.70
node-498.domain.tld           0.48                5887.73
node-501.domain.tld           0.46                8174.86
node-503.domain.tld           0.53                4474.15
node-505.domain.tld           1.04                9634.58
node-506.domain.tld           0.54                9831.55
node-507.domain.tld           0.53                4407.64
node-508.domain.tld           0.44                3410.02
node-51.domain.tld            1.07                8640.07
node-511.domain.tld           0.57                9836.55
node-517.domain.tld           0.87                9504.60
node-519.domain.tld           0.75                9837.11
node-522.domain.tld           0.64                4175.19
node-53.domain.tld            1.14                8984.19
node-54.domain.tld            0.41                6431.18
node-57.domain.tld            0.58                9796.50
node-59.domain.tld            1.26                7670.61
node-60.domain.tld            0.43                9015.44
node-61.domain.tld            0.46                9836.94
node-63.domain.tld            0.64                6141.46
node-64.domain.tld            0.65                6112.27
node-69.domain.tld            1.56                7781.95
node-70.domain.tld            1.23                8220.10
node-71.domain.tld            0.87                7056.84
node-76.domain.tld            0.60                7019.99
node-83.domain.tld            0.78                9828.32
node-84.domain.tld            0.76                9830.92
node-96.domain.tld            0.62                3340.93
node-99.domain.tld            0.59                9838.16
===================  =============  =====================

Upload
======

**Test Specification**:

.. code-block:: yaml

    class: flent
    method: tcp_upload
    title: Upload

.. image:: a3e3783a-6585-4e87-bd65-a3d91b37464c.*

**Stats**:

===========  =============  ===================
concurrency  ping_icmp, ms  tcp_upload, Mbits/s
===========  =============  ===================
          1           0.40              9838.59
          2           0.41              9839.58
          5           0.47              9837.58
         11           0.46              9837.70
         23           0.60              9704.95
         46           0.72              9204.54
         92           0.65              8982.29
        185           0.75              8024.40
===========  =============  ===================

Concurrency 1
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-228.domain.tld           0.40              9838.59
===================  =============  ===================

Concurrency 2
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-188.domain.tld           0.41              9839.49
node-228.domain.tld           0.40              9839.67
===================  =============  ===================

Concurrency 5
-------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-173.domain.tld           0.40              9840.03
node-175.domain.tld           0.57              9827.20
node-177.domain.tld           0.55              9840.23
node-188.domain.tld           0.42              9839.73
node-228.domain.tld           0.39              9840.73
===================  =============  ===================

Concurrency 11
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-173.domain.tld           0.50              9826.22
node-175.domain.tld           0.45              9835.88
node-177.domain.tld           0.47              9837.63
node-180.domain.tld           0.57              9838.73
node-182.domain.tld           0.42              9839.39
node-185.domain.tld           0.44              9839.60
node-188.domain.tld           0.43              9838.77
node-228.domain.tld           0.38              9840.28
node-248.domain.tld           0.42              9840.14
node-254.domain.tld           0.45              9840.26
node-61.domain.tld            0.52              9837.81
===================  =============  ===================

Concurrency 23
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            1.17              9143.17
node-104.domain.tld           1.23              8636.35
node-173.domain.tld           0.43              9840.22
node-175.domain.tld           0.58              9839.81
node-177.domain.tld           0.44              9766.17
node-180.domain.tld           0.63              9838.96
node-182.domain.tld           0.47              9796.70
node-185.domain.tld           0.59              9766.30
node-188.domain.tld           0.44              9839.81
node-228.domain.tld           0.40              9839.94
node-248.domain.tld           0.43              9839.85
node-254.domain.tld           0.49              9840.49
node-262.domain.tld           0.48              9836.31
node-377.domain.tld           0.45              9839.51
node-460.domain.tld           0.53              9838.83
node-473.domain.tld           0.57              9752.05
node-475.domain.tld           0.50              9838.78
node-481.domain.tld           0.43              9839.50
node-511.domain.tld           0.45              9839.16
node-517.domain.tld           0.44              9831.91
node-60.domain.tld            0.64              9837.74
node-61.domain.tld            0.63              9838.22
node-70.domain.tld            1.42              8934.13
===================  =============  ===================

Concurrency 46
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            0.87              9334.52
node-104.domain.tld           1.64              7580.81
node-173.domain.tld           0.42              9732.03
node-175.domain.tld           0.51              9744.88
node-177.domain.tld           0.47              9838.75
node-180.domain.tld           0.49              9837.67
node-182.domain.tld           0.66              9840.18
node-185.domain.tld           0.55              9838.68
node-188.domain.tld           0.49              6059.77
node-228.domain.tld           0.60              9839.14
node-248.domain.tld           0.56              7916.54
node-254.domain.tld           0.38              8534.72
node-260.domain.tld           1.32              7926.04
node-262.domain.tld           0.57              9833.52
node-276.domain.tld           1.51              7790.81
node-283.domain.tld           1.43              8517.18
node-301.domain.tld           1.29              8678.73
node-306.domain.tld           0.97              9153.47
node-343.domain.tld           0.58              9838.88
node-349.domain.tld           0.54              9835.24
node-350.domain.tld           0.55              9826.84
node-354.domain.tld           0.49              9839.25
node-359.domain.tld           0.57              9837.34
node-362.domain.tld           0.64              9782.76
node-363.domain.tld           0.49              8286.70
node-364.domain.tld           0.52              9820.15
node-372.domain.tld           0.48              9840.08
node-377.domain.tld           0.44              9839.68
node-382.domain.tld           0.49              9839.28
node-385.domain.tld           0.50              9837.94
node-386.domain.tld           0.43              9839.48
node-407.domain.tld           0.63              9839.39
node-420.domain.tld           0.45              9838.82
node-424.domain.tld           0.87              9209.90
node-429.domain.tld           0.46              9837.60
node-451.domain.tld           1.40              8296.01
node-460.domain.tld           0.70              9838.39
node-473.domain.tld           0.39              9836.47
node-475.domain.tld           0.50              9838.84
node-481.domain.tld           0.65              9840.20
node-496.domain.tld           0.45              9837.85
node-511.domain.tld           0.58              9837.20
node-517.domain.tld           1.37              7711.18
node-60.domain.tld            1.59              7302.05
node-61.domain.tld            0.40              8410.54
node-70.domain.tld            1.42              7673.32
===================  =============  ===================

Concurrency 92
--------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            1.19              8570.16
node-104.domain.tld           1.26              8876.41
node-141.domain.tld           0.46              9837.55
node-147.domain.tld           1.16              8839.51
node-149.domain.tld           0.49              6785.68
node-150.domain.tld           0.53              6607.74
node-153.domain.tld           0.59              7422.49
node-158.domain.tld           0.51              7620.95
node-173.domain.tld           0.68              9802.95
node-175.domain.tld           0.73              9622.20
node-177.domain.tld           0.68              9838.31
node-180.domain.tld           0.54              9833.18
node-182.domain.tld           0.46              9836.50
node-185.domain.tld           0.56              9839.83
node-188.domain.tld           0.31              6894.18
node-192.domain.tld           0.68              9836.50
node-195.domain.tld           0.52              9839.74
node-199.domain.tld           0.48              9838.56
node-202.domain.tld           0.46              9839.33
node-209.domain.tld           0.39              9837.92
node-211.domain.tld           0.51              9835.89
node-213.domain.tld           0.37              9839.52
node-214.domain.tld           0.58              9839.76
node-224.domain.tld           0.31              7646.09
node-228.domain.tld           0.58              9840.36
node-233.domain.tld           0.42              7964.09
node-236.domain.tld           0.41              9839.79
node-237.domain.tld           0.51              8187.60
node-241.domain.tld           0.47              9839.06
node-248.domain.tld           0.29              6437.60
node-254.domain.tld           0.58              6651.56
node-260.domain.tld           0.62              9833.48
node-262.domain.tld           0.51              7932.56
node-266.domain.tld           0.43              6515.72
node-276.domain.tld           1.38              8313.90
node-283.domain.tld           1.43              7696.69
node-287.domain.tld           0.51              9839.87
node-301.domain.tld           1.39              8193.82
node-306.domain.tld           0.94              9349.49
node-324.domain.tld           0.44              9836.23
node-328.domain.tld           0.52              9839.36
node-340.domain.tld           0.43              9839.78
node-342.domain.tld           0.58              9833.86
node-343.domain.tld           0.67              9834.55
node-349.domain.tld           1.27              8615.88
node-350.domain.tld           0.54              9834.01
node-354.domain.tld           0.45              9840.31
node-356.domain.tld           0.40              9839.79
node-359.domain.tld           1.10              9567.27
node-362.domain.tld           0.58              9838.04
node-363.domain.tld           0.27              6661.72
node-364.domain.tld           0.53              9818.03
node-368.domain.tld           0.55              9814.83
node-372.domain.tld           0.53              9363.26
node-374.domain.tld           0.51              9268.94
node-376.domain.tld           0.49              6675.53
node-377.domain.tld           0.43              6559.34
node-378.domain.tld           0.49              6605.40
node-382.domain.tld           0.44              9840.12
node-385.domain.tld           0.48              6604.92
node-386.domain.tld           0.45              6410.04
node-396.domain.tld           0.59              9777.61
node-397.domain.tld           0.60              9760.10
node-40.domain.tld            0.55              9836.82
node-402.domain.tld           0.42              9839.33
node-405.domain.tld           0.57              9839.71
node-406.domain.tld           0.47              9835.44
node-407.domain.tld           0.49              9838.86
node-414.domain.tld           0.55              9839.01
node-420.domain.tld           0.55              9838.37
node-424.domain.tld           1.08              8725.84
node-429.domain.tld           0.61              9837.30
node-43.domain.tld            0.60              9839.69
node-44.domain.tld            0.66              9832.92
node-451.domain.tld           1.21              8519.62
node-460.domain.tld           0.69              9838.21
node-47.domain.tld            1.16              8657.33
node-473.domain.tld           0.41              9837.74
node-475.domain.tld           0.63              9836.54
node-48.domain.tld            0.63              9833.47
node-481.domain.tld           0.25              6481.16
node-482.domain.tld           0.67              9828.15
node-496.domain.tld           0.40              9837.92
node-511.domain.tld           0.61              9830.83
node-517.domain.tld           1.11              8224.01
node-57.domain.tld            0.61              9834.06
node-60.domain.tld            1.25              8918.00
node-61.domain.tld            0.58              6361.03
node-63.domain.tld            0.59              9835.13
node-64.domain.tld            1.50              8260.92
node-70.domain.tld            1.37              9835.26
node-76.domain.tld            1.15              8602.16
===================  =============  ===================

Concurrency 185
---------------

**Stats**:

===================  =============  ===================
node                 ping_icmp, ms  tcp_upload, Mbits/s
===================  =============  ===================
node-10.domain.tld            1.15              7423.82
node-103.domain.tld           2.76              9838.88
node-104.domain.tld           1.47              7537.05
node-117.domain.tld           0.85              9696.91
node-121.domain.tld           0.60              6272.51
node-123.domain.tld           0.41              3483.18
node-126.domain.tld           0.80              9640.31
node-127.domain.tld           0.79              9804.28
node-131.domain.tld           1.21              8766.21
node-134.domain.tld           1.21              8922.69
node-136.domain.tld           0.49              4032.70
node-138.domain.tld           0.79              5174.01
node-139.domain.tld           0.70              9830.44
node-141.domain.tld           1.45              7971.81
node-142.domain.tld           0.59              3737.87
node-147.domain.tld           1.10              9164.76
node-149.domain.tld           0.60              4308.28
node-150.domain.tld           0.53              9167.37
node-153.domain.tld           0.99              8700.60
node-158.domain.tld           0.51              6639.14
node-162.domain.tld           0.68              5585.68
node-173.domain.tld           0.57              6110.85
node-175.domain.tld           0.57              6954.91
node-177.domain.tld           0.70              9645.56
node-180.domain.tld           0.52              9834.13
node-182.domain.tld           0.70              9727.69
node-185.domain.tld           0.55              9839.13
node-188.domain.tld           0.73              9773.92
node-192.domain.tld           0.70              9821.33
node-195.domain.tld           0.46              9837.32
node-199.domain.tld           2.49              5590.25
node-201.domain.tld           2.73              9840.39
node-202.domain.tld           0.47              9839.33
node-209.domain.tld           0.36              7055.40
node-211.domain.tld           0.35              7613.34
node-213.domain.tld           0.39              9839.93
node-214.domain.tld           0.40              5405.87
node-22.domain.tld            1.26              9504.09
node-224.domain.tld           0.51              5114.23
node-226.domain.tld           0.41              9839.43
node-228.domain.tld           0.87              9839.09
node-233.domain.tld           0.36              5869.68
node-236.domain.tld           0.42              6916.34
node-237.domain.tld           0.85              9835.59
node-241.domain.tld           0.53              9839.07
node-248.domain.tld           0.76              9558.11
node-254.domain.tld           0.63              5292.94
node-256.domain.tld           1.02              8967.71
node-259.domain.tld           0.36              7967.14
node-260.domain.tld           0.58              8039.78
node-262.domain.tld           0.65              3886.34
node-264.domain.tld           0.63              6739.29
node-266.domain.tld           0.55              4397.60
node-268.domain.tld           1.37              9838.90
node-271.domain.tld           0.44              5045.12
node-272.domain.tld           0.55              9836.29
node-275.domain.tld           0.51              9838.35
node-276.domain.tld           1.34              8589.98
node-283.domain.tld           1.20              8914.20
node-287.domain.tld           0.48              9839.29
node-291.domain.tld           0.48              9839.67
node-292.domain.tld           0.52              9837.71
node-298.domain.tld           0.47              6096.50
node-301.domain.tld           1.35              8744.44
node-303.domain.tld           0.90              9834.83
node-306.domain.tld           1.04              9184.64
node-309.domain.tld           0.58              5233.37
node-313.domain.tld           0.43              9840.04
node-315.domain.tld           0.56              6531.31
node-316.domain.tld           1.55              7921.62
node-317.domain.tld           0.53              6677.31
node-318.domain.tld           0.50              9839.36
node-321.domain.tld           0.67              9826.24
node-323.domain.tld           0.41              8556.72
node-324.domain.tld           0.48              9836.76
node-328.domain.tld           0.60              5833.50
node-336.domain.tld           0.53              9838.82
node-337.domain.tld           1.37              7730.56
node-339.domain.tld           0.50              8617.25
node-340.domain.tld           0.43              9840.26
node-342.domain.tld           0.33              5362.76
node-343.domain.tld           1.55              8412.27
node-345.domain.tld           0.58              9806.61
node-349.domain.tld           0.53              9839.73
node-350.domain.tld           0.58              9832.34
node-354.domain.tld           0.51              9839.65
node-356.domain.tld           0.48              9837.11
node-358.domain.tld           0.44              4947.97
node-359.domain.tld           0.58              7756.14
node-360.domain.tld           1.10              9094.62
node-362.domain.tld           0.62              5951.71
node-363.domain.tld           0.56              3935.90
node-364.domain.tld           0.61              6030.79
node-365.domain.tld           1.37              9054.97
node-368.domain.tld           0.57              6028.57
node-369.domain.tld           1.22              8528.91
node-372.domain.tld           0.48              4357.65
node-374.domain.tld           0.46              3925.55
node-376.domain.tld           0.51              4174.97
node-377.domain.tld           0.53              5250.86
node-378.domain.tld           0.63              3712.99
node-382.domain.tld           0.51              9835.59
node-385.domain.tld           0.64              5239.75
node-386.domain.tld           0.71              5753.79
node-390.domain.tld           1.30              8324.58
node-391.domain.tld           1.30              7929.90
node-396.domain.tld           0.96              9618.95
node-397.domain.tld           0.40              6265.56
node-40.domain.tld            0.78              9839.03
node-402.domain.tld           0.53              9825.72
node-405.domain.tld           0.62              5166.47
node-406.domain.tld           0.44              9838.84
node-407.domain.tld           0.50              9838.92
node-414.domain.tld           0.42              9838.07
node-418.domain.tld           1.56              7440.55
node-419.domain.tld           0.92              9447.40
node-420.domain.tld           0.48              6324.73
node-424.domain.tld           0.99              8790.92
node-429.domain.tld           0.82              9427.95
node-43.domain.tld            1.31              8135.64
node-431.domain.tld           0.44              9762.54
node-432.domain.tld           1.67              7508.26
node-433.domain.tld           0.39              9818.07
node-437.domain.tld           0.52              9832.67
node-439.domain.tld           0.59              6020.25
node-44.domain.tld            1.36              7996.92
node-440.domain.tld           0.52              7500.64
node-445.domain.tld           0.52              9836.39
node-449.domain.tld           0.67              9839.73
node-450.domain.tld           0.63              5877.48
node-451.domain.tld           1.06              9264.37
node-455.domain.tld           0.55              4974.59
node-456.domain.tld           0.80              9803.90
node-459.domain.tld           0.47              4693.65
node-460.domain.tld           0.81              9830.23
node-465.domain.tld           0.86              9831.90
node-466.domain.tld           0.59              9837.10
node-467.domain.tld           0.50              4353.69
node-469.domain.tld           0.52              5296.92
node-47.domain.tld            0.93              7641.01
node-470.domain.tld           0.82              9827.56
node-472.domain.tld           0.58              6314.06
node-473.domain.tld           0.39              9815.18
node-475.domain.tld           0.49              4734.97
node-479.domain.tld           0.65              9683.01
node-48.domain.tld            0.54              9834.80
node-481.domain.tld           0.45              5199.69
node-482.domain.tld           0.48              5654.06
node-483.domain.tld           0.94              9783.72
node-484.domain.tld           0.45              9839.15
node-485.domain.tld           0.50              7765.40
node-486.domain.tld           0.98              9809.03
node-488.domain.tld           0.66              9839.88
node-489.domain.tld           0.48              6838.93
node-490.domain.tld           0.41              9839.58
node-493.domain.tld           0.57              9828.99
node-496.domain.tld           0.36              8086.19
node-498.domain.tld           0.42              9822.03
node-501.domain.tld           0.62              9763.38
node-503.domain.tld           0.47              5352.42
node-505.domain.tld           0.88              4852.98
node-506.domain.tld           0.47              9835.77
node-507.domain.tld           0.72              5780.10
node-508.domain.tld           0.50              7973.68
node-51.domain.tld            1.29              8148.41
node-511.domain.tld           0.49              9837.84
node-517.domain.tld           1.13              8759.55
node-519.domain.tld           0.86              9730.58
node-522.domain.tld           1.10              8999.69
node-53.domain.tld            0.59              9824.96
node-54.domain.tld            1.02              9271.10
node-57.domain.tld            0.60              9808.68
node-59.domain.tld            0.50              9834.19
node-60.domain.tld            0.71              9837.42
node-61.domain.tld            0.57              3567.34
node-63.domain.tld            1.64              7206.04
node-64.domain.tld            0.40              7927.81
node-69.domain.tld            0.99              9611.04
node-70.domain.tld            0.41              7657.31
node-71.domain.tld            1.69              7855.18
node-76.domain.tld            1.23              8206.83
node-83.domain.tld            0.53              8946.66
node-84.domain.tld            0.67              7365.26
node-96.domain.tld            0.61              8674.99
node-99.domain.tld            0.77              9685.73
===================  =============  ===================

