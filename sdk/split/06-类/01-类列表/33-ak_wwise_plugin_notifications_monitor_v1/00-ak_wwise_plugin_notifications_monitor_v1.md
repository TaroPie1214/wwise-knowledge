# ak_wwise_plugin_notifications_monitor_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__notifications__monitor__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_notifications\_monitor\_v1结构体 参考

API for Sound Engine's Monitor Data notification.
[更多...](structak__wwise__plugin__notifications__monitor__v1.html#details)

`#include <Notifications.h>`

类 ak\_wwise\_plugin\_notifications\_monitor\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__notifications__monitor__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__notifications__monitor__v1_aec55cec473eaf42d4a1b95537417323d.html#aec55cec473eaf42d4a1b95537417323d) = [ak\_wwise\_plugin\_notifications\_monitor\_instance\_v1](structak__wwise__plugin__notifications__monitor__instance__v1.html) |
|  | Base instance type for receiving Sound Engine's monitoring data. [更多...](structak__wwise__plugin__notifications__monitor__v1_aec55cec473eaf42d4a1b95537417323d.html#aec55cec473eaf42d4a1b95537417323d) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_notifications\_monitor\_v1](structak__wwise__plugin__notifications__monitor__v1_acc5e4b0d26b3589380fcd6257c819fa3.html#acc5e4b0d26b3589380fcd6257c819fa3) () |
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
| void(\* | [NotifyMonitorData](structak__wwise__plugin__notifications__monitor__v1_ab2bbe58092e334737fd2a3fb7ab902ec.html#ab2bbe58092e334737fd2a3fb7ab902ec) )(struct [ak\_wwise\_plugin\_notifications\_monitor\_instance\_v1](structak__wwise__plugin__notifications__monitor__instance__v1.html) \*in\_this, [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) in\_iTimeStamp, const [AK::Wwise::Plugin::MonitorData](struct_a_k_1_1_wwise_1_1_plugin_1_1_monitor_data.html) \*in\_pMonitorDataArray, unsigned int in\_uMonitorDataArraySize, bool in\_bIsRealtime) |
|  | Received a new Monitor Data blob. [更多...](structak__wwise__plugin__notifications__monitor__v1_ab2bbe58092e334737fd2a3fb7ab902ec.html#ab2bbe58092e334737fd2a3fb7ab902ec) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

API for Sound Engine's Monitor Data notification.

在文件 [Notifications.h](_notifications_8h_source.html) 第 [44](_notifications_8h_source.html#l00044) 行定义.