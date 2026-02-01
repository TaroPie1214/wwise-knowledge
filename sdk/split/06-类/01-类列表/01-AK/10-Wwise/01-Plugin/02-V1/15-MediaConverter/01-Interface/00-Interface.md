# Interface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [MediaConverter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter.html)
- [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::MediaConverter::Interface结构体 参考

The C interface, fulfilled by your plug-in.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface.html#details)

`#include <MediaConverter.h>`

类 AK.Wwise::Plugin::V1::MediaConverter::Interface 继承关系图:

![](../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface_adada0e05d37ea6836ce94ec3e64283c8.html#adada0e05d37ea6836ce94ec3e64283c8) = [MediaConverter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter.html) |
|  | |
| - Public 类型 继承自 [ak\_wwise\_plugin\_media\_converter\_v1](structak__wwise__plugin__media__converter__v1.html) | |
| using | [Instance](structak__wwise__plugin__media__converter__v1_ac6e901fa00774f0486023c19d982622a.html#ac6e901fa00774f0486023c19d982622a) = [ak\_wwise\_plugin\_media\_converter\_instance\_v1](structak__wwise__plugin__media__converter__instance__v1.html) |
|  | Base instance type for providing custom media conversion. [更多...](structak__wwise__plugin__media__converter__v1_ac6e901fa00774f0486023c19d982622a.html#ac6e901fa00774f0486023c19d982622a) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface_a5e7114e0468d872fcfbdb1438aaa6345.html#a5e7114e0468d872fcfbdb1438aaa6345) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_media\_converter\_v1](structak__wwise__plugin__media__converter__v1.html) | |
|  | [ak\_wwise\_plugin\_media\_converter\_v1](structak__wwise__plugin__media__converter__v1_a5ad01a7be502667b3ec9b435e72f3d83.html#a5ad01a7be502667b3ec9b435e72f3d83) () |
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
| 额外继承的成员函数 | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_media\_converter\_v1](structak__wwise__plugin__media__converter__v1.html) | |
| [AK::Wwise::Plugin::ConversionResult](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3)(\* | [ConvertFile](structak__wwise__plugin__media__converter__v1_a3c66fa45a817b7ab9e4ec83146fdebe0.html#a3c66fa45a817b7ab9e4ec83146fdebe0) )(const struct [ak\_wwise\_plugin\_media\_converter\_instance\_v1](structak__wwise__plugin__media__converter__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const [BasePlatformID](struct_base_platform_i_d.html) \*in\_basePlatform, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_szSourceFile, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_szDestFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uSampleRate, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uBlockLength, [AK::Wwise::Plugin::IProgress](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress.html) \*in\_pProgress, [AK::Wwise::Plugin::IWriteString](class_a_k_1_1_wwise_1_1_plugin_1_1_i_write_string.html) \*io\_pError) |
|  | Converts a file. [更多...](structak__wwise__plugin__media__converter__v1_a3c66fa45a817b7ab9e4ec83146fdebe0.html#a3c66fa45a817b7ab9e4ec83146fdebe0) |
|  | |
| uint32\_t(\* | [GetCurrentConversionSettingsHash](structak__wwise__plugin__media__converter__v1_af34464d0979062fae50f8417c1ae984b.html#af34464d0979062fae50f8417c1ae984b) )(const struct [ak\_wwise\_plugin\_media\_converter\_instance\_v1](structak__wwise__plugin__media__converter__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uSampleRate, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uBlockLength) |
|  | Calculates the conversion setting's hash. [更多...](structak__wwise__plugin__media__converter__v1_af34464d0979062fae50f8417c1ae984b.html#af34464d0979062fae50f8417c1ae984b) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

The C interface, fulfilled by your plug-in.

在文件 [MediaConverter.h](_media_converter_8h_source.html) 第 [151](_media_converter_8h_source.html#l00151) 行定义.