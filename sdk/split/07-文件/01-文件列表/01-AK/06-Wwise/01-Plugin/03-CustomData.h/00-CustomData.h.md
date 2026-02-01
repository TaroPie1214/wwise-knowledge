# CustomData.h

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

CustomData.h 文件参考

Wwise Authoring Plug-ins - Backend API to load and save custom data in XML format.
[更多...](#details)

`#include "HostXml.h"`  
`#include "HostDataWriter.h"`

[浏览源代码.](_custom_data_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_custom\_data\_v1](structak__wwise__plugin__custom__data__v1.html) |
|  | Backend API to load and save custom data in XML format. [更多...](structak__wwise__plugin__custom__data__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::CustomData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.html) |
|  | Backend API to load and save custom data in XML format. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::CustomData::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_1_1_interface.html) |
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
| #define | [AK\_WWISE\_PLUGIN\_CUSTOM\_DATA\_V1\_ID](_custom_data_8h_a1dd149ef470912a30c08aa27ee8359e5.html#a1dd149ef470912a30c08aa27ee8359e5)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_CUSTOM\_DATA](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a866bd5f3bddd5bde6067ddc08ff882aa), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_CUSTOM\_DATA\_V1\_CTOR](_custom_data_8h_a712aaf49fd35cd0964197ad4ccb66180.html#a712aaf49fd35cd0964197ad4ccb66180)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CCustomData](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_af298eb6c35ed254f6b2b75b2df0ff39a.html#af298eb6c35ed254f6b2b75b2df0ff39a) = [ak\_wwise\_plugin\_custom\_data\_v1](structak__wwise__plugin__custom__data__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::CCustomData](namespace_a_k_1_1_wwise_1_1_plugin_a49cd878c81e427439d7e606515774bf7.html#a49cd878c81e427439d7e606515774bf7) = V1::CCustomData |
|  | Latest version of the C CustomData interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a49cd878c81e427439d7e606515774bf7.html#a49cd878c81e427439d7e606515774bf7) |
|  | |
| using | [AK::Wwise::Plugin::CustomData](namespace_a_k_1_1_wwise_1_1_plugin_ac1f7b957043934f47d294ecd2d71d0ca.html#ac1f7b957043934f47d294ecd2d71d0ca) = V1::CustomData |
|  | Latest version of the C++ CustomData interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ac1f7b957043934f47d294ecd2d71d0ca.html#ac1f7b957043934f47d294ecd2d71d0ca) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_aa4b2c7dcf92adb095fb6a83278a3c1fb.html#aa4b2c7dcf92adb095fb6a83278a3c1fb) (CustomData) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ac14b35b70e189aa7fdce95fea8684ca0.html#ac14b35b70e189aa7fdce95fea8684ca0) (CustomData) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Backend API to load and save custom data in XML format.

在文件 [CustomData.h](_custom_data_8h_source.html) 中定义.