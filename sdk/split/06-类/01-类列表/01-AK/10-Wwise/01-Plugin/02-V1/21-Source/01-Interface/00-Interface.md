# Interface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Source](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source.html)
- [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Source::Interface结构体 参考

The C interface, fulfilled by your plug-in.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface.html#details)

`#include <Source.h>`

类 AK.Wwise::Plugin::V1::Source::Interface 继承关系图:

![](../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface_a7d68d40de97e5f9c4ce226ac949db2c2.html#a7d68d40de97e5f9c4ce226ac949db2c2) = [Source](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source.html) |
|  | |
| - Public 类型 继承自 [ak\_wwise\_plugin\_source\_v1](structak__wwise__plugin__source__v1.html) | |
| using | [Instance](structak__wwise__plugin__source__v1_aee1d28a6a4ef6f754a70fba412907a84.html#aee1d28a6a4ef6f754a70fba412907a84) = [ak\_wwise\_plugin\_source\_instance\_v1](structak__wwise__plugin__source__instance__v1.html) |
|  | Base instance type for providing source-specific information. [更多...](structak__wwise__plugin__source__v1_aee1d28a6a4ef6f754a70fba412907a84.html#aee1d28a6a4ef6f754a70fba412907a84) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface_aab24ad53dfeb19c5026c3aa865815e05.html#aab24ad53dfeb19c5026c3aa865815e05) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_source\_v1](structak__wwise__plugin__source__v1.html) | |
|  | [ak\_wwise\_plugin\_source\_v1](structak__wwise__plugin__source__v1_aae47a3891db3d8b51a55127c62e1cf5e.html#aae47a3891db3d8b51a55127c62e1cf5e) () |
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
| - Public 属性 继承自 [ak\_wwise\_plugin\_source\_v1](structak__wwise__plugin__source__v1.html) | |
| bool(\* | [GetSourceDuration](structak__wwise__plugin__source__v1_acbbde39cc0fc257bf1d3e2fe1fb6ab43.html#acbbde39cc0fc257bf1d3e2fe1fb6ab43) )(const struct [ak\_wwise\_plugin\_source\_instance\_v1](structak__wwise__plugin__source__instance__v1.html) \*in\_this, double \*out\_dblMinDuration, double \*out\_dblMaxDuration) |
|  | Return the minimum and maximum duration, in seconds. [更多...](structak__wwise__plugin__source__v1_acbbde39cc0fc257bf1d3e2fe1fb6ab43.html#acbbde39cc0fc257bf1d3e2fe1fb6ab43) |
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

在文件 [Source.h](_source_8h_source.html) 第 [122](_source_8h_source.html#l00122) 行定义.