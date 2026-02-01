# AddCustomEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [UndoManager](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AddCustomEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_aeb06646805b2ed1844e2af28c188fe3d.html#aeb06646805b2ed1844e2af28c188fe3d) | | [CanAddEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a50469bb416b73bf94d8f7c31bb87a9bc.html#a50469bb416b73bf94d8f7c31bb87a9bc) | | [CanLogUndos](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a153df8eddf6d395fb2383b7e72ccaf47.html#a153df8eddf6d395fb2383b7e72ccaf47) | | [CloseGroup](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a8df113c765722217518ad343d516adce.html#a8df113c765722217518ad343d516adce) | | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a51cbcba089f95a039df5fa3d7d6b6a8c.html#a51cbcba089f95a039df5fa3d7d6b6a8c) | | [IsBusy](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_a3ebcf7bbe7f7cebb3af27340f35f329a.html#a3ebcf7bbe7f7cebb3af27340f35f329a) | | [OpenGroup](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager_ac3e57e2518e901d81ddc4d88724f4cec.html#ac3e57e2518e901d81ddc4d88724f4cec) | | [◆](#aeb06646805b2ed1844e2af28c188fe3d)AddCustomEvent() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | bool AK.Wwise::Plugin::V1::UndoManager::AddCustomEvent | ( | [BaseUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.html) \* | *in\_pEvent* | ) |  | | inline |  Adds a custom event to the currently opened group.  By default, you should be in a group while adding an event.  参数  |  |  |  | | --- | --- | --- | | [in] | in\_pEvent | Event to add to the current group. |  返回  true if successful.  在文件 [HostUndoManager.h](_host_undo_manager_8h_source.html) 第 [578](_host_undo_manager_8h_source.html#l00578) 行定义.  引用了 [ak\_wwise\_plugin\_host\_undo\_manager\_v1::AddCustomEvent](_host_undo_manager_8h_source.html#l00206), [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostUndoManager >::g\_cinterface](_plugin_info_generator_8h_source.html#l00089) , 以及 [MKBOOL](_plugin_helpers_8h_source.html#l00079). |