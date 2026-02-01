# MediaConverter.h

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

MediaConverter.h 文件参考

Wwise Authoring Plug-ins - API to convert used object medias to a format usable by the plug-in's Sound Engine part.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_media_converter_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_media\_converter\_v1](structak__wwise__plugin__media__converter__v1.html) |
|  | API to convert used object medias to a format usable by the plug-in's Sound Engine part. [更多...](structak__wwise__plugin__media__converter__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::MediaConverter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter.html) |
|  | |
| struct | [AK.Wwise::Plugin::V1::MediaConverter::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface.html#details) |
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
| #define | [AK\_WWISE\_PLUGIN\_MEDIA\_CONVERTER\_V1\_ID](_media_converter_8h_a49610bf2914022bd85df39a2e3fe389a.html#a49610bf2914022bd85df39a2e3fe389a)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_MEDIA\_CONVERTER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9acc6b762efd7653cabd05b42068cc7bc7), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_MEDIA\_CONVERTER\_V1\_CTOR](_media_converter_8h_a4ddca4c283375eb038f8d3180330ecab.html#a4ddca4c283375eb038f8d3180330ecab)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CMediaConverter](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a34d8135b75802c9013a7fcc885c29e17.html#a34d8135b75802c9013a7fcc885c29e17) = [ak\_wwise\_plugin\_media\_converter\_v1](structak__wwise__plugin__media__converter__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::CMediaConverter](namespace_a_k_1_1_wwise_1_1_plugin_aef95c4436b404946c77657144efac8bb.html#aef95c4436b404946c77657144efac8bb) = V1::CMediaConverter |
|  | Latest version of the C MediaConverter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aef95c4436b404946c77657144efac8bb.html#aef95c4436b404946c77657144efac8bb) |
|  | |
| using | [AK::Wwise::Plugin::MediaConverter](namespace_a_k_1_1_wwise_1_1_plugin_aca00f70c566ab8b103a983d07890f430.html#aca00f70c566ab8b103a983d07890f430) = V1::MediaConverter |
|  | Latest version of the C++ MediaConverter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aca00f70c566ab8b103a983d07890f430.html#aca00f70c566ab8b103a983d07890f430) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a4a5307fc7fed7f62ba82803278776355.html#a4a5307fc7fed7f62ba82803278776355) (MediaConverter) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a81949de0e066e835725453496d91f583.html#a81949de0e066e835725453496d91f583) (MediaConverter) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API to convert used object medias to a format usable by the plug-in's Sound Engine part.

在文件 [MediaConverter.h](_media_converter_8h_source.html) 中定义.