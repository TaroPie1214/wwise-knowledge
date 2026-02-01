# GetName

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [DynamicUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_a291784b0a998f17f4cfd4f38c9edd9d9.html#a291784b0a998f17f4cfd4f38c9edd9d9) | | [GetName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_a9e377b3561039445384d2d5e26e48704.html#a9e377b3561039445384d2d5e26e48704) | | [Redo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_a5023d6b0c01d89c17354d27f756c5536.html#a5023d6b0c01d89c17354d27f756c5536) | | [Undo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_af07a9ceb69c49faa8bdb9a0c22a18457.html#af07a9ceb69c49faa8bdb9a0c22a18457) | | [◆](#a9e377b3561039445384d2d5e26e48704)GetName() template<typename BackendDerivedClass >   |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual bool [AK.Wwise::Plugin::V1::DynamicUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event.html)< BackendDerivedClass >::GetName | ( | const char \*\* | *out\_csName* | ) | const | | pure virtual |  Get the event name, to show after the "Undo " and "Redo " terms in the menu.  参数  |  |  |  | | --- | --- | --- | | [out] | out\_csName | Pointer to a static name for this event. The buffer is owned by Authoring and is valid until the next API call. |  返回  true if successful. |