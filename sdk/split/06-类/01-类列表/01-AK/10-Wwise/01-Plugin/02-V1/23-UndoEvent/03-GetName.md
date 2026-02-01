# GetName

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [UndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_a30342aa2a944cf4d391c0d32766f1cc0.html#a30342aa2a944cf4d391c0d32766f1cc0) | | [GetName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_aad07cf18120d7d951f781fcb92edca43.html#aad07cf18120d7d951f781fcb92edca43) | | [Redo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_aa346dcb74fee30109385e723d7102d6d.html#aa346dcb74fee30109385e723d7102d6d) | | [Undo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_ac7f7250af8b8676f3d03e7c6cb3485a0.html#ac7f7250af8b8676f3d03e7c6cb3485a0) | | [◆](#aad07cf18120d7d951f781fcb92edca43)GetName() template<typename Backend >   |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual bool [AK.Wwise::Plugin::V1::UndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html)< Backend >::GetName | ( | const char \*\* | *out\_csName* | ) | const | | pure virtual |  Get the event name, to show after the "Undo " and "Redo " terms in the menu.  参数  |  |  |  | | --- | --- | --- | | [out] | out\_csName | Pointer to a static name for this event. This pointer needs to be accessible as long as the event is not destroyed. |  返回  true if successful. |