# CategoryStats

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [MemoryMgr](namespace_a_k_1_1_memory_mgr.html)
- [CategoryStats](struct_a_k_1_1_memory_mgr_1_1_category_stats.html)

[所有成员列表](struct_a_k_1_1_memory_mgr_1_1_category_stats-members.html) |
[Public 属性](#pub-attribs)

AK::MemoryMgr::CategoryStats结构体 参考

`#include <AkMemoryMgr.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uUsed](struct_a_k_1_1_memory_mgr_1_1_category_stats_a6b11d352a70265da1e5fbfa60dadfd19.html#a6b11d352a70265da1e5fbfa60dadfd19) |
|  | Used memory (in bytes) [更多...](struct_a_k_1_1_memory_mgr_1_1_category_stats_a6b11d352a70265da1e5fbfa60dadfd19.html#a6b11d352a70265da1e5fbfa60dadfd19) |
|  | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uPeakUsed](struct_a_k_1_1_memory_mgr_1_1_category_stats_a941fdc14c1ac037fd6f3f1cda236919f.html#a941fdc14c1ac037fd6f3f1cda236919f) |
|  | Peak used memory (in bytes) [更多...](struct_a_k_1_1_memory_mgr_1_1_category_stats_a941fdc14c1ac037fd6f3f1cda236919f.html#a941fdc14c1ac037fd6f3f1cda236919f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uAllocs](struct_a_k_1_1_memory_mgr_1_1_category_stats_a38af8a45c793fe405635b7d0e7ff189a.html#a38af8a45c793fe405635b7d0e7ff189a) |
|  | Number of allocation calls since initialization [更多...](struct_a_k_1_1_memory_mgr_1_1_category_stats_a38af8a45c793fe405635b7d0e7ff189a.html#a38af8a45c793fe405635b7d0e7ff189a) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uFrees](struct_a_k_1_1_memory_mgr_1_1_category_stats_a9b55a91f75392c2fc6f3d8020b34ed51.html#a9b55a91f75392c2fc6f3d8020b34ed51) |
|  | Number of free calls since initialization [更多...](struct_a_k_1_1_memory_mgr_1_1_category_stats_a9b55a91f75392c2fc6f3d8020b34ed51.html#a9b55a91f75392c2fc6f3d8020b34ed51) |
|  | |

## 详细描述

Memory category statistics.

备注
:   These statistics are not collected in the Release configuration of the default memory manager implementation.

参见
:   - [AK::MemoryMgr::GetCategoryStats()](namespace_a_k_1_1_memory_mgr_a4a00138319c6ee33a6a4c896cabcea34.html#a4a00138319c6ee33a6a4c896cabcea34)
    - [Memory Manager](memorymanager.html)

在文件 [AkMemoryMgr.h](_ak_memory_mgr_8h_source.html) 第 [92](_ak_memory_mgr_8h_source.html#l00092) 行定义.