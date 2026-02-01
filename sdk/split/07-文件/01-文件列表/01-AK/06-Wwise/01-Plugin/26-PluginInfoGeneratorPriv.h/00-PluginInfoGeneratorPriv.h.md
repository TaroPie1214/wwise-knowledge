# PluginInfoGeneratorPriv.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[命名空间](#namespaces) |
[宏定义](#define-members) |
[函数](#func-members)

PluginInfoGeneratorPriv.h 文件参考

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_plugin_info_generator_priv_8h_source.html)

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
| #define | [AK\_ADD\_FRONTEND\_PLUGIN\_CLASS\_TO\_CONTAINER](_plugin_info_generator_priv_8h_aa1a96f91771f45b44b65c7da26e14c8b.html#aa1a96f91771f45b44b65c7da26e14c8b)(ContainerName, WwiseClassName, AudioEngineRegisteredName, TemplateName) |
|  | (C++) Adds a Wwise Authoring frontend plug-in and a Sound Engine plug-in to a plug-in container. [更多...](_plugin_info_generator_priv_8h_aa1a96f91771f45b44b65c7da26e14c8b.html#aa1a96f91771f45b44b65c7da26e14c8b) |
|  | |
| #define | [AK\_ADD\_FRONTEND\_PLUGIN\_CLASSID\_TO\_CONTAINER](_plugin_info_generator_priv_8h_a2f60a565690ef631fec423828961aaff.html#a2f60a565690ef631fec423828961aaff)(ContainerName, WwiseClassName, CompanyID, PluginID, Type, TemplateName) |
|  | (C++) Adds a Wwise Authoring frontend plug-in to a plug-in container. [更多...](_plugin_info_generator_priv_8h_a2f60a565690ef631fec423828961aaff.html#a2f60a565690ef631fec423828961aaff) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| void | [AK::Wwise::Plugin::V1::AssignFrontendModelArgs](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a0176401da1ab1b06f7d197cdab007447.html#a0176401da1ab1b06f7d197cdab007447) ([AK::Wwise::Plugin::PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823) &io\_pluginInfo, [ak\_wwise\_plugin\_host\_frontend\_model\_args\_v1](structak__wwise__plugin__host__frontend__model__args__v1.html) \*in\_args) |
|  | Assign arguments for the [FrontendModel](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model.html "Interface used to interact with the frontend model.") service request [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a0176401da1ab1b06f7d197cdab007447.html#a0176401da1ab1b06f7d197cdab007447) |
|  | |