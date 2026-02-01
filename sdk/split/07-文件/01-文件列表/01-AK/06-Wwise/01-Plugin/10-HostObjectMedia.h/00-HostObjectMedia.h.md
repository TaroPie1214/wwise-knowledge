# HostObjectMedia.h

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

HostObjectMedia.h 文件参考

Wwise Authoring Plug-ins - API for retrieving and handling data files, as used in the plug-in.
[更多...](#details)

`#include "PluginInfoGenerator.h"`  
`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_host_object_media_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_object\_media\_v1](structak__wwise__plugin__host__object__media__v1.html) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_object\_media\_v1](structak__wwise__plugin__notifications__object__media__v1.html) |
|  | |
| class | [AK.Wwise::Plugin::V1::ObjectMedia](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media.html) |
|  | |
| class | [AK.Wwise::Plugin::V1::Notifications::ObjectMedia\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media__.html) |
|  | |
| struct | [AK.Wwise::Plugin::V1::Notifications::ObjectMedia\_::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___1_1_interface.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< ObjectMedia >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_media_01_4.html) |
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
| #define | [AK\_WWISE\_PLUGIN\_HOST\_OBJECT\_MEDIA\_V1\_ID](_host_object_media_8h_ac1711e7b846f977b6e285ddee827e192.html#ac1711e7b846f977b6e285ddee827e192)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_OBJECT\_MEDIA](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a123cdd811f15c89c6d15915c62fa0116), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_OBJECT\_MEDIA\_V1\_CTOR](_host_object_media_8h_a992c221848e9b3de30c1551905cbacd7.html#a992c221848e9b3de30c1551905cbacd7)() |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_OBJECT\_MEDIA\_V1\_ID](_host_object_media_8h_a77b0f14d42e7a52bdf746407cebf19dc.html#a77b0f14d42e7a52bdf746407cebf19dc)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_OBJECT\_MEDIA](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a3dad917a24d46fd680f342d8c6c299e8), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_OBJECT\_MEDIA\_V1\_CTOR](_host_object_media_8h_ad899ce0232267fdc29a0373b1a3e4283.html#ad899ce0232267fdc29a0373b1a3e4283)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CHostObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a8022609c599c92d28ea192e81b3175c6.html#a8022609c599c92d28ea192e81b3175c6) = [ak\_wwise\_plugin\_host\_object\_media\_v1](structak__wwise__plugin__host__object__media__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::Notifications::CObjectMedia\_](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_a473af17dd1b148efa108f7493f19904c.html#a473af17dd1b148efa108f7493f19904c) = [ak\_wwise\_plugin\_notifications\_object\_media\_v1](structak__wwise__plugin__notifications__object__media__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_abe0c5913cfd0cf4d76b48f46632d5aa3.html#abe0c5913cfd0cf4d76b48f46632d5aa3) = RequestedHostInterface< ObjectMedia > |
|  | Requests a [ObjectMedia](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media.html) interface, provided as m\_objectMedia variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_abe0c5913cfd0cf4d76b48f46632d5aa3.html#abe0c5913cfd0cf4d76b48f46632d5aa3) |
|  | |
| using | [AK::Wwise::Plugin::CHostObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a4a7fe49717628bdfda765fbaee107d7a.html#a4a7fe49717628bdfda765fbaee107d7a) = V1::CHostObjectMedia |
|  | Latest version of the C ObjectMedia interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4a7fe49717628bdfda765fbaee107d7a.html#a4a7fe49717628bdfda765fbaee107d7a) |
|  | |
| using | [AK::Wwise::Plugin::ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a0325d70f4523c31f1b4f5dc8acdf3e2b.html#a0325d70f4523c31f1b4f5dc8acdf3e2b) = V1::ObjectMedia |
|  | Latest version of the C++ ObjectMedia interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a0325d70f4523c31f1b4f5dc8acdf3e2b.html#a0325d70f4523c31f1b4f5dc8acdf3e2b) |
|  | |
| using | [AK::Wwise::Plugin::RequestObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a0d8a1c4d25d025d4614f072197956e60.html#a0d8a1c4d25d025d4614f072197956e60) = V1::RequestObjectMedia |
|  | Latest version of the requested C++ ObjectMedia interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a0d8a1c4d25d025d4614f072197956e60.html#a0d8a1c4d25d025d4614f072197956e60) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::CObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a5d6d5eb0e024a1947e5ba0f356df8d90.html#a5d6d5eb0e024a1947e5ba0f356df8d90) = V1::Notifications::CObjectMedia\_ |
|  | Latest version of the C ObjectMedia notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a5d6d5eb0e024a1947e5ba0f356df8d90.html#a5d6d5eb0e024a1947e5ba0f356df8d90) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ad0a911acd3094f2ebc4ba43d1421c16d.html#ad0a911acd3094f2ebc4ba43d1421c16d) = V1::Notifications::ObjectMedia\_ |
|  | Latest version of the C++ ObjectMedia notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ad0a911acd3094f2ebc4ba43d1421c16d.html#ad0a911acd3094f2ebc4ba43d1421c16d) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a96f3b71d458c24f10227c8e2fc9a0b49.html#a96f3b71d458c24f10227c8e2fc9a0b49) (ObjectMedia) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_af00a7debde2d2e2f857d567c1a9da843.html#af00a7debde2d2e2f857d567c1a9da843) (ObjectMedia) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_aebca6e7ac797d63f22d3895d81da5260.html#aebca6e7ac797d63f22d3895d81da5260) (Notifications::ObjectMedia) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a346b0c5c1520ea8c6f01c38357ba7fca.html#a346b0c5c1520ea8c6f01c38357ba7fca) (Notifications::ObjectMedia) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API for retrieving and handling data files, as used in the plug-in.

在文件 [HostObjectMedia.h](_host_object_media_8h_source.html) 中定义.