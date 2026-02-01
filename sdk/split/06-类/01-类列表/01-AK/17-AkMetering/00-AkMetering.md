# AkMetering

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [AkMetering](struct_a_k_1_1_ak_metering.html)

[所有成员列表](struct_a_k_1_1_ak_metering-members.html) |
[Public 属性](#pub-attribs)

AK::AkMetering结构体 参考

Struct containing metering information about a buffer. Depending on when this struct is generated, you may get metering data computed in the previous frame only.
[更多...](struct_a_k_1_1_ak_metering.html#details)

`#include <AkCommonDefs.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) | [peak](struct_a_k_1_1_ak_metering_a954f2565f746bb389d4e0a3ee6f42668.html#a954f2565f746bb389d4e0a3ee6f42668) |
|  | |
| [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) | [truePeak](struct_a_k_1_1_ak_metering_afb41ff18e6678d0c573b83e14d5ab61a.html#afb41ff18e6678d0c573b83e14d5ab61a) |
|  | |
| [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) | [rms](struct_a_k_1_1_ak_metering_ad074a15a5d85663056aec3bb87ada2b0.html#ad074a15a5d85663056aec3bb87ada2b0) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fMeanPowerK](struct_a_k_1_1_ak_metering_a4fbf7a87a580a2653bd90196c16f58c5.html#a4fbf7a87a580a2653bd90196c16f58c5) |
|  | |

## 详细描述

Struct containing metering information about a buffer. Depending on when this struct is generated, you may get metering data computed in the previous frame only.

在文件 [AkCommonDefs.h](_ak_common_defs_8h_source.html) 第 [192](_ak_common_defs_8h_source.html#l00192) 行定义.