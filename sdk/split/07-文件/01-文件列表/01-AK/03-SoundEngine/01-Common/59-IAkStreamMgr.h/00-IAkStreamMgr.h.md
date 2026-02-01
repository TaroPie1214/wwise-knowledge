# IAkStreamMgr.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces)

IAkStreamMgr.h 文件参考

`#include <AK/SoundEngine/Common/AkMemoryMgr.h>`  
`#include <AK/SoundEngine/Common/AkFileSystemFlags.h>`

[浏览源代码.](_i_ak_stream_mgr_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkStreamInfo](struct_ak_stream_info.html) |
|  | |
| struct | [AkAutoStmHeuristics](struct_ak_auto_stm_heuristics.html) |
|  | Automatic streams heuristics. [更多...](struct_ak_auto_stm_heuristics.html#details) |
|  | |
| struct | [AkAutoStmBufSettings](struct_ak_auto_stm_buf_settings.html) |
|  | Automatic streams buffer settings/constraints. [更多...](struct_ak_auto_stm_buf_settings.html#details) |
|  | |
| struct | [AkDeviceDesc](struct_ak_device_desc.html) |
|  | Device descriptor. [更多...](struct_ak_device_desc.html#details) |
|  | |
| struct | [AkDeviceData](struct_ak_device_data.html) |
|  | Device descriptor. [更多...](struct_ak_device_data.html#details) |
|  | |
| struct | [AkStreamRecord](struct_ak_stream_record.html) |
|  | Stream general information. [更多...](struct_ak_stream_record.html#details) |
|  | |
| struct | [AkStreamData](struct_ak_stream_data.html) |
|  | Stream statistics. [更多...](struct_ak_stream_data.html#details) |
|  | |
| struct | [AkFileOpenData](struct_ak_file_open_data.html) |
|  | |
| class | [AK::IAkStreamProfile](class_a_k_1_1_i_ak_stream_profile.html) |
|  | |
| class | [AK::IAkDeviceProfile](class_a_k_1_1_i_ak_device_profile.html) |
|  | |
| class | [AK::IAkStreamMgrProfile](class_a_k_1_1_i_ak_stream_mgr_profile.html) |
|  | |
| class | [AK::IAkStdStream](class_a_k_1_1_i_ak_std_stream.html) |
|  | |
| class | [AK::IAkAutoStream](class_a_k_1_1_i_ak_auto_stream.html) |
|  | |
| class | [AK::IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| Profiling string lengths. | |
| #define | [AK\_MONITOR\_STREAMNAME\_MAXLENGTH](_i_ak_stream_mgr_8h_a202e0d60e7364c98e0b80dec959562c5.html#a202e0d60e7364c98e0b80dec959562c5)   (64) |
|  | |
| #define | [AK\_MONITOR\_DEVICENAME\_MAXLENGTH](_i_ak_stream_mgr_8h_ac16733718d45598daf254e78868c3f21.html#ac16733718d45598daf254e78868c3f21)   (64) |
|  | |
| enum | [AkStmStatus](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307) {     [AK\_StmStatusIdle](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307ad4ecb6caad030aa72c8ef4d82e8c5500) = 0, [AK\_StmStatusCompleted](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307a4ee943eb5fbd1c15c114a7db3cd9620e) = 1, [AK\_StmStatusPending](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307ae15cf279e956aef361e9191916377b90) = 2, [AK\_StmStatusCancelled](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307a8122c26f72bda0dbe4cbeaa94917f4b0) = 3,     [AK\_StmStatusError](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307acd646559057f6060264897517d7af22e) = 4   } |
|  | Stream status. [更多...](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307) |
|  | |
| enum | [AkMoveMethod](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865) { [AK\_MoveBegin](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865aaafcaeced22c9ffabc151a3cf0585fee) = 0, [AK\_MoveCurrent](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865ad7036d3c0758b66299e6c1d0e60a14c5) = 1, [AK\_MoveEnd](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865a9e480024dfcc031dff589ed3660f444c) = 2 } |
|  | |
| enum | [AkOpenMode](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7) { [AK\_OpenModeRead](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab35230305828a2d0aee87a3190ff661f) = 0, [AK\_OpenModeWrite](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7af5e576f2a186adb267c05d6d9931879b) = 1, [AK\_OpenModeWriteOvrwr](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7a8880055e60302ffdb7fe89e4068bb926) = 2, [AK\_OpenModeReadWrite](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab17f6b95edc9ff7cd668878325ffd93a) = 3 } |
|  | File open mode. [更多...](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7) |
|  | |

## 详细描述

Defines the API of Audiokinetic's I/O streaming solution.

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 中定义.