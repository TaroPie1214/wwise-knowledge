# UndoEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [UndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event-members.html) |
[类](#nested-classes) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::UndoEvent< Backend > 模板类 参考abstract

Base API to create a custom undo event in a plug-in.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html#details)

`#include <HostUndoManager.h>`

类 AK.Wwise::Plugin::V1::UndoEvent< Backend > 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_1_1_interface.html) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [BaseUndoEvent::Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_ae842a059fdebdeeb075be53d62a301a5.html#ae842a059fdebdeeb075be53d62a301a5) \* | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_a30342aa2a944cf4d391c0d32766f1cc0.html#a30342aa2a944cf4d391c0d32766f1cc0) () final |
|  | |
| virtual bool | [Undo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_ac7f7250af8b8676f3d03e7c6cb3485a0.html#ac7f7250af8b8676f3d03e7c6cb3485a0) (Backend &in\_backend)=0 |
|  | Called when the user asks to undo an action. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_ac7f7250af8b8676f3d03e7c6cb3485a0.html#ac7f7250af8b8676f3d03e7c6cb3485a0) |
|  | |
| virtual bool | [Redo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_aa346dcb74fee30109385e723d7102d6d.html#aa346dcb74fee30109385e723d7102d6d) (Backend &in\_backend)=0 |
|  | Called when the user asks to redo an action. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_aa346dcb74fee30109385e723d7102d6d.html#aa346dcb74fee30109385e723d7102d6d) |
|  | |
| virtual bool | [GetName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_aad07cf18120d7d951f781fcb92edca43.html#aad07cf18120d7d951f781fcb92edca43) (const char \*\*out\_csName) const =0 |
|  | Get the event name, to show after the "Undo " and "Redo " terms in the menu. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_aad07cf18120d7d951f781fcb92edca43.html#aad07cf18120d7d951f781fcb92edca43) |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::V1::BaseUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.html) | |
| [CUndoEvent::Instance](structak__wwise__plugin__undo__event__v1_a2f3ddaf6257dcf06ca0c20ad1280c51a.html#a2f3ddaf6257dcf06ca0c20ad1280c51a) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_ac4584d58ed897a37cae2d482efb09242.html#ac4584d58ed897a37cae2d482efb09242) () |
|  | |
| const [CUndoEvent::Instance](structak__wwise__plugin__undo__event__v1_a2f3ddaf6257dcf06ca0c20ad1280c51a.html#a2f3ddaf6257dcf06ca0c20ad1280c51a) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a232705e053b90d9ca946700293a2b812.html#a232705e053b90d9ca946700293a2b812) () const |
|  | |
|  | [BaseUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_aeed2c9cdcbb01d0ce21e81871fe78c46.html#aeed2c9cdcbb01d0ce21e81871fe78c46) () |
|  | |
| virtual | [~BaseUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_aeb6f2c0b007941637d763be6c066f7d0.html#aeb6f2c0b007941637d763be6c066f7d0) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 类型 继承自 [AK.Wwise::Plugin::V1::BaseUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.html) | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a137141696b8eb70aa15d0b9111025475.html#a137141696b8eb70aa15d0b9111025475ae7372dd26d982339aaeccc1f0d72c5b1) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_UNDO\_EVENT } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a137141696b8eb70aa15d0b9111025475.html#a137141696b8eb70aa15d0b9111025475) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a35467a9a52f07811e0dfc4ca8b239f5e.html#a35467a9a52f07811e0dfc4ca8b239f5ea96684bd92ed20a3fef32ee486ccf9694) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a35467a9a52f07811e0dfc4ca8b239f5e.html#a35467a9a52f07811e0dfc4ca8b239f5e) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_ae842a059fdebdeeb075be53d62a301a5.html#ae842a059fdebdeeb075be53d62a301a5) = [CUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a0af52d142b140c8a7ada1115d2ed005d.html#a0af52d142b140c8a7ada1115d2ed005d) |
|  | |

## 详细描述

### template<typename Backend> class AK.Wwise::Plugin::V1::UndoEvent< Backend >

Base API to create a custom undo event in a plug-in.

This is useful when you handle custom properties, not handled by Property Sets.

Undo events should be derived by your undo class, providing [UndoEvent::Undo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_ac7f7250af8b8676f3d03e7c6cb3485a0.html#ac7f7250af8b8676f3d03e7c6cb3485a0), [UndoEvent::Redo](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_aa346dcb74fee30109385e723d7102d6d.html#aa346dcb74fee30109385e723d7102d6d) and [UndoEvent::GetName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event_aad07cf18120d7d951f781fcb92edca43.html#aad07cf18120d7d951f781fcb92edca43) methods.

No pointer to the backend class should be kept inside the undo event, as the object can be deleted and recreated when the plug-in gets removed through undo. The backend will be recreated at that point, making the pointer invalid.

模板参数
:   |  |  |
    | --- | --- |
    | Backend | The plug-in backend type. |

在文件 [HostUndoManager.h](_host_undo_manager_8h_source.html) 第 [327](_host_undo_manager_8h_source.html#l00327) 行定义.