# IAkPluginServiceAudioObjectAttenuation

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceAudioObjectAttenuation](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginServiceAudioObjectAttenuation类 参考abstract

Interface for the services related to extracting attenuation curves from audio objects and using them.
[更多...](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation.html#details)

`#include <IAkPlugin.h>`

类 AK::IAkPluginServiceAudioObjectAttenuation 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [GetAttenuation](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_af668b5dd447b40eedc097a3555cdfc61.html#af668b5dd447b40eedc097a3555cdfc61) (const [AkAudioObject](struct_ak_audio_object.html) &in\_object, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_distanceScaling) const =0 |
|  | |
| virtual bool | [ExtractCurves](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_a9fd0aceaaac87aecc88a7458aae48ed2.html#a9fd0aceaaac87aecc88a7458aae48ed2) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, const [AkAudioObject](struct_ak_audio_object.html) &in\_object, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_curveTypesMask, void \*out\_curves[]) const =0 |
|  | |
| virtual void | [Delete](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_af1edd8f1ee7a3ab12f9e3a726dcd5294.html#af1edd8f1ee7a3ab12f9e3a726dcd5294) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, void \*&io\_attenuationCurve)=0 |
|  | Free memory of curve obtained with AK::IAkPluginServiceAttenuationCurve::ExtractCurves. [更多...](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_af1edd8f1ee7a3ab12f9e3a726dcd5294.html#af1edd8f1ee7a3ab12f9e3a726dcd5294) |
|  | |
| virtual [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Evaluate](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_a1890704e590af2f7c3d75b4b2c4cc028.html#a1890704e590af2f7c3d75b4b2c4cc028) (void \*&io\_attenuationCurve, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) x)=0 |
|  | Evaluate the value of a curve at given x coordinate. [更多...](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_a1890704e590af2f7c3d75b4b2c4cc028.html#a1890704e590af2f7c3d75b4b2c4cc028) |
|  | |
| virtual void | [Linearize](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_a8a091dad213e19ca2c94c4ab0e094155.html#a8a091dad213e19ca2c94c4ab0e094155) (void \*&io\_attenuationCurve)=0 |
|  | Some curves are serialized in the log domain. Use this function to convert all the points to linear at once. [更多...](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_a8a091dad213e19ca2c94c4ab0e094155.html#a8a091dad213e19ca2c94c4ab0e094155) |
|  | |
| virtual const [AkRTPCGraphPoint](_ak_sound_engine_types_8h_aa706b42f8491bd4cd738427a53f04519.html#aa706b42f8491bd4cd738427a53f04519) & | [GetPoint](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_a37a8e4da84eb75e689d34568ea096668.html#a37a8e4da84eb75e689d34568ea096668) (const void \*in\_attenuationCurve, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) i) const =0 |
|  | Get the ith point of the curve. [更多...](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_a37a8e4da84eb75e689d34568ea096668.html#a37a8e4da84eb75e689d34568ea096668) |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetNumPoints](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_ad00a8396a968566d5870e16a33b5ff4c.html#ad00a8396a968566d5870e16a33b5ff4c) (const void \*in\_attenuationCurve) const =0 |
|  | Get the number of points on a curve. [更多...](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_ad00a8396a968566d5870e16a33b5ff4c.html#ad00a8396a968566d5870e16a33b5ff4c) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServiceAudioObjectAttenuation](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation_a2ae0caa31ce4afeca6d259f0fb29f8e0.html#a2ae0caa31ce4afeca6d259f0fb29f8e0) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

## 详细描述

Interface for the services related to extracting attenuation curves from audio objects and using them.

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1869](_i_ak_plugin_8h_source.html#l01869) 行定义.