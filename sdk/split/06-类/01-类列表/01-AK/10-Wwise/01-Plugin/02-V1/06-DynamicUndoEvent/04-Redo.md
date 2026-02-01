# Redo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [DynamicUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_a291784b0a998f17f4cfd4f38c9edd9d9.html#a291784b0a998f17f4cfd4f38c9edd9d9) | | [GetName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_a9e377b3561039445384d2d5e26e48704.html#a9e377b3561039445384d2d5e26e48704) | | [Redo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_a5023d6b0c01d89c17354d27f756c5536.html#a5023d6b0c01d89c17354d27f756c5536) | | [Undo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_af07a9ceb69c49faa8bdb9a0c22a18457.html#af07a9ceb69c49faa8bdb9a0c22a18457) | | [◆](#a5023d6b0c01d89c17354d27f756c5536)Redo() template<typename BackendDerivedClass >   |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual bool [AK.Wwise::Plugin::V1::DynamicUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event.html)< BackendDerivedClass >::Redo | ( | BackendDerivedClass & | *in\_backend* | ) |  | | pure virtual |  Called when the user asks to redo an action.   |  |  | | --- | --- | |  | **警告:** The backend instance is provided to you. You should never keep pointers to any plug-in instances or services, as these might have been deleted and recreated in the meantime. |   参数  |  |  |  | | --- | --- | --- | | [in] | in\_backend | The backend instance that created this event. | |