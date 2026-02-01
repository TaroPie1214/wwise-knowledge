# PluginDef.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[类型定义](#typedef-members) |
[枚举](#enum-members)

PluginDef.h 文件参考

Wwise Authoring Plug-ins - Base plug-in definitions
[更多...](#details)

`#include "PluginHelpers.h"`  
`#include "PluginInstanceTypes.h"`  
`#include "../../SoundEngine/Common/IAkPlugin.h"`

[浏览源代码.](_plugin_def_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AK.Wwise::Plugin::LicenseID](struct_a_k_1_1_wwise_1_1_plugin_1_1_license_i_d.html) |
|  | |
| struct | [AK.Wwise::Plugin::MonitorData](struct_a_k_1_1_wwise_1_1_plugin_1_1_monitor_data.html) |
|  | |
| struct | [AK.Wwise::Plugin::PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html) |
|  | |
| class | [AK.Wwise::Plugin::IProgress](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress.html) |
|  | |
| class | [AK.Wwise::Plugin::IWriteString](class_a_k_1_1_wwise_1_1_plugin_1_1_i_write_string.html) |
|  | |
| class | [AK.Wwise::Plugin::IReadOnlyProperties](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties.html) |
|  | Interfaces used to set and get the properties from a plug in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties.html#details) |
|  | |
| class | [AK.Wwise::Plugin::IReadWriteProperties](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties.html) |
|  | |
| struct | [AK.Wwise::Plugin::RiffHeader](struct_a_k_1_1_wwise_1_1_plugin_1_1_riff_header.html) |
|  | |
| struct | [AK.Wwise::Plugin::ConversionContext](struct_a_k_1_1_wwise_1_1_plugin_1_1_conversion_context.html) |
|  | |
| struct | [AK.Wwise::Plugin::ConvertedFileInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info.html) |
|  | |
| struct | [AK.Wwise::Plugin::OpenedConvertedFile](struct_a_k_1_1_wwise_1_1_plugin_1_1_opened_converted_file.html) |
|  | |
| struct | [ak\_wwise\_plugin\_undo\_event\_pair\_v1](structak__wwise__plugin__undo__event__pair__v1.html) |
|  | A definition of an undo event, with a specific interface and instance. [更多...](structak__wwise__plugin__undo__event__pair__v1.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::WwiseAuthoringAPI](namespace_a_k_1_1_wwise_authoring_a_p_i.html) |
|  | |
| namespace | [AK.Wwise](namespace_a_k_1_1_wwise.html) |
|  | |
|  | [AK::Wwise::Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef int | [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) |
|  | Unique identifier for a particular undo group. Useful to reopen an unapplied closed group session. [更多...](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) |
|  | |
| typedef uint32\_t | [ak\_wwise\_plugin\_property\_set\_braces](group__global_ga9e89de3693d568e58c5ef76bda84afbe.html#ga9e89de3693d568e58c5ef76bda84afbe) |
|  | Bitfield composed of values defined in `ak_wwise_plugin_property_set_braces_values` [更多...](group__global_ga9e89de3693d568e58c5ef76bda84afbe.html#ga9e89de3693d568e58c5ef76bda84afbe) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AK::Wwise::Plugin::LicenseType](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) { [AK::Wwise::Plugin::LicenseType\_Trial](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eba0fde948d3400bb26cd990ddefa70c77e) = 1, [AK::Wwise::Plugin::LicenseType\_Purchased](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eba15f3c33f220668c5a63d7245af208453), [AK::Wwise::Plugin::LicenseType\_Academic](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eba675553ed9581a261b6cd2028bacd8765) } |
|  | License type. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) |
|  | |
| enum | [AK::Wwise::Plugin::LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) { [AK::Wwise::Plugin::LicenseStatus\_Unlicensed](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4a8c8e1cff83b5e9cc5530fa23d7960ef1), [AK::Wwise::Plugin::LicenseStatus\_Expired](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4a18ce8e3a9a59b5ad2225ccfc11619426), [AK::Wwise::Plugin::LicenseStatus\_Valid](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4aa086b65bb2c637bdb40c1fe2f221323b), [AK::Wwise::Plugin::LicenseStatus\_Incompatible](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4a1388a62f60f5e74c0a378c8d8dbf6084) } |
|  | License status. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) |
|  | |
| enum | [AK::Wwise::Plugin::NotifyInnerObjectOperation](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987) { [AK::Wwise::Plugin::InnerObjectAdded](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987aaa6143b3eef559abe9343de72a8d8aae), [AK::Wwise::Plugin::InnerObjectRemoved](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987ae45d4ed0bf48bc0b4bd0c9b7c6b1075e) } |
|  | Type of operation for the NotifyInnerObjectAddedRemoved function. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987) |
|  | |
| enum | [AK::Wwise::Plugin::AudioFileChannel](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bd) {     [AK::Wwise::Plugin::Channel\_mono](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bdad8a49f18aa2494a325962d8e61490eb9) = 0, [AK::Wwise::Plugin::Channel\_stereo](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bda9011abe7c385ca940570417bfc6b693c) = 1, [AK::Wwise::Plugin::Channel\_mono\_drop](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bdab4e8b33959e6c90b5b367f6186e295a3) = 2, [AK::Wwise::Plugin::Channel\_stereo\_drop](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bda965d9a650d2b3dbab8d3f938df25ff66) = 3,     [AK::Wwise::Plugin::Channel\_as\_input](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bdae7e5b4dced0ca81802b11356c9fb6232) = 4, [AK::Wwise::Plugin::Channel\_mono\_drop\_right](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bda8f4b646bf486d9881566725bc596258a) = 5, [AK::Wwise::Plugin::Channel\_stereo\_balance](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bda7b25cc13404f2390bbc8cbb99a8cfab0) = 6   } |
|  | Import channel configuration options. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bd) |
|  | |
| enum | [AK::Wwise::Plugin::Severity](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67ed) {     [AK::Wwise::Plugin::Severity\_Success](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67eda154bdeafd831a9c2856c3c797a37d1f0) = -1, [AK::Wwise::Plugin::Severity\_Message](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67eda8985c15e804661fa6ca4fce0873d058b), [AK::Wwise::Plugin::Severity\_Warning](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67eda35f7fb0c5c0a59246ed922eb6af25794), [AK::Wwise::Plugin::Severity\_Error](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67edad6614394580b0bd272920538d93652f4),     [AK::Wwise::Plugin::Severity\_FatalError](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67eda88ae24bc50f05715c7bcd50e4d8e998d)   } |
|  | Log message severity. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67ed) |
|  | |
| enum | [AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) { [AK::Wwise::Plugin::SettingsDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da70f74e61c5e7bef5d95559c73c9978cc), [AK::Wwise::Plugin::ContentsEditorDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da6d085e723d1240d119005b403573dfb5) } |
|  | |
| enum | [AK::Wwise::Plugin::ConversionResult](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3) { [AK::Wwise::Plugin::ConversionSuccess](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3a292220d538f5f5381f6f0514c782059f) = 0, [AK::Wwise::Plugin::ConversionWarning](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3a0ec71d22a31f1cd710e9521200e0d1f2) = 1, [AK::Wwise::Plugin::ConversionFailed](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3a067c828fdfd88765697e4914fa192efc) = 2 } |
|  | Conversion error code. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3) |
|  | |
| enum | [ak\_wwise\_plugin\_undo\_group\_close\_action](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#ga49b0af3e4205b935aa476d7ab1c9f65c) {     [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_CLOSE](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65cab2808bcde599ec2d8622deb9ddb449f3), [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_APPLY](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65ca7b066ecc400936abe8602ec9deb27e5f), [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_APPLY\_FIRST\_EVENT\_NAME](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65cacd212f32bc852fcb9abc5a44bf906776), [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_APPLY\_LAST\_EVENT\_NAME](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65ca9b23a997b9bde905fbb6a1282a601f93),     [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_CANCEL](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65cac2211c2692785e248eaa51ffd5e4c0dd)   } |
|  | Action to apply once this undo group is closed. [更多...](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#ga49b0af3e4205b935aa476d7ab1c9f65c) |
|  | |
| enum | [ak\_wwise\_plugin\_property\_set\_braces\_values](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#ga3cfc97efdbbda4629a10f0e53e914eb9) {     [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_NO\_NOTIFY](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a6dff872c6af8fb5f681332bef9926c58) = 1 << 0, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_NO\_UNDO\_EVENTS](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9ab38bef13078d1c5551ed26629a62920c) = 1 << 1, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_SET\_VALUE](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a2d3687f237127acb70930ab25721d775) = 1 << 2, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_REORDER\_CHILDREN](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9ad88f6db345109a3b576a42832153ee88) = 1 << 3,     [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_DISABLE\_PROPERTY\_CONSTRAINTS](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a8c890977bfa84797f378e909e75066f7) = 1 << 4, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_NO\_DIRTY](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9aa950b9a5fe6890beb0816607483361a7) = 1 << 5, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_CREATE\_PROPERTY\_ON\_SET\_VALUE](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a495faffff7fa5e3a9b86e9bb8b247624) = 1 << 6, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_CHANGE\_TO\_EXISTING\_VALUE\_TYPE](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9ac740cc44214287bc9ae50b8bfcb87265) = 1 << 7,     [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_LOADING](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a82ad89401e7643e3db226f15e9acdf90) = 1 << 8, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_UNLOADING](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a48784d71f3015ddf7cc7def725db76ad) = 1 << 9, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_DELETING](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9af6b7ca3eb4b0186443eb76b4d7d8b934) = 1 << 10, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_SET\_OBJECT\_LIST](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9afa248dae2ff331d3a544ea0fae47a0f0) = 1 << 11   } |
|  | Bitfield values of brace types, used to delay or avoid certain actions normally triggered as a result of a property set mutation. [更多...](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#ga3cfc97efdbbda4629a10f0e53e914eb9) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Base plug-in definitions

在文件 [PluginDef.h](_plugin_def_8h_source.html) 中定义.