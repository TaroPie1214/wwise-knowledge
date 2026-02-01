# GlobalStats

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [MemoryMgr](namespace_a_k_1_1_memory_mgr.html)
- [GlobalStats](struct_a_k_1_1_memory_mgr_1_1_global_stats.html)

[所有成员列表](struct_a_k_1_1_memory_mgr_1_1_global_stats-members.html) |
[Public 属性](#pub-attribs)

AK::MemoryMgr::GlobalStats结构体 参考

`#include <AkMemoryMgr.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uUsed](struct_a_k_1_1_memory_mgr_1_1_global_stats_a21492cb4c3b1a521649d0803b53e8e72.html#a21492cb4c3b1a521649d0803b53e8e72) |
|  | Total memory used including all categories (in bytes) [更多...](struct_a_k_1_1_memory_mgr_1_1_global_stats_a21492cb4c3b1a521649d0803b53e8e72.html#a21492cb4c3b1a521649d0803b53e8e72) |
|  | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uReserved](struct_a_k_1_1_memory_mgr_1_1_global_stats_a657aa7025f67cfbd677aa743e56adde8.html#a657aa7025f67cfbd677aa743e56adde8) |
|  | Total reserved memory. (Used and unused). Will return 0 if the reserved memory is not traceable. [更多...](struct_a_k_1_1_memory_mgr_1_1_global_stats_a657aa7025f67cfbd677aa743e56adde8.html#a657aa7025f67cfbd677aa743e56adde8) |
|  | |

## 详细描述

Memory global statistics.

备注
:   These statistics are not collected in the Release configuration of the default memory manager implementation.

参见
:   - [AK::MemoryMgr::GetGlobalStats()](namespace_a_k_1_1_memory_mgr_a49ab92c52b9afa8e034863f2cdd2209e.html#a49ab92c52b9afa8e034863f2cdd2209e)
    - [Memory Manager](memorymanager.html)

在文件 [AkMemoryMgr.h](_ak_memory_mgr_8h_source.html) 第 [109](_ak_memory_mgr_8h_source.html#l00109) 行定义.