# ak_wwise_plugin_audio_plugin_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__audio__plugin__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_audio\_plugin\_v1结构体 参考

Wwise API for general Audio Plug-in's backend.
[更多...](structak__wwise__plugin__audio__plugin__v1.html#details)

`#include <AudioPlugin.h>`

类 ak\_wwise\_plugin\_audio\_plugin\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__audio__plugin__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__audio__plugin__v1_a98a20db02b16bcbb6e94d759fbadc6cf.html#a98a20db02b16bcbb6e94d759fbadc6cf) = [ak\_wwise\_plugin\_audio\_plugin\_instance\_v1](structak__wwise__plugin__audio__plugin__instance__v1.html) |
|  | Base instance type for providing audio plug-in backend services. [更多...](structak__wwise__plugin__audio__plugin__v1_a98a20db02b16bcbb6e94d759fbadc6cf.html#a98a20db02b16bcbb6e94d759fbadc6cf) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_audio\_plugin\_v1](structak__wwise__plugin__audio__plugin__v1_ae269c04f9b790abd2cfda9f3e58f5e72.html#ae269c04f9b790abd2cfda9f3e58f5e72) () |
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
| bool(\* | [GetBankParameters](structak__wwise__plugin__audio__plugin__v1_abd584886ab95277158307efdf633af78.html#abd584886ab95277158307efdf633af78) )(const struct [ak\_wwise\_plugin\_audio\_plugin\_instance\_v1](structak__wwise__plugin__audio__plugin__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_pDataWriter) |
|  | Obtains parameters that will be written to a bank. [更多...](structak__wwise__plugin__audio__plugin__v1_abd584886ab95277158307efdf633af78.html#abd584886ab95277158307efdf633af78) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Wwise API for general Audio Plug-in's backend.

参见
:   - [ak\_wwise\_plugin\_audio\_plugin\_instance\_v1](structak__wwise__plugin__audio__plugin__instance__v1.html) instance type
    - [AK::Wwise::Plugin::AudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_a989b8417cedde33d928b90171491fcc5.html#a989b8417cedde33d928b90171491fcc5) C++ Interface
    - [AK\_WWISE\_PLUGIN\_AUDIO\_PLUGIN\_V1\_ID](_audio_plugin_8h_af21f7290225f823c30ea9bba6173c2ae.html#af21f7290225f823c30ea9bba6173c2ae) Current ID for interface
    - [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_AUDIO\_PLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af60f00124117a22873d01c98255478ed)
    - [设计工具插件的后端](wwiseplugin_backend.html)

在文件 [AudioPlugin.h](_audio_plugin_8h_source.html) 第 [48](_audio_plugin_8h_source.html#l00048) 行定义.