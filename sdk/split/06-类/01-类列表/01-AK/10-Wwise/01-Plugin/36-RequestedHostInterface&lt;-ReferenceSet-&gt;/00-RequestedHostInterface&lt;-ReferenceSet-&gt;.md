# RequestedHostInterface&lt; ReferenceSet &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< ReferenceSet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< ReferenceSet >类 参考

`#include <HostReferenceSet.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< ReferenceSet > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4_ac36f45d03731bff3c2cd30a7f744b3ff.html#ac36f45d03731bff3c2cd30a7f744b3ff) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_aa9c66805a7050040225bb144c6be8d06.html#aa9c66805a7050040225bb144c6be8d06), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< ReferenceSet, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_aa9c66805a7050040225bb144c6be8d06.html#aa9c66805a7050040225bb144c6be8d06) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::Notifications::ReferenceSet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set__.html) | |
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
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4_a368f46fa0e0b2d57e9ed6010907ed7b1.html#a368f46fa0e0b2d57e9ed6010907ed7b1) () |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::Notifications::ReferenceSet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set__.html) | |
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

|  |  |
| --- | --- |
| Public 属性 | |
| [ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_aa9c66805a7050040225bb144c6be8d06.html#aa9c66805a7050040225bb144c6be8d06) ::[Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface.html) & | [g\_referenceSetInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4_a1b142bccb83db62c0d0f112100a55058.html#a1b142bccb83db62c0d0f112100a55058) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| [HostInterfaceDefinition::Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) & | [m\_referenceSet](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4_a5e1b4828803fb20fd986332bad42d531.html#a5e1b4828803fb20fd986332bad42d531) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< ReferenceSet, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [HostReferenceSet.h](_host_reference_set_8h_source.html) 第 [536](_host_reference_set_8h_source.html#l00536) 行定义.