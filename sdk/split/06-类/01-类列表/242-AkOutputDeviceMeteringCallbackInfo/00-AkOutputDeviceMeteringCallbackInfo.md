# AkOutputDeviceMeteringCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_output_device_metering_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkOutputDeviceMeteringCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

类 AkOutputDeviceMeteringCallbackInfo 继承关系图:

![](../../../images/struct_ak_output_device_metering_callback_info.png)

|  |  |
| --- | --- |
| Public 属性 | |
| [AK::AkMetering](struct_a_k_1_1_ak_metering.html) \* | [pMainMixMetering](struct_ak_output_device_metering_callback_info_a79e1d6c919ce4e3c701de2a95fe4a9bb.html#a79e1d6c919ce4e3c701de2a95fe4a9bb) |
|  | Metering information for the main mix [更多...](struct_ak_output_device_metering_callback_info_a79e1d6c919ce4e3c701de2a95fe4a9bb.html#a79e1d6c919ce4e3c701de2a95fe4a9bb) |
|  | |
| [AkChannelConfig](struct_ak_channel_config.html) | [mainMixConfig](struct_ak_output_device_metering_callback_info_a9507231a02d78903136eb9858d77db8b.html#a9507231a02d78903136eb9858d77db8b) |
|  | Channel configuration of the main mix [更多...](struct_ak_output_device_metering_callback_info_a9507231a02d78903136eb9858d77db8b.html#a9507231a02d78903136eb9858d77db8b) |
|  | |
| [AK::AkMetering](struct_a_k_1_1_ak_metering.html) \* | [pPassthroughMetering](struct_ak_output_device_metering_callback_info_a1414c43ff52a4a395117bb934b3bdedd.html#a1414c43ff52a4a395117bb934b3bdedd) |
|  | Metering information for the passthrough mix (if any; will be null otherwise) [更多...](struct_ak_output_device_metering_callback_info_a1414c43ff52a4a395117bb934b3bdedd.html#a1414c43ff52a4a395117bb934b3bdedd) |
|  | |
| [AkChannelConfig](struct_ak_channel_config.html) | [passthroughMixConfig](struct_ak_output_device_metering_callback_info_a975241174f1318dbc618a6c105165bf8.html#a975241174f1318dbc618a6c105165bf8) |
|  | Channel configuration of the passthrough mix (if any; will be invalid otherwise) [更多...](struct_ak_output_device_metering_callback_info_a975241174f1318dbc618a6c105165bf8.html#a975241174f1318dbc618a6c105165bf8) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumSystemAudioObjects](struct_ak_output_device_metering_callback_info_a6ca726eb16be70eee4ec6f67401a78dc.html#a6ca726eb16be70eee4ec6f67401a78dc) |
|  | Number of System Audio Objects going out of the output device [更多...](struct_ak_output_device_metering_callback_info_a6ca726eb16be70eee4ec6f67401a78dc.html#a6ca726eb16be70eee4ec6f67401a78dc) |
|  | |
| [AK::AkMetering](struct_a_k_1_1_ak_metering.html) \*\* | [ppSystemAudioObjectMetering](struct_ak_output_device_metering_callback_info_a14dd9e3a2e08aac435df8ff58bfcaa43.html#a14dd9e3a2e08aac435df8ff58bfcaa43) |
|  | Metering information for each System Audio Object (number of elements is equal to uNumSystemAudioObjects) [更多...](struct_ak_output_device_metering_callback_info_a14dd9e3a2e08aac435df8ff58bfcaa43.html#a14dd9e3a2e08aac435df8ff58bfcaa43) |
|  | |
| [AkMeteringFlags](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729) | [eMeteringFlags](struct_ak_output_device_metering_callback_info_ada78e00a75d607887dc98fba1319fd66.html#ada78e00a75d607887dc98fba1319fd66) |
|  | Metering flags that were asked for in [RegisterOutputDeviceMeteringCallback()](namespace_a_k_1_1_sound_engine_a1b27b0ecd5d9fd3ae78e38ea7d4230da.html#a1b27b0ecd5d9fd3ae78e38ea7d4230da). You may only access corresponding meter values from the metering objects. Others will fail. [更多...](struct_ak_output_device_metering_callback_info_ada78e00a75d607887dc98fba1319fd66.html#ada78e00a75d607887dc98fba1319fd66) |
|  | |
| - Public 属性 继承自 [AkCallbackInfo](struct_ak_callback_info.html) | |
| void \* | [pCookie](struct_ak_callback_info_a459248bd71e5a7fc85846d845c38dbe8.html#a459248bd71e5a7fc85846d845c38dbe8) |
|  | User data, passed to [PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) [更多...](struct_ak_callback_info_a459248bd71e5a7fc85846d845c38dbe8.html#a459248bd71e5a7fc85846d845c38dbe8) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjID](struct_ak_callback_info_a035c8b8516ffcb2975a5df8fec1dcc39.html#a035c8b8516ffcb2975a5df8fec1dcc39) |
|  | Game object ID [更多...](struct_ak_callback_info_a035c8b8516ffcb2975a5df8fec1dcc39.html#a035c8b8516ffcb2975a5df8fec1dcc39) |
|  | |

## 详细描述

Callback information structure allowing to query signal metering on output devices, at each frame. Register the callback using [AK::SoundEngine::RegisterOutputDeviceMeteringCallback](namespace_a_k_1_1_sound_engine_a1b27b0ecd5d9fd3ae78e38ea7d4230da.html#a1b27b0ecd5d9fd3ae78e38ea7d4230da).

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [289](_ak_callback_types_8h_source.html#l00289) 行定义.