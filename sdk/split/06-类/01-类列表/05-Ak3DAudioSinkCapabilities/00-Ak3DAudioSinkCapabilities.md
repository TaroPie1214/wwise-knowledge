# Ak3DAudioSinkCapabilities

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak3_d_audio_sink_capabilities-members.html) |
[Public 属性](#pub-attribs)

Ak3DAudioSinkCapabilities结构体 参考

`#include <AkSoundEngineTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkChannelConfig](struct_ak_channel_config.html) | [channelConfig](struct_ak3_d_audio_sink_capabilities_a164aa26ac716a5d4d8373190bcd4f9ab.html#a164aa26ac716a5d4d8373190bcd4f9ab) |
|  | Channel configuration of the main mix. [更多...](struct_ak3_d_audio_sink_capabilities_a164aa26ac716a5d4d8373190bcd4f9ab.html#a164aa26ac716a5d4d8373190bcd4f9ab) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxSystemAudioObjects](struct_ak3_d_audio_sink_capabilities_ac09b0ffec60df2f305e3643ed1a77d45.html#ac09b0ffec60df2f305e3643ed1a77d45) |
|  | Maximum number of System Audio Objects that can be active concurrently. A value of zero indicates the system does not support this feature. [更多...](struct_ak3_d_audio_sink_capabilities_ac09b0ffec60df2f305e3643ed1a77d45.html#ac09b0ffec60df2f305e3643ed1a77d45) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uAvailableSystemAudioObjects](struct_ak3_d_audio_sink_capabilities_aa8763c43ed9f9ba791873472a3bad821.html#aa8763c43ed9f9ba791873472a3bad821) |
|  | How many System Audio Objects can currently be sent to the sink. This value can change at runtime depending on what is playing. Can never be higher than uMaxSystemAudioObjects. [更多...](struct_ak3_d_audio_sink_capabilities_aa8763c43ed9f9ba791873472a3bad821.html#aa8763c43ed9f9ba791873472a3bad821) |
|  | |
| bool | [bPassthrough](struct_ak3_d_audio_sink_capabilities_afe3158a19bf34e0e124b08ab4b0b94a1.html#afe3158a19bf34e0e124b08ab4b0b94a1) |
|  | Separate pass-through mix is supported. [更多...](struct_ak3_d_audio_sink_capabilities_afe3158a19bf34e0e124b08ab4b0b94a1.html#afe3158a19bf34e0e124b08ab4b0b94a1) |
|  | |
| bool | [bMultiChannelObjects](struct_ak3_d_audio_sink_capabilities_aac3c507bfe79952bae234720542cf525.html#aac3c507bfe79952bae234720542cf525) |
|  | Can handle multi-channel objects [更多...](struct_ak3_d_audio_sink_capabilities_aac3c507bfe79952bae234720542cf525.html#aac3c507bfe79952bae234720542cf525) |
|  | |

## 详细描述

Structure containing information about system-level support for 3D audio. "3D Audio" refers to a system's ability to position sound sources in a virtual 3D space, pan them accordingly on a range of physical speakers, and produce a binaural mix where appropriate. We prefer "3D Audio" to "Spatial" to avoid ambiguity with spatial audio, which typically involves sound propagation and environment effects.

在文件 [AkSoundEngineTypes.h](_ak_sound_engine_types_8h_source.html) 第 [76](_ak_sound_engine_types_8h_source.html#l00076) 行定义.