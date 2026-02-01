# AkDeviceData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_device_data-members.html) |
[Public 属性](#pub-attribs)

AkDeviceData结构体 参考

Device descriptor.
[更多...](struct_ak_device_data.html#details)

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) | [deviceID](struct_ak_device_data_aa567b7488a340d68e0d3212874770e45.html#aa567b7488a340d68e0d3212874770e45) |
|  | Device ID [更多...](struct_ak_device_data_aa567b7488a340d68e0d3212874770e45.html#aa567b7488a340d68e0d3212874770e45) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMemSize](struct_ak_device_data_a9d8c093ff6fe920b86b31b95ddfe9bf9.html#a9d8c093ff6fe920b86b31b95ddfe9bf9) |
|  | IO memory pool size [更多...](struct_ak_device_data_a9d8c093ff6fe920b86b31b95ddfe9bf9.html#a9d8c093ff6fe920b86b31b95ddfe9bf9) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMemUsed](struct_ak_device_data_a218fe09c7e3b8eb3d2f5901992ba5a59.html#a218fe09c7e3b8eb3d2f5901992ba5a59) |
|  | IO memory pool used [更多...](struct_ak_device_data_a218fe09c7e3b8eb3d2f5901992ba5a59.html#a218fe09c7e3b8eb3d2f5901992ba5a59) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uAllocs](struct_ak_device_data_a8d52303456b144be4a16ab487ab6135f.html#a8d52303456b144be4a16ab487ab6135f) |
|  | Cumulative number of allocations [更多...](struct_ak_device_data_a8d52303456b144be4a16ab487ab6135f.html#a8d52303456b144be4a16ab487ab6135f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uFrees](struct_ak_device_data_a813e05a291b81ccbd3c39ceea0d61339.html#a813e05a291b81ccbd3c39ceea0d61339) |
|  | Cumulative number of deallocations [更多...](struct_ak_device_data_a813e05a291b81ccbd3c39ceea0d61339.html#a813e05a291b81ccbd3c39ceea0d61339) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakRefdMemUsed](struct_ak_device_data_a9008be67958e4c34afee2c68ff2e997a.html#a9008be67958e4c34afee2c68ff2e997a) |
|  | Memory peak since monitoring started [更多...](struct_ak_device_data_a9008be67958e4c34afee2c68ff2e997a.html#a9008be67958e4c34afee2c68ff2e997a) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uUnreferencedCachedBytes](struct_ak_device_data_a0bffbbc054088fc98fdf3ce70d097162.html#a0bffbbc054088fc98fdf3ce70d097162) |
|  | IO memory that is cached but is not currently used for active streams. [更多...](struct_ak_device_data_a0bffbbc054088fc98fdf3ce70d097162.html#a0bffbbc054088fc98fdf3ce70d097162) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uGranularity](struct_ak_device_data_a73ceca6480ceffa50466df30b5d2120f.html#a73ceca6480ceffa50466df30b5d2120f) |
|  | IO memory pool block size [更多...](struct_ak_device_data_a73ceca6480ceffa50466df30b5d2120f.html#a73ceca6480ceffa50466df30b5d2120f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumActiveStreams](struct_ak_device_data_a77c9f507f5ccfa799006e9ff2bcbc65d.html#a77c9f507f5ccfa799006e9ff2bcbc65d) |
|  | Number of streams that have been active in the previous frame [更多...](struct_ak_device_data_a77c9f507f5ccfa799006e9ff2bcbc65d.html#a77c9f507f5ccfa799006e9ff2bcbc65d) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uTotalBytesTransferred](struct_ak_device_data_afa0b39a33bf3bcca62ebece6073b4d3f.html#afa0b39a33bf3bcca62ebece6073b4d3f) |
|  | Number of bytes transferred, including cached transfers [更多...](struct_ak_device_data_afa0b39a33bf3bcca62ebece6073b4d3f.html#afa0b39a33bf3bcca62ebece6073b4d3f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uLowLevelBytesTransferred](struct_ak_device_data_a11f8e27d60396755cc02986a40542432.html#a11f8e27d60396755cc02986a40542432) |
|  | Number of bytes transferred exclusively via low-level [更多...](struct_ak_device_data_a11f8e27d60396755cc02986a40542432.html#a11f8e27d60396755cc02986a40542432) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fAvgCacheEfficiency](struct_ak_device_data_a58d8d0b1e24cf16f684319e2581818e3.html#a58d8d0b1e24cf16f684319e2581818e3) |
|  | Total bytes from cache as a percentage of total bytes. [更多...](struct_ak_device_data_a58d8d0b1e24cf16f684319e2581818e3.html#a58d8d0b1e24cf16f684319e2581818e3) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumLowLevelRequestsCompleted](struct_ak_device_data_a6d8c8544f86b4a0459e539f1c86bd5dc.html#a6d8c8544f86b4a0459e539f1c86bd5dc) |
|  | Number of low-level transfers that have completed in the previous monitoring frame [更多...](struct_ak_device_data_a6d8c8544f86b4a0459e539f1c86bd5dc.html#a6d8c8544f86b4a0459e539f1c86bd5dc) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumLowLevelRequestsCancelled](struct_ak_device_data_a42424cf3d090a4a81800d04222b05b8f.html#a42424cf3d090a4a81800d04222b05b8f) |
|  | Number of low-level transfers that were cancelled in the previous monitoring frame [更多...](struct_ak_device_data_a42424cf3d090a4a81800d04222b05b8f.html#a42424cf3d090a4a81800d04222b05b8f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumLowLevelRequestsPending](struct_ak_device_data_a289c2bbeab4b8411cffa59f51e2650b6.html#a289c2bbeab4b8411cffa59f51e2650b6) |
|  | Number of low-level transfers that are currently pending [更多...](struct_ak_device_data_a289c2bbeab4b8411cffa59f51e2650b6.html#a289c2bbeab4b8411cffa59f51e2650b6) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uCustomParam](struct_ak_device_data_a0ce373f0b08d42a6b64653ace764abe5.html#a0ce373f0b08d42a6b64653ace764abe5) |
|  | Custom number queried from low-level IO. [更多...](struct_ak_device_data_a0ce373f0b08d42a6b64653ace764abe5.html#a0ce373f0b08d42a6b64653ace764abe5) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uCachePinnedBytes](struct_ak_device_data_a715e6afa5d4a56332ebac36519868a52.html#a715e6afa5d4a56332ebac36519868a52) |
|  | Number of bytes that can be pinned into cache. [更多...](struct_ak_device_data_a715e6afa5d4a56332ebac36519868a52.html#a715e6afa5d4a56332ebac36519868a52) |
|  | |

## 详细描述

Device descriptor.

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [133](_i_ak_stream_mgr_8h_source.html#l00133) 行定义.