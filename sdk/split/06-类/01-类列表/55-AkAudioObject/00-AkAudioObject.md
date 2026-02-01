# AkAudioObject

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_audio_object-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs) |
[静态 Public 属性](#pub-static-attribs)

AkAudioObject结构体 参考

`#include <AkAudioObject.h>`

|  |  |
| --- | --- |
| 类 | |
| class | [ArrayCustomMetadata](class_ak_audio_object_1_1_array_custom_metadata.html) |
|  | Array type for carrying custom metadata. [更多...](class_ak_audio_object_1_1_array_custom_metadata.html#details) |
|  | |
| struct | [CustomMetadata](struct_ak_audio_object_1_1_custom_metadata.html) |
|  | Custom object metadata. [更多...](struct_ak_audio_object_1_1_custom_metadata.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| typedef [AkString](class_ak_string.html)< [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html), char > | [String](struct_ak_audio_object_a4221b169c325991e10845a276c538f21.html#a4221b169c325991e10845a276c538f21) |
|  | String type for use in 3D audio objects. [更多...](struct_ak_audio_object_a4221b169c325991e10845a276c538f21.html#a4221b169c325991e10845a276c538f21) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkAudioObject](struct_ak_audio_object_af2c75dd57b033a7eb4f59f82f2b1310c.html#af2c75dd57b033a7eb4f59f82f2b1310c) () |
|  | Constructor [更多...](struct_ak_audio_object_af2c75dd57b033a7eb4f59f82f2b1310c.html#af2c75dd57b033a7eb4f59f82f2b1310c) |
|  | |
|  | [~AkAudioObject](struct_ak_audio_object_ab6f5f7df55fbf830b86e674b0c74ba66.html#ab6f5f7df55fbf830b86e674b0c74ba66) () |
|  | Destructor [更多...](struct_ak_audio_object_ab6f5f7df55fbf830b86e674b0c74ba66.html#ab6f5f7df55fbf830b86e674b0c74ba66) |
|  | |
| void | [CopyContents](struct_ak_audio_object_a2c272633ee504446ed98e750d3d167c4.html#a2c272633ee504446ed98e750d3d167c4) (const [AkAudioObject](struct_ak_audio_object.html) &in\_src) |
|  | Copies object metadata (everything but the key) from another object. [更多...](struct_ak_audio_object_a2c272633ee504446ed98e750d3d167c4.html#a2c272633ee504446ed98e750d3d167c4) |
|  | |
| void | [TransferContents](struct_ak_audio_object_afa82a3b8551f12ca4131b8ada27f8c28.html#afa82a3b8551f12ca4131b8ada27f8c28) ([AkAudioObject](struct_ak_audio_object.html) &in\_src) |
|  | Moves object metadata (everything but the key) from another object. [更多...](struct_ak_audio_object_afa82a3b8551f12ca4131b8ada27f8c28.html#afa82a3b8551f12ca4131b8ada27f8c28) |
|  | |
| void | [SetCustomMetadata](struct_ak_audio_object_a6b1c22b86b4e3f4b6d43316ee177d747.html#a6b1c22b86b4e3f4b6d43316ee177d747) ([CustomMetadata](struct_ak_audio_object_1_1_custom_metadata.html) \*in\_aCustomMetadata, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLength) |
|  | |
| void | [Transfer](struct_ak_audio_object_ac0d4bdf0602d9470ead5461eb40ed6ef.html#ac0d4bdf0602d9470ead5461eb40ed6ef) ([AkAudioObject](struct_ak_audio_object.html) &in\_from) |
|  | Transfer function for transfer move policies. [更多...](struct_ak_audio_object_ac0d4bdf0602d9470ead5461eb40ed6ef.html#ac0d4bdf0602d9470ead5461eb40ed6ef) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetName](struct_ak_audio_object_a0254e6325540e0edec1c72a19a39d70d.html#a0254e6325540e0edec1c72a19a39d70d) ([AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, const char \*in\_szName) |
|  | |
| void | [ResetState](struct_ak_audio_object_ab6614dc5c330ce98499c97f041b5ce82.html#ab6614dc5c330ce98499c97f041b5ce82) () |
|  | Reset object state in preparation for next frame. [更多...](struct_ak_audio_object_ab6614dc5c330ce98499c97f041b5ce82.html#ab6614dc5c330ce98499c97f041b5ce82) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkAudioObjectID](_ak_typedefs_8h_a6cadc0376ae4f945438db69f6306f21a.html#a6cadc0376ae4f945438db69f6306f21a) | [key](struct_ak_audio_object_a4b5cc754786f067fa2b3fbed875652d8.html#a4b5cc754786f067fa2b3fbed875652d8) |
|  | Unique ID, local to a given bus. Only the lower 56 of 64 bits are used for the object itself. The highest 8 bits are available for channel indexing. [更多...](struct_ak_audio_object_a4b5cc754786f067fa2b3fbed875652d8.html#a4b5cc754786f067fa2b3fbed875652d8) |
|  | |
| [AkPositioningData](struct_ak_positioning_data.html) | [positioning](struct_ak_audio_object_a1dccda4d0468b93e4347842a9de4e98e.html#a1dccda4d0468b93e4347842a9de4e98e) |
|  | Positioning data for deferred 3D rendering. [更多...](struct_ak_audio_object_a1dccda4d0468b93e4347842a9de4e98e.html#a1dccda4d0468b93e4347842a9de4e98e) |
|  | |
| [AkRamp](struct_ak_ramp.html) | [cumulativeGain](struct_ak_audio_object_a3013d844d7544da19d30cf90bef6aef5.html#a3013d844d7544da19d30cf90bef6aef5) |
|  | Cumulative ramping gain to apply when mixing down to speaker bed or final endpoint [更多...](struct_ak_audio_object_a3013d844d7544da19d30cf90bef6aef5.html#a3013d844d7544da19d30cf90bef6aef5) |
|  | |
| [AkPipelineID](_ak_typedefs_8h_aa1f98bb2addc6fbfe759902751548cbc.html#aa1f98bb2addc6fbfe759902751548cbc) | [instigatorID](struct_ak_audio_object_aa66019a628335335705ba44114bd2484.html#aa66019a628335335705ba44114bd2484) |
|  | Profiling ID of the node from which the object stems (typically the voice, instance of a Property Container). [更多...](struct_ak_audio_object_aa66019a628335335705ba44114bd2484.html#aa66019a628335335705ba44114bd2484) |
|  | |
| [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) | [priority](struct_ak_audio_object_a09ff304d835f52dc44b8caa1521de69a.html#a09ff304d835f52dc44b8caa1521de69a) |
|  | Audio object playback priority. Object with a higher priority will be rendered using the hardware's object functionality on platforms that supports it, whereas objects with a lower priority will be downmixed to a lower resolution 3D bed. Audio object priorities should be retrieved, or set through IAkPluginServiceAudioObjectPriority to retain compatibility with future Wwise releases. [更多...](struct_ak_audio_object_a09ff304d835f52dc44b8caa1521de69a.html#a09ff304d835f52dc44b8caa1521de69a) |
|  | |
| [ArrayCustomMetadata](class_ak_audio_object_1_1_array_custom_metadata.html) | [arCustomMetadata](struct_ak_audio_object_a40f457c25d198d643eb3a93fd844771f.html#a40f457c25d198d643eb3a93fd844771f) |
|  | Array of custom metadata, gathered from visited objects. Note: any custom metadata is expected to exist for only the current sound engine render tick, and persistent references to it should not be stored. [更多...](struct_ak_audio_object_a40f457c25d198d643eb3a93fd844771f.html#a40f457c25d198d643eb3a93fd844771f) |
|  | |
| [String](struct_ak_audio_object_a4221b169c325991e10845a276c538f21.html#a4221b169c325991e10845a276c538f21) | [objectName](struct_ak_audio_object_a091f4368a679f03a5c00d2ac6fce2371.html#a091f4368a679f03a5c00d2ac6fce2371) |
|  | Name string of the object, to appear in the object profiler. This is normally used by out-of-place object processors for naming their output objects. Built-in sound engine structures don't use it. [更多...](struct_ak_audio_object_a091f4368a679f03a5c00d2ac6fce2371.html#a091f4368a679f03a5c00d2ac6fce2371) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static const [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [kObjectKeyNumBits](struct_ak_audio_object_a55bf608735a909fb819a10799dbf7b31.html#a55bf608735a909fb819a10799dbf7b31) = 56 |
|  | |
| static const [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [kObjectKeyMask](struct_ak_audio_object_aab7d888dea9a214f2dbe6b42521b6941.html#aab7d888dea9a214f2dbe6b42521b6941) = ((([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec))1 << [kObjectKeyNumBits](struct_ak_audio_object_a55bf608735a909fb819a10799dbf7b31.html#a55bf608735a909fb819a10799dbf7b31)) - 1) |
|  | |

## 详细描述

An audio object refers to an audio signal with some attached metadata going through the sound engine pipeline. The [AkAudioObject](struct_ak_audio_object.html) struct encapsulates the metadata part. The signal itself is contained in a separate [AkAudioBuffer](class_ak_audio_buffer.html) instance.

在文件 [AkAudioObject.h](_ak_audio_object_8h_source.html) 第 [45](_ak_audio_object_8h_source.html#l00045) 行定义.