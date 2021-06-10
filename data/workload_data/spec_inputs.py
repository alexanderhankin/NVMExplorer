# This file includes workload data collected using Sniper for SPECrate 2017 run on a simulated processor 
# similar to an Intel Skylake. 
#
# Various last level cache (LLC) sizes were studied). For each LLC size, the data values included are:
# 1. Number of LLC reads
# 2. Number of LLC writes
# 3. Execution time
#
# For an LLC size of 16MB, the following data values are also included:
# 4. Number of DRAM reads
# 5. Number of DRAM writes
# 6. Number of L2 reads
# 7. Number of L2 writes 
#
# References:
#
# T. E. Carlson, W. Heirman, S. Eyerman, I. Hur, and L. Eeckhout, “An evaluation of high-level mechanistic 
# core models,”ACMTransactions on Architecture and Code Optimization (TACO), 2014.


spec8MBLLC = {
  "names": ["544.nab_r",
    "502.gcc_r",
    "520.omnetpp_r",
    "527.cam4_r",
    "525.x264_r",
    "523.xalancbmk_r",
    "505.mcf_r",
    "503.bwaves_r",
    "511.povray_r",
    "510.parest_r",
    "521.wrf_r",
    "500.perlbench_r",
    "508.namd_r",
    "519.lbm_r",
    "526.blender_r",
    "531.deepsjeng_r",
    "538.imagick_r",
    "541.leela_r",
    "549.fotonik3d_r",
    "557.xz_r",
    "548.exchange2_r",
    "554.roms_r",
  ],
  "reads": [718221,
    315974,
    3247385,
    0,
    1694407,
    14189676,
    21663715,
    0,
    367,
    0,
    0,
    537236,
    88373,
    15594920,
    7088,
    216957,
    131702,
    43089,
    0,
    348859,
    0,
    0,
  ],
  "writes": [316842,
    492005,
    461957,
    0,
    988554,
    177170,
    16453043,
    0,
    948,
    0,
    0,
    432168,
    769990,
    15602139,
    133884,
    238895,
    800795,
    57942,
    0,
    879848,
    0,
    0,
  ],
  "ex_time": [0.13499321,
    0.119132203,
    0.128960125,
    0,
    0.076020581,
    0.127457892,
    0.299732027,
    0,
    0.098303235,
    0,
    0,
    0.123662168,
    0.087542673,
    0.338967826,
    0.101472204,
    0.104507865,
    0.069970796,
    0.105329386,
    0,
    0.118264606,
    0,
    0,
  ]
}
#names stay same for other LLC provisioning, just swap read/write/time info
spec16MBLLC = spec8MBLLC.copy()

#turns out names are reordered per sheet, so I'll just paste here for consistency
spec16MBLLC["names"] = ["500.perlbench_r",
    "544.nab_r",
    "527.cam4_r",
    "541.leela_r",
    "502.gcc_r",
    "510.parest_r",
    "523.xalancbmk_r",
    "520.omnetpp_r",
    "511.povray_r",
    "521.wrf_r",
    "525.x264_r",
    "503.bwaves_r",
    "526.blender_r",
    "531.deepsjeng_r",
    "538.imagick_r",
    "548.exchange2_r",
    "549.fotonik3d_r",
    "554.roms_r",
    "519.lbm_r",
    "557.xz_r",
    "505.mcf_r",
    "508.namd_r",
  ]

spec16MBLLC["reads"] = [720597,
    742402,
    3908070,
    44306,
    361550,
    4598398,
    14185521,
    3093580,
    291,
    5775967,
    1694352,
    3808468,
    7341,
    220424,
    150822,
    0,
    1956,
    551532,
    15590958,
    393408,
    38123201,
    89875,
  ]

spec16MBLLC["writes"] = [203912,
    265299,
    6015783,
    57939,
    479091,
    6199456,
    176657,
    462004,
    948,
    1155067,
    988554,
    18047213,
    133809,
    228938,
    781566,
    1639,
    41130,
    4819389,
    15602075,
    833701,
    558,
    767878,
  ]

spec16MBLLC["ex_time"] = [0.117277899,
    0.13260924,
    0.172031649,
    0.105311142,
    0.118511322,
    0.326452344,
    0.12737804,
    0.128037836,
    0.098384804,
    0.123238086,
    0.076003783,
    0.443826143,
    0.102297271,
    0.104075317,
    0.069700823,
    0.089839366,
    0.077052839,
    0.197093742,
    0.338424105,
    0.116153859,
    0.158765953,
    0.086823273,
  ]

spec16MBDRAM = spec16MBLLC.copy()

spec16MBDRAM["reads"] = [203912,
    265299,
    6015783,
    57939,
    479091,
    6199456,
    176657,
    462004,
    948,
    1155067,
    988554,
    18047213,
    133809,
    228938,
    781566,
    1639,
    41130,
    4819389,
    15602075,
    833701,
    558,
    767878,
  ]

