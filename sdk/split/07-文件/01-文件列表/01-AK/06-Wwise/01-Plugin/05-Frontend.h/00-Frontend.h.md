# Frontend.h

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

Frontend.h 文件参考

Wwise Authoring Plug-ins - Frontend plug-in API for Audio plug-ins.
[更多...](#details)

`#include "AudioPlugin.h"`  
`#include "HostFrontendModel.h"`

[浏览源代码.](_frontend_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_frontend\_v1](structak__wwise__plugin__frontend__v1.html) |
|  | Frontend plug-in API for Audio plug-ins. [更多...](structak__wwise__plugin__frontend__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html) |
|  | [Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html "Frontend plug-in API for Audio plug-ins.") plug-in API for Audio plug-ins. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::Frontend::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_1_1_interface.html#details) |
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
| #define | [AK\_WWISE\_PLUGIN\_FRONTEND\_ID](_frontend_8h_a32bc00a8cc712d46982d4c0e678727dd.html#a32bc00a8cc712d46982d4c0e678727dd)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FRONTEND](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aa58ee40b40c495300ba7b919da18bceb), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_FRONTEND\_CTOR](_frontend_8h_a2b043ca1ed0f2f05ceb7e88d6eb72299.html#a2b043ca1ed0f2f05ceb7e88d6eb72299)(in\_pluginInfo, in\_data) |
|  | |
| #define | [WM\_AK\_PRIVATE\_SHOW\_HELP\_TOPIC](_frontend_8h_ab81845f4c56463f65fdbc6c4712ea9a4.html#ab81845f4c56463f65fdbc6c4712ea9a4)   0x4981 |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CFrontend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_aefff5dbb0c5445942b31da2c4ea2e016.html#aefff5dbb0c5445942b31da2c4ea2e016) = [ak\_wwise\_plugin\_frontend\_v1](structak__wwise__plugin__frontend__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::CFrontend](namespace_a_k_1_1_wwise_1_1_plugin_a50e3966725bc51606e5e5200f42c7fb0.html#a50e3966725bc51606e5e5200f42c7fb0) = V1::CFrontend |
|  | Latest version of the C Frontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a50e3966725bc51606e5e5200f42c7fb0.html#a50e3966725bc51606e5e5200f42c7fb0) |
|  | |
| using | [AK::Wwise::Plugin::Frontend](namespace_a_k_1_1_wwise_1_1_plugin_ade7bf4707d85e10aae30ea0780abe527.html#ade7bf4707d85e10aae30ea0780abe527) = V1::Frontend |
|  | Latest version of the C++ Frontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ade7bf4707d85e10aae30ea0780abe527.html#ade7bf4707d85e10aae30ea0780abe527) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a27dc9d787fc7d362febc033146124b1a.html#a27dc9d787fc7d362febc033146124b1a) (Frontend) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a91c243b3733347886fb8b3c2e4d974f1.html#a91c243b3733347886fb8b3c2e4d974f1) (Frontend) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Frontend plug-in API for Audio plug-ins.

在文件 [Frontend.h](_frontend_8h_source.html) 中定义.