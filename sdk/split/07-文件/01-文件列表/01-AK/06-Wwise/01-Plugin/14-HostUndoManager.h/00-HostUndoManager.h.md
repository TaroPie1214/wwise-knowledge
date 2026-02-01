# HostUndoManager.h

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

HostUndoManager.h 文件参考

Wwise Authoring Plug-ins - API to provide custom undo event and manage undo groups.
[更多...](#details)

`#include "HostPropertySet.h"`

[浏览源代码.](_host_undo_manager_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1.html) |
|  | API to create a custom undo event in a plug-in. [更多...](structak__wwise__plugin__undo__event__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_undo\_manager\_v1](structak__wwise__plugin__host__undo__manager__v1.html) |
|  | Host API to handle the plug-in's undo operations. [更多...](structak__wwise__plugin__host__undo__manager__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::BaseUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.html) |
|  | Base API to create a custom undo event in a plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::UndoEvent< Backend >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html) |
|  | Base API to create a custom undo event in a plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::UndoEvent< Backend >::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_1_1_interface.html) |
|  | |
| class | [AK.Wwise::Plugin::V1::DynamicUndoEvent< BackendDerivedClass >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event.html) |
|  | |
| struct | [AK.Wwise::Plugin::V1::DynamicUndoEvent< BackendDerivedClass >::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_1_1_interface.html) |
|  | |
| class | [AK.Wwise::Plugin::V1::UndoManager](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager.html) |
|  | Host API to handle the plug-in's undo operations. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< UndoManager >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_undo_manager_01_4.html) |
|  | |
| class | [AK.Wwise::Plugin::AutoUndoGroup](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group.html) |
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
| #define | [AK\_WWISE\_PLUGIN\_UNDO\_EVENT\_V1\_ID](_host_undo_manager_8h_a759a6dc7a2c4b487c6ce74d91fd7f30d.html#a759a6dc7a2c4b487c6ce74d91fd7f30d)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_UNDO\_EVENT](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a84bd3a1272d5f343df1bab3a826ffe65), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_UNDO\_EVENT\_V1\_CTOR](_host_undo_manager_8h_ab1a04dccff4d0d57766bf92573ab5383.html#ab1a04dccff4d0d57766bf92573ab5383)() |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_UNDO\_MANAGER\_V1\_ID](_host_undo_manager_8h_a49798ec60cc7afbd483eddbfd0e4e647.html#a49798ec60cc7afbd483eddbfd0e4e647)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_UNDO\_MANAGER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a07328d19f39944a12c7b57ae1955f520), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_UNDO\_MANAGER\_V1\_CTOR](_host_undo_manager_8h_ae87228df4ada156b5f9b34fde84c3929.html#ae87228df4ada156b5f9b34fde84c3929)() |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a0af52d142b140c8a7ada1115d2ed005d.html#a0af52d142b140c8a7ada1115d2ed005d) = [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::CUndoEventPair](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ab1ef9aa1581c7d193674714b1276c201.html#ab1ef9aa1581c7d193674714b1276c201) = [ak\_wwise\_plugin\_undo\_event\_pair\_v1](structak__wwise__plugin__undo__event__pair__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::CHostUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a52afd9e84cbd6263c830cc1340cb27ed.html#a52afd9e84cbd6263c830cc1340cb27ed) = [ak\_wwise\_plugin\_host\_undo\_manager\_v1](structak__wwise__plugin__host__undo__manager__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a9272de2d94abfaabb9d10a1414146a0f.html#a9272de2d94abfaabb9d10a1414146a0f) = RequestedHostInterface< UndoManager > |
|  | Requests an [UndoManager](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager.html "Host API to handle the plug-in's undo operations.") interface, provided as m\_undoManager variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a9272de2d94abfaabb9d10a1414146a0f.html#a9272de2d94abfaabb9d10a1414146a0f) |
|  | |
| using | [AK::Wwise::Plugin::CUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_ae4ec3b2c8d557d96a6c79ad1f999da0f.html#ae4ec3b2c8d557d96a6c79ad1f999da0f) = V1::CUndoEvent |
|  | Latest version of the C UndoEvent interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ae4ec3b2c8d557d96a6c79ad1f999da0f.html#ae4ec3b2c8d557d96a6c79ad1f999da0f) |
|  | |
| using | [AK::Wwise::Plugin::BaseUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_a106b6fb5a0b6171d250ccbb5059e4961.html#a106b6fb5a0b6171d250ccbb5059e4961) = V1::BaseUndoEvent |
|  | Latest version of the C++ BaseUndoEvent interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a106b6fb5a0b6171d250ccbb5059e4961.html#a106b6fb5a0b6171d250ccbb5059e4961) |
|  | |
| template<typename Backend > | |
| using | [AK::Wwise::Plugin::UndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_a88dacbb21afe6f7190ae605d5aeeabd9.html#a88dacbb21afe6f7190ae605d5aeeabd9) = V1::UndoEvent< Backend > |
|  | Latest version of the C++ UndoEvent template helper. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a88dacbb21afe6f7190ae605d5aeeabd9.html#a88dacbb21afe6f7190ae605d5aeeabd9) |
|  | |
| template<typename BackendDerivedClass > | |
| using | [AK::Wwise::Plugin::DynamicUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_ab9f3b59b0e77d18ab37a9de10ef22819.html#ab9f3b59b0e77d18ab37a9de10ef22819) = V1::DynamicUndoEvent< BackendDerivedClass > |
|  | Latest version of the C++ DynamicUndoEvent template helper. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ab9f3b59b0e77d18ab37a9de10ef22819.html#ab9f3b59b0e77d18ab37a9de10ef22819) |
|  | |
| using | [AK::Wwise::Plugin::CHostUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a6f05bedc5077d964a3015045f166aec9.html#a6f05bedc5077d964a3015045f166aec9) = V1::CHostUndoManager |
|  | Latest version of the C UndoManager interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a6f05bedc5077d964a3015045f166aec9.html#a6f05bedc5077d964a3015045f166aec9) |
|  | |
| using | [AK::Wwise::Plugin::UndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b) = V1::UndoManager |
|  | Latest version of the C++ UndoManager interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b) |
|  | |
| using | [AK::Wwise::Plugin::RequestUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a30d4abb3af40b4d9340aebfca998aabc.html#a30d4abb3af40b4d9340aebfca998aabc) = V1::RequestUndoManager |
|  | Latest version of the requested C++ UndoManager interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a30d4abb3af40b4d9340aebfca998aabc.html#a30d4abb3af40b4d9340aebfca998aabc) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a3131077b4a41bd0ddbed2fb17f0108e9.html#a3131077b4a41bd0ddbed2fb17f0108e9) (BaseUndoEvent) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_acc431a02e3a48459ec26540fc147f79a.html#acc431a02e3a48459ec26540fc147f79a) (UndoManager) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_aa3ab9f1d6ab2fa806a700629b7b77e14.html#aa3ab9f1d6ab2fa806a700629b7b77e14) (BaseUndoEvent) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ace96f8f301cbddb96750ae6535792fe7.html#ace96f8f301cbddb96750ae6535792fe7) (UndoManager) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API to provide custom undo event and manage undo groups.

在文件 [HostUndoManager.h](_host_undo_manager_8h_source.html) 中定义.