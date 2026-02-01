# IAkPluginTempAlloc.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members)

IAkPluginTempAlloc.h 文件参考

`#include <AK/SoundEngine/Common/IAkPlugin.h>`  
`#include <AK/SoundEngine/Common/IAkPluginMemAlloc.h>`

[浏览源代码.](_i_ak_plugin_temp_alloc_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AK::IAkPluginServiceTempAlloc](class_a_k_1_1_i_ak_plugin_service_temp_alloc.html) |
|  | |
| struct | [AK::PluginBookmarkAllocRegion](struct_a_k_1_1_plugin_bookmark_alloc_region.html) |
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
| #define | [AK\_GET\_PLUGIN\_SERVICE\_TEMPALLOC](_i_ak_plugin_temp_alloc_8h_aa92d94ec2912b3f1e3592c8783ea581b.html#aa92d94ec2912b3f1e3592c8783ea581b)(plugin\_ctx)   static\_cast<[AK::IAkPluginServiceTempAlloc](class_a_k_1_1_i_ak_plugin_service_temp_alloc.html)\*>(plugin\_ctx->GetPluginService([AK::PluginServiceType\_TempAlloc](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99aee6c7322e6ef27b9969c8ab43b3b07b4))) |
|  | |

## 详细描述

Plug-in interface for temp-alloc systems

在文件 [IAkPluginTempAlloc.h](_i_ak_plugin_temp_alloc_8h_source.html) 中定义.