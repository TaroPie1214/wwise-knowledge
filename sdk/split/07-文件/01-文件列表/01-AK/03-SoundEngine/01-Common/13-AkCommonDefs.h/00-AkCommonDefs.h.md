# AkCommonDefs.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[枚举](#enum-members) |
[函数](#func-members) |
[变量](#var-members)

AkCommonDefs.h 文件参考

`#include <AK/SoundEngine/Common/AkSpeakerConfig.h>`  
`#include <AK/SoundEngine/Common/AkSpeakerVolumes.h>`  
`#include <AK/Tools/Common/AkBitFuncs.h>`  
`#include <AK/Tools/Common/AkAssert.h>`

[浏览源代码.](_ak_common_defs_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkAudioFormat](struct_ak_audio_format.html) |
|  | Defines the parameters of an audio buffer format. [更多...](struct_ak_audio_format.html#details) |
|  | |
| struct | [AK::AkMetering](struct_a_k_1_1_ak_metering.html) |
|  | Struct containing metering information about a buffer. Depending on when this struct is generated, you may get metering data computed in the previous frame only. [更多...](struct_a_k_1_1_ak_metering.html#details) |
|  | |
| struct | [Ak3dData](struct_ak3d_data.html) |
|  | |
| struct | [AkBehavioralPositioningData](struct_ak_behavioral_positioning_data.html) |
|  | Positioning data inherited from sound structures and mix busses. [更多...](struct_ak_behavioral_positioning_data.html#details) |
|  | |
| struct | [AkPositioningData](struct_ak_positioning_data.html) |
|  | Positioning data of 3D audio objects. [更多...](struct_ak_positioning_data.html#details) |
|  | |
| class | [AkAudioBuffer](class_ak_audio_buffer.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_MAKE\_CHANNELCONFIGOVERRIDE](_ak_common_defs_8h_a39573d41ef9e892731fdb7170d4cf99d.html#a39573d41ef9e892731fdb7170d4cf99d)(\_config, \_order)   (([AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c))\_config.Serialize()|(([AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c))\_order<<32)) |
|  | |
| #define | [AK\_GET\_CHANNELCONFIGOVERRIDE\_CONFIG](_ak_common_defs_8h_a5ddbea8323172fbc0bb2a3cce5055534.html#a5ddbea8323172fbc0bb2a3cce5055534)(\_over)   (\_over&UINT\_MAX) |
|  | |
| #define | [AK\_GET\_CHANNELCONFIGOVERRIDE\_ORDERING](_ak_common_defs_8h_a77f3fde6cc00e82d19c8c6734c4a12a5.html#a77f3fde6cc00e82d19c8c6734c4a12a5)(\_over)   (([AK::AkChannelOrdering](namespace_a_k_a96a4d4c0205f609855344ad8365d5e42.html#a96a4d4c0205f609855344ad8365d5e42))(\_over>>32)) |
|  | |
| #define | [AKMAKECLASSID](_ak_common_defs_8h_ac73a5e1e4a45a0aeea1b11b08ba93516.html#ac73a5e1e4a45a0aeea1b11b08ba93516)(in\_pluginType, in\_companyID, in\_pluginID)    ( (in\_pluginType) + ( (in\_companyID) << 4 ) + ( (in\_pluginID) << ( 4 + 12 ) ) ) |
|  | |
| #define | [AKGETPLUGINTYPEFROMCLASSID](_ak_common_defs_8h_acfee94d7aa1dbeb7a64b12c372830675.html#acfee94d7aa1dbeb7a64b12c372830675)(in\_classID)   ( (in\_classID) & [AkPluginTypeMask](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4a73e22b3cf4444ac59de4b0050d9b3dfc) ) |
|  | |
| #define | [AKGETCOMPANYIDFROMCLASSID](_ak_common_defs_8h_a6a6429f96744b8b86a66f428ffcbfaf0.html#a6a6429f96744b8b86a66f428ffcbfaf0)(in\_classID)   ( ( (in\_classID) & 0x0000FFF0 ) >> 4 ) |
|  | |
| #define | [AKGETPLUGINIDFROMCLASSID](_ak_common_defs_8h_a82ec8d8e285bca3dc0a2c4abafb3f383.html#a82ec8d8e285bca3dc0a2c4abafb3f383)(in\_classID)   ( ( (in\_classID) & 0xFFFF0000 ) >> ( 4 + 12 ) ) |
|  | |
| #define | [CODECID\_FROM\_PLUGINID](_ak_common_defs_8h_a19c1760dbbd0a14b62e3c72a14438240.html#a19c1760dbbd0a14b62e3c72a14438240)   [AKGETPLUGINIDFROMCLASSID](_ak_common_defs_8h_a82ec8d8e285bca3dc0a2c4abafb3f383.html#a82ec8d8e285bca3dc0a2c4abafb3f383) |
|  | |
| #define | [AK\_DEFAULT\_LISTENER\_POSITION\_X](_ak_common_defs_8h_aef5981f1d81ff278b35d975b43a46b0f.html#aef5981f1d81ff278b35d975b43a46b0f)   (0.0f) |
|  | Default listener transform. [更多...](_ak_common_defs_8h_aef5981f1d81ff278b35d975b43a46b0f.html#aef5981f1d81ff278b35d975b43a46b0f) |
|  | |
| #define | [AK\_DEFAULT\_LISTENER\_POSITION\_Y](_ak_common_defs_8h_a439d15227dcf1dec59d53a2c35777fef.html#a439d15227dcf1dec59d53a2c35777fef)   (0.0f) |
|  | |
| #define | [AK\_DEFAULT\_LISTENER\_POSITION\_Z](_ak_common_defs_8h_a22e1b9570d1faceb9bdbcaed521efde2.html#a22e1b9570d1faceb9bdbcaed521efde2)   (0.0f) |
|  | |
| #define | [AK\_DEFAULT\_LISTENER\_FRONT\_X](_ak_common_defs_8h_ad9b4be239cd9d879b27e9ccf4d7de003.html#ad9b4be239cd9d879b27e9ccf4d7de003)   (0.0f) |
|  | |
| #define | [AK\_DEFAULT\_LISTENER\_FRONT\_Y](_ak_common_defs_8h_a015a446332026a0170507dc732293670.html#a015a446332026a0170507dc732293670)   (0.0f) |
|  | |
| #define | [AK\_DEFAULT\_LISTENER\_FRONT\_Z](_ak_common_defs_8h_a535e85c1b0b5de024353791c31421c79.html#a535e85c1b0b5de024353791c31421c79)   (1.0f) |
|  | |
| #define | [AK\_DEFAULT\_TOP\_X](_ak_common_defs_8h_a13bf2ad3bc9a10d1548375f1f22f1e66.html#a13bf2ad3bc9a10d1548375f1f22f1e66)   (0.0f) |
|  | |
| #define | [AK\_DEFAULT\_TOP\_Y](_ak_common_defs_8h_ac357a05bdb676c223bcc03e04acc9171.html#ac357a05bdb676c223bcc03e04acc9171)   (1.0f) |
|  | |
| #define | [AK\_DEFAULT\_TOP\_Z](_ak_common_defs_8h_a085fcaff12b7c8df71b546c4d918b67f.html#a085fcaff12b7c8df71b546c4d918b67f)   (0.0f) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270)(\* | [AkChannelMappingFunc](_ak_common_defs_8h_a3e182f88e43c42509f2b168495a8aeaa.html#a3e182f88e43c42509f2b168495a8aeaa)) (const [AkChannelConfig](struct_ak_channel_config.html) &config, [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) idx) |
|  | |
| typedef [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AkSampleType](_ak_common_defs_8h_a58f11a728038d16fe4187612a7a842fb.html#a58f11a728038d16fe4187612a7a842fb) |
|  | Audio sample data type (32 bit floating point) [更多...](_ak_common_defs_8h_a58f11a728038d16fe4187612a7a842fb.html#a58f11a728038d16fe4187612a7a842fb) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AkAudioObjectDestination](_ak_common_defs_8h_ae853d151004b46a95472c3bd26f05733.html#ae853d151004b46a95472c3bd26f05733) { [AkAudioObjectDestination::eDefault](_ak_common_defs_8h_ae853d151004b46a95472c3bd26f05733.html#ae853d151004b46a95472c3bd26f05733aaf71f03861810014d736fcbae9d6050e) = 0, [AkAudioObjectDestination::eMainMix](_ak_common_defs_8h_ae853d151004b46a95472c3bd26f05733.html#ae853d151004b46a95472c3bd26f05733a9c28c25d9bc07c279cd0f077f96386fd) = 1, [AkAudioObjectDestination::ePassthrough](_ak_common_defs_8h_ae853d151004b46a95472c3bd26f05733.html#ae853d151004b46a95472c3bd26f05733a6da7709a332b445b91fb3c78a781082e) = 2, [AkAudioObjectDestination::eSystemAudioObject](_ak_common_defs_8h_ae853d151004b46a95472c3bd26f05733.html#ae853d151004b46a95472c3bd26f05733ae1dc3fd745dc677793da3398612c6e04) = 3 } |
|  | Enum of the possible object destinations when reaching a 3D audio-capable sink [更多...](_ak_common_defs_8h_ae853d151004b46a95472c3bd26f05733.html#ae853d151004b46a95472c3bd26f05733) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| static bool | [AK::IsBankCodecID](namespace_a_k_a2c33e14ea3a8cb877f43d74b612998d2.html#a2c33e14ea3a8cb877f43d74b612998d2) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_codecID) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| const [AkDataTypeID](_ak_typedefs_8h_a2c2492d7eac66159d80f80d69c8ccd64.html#a2c2492d7eac66159d80f80d69c8ccd64) | [AK\_INT](_ak_common_defs_8h_a27e63de612e818dbe8b87e583bc175e7.html#a27e63de612e818dbe8b87e583bc175e7) = 0 |
|  | Integer data type (uchar, short, and so on) [更多...](_ak_common_defs_8h_a27e63de612e818dbe8b87e583bc175e7.html#a27e63de612e818dbe8b87e583bc175e7) |
|  | |
| const [AkDataTypeID](_ak_typedefs_8h_a2c2492d7eac66159d80f80d69c8ccd64.html#a2c2492d7eac66159d80f80d69c8ccd64) | [AK\_FLOAT](_ak_common_defs_8h_ac2305ab9975d0dcb95000fed26f5d85f.html#ac2305ab9975d0dcb95000fed26f5d85f) = 1 |
|  | Float data type [更多...](_ak_common_defs_8h_ac2305ab9975d0dcb95000fed26f5d85f.html#ac2305ab9975d0dcb95000fed26f5d85f) |
|  | |
| const [AkDataInterleaveID](_ak_typedefs_8h_a25f0ba8543113ea7b34ce6cb143e14ee.html#a25f0ba8543113ea7b34ce6cb143e14ee) | [AK\_INTERLEAVED](_ak_common_defs_8h_a7fa3ccbf7577c429ea9612d9528350b8.html#a7fa3ccbf7577c429ea9612d9528350b8) = 0 |
|  | Interleaved data [更多...](_ak_common_defs_8h_a7fa3ccbf7577c429ea9612d9528350b8.html#a7fa3ccbf7577c429ea9612d9528350b8) |
|  | |
| const [AkDataInterleaveID](_ak_typedefs_8h_a25f0ba8543113ea7b34ce6cb143e14ee.html#a25f0ba8543113ea7b34ce6cb143e14ee) | [AK\_NONINTERLEAVED](_ak_common_defs_8h_af1105ef3c1bb2986161cbc4c1ef76cb6.html#af1105ef3c1bb2986161cbc4c1ef76cb6) = 1 |
|  | Non-interleaved data [更多...](_ak_common_defs_8h_af1105ef3c1bb2986161cbc4c1ef76cb6.html#af1105ef3c1bb2986161cbc4c1ef76cb6) |
|  | |
| const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK\_LE\_NATIVE\_BITSPERSAMPLE](_ak_common_defs_8h_ae18ecd01910d368ac2decf1d5aba056b.html#ae18ecd01910d368ac2decf1d5aba056b) = 32 |
|  | Native number of bits per sample. [更多...](_ak_common_defs_8h_ae18ecd01910d368ac2decf1d5aba056b.html#ae18ecd01910d368ac2decf1d5aba056b) |
|  | |
| const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK\_LE\_NATIVE\_SAMPLETYPE](_ak_common_defs_8h_ae70b5a0eea10630c01c64cbf163f496f.html#ae70b5a0eea10630c01c64cbf163f496f) = [AK\_FLOAT](_ak_common_defs_8h_ac2305ab9975d0dcb95000fed26f5d85f.html#ac2305ab9975d0dcb95000fed26f5d85f) |
|  | Native data type. [更多...](_ak_common_defs_8h_ae70b5a0eea10630c01c64cbf163f496f.html#ae70b5a0eea10630c01c64cbf163f496f) |
|  | |
| const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK\_LE\_NATIVE\_INTERLEAVE](_ak_common_defs_8h_a1c46b5d0572c57c834b59aac0cf4c25c.html#a1c46b5d0572c57c834b59aac0cf4c25c) = [AK\_NONINTERLEAVED](_ak_common_defs_8h_af1105ef3c1bb2986161cbc4c1ef76cb6.html#af1105ef3c1bb2986161cbc4c1ef76cb6) |
|  | Native interleaved setting. [更多...](_ak_common_defs_8h_a1c46b5d0572c57c834b59aac0cf4c25c.html#a1c46b5d0572c57c834b59aac0cf4c25c) |
|  | |

## 详细描述

AudioLib common defines, enums, and structs.

在文件 [AkCommonDefs.h](_ak_common_defs_8h_source.html) 中定义.