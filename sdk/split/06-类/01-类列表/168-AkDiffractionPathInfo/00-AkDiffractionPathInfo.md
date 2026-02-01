# AkDiffractionPathInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_diffraction_path_info-members.html) |
[Public 属性](#pub-attribs) |
[静态 Public 属性](#pub-static-attribs)

AkDiffractionPathInfo结构体 参考

`#include <AkSpatialAudioTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkVector64](struct_ak_vector64.html) | [nodes](struct_ak_diffraction_path_info_aded09ae34899c9e734293882a4e1cd20.html#aded09ae34899c9e734293882a4e1cd20) [[AK\_MAX\_SOUND\_PROPAGATION\_DEPTH](_ak_spatial_audio_types_8h_aa3e56c32283503b4050c2a4c1383042c.html#aa3e56c32283503b4050c2a4c1383042c)] |
|  | |
| struct [AkVector64](struct_ak_vector64.html) | [emitterPos](struct_ak_diffraction_path_info_a8b927c112802aaffc68635694edd792d.html#a8b927c112802aaffc68635694edd792d) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [angles](struct_ak_diffraction_path_info_a7e27c9d0ff04171e8fbaa513b59eb64e.html#a7e27c9d0ff04171e8fbaa513b59eb64e) [[AK\_MAX\_SOUND\_PROPAGATION\_DEPTH](_ak_spatial_audio_types_8h_aa3e56c32283503b4050c2a4c1383042c.html#aa3e56c32283503b4050c2a4c1383042c)] |
|  | Raw diffraction angles at each point, in radians. [更多...](struct_ak_diffraction_path_info_a7e27c9d0ff04171e8fbaa513b59eb64e.html#a7e27c9d0ff04171e8fbaa513b59eb64e) |
|  | |
| [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992) | [portals](struct_ak_diffraction_path_info_a6b55a85eb292da656509d67439d6d337.html#a6b55a85eb292da656509d67439d6d337) [[AK\_MAX\_SOUND\_PROPAGATION\_DEPTH](_ak_spatial_audio_types_8h_aa3e56c32283503b4050c2a4c1383042c.html#aa3e56c32283503b4050c2a4c1383042c)] |
|  | |
| [AkRoomID](struct_ak_room_i_d.html) | [rooms](struct_ak_diffraction_path_info_a698710a9d2dfff1584547632f38fcd9d.html#a698710a9d2dfff1584547632f38fcd9d) [[AK\_MAX\_SOUND\_PROPAGATION\_DEPTH](_ak_spatial_audio_types_8h_aa3e56c32283503b4050c2a4c1383042c.html#aa3e56c32283503b4050c2a4c1383042c)+1] |
|  | |
| struct [AkWorldTransform](struct_ak_world_transform.html) | [virtualPos](struct_ak_diffraction_path_info_aba439db3bc3a38aa5e7aacb3d24247f8.html#aba439db3bc3a38aa5e7aacb3d24247f8) |
|  | Virtual emitter position. This is the position that is passed to the sound engine to render the audio using multi-positioning, for this particular path. [更多...](struct_ak_diffraction_path_info_aba439db3bc3a38aa5e7aacb3d24247f8.html#aba439db3bc3a38aa5e7aacb3d24247f8) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [nodeCount](struct_ak_diffraction_path_info_a0d7742d43279e77ec1c3c501f9a499b8.html#a0d7742d43279e77ec1c3c501f9a499b8) |
|  | Total number of nodes in the path. Defines the number of valid entries in the `nodes`, `angles`, and `portals` arrays. The `rooms` array has one extra slot to fit the emitter's room. [更多...](struct_ak_diffraction_path_info_a0d7742d43279e77ec1c3c501f9a499b8.html#a0d7742d43279e77ec1c3c501f9a499b8) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [diffraction](struct_ak_diffraction_path_info_a5616655d22e545447b998912cce8c58a.html#a5616655d22e545447b998912cce8c58a) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [transmissionLoss](struct_ak_diffraction_path_info_aafac0b86268acbb13e49e983b7d40f11.html#aafac0b86268acbb13e49e983b7d40f11) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [totLength](struct_ak_diffraction_path_info_aad06df6d9d7f93f18ba4a17a8cd59789.html#aad06df6d9d7f93f18ba4a17a8cd59789) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [obstructionValue](struct_ak_diffraction_path_info_a35b825b912e5a77e0a8425e90f31a5ce.html#a35b825b912e5a77e0a8425e90f31a5ce) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [occlusionValue](struct_ak_diffraction_path_info_a5304266b6af3bc9ba50d2cdcab5db1f7.html#a5304266b6af3bc9ba50d2cdcab5db1f7) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [gain](struct_ak_diffraction_path_info_a412f233dc98097d2a2c55711ce61374e.html#a412f233dc98097d2a2c55711ce61374e) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [kMaxNodes](struct_ak_diffraction_path_info_af174638221e87cd01711c0a26a61ff08.html#af174638221e87cd01711c0a26a61ff08) = [AK\_MAX\_SOUND\_PROPAGATION\_DEPTH](_ak_spatial_audio_types_8h_aa3e56c32283503b4050c2a4c1383042c.html#aa3e56c32283503b4050c2a4c1383042c) |
|  | Defines the maximum number of nodes that a user can retrieve information about. Longer paths will be truncated. [更多...](struct_ak_diffraction_path_info_af174638221e87cd01711c0a26a61ff08.html#af174638221e87cd01711c0a26a61ff08) |
|  | |

## 详细描述

Structure for retrieving information about paths for a given emitter. The diffraction paths represent indirect sound paths from the emitter to the listener, whether they go through portals (via the rooms and portals API) or are diffracted around edges (via the geometric diffraction API). The direct path is included here and can be identified by checking `nodeCount` == 0. The direct path may have a non-zero transmission loss if it passes through geometry or between rooms.

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [524](_ak_spatial_audio_types_8h_source.html#l00524) 行定义.