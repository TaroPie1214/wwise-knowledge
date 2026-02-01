# ak_wwise_plugin_link_frontend_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__link__frontend__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_link\_frontend\_v1结构体 参考

Host API to retrieve a link to the plug-in's frontend interfaces.
[更多...](structak__wwise__plugin__link__frontend__v1.html#details)

`#include <PluginLinks.h>`

类 ak\_wwise\_plugin\_link\_frontend\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__link__frontend__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__link__frontend__v1_ae5416fd3b28a4ef2810238b2c85267d7.html#ae5416fd3b28a4ef2810238b2c85267d7) = [ak\_wwise\_plugin\_link\_frontend\_instance\_v1](structak__wwise__plugin__link__frontend__instance__v1.html) |
|  | Base host-provided instance to retrieve the related frontend instances related to the current backend. [更多...](structak__wwise__plugin__link__frontend__v1_ae5416fd3b28a4ef2810238b2c85267d7.html#ae5416fd3b28a4ef2810238b2c85267d7) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_link\_frontend\_v1](structak__wwise__plugin__link__frontend__v1_a762aef278af0fdaa1ac1f4e2be0fc4c9.html#a762aef278af0fdaa1ac1f4e2be0fc4c9) () |
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
| [ak\_wwise\_plugin\_frontend\_instance](structak__wwise__plugin__frontend__instance.html) \*\*(\* | [GetArray](structak__wwise__plugin__link__frontend__v1_a54de59efdb83e3feeca57605baa5783f.html#a54de59efdb83e3feeca57605baa5783f) )(const [ak\_wwise\_plugin\_link\_frontend\_instance\_v1](structak__wwise__plugin__link__frontend__instance__v1.html) \*in\_this, int \*out\_count) |
|  | Retrieves an array of the plug-in's frontend instances. [更多...](structak__wwise__plugin__link__frontend__v1_a54de59efdb83e3feeca57605baa5783f.html#a54de59efdb83e3feeca57605baa5783f) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Host API to retrieve a link to the plug-in's frontend interfaces.

Useful for the Backend when there are special properties that don't use property sets.

在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [78](_plugin_links_8h_source.html#l00078) 行定义.