# CustomMetadata

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkAudioObject](struct_ak_audio_object.html)
- [CustomMetadata](struct_ak_audio_object_1_1_custom_metadata.html)

[所有成员列表](struct_ak_audio_object_1_1_custom_metadata-members.html) |
[Public 属性](#pub-attribs)

AkAudioObject::CustomMetadata结构体 参考

Custom object metadata.
[更多...](struct_ak_audio_object_1_1_custom_metadata.html#details)

`#include <AkAudioObject.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) | [pluginID](struct_ak_audio_object_1_1_custom_metadata_ae105d977b4642020ac679ac44ad25fd3.html#ae105d977b4642020ac679ac44ad25fd3) |
|  | Full plugin ID, including company ID and plugin type. See AKMAKECLASSID macro. [更多...](struct_ak_audio_object_1_1_custom_metadata_ae105d977b4642020ac679ac44ad25fd3.html#ae105d977b4642020ac679ac44ad25fd3) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [contextID](struct_ak_audio_object_1_1_custom_metadata_adc214e4ad956fcc505c76a30cd351a3f.html#adc214e4ad956fcc505c76a30cd351a3f) |
|  | (Profiling) ID of the sound or bus from which the custom metadata was fetched. [更多...](struct_ak_audio_object_1_1_custom_metadata_adc214e4ad956fcc505c76a30cd351a3f.html#adc214e4ad956fcc505c76a30cd351a3f) |
|  | |
| [AK::IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html) \* | [pParam](struct_ak_audio_object_1_1_custom_metadata_a57b7c2bd330d588f1a66ef910afd0ff3.html#a57b7c2bd330d588f1a66ef910afd0ff3) |
|  | Custom, pluggable medata. Note: any custom metadata is expected to exist for only the current sound engine render tick, and persistent references to it should not be stored. [更多...](struct_ak_audio_object_1_1_custom_metadata_a57b7c2bd330d588f1a66ef910afd0ff3.html#a57b7c2bd330d588f1a66ef910afd0ff3) |
|  | |

## 详细描述

Custom object metadata.

在文件 [AkAudioObject.h](_ak_audio_object_8h_source.html) 第 [73](_ak_audio_object_8h_source.html#l00073) 行定义.