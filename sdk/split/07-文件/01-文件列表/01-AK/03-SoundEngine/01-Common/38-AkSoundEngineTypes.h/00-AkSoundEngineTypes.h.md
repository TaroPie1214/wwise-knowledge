# AkSoundEngineTypes.h

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
[函数](#func-members)

AkSoundEngineTypes.h 文件参考

`#include <AK/AkPlatforms.h>`  
`#include <AK/SoundEngine/Common/AkSoundEngineExport.h>`  
`#include <AK/SoundEngine/Common/AkNumeralTypes.h>`  
`#include <AK/SoundEngine/Common/AkTypedefs.h>`  
`#include <AK/SoundEngine/Common/AkEnums.h>`  
`#include <AK/SoundEngine/Common/AkSpeakerConfig.h>`

[浏览源代码.](_ak_sound_engine_types_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkAudioSettings](struct_ak_audio_settings.html) |
|  | Configured audio settings [更多...](struct_ak_audio_settings.html#details) |
|  | |
| struct | [AkDeviceDescription](struct_ak_device_description.html) |
|  | |
| struct | [AkMotionDeviceData](struct_ak_motion_device_data.html) |
|  | |
| struct | [Ak3DAudioSinkCapabilities](struct_ak3_d_audio_sink_capabilities.html) |
|  | |
| struct | [AkOutputDeviceInfo](struct_ak_output_device_info.html) |
|  | |
| struct | [AkObstructionOcclusionValues](struct_ak_obstruction_occlusion_values.html) |
|  | Obstruction/occlusion pair for a position [更多...](struct_ak_obstruction_occlusion_values.html#details) |
|  | |
| struct | [AkAuxSendValue](struct_ak_aux_send_value.html) |
|  | Auxiliary bus sends information per game object per given auxiliary bus. [更多...](struct_ak_aux_send_value.html#details) |
|  | |
| struct | [AkExternalSourceInfo](struct_ak_external_source_info.html) |
|  | |
| struct | [AkRamp](struct_ak_ramp.html) |
|  | Volume ramp specified by end points "previous" and "next". [更多...](struct_ak_ramp.html#details) |
|  | |
| struct | [AkOutputSettings](struct_ak_output_settings.html) |
|  | Platform-independent initialization settings of output devices. [更多...](struct_ak_output_settings.html#details) |
|  | |
| struct | [AkCodecDescriptor](struct_ak_codec_descriptor.html) |
|  | |
| struct | [WwiseObjectIDext](struct_wwise_object_i_dext.html) |
|  | |
| struct | [WwiseObjectID](struct_wwise_object_i_d.html) |
|  | |
| struct | [AkGraphPointBase< VALUE\_TYPE >](struct_ak_graph_point_base.html) |
|  | Type for a point in an RTPC or Attenuation curve. [更多...](struct_ak_graph_point_base.html#details) |
|  | |
| struct | [AkFileParser::EnvelopePoint](struct_ak_file_parser_1_1_envelope_point.html) |
|  | Analyzed envelope point. [更多...](struct_ak_file_parser_1_1_envelope_point.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
|  | [AkFileParser](namespace_ak_file_parser.html) |
|  | Public data structures for converted file format. |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WPTR](_ak_sound_engine_types_8h_afaf424df6a9c6a1a8c2c502aacbef817.html#afaf424df6a9c6a1a8c2c502aacbef817)(\_\_t\_\_, \_\_n\_\_) |
|  | |
| #define | [AkMax](_ak_sound_engine_types_8h_ac5bad2f7506f5090e3dcad675d808d9e.html#ac5bad2f7506f5090e3dcad675d808d9e)(x1, x2)   (((x1) > (x2))? (x1): (x2)) |
|  | |
| #define | [AkMin](_ak_sound_engine_types_8h_a4f1b4847274355e539e2d88757914605.html#a4f1b4847274355e539e2d88757914605)(x1, x2)   (((x1) < (x2))? (x1): (x2)) |
|  | |
| #define | [AkClamp](_ak_sound_engine_types_8h_ab502dbfef7a86a87ce28f6a08c53b3b7.html#ab502dbfef7a86a87ce28f6a08c53b3b7)(x, min, max)   ((x) < (min)) ? (min) : (((x) > (max) ? (max) : (x))) |
|  | |
| #define | [AK\_ASYNC\_OPEN\_DEFAULT](_ak_sound_engine_types_8h_aba586a9275a726a08f0fd8ac9f91417b.html#aba586a9275a726a08f0fd8ac9f91417b)   (false) |
|  | Refers to asynchronous file opening in default low-level IO. [更多...](_ak_sound_engine_types_8h_aba586a9275a726a08f0fd8ac9f91417b.html#aba586a9275a726a08f0fd8ac9f91417b) |
|  | |
| #define | [AK\_COMM\_DEFAULT\_DISCOVERY\_PORT](_ak_sound_engine_types_8h_a88dea84766161d404b8d5fbb6f1a636e.html#a88dea84766161d404b8d5fbb6f1a636e)   24024 |
|  | Default discovery port for most platforms using IP sockets for communication. [更多...](_ak_sound_engine_types_8h_a88dea84766161d404b8d5fbb6f1a636e.html#a88dea84766161d404b8d5fbb6f1a636e) |
|  | |
| #define | [AkRegister](_ak_sound_engine_types_8h_afffcbfc01fe6cf4d7c65a766905e1749.html#afffcbfc01fe6cf4d7c65a766905e1749) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef IAkSoftwareCodec \*(\* | [AkCreateFileSourceCallback](_ak_sound_engine_types_8h_ab1af7c591ff110a96afe92f34cc4e839.html#ab1af7c591ff110a96afe92f34cc4e839)) (void \*in\_pCtx) |
|  | Registered file source creation function prototype. [更多...](_ak_sound_engine_types_8h_ab1af7c591ff110a96afe92f34cc4e839.html#ab1af7c591ff110a96afe92f34cc4e839) |
|  | |
| typedef IAkSoftwareCodec \*(\* | [AkCreateBankSourceCallback](_ak_sound_engine_types_8h_ae33290ab81b22a844df5c2ab3bf675c2.html#ae33290ab81b22a844df5c2ab3bf675c2)) (void \*in\_pCtx) |
|  | Registered bank source node creation function prototype. [更多...](_ak_sound_engine_types_8h_ae33290ab81b22a844df5c2ab3bf675c2.html#ae33290ab81b22a844df5c2ab3bf675c2) |
|  | |
| typedef IAkFileCodec \*(\* | [AkCreateFileCodecCallback](_ak_sound_engine_types_8h_af6c3442917e9143cc36c9f2a3e055a16.html#af6c3442917e9143cc36c9f2a3e055a16)) () |
|  | Registered FileCodec creation function prototype. [更多...](_ak_sound_engine_types_8h_af6c3442917e9143cc36c9f2a3e055a16.html#af6c3442917e9143cc36c9f2a3e055a16) |
|  | |
| typedef IAkGrainCodec \*(\* | [AkCreateGrainCodecCallback](_ak_sound_engine_types_8h_a466d6280e1ea7ce066aa88c31dae0b1a.html#a466d6280e1ea7ce066aa88c31dae0b1a)) () |
|  | Registered IAkGrainCodec creation function prototype. [更多...](_ak_sound_engine_types_8h_a466d6280e1ea7ce066aa88c31dae0b1a.html#a466d6280e1ea7ce066aa88c31dae0b1a) |
|  | |
| typedef [AkGraphPointBase](struct_ak_graph_point_base.html)< [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) > | [AkRTPCGraphPoint](_ak_sound_engine_types_8h_aa706b42f8491bd4cd738427a53f04519.html#aa706b42f8491bd4cd738427a53f04519) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkRamp](struct_ak_ramp.html) | [operator\*](_ak_sound_engine_types_8h_a65d49abf75b195e8d8b3f7f99bc8cff6.html#a65d49abf75b195e8d8b3f7f99bc8cff6) (const [AkRamp](struct_ak_ramp.html) &in\_rLhs, const [AkRamp](struct_ak_ramp.html) &in\_rRhs) |
|  | |