# Host.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)
- [V1](dir_10937d581a95c323ab8a50394190447e.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[函数](#func-members)

Host.h 文件参考

Wwise Authoring Plug-ins - API to request host's current state and services.
[更多...](#details)

`#include "../PlatformID.h"`  
`#include "../PluginInfoGenerator.h"`

[浏览源代码.](_v1_2_host_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_v1](structak__wwise__plugin__host__v1.html) |
|  | API to request host's current state and services. [更多...](structak__wwise__plugin__host__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_host\_v1](structak__wwise__plugin__notifications__host__v1.html) |
|  | API to receive host's update notifications. [更多...](structak__wwise__plugin__notifications__host__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::HostBase< CHostT, interface\_version >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base.html) |
|  | API to request host's current state and services. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::Notifications::Host\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host__.html) |
|  | API to receive host's update notifications. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host__.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::Notifications::Host\_::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___1_1_interface.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< V1::Host >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_v1_1_1_host_01_4.html) |
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
|  | [AK::Wwise::Plugin::V1::Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html) |
|  | [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html "Notifications namespace") namespace |
|  | |
|  | [AK::Wwise::Plugin::Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_V1\_ID](_v1_2_host_8h_a334e2d408897f931ea29fb28c61e9c71.html#a334e2d408897f931ea29fb28c61e9c71)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af1c18a159e804b70aa8e3bafd53ccfe1), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_V1\_CTOR](_v1_2_host_8h_a9a364c6e0e4fb6c5337c81ba6d3b3249.html#a9a364c6e0e4fb6c5337c81ba6d3b3249)() |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_HOST\_V1\_ID](_v1_2_host_8h_acbd95f3c8b720e054cd75d34c60d05a7.html#acbd95f3c8b720e054cd75d34c60d05a7)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_HOST](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a39cce7a5d163d7e82aac57807a80e831), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_HOST\_V1\_CTOR](_v1_2_host_8h_aac6bb3cfef4af5767b2b57eeaaf9dcc0.html#aac6bb3cfef4af5767b2b57eeaaf9dcc0)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CHost](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_aa4a7e1a93cadbaa4c6804a5a5c663024.html#aa4a7e1a93cadbaa4c6804a5a5c663024) = [ak\_wwise\_plugin\_host\_v1](structak__wwise__plugin__host__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::Host](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a9d626a275c527c46df80b121bcb34187.html#a9d626a275c527c46df80b121bcb34187) = HostBase<> |
|  | |
| using | [AK::Wwise::Plugin::V1::Notifications::CHost\_](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_ad7d03c0e80f9c244a614e8d23f160599.html#ad7d03c0e80f9c244a614e8d23f160599) = [ak\_wwise\_plugin\_notifications\_host\_v1](structak__wwise__plugin__notifications__host__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestHost](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a065857a76d9d90a1b2d3c0175a40ef3c.html#a065857a76d9d90a1b2d3c0175a40ef3c) = RequestedHostInterface< Host > |
|  | Requests a Host interface, provided as m\_host variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a065857a76d9d90a1b2d3c0175a40ef3c.html#a065857a76d9d90a1b2d3c0175a40ef3c) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::CCHost](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a041d8c3b6699783c1be6971e10bc2c23.html#a041d8c3b6699783c1be6971e10bc2c23) = V1::Notifications::Host\_ |
|  | Latest version of the C Host notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a041d8c3b6699783c1be6971e10bc2c23.html#a041d8c3b6699783c1be6971e10bc2c23) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::Host](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a6dff5e61f3799bce1119112cfc8da5d2.html#a6dff5e61f3799bce1119112cfc8da5d2) = V1::Notifications::Host\_ |
|  | Latest version of the C++ Host notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a6dff5e61f3799bce1119112cfc8da5d2.html#a6dff5e61f3799bce1119112cfc8da5d2) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ab8aebd300ad4e0655eeacf4af0ee5ab2.html#ab8aebd300ad4e0655eeacf4af0ee5ab2) (V1::Host) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a90773f41f32b15879c680faf4c9727fa.html#a90773f41f32b15879c680faf4c9727fa) (Notifications::Host) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_afaedc58d039beb0d0b02f1c4241ebfeb.html#afaedc58d039beb0d0b02f1c4241ebfeb) (Notifications::Host) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API to request host's current state and services.

在文件 [Host.h](_v1_2_host_8h_source.html) 中定义.