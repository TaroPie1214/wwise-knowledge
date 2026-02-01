# ak_wwise_plugin_host_object_media_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__host__object__media__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_host\_object\_media\_v1结构体 参考

`#include <HostObjectMedia.h>`

类 ak\_wwise\_plugin\_host\_object\_media\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__host__object__media__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__host__object__media__v1_ad3c2bfcb1f6e8f37fa53f2d196101117.html#ad3c2bfcb1f6e8f37fa53f2d196101117) = [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_object\_media\_v1](structak__wwise__plugin__host__object__media__v1.html). [更多...](structak__wwise__plugin__host__object__media__v1_ad3c2bfcb1f6e8f37fa53f2d196101117.html#ad3c2bfcb1f6e8f37fa53f2d196101117) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_host\_object\_media\_v1](structak__wwise__plugin__host__object__media__v1_a1b493724a1c538ad7a69bac5aade451e.html#a1b493724a1c538ad7a69bac5aade451e) () |
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
| bool(\* | [SetMediaSource](structak__wwise__plugin__host__object__media__v1_aa6f99ff63347bb63d06ebfc9e607c51d.html#aa6f99ff63347bb63d06ebfc9e607c51d) )(struct [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) \*in\_this, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszFilePathToImport, unsigned int in\_Index, bool in\_bReplace) |
|  | Requests to set the specified file as a data input file. [更多...](structak__wwise__plugin__host__object__media__v1_aa6f99ff63347bb63d06ebfc9e607c51d.html#aa6f99ff63347bb63d06ebfc9e607c51d) |
|  | |
| void(\* | [RemoveMediaSource](structak__wwise__plugin__host__object__media__v1_a8a1faa881532affb5ea85acd51a0a585.html#a8a1faa881532affb5ea85acd51a0a585) )(struct [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) \*in\_this, unsigned int in\_Index) |
|  | Requests to remove the specified index file as data input file. [更多...](structak__wwise__plugin__host__object__media__v1_a8a1faa881532affb5ea85acd51a0a585.html#a8a1faa881532affb5ea85acd51a0a585) |
|  | |
| unsigned int(\* | [GetMediaSourceCount](structak__wwise__plugin__host__object__media__v1_a8fe4f5d24a807283fe9fd36c3fc69a98.html#a8fe4f5d24a807283fe9fd36c3fc69a98) )(const struct [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) \*in\_this) |
|  | Retrieve the number of media source indexes. [更多...](structak__wwise__plugin__host__object__media__v1_a8fe4f5d24a807283fe9fd36c3fc69a98.html#a8fe4f5d24a807283fe9fd36c3fc69a98) |
|  | |
| unsigned int(\* | [GetMediaSourceFileName](structak__wwise__plugin__host__object__media__v1_aa042fbafc6c9b84bc7021f40e7a71571.html#aa042fbafc6c9b84bc7021f40e7a71571) )(const struct [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) \*in\_this, [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszFileName, unsigned int in\_uiBufferSize, unsigned int in\_Index) |
|  | Retrieve the file name of the source plug-in data at the specified index, as provided in SetMediaSource. [更多...](structak__wwise__plugin__host__object__media__v1_aa042fbafc6c9b84bc7021f40e7a71571.html#aa042fbafc6c9b84bc7021f40e7a71571) |
|  | |
| unsigned int(\* | [GetMediaSourceOriginalFilePath](structak__wwise__plugin__host__object__media__v1_a751ac070a659205d528f9e56eab9a5e8.html#a751ac070a659205d528f9e56eab9a5e8) )(const struct [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) \*in\_this, [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszFilePath, unsigned int in\_uiBufferSize, unsigned int in\_Index) |
|  | Retrieve the full file path of the source plug-in data at the specified index. [更多...](structak__wwise__plugin__host__object__media__v1_a751ac070a659205d528f9e56eab9a5e8.html#a751ac070a659205d528f9e56eab9a5e8) |
|  | |
| unsigned int(\* | [GetMediaSourceConvertedFilePath](structak__wwise__plugin__host__object__media__v1_a30845ea55408be0ff4aa9f7751c2bb81.html#a30845ea55408be0ff4aa9f7751c2bb81) )(const struct [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) \*in\_this, [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszFilePath, unsigned int in\_uiBufferSize, const GUID \*in\_guidPlatform, unsigned int in\_Index) |
|  | Retrieve the full file path of the converted plug-in data at the specified index. [更多...](structak__wwise__plugin__host__object__media__v1_a30845ea55408be0ff4aa9f7751c2bb81.html#a30845ea55408be0ff4aa9f7751c2bb81) |
|  | |
| void(\* | [InvalidateMediaSource](structak__wwise__plugin__host__object__media__v1_a07f46f25ef9cb73dd268cde26c4435e6.html#a07f46f25ef9cb73dd268cde26c4435e6) )(struct [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) \*in\_this, unsigned int in\_Index) |
|  | Request Wwise to perform any required conversion on the data. [更多...](structak__wwise__plugin__host__object__media__v1_a07f46f25ef9cb73dd268cde26c4435e6.html#a07f46f25ef9cb73dd268cde26c4435e6) |
|  | |
| unsigned int(\* | [GetOriginalDirectory](structak__wwise__plugin__host__object__media__v1_aa2b51f87cebf98b0d5046c8779422a02.html#aa2b51f87cebf98b0d5046c8779422a02) )(const struct [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) \*in\_this, [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszDirectory, unsigned int in\_uiBufferSize) |
|  | Obtain the Original directory for the plug-in. [更多...](structak__wwise__plugin__host__object__media__v1_aa2b51f87cebf98b0d5046c8779422a02.html#aa2b51f87cebf98b0d5046c8779422a02) |
|  | |
| unsigned int(\* | [GetConvertedDirectory](structak__wwise__plugin__host__object__media__v1_a87173e2b037d7b1ff33117801c9a5558.html#a87173e2b037d7b1ff33117801c9a5558) )(const struct [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) \*in\_this, [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszDirectory, unsigned int in\_uiBufferSize, const GUID \*in\_guidPlatform) |
|  | Obtain the Converted directory for the plug-in and platform. [更多...](structak__wwise__plugin__host__object__media__v1_a87173e2b037d7b1ff33117801c9a5558.html#a87173e2b037d7b1ff33117801c9a5558) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Plug-in object media interface. Can be used to normalize media file handling inside the project.

在文件 [HostObjectMedia.h](_host_object_media_8h_source.html) 第 [41](_host_object_media_8h_source.html#l00041) 行定义.