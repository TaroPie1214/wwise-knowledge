# ak_wwise_plugin_link_backend_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__link__backend__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_link\_backend\_v1结构体 参考

Host API to retrieve a link to the plug-in's backend instance.
[更多...](structak__wwise__plugin__link__backend__v1.html#details)

`#include <PluginLinks.h>`

类 ak\_wwise\_plugin\_link\_backend\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__link__backend__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__link__backend__v1_a2712f50d873479cc047f2b5938fe290e.html#a2712f50d873479cc047f2b5938fe290e) = [ak\_wwise\_plugin\_link\_backend\_instance\_v1](structak__wwise__plugin__link__backend__instance__v1.html) |
|  | Base host-provided instance to retrieve the related backend instance, as shown in the frontend. [更多...](structak__wwise__plugin__link__backend__v1_a2712f50d873479cc047f2b5938fe290e.html#a2712f50d873479cc047f2b5938fe290e) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_link\_backend\_v1](structak__wwise__plugin__link__backend__v1_a96e42e8ac53f085771bb7a7f3f3eae5c.html#a96e42e8ac53f085771bb7a7f3f3eae5c) () |
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
| [ak\_wwise\_plugin\_backend\_instance](structak__wwise__plugin__backend__instance.html) \*(\* | [Get](structak__wwise__plugin__link__backend__v1_ae3409b86755654f59f4161846eee5466.html#ae3409b86755654f59f4161846eee5466) )(const [ak\_wwise\_plugin\_link\_backend\_instance\_v1](structak__wwise__plugin__link__backend__instance__v1.html) \*in\_this) |
|  | Retrieves a link to the plug-in's backend instance. [更多...](structak__wwise__plugin__link__backend__v1_ae3409b86755654f59f4161846eee5466.html#ae3409b86755654f59f4161846eee5466) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Host API to retrieve a link to the plug-in's backend instance.

Useful for the Frontend (GUI) when a special function must be called to get a value, or update elements.

在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [41](_plugin_links_8h_source.html#l00041) 行定义.