# AkSpatialAudioTypes.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SpatialAudio](dir_e8de1cf052ef123fb045439c856e4598.html)
- [Common](dir_63e2f66e68c54d3307d872c42bbe429e.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[枚举](#enum-members) |
[变量](#var-members)

AkSpatialAudioTypes.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/Tools/Common/AkString.h>`

[浏览源代码.](_ak_spatial_audio_types_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) |
|  | Base type for ID's used by Wwise spatial audio.   [更多...](struct_ak_spatial_audio_i_d.html#details) |
|  | |
| struct | [AkRoomID](struct_ak_room_i_d.html) |
|  | |
| struct | [AkVertex](struct_ak_vertex.html) |
|  | |
| struct | [AkImageSourceName](struct_ak_image_source_name.html) |
|  | Data used to describe one image source in Reflect. [更多...](struct_ak_image_source_name.html#details) |
|  | |
| struct | [AkSpatialAudioInitSettings](struct_ak_spatial_audio_init_settings.html) |
|  | Initialization settings of the spatial audio module. [更多...](struct_ak_spatial_audio_init_settings.html#details) |
|  | |
| struct | [AkImageSourceParams](struct_ak_image_source_params.html) |
|  | |
| struct | [AkImageSourceTexture](struct_ak_image_source_texture.html) |
|  | |
| struct | [AkImageSourceSettings](struct_ak_image_source_settings.html) |
|  | Settings for individual image sources. [更多...](struct_ak_image_source_settings.html#details) |
|  | |
| struct | [AkExtent](struct_ak_extent.html) |
|  | |
| struct | [AkTriangle](struct_ak_triangle.html) |
|  | Triangle for a spatial audio mesh. [更多...](struct_ak_triangle.html#details) |
|  | |
| struct | [AkAcousticSurface](struct_ak_acoustic_surface.html) |
|  | |
| struct | [AkReflectionPathInfo](struct_ak_reflection_path_info.html) |
|  | Structure for retrieving information about the indirect paths of a sound that have been calculated via the geometric reflections API. Useful for debug draw applications. [更多...](struct_ak_reflection_path_info.html#details) |
|  | |
| struct | [AkDiffractionPathInfo](struct_ak_diffraction_path_info.html) |
|  | |
| struct | [AkPortalParams](struct_ak_portal_params.html) |
|  | Parameters passed to `SetPortal` [更多...](struct_ak_portal_params.html#details) |
|  | |
| struct | [AkRoomParams](struct_ak_room_params.html) |
|  | Parameters passed to `SetRoom` [更多...](struct_ak_room_params.html#details) |
|  | |
| struct | [AkGeometryParams](struct_ak_geometry_params.html) |
|  | Parameters passed to `SetGeometry` [更多...](struct_ak_geometry_params.html#details) |
|  | |
| struct | [AkGeometryInstanceParams](struct_ak_geometry_instance_params.html) |
|  | Parameters passed to `SetGeometryInstance` [更多...](struct_ak_geometry_instance_params.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::SpatialAudio](namespace_a_k_1_1_spatial_audio.html) |
|  | Audiokinetic spatial audio namespace |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_MAX\_NUM\_TEXTURE](_ak_spatial_audio_types_8h_a9c93fceeb1bf78b6b3df893cc7590fd3.html#a9c93fceeb1bf78b6b3df893cc7590fd3)   4 |
|  | |
| #define | [AK\_MAX\_REFLECT\_ORDER](_ak_spatial_audio_types_8h_a0f0ba7d6af53ea841932c7f2bb783611.html#a0f0ba7d6af53ea841932c7f2bb783611)   4 |
|  | |
| #define | [AK\_MAX\_REFLECTION\_PATH\_LENGTH](_ak_spatial_audio_types_8h_a6c8404a53ed551035147b6736cdcf2b2.html#a6c8404a53ed551035147b6736cdcf2b2)   ([AK\_MAX\_REFLECT\_ORDER](_ak_spatial_audio_types_8h_a0f0ba7d6af53ea841932c7f2bb783611.html#a0f0ba7d6af53ea841932c7f2bb783611) + 4) |
|  | |
| #define | [AK\_STOCHASTIC\_RESERVE\_LENGTH](_ak_spatial_audio_types_8h_a3d909f4d5ce1c90f398434c3a16a8799.html#a3d909f4d5ce1c90f398434c3a16a8799)   [AK\_MAX\_REFLECTION\_PATH\_LENGTH](_ak_spatial_audio_types_8h_a6c8404a53ed551035147b6736cdcf2b2.html#a6c8404a53ed551035147b6736cdcf2b2) |
|  | |
| #define | [AK\_MAX\_SOUND\_PROPAGATION\_DEPTH](_ak_spatial_audio_types_8h_aa3e56c32283503b4050c2a4c1383042c.html#aa3e56c32283503b4050c2a4c1383042c)   8 |
|  | |
| #define | [AK\_MAX\_SOUND\_PROPAGATION\_WIDTH](_ak_spatial_audio_types_8h_a1f076275d6659e087f28432337cfe6e1.html#a1f076275d6659e087f28432337cfe6e1)   32 |
|  | |
| #define | [AK\_SA\_EPSILON](_ak_spatial_audio_types_8h_a0bb59d647ba16302030f3806218fcf74.html#a0bb59d647ba16302030f3806218fcf74)   (0.001f) |
|  | |
| #define | [AK\_SA\_DIFFRACTION\_EPSILON](_ak_spatial_audio_types_8h_a22ee9365bc7373ecf5e45f2cd4983957.html#a22ee9365bc7373ecf5e45f2cd4983957)   (0.01f) |
|  | |
| #define | [AK\_SA\_DIFFRACTION\_DOT\_EPSILON](_ak_spatial_audio_types_8h_af79fe559f6cc6400c31de5326137f874.html#af79fe559f6cc6400c31de5326137f874)   (0.00005f) |
|  | |
| #define | [AK\_SA\_PLANE\_THICKNESS](_ak_spatial_audio_types_8h_a1485a3506a351079eda3a414f82ac41b.html#a1485a3506a351079eda3a414f82ac41b)   (0.01f) |
|  | |
| #define | [AK\_SA\_MIN\_ENVIRONMENT\_ABSORPTION](_ak_spatial_audio_types_8h_ac21e490fa62dcfd2962c221b80dd2588.html#ac21e490fa62dcfd2962c221b80dd2588)   (0.01f) |
|  | |
| #define | [AK\_SA\_MIN\_ENVIRONMENT\_SURFACE\_AREA](_ak_spatial_audio_types_8h_abfae7830a9584a9f1e8bc5d4165ff8f9.html#abfae7830a9584a9f1e8bc5d4165ff8f9)   (1.0f) |
|  | |
| #define | [AK\_INVALID\_VERTEX](_ak_spatial_audio_types_8h_a02b4b23024a4d24cf1efad4f4d2ef99d.html#a02b4b23024a4d24cf1efad4f4d2ef99d)   (([AkVertIdx](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6))(-1)) |
|  | |
| #define | [AK\_INVALID\_TRIANGLE](_ak_spatial_audio_types_8h_ad6a69efe841c178c75e6ee268e8d5a02.html#ad6a69efe841c178c75e6ee268e8d5a02)   (([AkTriIdx](_ak_typedefs_8h_ac81a13a3296704cf7a21c3d34241bf88.html#ac81a13a3296704cf7a21c3d34241bf88))(-1)) |
|  | |
| #define | [AK\_INVALID\_SURFACE](_ak_spatial_audio_types_8h_a7337568b9fbbebad8780fc98aeeb25e3.html#a7337568b9fbbebad8780fc98aeeb25e3)   (([AkSurfIdx](_ak_typedefs_8h_a1d462cf28f5a36878db54c59ab410fc0.html#a1d462cf28f5a36878db54c59ab410fc0))(-1)) |
|  | |
| #define | [AK\_INVALID\_SA\_ID](_ak_spatial_audio_types_8h_a7ffb9d0813fe1ebca593b4bc6593af63.html#a7ffb9d0813fe1ebca593b4bc6593af63)   (([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec))-1) |
|  | |
| #define | [AK\_OUTDOORS\_ROOM\_ID](_ak_spatial_audio_types_8h_a62ad8b5b6e2398f717a9c4a4beb8b144.html#a62ad8b5b6e2398f717a9c4a4beb8b144)   [AK\_INVALID\_SA\_ID](_ak_spatial_audio_types_8h_a7ffb9d0813fe1ebca593b4bc6593af63.html#a7ffb9d0813fe1ebca593b4bc6593af63) |
|  | |
| #define | [AK\_DEFAULT\_GEOMETRY\_POSITION\_X](_ak_spatial_audio_types_8h_a33825309f921df3192a1560d16ad5695.html#a33825309f921df3192a1560d16ad5695)   (0.0) |
|  | |
| #define | [AK\_DEFAULT\_GEOMETRY\_POSITION\_Y](_ak_spatial_audio_types_8h_ab20d2f0f1d63dfbaca452ae75a4a170b.html#ab20d2f0f1d63dfbaca452ae75a4a170b)   (0.0) |
|  | |
| #define | [AK\_DEFAULT\_GEOMETRY\_POSITION\_Z](_ak_spatial_audio_types_8h_a240bcfad8939f39f0f3426926dfdca62.html#a240bcfad8939f39f0f3426926dfdca62)   (0.0) |
|  | |
| #define | [AK\_DEFAULT\_GEOMETRY\_FRONT\_X](_ak_spatial_audio_types_8h_aec3c496cf42d28e0c3dc812170a92ae2.html#aec3c496cf42d28e0c3dc812170a92ae2)   (0.0) |
|  | |
| #define | [AK\_DEFAULT\_GEOMETRY\_FRONT\_Y](_ak_spatial_audio_types_8h_a2fe703776a7623610d008337d5a7a559.html#a2fe703776a7623610d008337d5a7a559)   (0.0) |
|  | |
| #define | [AK\_DEFAULT\_GEOMETRY\_FRONT\_Z](_ak_spatial_audio_types_8h_a784ff777e9257a3eab6997d9c25b1f97.html#a784ff777e9257a3eab6997d9c25b1f97)   (1.0) |
|  | |
| #define | [AK\_DEFAULT\_GEOMETRY\_TOP\_X](_ak_spatial_audio_types_8h_a236fd2446d523f48dd221a07a5218c4e.html#a236fd2446d523f48dd221a07a5218c4e)   (0.0) |
|  | |
| #define | [AK\_DEFAULT\_GEOMETRY\_TOP\_Y](_ak_spatial_audio_types_8h_a7b1d84ed0e0b8bd18ad364b5f4bbec32.html#a7b1d84ed0e0b8bd18ad364b5f4bbec32)   (1.0) |
|  | |
| #define | [AK\_DEFAULT\_GEOMETRY\_TOP\_Z](_ak_spatial_audio_types_8h_a5f49d4e4e3e71e8c22ab9bdca192b91c.html#a5f49d4e4e3e71e8c22ab9bdca192b91c)   (0.0) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [AkTransmissionOperation\_t](_ak_spatial_audio_types_8h_a903b9a9264616cccc1e1c4eaad8b24c5.html#a903b9a9264616cccc1e1c4eaad8b24c5) |
|  | |
| typedef [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [AkRoomDistanceBehavior\_t](_ak_spatial_audio_types_8h_af59c3d383610cd592084eabe1e488602.html#af59c3d383610cd592084eabe1e488602) |
|  | |
| typedef [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) | [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992) |
|  | |
| typedef [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) | [AkGeometrySetID](_ak_spatial_audio_types_8h_a4eccc0cc5fbd68160830c3201a8878a5.html#a4eccc0cc5fbd68160830c3201a8878a5) |
|  | |
| typedef [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) | [AkGeometryInstanceID](_ak_spatial_audio_types_8h_a825e3949bdcda8b78d677b95b60ca2f9.html#a825e3949bdcda8b78d677b95b60ca2f9) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AkTransmissionOperation](_ak_spatial_audio_types_8h_aa15f2f697dced35d82fcc58bc437cfb8.html#aa15f2f697dced35d82fcc58bc437cfb8) { [AkTransmissionOperation\_Add](_ak_spatial_audio_types_8h_aa15f2f697dced35d82fcc58bc437cfb8.html#aa15f2f697dced35d82fcc58bc437cfb8a7470a989ed27a4d675a30c93d38aa88f), [AkTransmissionOperation\_Multiply](_ak_spatial_audio_types_8h_aa15f2f697dced35d82fcc58bc437cfb8.html#aa15f2f697dced35d82fcc58bc437cfb8ac4e0ed23f7633390d14a0a931c309c4b), [AkTransmissionOperation\_Max](_ak_spatial_audio_types_8h_aa15f2f697dced35d82fcc58bc437cfb8.html#aa15f2f697dced35d82fcc58bc437cfb8a95879c785b57231bc052e5d7fb217097), [AkTransmissionOperation\_Default](_ak_spatial_audio_types_8h_aa15f2f697dced35d82fcc58bc437cfb8.html#aa15f2f697dced35d82fcc58bc437cfb8ab97cea07b902b95eafd844f796c6a16d) = AkTransmissionOperation\_Max } |
|  | |
| enum | [AkRoomDistanceBehavior](_ak_spatial_audio_types_8h_aafef0cf242d9f68863f696c3bbda2373.html#aafef0cf242d9f68863f696c3bbda2373) { [AkRoomDistanceBehavior\_Subtract](_ak_spatial_audio_types_8h_aafef0cf242d9f68863f696c3bbda2373.html#aafef0cf242d9f68863f696c3bbda2373a56a23434adfbf855362f146b25b32014), [AkRoomDistanceBehavior\_Exclude](_ak_spatial_audio_types_8h_aafef0cf242d9f68863f696c3bbda2373.html#aafef0cf242d9f68863f696c3bbda2373ace4322e671e29157bd0f7e1eb5805b70), [AkRoomDistanceBehavior\_Default](_ak_spatial_audio_types_8h_aafef0cf242d9f68863f696c3bbda2373.html#aafef0cf242d9f68863f696c3bbda2373a7620c226acc7d2f5d3b6f22eba876ee9) = AkRoomDistanceBehavior\_Subtract } |
|  | Determines how a room interacts with the distance calculation of other rooms that it overlaps or is nested within. [更多...](_ak_spatial_audio_types_8h_aafef0cf242d9f68863f696c3bbda2373.html#aafef0cf242d9f68863f696c3bbda2373) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| constexpr [AkRoomID](struct_ak_room_i_d.html) | [AK::SpatialAudio::kOutdoorRoomID](namespace_a_k_1_1_spatial_audio_a0b178cf8987e4fe5e2b33a6d51116a1c.html#a0b178cf8987e4fe5e2b33a6d51116a1c) |
|  | The outdoor room ID. This room is created automatically and is typically used for outdoors, i.e. when not in a room. [更多...](namespace_a_k_1_1_spatial_audio_a0b178cf8987e4fe5e2b33a6d51116a1c.html#a0b178cf8987e4fe5e2b33a6d51116a1c) |
|  | |

## 详细描述

Spatial audio data type definitions.

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 中定义.