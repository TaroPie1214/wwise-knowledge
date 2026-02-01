# PluginInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [ISourceControl](class_a_k_1_1_wwise_1_1_i_source_control.html)
- [PluginInfo](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info-members.html) |
[Public 属性](#pub-attribs)

AK.Wwise::ISourceControl::PluginInfo类 参考

Plug-in information structure. This structure gives a simple overview of the plug-in's capabilities.
[更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info.html#details)

`#include <ISourceControl.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| BSTR | [m\_bstrName](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a268ed5a98db68c7c5f992e8152525a8b.html#a268ed5a98db68c7c5f992e8152525a8b) |
|  | The name of the plug-in displayed in the Project Settings plug-in list [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a268ed5a98db68c7c5f992e8152525a8b.html#a268ed5a98db68c7c5f992e8152525a8b) |
|  | |
| unsigned int | [m\_uiVersion](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a65d2de9be85a5c323ac002bfa561f15a.html#a65d2de9be85a5c323ac002bfa561f15a) |
|  | The current version of the plug-in [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a65d2de9be85a5c323ac002bfa561f15a.html#a65d2de9be85a5c323ac002bfa561f15a) |
|  | |
| bool | [m\_bShowConfigDlgAvailable](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a8bbaffdff539c62271eba2e5ae4b2712.html#a8bbaffdff539c62271eba2e5ae4b2712) |
|  | Used to enable/disable the 'Config...' button in the Project Settings [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a8bbaffdff539c62271eba2e5ae4b2712.html#a8bbaffdff539c62271eba2e5ae4b2712) |
|  | |
| DWORD | [m\_dwUpdateCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a7d2aa2c074d59449d5f74f422f5dde64.html#a7d2aa2c074d59449d5f74f422f5dde64) |
|  | Indicates the command ID for the Update command, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a7d2aa2c074d59449d5f74f422f5dde64.html#a7d2aa2c074d59449d5f74f422f5dde64) |
|  | |
| DWORD | [m\_dwCommitCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_ac2df7944a19ae45494b06face30400bf.html#ac2df7944a19ae45494b06face30400bf) |
|  | Indicates the command ID for the Commit/Submit/Checkin command, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_ac2df7944a19ae45494b06face30400bf.html#ac2df7944a19ae45494b06face30400bf) |
|  | |
| DWORD | [m\_dwRenameCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_adfa06e905971c7b871d8acbd553d80aa.html#adfa06e905971c7b871d8acbd553d80aa) |
|  | Indicates the command ID for the Rename command, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_adfa06e905971c7b871d8acbd553d80aa.html#adfa06e905971c7b871d8acbd553d80aa) |
|  | |
| DWORD | [m\_dwMoveCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_aec77a60a22f4960b0e222e13a9583361.html#aec77a60a22f4960b0e222e13a9583361) |
|  | Indicates the command ID for the Move command, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_aec77a60a22f4960b0e222e13a9583361.html#aec77a60a22f4960b0e222e13a9583361) |
|  | |
| DWORD | [m\_dwAddCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a1fd8b4f8143a1b3796084e10a38a5a6e.html#a1fd8b4f8143a1b3796084e10a38a5a6e) |
|  | Indicates the command ID for the Add command, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a1fd8b4f8143a1b3796084e10a38a5a6e.html#a1fd8b4f8143a1b3796084e10a38a5a6e) |
|  | |
| DWORD | [m\_dwDeleteCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a8e526f939e68b77247562571376644c5.html#a8e526f939e68b77247562571376644c5) |
|  | Indicates the command ID for the Delete command, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a8e526f939e68b77247562571376644c5.html#a8e526f939e68b77247562571376644c5) |
|  | |
| DWORD | [m\_dwRevertCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a97fe73888f5f7a95879b31875f503aac.html#a97fe73888f5f7a95879b31875f503aac) |
|  | Indicates the command ID for the Revert command, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a97fe73888f5f7a95879b31875f503aac.html#a97fe73888f5f7a95879b31875f503aac) |
|  | |
| DWORD | [m\_dwDiffCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_acd102de8a70a4eed402ceb92d3943fc4.html#acd102de8a70a4eed402ceb92d3943fc4) |
|  | Indicates the command ID for the Diff command, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_acd102de8a70a4eed402ceb92d3943fc4.html#acd102de8a70a4eed402ceb92d3943fc4) |
|  | |
| DWORD | [m\_dwCheckOutCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_af9a43ebf20727c3dfb7ac1436c029dad.html#af9a43ebf20727c3dfb7ac1436c029dad) |
|  | Indicates the command ID for the CheckOut command, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_af9a43ebf20727c3dfb7ac1436c029dad.html#af9a43ebf20727c3dfb7ac1436c029dad) |
|  | |
| DWORD | [m\_dwRenameNoUICommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a755709add59549c396cd6553135fdd8a.html#a755709add59549c396cd6553135fdd8a) |
|  | Indicates the command ID for the Rename command, showing no User Interface, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a755709add59549c396cd6553135fdd8a.html#a755709add59549c396cd6553135fdd8a) |
|  | |
| DWORD | [m\_dwMoveNoUICommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a8a31d2194891dcc57b2d633f42aa746a.html#a8a31d2194891dcc57b2d633f42aa746a) |
|  | Indicates the command ID for the Move command, showing no User Interface, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a8a31d2194891dcc57b2d633f42aa746a.html#a8a31d2194891dcc57b2d633f42aa746a) |
|  | |
| DWORD | [m\_dwAddNoUICommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a5cda2f90f2377c7990f71debce9d53be.html#a5cda2f90f2377c7990f71debce9d53be) |
|  | Indicates the command ID for the Add command, showing no User Interface, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a5cda2f90f2377c7990f71debce9d53be.html#a5cda2f90f2377c7990f71debce9d53be) |
|  | |
| DWORD | [m\_dwDeleteNoUICommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_af78e363e34c7fce88c6b5484f95c0e59.html#af78e363e34c7fce88c6b5484f95c0e59) |
|  | Indicates the command ID for the Delete command, showing no User Interface, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_af78e363e34c7fce88c6b5484f95c0e59.html#af78e363e34c7fce88c6b5484f95c0e59) |
|  | |
| DWORD | [m\_dwRevertNoUICommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a9d18eff6e25a6c937864a0d7e3861995.html#a9d18eff6e25a6c937864a0d7e3861995) |
|  | Indicates the command ID for the Revert command, showing no User Interface, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a9d18eff6e25a6c937864a0d7e3861995.html#a9d18eff6e25a6c937864a0d7e3861995) |
|  | |
| DWORD | [m\_dwCheckOutNoUICommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a11d05af31d61791783d7849175549d50.html#a11d05af31d61791783d7849175549d50) |
|  | Indicates the command ID for the CheckOut command, showing no User Interface, s\_dwInvalidOperationID (-1) if not supported [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a11d05af31d61791783d7849175549d50.html#a11d05af31d61791783d7849175549d50) |
|  | |
| bool | [m\_bStatusIconAvailable](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a4564f014cd3d12853ef34612e237b5a7.html#a4564f014cd3d12853ef34612e237b5a7) |
|  | Indicates that the plug-in supports Project Explorer custom icons [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a4564f014cd3d12853ef34612e237b5a7.html#a4564f014cd3d12853ef34612e237b5a7) |
|  | |

## 详细描述

Plug-in information structure. This structure gives a simple overview of the plug-in's capabilities.

在文件 [ISourceControl.h](_i_source_control_8h_source.html) 第 [220](_i_source_control_8h_source.html#l00220) 行定义.