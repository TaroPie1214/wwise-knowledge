# AkTempAllocDefs.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces)

AkTempAllocDefs.h 文件参考

`#include <AK/SoundEngine/Common/AkSoundEngineExport.h>`  
`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_ak_temp_alloc_defs_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AK::TempAlloc::Stats](struct_a_k_1_1_temp_alloc_1_1_stats.html) |
|  | |
| struct | [AK::TempAlloc::InitSettings](struct_a_k_1_1_temp_alloc_1_1_init_settings.html) |
|  | |
| struct | [AK::BookmarkAlloc::Stats](struct_a_k_1_1_bookmark_alloc_1_1_stats.html) |
|  | |
| struct | [AK::BookmarkAlloc::InitSettings](struct_a_k_1_1_bookmark_alloc_1_1_init_settings.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::TempAlloc](namespace_a_k_1_1_temp_alloc.html) |
|  | |
|  | [AK::BookmarkAlloc](namespace_a_k_1_1_bookmark_alloc.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| BookmarkAlloc systems | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::BookmarkAlloc::GetStats](namespace_a_k_1_1_bookmark_alloc_a78703377dee103f212b970697b44b38f.html#a78703377dee103f212b970697b44b38f) (Stats &out\_stats) |
|  | Get simple statistics for the Bookmark allocator [更多...](namespace_a_k_1_1_bookmark_alloc_a78703377dee103f212b970697b44b38f.html#a78703377dee103f212b970697b44b38f) |
|  | |

|  |  |
| --- | --- |
| TempAlloc systems | |
| enum | [AK::TempAlloc::Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9) { [AK::TempAlloc::Type\_AudioRender](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9a53147f87306352fff3f6f4800999bda2), [AK::TempAlloc::Type\_NUM](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9a4b1e87ec36a0ff9c1a4039f8928c4bc2) } |
|  | IDs of temporary memory pools used by the sound engine. [更多...](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9) |
|  | |
| enum | [AK::TempAlloc::Lifetime](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229) { [AK::TempAlloc::Lifetime\_CurrentTick](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229ac6deb77098680329c5a963ce3e55a0e8) = 0, [AK::TempAlloc::Lifetime\_DoubleTick](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229acdbfc7e9b87b1c22727154e2efb73757) = 1, [AK::TempAlloc::Lifetime\_NUM](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229a7c0847e69ff3e236b789e67345b38fc7) } |
|  | Lifetimes of temporary allocations available. [更多...](namespace_a_k_1_1_temp_alloc_a9e133fbbb2e0cc473595ce3cf83c2229.html#a9e133fbbb2e0cc473595ce3cf83c2229) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::TempAlloc::GetStats](namespace_a_k_1_1_temp_alloc_a685fc3e0a2b3ade4c442a848979274e9.html#a685fc3e0a2b3ade4c442a848979274e9) (Type in\_eType, Stats &out\_stats) |
|  | Get simple statistics for a given temporary-memory pool [更多...](namespace_a_k_1_1_temp_alloc_a685fc3e0a2b3ade4c442a848979274e9.html#a685fc3e0a2b3ade4c442a848979274e9) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::TempAlloc::DumpTempAllocsToFile](namespace_a_k_1_1_temp_alloc_ad7ca1e1f7b04720475c801ce21e1d50e.html#ad7ca1e1f7b04720475c801ce21e1d50e) (Type in\_eType, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*pszFilename) |
|  | |

## 详细描述

namespace for handling temp-allocations (incl. stack allocs)

在文件 [AkTempAllocDefs.h](_ak_temp_alloc_defs_8h_source.html) 中定义.