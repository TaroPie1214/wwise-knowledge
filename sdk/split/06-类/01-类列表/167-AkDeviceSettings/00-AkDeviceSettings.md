# AkDeviceSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_device_settings-members.html) |
[Public 属性](#pub-attribs)

AkDeviceSettings结构体 参考

`#include <AkStreamMgrModule.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| void \* | [pIOMemory](struct_ak_device_settings_a3a99efb65d353954df652c007ac761c5.html#a3a99efb65d353954df652c007ac761c5) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uIOMemorySize](struct_ak_device_settings_a75893592924a59881fe2cbca4e4ddd04.html#a75893592924a59881fe2cbca4e4ddd04) |
|  | Size of memory for I/O (for automatic streams). It is passed directly to [AK::MemoryMgr::Malign()](namespace_a_k_1_1_memory_mgr_aeb57745b9cfdc88c9775e5bc504e9ab5.html#aeb57745b9cfdc88c9775e5bc504e9ab5), after having been rounded down to a multiple of uGranularity. [更多...](struct_ak_device_settings_a75893592924a59881fe2cbca4e4ddd04.html#a75893592924a59881fe2cbca4e4ddd04) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uIOMemoryAlignment](struct_ak_device_settings_ae4d4ef1d88e6a43dd134845f18e26b42.html#ae4d4ef1d88e6a43dd134845f18e26b42) |
|  | I/O memory alignment. It is passed directly to [AK::MemoryMgr::Malign()](namespace_a_k_1_1_memory_mgr_aeb57745b9cfdc88c9775e5bc504e9ab5.html#aeb57745b9cfdc88c9775e5bc504e9ab5). [更多...](struct_ak_device_settings_ae4d4ef1d88e6a43dd134845f18e26b42.html#ae4d4ef1d88e6a43dd134845f18e26b42) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [ePoolAttributes](struct_ak_device_settings_ac765faebf4d47270efbe33cc762192cb.html#ac765faebf4d47270efbe33cc762192cb) |
|  | Attributes for I/O memory. Here, specify the allocation type (AkMemType\_Device, and so on). It is passed directly to [AK::MemoryMgr::Malign()](namespace_a_k_1_1_memory_mgr_aeb57745b9cfdc88c9775e5bc504e9ab5.html#aeb57745b9cfdc88c9775e5bc504e9ab5). [更多...](struct_ak_device_settings_ac765faebf4d47270efbe33cc762192cb.html#ac765faebf4d47270efbe33cc762192cb) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uGranularity](struct_ak_device_settings_abd4879bfd150b9a2f898102e3815dbe2.html#abd4879bfd150b9a2f898102e3815dbe2) |
|  | I/O requests granularity (typical bytes/request). [更多...](struct_ak_device_settings_abd4879bfd150b9a2f898102e3815dbe2.html#abd4879bfd150b9a2f898102e3815dbe2) |
|  | |
| [AkThreadProperties](struct_ak_thread_properties.html) | [threadProperties](struct_ak_device_settings_a66496eabd7bf4cd482f2ef9925e489c4.html#a66496eabd7bf4cd482f2ef9925e489c4) |
|  | Scheduler thread properties. [更多...](struct_ak_device_settings_a66496eabd7bf4cd482f2ef9925e489c4.html#a66496eabd7bf4cd482f2ef9925e489c4) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fTargetAutoStmBufferLength](struct_ak_device_settings_af396c1626da7df1bbb6d9129e132b02f.html#af396c1626da7df1bbb6d9129e132b02f) |
|  | Targetted automatic stream buffer length (ms). When a stream reaches that buffering, it stops being scheduled for I/O except if the scheduler is idle. [更多...](struct_ak_device_settings_af396c1626da7df1bbb6d9129e132b02f.html#af396c1626da7df1bbb6d9129e132b02f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxConcurrentIO](struct_ak_device_settings_af49f8b3af816b58296e952b20de2d7a3.html#af49f8b3af816b58296e952b20de2d7a3) |
|  | Maximum number of transfers that can be sent simultaneously to the Low-Level I/O. [更多...](struct_ak_device_settings_af49f8b3af816b58296e952b20de2d7a3.html#af49f8b3af816b58296e952b20de2d7a3) |
|  | |
| bool | [bUseStreamCache](struct_ak_device_settings_aaa0e8dc2b18f827559aaf8672705dd49.html#aaa0e8dc2b18f827559aaf8672705dd49) |
|  | If true, the device attempts to reuse I/O buffers that have already been streamed from disk. This is particularly useful when streaming small looping sounds. However, there is a small increase in CPU usage when allocating memory, and a slightly larger memory footprint in the StreamManager pool.   [更多...](struct_ak_device_settings_aaa0e8dc2b18f827559aaf8672705dd49.html#aaa0e8dc2b18f827559aaf8672705dd49) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxCachePinnedBytes](struct_ak_device_settings_a08d0804974f70f6d8b7b0733ad4109dc.html#a08d0804974f70f6d8b7b0733ad4109dc) |
|  | Maximum number of bytes that can be "pinned" using [AK::SoundEngine::PinEventInStreamCache()](namespace_a_k_1_1_sound_engine_ae98b64113d2b9bd2e63adef8cee96805.html#ae98b64113d2b9bd2e63adef8cee96805) or [AK::IAkStreamMgr::PinFileInCache()](class_a_k_1_1_i_ak_stream_mgr_a702436773924b830729f94d609c62fc2.html#a702436773924b830729f94d609c62fc2) [更多...](struct_ak_device_settings_a08d0804974f70f6d8b7b0733ad4109dc.html#a08d0804974f70f6d8b7b0733ad4109dc) |
|  | |

## 详细描述

High-level IO devices initialization settings.

参见
:   - [AK::IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html)
    - [AK::StreamMgr::CreateDevice()](namespace_a_k_1_1_stream_mgr_a64a22d377d25137222fbb66ff21965d5.html#a64a22d377d25137222fbb66ff21965d5)
    - [Audiokinetic Stream Manager 初始化设置](streamingmanager_settings.html)

在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [58](_ak_stream_mgr_module_8h_source.html#l00058) 行定义.