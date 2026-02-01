# Source.h

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

Source.h 文件参考

Wwise Authoring Plug-ins - API specific for source plug-in.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_source_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_source\_v1](structak__wwise__plugin__source__v1.html) |
|  | API specific for source plug-in. [更多...](structak__wwise__plugin__source__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::Source](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source.html) |
|  | [Wwise](namespace_a_k_1_1_wwise.html) API for general Audio Plug-in's backend. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::Source::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface.html#details) |
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
| #define | [AK\_WWISE\_PLUGIN\_SOURCE\_V1\_ID](_source_8h_a3bd12aa21014e48d9e45317996746c35.html#a3bd12aa21014e48d9e45317996746c35)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SOURCE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a8d2a79ba3f9d7006fee4a710c35a2623), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_SOURCE\_V1\_CTOR](_source_8h_ac8ed9807d7646326535fa3d492e1cea9.html#ac8ed9807d7646326535fa3d492e1cea9)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CSource](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a348aca37a6ae52b1c250d85ad45261d4.html#a348aca37a6ae52b1c250d85ad45261d4) = [ak\_wwise\_plugin\_source\_v1](structak__wwise__plugin__source__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::CSource](namespace_a_k_1_1_wwise_1_1_plugin_a38b3d2f1d2482266ceb25c024375134c.html#a38b3d2f1d2482266ceb25c024375134c) = V1::CSource |
|  | Latest version of the C Source interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a38b3d2f1d2482266ceb25c024375134c.html#a38b3d2f1d2482266ceb25c024375134c) |
|  | |
| using | [AK::Wwise::Plugin::Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af) = V1::Source |
|  | Latest version of the C++ Source interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ab1c3fdbee20d7c500864d497a485ddd3.html#ab1c3fdbee20d7c500864d497a485ddd3) (Source) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ad743420fa3f22b37ac4fdb363c7e5ca1.html#ad743420fa3f22b37ac4fdb363c7e5ca1) (Source) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API specific for source plug-in.

在文件 [Source.h](_source_8h_source.html) 中定义.