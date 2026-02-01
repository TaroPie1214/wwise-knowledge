# AkIoHeuristics

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_io_heuristics-members.html) |
[Public 属性](#pub-attribs)

AkIoHeuristics结构体 参考

`#include <AkStreamMgrModule.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fDeadline](struct_ak_io_heuristics_ae06c2754de52f04121fcb9a702802f3e.html#ae06c2754de52f04121fcb9a702802f3e) |
|  | Operation deadline (ms). [更多...](struct_ak_io_heuristics_ae06c2754de52f04121fcb9a702802f3e.html#ae06c2754de52f04121fcb9a702802f3e) |
|  | |
| [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) | [priority](struct_ak_io_heuristics_aad08e74728cfdc012810f51e288b5be6.html#aad08e74728cfdc012810f51e288b5be6) |
|  | Operation priority (at the time it was scheduled and sent to the Low-Level I/O). Range is [AK\_MIN\_PRIORITY,AK\_MAX\_PRIORITY], inclusively. [更多...](struct_ak_io_heuristics_aad08e74728cfdc012810f51e288b5be6.html#aad08e74728cfdc012810f51e288b5be6) |
|  | |

## 详细描述

Low-Level I/O requests heuristics. Used for asynchronous read requests.

参见
:   - [AK::StreamMgr::IAkLowLevelIOHook::BatchRead()](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a9bc325405bc17c0a5105d0a53981b186.html#a9bc325405bc17c0a5105d0a53981b186)
    - [AK::StreamMgr::IAkLowLevelIOHook::BatchWrite()](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a8f5041a24e395784437a62cdd2140505.html#a8f5041a24e395784437a62cdd2140505)

在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [212](_ak_stream_mgr_module_8h_source.html#l00212) 行定义.