# HostFrontendModel.h

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

HostFrontendModel.h 文件参考

Wwise Authoring Plug-ins - Plug-in API for the Frontend Model.
[更多...](#details)

`#include "PluginInfoGenerator.h"`  
`#include "PluginDef.h"`

[浏览源代码.](_host_frontend_model_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_frontend\_model\_v1](structak__wwise__plugin__host__frontend__model__v1.html) |
|  | Interface used to interact with the frontend model. [更多...](structak__wwise__plugin__host__frontend__model__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::FrontendModel](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model.html) |
|  | Interface used to interact with the frontend model. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< FrontendModel >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4.html) |
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
| #define | [AK\_WWISE\_PLUGIN\_HOST\_FRONTEND\_MODEL\_V1\_ID](_host_frontend_model_8h_aa49900f308c7e15f9a40465753dbd249.html#aa49900f308c7e15f9a40465753dbd249)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_FRONTEND\_MODEL](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a59544c57eb30361f5a4df4f25fe8ca2a), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_FRONTEND\_MODEL\_V1\_CTOR](_host_frontend_model_8h_a38f35871bdc86944b6417befea78a48c.html#a38f35871bdc86944b6417befea78a48c)() |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CHostFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a427443c428bc8db3bcdda5fff6a5fe4a.html#a427443c428bc8db3bcdda5fff6a5fe4a) = [ak\_wwise\_plugin\_host\_frontend\_model\_v1](structak__wwise__plugin__host__frontend__model__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a04cfe873a10a643f151a6717375312cf.html#a04cfe873a10a643f151a6717375312cf) = RequestedHostInterface< FrontendModel > |
|  | Requests a [FrontendModel](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model.html "Interface used to interact with the frontend model.") interface, provided as m\_frontendModel variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a04cfe873a10a643f151a6717375312cf.html#a04cfe873a10a643f151a6717375312cf) |
|  | |
| using | [AK::Wwise::Plugin::CHostFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_af24a3f1547c57009739461b422fb7a90.html#af24a3f1547c57009739461b422fb7a90) = V1::CHostFrontendModel |
|  | Latest version of the C FrontendModel interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af24a3f1547c57009739461b422fb7a90.html#af24a3f1547c57009739461b422fb7a90) |
|  | |
| using | [AK::Wwise::Plugin::FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb) = V1::FrontendModel |
|  | Latest version of the C++ FrontendModel interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb) |
|  | |
| using | [AK::Wwise::Plugin::RequestFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a08800f5f1455eee4531b3ffa1b8fbf7a.html#a08800f5f1455eee4531b3ffa1b8fbf7a) = V1::RequestFrontendModel |
|  | Latest version of the requested C++ FrontendModel interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a08800f5f1455eee4531b3ffa1b8fbf7a.html#a08800f5f1455eee4531b3ffa1b8fbf7a) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a673a63aed65f792e4a29546d85b723ad.html#a673a63aed65f792e4a29546d85b723ad) (FrontendModel) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a3e2415c2500d0ce4cd77034397be568e.html#a3e2415c2500d0ce4cd77034397be568e) (FrontendModel) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Plug-in API for the Frontend Model.

在文件 [HostFrontendModel.h](_host_frontend_model_8h_source.html) 中定义.