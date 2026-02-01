# ak_wwise_plugin_notifications_host_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__notifications__host__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_notifications\_host\_v1结构体 参考

API to receive host's update notifications.
[更多...](structak__wwise__plugin__notifications__host__v1.html#details)

`#include <Host.h>`

类 ak\_wwise\_plugin\_notifications\_host\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__notifications__host__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__notifications__host__v1_a2be163bb727db442e2a06b70ce45dcd0.html#a2be163bb727db442e2a06b70ce45dcd0) = [ak\_wwise\_plugin\_notifications\_host\_instance\_v1](structak__wwise__plugin__notifications__host__instance__v1.html) |
|  | Base instance type for receiving notifications on host changes events. [更多...](structak__wwise__plugin__notifications__host__v1_a2be163bb727db442e2a06b70ce45dcd0.html#a2be163bb727db442e2a06b70ce45dcd0) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_notifications\_host\_v1](structak__wwise__plugin__notifications__host__v1_a2b38d9090ee45f780177974b5dda8d93.html#a2b38d9090ee45f780177974b5dda8d93) () |
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
| void(\* | [NotifyCurrentPlatformChanged](structak__wwise__plugin__notifications__host__v1_a5906b30c4623ca87f4d1caecf9bfebbe.html#a5906b30c4623ca87f4d1caecf9bfebbe) )(struct [ak\_wwise\_plugin\_notifications\_host\_instance\_v1](structak__wwise__plugin__notifications__host__instance__v1.html) \*in\_this, const GUID \*in\_guidCurrentPlatform) |
|  | Received when the current platform changes. [更多...](structak__wwise__plugin__notifications__host__v1_a5906b30c4623ca87f4d1caecf9bfebbe.html#a5906b30c4623ca87f4d1caecf9bfebbe) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

API to receive host's update notifications.

在文件 [Host.h](_v1_2_host_8h_source.html) 第 [186](_v1_2_host_8h_source.html#l00186) 行定义.