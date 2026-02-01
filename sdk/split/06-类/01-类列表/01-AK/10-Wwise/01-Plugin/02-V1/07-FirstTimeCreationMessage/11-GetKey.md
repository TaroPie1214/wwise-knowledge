# GetKey

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a788cae943df5ca6452f103c34e90f1dc.html#a788cae943df5ca6452f103c34e90f1dc) | | [GetCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a939b1764d2278241a55c3348dc663270.html#a939b1764d2278241a55c3348dc663270) | | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_ac1a18a91d0d7760485a940526532c8d2.html#ac1a18a91d0d7760485a940526532c8d2) | | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a0dd0ca561e8a8d495d34b9abfc130076.html#a0dd0ca561e8a8d495d34b9abfc130076) | | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a9778245b3ccd077dd628389977e8dcef.html#a9778245b3ccd077dd628389977e8dcef) | | [GetKey](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a8315ef166cad4835421751a9bc3b9b31.html#a8315ef166cad4835421751a9bc3b9b31) | | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a2487dfa280176a2ecf2461ebbd6eac69.html#a2487dfa280176a2ecf2461ebbd6eac69) | | [~FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_aa83a4cf4380d0c46b9cf7cf3e411e78f.html#aa83a4cf4380d0c46b9cf7cf3e411e78f) | | [◆](#a8315ef166cad4835421751a9bc3b9b31)GetKey() |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | virtual const char\* AK.Wwise::Plugin::V1::FirstTimeCreationMessage::GetKey | ( |  | ) | const | | pure virtual |  Returns a unique key used in the .wproj to indicate whether the licensing message was shown.  The key should be representative of the plug-in or plug-in family, as well as user readable. Even if a GUID would be unique, it would not be helpful to the user.  返回  Null-terminated string uniquely representing this plug-in or plug-in family. |