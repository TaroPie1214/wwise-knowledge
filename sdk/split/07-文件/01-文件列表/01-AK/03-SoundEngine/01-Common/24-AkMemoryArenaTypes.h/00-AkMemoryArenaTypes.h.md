# AkMemoryArenaTypes.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[类型定义](#typedef-members) |
[变量](#var-members)

AkMemoryArenaTypes.h 文件参考

`#include <AK/SoundEngine/Common/AkSoundEngineExport.h>`  
`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_ak_memory_arena_types_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AK::MemoryArena::AkMemoryArenaSettings](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::MemoryArena](namespace_a_k_1_1_memory_arena.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef void \*(\* | [AkAllocSpan](_ak_memory_arena_types_8h_a21bcd69577908bb71252c552e67d39c1.html#a21bcd69577908bb71252c552e67d39c1)) (size\_t in\_uSize, size\_t \*out\_userData) |
|  | |
| typedef void(\* | [AkFreeSpan](_ak_memory_arena_types_8h_ac356630f9618ee1879296eedc1ea2efd.html#ac356630f9618ee1879296eedc1ea2efd)) (void \*in\_pAddress, size\_t in\_uSize, size\_t in\_userData) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK::MemoryArena::kMemoryArenaSize](namespace_a_k_1_1_memory_arena_a0cce863b31862bdcdc6d1da1523b4917.html#a0cce863b31862bdcdc6d1da1523b4917) = 8192 |
|  | |
| const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK::MemoryArena::kMemoryArenaSpanOverhead](namespace_a_k_1_1_memory_arena_ada200fa0219fcccc914ead1ec646ba7c.html#ada200fa0219fcccc914ead1ec646ba7c) = 64 |
|  | |

## 详细描述

namespace for handling Wwise internal memory arena.

在文件 [AkMemoryArenaTypes.h](_ak_memory_arena_types_8h_source.html) 中定义.