# AkPositioningInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_positioning_info-members.html) |
[Public 属性](#pub-attribs)

AkPositioningInfo结构体 参考

Positioning information obtained from an object
[更多...](struct_ak_positioning_info.html#details)

`#include <AkQueryParameters.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fCenterPct](struct_ak_positioning_info_a87ed7f98906e771110b24a218b36304e.html#a87ed7f98906e771110b24a218b36304e) |
|  | Center % [0..1] [更多...](struct_ak_positioning_info_a87ed7f98906e771110b24a218b36304e.html#a87ed7f98906e771110b24a218b36304e) |
|  | |
| [AkSpeakerPanningType](_ak_enums_8h_a229e1503503cb92fbca8a437196b283f.html#a229e1503503cb92fbca8a437196b283f) | [pannerType](struct_ak_positioning_info_a3868dab6fd94eec42b029589ce6d22f9.html#a3868dab6fd94eec42b029589ce6d22f9) |
|  | Speaker panning type: type of panning logic when object is not 3D spatialized. [更多...](struct_ak_positioning_info_a3868dab6fd94eec42b029589ce6d22f9.html#a3868dab6fd94eec42b029589ce6d22f9) |
|  | |
| [Ak3DPositionType](_ak_enums_8h_a8a19085bec27023e23cca57f634f5ba7.html#a8a19085bec27023e23cca57f634f5ba7) | [e3dPositioningType](struct_ak_positioning_info_af3bdaa5bd3896db2ab0949af81e3bec6.html#af3bdaa5bd3896db2ab0949af81e3bec6) |
|  | 3D position type: defines what acts as the emitter position for computing spatialization against the listener. [更多...](struct_ak_positioning_info_af3bdaa5bd3896db2ab0949af81e3bec6.html#af3bdaa5bd3896db2ab0949af81e3bec6) |
|  | |
| bool | [bHoldEmitterPosAndOrient](struct_ak_positioning_info_aa704cd5060c986c0a1aae2b82bdbda61.html#aa704cd5060c986c0a1aae2b82bdbda61) |
|  | Hold emitter position and orientation values when starting playback. [更多...](struct_ak_positioning_info_aa704cd5060c986c0a1aae2b82bdbda61.html#aa704cd5060c986c0a1aae2b82bdbda61) |
|  | |
| [Ak3DSpatializationMode](_ak_enums_8h_a2091df555ad6110b01ce6905325a3a14.html#a2091df555ad6110b01ce6905325a3a14) | [e3DSpatializationMode](struct_ak_positioning_info_a2f742a4509b712687c9b10f9622aff0e.html#a2f742a4509b712687c9b10f9622aff0e) |
|  | Spatialization mode [更多...](struct_ak_positioning_info_a2f742a4509b712687c9b10f9622aff0e.html#a2f742a4509b712687c9b10f9622aff0e) |
|  | |
| bool | [bEnableAttenuation](struct_ak_positioning_info_a9e3206d530117089bde4a2e8661d3488.html#a9e3206d530117089bde4a2e8661d3488) |
|  | Attenuation parameter set is active. [更多...](struct_ak_positioning_info_a9e3206d530117089bde4a2e8661d3488.html#a9e3206d530117089bde4a2e8661d3488) |
|  | |
| bool | [bUseConeAttenuation](struct_ak_positioning_info_ab9a8ba37a22036307cd4edd1c30bc17e.html#ab9a8ba37a22036307cd4edd1c30bc17e) |
|  | Use the cone attenuation [更多...](struct_ak_positioning_info_ab9a8ba37a22036307cd4edd1c30bc17e.html#ab9a8ba37a22036307cd4edd1c30bc17e) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fInnerAngle](struct_ak_positioning_info_ac45dcd5c7b12394bb474ab78f6d38d2f.html#ac45dcd5c7b12394bb474ab78f6d38d2f) |
|  | Inner angle [更多...](struct_ak_positioning_info_ac45dcd5c7b12394bb474ab78f6d38d2f.html#ac45dcd5c7b12394bb474ab78f6d38d2f) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fOuterAngle](struct_ak_positioning_info_af66171fb2435dcbb051791ddf329e0b5.html#af66171fb2435dcbb051791ddf329e0b5) |
|  | Outer angle [更多...](struct_ak_positioning_info_af66171fb2435dcbb051791ddf329e0b5.html#af66171fb2435dcbb051791ddf329e0b5) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fConeMaxAttenuation](struct_ak_positioning_info_a20e5af3b156d4385a76f2e407a466b4d.html#a20e5af3b156d4385a76f2e407a466b4d) |
|  | Cone max attenuation [更多...](struct_ak_positioning_info_a20e5af3b156d4385a76f2e407a466b4d.html#a20e5af3b156d4385a76f2e407a466b4d) |
|  | |
| [AkLPFType](_ak_typedefs_8h_a2cc45412d6a5527f94c0f5a6da620c04.html#a2cc45412d6a5527f94c0f5a6da620c04) | [LPFCone](struct_ak_positioning_info_a4a46ef350f3de1c3b348cac59b5d9d2d.html#a4a46ef350f3de1c3b348cac59b5d9d2d) |
|  | Cone low pass filter value [更多...](struct_ak_positioning_info_a4a46ef350f3de1c3b348cac59b5d9d2d.html#a4a46ef350f3de1c3b348cac59b5d9d2d) |
|  | |
| [AkLPFType](_ak_typedefs_8h_a2cc45412d6a5527f94c0f5a6da620c04.html#a2cc45412d6a5527f94c0f5a6da620c04) | [HPFCone](struct_ak_positioning_info_ab6a44991819ca8bf185b210f33eef14d.html#ab6a44991819ca8bf185b210f33eef14d) |
|  | Cone low pass filter value [更多...](struct_ak_positioning_info_ab6a44991819ca8bf185b210f33eef14d.html#ab6a44991819ca8bf185b210f33eef14d) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fMaxDistance](struct_ak_positioning_info_a950111f22c76997108dccda15b7044b3.html#a950111f22c76997108dccda15b7044b3) |
|  | Maximum distance [更多...](struct_ak_positioning_info_a950111f22c76997108dccda15b7044b3.html#a950111f22c76997108dccda15b7044b3) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fVolDryAtMaxDist](struct_ak_positioning_info_a431e513849b703de33006f1d195f88ed.html#a431e513849b703de33006f1d195f88ed) |
|  | Volume dry at maximum distance [更多...](struct_ak_positioning_info_a431e513849b703de33006f1d195f88ed.html#a431e513849b703de33006f1d195f88ed) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fVolAuxGameDefAtMaxDist](struct_ak_positioning_info_a062c740cd6a52651fb398ad73e953e8f.html#a062c740cd6a52651fb398ad73e953e8f) |
|  | Volume wet at maximum distance (if any) (based on the Game defined distance attenuation) [更多...](struct_ak_positioning_info_a062c740cd6a52651fb398ad73e953e8f.html#a062c740cd6a52651fb398ad73e953e8f) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fVolAuxUserDefAtMaxDist](struct_ak_positioning_info_ad573c8000b8a6bcc4ba3bc5271727764.html#ad573c8000b8a6bcc4ba3bc5271727764) |
|  | Volume wet at maximum distance (if any) (based on the User defined distance attenuation) [更多...](struct_ak_positioning_info_ad573c8000b8a6bcc4ba3bc5271727764.html#ad573c8000b8a6bcc4ba3bc5271727764) |
|  | |
| [AkLPFType](_ak_typedefs_8h_a2cc45412d6a5527f94c0f5a6da620c04.html#a2cc45412d6a5527f94c0f5a6da620c04) | [LPFValueAtMaxDist](struct_ak_positioning_info_a0027b35dcd72f2886995d9986cf6949b.html#a0027b35dcd72f2886995d9986cf6949b) |
|  | Low pass filter value at max distance (if any) [更多...](struct_ak_positioning_info_a0027b35dcd72f2886995d9986cf6949b.html#a0027b35dcd72f2886995d9986cf6949b) |
|  | |
| [AkLPFType](_ak_typedefs_8h_a2cc45412d6a5527f94c0f5a6da620c04.html#a2cc45412d6a5527f94c0f5a6da620c04) | [HPFValueAtMaxDist](struct_ak_positioning_info_aec7f11677ff84ec6ad83dd2a63cdaf87.html#aec7f11677ff84ec6ad83dd2a63cdaf87) |
|  | High pass filter value at max distance (if any) [更多...](struct_ak_positioning_info_aec7f11677ff84ec6ad83dd2a63cdaf87.html#aec7f11677ff84ec6ad83dd2a63cdaf87) |
|  | |

## 详细描述

Positioning information obtained from an object

在文件 [AkQueryParameters.h](_ak_query_parameters_8h_source.html) 第 [42](_ak_query_parameters_8h_source.html#l00042) 行定义.