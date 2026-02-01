# HostObjectStore.h

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

HostObjectStore.h 文件参考

Wwise Authoring Plug-ins - API for storing objects not in the plug-in XML.
[更多...](#details)

`#include "HostPropertySet.h"`

[浏览源代码.](_host_object_store_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html) |
|  | Custom inner property set interface. [更多...](structak__wwise__plugin__host__object__store__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_object\_store\_v1](structak__wwise__plugin__notifications__object__store__v1.html) |
|  | Interface able to receive notifications for custom inner property sets. [更多...](structak__wwise__plugin__notifications__object__store__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::ObjectStore< PropertySetT >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.html) |
|  | Custom inner property set interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__.html) |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html "The C interface, fulfilled by your plug-in.") able to receive notifications for custom inner property sets. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT >::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< ObjectStore >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_store_01_4.html) |
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
| #define | [AK\_WWISE\_PLUGIN\_HOST\_OBJECT\_STORE\_V1\_ID](_host_object_store_8h_a4ddc0395c34a03f56cfa13f5c35b3715.html#a4ddc0395c34a03f56cfa13f5c35b3715)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_OBJECT\_STORE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a548777b0657519d6b6e634574170c29f), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_OBJECT\_STORE\_V1\_CTOR](_host_object_store_8h_abc13c44580ff64ac1c518c2451e288f1.html#abc13c44580ff64ac1c518c2451e288f1)() |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_OBJECT\_STORE\_V1\_ID](_host_object_store_8h_a73ba87a321004d2c009801193b145d33.html#a73ba87a321004d2c009801193b145d33)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_OBJECT\_STORE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a257b8a3c00de2195a4d19871830f93cd), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_OBJECT\_STORE\_V1\_CTOR](_host_object_store_8h_ab01fe0feb6de91a18caf471786e0299a.html#ab01fe0feb6de91a18caf471786e0299a)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CHostObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a47bf77f6f1de2492c10a8788039f1a08.html#a47bf77f6f1de2492c10a8788039f1a08) = [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::Notifications::CObjectStore\_](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_a920997360030af683efd6525a010063b.html#a920997360030af683efd6525a010063b) = [ak\_wwise\_plugin\_notifications\_object\_store\_v1](structak__wwise__plugin__notifications__object__store__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestObjectStore\_PropertySet\_v1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ad9598cf0b1a6c02f5f8b2e63017c986d.html#ad9598cf0b1a6c02f5f8b2e63017c986d) = RequestedHostInterface< ObjectStore< [AK::Wwise::Plugin::V1::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ab5503ef97167a06c2b7d7be5c043d081.html#ab5503ef97167a06c2b7d7be5c043d081) > > |
|  | Requests an [ObjectStore](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.html "Custom inner property set interface.") interface, provided as m\_objectStore variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ad9598cf0b1a6c02f5f8b2e63017c986d.html#ad9598cf0b1a6c02f5f8b2e63017c986d) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestObjectStore\_PropertySet\_v2](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a2da36a8b8d8e3905225648968c262dfe.html#a2da36a8b8d8e3905225648968c262dfe) = RequestedHostInterface< ObjectStore< [AK::Wwise::Plugin::V2::PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html) > > |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a1ffe19f6268c48cb9afae1996296714f.html#a1ffe19f6268c48cb9afae1996296714f) = RequestObjectStore\_PropertySet\_v2 |
|  | |
| using | [AK::Wwise::Plugin::CHostObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_adaab29f68e9ece2d4649c56f52c53e96.html#adaab29f68e9ece2d4649c56f52c53e96) = V1::CHostObjectStore |
|  | Latest version of the C ObjectStore interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_adaab29f68e9ece2d4649c56f52c53e96.html#adaab29f68e9ece2d4649c56f52c53e96) |
|  | |
| using | [AK::Wwise::Plugin::ObjectStore\_PropertySet\_v1](namespace_a_k_1_1_wwise_1_1_plugin_ac634cf28c4a943245fb6e127758cc02f.html#ac634cf28c4a943245fb6e127758cc02f) = V1::ObjectStore< [AK::Wwise::Plugin::V1::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ab5503ef97167a06c2b7d7be5c043d081.html#ab5503ef97167a06c2b7d7be5c043d081) > |
|  | Latest version of the C++ ObjectStore interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ac634cf28c4a943245fb6e127758cc02f.html#ac634cf28c4a943245fb6e127758cc02f) |
|  | |
| using | [AK::Wwise::Plugin::ObjectStore\_PropertySet\_v2](namespace_a_k_1_1_wwise_1_1_plugin_ad0bd3a3df770388385fa7d803d25941e.html#ad0bd3a3df770388385fa7d803d25941e) = V1::ObjectStore< [AK::Wwise::Plugin::V2::PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html) > |
|  | |
| using | [AK::Wwise::Plugin::ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_aa1a4c71b6a4959d8e06f9e3cc976c749.html#aa1a4c71b6a4959d8e06f9e3cc976c749) = ObjectStore\_PropertySet\_v2 |
|  | |
| using | [AK::Wwise::Plugin::RequestObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_aa75f21542f68316133473c611537a0b9.html#aa75f21542f68316133473c611537a0b9) = V1::RequestObjectStore |
|  | Latest version of the requested C++ ObjectStore interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aa75f21542f68316133473c611537a0b9.html#aa75f21542f68316133473c611537a0b9) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::CObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a5ce01ed7dd9d15ec8560793c86dcb0aa.html#a5ce01ed7dd9d15ec8560793c86dcb0aa) = V1::Notifications::CObjectStore\_ |
|  | Latest version of the C ObjectStore notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a5ce01ed7dd9d15ec8560793c86dcb0aa.html#a5ce01ed7dd9d15ec8560793c86dcb0aa) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::ObjectStore\_PropertySet\_v1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a388ab7c68c38eabe29f955f95c3500b7.html#a388ab7c68c38eabe29f955f95c3500b7) = V1::Notifications::ObjectStore\_< [AK::Wwise::Plugin::V1::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ab5503ef97167a06c2b7d7be5c043d081.html#ab5503ef97167a06c2b7d7be5c043d081) > |
|  | Latest version of the C++ ObjectStore notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a388ab7c68c38eabe29f955f95c3500b7.html#a388ab7c68c38eabe29f955f95c3500b7) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::ObjectStore\_PropertySet\_v2](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a0b707a3512a44d0c6063d8ad75690f0c.html#a0b707a3512a44d0c6063d8ad75690f0c) = V1::Notifications::ObjectStore\_< [AK::Wwise::Plugin::V2::PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html) > |
|  | |
| using | [AK::Wwise::Plugin::Notifications::ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ac1426dcd81fe89e4e0d7d40abd92eb88.html#ac1426dcd81fe89e4e0d7d40abd92eb88) = ObjectStore\_PropertySet\_v2 |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ad2eee5be97fa2bc4a8fb3af43eee867a.html#ad2eee5be97fa2bc4a8fb3af43eee867a) (ObjectStore) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ab53d90190847b24b30f0c2fef6d36080.html#ab53d90190847b24b30f0c2fef6d36080) (ObjectStore) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_aff7d0fdb394787aa869eeedd82b22bcd.html#aff7d0fdb394787aa869eeedd82b22bcd) (Notifications::ObjectStore) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a1491ed0e88c4ec9dac22da4b27bb0279.html#a1491ed0e88c4ec9dac22da4b27bb0279) (Notifications::ObjectStore) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API for storing objects not in the plug-in XML.

在文件 [HostObjectStore.h](_host_object_store_8h_source.html) 中定义.