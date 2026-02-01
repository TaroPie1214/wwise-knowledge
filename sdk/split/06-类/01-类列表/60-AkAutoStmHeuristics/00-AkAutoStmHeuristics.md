# AkAutoStmHeuristics

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_auto_stm_heuristics-members.html) |
[Public 属性](#pub-attribs)

AkAutoStmHeuristics结构体 参考

Automatic streams heuristics.
[更多...](struct_ak_auto_stm_heuristics.html#details)

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fThroughput](struct_ak_auto_stm_heuristics_a4765f706b096765eb25dd6c06073d9af.html#a4765f706b096765eb25dd6c06073d9af) |
|  | Average throughput in bytes/ms [更多...](struct_ak_auto_stm_heuristics_a4765f706b096765eb25dd6c06073d9af.html#a4765f706b096765eb25dd6c06073d9af) |
|  | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uLoopStart](struct_ak_auto_stm_heuristics_afe02155d1e487ebba5cf6b467c40f24d.html#afe02155d1e487ebba5cf6b467c40f24d) |
|  | Set to the start of loop (byte offset from the beginning of the stream) for streams that loop, 0 otherwise [更多...](struct_ak_auto_stm_heuristics_afe02155d1e487ebba5cf6b467c40f24d.html#afe02155d1e487ebba5cf6b467c40f24d) |
|  | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uLoopEnd](struct_ak_auto_stm_heuristics_a378d13e909830ce63e57782d9389506a.html#a378d13e909830ce63e57782d9389506a) |
|  | Set to the end of loop (byte offset from the beginning of the stream) for streams that loop, 0 otherwise [更多...](struct_ak_auto_stm_heuristics_a378d13e909830ce63e57782d9389506a.html#a378d13e909830ce63e57782d9389506a) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [uMinNumBuffers](struct_ak_auto_stm_heuristics_aeda0fa45777364065a470210b54bffea.html#aeda0fa45777364065a470210b54bffea) |
|  | |
| [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) | [priority](struct_ak_auto_stm_heuristics_a574352be21d197e2bbca4e87177a48ab.html#a574352be21d197e2bbca4e87177a48ab) |
|  | The stream priority. it should be between AK\_MIN\_PRIORITY and AK\_MAX\_PRIORITY (included). [更多...](struct_ak_auto_stm_heuristics_a574352be21d197e2bbca4e87177a48ab.html#a574352be21d197e2bbca4e87177a48ab) |
|  | |

## 详细描述

Automatic streams heuristics.

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [94](_i_ak_stream_mgr_8h_source.html#l00094) 行定义.