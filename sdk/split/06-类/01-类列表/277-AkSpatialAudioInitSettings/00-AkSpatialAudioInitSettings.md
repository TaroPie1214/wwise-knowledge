# AkSpatialAudioInitSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_spatial_audio_init_settings-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkSpatialAudioInitSettings结构体 参考

Initialization settings of the spatial audio module.
[更多...](struct_ak_spatial_audio_init_settings.html#details)

`#include <AkSpatialAudioTypes.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkSpatialAudioInitSettings](struct_ak_spatial_audio_init_settings_aa814b8c60f74c0a812ef1cf3210a55df.html#aa814b8c60f74c0a812ef1cf3210a55df) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxSoundPropagationDepth](struct_ak_spatial_audio_init_settings_a4d07df03b41fed0b33c61b84c692c22e.html#a4d07df03b41fed0b33c61b84c692c22e) |
|  | Maximum number of rooms that sound can propagate through; must be less than or equal to AK\_MAX\_SOUND\_PROPAGATION\_DEPTH. Values below 2 will not propagate sound past the listener's own room. [更多...](struct_ak_spatial_audio_init_settings_a4d07df03b41fed0b33c61b84c692c22e.html#a4d07df03b41fed0b33c61b84c692c22e) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fMovementThreshold](struct_ak_spatial_audio_init_settings_a15f96c2d6a69f821c8ae6d677e6d29f4.html#a15f96c2d6a69f821c8ae6d677e6d29f4) |
|  | Amount that an emitter or listener has to move to trigger a validation of reflections/diffraction. Larger values can reduce the CPU load at the cost of reduced accuracy. Note that the ray tracing itself is not affected by this value. Rays are cast each time a Spatial Audio update is executed. [更多...](struct_ak_spatial_audio_init_settings_a15f96c2d6a69f821c8ae6d677e6d29f4.html#a15f96c2d6a69f821c8ae6d677e6d29f4) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumberOfPrimaryRays](struct_ak_spatial_audio_init_settings_ae11fb70d949998617a050b5b312ed767.html#ae11fb70d949998617a050b5b312ed767) |
|  | The number of primary rays used in the ray tracing engine. A larger number of rays will increase the chances of finding reflection and diffraction paths, but will result in higher CPU usage. [更多...](struct_ak_spatial_audio_init_settings_ae11fb70d949998617a050b5b312ed767.html#ae11fb70d949998617a050b5b312ed767) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxReflectionOrder](struct_ak_spatial_audio_init_settings_a346377be1b9f6905fb2d8d3e1540eb39.html#a346377be1b9f6905fb2d8d3e1540eb39) |
|  | Maximum reflection order [1, 4] - the number of 'bounces' in a reflection path. A high reflection order renders more details at the expense of higher CPU usage. [更多...](struct_ak_spatial_audio_init_settings_a346377be1b9f6905fb2d8d3e1540eb39.html#a346377be1b9f6905fb2d8d3e1540eb39) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxDiffractionOrder](struct_ak_spatial_audio_init_settings_a0e01d0d34659de40a8d84d93e05dfeab.html#a0e01d0d34659de40a8d84d93e05dfeab) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxDiffractionPaths](struct_ak_spatial_audio_init_settings_a94f819cee9905b9745f9d628aedf7cf2.html#a94f819cee9905b9745f9d628aedf7cf2) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxGlobalReflectionPaths](struct_ak_spatial_audio_init_settings_a79d0a9ef505102dd2960e339e526f6b8.html#a79d0a9ef505102dd2960e339e526f6b8) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxEmitterRoomAuxSends](struct_ak_spatial_audio_init_settings_a733e7d1ef6c4bf44af5bd55369ab4a3f.html#a733e7d1ef6c4bf44af5bd55369ab4a3f) |
|  | Set to 1 to only allow emitters to send directly to their current room, and to the room a listener is transitioning to if inside a portal. Set to 0 to disable the limit. [更多...](struct_ak_spatial_audio_init_settings_a733e7d1ef6c4bf44af5bd55369ab4a3f.html#a733e7d1ef6c4bf44af5bd55369ab4a3f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uDiffractionOnReflectionsOrder](struct_ak_spatial_audio_init_settings_a245b315e0cca157bdbef7cde581e8561.html#a245b315e0cca157bdbef7cde581e8561) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fMaxDiffractionAngleDegrees](struct_ak_spatial_audio_init_settings_aa22a7e11434285a698fe938d477e8279.html#aa22a7e11434285a698fe938d477e8279) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fMaxPathLength](struct_ak_spatial_audio_init_settings_a9a624f3d1ef7b4eba57930634b4c3c0c.html#a9a624f3d1ef7b4eba57930634b4c3c0c) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fCPULimitPercentage](struct_ak_spatial_audio_init_settings_add22106d4e299a6697a4c8c0728dc9a9.html#add22106d4e299a6697a4c8c0728dc9a9) |
|  | Defines the targeted max computation time allocated for spatial audio. Defined as a percentage [0, 100] of the current audio frame. When the value is different from 0, Spatial Audio adapts dynamically the load balancing spread value between 1 and the specified [AkSpatialAudioInitSettings::uLoadBalancingSpread](struct_ak_spatial_audio_init_settings_adb7560b0a616975d9f95fb932380002e.html#adb7560b0a616975d9f95fb932380002e "Spread the computation of paths on uLoadBalancingSpread frames [1..[. When uLoadBalancingSpread is se...") according to current CPU usage and the specified CPU limit. Set to 0 to disable the dynamic load balancing spread computation. [更多...](struct_ak_spatial_audio_init_settings_add22106d4e299a6697a4c8c0728dc9a9.html#add22106d4e299a6697a4c8c0728dc9a9) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uLoadBalancingSpread](struct_ak_spatial_audio_init_settings_adb7560b0a616975d9f95fb932380002e.html#adb7560b0a616975d9f95fb932380002e) |
|  | Spread the computation of paths on uLoadBalancingSpread frames [1..[. When uLoadBalancingSpread is set to 1, no load balancing is done. Values greater than 1 indicate the computation of paths will be spread on this number of frames. When CPU limit is active (see [AkSpatialAudioInitSettings::fCPULimitPercentage](struct_ak_spatial_audio_init_settings_add22106d4e299a6697a4c8c0728dc9a9.html#add22106d4e299a6697a4c8c0728dc9a9 "Defines the targeted max computation time allocated for spatial audio. Defined as a percentage [0,...")), this setting represents the upper bound spread used by the dynamic load balancing instead of a fixed value. [更多...](struct_ak_spatial_audio_init_settings_adb7560b0a616975d9f95fb932380002e.html#adb7560b0a616975d9f95fb932380002e) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fSmoothingConstantMs](struct_ak_spatial_audio_init_settings_a406bea3f65e5fef84954eb2603b8ecd0.html#a406bea3f65e5fef84954eb2603b8ecd0) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fAdjacentRoomBleed](struct_ak_spatial_audio_init_settings_ab75b8c41dbd117179bf344a469c7f5b1.html#ab75b8c41dbd117179bf344a469c7f5b1) |
|  | |
| bool | [bEnableGeometricDiffractionAndTransmission](struct_ak_spatial_audio_init_settings_ae7b27a1b56cb22eb2903de626f43f017.html#ae7b27a1b56cb22eb2903de626f43f017) |
|  | |
| bool | [bCalcEmitterVirtualPosition](struct_ak_spatial_audio_init_settings_a7b44a84de6c25d0abe4004c1c264aa13.html#a7b44a84de6c25d0abe4004c1c264aa13) |
|  | An emitter that is diffracted through a portal or around geometry will have its apparent or virtual position calculated by Wwise Spatial Audio and passed on to the sound engine. [更多...](struct_ak_spatial_audio_init_settings_a7b44a84de6c25d0abe4004c1c264aa13.html#a7b44a84de6c25d0abe4004c1c264aa13) |
|  | |
| enum [AkTransmissionOperation](_ak_spatial_audio_types_8h_aa15f2f697dced35d82fcc58bc437cfb8.html#aa15f2f697dced35d82fcc58bc437cfb8) | [eTransmissionOperation](struct_ak_spatial_audio_init_settings_a2580ab2686a91ec9e2f6038815ad6cec.html#a2580ab2686a91ec9e2f6038815ad6cec) |
|  | The operation used to determine transmission loss on direct paths. [更多...](struct_ak_spatial_audio_init_settings_a2580ab2686a91ec9e2f6038815ad6cec.html#a2580ab2686a91ec9e2f6038815ad6cec) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uClusteringMinPoints](struct_ak_spatial_audio_init_settings_a66dd539940098f9ed9bfd600262c1fa5.html#a66dd539940098f9ed9bfd600262c1fa5) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fClusteringMaxDistance](struct_ak_spatial_audio_init_settings_ac3eab08f2b45134b17d0a4d34f14a77d.html#ac3eab08f2b45134b17d0a4d34f14a77d) |
|  | Max distance between emitters to be considered as neighbors. This distance is specified for the reference distance defined by fClusteringDeadZoneDistance. Default value is 5.0. [更多...](struct_ak_spatial_audio_init_settings_ac3eab08f2b45134b17d0a4d34f14a77d.html#ac3eab08f2b45134b17d0a4d34f14a77d) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fClusteringDeadZoneDistance](struct_ak_spatial_audio_init_settings_ada511d087ecb7f920a1ff0f62460e8d7.html#ada511d087ecb7f920a1ff0f62460e8d7) |
|  | Defines a dead zone around the listener where no emitters are clusters. Default value is 10.0. [更多...](struct_ak_spatial_audio_init_settings_ada511d087ecb7f920a1ff0f62460e8d7.html#ada511d087ecb7f920a1ff0f62460e8d7) |
|  | |

## 详细描述

Initialization settings of the spatial audio module.

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [219](_ak_spatial_audio_types_8h_source.html#l00219) 行定义.