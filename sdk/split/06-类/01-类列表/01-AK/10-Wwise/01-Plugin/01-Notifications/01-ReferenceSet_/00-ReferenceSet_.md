# ReferenceSet_

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications.html)
- [ReferenceSet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set__.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set__-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::Notifications::ReferenceSet\_类 参考

[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set__.html#details)

`#include <HostReferenceSet.h>`

类 AK.Wwise::Plugin::Notifications::ReferenceSet\_ 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set__.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___a963d672473951a31d6ed58b9643ba724.html#a963d672473951a31d6ed58b9643ba724a1238d1640d8e419c9d245771159b97cf) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_REFERENCE\_SET } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___a963d672473951a31d6ed58b9643ba724.html#a963d672473951a31d6ed58b9643ba724) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___aa0250d6579d1ccd068ded8b315a74dcc.html#aa0250d6579d1ccd068ded8b315a74dcca318461d11460408a2fc37b66ebebb708) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___aa0250d6579d1ccd068ded8b315a74dcc.html#aa0250d6579d1ccd068ded8b315a74dcc) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___a31d3be7fa6343abdce4ca3caaffd6e62.html#a31d3be7fa6343abdce4ca3caaffd6e62) = [CReferenceSet\_::Instance](structak__wwise__plugin__notifications__reference__set__v1_a870d2ce039dd748e690e2b475765ae11.html#a870d2ce039dd748e690e2b475765ae11) |
|  | Base instance type for receiving notifications on reference set's changes. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___a31d3be7fa6343abdce4ca3caaffd6e62.html#a31d3be7fa6343abdce4ca3caaffd6e62) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___a4528d86cbac1311789f42207afea2abc.html#a4528d86cbac1311789f42207afea2abc) () |
|  | |
| [CReferenceSet\_::Instance](structak__wwise__plugin__notifications__reference__set__v1_a870d2ce039dd748e690e2b475765ae11.html#a870d2ce039dd748e690e2b475765ae11) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___a78b9b3a946b00826dd555b60493a0800.html#a78b9b3a946b00826dd555b60493a0800) () |
|  | |
| const [CReferenceSet\_::Instance](structak__wwise__plugin__notifications__reference__set__v1_a870d2ce039dd748e690e2b475765ae11.html#a870d2ce039dd748e690e2b475765ae11) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___afef1039c3617235a8f0b02f4919c3c0a.html#afef1039c3617235a8f0b02f4919c3c0a) () const |
|  | |
|  | [ReferenceSet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___a0cf17a397751e2108c5d475ff8d5a5d4.html#a0cf17a397751e2108c5d475ff8d5a5d4) () |
|  | |
| virtual | [~ReferenceSet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___af2cb6eebce7f11d88f849dfaaf588a93.html#af2cb6eebce7f11d88f849dfaaf588a93) () |
|  | |
| virtual void | [NotifyReferenceChanged](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___aa89f7b9b36764faa3442620a1c980b55.html#aa89f7b9b36764faa3442620a1c980b55) (const GUID &in\_guidPlatform, const char \*in\_pszReferenceName) |
|  | This function is called by [Wwise](namespace_a_k_1_1_wwise.html) when a plug-in reference changes. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___aa89f7b9b36764faa3442620a1c980b55.html#aa89f7b9b36764faa3442620a1c980b55) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

在文件 [HostReferenceSet.h](_host_reference_set_8h_source.html) 第 [430](_host_reference_set_8h_source.html#l00430) 行定义.