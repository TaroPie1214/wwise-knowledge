# Interface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications.html)
- [ReferenceSet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set__.html)
- [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::Notifications::ReferenceSet\_::Interface结构体 参考

The C interface, fulfilled by your plug-in.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface.html#details)

`#include <HostReferenceSet.h>`

类 AK.Wwise::Plugin::Notifications::ReferenceSet\_::Interface 继承关系图:

![](../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface_a5eb3c4753b5dee65d7196ce29b0dcd93.html#a5eb3c4753b5dee65d7196ce29b0dcd93) = [ReferenceSet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set__.html) |
|  | |
| - Public 类型 继承自 [ak\_wwise\_plugin\_notifications\_reference\_set\_v1](structak__wwise__plugin__notifications__reference__set__v1.html) | |
| using | [Instance](structak__wwise__plugin__notifications__reference__set__v1_a870d2ce039dd748e690e2b475765ae11.html#a870d2ce039dd748e690e2b475765ae11) = [ak\_wwise\_plugin\_notifications\_reference\_set\_instance\_v1](structak__wwise__plugin__notifications__reference__set__instance__v1.html) |
|  | Base instance type for receiving notifications on reference set's changes. [更多...](structak__wwise__plugin__notifications__reference__set__v1_a870d2ce039dd748e690e2b475765ae11.html#a870d2ce039dd748e690e2b475765ae11) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_notifications_1_1_reference_set___1_1_interface_ad05676aea82b86cc46ab1a2421242238.html#ad05676aea82b86cc46ab1a2421242238) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_notifications\_reference\_set\_v1](structak__wwise__plugin__notifications__reference__set__v1.html) | |
|  | [ak\_wwise\_plugin\_notifications\_reference\_set\_v1](structak__wwise__plugin__notifications__reference__set__v1_a38b89496a0dd3b8c57d0eb11f3bf37d7.html#a38b89496a0dd3b8c57d0eb11f3bf37d7) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_a7d1ff21fd409fc7363077edecb25a85d.html#a7d1ff21fd409fc7363077edecb25a85d) (decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9)) in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_aef726120a06d869829ad6ec67df4f2a4.html#aef726120a06d869829ad6ec67df4f2a4) () |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_acefd1ca37e4c88b6c792ec43953d3f9c.html#acefd1ca37e4c88b6c792ec43953d3f9c) (std::underlying\_type< decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9))>::type in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_notifications\_reference\_set\_v1](structak__wwise__plugin__notifications__reference__set__v1.html) | |
| void(\* | [NotifyReferenceChanged](structak__wwise__plugin__notifications__reference__set__v1_a3daf589e21b7851c22b534d5b15df4c2.html#a3daf589e21b7851c22b534d5b15df4c2) )(struct [ak\_wwise\_plugin\_notifications\_reference\_set\_instance\_v1](structak__wwise__plugin__notifications__reference__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszReferenceName) |
|  | This function is called by Wwise when a plug-in reference changes. [更多...](structak__wwise__plugin__notifications__reference__set__v1_a3daf589e21b7851c22b534d5b15df4c2.html#a3daf589e21b7851c22b534d5b15df4c2) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

The C interface, fulfilled by your plug-in.

在文件 [HostReferenceSet.h](_host_reference_set_8h_source.html) 第 [462](_host_reference_set_8h_source.html#l00462) 行定义.