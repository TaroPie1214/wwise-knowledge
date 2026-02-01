# BaseUndoEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [BaseUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::BaseUndoEvent类 参考abstract

Base API to create a custom undo event in a plug-in.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.html#details)

`#include <HostUndoManager.h>`

类 AK.Wwise::Plugin::V1::BaseUndoEvent 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a137141696b8eb70aa15d0b9111025475.html#a137141696b8eb70aa15d0b9111025475ae7372dd26d982339aaeccc1f0d72c5b1) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_UNDO\_EVENT } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a137141696b8eb70aa15d0b9111025475.html#a137141696b8eb70aa15d0b9111025475) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a35467a9a52f07811e0dfc4ca8b239f5e.html#a35467a9a52f07811e0dfc4ca8b239f5ea96684bd92ed20a3fef32ee486ccf9694) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a35467a9a52f07811e0dfc4ca8b239f5e.html#a35467a9a52f07811e0dfc4ca8b239f5e) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_ae842a059fdebdeeb075be53d62a301a5.html#ae842a059fdebdeeb075be53d62a301a5) = [CUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a0af52d142b140c8a7ada1115d2ed005d.html#a0af52d142b140c8a7ada1115d2ed005d) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_ae842a059fdebdeeb075be53d62a301a5.html#ae842a059fdebdeeb075be53d62a301a5) \* | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event_a150b615149c3931e1dd8bb23c46827a0.html#a150b615149c3931e1dd8bb23c46827a0) ()=0 |
|  | |
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

## 详细描述

Base API to create a custom undo event in a plug-in.

This is useful when you handle custom properties, not handled by Property Sets.

[UndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html "Base API to create a custom undo event in a plug-in.") should be handled by the [UndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html) template.

在文件 [HostUndoManager.h](_host_undo_manager_8h_source.html) 第 [268](_host_undo_manager_8h_source.html#l00268) 行定义.