spec16MBDRAM["writes"] = [200077,
    82767,
    5999325,
    0,
    468926,
    3459924,
    34515,
    425731,
    0,
    984095,
    988548,
    9501948,
    91611,
    205596,
    493260,
    0,
    0,
    4271921,
    7851229,
    750868,
    558,
    537684,
  ]

spec16MBL2 = spec16MBLLC.copy()

spec16MBL2["reads"] = [27280317,
    5627877,
    2367475,
    1904490,
    21307562,
    5300157,
    14153610,
    20843420,
    7673380,
    12591175,
    172977,
    42902989,
    52484,
    1673534,
    9428963,
    485747,
    16964,
    69971,
    20163895,
    1390511,
    14071805,
    1652130,
  ]

spec16MBL2["writes"] = [912480,
    997372,
    9859498,
    102225,
    756148,
    8196866,
    14361630,
    3100610,
    1239,
    6711427,
    2682607,
    21855370,
    140713,
    292181,
    932307,
    1639,
    43086,
    5370576,
    31193029,
    1215047,
    38123369,
    830670,
  ]


spec32MBLLC = spec8MBLLC.copy()

spec32MBLLC["names"] = ["544.nab_r",
    "500.perlbench_r",
    "503.bwaves_r",
    "505.mcf_r",
    "502.gcc_r",
    "508.namd_r",
    "510.parest_r",
    "519.lbm_r",
    "511.povray_r",
    "520.omnetpp_r",
    "521.wrf_r",
    "525.x264_r",
    "523.xalancbmk_r",
    "526.blender_r",
    "527.cam4_r",
    "531.deepsjeng_r",
    "538.imagick_r",
    "541.leela_r",
    "548.exchange2_r",
    "549.fotonik3d_r",
    "557.xz_r",
    "554.roms_r",
  ]

spec32MBLLC["reads"] = [834183,
    751687,
    0,
    38014106,
    362193,
    93802,
    0,
    15595026,
    361,
    3127847,
    0,
    1694095,
    13999904,
    12509,
    0,
    226709,
    267209,
    39672,
    0,
    0,
    431895,
    0,
  ]
spec32MBLLC["writes"] = [265366,
    173123,
    0,
    410,
    473573,
    763878,
    0,
    15602064,
    947,
    458017,
    0,
    988543,
    176643,
    128421,
    0,
    223084,
    665644,
    57938,
    0,
    0,
    802728,
    0,
  ]
spec32MBLLC["ex_time"] = [0.132646094,
    0.115587209,
    0,
    0.158680376,
    0.118546595,
    0.084056173,
    0,
    0.338437299,
    0.097861697,
    0.126399847,
    0,
    0.076056556,
    0.127091625,
    0.101489282,
    0,
    0.103849673,
    0.068295375,
    0.105306359,
    0,
    0,
    0.114494025,
    0,
  ]

spec64MBLLC = spec8MBLLC.copy()

spec64MBLLC["names"] = ["523.xalancbmk_r",
    "511.povray_r",
    "500.perlbench_r",
    "508.namd_r",
    "554.roms_r",
    "525.x264_r",
    "521.wrf_r",
    "526.blender_r",
    "505.mcf_r",
    "548.exchange2_r",
    "531.deepsjeng_r",
    "541.leela_r",
    "519.lbm_r",
    "520.omnetpp_r",
    "502.gcc_r",
    "527.cam4_r",
    "510.parest_r",
    "557.xz_r",
    "549.fotonik3d_r",
    "538.imagick_r",
    "503.bwaves_r",
    "544.nab_r",
  ]

spec64MBLLC["reads"] = [14086107,
    398,
    712958,
    164559,
    0,
    1672116,
    0,
    12939,
    38134872,
    0,
    223902,
    57290,
    15590497,
    3140576,
    320437,
    0,
    0,
    437097,
    0,
    394400,
    0,
    770858,
  ]
spec64MBLLC["writes"] = [176643,
    948,
    173123,
    693331,
    0,
    1010272,
    0,
    127997,
    410,
    0,
    212456,
    57941,
    15602673,
    457882,
    473121,
    0,
    0,
    787148,
    0,
    538345,
    0,
    265408,
  ]
spec64MBLLC["ex_time"] = [0.127011433,
    0.097991111,
    0.11565751,
    0.081835573,
    0,
    0.074974698,
    0,
    0.100817816,
    0.158810747,
    0,
    0.103915604,
    0.105329248,
    0.401782854,
    0.125242519,
    0.118265077,
    0,
    0,
    0.112324086,
    0,
    0.066648775,
    0,
    0.132567377,
  ]

spec8MBLLC["names"] = [ name+"8MB" for name in spec8MBLLC["names"] ]
spec16MBLLC["names"] = [ name+"16MB" for name in spec16MBLLC["names"] ]
spec16MBDRAM["names"] = [ name+"16MB_main" for name in spec16MBDRAM["names"] ]
spec16MBL2["names"] = [ name+"16MB_l2" for name in spec16MBL2["names"] ]
spec32MBLLC["names"] = [ name+"32MB" for name in spec32MBLLC["names"] ]
spec64MBLLC["names"] = [ name+"64MB" for name in spec64MBLLC["names"] ]
