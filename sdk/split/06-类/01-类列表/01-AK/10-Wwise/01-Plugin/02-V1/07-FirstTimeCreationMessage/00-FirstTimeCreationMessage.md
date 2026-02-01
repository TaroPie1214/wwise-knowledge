# FirstTimeCreationMessage

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::FirstTimeCreationMessage类 参考abstract

`#include <FirstTimeCreationMessage.h>`

类 AK.Wwise::Plugin::V1::FirstTimeCreationMessage 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a9dc78588ef6abdda48359a9a2dd1f96a.html#a9dc78588ef6abdda48359a9a2dd1f96aa8cf349c901a671db80e9196ff6627ac1) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FIRST\_TIME\_CREATION\_MESSAGE } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a9dc78588ef6abdda48359a9a2dd1f96a.html#a9dc78588ef6abdda48359a9a2dd1f96a) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a2391b20bf70a5c08f6273586e496ebce.html#a2391b20bf70a5c08f6273586e496ebceac76ec106f77f3599de4a92835a950148) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a2391b20bf70a5c08f6273586e496ebce.html#a2391b20bf70a5c08f6273586e496ebce) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a2487dfa280176a2ecf2461ebbd6eac69.html#a2487dfa280176a2ecf2461ebbd6eac69) = [CFirstTimeCreationMessage::Instance](structak__wwise__plugin__first__time__creation__message__v1_a1c9a5836249ac8dae52e0819ce04e372.html#a1c9a5836249ac8dae52e0819ce04e372) |
|  | Base instance type for providing a message shown the first time an instance is created. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a2487dfa280176a2ecf2461ebbd6eac69.html#a2487dfa280176a2ecf2461ebbd6eac69) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a9778245b3ccd077dd628389977e8dcef.html#a9778245b3ccd077dd628389977e8dcef) () |
|  | |
| [CFirstTimeCreationMessage::Instance](structak__wwise__plugin__first__time__creation__message__v1_a1c9a5836249ac8dae52e0819ce04e372.html#a1c9a5836249ac8dae52e0819ce04e372) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_ac1a18a91d0d7760485a940526532c8d2.html#ac1a18a91d0d7760485a940526532c8d2) () |
|  | |
| const [CFirstTimeCreationMessage::Instance](structak__wwise__plugin__first__time__creation__message__v1_a1c9a5836249ac8dae52e0819ce04e372.html#a1c9a5836249ac8dae52e0819ce04e372) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a0dd0ca561e8a8d495d34b9abfc130076.html#a0dd0ca561e8a8d495d34b9abfc130076) () const |
|  | |
|  | [FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a788cae943df5ca6452f103c34e90f1dc.html#a788cae943df5ca6452f103c34e90f1dc) () |
|  | |
| virtual | [~FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_aa83a4cf4380d0c46b9cf7cf3e411e78f.html#aa83a4cf4380d0c46b9cf7cf3e411e78f) () |
|  | |
| virtual const char \* | [GetKey](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a8315ef166cad4835421751a9bc3b9b31.html#a8315ef166cad4835421751a9bc3b9b31) () const =0 |
|  | Returns a unique key used in the .wproj to indicate whether the licensing message was shown. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a8315ef166cad4835421751a9bc3b9b31.html#a8315ef166cad4835421751a9bc3b9b31) |
|  | |
| virtual const char \* | [GetCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a939b1764d2278241a55c3348dc663270.html#a939b1764d2278241a55c3348dc663270) () const =0 |
|  | Returns a unique creation message shown to the user. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_a939b1764d2278241a55c3348dc663270.html#a939b1764d2278241a55c3348dc663270) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

在文件 [FirstTimeCreationMessage.h](_first_time_creation_message_8h_source.html) 第 [95](_first_time_creation_message_8h_source.html#l00095) 行定义.