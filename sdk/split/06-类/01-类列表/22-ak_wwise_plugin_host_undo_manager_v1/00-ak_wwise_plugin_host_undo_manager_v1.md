# ak_wwise_plugin_host_undo_manager_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__host__undo__manager__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_host\_undo\_manager\_v1结构体 参考

Host API to handle the plug-in's undo operations.
[更多...](structak__wwise__plugin__host__undo__manager__v1.html#details)

`#include <HostUndoManager.h>`

类 ak\_wwise\_plugin\_host\_undo\_manager\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__host__undo__manager__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__host__undo__manager__v1_a6d9c1167d6b6a3923e13ae1ae5dd0d5f.html#a6d9c1167d6b6a3923e13ae1ae5dd0d5f) = [ak\_wwise\_plugin\_host\_undo\_manager\_instance\_v1](structak__wwise__plugin__host__undo__manager__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_undo\_manager\_v1](structak__wwise__plugin__host__undo__manager__v1.html "Host API to handle the plug-in's undo operations."). [更多...](structak__wwise__plugin__host__undo__manager__v1_a6d9c1167d6b6a3923e13ae1ae5dd0d5f.html#a6d9c1167d6b6a3923e13ae1ae5dd0d5f) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_host\_undo\_manager\_v1](structak__wwise__plugin__host__undo__manager__v1_a01cd4e72126c42aaaefb0b7bd8499037.html#a01cd4e72126c42aaaefb0b7bd8499037) () |
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
| Public 属性 | |
| [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524)(\* | [OpenGroup](structak__wwise__plugin__host__undo__manager__v1_a0d3457469940d6c51413b280190f4b13.html#a0d3457469940d6c51413b280190f4b13) )(struct [ak\_wwise\_plugin\_host\_undo\_manager\_instance\_v1](structak__wwise__plugin__host__undo__manager__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) in\_reopenGroupId) |
|  | Open a group that will contain all subsequent undo events. [更多...](structak__wwise__plugin__host__undo__manager__v1_a0d3457469940d6c51413b280190f4b13.html#a0d3457469940d6c51413b280190f4b13) |
|  | |
| bool(\* | [CloseGroup](structak__wwise__plugin__host__undo__manager__v1_aca58a90c1bf1bd0c1585b6c7f24ceb0c.html#aca58a90c1bf1bd0c1585b6c7f24ceb0c) )(struct [ak\_wwise\_plugin\_host\_undo\_manager\_instance\_v1](structak__wwise__plugin__host__undo__manager__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_undo\_group\_close\_action](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#ga49b0af3e4205b935aa476d7ab1c9f65c) in\_action, [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) in\_groupId, const char \*in\_szApplyEventName) |
|  | Closes the last opened group, in stack ordering. [更多...](structak__wwise__plugin__host__undo__manager__v1_aca58a90c1bf1bd0c1585b6c7f24ceb0c.html#aca58a90c1bf1bd0c1585b6c7f24ceb0c) |
|  | |
| bool(\* | [AddCustomEvent](structak__wwise__plugin__host__undo__manager__v1_a380b66ee7d210b281755d781f878c104.html#a380b66ee7d210b281755d781f878c104) )(struct [ak\_wwise\_plugin\_host\_undo\_manager\_instance\_v1](structak__wwise__plugin__host__undo__manager__instance__v1.html) \*in\_this, struct [ak\_wwise\_plugin\_undo\_event\_pair\_v1](structak__wwise__plugin__undo__event__pair__v1.html) in\_event) |
|  | Adds a custom event to the currently opened group. [更多...](structak__wwise__plugin__host__undo__manager__v1_a380b66ee7d210b281755d781f878c104.html#a380b66ee7d210b281755d781f878c104) |
|  | |
| bool(\* | [CanAddEvent](structak__wwise__plugin__host__undo__manager__v1_a7d1010234961d4cc18150521ef401ab3.html#a7d1010234961d4cc18150521ef401ab3) )(const struct [ak\_wwise\_plugin\_host\_undo\_manager\_instance\_v1](structak__wwise__plugin__host__undo__manager__instance__v1.html) \*in\_this) |
|  | Check if we are currently in a state where we can add undo events. [更多...](structak__wwise__plugin__host__undo__manager__v1_a7d1010234961d4cc18150521ef401ab3.html#a7d1010234961d4cc18150521ef401ab3) |
|  | |
| bool(\* | [IsBusy](structak__wwise__plugin__host__undo__manager__v1_acff0bd05baeada26c0e793545632c1eb.html#acff0bd05baeada26c0e793545632c1eb) )(const struct [ak\_wwise\_plugin\_host\_undo\_manager\_instance\_v1](structak__wwise__plugin__host__undo__manager__instance__v1.html) \*in\_this) |
|  | Check if we are busy (undoing or redoing). [更多...](structak__wwise__plugin__host__undo__manager__v1_acff0bd05baeada26c0e793545632c1eb.html#acff0bd05baeada26c0e793545632c1eb) |
|  | |
| bool(\* | [CanLogUndos](structak__wwise__plugin__host__undo__manager__v1_a941b1ba71e6e65529cfc8ab2e2277ee2.html#a941b1ba71e6e65529cfc8ab2e2277ee2) )(const struct [ak\_wwise\_plugin\_host\_undo\_manager\_instance\_v1](structak__wwise__plugin__host__undo__manager__instance__v1.html) \*in\_this) |
|  | Returns whether logging can occur or not. [更多...](structak__wwise__plugin__host__undo__manager__v1_a941b1ba71e6e65529cfc8ab2e2277ee2.html#a941b1ba71e6e65529cfc8ab2e2277ee2) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Host API to handle the plug-in's undo operations.

在文件 [HostUndoManager.h](_host_undo_manager_8h_source.html) 第 [123](_host_undo_manager_8h_source.html#l00123) 行定义.