# bDebugStandaloneAllocs

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [TempAlloc](namespace_a_k_1_1_temp_alloc.html)
- [InitSettings](struct_a_k_1_1_temp_alloc_1_1_init_settings.html)

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [bDebugClearMemory](struct_a_k_1_1_temp_alloc_1_1_init_settings_a6d1a7c2066385c5d98c3b8e198267a16.html#a6d1a7c2066385c5d98c3b8e198267a16) | | [bDebugDetailedStats](struct_a_k_1_1_temp_alloc_1_1_init_settings_a03e19747bfa243389cdd6d6f9e13f2a0.html#a03e19747bfa243389cdd6d6f9e13f2a0) | | [bDebugEnableSentinels](struct_a_k_1_1_temp_alloc_1_1_init_settings_a76625e926d53a8d79283411bbc2cc9dd.html#a76625e926d53a8d79283411bbc2cc9dd) | | [bDebugFlushBlocks](struct_a_k_1_1_temp_alloc_1_1_init_settings_a7e3484c294f840bd4052f1ba8a5a376c.html#a7e3484c294f840bd4052f1ba8a5a376c) | | [bDebugStandaloneAllocs](struct_a_k_1_1_temp_alloc_1_1_init_settings_aa96cd186984f5a81e72a66ab723e0f5e.html#aa96cd186984f5a81e72a66ab723e0f5e) | | [uMaximumUnusedBlocks](struct_a_k_1_1_temp_alloc_1_1_init_settings_a0869a066e6830c5665538f01ef3c9033.html#a0869a066e6830c5665538f01ef3c9033) | | [uMinimumBlockCount](struct_a_k_1_1_temp_alloc_1_1_init_settings_a2f1fb0fceeb796d39542cc3cd1f3d1fa.html#a2f1fb0fceeb796d39542cc3cd1f3d1fa) | | [uMinimumBlockSize](struct_a_k_1_1_temp_alloc_1_1_init_settings_aaa251de5c00ef8acbf3be694b4d60c6f.html#aaa251de5c00ef8acbf3be694b4d60c6f) | | [◆](#aa96cd186984f5a81e72a66ab723e0f5e)bDebugStandaloneAllocs |  | | --- | | bool AK::TempAlloc::InitSettings::bDebugStandaloneAllocs |  Enable to force the block size to be as small as possible for each allocation (smaller than can be achieved by just setting uMinimumBlockSize to very low values). Useful to investigate memory overruns in-depth, especially in conjunction with other options like bDebugFlushBlocks and the [MemoryMgr](namespace_a_k_1_1_memory_mgr.html)'s stomp allocator. If enabled, bDebugDetailedStats and bDebugEnableSentinels will be disabled. Greatly increases CPU and memory usage.  在文件 [AkTempAllocDefs.h](_ak_temp_alloc_defs_8h_source.html) 第 [88](_ak_temp_alloc_defs_8h_source.html#l00088) 行定义. |