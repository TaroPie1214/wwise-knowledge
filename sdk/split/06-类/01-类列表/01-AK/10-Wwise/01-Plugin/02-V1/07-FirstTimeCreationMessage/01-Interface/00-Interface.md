# Interface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message.html)
- [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::FirstTimeCreationMessage::Interface结构体 参考

The C interface, fulfilled by your plug-in.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface.html#details)

`#include <FirstTimeCreationMessage.h>`

类 AK.Wwise::Plugin::V1::FirstTimeCreationMessage::Interface 继承关系图:

![](../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface_af5dca7ec8acec34854768f2268164624.html#af5dca7ec8acec34854768f2268164624) = [FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message.html) |
|  | |
| - Public 类型 继承自 [ak\_wwise\_plugin\_first\_time\_creation\_message\_v1](structak__wwise__plugin__first__time__creation__message__v1.html) | |
| using | [Instance](structak__wwise__plugin__first__time__creation__message__v1_a1c9a5836249ac8dae52e0819ce04e372.html#a1c9a5836249ac8dae52e0819ce04e372) = [ak\_wwise\_plugin\_first\_time\_creation\_message\_instance\_v1](structak__wwise__plugin__first__time__creation__message__instance__v1.html) |
|  | Base instance type for providing a message shown the first time an instance is created. [更多...](structak__wwise__plugin__first__time__creation__message__v1_a1c9a5836249ac8dae52e0819ce04e372.html#a1c9a5836249ac8dae52e0819ce04e372) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface_af68551d4db849232bde2fa792363eb8a.html#af68551d4db849232bde2fa792363eb8a) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_first\_time\_creation\_message\_v1](structak__wwise__plugin__first__time__creation__message__v1.html) | |
|  | [ak\_wwise\_plugin\_first\_time\_creation\_message\_v1](structak__wwise__plugin__first__time__creation__message__v1_adb5c5fc3786aa19b5e4cac479483ccd1.html#adb5c5fc3786aa19b5e4cac479483ccd1) () |
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
| - Public 属性 继承自 [ak\_wwise\_plugin\_first\_time\_creation\_message\_v1](structak__wwise__plugin__first__time__creation__message__v1.html) | |
| const char \*(\* | [GetKey](structak__wwise__plugin__first__time__creation__message__v1_a16dee487f9b91bf1b3f912d6e14a1d43.html#a16dee487f9b91bf1b3f912d6e14a1d43) )(const struct [ak\_wwise\_plugin\_first\_time\_creation\_message\_instance\_v1](structak__wwise__plugin__first__time__creation__message__instance__v1.html) \*in\_this) |
|  | Returns a unique key used in the .wproj to indicate whether the licensing message was shown. [更多...](structak__wwise__plugin__first__time__creation__message__v1_a16dee487f9b91bf1b3f912d6e14a1d43.html#a16dee487f9b91bf1b3f912d6e14a1d43) |
|  | |
| const char \*(\* | [GetCreationMessage](structak__wwise__plugin__first__time__creation__message__v1_ad0ebe12f6bfd42d23870916e3dc5c7b1.html#ad0ebe12f6bfd42d23870916e3dc5c7b1) )(const struct [ak\_wwise\_plugin\_first\_time\_creation\_message\_instance\_v1](structak__wwise__plugin__first__time__creation__message__instance__v1.html) \*in\_this) |
|  | Returns a unique creation message shown to the user. [更多...](structak__wwise__plugin__first__time__creation__message__v1_ad0ebe12f6bfd42d23870916e3dc5c7b1.html#ad0ebe12f6bfd42d23870916e3dc5c7b1) |
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

在文件 [FirstTimeCreationMessage.h](_first_time_creation_message_8h_source.html) 第 [127](_first_time_creation_message_8h_source.html#l00127) 行定义.