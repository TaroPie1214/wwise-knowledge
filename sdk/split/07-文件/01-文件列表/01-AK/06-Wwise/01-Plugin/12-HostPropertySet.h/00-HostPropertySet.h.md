# HostPropertySet.h

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

HostPropertySet.h 文件参考

Wwise Authoring Plug-ins - Plug-in API for property sets.
[更多...](#details)

`#include "PluginInfoGenerator.h"`  
`#include "./V1/HostPropertySet.h"`

[浏览源代码.](_host_property_set_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_property\_set\_v2](structak__wwise__plugin__host__property__set__v2.html) |
|  | |
| class | [AK.Wwise::Plugin::V2::PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html) |
|  | Interface used to interact with property sets. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< PropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4.html) |
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
|  | [AK::Wwise::Plugin::V2](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_PROPERTY\_SET\_V2\_ID](_host_property_set_8h_af9668854445bdecfb496f44ad78b81d7.html#af9668854445bdecfb496f44ad78b81d7)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_PROPERTY\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a76f67f330dab04093a4600d4d63d4446), 2) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_PROPERTY\_SET\_V2\_CTOR](_host_property_set_8h_a1dfff4dc304904de9330231e79f22f11.html#a1dfff4dc304904de9330231e79f22f11)() |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V2::CHostPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_adadefb669a14a661a38960b441d2de02.html#adadefb669a14a661a38960b441d2de02) = [ak\_wwise\_plugin\_host\_property\_set\_v2](structak__wwise__plugin__host__property__set__v2.html) |
|  | |
| using | [AK::Wwise::Plugin::V2::RequestPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a75474e2ae58b9851b89d7ccd9a4fbcdf.html#a75474e2ae58b9851b89d7ccd9a4fbcdf) = RequestedHostInterface< PropertySet > |
|  | Requests a [PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html "Interface used to interact with property sets.") interface, provided as m\_propertySet variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a75474e2ae58b9851b89d7ccd9a4fbcdf.html#a75474e2ae58b9851b89d7ccd9a4fbcdf) |
|  | |
| using | [AK::Wwise::Plugin::CHostPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a485c72db20c02ae9f16af1baca14bde4.html#a485c72db20c02ae9f16af1baca14bde4) = V2::CHostPropertySet |
|  | Latest version of the C PropertySet interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a485c72db20c02ae9f16af1baca14bde4.html#a485c72db20c02ae9f16af1baca14bde4) |
|  | |
| using | [AK::Wwise::Plugin::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de) = V2::PropertySet |
|  | Latest version of the C++ PropertySet interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de) |
|  | |
| using | [AK::Wwise::Plugin::RequestPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a5eb9b772d01c414e7c77b44ef66e661f.html#a5eb9b772d01c414e7c77b44ef66e661f) = V2::RequestPropertySet |
|  | Latest version of the requested C++ PropertySet interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a5eb9b772d01c414e7c77b44ef66e661f.html#a5eb9b772d01c414e7c77b44ef66e661f) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_abb2cf51a8149e8b87c3176e0d6948df5.html#abb2cf51a8149e8b87c3176e0d6948df5) (PropertySet) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a86cd47ff2861e2907081e1efd2485e13.html#a86cd47ff2861e2907081e1efd2485e13) (PropertySet) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Plug-in API for property sets.

在文件 [HostPropertySet.h](_host_property_set_8h_source.html) 中定义.