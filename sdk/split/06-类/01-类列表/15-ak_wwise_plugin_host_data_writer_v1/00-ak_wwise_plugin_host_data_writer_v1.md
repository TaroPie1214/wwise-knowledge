# ak_wwise_plugin_host_data_writer_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__host__data__writer__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_host\_data\_writer\_v1结构体 参考

Interface used to write data during sound bank generation.
[更多...](structak__wwise__plugin__host__data__writer__v1.html#details)

`#include <HostDataWriter.h>`

类 ak\_wwise\_plugin\_host\_data\_writer\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__host__data__writer__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__host__data__writer__v1_aae0cf760ad10a17a27616f5d6d1c0487.html#aae0cf760ad10a17a27616f5d6d1c0487) = [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_data\_writer\_v1](structak__wwise__plugin__host__data__writer__v1.html "Interface used to write data during sound bank generation."). [更多...](structak__wwise__plugin__host__data__writer__v1_aae0cf760ad10a17a27616f5d6d1c0487.html#aae0cf760ad10a17a27616f5d6d1c0487) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_host\_data\_writer\_v1](structak__wwise__plugin__host__data__writer__v1_a2f64238ca3d9e095c3a60b52851f8323.html#a2f64238ca3d9e095c3a60b52851f8323) () |
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
| bool(\* | [WriteData](structak__wwise__plugin__host__data__writer__v1_a639d0c6385cbb61bf5e6c18a63fb9e69.html#a639d0c6385cbb61bf5e6c18a63fb9e69) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, const void \*in\_pData, uint32\_t in\_cBytes, uint32\_t \*out\_cWritten) |
|  | Writes a block of data. [更多...](structak__wwise__plugin__host__data__writer__v1_a639d0c6385cbb61bf5e6c18a63fb9e69.html#a639d0c6385cbb61bf5e6c18a63fb9e69) |
|  | |
| bool(\* | [WriteString](structak__wwise__plugin__host__data__writer__v1_abc22549fa8f38b803a946f88e34be241.html#abc22549fa8f38b803a946f88e34be241) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, const char \*in\_szString) |
|  | Writes a string. [更多...](structak__wwise__plugin__host__data__writer__v1_abc22549fa8f38b803a946f88e34be241.html#abc22549fa8f38b803a946f88e34be241) |
|  | |
| bool(\* | [WriteInt64](structak__wwise__plugin__host__data__writer__v1_afe62e3e70cf5173f1f5ef2abfe27c065.html#afe62e3e70cf5173f1f5ef2abfe27c065) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, int64\_t in\_value) |
|  | Writes a 64-bit signed integer value. [更多...](structak__wwise__plugin__host__data__writer__v1_afe62e3e70cf5173f1f5ef2abfe27c065.html#afe62e3e70cf5173f1f5ef2abfe27c065) |
|  | |
| bool(\* | [WriteInt32](structak__wwise__plugin__host__data__writer__v1_a1fc557c12fd97445846cc78fea2fbc27.html#a1fc557c12fd97445846cc78fea2fbc27) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, int32\_t in\_value) |
|  | Writes a 32-bit signed integer value. [更多...](structak__wwise__plugin__host__data__writer__v1_a1fc557c12fd97445846cc78fea2fbc27.html#a1fc557c12fd97445846cc78fea2fbc27) |
|  | |
| bool(\* | [WriteInt16](structak__wwise__plugin__host__data__writer__v1_a08a670541087783cc150b9c71c7f2ff0.html#a08a670541087783cc150b9c71c7f2ff0) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, int16\_t in\_value) |
|  | Writes a 16-bit signed integer value. [更多...](structak__wwise__plugin__host__data__writer__v1_a08a670541087783cc150b9c71c7f2ff0.html#a08a670541087783cc150b9c71c7f2ff0) |
|  | |
| bool(\* | [WriteInt8](structak__wwise__plugin__host__data__writer__v1_a04a80b1fcc7fc47aebcbc9790cab7ad5.html#a04a80b1fcc7fc47aebcbc9790cab7ad5) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, int8\_t in\_value) |
|  | Writes an 8-bit signed integer value. [更多...](structak__wwise__plugin__host__data__writer__v1_a04a80b1fcc7fc47aebcbc9790cab7ad5.html#a04a80b1fcc7fc47aebcbc9790cab7ad5) |
|  | |
| bool(\* | [WriteUInt64](structak__wwise__plugin__host__data__writer__v1_a03bc0ebd70097ab691c3f890b58f747f.html#a03bc0ebd70097ab691c3f890b58f747f) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, uint64\_t in\_value) |
|  | Writes a 64-bit unsigned integer value. [更多...](structak__wwise__plugin__host__data__writer__v1_a03bc0ebd70097ab691c3f890b58f747f.html#a03bc0ebd70097ab691c3f890b58f747f) |
|  | |
| bool(\* | [WriteUInt32](structak__wwise__plugin__host__data__writer__v1_a9876d0f53bee493ef9317f37931a2051.html#a9876d0f53bee493ef9317f37931a2051) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, uint32\_t in\_value) |
|  | Writes a 32-bit unsigned integer value. [更多...](structak__wwise__plugin__host__data__writer__v1_a9876d0f53bee493ef9317f37931a2051.html#a9876d0f53bee493ef9317f37931a2051) |
|  | |
| bool(\* | [WriteUInt16](structak__wwise__plugin__host__data__writer__v1_a9dbf078a77a9d6ca90f035ebc329f9f8.html#a9dbf078a77a9d6ca90f035ebc329f9f8) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, uint16\_t in\_value) |
|  | Writes a 16-bit unsigned integer value. [更多...](structak__wwise__plugin__host__data__writer__v1_a9dbf078a77a9d6ca90f035ebc329f9f8.html#a9dbf078a77a9d6ca90f035ebc329f9f8) |
|  | |
| bool(\* | [WriteUInt8](structak__wwise__plugin__host__data__writer__v1_a68b268897dcd427a1155af8bdd84f064.html#a68b268897dcd427a1155af8bdd84f064) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, uint8\_t in\_value) |
|  | Writes an 8-bit unsigned integer value. [更多...](structak__wwise__plugin__host__data__writer__v1_a68b268897dcd427a1155af8bdd84f064.html#a68b268897dcd427a1155af8bdd84f064) |
|  | |
| bool(\* | [WriteReal64](structak__wwise__plugin__host__data__writer__v1_ad4002da8a0f07ba174304a38ad9cec31.html#ad4002da8a0f07ba174304a38ad9cec31) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, double in\_value) |
|  | Writes a 64-bit, double-precision floating point value. [更多...](structak__wwise__plugin__host__data__writer__v1_ad4002da8a0f07ba174304a38ad9cec31.html#ad4002da8a0f07ba174304a38ad9cec31) |
|  | |
| bool(\* | [WriteReal32](structak__wwise__plugin__host__data__writer__v1_aff0eb855310701e1c96e8641049d6c2e.html#aff0eb855310701e1c96e8641049d6c2e) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, float in\_value) |
|  | Writes a 32-bit, single-precision floating point value. [更多...](structak__wwise__plugin__host__data__writer__v1_aff0eb855310701e1c96e8641049d6c2e.html#aff0eb855310701e1c96e8641049d6c2e) |
|  | |
| bool(\* | [WriteBool](structak__wwise__plugin__host__data__writer__v1_a5e97678e3b8ef19762885fddd21afaa3.html#a5e97678e3b8ef19762885fddd21afaa3) )(struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_this, bool in\_value) |
|  | Writes a boolean value. [更多...](structak__wwise__plugin__host__data__writer__v1_a5e97678e3b8ef19762885fddd21afaa3.html#a5e97678e3b8ef19762885fddd21afaa3) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Interface used to write data during sound bank generation.

|  |  |
| --- | --- |
|  | **备注:** All functions perform the appropriate platform-specific byte reordering, except where noted. |

参见
:   - [生成声音包](wwiseplugin_backend.html#wwiseplugin_bank)
    - AK::Wwise::Plugin::Plugin::GetBankParameters()

在文件 [HostDataWriter.h](_host_data_writer_8h_source.html) 第 [47](_host_data_writer_8h_source.html#l00047) 行定义.