# UndoManager

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [UndoManager](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::UndoManager类 参考

Host API to handle the plug-in's undo operations.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager.html#details)

`#include <HostUndoManager.h>`

类 AK.Wwise::Plugin::V1::UndoManager 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_ae4b979d1eef86508c53cbff74e01b3d4.html#ae4b979d1eef86508c53cbff74e01b3d4a0eb0d8c5ae36dd0fe2324aa4bedc2d00) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_UNDO\_MANAGER } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_ae4b979d1eef86508c53cbff74e01b3d4.html#ae4b979d1eef86508c53cbff74e01b3d4) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a9187b061e97d696e6033c121bc6d4978.html#a9187b061e97d696e6033c121bc6d4978a807cc4f8d02ea1326ea4ee18778ff202) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a9187b061e97d696e6033c121bc6d4978.html#a9187b061e97d696e6033c121bc6d4978) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a51cbcba089f95a039df5fa3d7d6b6a8c.html#a51cbcba089f95a039df5fa3d7d6b6a8c) = [CHostUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a52afd9e84cbd6263c830cc1340cb27ed.html#a52afd9e84cbd6263c830cc1340cb27ed) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHostUndoManager >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostUndoManager >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHostUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a6f05bedc5077d964a3015045f166aec9.html#a6f05bedc5077d964a3015045f166aec9) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) | [OpenGroup](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_ac3e57e2518e901d81ddc4d88724f4cec.html#ac3e57e2518e901d81ddc4d88724f4cec) ([ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) in\_reopenGroupId=0) |
|  | Open a group that will contain all subsequent undo events. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_ac3e57e2518e901d81ddc4d88724f4cec.html#ac3e57e2518e901d81ddc4d88724f4cec) |
|  | |
| bool | [CloseGroup](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a8df113c765722217518ad343d516adce.html#a8df113c765722217518ad343d516adce) ([ak\_wwise\_plugin\_undo\_group\_close\_action](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#ga49b0af3e4205b935aa476d7ab1c9f65c) in\_action=[AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_APPLY](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65ca7b066ecc400936abe8602ec9deb27e5f), [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) in\_groupId=0, const char \*in\_szApplyEventName=nullptr) |
|  | Closes the last opened group, in stack ordering. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a8df113c765722217518ad343d516adce.html#a8df113c765722217518ad343d516adce) |
|  | |
| bool | [AddCustomEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_aeb06646805b2ed1844e2af28c188fe3d.html#aeb06646805b2ed1844e2af28c188fe3d) ([BaseUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.html) \*in\_pEvent) |
|  | Adds a custom event to the currently opened group. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_aeb06646805b2ed1844e2af28c188fe3d.html#aeb06646805b2ed1844e2af28c188fe3d) |
|  | |
| bool | [CanAddEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a50469bb416b73bf94d8f7c31bb87a9bc.html#a50469bb416b73bf94d8f7c31bb87a9bc) () const |
|  | Check if we are currently in a state where we can add undo events. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a50469bb416b73bf94d8f7c31bb87a9bc.html#a50469bb416b73bf94d8f7c31bb87a9bc) |
|  | |
| bool | [IsBusy](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a3ebcf7bbe7f7cebb3af27340f35f329a.html#a3ebcf7bbe7f7cebb3af27340f35f329a) () const |
|  | Check if we are busy (undoing or redoing). [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a3ebcf7bbe7f7cebb3af27340f35f329a.html#a3ebcf7bbe7f7cebb3af27340f35f329a) |
|  | |
| bool | [CanLogUndos](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a153df8eddf6d395fb2383b7e72ccaf47.html#a153df8eddf6d395fb2383b7e72ccaf47) () const |
|  | Returns whether logging can occur or not. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a153df8eddf6d395fb2383b7e72ccaf47.html#a153df8eddf6d395fb2383b7e72ccaf47) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostUndoManager >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

Host API to handle the plug-in's undo operations.

在文件 [HostUndoManager.h](_host_undo_manager_8h_source.html) 第 [487](_host_undo_manager_8h_source.html#l00487) 行定义.