# ak_wwise_plugin_sink_devices_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__sink__devices__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_sink\_devices\_v1结构体 参考

Device enumerator for sink plug-ins.
[更多...](structak__wwise__plugin__sink__devices__v1.html#details)

`#include <SinkDevices.h>`

类 ak\_wwise\_plugin\_sink\_devices\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__sink__devices__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__sink__devices__v1_aa5f405106aa1af9ef69f1c5093ebe2f4.html#aa5f405106aa1af9ef69f1c5093ebe2f4) = [ak\_wwise\_plugin\_sink\_devices\_instance\_v1](structak__wwise__plugin__sink__devices__instance__v1.html) |
|  | Base instance type for providing a device list for your custom sink through [ak\_wwise\_plugin\_sink\_devices\_v1](structak__wwise__plugin__sink__devices__v1.html "Device enumerator for sink plug-ins."). [更多...](structak__wwise__plugin__sink__devices__v1_aa5f405106aa1af9ef69f1c5093ebe2f4.html#aa5f405106aa1af9ef69f1c5093ebe2f4) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_sink\_devices\_v1](structak__wwise__plugin__sink__devices__v1_a00d14c5c24ed012b3c31417a48d23702.html#a00d14c5c24ed012b3c31417a48d23702) () |
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
| int(\* | [GetCount](structak__wwise__plugin__sink__devices__v1_affe92d49a2287df1a99fb0df541b9f79.html#affe92d49a2287df1a99fb0df541b9f79) )(const struct [ak\_wwise\_plugin\_sink\_devices\_instance\_v1](structak__wwise__plugin__sink__devices__instance__v1.html) \*in\_this) |
|  | Get a count of the number of interfaces currently available. [更多...](structak__wwise__plugin__sink__devices__v1_affe92d49a2287df1a99fb0df541b9f79.html#affe92d49a2287df1a99fb0df541b9f79) |
|  | |
| const char \*(\* | [GetName](structak__wwise__plugin__sink__devices__v1_af5aaf3c1f014dd975d7454f188f747e6.html#af5aaf3c1f014dd975d7454f188f747e6) )(const struct [ak\_wwise\_plugin\_sink\_devices\_instance\_v1](structak__wwise__plugin__sink__devices__instance__v1.html) \*in\_this, int in\_num) |
|  | Get a user-presentable name for the device number in\_num. [更多...](structak__wwise__plugin__sink__devices__v1_af5aaf3c1f014dd975d7454f188f747e6.html#af5aaf3c1f014dd975d7454f188f747e6) |
|  | |
| uint32\_t(\* | [GetDeviceID](structak__wwise__plugin__sink__devices__v1_ad322757eaa29d389f70cc8a313d61149.html#ad322757eaa29d389f70cc8a313d61149) )(const struct [ak\_wwise\_plugin\_sink\_devices\_instance\_v1](structak__wwise__plugin__sink__devices__instance__v1.html) \*in\_this, int in\_num) |
|  | Get a device ID for the device number in\_num. [更多...](structak__wwise__plugin__sink__devices__v1_ad322757eaa29d389f70cc8a313d61149.html#ad322757eaa29d389f70cc8a313d61149) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Device enumerator for sink plug-ins.

Allows your plug-in to provide a list of up-to-date device IDs that can be used to instantiate a new Sound Engine sink.

This plug-in interface cannot be linked to a backend or a frontend plug-in, it must be standalone.

参见
:   - [ak\_wwise\_plugin\_sink\_devices\_instance\_v1](structak__wwise__plugin__sink__devices__instance__v1.html) instance type
    - [AK::Wwise::Plugin::SinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_afd1d6878bfb9cc5c27a1741a7a9cd5d1.html#afd1d6878bfb9cc5c27a1741a7a9cd5d1) C++ Interface
    - [AK\_WWISE\_PLUGIN\_SINK\_DEVICES\_V1\_ID](_sink_devices_8h_aab9c7a90deefe0e7f9101e6269acdcb7.html#aab9c7a90deefe0e7f9101e6269acdcb7) Current ID for interface
    - [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SINK\_DEVICES](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a821f9229a08f07baaf0783425ced53d1)

在文件 [SinkDevices.h](_sink_devices_8h_source.html) 第 [58](_sink_devices_8h_source.html#l00058) 行定义.