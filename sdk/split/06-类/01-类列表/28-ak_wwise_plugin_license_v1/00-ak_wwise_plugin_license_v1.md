# ak_wwise_plugin_license_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__license__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_license\_v1结构体 参考

Backend API to specify licensing requirements
[更多...](structak__wwise__plugin__license__v1.html#details)

`#include <License.h>`

类 ak\_wwise\_plugin\_license\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__license__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__license__v1_aeb5502440bfc400f8c509bb1f9a6a66a.html#aeb5502440bfc400f8c509bb1f9a6a66a) = [ak\_wwise\_plugin\_license\_instance\_v1](structak__wwise__plugin__license__instance__v1.html) |
|  | Base instance type for providing licensing information. [更多...](structak__wwise__plugin__license__v1_aeb5502440bfc400f8c509bb1f9a6a66a.html#aeb5502440bfc400f8c509bb1f9a6a66a) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_license\_v1](structak__wwise__plugin__license__v1_a6b49086b01f52500252ab95fc6e97f47.html#a6b49086b01f52500252ab95fc6e97f47) () |
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
| [AK::Wwise::Plugin::LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4)(\* | [GetLicenseStatus](structak__wwise__plugin__license__v1_a664db1c0412ec70f76346ae52837753f.html#a664db1c0412ec70f76346ae52837753f) )(const struct [ak\_wwise\_plugin\_license\_instance\_v1](structak__wwise__plugin__license__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, [AK::Wwise::Plugin::Severity](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67ed) \*out\_eSeverity, char \*out\_pszMessage, unsigned int in\_uiBufferSize) |
|  | Retrieve the licensing status of the plug-in for the given platform. [更多...](structak__wwise__plugin__license__v1_a664db1c0412ec70f76346ae52837753f.html#a664db1c0412ec70f76346ae52837753f) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Backend API to specify licensing requirements

在文件 [License.h](_license_8h_source.html) 第 [39](_license_8h_source.html#l00039) 行定义.