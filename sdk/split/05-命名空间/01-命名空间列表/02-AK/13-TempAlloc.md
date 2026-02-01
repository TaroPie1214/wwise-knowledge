# TempAlloc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [TempAlloc](namespace_a_k_1_1_temp_alloc.html)

[类](#nested-classes)

AK::TempAlloc 命名空间参考

|  |  |
| --- | --- |
| 类 | |
| struct | [InitSettings](struct_a_k_1_1_temp_alloc_1_1_init_settings.html) |
|  | |
| struct | [Stats](struct_a_k_1_1_temp_alloc_1_1_stats.html) |
|  | |

|  |  |
| --- | --- |
| TempAlloc systems | |
| enum | [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9) { [Type\_AudioRender](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9a53147f87306352fff3f6f4800999bda2), [Type\_NUM](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9a4b1e87ec36a0ff9c1a4039f8928c4bc2) } |
|  | IDs of temporary memory pools used by the sound engine. [更多...](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9) |
|  | |
| enum | [Lifetime](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229) { [Lifetime\_CurrentTick](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229ac6deb77098680329c5a963ce3e55a0e8) = 0, [Lifetime\_DoubleTick](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229acdbfc7e9b87b1c22727154e2efb73757) = 1, [Lifetime\_NUM](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229a7c0847e69ff3e236b789e67345b38fc7) } |
|  | Lifetimes of temporary allocations available. [更多...](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [GetStats](namespace_a_k_1_1_temp_alloc_a685fc3e0a2b3ade4c442a848979274e9.html#a685fc3e0a2b3ade4c442a848979274e9) ([Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9) in\_eType, [Stats](struct_a_k_1_1_temp_alloc_1_1_stats.html) &out\_stats) |
|  | Get simple statistics for a given temporary-memory pool [更多...](namespace_a_k_1_1_temp_alloc_a685fc3e0a2b3ade4c442a848979274e9.html#a685fc3e0a2b3ade4c442a848979274e9) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [DumpTempAllocsToFile](namespace_a_k_1_1_temp_alloc_ad7ca1e1f7b04720475c801ce21e1d50e.html#ad7ca1e1f7b04720475c801ce21e1d50e) ([Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9) in\_eType, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*pszFilename) |
|  | |

## 详细描述

[TempAlloc](namespace_a_k_1_1_temp_alloc.html) namespace.

备注
:   The functions in this namespace are thread-safe, unless stated otherwise.

参见
:   - [调节 Temp Alloc 内存](goingfurther_optimizingmempools_reducing_memory.html#goingfurther_optimizingmempools_tempallocs)