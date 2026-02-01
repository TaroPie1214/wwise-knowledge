# InitSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [BookmarkAlloc](namespace_a_k_1_1_bookmark_alloc.html)
- [InitSettings](struct_a_k_1_1_bookmark_alloc_1_1_init_settings.html)

[所有成员列表](struct_a_k_1_1_bookmark_alloc_1_1_init_settings-members.html) |
[Public 属性](#pub-attribs)

AK::BookmarkAlloc::InitSettings结构体 参考

`#include <AkTempAllocDefs.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMinimumBlockCount](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a12c53c74a26531dd2210998cd259fb0a.html#a12c53c74a26531dd2210998cd259fb0a) |
|  | The number of blocks of memory the system is initialized with and is the minimum kept around forever. Defaults to 1. Higher values increase upfront memory use, but can reduce, or eliminate, the creation and destruction of memory blocks over time. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a12c53c74a26531dd2210998cd259fb0a.html#a12c53c74a26531dd2210998cd259fb0a) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMinimumBlockSize](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_ad2444d4b53c747f71651d541a1b7fdb2.html#ad2444d4b53c747f71651d541a1b7fdb2) |
|  | The minimum size of each block. If a new allocation requests a new block of memory, then the new block is the size of the requested allocation times four, and then rounded up to the next multiple of this value. Defaults to 64 KiB. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_ad2444d4b53c747f71651d541a1b7fdb2.html#ad2444d4b53c747f71651d541a1b7fdb2) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaximumUnusedBlocks](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_ad4e70719eb5243ae4fdd8e833abf57b8.html#ad4e70719eb5243ae4fdd8e833abf57b8) |
|  | The maximum number of blocks that the system keeps in an unused state, and avoids freeing. Defaults to 1. Higher values do not increase the peak memory use, but do prevent unused memory from being freed, in order to reduce creation and destruction of memory blocks. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_ad4e70719eb5243ae4fdd8e833abf57b8.html#ad4e70719eb5243ae4fdd8e833abf57b8) |
|  | |
| bool | [bDebugDetailedStats](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a7b27d0bcea0ad9c36ed41c2e602168f0.html#a7b27d0bcea0ad9c36ed41c2e602168f0) |
|  | Enable to track detailed stats, specifically collection of [Stats::uRecentPeakMemUsed](struct_a_k_1_1_bookmark_alloc_1_1_stats_aac7e15c32ebf613e64b1b6f2a2cb9f75.html#aac7e15c32ebf613e64b1b6f2a2cb9f75 "Peak used memory in a single BookmarkAlloc region since the last tick (in bytes)."). Enabled by default. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a7b27d0bcea0ad9c36ed41c2e602168f0.html#a7b27d0bcea0ad9c36ed41c2e602168f0) |
|  | |
| bool | [bDebugClearMemory](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a78848d974865e0fdaf94944c8e5aee24.html#a78848d974865e0fdaf94944c8e5aee24) |
|  | Enable to clear any allocation to a deterministic garbage value during allocs, and after the stack is rewound to a bookmark. Useful to make sure memory is initialized properly. Disabled by default. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a78848d974865e0fdaf94944c8e5aee24.html#a78848d974865e0fdaf94944c8e5aee24) |
|  | |
| bool | [bDebugEnableSentinels](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a42b4d040a0a0685a786439ad0146769e.html#a42b4d040a0a0685a786439ad0146769e) |
|  | Enable to write out sentinels between most allocations to help detect memory overwrites, which are verified at the termination of a bookmark alloc region. Enabled by default. Increases memory usage of blocks slightly. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a42b4d040a0a0685a786439ad0146769e.html#a42b4d040a0a0685a786439ad0146769e) |
|  | |
| bool | [bDebugStandaloneAllocs](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_ac1e0b8831640622dd212fcd8b5f34589.html#ac1e0b8831640622dd212fcd8b5f34589) |
|  | Enable to force the block size to be as small as possible for each allocation (smaller than can be achieved by just setting uMinimumBlockSize to very low values). Useful to investigate memory overruns in-depth, especially in conjunction with the [MemoryMgr](namespace_a_k_1_1_memory_mgr.html)'s stomp allocator. If enabled, bDebugEnableSentinels will be disabled. Greatly increases CPU and memory usage. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_ac1e0b8831640622dd212fcd8b5f34589.html#ac1e0b8831640622dd212fcd8b5f34589) |
|  | |

## 详细描述

Initialization settings for Bookmark-allocator memory.

备注
:   The debug options are intended for monitoring and analyzing potential issues in usage of the [BookmarkAlloc](namespace_a_k_1_1_bookmark_alloc.html) system during development. Their functionality is specifically removed in Release configurations of the AkMemoryMgr.

在文件 [AkTempAllocDefs.h](_ak_temp_alloc_defs_8h_source.html) 第 [133](_ak_temp_alloc_defs_8h_source.html#l00133) 行定义.