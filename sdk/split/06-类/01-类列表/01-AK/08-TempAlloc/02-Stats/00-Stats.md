# Stats

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [TempAlloc](namespace_a_k_1_1_temp_alloc.html)
- [Stats](struct_a_k_1_1_temp_alloc_1_1_stats.html)

[所有成员列表](struct_a_k_1_1_temp_alloc_1_1_stats-members.html) |
[Public 属性](#pub-attribs)

AK::TempAlloc::Stats结构体 参考

`#include <AkTempAllocDefs.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMemUsed](struct_a_k_1_1_temp_alloc_1_1_stats_a152743ba0ea86eb55e15017730280d3e.html#a152743ba0ea86eb55e15017730280d3e) |
|  | Used memory (in bytes). [更多...](struct_a_k_1_1_temp_alloc_1_1_stats_a152743ba0ea86eb55e15017730280d3e.html#a152743ba0ea86eb55e15017730280d3e) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMemAllocated](struct_a_k_1_1_temp_alloc_1_1_stats_a0b7a6c946bacf5b4628e63b17263b576.html#a0b7a6c946bacf5b4628e63b17263b576) |
|  | Allocated memory (in bytes). [更多...](struct_a_k_1_1_temp_alloc_1_1_stats_a0b7a6c946bacf5b4628e63b17263b576.html#a0b7a6c946bacf5b4628e63b17263b576) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uBlocksUsed](struct_a_k_1_1_temp_alloc_1_1_stats_a7fae92f31ff1e43fa32008b4449a1584.html#a7fae92f31ff1e43fa32008b4449a1584) |
|  | Number of individual blocks used. [更多...](struct_a_k_1_1_temp_alloc_1_1_stats_a7fae92f31ff1e43fa32008b4449a1584.html#a7fae92f31ff1e43fa32008b4449a1584) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakMemUsed](struct_a_k_1_1_temp_alloc_1_1_stats_a2a050f4d48768bdb1287c2b3150394c6.html#a2a050f4d48768bdb1287c2b3150394c6) |
|  | The peak value for uMemUsed since initialization. [更多...](struct_a_k_1_1_temp_alloc_1_1_stats_a2a050f4d48768bdb1287c2b3150394c6.html#a2a050f4d48768bdb1287c2b3150394c6) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakMemAllocated](struct_a_k_1_1_temp_alloc_1_1_stats_afd67fc41c8ad8df602ac7420465c1d8b.html#afd67fc41c8ad8df602ac7420465c1d8b) |
|  | The peak value for uMemAllocated since initialization. [更多...](struct_a_k_1_1_temp_alloc_1_1_stats_afd67fc41c8ad8df602ac7420465c1d8b.html#afd67fc41c8ad8df602ac7420465c1d8b) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakBlocksUsed](struct_a_k_1_1_temp_alloc_1_1_stats_a061d7b314dabe8173290e2a9e10ef2fd.html#a061d7b314dabe8173290e2a9e10ef2fd) |
|  | The peak value for uBlocksUsed since initialization. [更多...](struct_a_k_1_1_temp_alloc_1_1_stats_a061d7b314dabe8173290e2a9e10ef2fd.html#a061d7b314dabe8173290e2a9e10ef2fd) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakBlockUsed](struct_a_k_1_1_temp_alloc_1_1_stats_afffe17b4848f0fefe323947fb148b086.html#afffe17b4848f0fefe323947fb148b086) |
|  | The peak amount of used memory in any single block since initialization. [更多...](struct_a_k_1_1_temp_alloc_1_1_stats_afffe17b4848f0fefe323947fb148b086.html#afffe17b4848f0fefe323947fb148b086) |
|  | |

## 详细描述

Temp-alloc memory statistics. Whenever these are fetched, they represent the last completed temp-alloc "tick".

备注
:   These statistics are not collected in the Release configuration of the memory mgr.

在文件 [AkTempAllocDefs.h](_ak_temp_alloc_defs_8h_source.html) 第 [49](_ak_temp_alloc_defs_8h_source.html#l00049) 行定义.