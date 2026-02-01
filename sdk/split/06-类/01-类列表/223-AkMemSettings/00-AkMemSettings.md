# AkMemSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_mem_settings-members.html)

AkMemSettings结构体 参考

`#include <AkMemoryMgrModule.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| High-level memory allocation hooks. When not NULL, redirect allocations normally forwarded to internal memory systems. | |
| [AkMemInitForThread](_ak_memory_mgr_module_8h_a8eb2200ee7ce4f8fd9163c4ef920c660.html#a8eb2200ee7ce4f8fd9163c4ef920c660) | [pfInitForThread](struct_ak_mem_settings_a64de7db44eeaaf01011d473529667b7d.html#a64de7db44eeaaf01011d473529667b7d) |
|  | (Optional) Thread-specific allocator initialization hook. [更多...](struct_ak_mem_settings_a64de7db44eeaaf01011d473529667b7d.html#a64de7db44eeaaf01011d473529667b7d) |
|  | |
| [AkMemTermForThread](_ak_memory_mgr_module_8h_a382c6e27bfdb1ef0f86f27469242ff31.html#a382c6e27bfdb1ef0f86f27469242ff31) | [pfTermForThread](struct_ak_mem_settings_adec2f9a28716236a5e1b2c7a258b8c6e.html#adec2f9a28716236a5e1b2c7a258b8c6e) |
|  | (Optional) Thread-specific allocator termination hook. [更多...](struct_ak_mem_settings_adec2f9a28716236a5e1b2c7a258b8c6e.html#adec2f9a28716236a5e1b2c7a258b8c6e) |
|  | |
| [AkMemTrimForThread](_ak_memory_mgr_module_8h_a18902debaee9178ca56951d96c11cdee.html#a18902debaee9178ca56951d96c11cdee) | [pfTrimForThread](struct_ak_mem_settings_afbf907696820f2fd30f88af36620bdd8.html#afbf907696820f2fd30f88af36620bdd8) |
|  | (Optional) Thread-specific allocator "trimming" hook. Used to relinquish memory resources when threads enter a period of inactivity. [更多...](struct_ak_mem_settings_afbf907696820f2fd30f88af36620bdd8.html#afbf907696820f2fd30f88af36620bdd8) |
|  | |
| [AkMemMalloc](_ak_memory_mgr_module_8h_a029efc97dac467b5a32c05f5a98a0be9.html#a029efc97dac467b5a32c05f5a98a0be9) | [pfMalloc](struct_ak_mem_settings_a7b0974f6f5480a8fd549d5350b960079.html#a7b0974f6f5480a8fd549d5350b960079) |
|  | (Optional) Memory allocation hook. [更多...](struct_ak_mem_settings_a7b0974f6f5480a8fd549d5350b960079.html#a7b0974f6f5480a8fd549d5350b960079) |
|  | |
| [AkMemMalign](_ak_memory_mgr_module_8h_aee41c8e4dcb40ccf365164f92833520a.html#aee41c8e4dcb40ccf365164f92833520a) | [pfMalign](struct_ak_mem_settings_a71352af10d5b691094fb319ab5e36b38.html#a71352af10d5b691094fb319ab5e36b38) |
|  | (Optional) Memory allocation hook. [更多...](struct_ak_mem_settings_a71352af10d5b691094fb319ab5e36b38.html#a71352af10d5b691094fb319ab5e36b38) |
|  | |
| [AkMemRealloc](_ak_memory_mgr_module_8h_a5953a53e49ecf87aa7b27c16d772d41a.html#a5953a53e49ecf87aa7b27c16d772d41a) | [pfRealloc](struct_ak_mem_settings_a6ccdc83c31c9dfdc5b9d22423bd7aee9.html#a6ccdc83c31c9dfdc5b9d22423bd7aee9) |
|  | (Optional) Memory allocation hook. [更多...](struct_ak_mem_settings_a6ccdc83c31c9dfdc5b9d22423bd7aee9.html#a6ccdc83c31c9dfdc5b9d22423bd7aee9) |
|  | |
| [AkMemReallocAligned](_ak_memory_mgr_module_8h_a86749afaecf1e9e68d6f8a3b62499b87.html#a86749afaecf1e9e68d6f8a3b62499b87) | [pfReallocAligned](struct_ak_mem_settings_ac0d8bbabfbffec67ddf03f66602137b3.html#ac0d8bbabfbffec67ddf03f66602137b3) |
|  | (Optional) Memory allocation hook. [更多...](struct_ak_mem_settings_ac0d8bbabfbffec67ddf03f66602137b3.html#ac0d8bbabfbffec67ddf03f66602137b3) |
|  | |
| [AkMemFree](_ak_memory_mgr_module_8h_ac6982afe3d12d5af12af319d7c80d411.html#ac6982afe3d12d5af12af319d7c80d411) | [pfFree](struct_ak_mem_settings_a3acf39bd77470f4b6adf8441b5f8ddd2.html#a3acf39bd77470f4b6adf8441b5f8ddd2) |
|  | (Optional) Memory allocation hook. [更多...](struct_ak_mem_settings_a3acf39bd77470f4b6adf8441b5f8ddd2.html#a3acf39bd77470f4b6adf8441b5f8ddd2) |
|  | |
| [AkMemTotalReservedMemorySize](_ak_memory_mgr_module_8h_ad18caa43a0995ec341bd0100d2424ac5.html#ad18caa43a0995ec341bd0100d2424ac5) | [pfTotalReservedMemorySize](struct_ak_mem_settings_ad1f86b301a24dceb8622a9ee74466bcb.html#ad1f86b301a24dceb8622a9ee74466bcb) |
|  | (Optional) Memory allocation statistics hook. [更多...](struct_ak_mem_settings_ad1f86b301a24dceb8622a9ee74466bcb.html#ad1f86b301a24dceb8622a9ee74466bcb) |
|  | |
| [AkMemSizeOfMemory](_ak_memory_mgr_module_8h_a7226b7b4a72db37bae1e2c5e0998adf2.html#a7226b7b4a72db37bae1e2c5e0998adf2) | [pfSizeOfMemory](struct_ak_mem_settings_a27eaf83daea702267d7d71e734cba836.html#a27eaf83daea702267d7d71e734cba836) |
|  | (Optional) Memory allocation statistics hook. [更多...](struct_ak_mem_settings_a27eaf83daea702267d7d71e734cba836.html#a27eaf83daea702267d7d71e734cba836) |
|  | |
| Configuration. | |
| [AK::MemoryArena::AkMemoryArenaSettings](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings.html) | [memoryArenaSettings](struct_ak_mem_settings_ad938c0122f4ed866a1ae1c459812d597.html#ad938c0122f4ed866a1ae1c459812d597) [[AkMemoryMgrArena\_NUM](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4ca6d04cd32dae8081d7af43611f5f67ab6)] |
|  | Configuration of memory arenas for default memory allocator. For more information, see [AkMemoryArena 的配置和调整](goingfurther_memoryarenas.html). [更多...](struct_ak_mem_settings_ad938c0122f4ed866a1ae1c459812d597.html#ad938c0122f4ed866a1ae1c459812d597) |
|  | |
| [AK::TempAlloc::InitSettings](struct_a_k_1_1_temp_alloc_1_1_init_settings.html) | [tempAllocSettings](struct_ak_mem_settings_a45ed232810c97cc3a71146dc449881ff.html#a45ed232810c97cc3a71146dc449881ff) [[AK::TempAlloc::Type\_NUM](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9a4b1e87ec36a0ff9c1a4039f8928c4bc2)] |
|  | Configuration of behavior for the temporary-memory pools. For more information, see [调节 Temp Alloc 内存](goingfurther_optimizingmempools_reducing_memory.html#goingfurther_optimizingmempools_tempallocs). [更多...](struct_ak_mem_settings_a45ed232810c97cc3a71146dc449881ff.html#a45ed232810c97cc3a71146dc449881ff) |
|  | |
| [AK::BookmarkAlloc::InitSettings](struct_a_k_1_1_bookmark_alloc_1_1_init_settings.html) | [bookmarkAllocSettings](struct_ak_mem_settings_a4b579106e81604c7842ec6ae262a00ff.html#a4b579106e81604c7842ec6ae262a00ff) |
|  | Configuration of behavior for the bookmark-allocated memory. For more information, see [调节 Bookmark Allocator 内存](goingfurther_optimizingmempools_reducing_memory.html#goingfurther_optimizingmempools_bookmarkalloc). [更多...](struct_ak_mem_settings_a4b579106e81604c7842ec6ae262a00ff.html#a4b579106e81604c7842ec6ae262a00ff) |
|  | |
| Memory allocation debugging. | |
| [AkMemDebugMalloc](_ak_memory_mgr_module_8h_a868d7cb6a8696f0254f572959fa8058f.html#a868d7cb6a8696f0254f572959fa8058f) | [pfDebugMalloc](struct_ak_mem_settings_aa7ad0e0dd66eaf23d3721301fc516be6.html#aa7ad0e0dd66eaf23d3721301fc516be6) |
|  | (Optional) Memory allocation debugging hook. Used for tracking calls to pfMalloc. [更多...](struct_ak_mem_settings_aa7ad0e0dd66eaf23d3721301fc516be6.html#aa7ad0e0dd66eaf23d3721301fc516be6) |
|  | |
| [AkMemDebugMalign](_ak_memory_mgr_module_8h_a0007c7fcd5e73e862d2338123ec46d97.html#a0007c7fcd5e73e862d2338123ec46d97) | [pfDebugMalign](struct_ak_mem_settings_ab590383aaeabbb4d198151f9041f7517.html#ab590383aaeabbb4d198151f9041f7517) |
|  | (Optional) Memory allocation debugging hook. Used for tracking calls to pfMalign. [更多...](struct_ak_mem_settings_ab590383aaeabbb4d198151f9041f7517.html#ab590383aaeabbb4d198151f9041f7517) |
|  | |
| [AkMemDebugRealloc](_ak_memory_mgr_module_8h_ae82460c988c5e6eb441b905447fa8fc9.html#ae82460c988c5e6eb441b905447fa8fc9) | [pfDebugRealloc](struct_ak_mem_settings_ad1a6c086b143f9a84de67a552b2a63dd.html#ad1a6c086b143f9a84de67a552b2a63dd) |
|  | (Optional) Memory allocation debugging hook. Used for tracking calls to pfRealloc. [更多...](struct_ak_mem_settings_ad1a6c086b143f9a84de67a552b2a63dd.html#ad1a6c086b143f9a84de67a552b2a63dd) |
|  | |
| [AkMemDebugReallocAligned](_ak_memory_mgr_module_8h_abea2c80bd6bfbcfd82ffcfe3ca3ffea4.html#abea2c80bd6bfbcfd82ffcfe3ca3ffea4) | [pfDebugReallocAligned](struct_ak_mem_settings_ac7c193c97ce96bcfac624e98c941c681.html#ac7c193c97ce96bcfac624e98c941c681) |
|  | (Optional) Memory allocation debugging hook. Used for tracking calls to pfReallocAligned. [更多...](struct_ak_mem_settings_ac7c193c97ce96bcfac624e98c941c681.html#ac7c193c97ce96bcfac624e98c941c681) |
|  | |
| [AkMemDebugFree](_ak_memory_mgr_module_8h_aac6a537e02b9f4d99c0de1cba128f70c.html#aac6a537e02b9f4d99c0de1cba128f70c) | [pfDebugFree](struct_ak_mem_settings_ac50c4db30282223a2de087fc2d40b88c.html#ac50c4db30282223a2de087fc2d40b88c) |
|  | (Optional) Memory allocation debugging hook. Used for tracking calls to pfFree. [更多...](struct_ak_mem_settings_ac50c4db30282223a2de087fc2d40b88c.html#ac50c4db30282223a2de087fc2d40b88c) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMemoryDebugLevel](struct_ak_mem_settings_ae97967db68ec10e8410af9f776f89e0d.html#ae97967db68ec10e8410af9f776f89e0d) |
|  | Default 0 disabled. 1 debug enabled. 2 stomp allocator enabled. 3 stomp allocator and debug enabled. User implementations may use multiple non-zero values to offer different features. [更多...](struct_ak_mem_settings_ae97967db68ec10e8410af9f776f89e0d.html#ae97967db68ec10e8410af9f776f89e0d) |
|  | |

## 详细描述

Initialization settings for the default implementation of the Memory Manager. For more details, see [初始化](memorymanager.html#memorymanager_init).

参见
:   [AK::MemoryMgr](namespace_a_k_1_1_memory_mgr.html)

在文件 [AkMemoryMgrModule.h](_ak_memory_mgr_module_8h_source.html) 第 [148](_ak_memory_mgr_module_8h_source.html#l00148) 行定义.