# uMaximumUnusedBlocks

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [TempAlloc](namespace_a_k_1_1_temp_alloc.html)
- [InitSettings](struct_a_k_1_1_temp_alloc_1_1_init_settings.html)

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [bDebugClearMemory](struct_a_k_1_1_temp_alloc_1_1_init_settings_a6d1a7c2066385c5d98c3b8e198267a16.html#a6d1a7c2066385c5d98c3b8e198267a16) | | [bDebugDetailedStats](struct_a_k_1_1_temp_alloc_1_1_init_settings_a03e19747bfa243389cdd6d6f9e13f2a0.html#a03e19747bfa243389cdd6d6f9e13f2a0) | | [bDebugEnableSentinels](struct_a_k_1_1_temp_alloc_1_1_init_settings_a76625e926d53a8d79283411bbc2cc9dd.html#a76625e926d53a8d79283411bbc2cc9dd) | | [bDebugFlushBlocks](struct_a_k_1_1_temp_alloc_1_1_init_settings_a7e3484c294f840bd4052f1ba8a5a376c.html#a7e3484c294f840bd4052f1ba8a5a376c) | | [bDebugStandaloneAllocs](struct_a_k_1_1_temp_alloc_1_1_init_settings_aa96cd186984f5a81e72a66ab723e0f5e.html#aa96cd186984f5a81e72a66ab723e0f5e) | | [uMaximumUnusedBlocks](struct_a_k_1_1_temp_alloc_1_1_init_settings_a0869a066e6830c5665538f01ef3c9033.html#a0869a066e6830c5665538f01ef3c9033) | | [uMinimumBlockCount](struct_a_k_1_1_temp_alloc_1_1_init_settings_a2f1fb0fceeb796d39542cc3cd1f3d1fa.html#a2f1fb0fceeb796d39542cc3cd1f3d1fa) | | [uMinimumBlockSize](struct_a_k_1_1_temp_alloc_1_1_init_settings_aaa251de5c00ef8acbf3be694b4d60c6f.html#aaa251de5c00ef8acbf3be694b4d60c6f) | | [◆](#a0869a066e6830c5665538f01ef3c9033)uMaximumUnusedBlocks |  | | --- | | [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) AK::TempAlloc::InitSettings::uMaximumUnusedBlocks |  The maximum number of blocks that the system keeps in an unused state, and avoids freeing. Defaults to 1. Higher values do not increase the peak memory use, but do prevent unused memory from being freed, in order to reduce creation and destruction of memory blocks.  在文件 [AkTempAllocDefs.h](_ak_temp_alloc_defs_8h_source.html) 第 [82](_ak_temp_alloc_defs_8h_source.html#l00082) 行定义. |