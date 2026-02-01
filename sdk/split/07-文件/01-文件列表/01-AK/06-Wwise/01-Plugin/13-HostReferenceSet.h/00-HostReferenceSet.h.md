# HostReferenceSet.h

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

HostReferenceSet.h 文件参考

Wwise Authoring Plug-ins - Plug-in API for reference sets.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_host_reference_set_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_reference\_set\_v1](structak__wwise__plugin__host__reference__set__v1.html) |
|  | Interface used to interact with reference sets. [更多...](structak__wwise__plugin__host__reference__set__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_reference\_set\_v1](structak__wwise__plugin__notifications__reference__set__v1.html) |
|  | |
| class | [AK.Wwise::Plugin::ReferenceSetBase< CHostReferenceSetT, interface\_version >](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base.html) |
|  | Interface used to interact with reference sets. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base.html#details) |
|  | |
| class | [AK.Wwise::Plugin::Notifications::ReferenceSet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set__.html) |
|  | |
| struct | [AK.Wwise::Plugin::Notifications::ReferenceSet\_::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< ReferenceSet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4.html) |
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
|  | [AK::Wwise::Plugin::Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_REFERENCE\_SET\_V1\_ID](_host_reference_set_8h_a65c7fb7ee8c78ce10a642bd58d9d462e.html#a65c7fb7ee8c78ce10a642bd58d9d462e)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_REFERENCE\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aaebf595516f8a6f606ec4f08c12d8175), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_REFERENCE\_SET\_V1\_CTOR](_host_reference_set_8h_ab6e1477823399cddc2e6726a454402bd.html#ab6e1477823399cddc2e6726a454402bd)() |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_REFERENCE\_SET\_V1\_ID](_host_reference_set_8h_ae2622db4bc11cb2bdfdcb41e5253c30e.html#ae2622db4bc11cb2bdfdcb41e5253c30e)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_REFERENCE\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aea11355fbccff969a4def18261402dc5), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_REFERENCE\_SET\_V1\_CTOR](_host_reference_set_8h_af22460484815a339686e69c17789c52b.html#af22460484815a339686e69c17789c52b)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::CHostReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_a536d3a045013fa219001b7b005112feb.html#a536d3a045013fa219001b7b005112feb) = [ak\_wwise\_plugin\_host\_reference\_set\_v1](structak__wwise__plugin__host__reference__set__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_aa9c66805a7050040225bb144c6be8d06.html#aa9c66805a7050040225bb144c6be8d06) = ReferenceSetBase<> |
|  | |
| using | [AK::Wwise::Plugin::Notifications::CReferenceSet\_](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a9cb59fa54f180f0fa26606333ac5fecc.html#a9cb59fa54f180f0fa26606333ac5fecc) = [ak\_wwise\_plugin\_notifications\_reference\_set\_v1](structak__wwise__plugin__notifications__reference__set__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::RequestReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_af440c5da9f9765a6b9518ea8b7c3f2c1.html#af440c5da9f9765a6b9518ea8b7c3f2c1) = RequestedHostInterface< ReferenceSet > |
|  | Requests a ReferenceSet interface, provided as m\_referenceSet variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af440c5da9f9765a6b9518ea8b7c3f2c1.html#af440c5da9f9765a6b9518ea8b7c3f2c1) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::CReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a0bb873d00dc91eb6f93261f409e4a1c9.html#a0bb873d00dc91eb6f93261f409e4a1c9) = Notifications::CReferenceSet\_ |
|  | Latest version of the C ReferenceSet notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a0bb873d00dc91eb6f93261f409e4a1c9.html#a0bb873d00dc91eb6f93261f409e4a1c9) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ae433979cbee5cd9d8ca01fe22da6b377.html#ae433979cbee5cd9d8ca01fe22da6b377) = Notifications::ReferenceSet\_ |
|  | Latest version of the C++ ReferenceSet notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ae433979cbee5cd9d8ca01fe22da6b377.html#ae433979cbee5cd9d8ca01fe22da6b377) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ac83b7f21da2872e6ec16079f4c5d3e0e.html#ac83b7f21da2872e6ec16079f4c5d3e0e) (ReferenceSet) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a14f5142bd4cf5ca1badadcd692a49f12.html#a14f5142bd4cf5ca1badadcd692a49f12) (Notifications::ReferenceSet) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a5b3707f2b2686106b16b1fa472228562.html#a5b3707f2b2686106b16b1fa472228562) (Notifications::ReferenceSet) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Plug-in API for reference sets.

在文件 [HostReferenceSet.h](_host_reference_set_8h_source.html) 中定义.