# Interface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html)
- [PropertySet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set__.html)
- [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Notifications::PropertySet\_::Interface结构体 参考

The C interface, fulfilled by your plug-in.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface.html#details)

`#include <HostPropertySet.h>`

类 AK.Wwise::Plugin::V1::Notifications::PropertySet\_::Interface 继承关系图:

![](../../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface_a313b1ea9ba29044120e878e80b5afbe1.html#a313b1ea9ba29044120e878e80b5afbe1) = [PropertySet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set__.html) |
|  | |
| - Public 类型 继承自 [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1.html) | |
| using | [Instance](structak__wwise__plugin__notifications__property__set__v1_a914951e9383ed25224afd6b9c435f1a7.html#a914951e9383ed25224afd6b9c435f1a7) = [ak\_wwise\_plugin\_notifications\_property\_set\_instance\_v1](structak__wwise__plugin__notifications__property__set__instance__v1.html) |
|  | Base instance type for receiving notifications on property set's changes. [更多...](structak__wwise__plugin__notifications__property__set__v1_a914951e9383ed25224afd6b9c435f1a7.html#a914951e9383ed25224afd6b9c435f1a7) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface_ae8e992448882cf88e6448419ed21308a.html#ae8e992448882cf88e6448419ed21308a) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1.html) | |
|  | [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1_aa0bb498d5a4cf51b639b6bbf7f4e182d.html#aa0bb498d5a4cf51b639b6bbf7f4e182d) () |
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
| - Public 属性 继承自 [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1.html) | |
| void(\* | [NotifyPropertyChanged](structak__wwise__plugin__notifications__property__set__v1_ac5b5e93308665275465df0ecff5eb2c3.html#ac5b5e93308665275465df0ecff5eb2c3) )(struct [ak\_wwise\_plugin\_notifications\_property\_set\_instance\_v1](structak__wwise__plugin__notifications__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | This function is called by Wwise when a plug-in property changes. [更多...](structak__wwise__plugin__notifications__property__set__v1_ac5b5e93308665275465df0ecff5eb2c3.html#ac5b5e93308665275465df0ecff5eb2c3) |
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

在文件 [HostPropertySet.h](_v1_2_host_property_set_8h_source.html) 第 [2368](_v1_2_host_property_set_8h_source.html#l02368) 行定义.