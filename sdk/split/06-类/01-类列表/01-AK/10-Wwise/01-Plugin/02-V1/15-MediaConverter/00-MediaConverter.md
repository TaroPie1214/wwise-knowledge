# MediaConverter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [MediaConverter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::MediaConverter类 参考abstract

`#include <MediaConverter.h>`

类 AK.Wwise::Plugin::V1::MediaConverter 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_acffaf98189762c1d0ced10a843aa3de9.html#acffaf98189762c1d0ced10a843aa3de9a6088f2283e327ac537a335bf49316bff) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_MEDIA\_CONVERTER } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_acffaf98189762c1d0ced10a843aa3de9.html#acffaf98189762c1d0ced10a843aa3de9) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_af75ca49ca90dc7703e9d9cfc893143ef.html#af75ca49ca90dc7703e9d9cfc893143efa27ff9cfdc55b96c0109aeb4e0d84ca49) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_af75ca49ca90dc7703e9d9cfc893143ef.html#af75ca49ca90dc7703e9d9cfc893143ef) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_aa3e1295a4580cf18fb755af5922edad9.html#aa3e1295a4580cf18fb755af5922edad9) () |
|  | |
| [CMediaConverter::Instance](structak__wwise__plugin__media__converter__v1_ac6e901fa00774f0486023c19d982622a.html#ac6e901fa00774f0486023c19d982622a) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_aed8e62cc7c9021e25b4bfe14bdf6599c.html#aed8e62cc7c9021e25b4bfe14bdf6599c) () |
|  | |
| const [CMediaConverter::Instance](structak__wwise__plugin__media__converter__v1_ac6e901fa00774f0486023c19d982622a.html#ac6e901fa00774f0486023c19d982622a) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_a6e13761f6542321a28ae3fce1edba4cb.html#a6e13761f6542321a28ae3fce1edba4cb) () const |
|  | |
|  | [MediaConverter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_a91820264c38c2a794a84a836b779c0f8.html#a91820264c38c2a794a84a836b779c0f8) () |
|  | |
| virtual | [~MediaConverter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_a5a90aa73a0669ebf89748730a55e2ff2.html#a5a90aa73a0669ebf89748730a55e2ff2) () |
|  | |
| virtual [ConversionResult](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3) | [ConvertFile](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_a4324f69ea75774cbb8270c01bf607dd7.html#a4324f69ea75774cbb8270c01bf607dd7) (const GUID &in\_guidPlatform, const [BasePlatformID](struct_base_platform_i_d.html) &in\_basePlatform, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_szSourceFile, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_szDestFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uSampleRate, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uBlockLength, [IProgress](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress.html) \*in\_pProgress, [IWriteString](class_a_k_1_1_wwise_1_1_plugin_1_1_i_write_string.html) \*io\_pError) const =0 |
|  | Converts a file. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_a4324f69ea75774cbb8270c01bf607dd7.html#a4324f69ea75774cbb8270c01bf607dd7) |
|  | |
| virtual uint32\_t | [GetCurrentConversionSettingsHash](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_a5523307ba4ba9bd1debd7d8cf40e3f5e.html#a5523307ba4ba9bd1debd7d8cf40e3f5e) (const GUID &in\_guidPlatform, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uSampleRate=0, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uBlockLength=0) const =0 |
|  | Calculates the conversion setting's hash. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_a5523307ba4ba9bd1debd7d8cf40e3f5e.html#a5523307ba4ba9bd1debd7d8cf40e3f5e) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

在文件 [MediaConverter.h](_media_converter_8h_source.html) 第 [124](_media_converter_8h_source.html#l00124) 行定义.