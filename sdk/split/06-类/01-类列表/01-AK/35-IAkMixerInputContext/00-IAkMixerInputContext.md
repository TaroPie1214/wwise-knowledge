# IAkMixerInputContext

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkMixerInputContext](class_a_k_1_1_i_ak_mixer_input_context.html)

[所有成员列表](class_a_k_1_1_i_ak_mixer_input_context-members.html) |
[Public 成员函数](#pub-methods)

AK::IAkMixerInputContext类 参考abstract

Interface to retrieve information about an input of a mix connection (for processing during the SpeakerVolumeMatrix Callback)
[更多...](class_a_k_1_1_i_ak_mixer_input_context.html#details)

`#include <IAkPlugin.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [IAkVoicePluginInfo](class_a_k_1_1_i_ak_voice_plugin_info.html) \* | [GetVoiceInfo](class_a_k_1_1_i_ak_mixer_input_context_afff91983cd78acdd305fd224b26501ee.html#afff91983cd78acdd305fd224b26501ee) ()=0 |
|  | |
| virtual [IAkGameObjectPluginInfo](class_a_k_1_1_i_ak_game_object_plugin_info.html) \* | [GetGameObjectInfo](class_a_k_1_1_i_ak_mixer_input_context_afdd2330826354684d6c3171ce9d60d36.html#afdd2330826354684d6c3171ce9d60d36) ()=0 |
|  | |
| virtual [AkConnectionType](_ak_enums_8h_a6f995e33d25d16eac499fb607bde0e4b.html#a6f995e33d25d16eac499fb607bde0e4b) | [GetConnectionType](class_a_k_1_1_i_ak_mixer_input_context_af565668adf1cb18d980c9430f8eb4671.html#af565668adf1cb18d980c9430f8eb4671) ()=0 |
|  | |
| virtual void \* | [GetUserData](class_a_k_1_1_i_ak_mixer_input_context_a014cbc876733b397572b95beac98745b.html#a014cbc876733b397572b95beac98745b) ()=0 |
|  | |
| virtual void | [SetUserData](class_a_k_1_1_i_ak_mixer_input_context_a6c723d5c887bf02536e3a31214c8a3c5.html#a6c723d5c887bf02536e3a31214c8a3c5) (void \*in\_pUserData)=0 |
|  | |
| virtual [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetCenterPerc](class_a_k_1_1_i_ak_mixer_input_context_ad4e9e9d4667099f24dcc8820dbc62e05.html#ad4e9e9d4667099f24dcc8820dbc62e05) ()=0 |
|  | |
| virtual [AkSpeakerPanningType](_ak_enums_8h_a229e1503503cb92fbca8a437196b283f.html#a229e1503503cb92fbca8a437196b283f) | [GetSpeakerPanningType](class_a_k_1_1_i_ak_mixer_input_context_aadf276dcd214deea9a4c121ba14eb85a.html#aadf276dcd214deea9a4c121ba14eb85a) ()=0 |
|  | |
| virtual void | [GetPannerPosition](class_a_k_1_1_i_ak_mixer_input_context_aed9c1760acbb5a0858003aa3266660d5.html#aed9c1760acbb5a0858003aa3266660d5) ([AkVector](struct_ak_vector.html) &out\_position)=0 |
|  | |
| virtual bool | [HasListenerRelativeRouting](class_a_k_1_1_i_ak_mixer_input_context_ae097823ba7acd8dd7c23af084164a6f3.html#ae097823ba7acd8dd7c23af084164a6f3) ()=0 |
|  | |
| virtual [Ak3DPositionType](_ak_enums_8h_a8a19085bec27023e23cca57f634f5ba7.html#a8a19085bec27023e23cca57f634f5ba7) | [Get3DPositionType](class_a_k_1_1_i_ak_mixer_input_context_a8c2c6370b8cbacd582d1f68de3e396ab.html#a8c2c6370b8cbacd582d1f68de3e396ab) ()=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetNum3DPositions](class_a_k_1_1_i_ak_mixer_input_context_a8d99842f211d766d9d7fc6479902facf.html#a8d99842f211d766d9d7fc6479902facf) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Get3DPosition](class_a_k_1_1_i_ak_mixer_input_context_a2e9f1dcc64cabb23a43b2f07b16d05df.html#a2e9f1dcc64cabb23a43b2f07b16d05df) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uIndex, [AkEmitterListenerPair](class_ak_emitter_listener_pair.html) &out\_soundPosition)=0 |
|  | |
| virtual [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetSpread](class_a_k_1_1_i_ak_mixer_input_context_a4c1d6a4163b0a1d64ee70486d0c81be5.html#a4c1d6a4163b0a1d64ee70486d0c81be5) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uIndex)=0 |
|  | |
| virtual [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetFocus](class_a_k_1_1_i_ak_mixer_input_context_ad32391f2f5dba6d7eb2f34dd9d604a31.html#ad32391f2f5dba6d7eb2f34dd9d604a31) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uIndex)=0 |
|  | |
| virtual bool | [GetMaxAttenuationDistance](class_a_k_1_1_i_ak_mixer_input_context_a3b977330da3255127d196a70ff01b3d0.html#a3b977330da3255127d196a70ff01b3d0) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_fMaxAttenuationDistance)=0 |
|  | |
| virtual [Ak3DSpatializationMode](_ak_enums_8h_a2091df555ad6110b01ce6905325a3a14.html#a2091df555ad6110b01ce6905325a3a14) | [Get3DSpatializationMode](class_a_k_1_1_i_ak_mixer_input_context_a2b46119de056293abcbedbb3fbbaf45e.html#a2b46119de056293abcbedbb3fbbaf45e) ()=0 |
|  | |

## 详细描述

Interface to retrieve information about an input of a mix connection (for processing during the SpeakerVolumeMatrix Callback)

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1002](_i_ak_plugin_8h_source.html#l01002) 行定义.