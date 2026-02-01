# AkOutputDeviceInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_output_device_info-members.html) |
[Public 属性](#pub-attribs)

AkOutputDeviceInfo结构体 参考

`#include <AkSoundEngineTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) | [pluginID](struct_ak_output_device_info_a7c7ee58e40f2d6a691be85aee49aec80.html#a7c7ee58e40f2d6a691be85aee49aec80) |
|  | Full plugin ID, including company ID and plugin type. See AKMAKECLASSID macro. [更多...](struct_ak_output_device_info_a7c7ee58e40f2d6a691be85aee49aec80.html#a7c7ee58e40f2d6a691be85aee49aec80) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [audioDeviceShareset](struct_ak_output_device_info_ae6e053118b85fc2f2d169eda3246da41.html#ae6e053118b85fc2f2d169eda3246da41) |
|  | ID of shareset for this output device [更多...](struct_ak_output_device_info_ae6e053118b85fc2f2d169eda3246da41.html#ae6e053118b85fc2f2d169eda3246da41) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [idDevice](struct_ak_output_device_info_a8b055436623a200feb494068df276b0f.html#a8b055436623a200feb494068df276b0f) |
|  | Device ID that was specified in the Output Settings for this output device [更多...](struct_ak_output_device_info_a8b055436623a200feb494068df276b0f.html#a8b055436623a200feb494068df276b0f) |
|  | |
| struct [AkChannelConfig](struct_ak_channel_config.html) | [channelConfig](struct_ak_output_device_info_a6121e3ee0248ed794aef054b6a8cf390.html#a6121e3ee0248ed794aef054b6a8cf390) |
|  | Channel configuration of the output device [更多...](struct_ak_output_device_info_a6121e3ee0248ed794aef054b6a8cf390.html#a6121e3ee0248ed794aef054b6a8cf390) |
|  | |
| struct [Ak3DAudioSinkCapabilities](struct_ak3_d_audio_sink_capabilities.html) | [capabilities](struct_ak_output_device_info_a0452602c2f28ee38b78b05177c165b0d.html#a0452602c2f28ee38b78b05177c165b0d) |
|  | 3D Audio capabilities of the output device instance [更多...](struct_ak_output_device_info_a0452602c2f28ee38b78b05177c165b0d.html#a0452602c2f28ee38b78b05177c165b0d) |
|  | |
| void \* | [customData](struct_ak_output_device_info_ae8c94cc6453d7bdab7bf967aa80ee32e.html#ae8c94cc6453d7bdab7bf967aa80ee32e) |
|  | Custom data containing additional information about the device. This is plug-in implementation-defined. For Wwise Motion, this can be cast to [AkMotionDeviceData](struct_ak_motion_device_data.html). [更多...](struct_ak_output_device_info_ae8c94cc6453d7bdab7bf967aa80ee32e.html#ae8c94cc6453d7bdab7bf967aa80ee32e) |
|  | |

## 详细描述

Information about an output device instance.

This data can be retrieved by plug-ins via [AK::IAkPluginContextBase::GetOutputDeviceInfo](class_a_k_1_1_i_ak_plugin_context_base_a63d145ee193a2498bd18c36d1da22f85.html#a63d145ee193a2498bd18c36d1da22f85).

在文件 [AkSoundEngineTypes.h](_ak_sound_engine_types_8h_source.html) 第 [88](_ak_sound_engine_types_8h_source.html#l00088) 行定义.