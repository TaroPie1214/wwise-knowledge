# PropertyDisplayName.h

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

PropertyDisplayName.h 文件参考

Wwise Authoring Plug-ins - Plug-in API for property display name.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_property_display_name_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_property\_display\_name\_v1](structak__wwise__plugin__property__display__name__v1.html) |
|  | Backend API to specify display names for properties [更多...](structak__wwise__plugin__property__display__name__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::PropertyDisplayName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name.html) |
|  | |
| struct | [AK.Wwise::Plugin::V1::PropertyDisplayName::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface.html#details) |
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
| #define | [AK\_WWISE\_PLUGIN\_PROPERTY\_DISPLAY\_NAME\_V1\_ID](_property_display_name_8h_a8387de9f4dbe74021f8e4ca32bfc06f6.html#a8387de9f4dbe74021f8e4ca32bfc06f6)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PROPERTY\_DISPLAY\_NAME](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af99e8cd163b565d2cc56a3822dec423d), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_PROPERTY\_DISPLAY\_NAME\_V1\_CTOR](_property_display_name_8h_a2d8da25c167e0b5b0bc207889246fc64.html#a2d8da25c167e0b5b0bc207889246fc64)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CPropertyDisplayName](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_aee3bc6e9d3c6b81eb81096cadcb95a50.html#aee3bc6e9d3c6b81eb81096cadcb95a50) = [ak\_wwise\_plugin\_property\_display\_name\_v1](structak__wwise__plugin__property__display__name__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::CPropertyDisplayName](namespace_a_k_1_1_wwise_1_1_plugin_a874928bdb5e2c0fccdf1e0c50c1041f3.html#a874928bdb5e2c0fccdf1e0c50c1041f3) = V1::CPropertyDisplayName |
|  | Latest version of the C PropertyDisplayName interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a874928bdb5e2c0fccdf1e0c50c1041f3.html#a874928bdb5e2c0fccdf1e0c50c1041f3) |
|  | |
| using | [AK::Wwise::Plugin::PropertyDisplayName](namespace_a_k_1_1_wwise_1_1_plugin_a6f10eb912f168dc570304ae3ee97ec6f.html#a6f10eb912f168dc570304ae3ee97ec6f) = V1::PropertyDisplayName |
|  | Latest version of the C++ PropertyDisplayName interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a6f10eb912f168dc570304ae3ee97ec6f.html#a6f10eb912f168dc570304ae3ee97ec6f) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ab95897d57921201fca57bb3d49bd3a4f.html#ab95897d57921201fca57bb3d49bd3a4f) (PropertyDisplayName) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a76d46caf648ca01da735fb573ae63f00.html#a76d46caf648ca01da735fb573ae63f00) (PropertyDisplayName) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Plug-in API for property display name.

在文件 [PropertyDisplayName.h](_property_display_name_8h_source.html) 中定义.