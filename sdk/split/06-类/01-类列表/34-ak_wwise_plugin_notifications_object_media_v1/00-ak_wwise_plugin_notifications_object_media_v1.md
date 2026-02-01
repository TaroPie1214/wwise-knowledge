# ak_wwise_plugin_notifications_object_media_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__notifications__object__media__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_notifications\_object\_media\_v1结构体 参考

`#include <HostObjectMedia.h>`

类 ak\_wwise\_plugin\_notifications\_object\_media\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__notifications__object__media__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__notifications__object__media__v1_ab0fc4bef5cfb0af039208cd8798864db.html#ab0fc4bef5cfb0af039208cd8798864db) = [ak\_wwise\_plugin\_notifications\_object\_media\_instance\_v1](structak__wwise__plugin__notifications__object__media__instance__v1.html) |
|  | Base instance type for receiving notifications on related object media's changes. [更多...](structak__wwise__plugin__notifications__object__media__v1_ab0fc4bef5cfb0af039208cd8798864db.html#ab0fc4bef5cfb0af039208cd8798864db) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_notifications\_object\_media\_v1](structak__wwise__plugin__notifications__object__media__v1_a6fb00ffd47ea7f2f7ba14a1022cb0678.html#a6fb00ffd47ea7f2f7ba14a1022cb0678) () |
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
| void(\* | [NotifyPluginMediaChanged](structak__wwise__plugin__notifications__object__media__v1_a44f854ad97fca4a74adc41d3dae11f5f.html#a44f854ad97fca4a74adc41d3dae11f5f) )(struct [ak\_wwise\_plugin\_notifications\_object\_media\_instance\_v1](structak__wwise__plugin__notifications__object__media__instance__v1.html) \*in\_this) |
|  | This function is called by Wwise when any of the plug-in media changes. [更多...](structak__wwise__plugin__notifications__object__media__v1_a44f854ad97fca4a74adc41d3dae11f5f.html#a44f854ad97fca4a74adc41d3dae11f5f) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

在文件 [HostObjectMedia.h](_host_object_media_8h_source.html) 第 [243](_host_object_media_8h_source.html#l00243) 行定义.