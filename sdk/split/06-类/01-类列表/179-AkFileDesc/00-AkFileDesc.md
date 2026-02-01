# AkFileDesc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_file_desc-members.html) |
[Public 属性](#pub-attribs)

AkFileDesc结构体 参考

`#include <AkStreamMgrModule.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) | [iFileSize](struct_ak_file_desc_a243a35ffa3e375605563c318370931fd.html#a243a35ffa3e375605563c318370931fd) = 0 |
|  | File size in bytes [更多...](struct_ak_file_desc_a243a35ffa3e375605563c318370931fd.html#a243a35ffa3e375605563c318370931fd) |
|  | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uSector](struct_ak_file_desc_a3fc9acc74908496f0966c75b41b8e61e.html#a3fc9acc74908496f0966c75b41b8e61e) = 0 |
|  | |
| [AkFileHandle](_platforms_2_windows_2_ak_types_8h_a2b0b834e6d7c934fb7e04a739f38025d.html#a2b0b834e6d7c934fb7e04a739f38025d) | [hFile](struct_ak_file_desc_ad8ff92ae5cb0cb666d77688189f5ef3f.html#ad8ff92ae5cb0cb666d77688189f5ef3f) = [AkFileHandle](_platforms_2_windows_2_ak_types_8h_a2b0b834e6d7c934fb7e04a739f38025d.html#a2b0b834e6d7c934fb7e04a739f38025d)() |
|  | File handle/identifier [更多...](struct_ak_file_desc_ad8ff92ae5cb0cb666d77688189f5ef3f.html#ad8ff92ae5cb0cb666d77688189f5ef3f) |
|  | |
| [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) | [deviceID](struct_ak_file_desc_ab0a8deecfeedafa5760158ae01462d4b.html#ab0a8deecfeedafa5760158ae01462d4b) = [AK\_INVALID\_DEVICE\_ID](_ak_constants_8h_a377a957bb4c5022c2db433b401088901.html#a377a957bb4c5022c2db433b401088901) |
|  | Device ID, obtained from [CreateDevice()](namespace_a_k_1_1_stream_mgr_a64a22d377d25137222fbb66ff21965d5.html#a64a22d377d25137222fbb66ff21965d5) [更多...](struct_ak_file_desc_ab0a8deecfeedafa5760158ae01462d4b.html#ab0a8deecfeedafa5760158ae01462d4b) |
|  | |

## 详细描述

File descriptor. File identification for the low-level I/O.

参见
:   - [AK::StreamMgr::IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook.html)
    - [AK::StreamMgr::IAkLowLevelIOHook::BatchOpen](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a0abfde848b599b5e5b8e8ed63dc8b555.html#a0abfde848b599b5e5b8e8ed63dc8b555)
    - [AK::StreamMgr::IAkLowLevelIOHook::Close](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a7a50a7a5fa624691d7bb7608753dc096.html#a7a50a7a5fa624691d7bb7608753dc096)

在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [79](_ak_stream_mgr_module_8h_source.html#l00079) 行定义.