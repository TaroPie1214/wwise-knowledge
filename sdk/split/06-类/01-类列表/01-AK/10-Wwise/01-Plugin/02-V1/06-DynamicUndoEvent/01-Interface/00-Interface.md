# Interface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [DynamicUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event.html)
- [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_1_1_interface.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_1_1_interface-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::DynamicUndoEvent< BackendDerivedClass >::Interface结构体 参考

`#include <HostUndoManager.h>`

类 AK.Wwise::Plugin::V1::DynamicUndoEvent< BackendDerivedClass >::Interface 继承关系图:

![](../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_1_1_interface.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_1_1_interface_aea3ccfc791bf0b5e354bb9f4b1c31f96.html#aea3ccfc791bf0b5e354bb9f4b1c31f96) = [DynamicUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event.html) |
|  | |
| - Public 类型 继承自 [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1.html) | |
| using | [Instance](structak__wwise__plugin__undo__event__v1_a2f3ddaf6257dcf06ca0c20ad1280c51a.html#a2f3ddaf6257dcf06ca0c20ad1280c51a) = [ak\_wwise\_plugin\_undo\_event\_instance\_v1](structak__wwise__plugin__undo__event__instance__v1.html) |
|  | Base instance type for providing custom undo operations. [更多...](structak__wwise__plugin__undo__event__v1_a2f3ddaf6257dcf06ca0c20ad1280c51a.html#a2f3ddaf6257dcf06ca0c20ad1280c51a) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_1_1_interface_aa57abd9dae4b7f4cca36cc0b106deae6.html#aa57abd9dae4b7f4cca36cc0b106deae6) () |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event_1_1_interface_aa57abd9dae4b7f4cca36cc0b106deae6.html#aa57abd9dae4b7f4cca36cc0b106deae6) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1.html) | |
|  | [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1_a70137d46a71d6f61e4a99c7485da1768.html#a70137d46a71d6f61e4a99c7485da1768) () |
|  | |
|  | [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1_a44484f5e56ee5e2e129ad5cb95a7f6b8.html#a44484f5e56ee5e2e129ad5cb95a7f6b8) (decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9)) in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |
|  | [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1_a08dfc0758cb6db28709d0a4b96749083.html#a08dfc0758cb6db28709d0a4b96749083) (std::underlying\_type< decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9))>::type in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
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
| - Public 属性 继承自 [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1.html) | |
| void(\* | [Destroy](structak__wwise__plugin__undo__event__v1_a2f2b99edecfefc7e16ceb490fbf68612.html#a2f2b99edecfefc7e16ceb490fbf68612) )(struct [ak\_wwise\_plugin\_undo\_event\_instance\_v1](structak__wwise__plugin__undo__event__instance__v1.html) \*in\_this) |
|  | Called when the system needs to destroy your [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1.html "API to create a custom undo event in a plug-in.") instance. [更多...](structak__wwise__plugin__undo__event__v1_a2f2b99edecfefc7e16ceb490fbf68612.html#a2f2b99edecfefc7e16ceb490fbf68612) |
|  | |
| bool(\* | [Undo](structak__wwise__plugin__undo__event__v1_a7fa6a5518332aaadc42cacdacfbda754.html#a7fa6a5518332aaadc42cacdacfbda754) )(struct [ak\_wwise\_plugin\_undo\_event\_instance\_v1](structak__wwise__plugin__undo__event__instance__v1.html) \*in\_this, struct [ak\_wwise\_plugin\_backend\_instance](structak__wwise__plugin__backend__instance.html) \*in\_backend) |
|  | Called when the user asks to undo an action. [更多...](structak__wwise__plugin__undo__event__v1_a7fa6a5518332aaadc42cacdacfbda754.html#a7fa6a5518332aaadc42cacdacfbda754) |
|  | |
| bool(\* | [Redo](structak__wwise__plugin__undo__event__v1_a496e6baf329670ea1e59773e7a59b472.html#a496e6baf329670ea1e59773e7a59b472) )(struct [ak\_wwise\_plugin\_undo\_event\_instance\_v1](structak__wwise__plugin__undo__event__instance__v1.html) \*in\_this, struct [ak\_wwise\_plugin\_backend\_instance](structak__wwise__plugin__backend__instance.html) \*in\_backend) |
|  | Called when the user asks to redo an action. [更多...](structak__wwise__plugin__undo__event__v1_a496e6baf329670ea1e59773e7a59b472.html#a496e6baf329670ea1e59773e7a59b472) |
|  | |
| bool(\* | [GetName](structak__wwise__plugin__undo__event__v1_a7952f1fb84dd13dc967813feecd997b4.html#a7952f1fb84dd13dc967813feecd997b4) )(const struct [ak\_wwise\_plugin\_undo\_event\_instance\_v1](structak__wwise__plugin__undo__event__instance__v1.html) \*in\_this, const char \*\*out\_csName) |
|  | Get the event name, to show after the "Undo " and "Redo " terms in the menu. [更多...](structak__wwise__plugin__undo__event__v1_a7952f1fb84dd13dc967813feecd997b4.html#a7952f1fb84dd13dc967813feecd997b4) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

### template<typename BackendDerivedClass> struct AK.Wwise::Plugin::V1::DynamicUndoEvent< BackendDerivedClass >::Interface

在文件 [HostUndoManager.h](_host_undo_manager_8h_source.html) 第 [405](_host_undo_manager_8h_source.html#l00405) 行定义.