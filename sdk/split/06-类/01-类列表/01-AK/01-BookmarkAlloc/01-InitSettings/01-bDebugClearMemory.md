# bDebugClearMemory

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [BookmarkAlloc](namespace_a_k_1_1_bookmark_alloc.html)
- [InitSettings](struct_a_k_1_1_bookmark_alloc_1_1_init_settings.html)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [bDebugClearMemory](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a78848d974865e0fdaf94944c8e5aee24.html#a78848d974865e0fdaf94944c8e5aee24) | | [bDebugDetailedStats](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a7b27d0bcea0ad9c36ed41c2e602168f0.html#a7b27d0bcea0ad9c36ed41c2e602168f0) | | [bDebugEnableSentinels](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a42b4d040a0a0685a786439ad0146769e.html#a42b4d040a0a0685a786439ad0146769e) | | [bDebugStandaloneAllocs](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_ac1e0b8831640622dd212fcd8b5f34589.html#ac1e0b8831640622dd212fcd8b5f34589) | | [uMaximumUnusedBlocks](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_ad4e70719eb5243ae4fdd8e833abf57b8.html#ad4e70719eb5243ae4fdd8e833abf57b8) | | [uMinimumBlockCount](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_a12c53c74a26531dd2210998cd259fb0a.html#a12c53c74a26531dd2210998cd259fb0a) | | [uMinimumBlockSize](struct_a_k_1_1_bookmark_alloc_1_1_init_settings_ad2444d4b53c747f71651d541a1b7fdb2.html#ad2444d4b53c747f71651d541a1b7fdb2) | | [◆](#a78848d974865e0fdaf94944c8e5aee24)bDebugClearMemory |  | | --- | | bool AK::BookmarkAlloc::InitSettings::bDebugClearMemory |  Enable to clear any allocation to a deterministic garbage value during allocs, and after the stack is rewound to a bookmark. Useful to make sure memory is initialized properly. Disabled by default.  在文件 [AkTempAllocDefs.h](_ak_temp_alloc_defs_8h_source.html) 第 [140](_ak_temp_alloc_defs_8h_source.html#l00140) 行定义. |