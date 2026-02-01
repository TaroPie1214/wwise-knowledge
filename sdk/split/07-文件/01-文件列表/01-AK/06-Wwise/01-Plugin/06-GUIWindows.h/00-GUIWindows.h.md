# GUIWindows.h

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
[函数](#func-members) |
[变量](#var-members)

GUIWindows.h 文件参考

Wwise Authoring Plug-ins - Windows frontend plug-in API for Audio plug-ins.
[更多...](#details)

`#include "AudioPlugin.h"`

[浏览源代码.](_g_u_i_windows_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_gui\_windows\_v1](structak__wwise__plugin__gui__windows__v1.html) |
|  | Windows frontend plug-in API for Audio plug-ins. [更多...](structak__wwise__plugin__gui__windows__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::GUIWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.html) |
|  | Windows frontend plug-in API for Audio plug-ins. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::GUIWindows::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_1_1_interface.html#details) |
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
| #define | [AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_BEGIN\_POPULATE\_TABLE](_g_u_i_windows_8h_ace7e697c1d8a310c9794cf05ce8ce1d8.html#ace7e697c1d8a310c9794cf05ce8ce1d8)(theName)   [AK::Wwise::Plugin::PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html) theName[] = { |
|  | Starts a new property-control bindings table. [更多...](_g_u_i_windows_8h_ace7e697c1d8a310c9794cf05ce8ce1d8.html#ace7e697c1d8a310c9794cf05ce8ce1d8) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_POP\_ITEM](_g_u_i_windows_8h_af6140142c9fe6ff132aee5ad0fde1caf.html#af6140142c9fe6ff132aee5ad0fde1caf)(theID, theProp)   {theID, theProp }, |
|  | Declares an association between a control and a property within a property-control bindings table. [更多...](_g_u_i_windows_8h_af6140142c9fe6ff132aee5ad0fde1caf.html#af6140142c9fe6ff132aee5ad0fde1caf) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_END\_POPULATE\_TABLE](_g_u_i_windows_8h_a286a575e82a4a1b002ff737b186d4c76.html#a286a575e82a4a1b002ff737b186d4c76)()   [AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_POP\_ITEM](_g_u_i_windows_8h_af6140142c9fe6ff132aee5ad0fde1caf.html#af6140142c9fe6ff132aee5ad0fde1caf)(0, NULL) }; |
|  | Ends the declaration of a property-control bindings table. [更多...](_g_u_i_windows_8h_a286a575e82a4a1b002ff737b186d4c76.html#a286a575e82a4a1b002ff737b186d4c76) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_ID](_g_u_i_windows_8h_a1c0bbba0015c10e703cc23c0281658f0.html#a1c0bbba0015c10e703cc23c0281658f0)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_GUI\_WINDOWS](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af55117f741b99ad4a3d7eb6668dc8efe), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_CTOR](_g_u_i_windows_8h_aad8523cb0c751e53114cbac34067c061.html#aad8523cb0c751e53114cbac34067c061)(in\_pluginInfo, in\_data) |
|  | |
| #define | [WM\_AK\_PRIVATE\_SHOW\_HELP\_TOPIC](_g_u_i_windows_8h_ab81845f4c56463f65fdbc6c4712ea9a4.html#ab81845f4c56463f65fdbc6c4712ea9a4)   0x4981 |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CGUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_afd79a3a4b81bc5601ec3e2223bcd8974.html#afd79a3a4b81bc5601ec3e2223bcd8974) = [ak\_wwise\_plugin\_gui\_windows\_v1](structak__wwise__plugin__gui__windows__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::CGUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_ab13f5dbcc6517ad4c728d74301996232.html#ab13f5dbcc6517ad4c728d74301996232) = V1::CGUIWindows |
|  | Latest version of the C GUIWindows interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ab13f5dbcc6517ad4c728d74301996232.html#ab13f5dbcc6517ad4c728d74301996232) |
|  | |
| using | [AK::Wwise::Plugin::GUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_a5d74c88aa83c4e608fb75d1ac5555c9b.html#a5d74c88aa83c4e608fb75d1ac5555c9b) = V1::GUIWindows |
|  | Latest version of the C++ GUIWindows interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a5d74c88aa83c4e608fb75d1ac5555c9b.html#a5d74c88aa83c4e608fb75d1ac5555c9b) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a60ee146ea530ccf391bdad675091f24d.html#a60ee146ea530ccf391bdad675091f24d) (GUIWindows) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a4b75e53ecef29425a5b033bc257e7082.html#a4b75e53ecef29425a5b033bc257e7082) (GUIWindows) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| IMAGE\_DOS\_HEADER | [\_\_ImageBase](_g_u_i_windows_8h_a983773bd0fac8b545d479971ff56db4d.html#a983773bd0fac8b545d479971ff56db4d) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Windows frontend plug-in API for Audio plug-ins.

在文件 [GUIWindows.h](_g_u_i_windows_8h_source.html) 中定义.