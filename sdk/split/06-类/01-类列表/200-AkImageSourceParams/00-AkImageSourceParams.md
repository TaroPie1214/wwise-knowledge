# AkImageSourceParams

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_image_source_params-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkImageSourceParams结构体 参考

`#include <AkSpatialAudioTypes.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkImageSourceParams](struct_ak_image_source_params_a3bcf0065106f2d758312daae17bdb707.html#a3bcf0065106f2d758312daae17bdb707) () |
|  | |
|  | [AkImageSourceParams](struct_ak_image_source_params_a272ce62ac7b58c4dcb7733adde134cda.html#a272ce62ac7b58c4dcb7733adde134cda) ([AkVector64](struct_ak_vector64.html) in\_sourcePosition, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fDistanceScalingFactor, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fLevel) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkVector64](struct_ak_vector64.html) | [sourcePosition](struct_ak_image_source_params_a2e54fdb6e559ed703bd8c7612b24e55d.html#a2e54fdb6e559ed703bd8c7612b24e55d) |
|  | Image source position, relative to the world. [更多...](struct_ak_image_source_params_a2e54fdb6e559ed703bd8c7612b24e55d.html#a2e54fdb6e559ed703bd8c7612b24e55d) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fDistanceScalingFactor](struct_ak_image_source_params_a1b16cbf38c143fd693eb407fffc4dc59.html#a1b16cbf38c143fd693eb407fffc4dc59) |
|  | Image source distance scaling. This number effectively scales the sourcePosition vector with respect to the listener and, consequently, scales distance and preserves orientation. [更多...](struct_ak_image_source_params_a1b16cbf38c143fd693eb407fffc4dc59.html#a1b16cbf38c143fd693eb407fffc4dc59) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fLevel](struct_ak_image_source_params_ac6adade37cf47e9ad2ba38b587cface3.html#ac6adade37cf47e9ad2ba38b587cface3) |
|  | Game-controlled level for this source, linear. [更多...](struct_ak_image_source_params_ac6adade37cf47e9ad2ba38b587cface3.html#ac6adade37cf47e9ad2ba38b587cface3) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fDiffraction](struct_ak_image_source_params_ae596eee80eed639db29773bc51de83ac.html#ae596eee80eed639db29773bc51de83ac) |
|  | Diffraction amount, normalized to the range [0,1]. [更多...](struct_ak_image_source_params_ae596eee80eed639db29773bc51de83ac.html#ae596eee80eed639db29773bc51de83ac) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fOcclusion](struct_ak_image_source_params_ab94ae302b44a036b4305795581431661.html#ab94ae302b44a036b4305795581431661) |
|  | Portal occlusion amount, in the range [0,1]. [更多...](struct_ak_image_source_params_ab94ae302b44a036b4305795581431661.html#ab94ae302b44a036b4305795581431661) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [uDiffractionEmitterSide](struct_ak_image_source_params_a5c09d80425f3228a1bbcbd4ddd9eba9a.html#a5c09d80425f3228a1bbcbd4ddd9eba9a) |
|  | If there is a shadow zone diffraction just after the emitter in the reflection path, indicates the number of diffraction edges, otherwise 0 if no diffraction. [更多...](struct_ak_image_source_params_a5c09d80425f3228a1bbcbd4ddd9eba9a.html#a5c09d80425f3228a1bbcbd4ddd9eba9a) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [uDiffractionListenerSide](struct_ak_image_source_params_a0f65cd3d7813be24855a46b9120def80.html#a0f65cd3d7813be24855a46b9120def80) |
|  | If there is a shadow zone diffraction before reaching the listener in the reflection path, indicates the number of diffraction edges, otherwise 0 if no diffraction. [更多...](struct_ak_image_source_params_a0f65cd3d7813be24855a46b9120def80.html#a0f65cd3d7813be24855a46b9120def80) |
|  | |

## 详细描述

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [312](_ak_spatial_audio_types_8h_source.html#l00312) 行定义.