# IAkPluginServiceMeter.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members)

IAkPluginServiceMeter.h 文件参考

`#include <AK/SoundEngine/Common/AkCommonDefs.h>`  
`#include <AK/SoundEngine/Common/AkSpeakerConfig.h>`  
`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/SoundEngine/Common/IAkPlugin.h>`

[浏览源代码.](_i_ak_plugin_service_meter_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AK::IAkPluginServiceMeter](class_a_k_1_1_i_ak_plugin_service_meter.html) |
|  | Interface for the "Meter" plug-in service, to handle metering of signals in various ways [更多...](class_a_k_1_1_i_ak_plugin_service_meter.html#details) |
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
| #define | [AK\_GET\_PLUGIN\_SERVICE\_METER](_i_ak_plugin_service_meter_8h_ae4edbd42f0812f62e35f87d0f813e200.html#ae4edbd42f0812f62e35f87d0f813e200)(plugin\_ctx)   static\_cast<[AK::IAkPluginServiceMeter](class_a_k_1_1_i_ak_plugin_service_meter.html)\*>(plugin\_ctx->GetPluginService([AK::PluginServiceType\_Meter](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a822d77a52b3b7ccc17268be9f511034b))) |
|  | |

## 详细描述

Plug-in interface for accessing mixing-related functionality for plug-ins

在文件 [IAkPluginServiceMeter.h](_i_ak_plugin_service_meter_8h_source.html) 中定义.