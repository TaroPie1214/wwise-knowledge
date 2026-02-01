# HostPropertySet.h

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

HostPropertySet.h 文件参考

Wwise Authoring Plug-ins - Plug-in API for property sets.
[更多...](#details)

`#include "../PluginInfoGenerator.h"`

[浏览源代码.](_v1_2_host_property_set_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_property\_set\_v1](structak__wwise__plugin__host__property__set__v1.html) |
|  | Interface used to interact with property sets. [更多...](structak__wwise__plugin__host__property__set__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1.html) |
|  | |
| class | [AK.Wwise::Plugin::V1::PropertySetBase< CHostPropertySetT, interface\_version >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base.html) |
|  | Interface used to interact with property sets. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::Notifications::PropertySet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set__.html) |
|  | |
| struct | [AK.Wwise::Plugin::V1::Notifications::PropertySet\_::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< V1::PropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_v1_1_1_property_set_01_4.html) |
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
| #define | [AK\_WWISE\_PLUGIN\_HOST\_PROPERTY\_SET\_V1\_ID](_v1_2_host_property_set_8h_aa3a22242d5e70320ffb4a310b7cb7032.html#aa3a22242d5e70320ffb4a310b7cb7032)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_PROPERTY\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a76f67f330dab04093a4600d4d63d4446), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_PROPERTY\_SET\_V1\_CTOR](_v1_2_host_property_set_8h_a425b295f1e4f50cbbcae9a4884173428.html#a425b295f1e4f50cbbcae9a4884173428)() |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_PROPERTY\_SET\_V1\_ID](_v1_2_host_property_set_8h_ada07021c5bec8fcde9e1346455af82fa.html#ada07021c5bec8fcde9e1346455af82fa)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_PROPERTY\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a8393a83801f2e47851845c2d09b71659), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_PROPERTY\_SET\_V1\_CTOR](_v1_2_host_property_set_8h_ad04c8776057339e23d350a2ae033a057.html#ad04c8776057339e23d350a2ae033a057)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CHostPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a977c67b76548703aa34a942c0afd0e58.html#a977c67b76548703aa34a942c0afd0e58) = [ak\_wwise\_plugin\_host\_property\_set\_v1](structak__wwise__plugin__host__property__set__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ab5503ef97167a06c2b7d7be5c043d081.html#ab5503ef97167a06c2b7d7be5c043d081) = PropertySetBase<> |
|  | |
| using | [AK::Wwise::Plugin::V1::Notifications::CPropertySet\_](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_af1d2d2929ef640622dec4421e1c756e9.html#af1d2d2929ef640622dec4421e1c756e9) = [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a262b0abc85c3e066bb046298432c46e3.html#a262b0abc85c3e066bb046298432c46e3) = RequestedHostInterface< PropertySet > |
|  | Requests a PropertySet interface, provided as m\_propertySet variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a262b0abc85c3e066bb046298432c46e3.html#a262b0abc85c3e066bb046298432c46e3) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::CPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a08e89308b48732c29148f85fe12d1310.html#a08e89308b48732c29148f85fe12d1310) = V1::Notifications::CPropertySet\_ |
|  | Latest version of the C PropertySet notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a08e89308b48732c29148f85fe12d1310.html#a08e89308b48732c29148f85fe12d1310) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ac1ebce6cd84c63ffb93e086d46cbd7f8.html#ac1ebce6cd84c63ffb93e086d46cbd7f8) = V1::Notifications::PropertySet\_ |
|  | Latest version of the C++ PropertySet notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ac1ebce6cd84c63ffb93e086d46cbd7f8.html#ac1ebce6cd84c63ffb93e086d46cbd7f8) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_adb5842e5c4c9a1e04a53e64c8f6a14e3.html#adb5842e5c4c9a1e04a53e64c8f6a14e3) (V1::PropertySet) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a7737ab85f831030bbff061276168fd6f.html#a7737ab85f831030bbff061276168fd6f) (Notifications::PropertySet) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a1a3fd520310dbed80d8c6fc0bc1c639b.html#a1a3fd520310dbed80d8c6fc0bc1c639b) (Notifications::PropertySet) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Plug-in API for property sets.

在文件 [HostPropertySet.h](_v1_2_host_property_set_8h_source.html) 中定义.