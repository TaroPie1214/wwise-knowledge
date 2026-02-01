# ak_wwise_plugin_interface_ptr

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__base__interface-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_interface\_ptr结构体 参考

[Global](group__global.html)

Interface description and base class for every Wwise Authoring plug-in interface.
[更多...](structak__wwise__plugin__base__interface.html#details)

`#include <PluginBaseInterface.h>`

类 ak\_wwise\_plugin\_interface\_ptr 继承关系图:

![](../../../images/structak__wwise__plugin__base__interface.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_a7d1ff21fd409fc7363077edecb25a85d.html#a7d1ff21fd409fc7363077edecb25a85d) (decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9)) in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_aef726120a06d869829ad6ec67df4f2a4.html#aef726120a06d869829ad6ec67df4f2a4) () |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_acefd1ca37e4c88b6c792ec43953d3f9c.html#acefd1ca37e4c88b6c792ec43953d3f9c) (std::underlying\_type< decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9))>::type in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Interface description and base class for every Wwise Authoring plug-in interface.

Pointer to a generic base from a plug-in interface.

The interface description is expected to never change, and to contain two basic values: the interface type, which is an incrementing value for every single possibility of known interfaces, as well as the version of this interface, starting from 1 at the interface's public release.

An interface can either be provided by the plug-in (for example, AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_AUDIO\_PLUGIN), where the plug-in provides the functionality of the callback; or it can be requested to the Wwise Authoring host (for example, AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_PROPERTY\_SET), where the data will be filled by the host for the plug-in to call.

All requested or provided interfaces are deemed mandatory in order to instantiate a plug-in. An unknown or an invalid interface in a context (AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_GUI\_WINDOWS in WwiseConsole.exe or on Linux) causes the host to skip the plug-in.

在文件 [PluginBaseInterface.h](_plugin_base_interface_8h_source.html) 第 [124](_plugin_base_interface_8h_source.html#l00124) 行定义.