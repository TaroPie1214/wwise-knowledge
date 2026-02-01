# AudioPlugin.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[函数](#func-members)

AudioPlugin.h 文件参考

Wwise Authoring Plug-ins - API for general Audio Plug-in's backend (Source, Effect, Mixer).
[更多...](#details)

`#include "HostPropertySet.h"`  
`#include "HostDataWriter.h"`

[浏览源代码.](_audio_plugin_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_audio\_plugin\_v1](structak__wwise__plugin__audio__plugin__v1.html) |
|  | Wwise API for general Audio Plug-in's backend. [更多...](structak__wwise__plugin__audio__plugin__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html) |
|  | [Wwise](namespace_a_k_1_1_wwise.html) API for general Audio Plug-in's backend. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::AudioPlugin::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
| namespace | [AK.Wwise](namespace_a_k_1_1_wwise.html) |
|  | |
|  | [AK::Wwise::Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html) |
|  | |
|  | [AK::Wwise::Plugin::V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_AUDIO\_PLUGIN\_V1\_ID](_audio_plugin_8h_af21f7290225f823c30ea9bba6173c2ae.html#af21f7290225f823c30ea9bba6173c2ae)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_AUDIO\_PLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af60f00124117a22873d01c98255478ed), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_AUDIO\_PLUGIN\_V1\_CTOR](_audio_plugin_8h_adad5870da3ea5c8c619d71193d7cbf83.html#adad5870da3ea5c8c619d71193d7cbf83)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CAudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ae5b0d46ea918e3573f5efbd0f6d0b9d0.html#ae5b0d46ea918e3573f5efbd0f6d0b9d0) = [ak\_wwise\_plugin\_audio\_plugin\_v1](structak__wwise__plugin__audio__plugin__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::CAudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_a5b3913f268e5fae72c8a73a2e6f5ca53.html#a5b3913f268e5fae72c8a73a2e6f5ca53) = V1::CAudioPlugin |
|  | Latest version of the C AudioPlugin interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a5b3913f268e5fae72c8a73a2e6f5ca53.html#a5b3913f268e5fae72c8a73a2e6f5ca53) |
|  | |
| using | [AK::Wwise::Plugin::AudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_a989b8417cedde33d928b90171491fcc5.html#a989b8417cedde33d928b90171491fcc5) = V1::AudioPlugin |
|  | Latest version of the C++ AudioPlugin interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a989b8417cedde33d928b90171491fcc5.html#a989b8417cedde33d928b90171491fcc5) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_af0fc7e36e72cee4b416aecef62580074.html#af0fc7e36e72cee4b416aecef62580074) (AudioPlugin) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a6323c7c48b3e596a558fe5dfb0f74612.html#a6323c7c48b3e596a558fe5dfb0f74612) (AudioPlugin) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API for general Audio Plug-in's backend (Source, Effect, Mixer).

在文件 [AudioPlugin.h](_audio_plugin_8h_source.html) 中定义.