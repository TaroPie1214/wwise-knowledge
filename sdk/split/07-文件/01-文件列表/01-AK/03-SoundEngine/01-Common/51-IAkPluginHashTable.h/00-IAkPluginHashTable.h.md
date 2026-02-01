# IAkPluginHashTable.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[函数](#func-members)

IAkPluginHashTable.h 文件参考

`#include <type_traits>`  
`#include <AK/SoundEngine/Common/AkAudioObject.h>`  
`#include <AK/SoundEngine/Common/AkHashTableTypes.h>`  
`#include <AK/SoundEngine/Common/AkHashTableFuncs.h>`  
`#include <AK/SoundEngine/Common/IAkPlugin.h>`  
`#include <AK/Tools/Common/AkMurMurHash.h>`  
`#include <AK/Tools/Common/AkPlacementNew.h>`

[浏览源代码.](_i_ak_plugin_hash_table_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AK::IAkPluginServiceHashTable](class_a_k_1_1_i_ak_plugin_service_hash_table.html) |
|  | |
| struct | [AK::AkAudioObjectBuffer](struct_a_k_1_1_ak_audio_object_buffer.html) |
|  | A common hashtable for mapping audioobjectIds to a combination of audio buffers and objects [更多...](struct_a_k_1_1_ak_audio_object_buffer.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_GET\_PLUGIN\_SERVICE\_HASHTABLE](_i_ak_plugin_hash_table_8h_a251aca0e25ad9844865b48329621f2e6.html#a251aca0e25ad9844865b48329621f2e6)(plugin\_ctx)   static\_cast<[AK::IAkPluginServiceHashTable](class_a_k_1_1_i_ak_plugin_service_hash_table.html)\*>(plugin\_ctx->GetPluginService([AK::PluginServiceType\_HashTable](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a997d534c2263e1c8f7726f6e038d46d2))) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AK::AkHashTable](struct_a_k_1_1_ak_hash_table.html)< [AkAudioObjectID](_ak_typedefs_8h_a6cadc0376ae4f945438db69f6306f21a.html#a6cadc0376ae4f945438db69f6306f21a), AkAudioObjectBuffer > | [AK::AkAudioObjectBufferMap](namespace_a_k_ad5c73f45b229df23e84b6dc3d46a04da.html#ad5c73f45b229df23e84b6dc3d46a04da) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [AK::GetObjectChannelHash](namespace_a_k_a29351f59ac25ccfa5ee886ae55826647.html#a29351f59ac25ccfa5ee886ae55826647) ([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uAudioObjectId, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uChannelIdx) |
|  | Common hash function for getting a unique hash for a channel on an audio object [更多...](namespace_a_k_a29351f59ac25ccfa5ee886ae55826647.html#a29351f59ac25ccfa5ee886ae55826647) |
|  | |

## 详细描述

Plug-in interface for HashTable

在文件 [IAkPluginHashTable.h](_i_ak_plugin_hash_table_8h_source.html) 中定义.