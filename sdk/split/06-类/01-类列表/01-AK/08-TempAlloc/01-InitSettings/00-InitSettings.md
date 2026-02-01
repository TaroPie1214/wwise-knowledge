# InitSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [TempAlloc](namespace_a_k_1_1_temp_alloc.html)
- [InitSettings](struct_a_k_1_1_temp_alloc_1_1_init_settings.html)

[所有成员列表](struct_a_k_1_1_temp_alloc_1_1_init_settings-members.html) |
[Public 属性](#pub-attribs)

AK::TempAlloc::InitSettings结构体 参考

`#include <AkTempAllocDefs.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMinimumBlockCount](struct_a_k_1_1_temp_alloc_1_1_init_settings_a2f1fb0fceeb796d39542cc3cd1f3d1fa.html#a2f1fb0fceeb796d39542cc3cd1f3d1fa) |
|  | The number of blocks of memory the system is initialized with and is the minimum kept around forever. Defaults to 1. Higher values increase upfront memory use, but can reduce, or eliminate, the creation and destruction of memory blocks over time. [更多...](struct_a_k_1_1_temp_alloc_1_1_init_settings_a2f1fb0fceeb796d39542cc3cd1f3d1fa.html#a2f1fb0fceeb796d39542cc3cd1f3d1fa) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMinimumBlockSize](struct_a_k_1_1_temp_alloc_1_1_init_settings_aaa251de5c00ef8acbf3be694b4d60c6f.html#aaa251de5c00ef8acbf3be694b4d60c6f) |
|  | The minimum size of each block. If a new allocation requests a new block of memory, then the new block is the size of the requested allocation times four, and then rounded up to the next multiple of this value. Defaults to 512 KiB. [更多...](struct_a_k_1_1_temp_alloc_1_1_init_settings_aaa251de5c00ef8acbf3be694b4d60c6f.html#aaa251de5c00ef8acbf3be694b4d60c6f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaximumUnusedBlocks](struct_a_k_1_1_temp_alloc_1_1_init_settings_a0869a066e6830c5665538f01ef3c9033.html#a0869a066e6830c5665538f01ef3c9033) |
|  | The maximum number of blocks that the system keeps in an unused state, and avoids freeing. Defaults to 1. Higher values do not increase the peak memory use, but do prevent unused memory from being freed, in order to reduce creation and destruction of memory blocks. [更多...](struct_a_k_1_1_temp_alloc_1_1_init_settings_a0869a066e6830c5665538f01ef3c9033.html#a0869a066e6830c5665538f01ef3c9033) |
|  | |
| bool | [bDebugDetailedStats](struct_a_k_1_1_temp_alloc_1_1_init_settings_a03e19747bfa243389cdd6d6f9e13f2a0.html#a03e19747bfa243389cdd6d6f9e13f2a0) |
|  | Enable to track detailed stats and include them in the detailed stat dump. Detailed stats include the size and quantity of each type of allocation from the system. Disabled by default. [更多...](struct_a_k_1_1_temp_alloc_1_1_init_settings_a03e19747bfa243389cdd6d6f9e13f2a0.html#a03e19747bfa243389cdd6d6f9e13f2a0) |
|  | |
| bool | [bDebugClearMemory](struct_a_k_1_1_temp_alloc_1_1_init_settings_a6d1a7c2066385c5d98c3b8e198267a16.html#a6d1a7c2066385c5d98c3b8e198267a16) |
|  | Enable to clear any allocation to a deterministic garbage value. Useful to make sure memory is initialized properly. Disabled by default. [更多...](struct_a_k_1_1_temp_alloc_1_1_init_settings_a6d1a7c2066385c5d98c3b8e198267a16.html#a6d1a7c2066385c5d98c3b8e198267a16) |
|  | |
| bool | [bDebugEnableSentinels](struct_a_k_1_1_temp_alloc_1_1_init_settings_a76625e926d53a8d79283411bbc2cc9dd.html#a76625e926d53a8d79283411bbc2cc9dd) |
|  | Enable to write out sentinels between most allocations to help detect memory overwrites, verified at the end of a tick. Enabled by default. Increases memory usage of blocks slightly. [更多...](struct_a_k_1_1_temp_alloc_1_1_init_settings_a76625e926d53a8d79283411bbc2cc9dd.html#a76625e926d53a8d79283411bbc2cc9dd) |
|  | |
| bool | [bDebugFlushBlocks](struct_a_k_1_1_temp_alloc_1_1_init_settings_a7e3484c294f840bd4052f1ba8a5a376c.html#a7e3484c294f840bd4052f1ba8a5a376c) |
|  | Enable to forcefully release all blocks at the end of a tick and recreate them from scratch every tick. Useful to ensure stale memory is not being accessed. Disabled by default. This might interfere with some stats reporting due to blocks being released between ticks. [更多...](struct_a_k_1_1_temp_alloc_1_1_init_settings_a7e3484c294f840bd4052f1ba8a5a376c.html#a7e3484c294f840bd4052f1ba8a5a376c) |
|  | |
| bool | [bDebugStandaloneAllocs](struct_a_k_1_1_temp_alloc_1_1_init_settings_aa96cd186984f5a81e72a66ab723e0f5e.html#aa96cd186984f5a81e72a66ab723e0f5e) |
|  | Enable to force the block size to be as small as possible for each allocation (smaller than can be achieved by just setting uMinimumBlockSize to very low values). Useful to investigate memory overruns in-depth, especially in conjunction with other options like bDebugFlushBlocks and the [MemoryMgr](namespace_a_k_1_1_memory_mgr.html)'s stomp allocator. If enabled, bDebugDetailedStats and bDebugEnableSentinels will be disabled. Greatly increases CPU and memory usage. [更多...](struct_a_k_1_1_temp_alloc_1_1_init_settings_aa96cd186984f5a81e72a66ab723e0f5e.html#aa96cd186984f5a81e72a66ab723e0f5e) |
|  | |

## 详细描述

Initialization settings for temporary-memory pools. Separate settings are specified for each temporary-memory pool.

备注
:   The debug options are intended for monitoring and analyzing potential issues in usage of the [TempAlloc](namespace_a_k_1_1_temp_alloc.html) system during development. Their functionality is specifically removed in Release configurations of the AkMemoryMgr.

在文件 [AkTempAllocDefs.h](_ak_temp_alloc_defs_8h_source.html) 第 [78](_ak_temp_alloc_defs_8h_source.html#l00078) 行定义.