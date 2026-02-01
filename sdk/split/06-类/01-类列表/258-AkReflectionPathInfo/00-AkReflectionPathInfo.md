# AkReflectionPathInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_reflection_path_info-members.html) |
[Public 属性](#pub-attribs)

AkReflectionPathInfo结构体 参考

Structure for retrieving information about the indirect paths of a sound that have been calculated via the geometric reflections API. Useful for debug draw applications.
[更多...](struct_ak_reflection_path_info.html#details)

`#include <AkSpatialAudioTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkVector64](struct_ak_vector64.html) | [imageSource](struct_ak_reflection_path_info_a436653d1c149125f55a0c46ecb3a1955.html#a436653d1c149125f55a0c46ecb3a1955) |
|  | Apparent source of the reflected sound that follows this path. [更多...](struct_ak_reflection_path_info_a436653d1c149125f55a0c46ecb3a1955.html#a436653d1c149125f55a0c46ecb3a1955) |
|  | |
| struct [AkVector64](struct_ak_vector64.html) | [pathPoint](struct_ak_reflection_path_info_ac5a677db0f71c7700b8aafb478142f18.html#ac5a677db0f71c7700b8aafb478142f18) [[AK\_MAX\_REFLECTION\_PATH\_LENGTH](_ak_spatial_audio_types_8h_a6c8404a53ed551035147b6736cdcf2b2.html#a6c8404a53ed551035147b6736cdcf2b2)] |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [textureIDs](struct_ak_reflection_path_info_a321b02541488f6ba2e6ca75979e05c17.html#a321b02541488f6ba2e6ca75979e05c17) [[AK\_MAX\_REFLECTION\_PATH\_LENGTH](_ak_spatial_audio_types_8h_a6c8404a53ed551035147b6736cdcf2b2.html#a6c8404a53ed551035147b6736cdcf2b2)] |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numPathPoints](struct_ak_reflection_path_info_ac2c97d22a584e7177fc3ab97969d538f.html#ac2c97d22a584e7177fc3ab97969d538f) |
|  | Number of valid elements in the `pathPoint`[], `surfaces`[], and `diffraction`[] arrays. [更多...](struct_ak_reflection_path_info_ac2c97d22a584e7177fc3ab97969d538f.html#ac2c97d22a584e7177fc3ab97969d538f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numReflections](struct_ak_reflection_path_info_a9a1d31d317e23146da39280528dba6cf.html#a9a1d31d317e23146da39280528dba6cf) |
|  | Number of reflections in the `pathPoint`[] array. Shadow zone diffraction does not count as a reflection. If there is no shadow zone diffraction, `numReflections` is equal to `numPathPoints`. [更多...](struct_ak_reflection_path_info_a9a1d31d317e23146da39280528dba6cf.html#a9a1d31d317e23146da39280528dba6cf) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [diffraction](struct_ak_reflection_path_info_ac1ca1c40c408b573a1f0baff99b7ee96.html#ac1ca1c40c408b573a1f0baff99b7ee96) [[AK\_MAX\_REFLECTION\_PATH\_LENGTH](_ak_spatial_audio_types_8h_a6c8404a53ed551035147b6736cdcf2b2.html#a6c8404a53ed551035147b6736cdcf2b2)] |
|  | Diffraction amount, normalized to the range [0,1] [更多...](struct_ak_reflection_path_info_ac1ca1c40c408b573a1f0baff99b7ee96.html#ac1ca1c40c408b573a1f0baff99b7ee96) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [level](struct_ak_reflection_path_info_a867c2bcdc219e917b8b8d39737a71484.html#a867c2bcdc219e917b8b8d39737a71484) |
|  | Linear gain applied to image source. [更多...](struct_ak_reflection_path_info_a867c2bcdc219e917b8b8d39737a71484.html#a867c2bcdc219e917b8b8d39737a71484) |
|  | |
| bool | [isOccluded](struct_ak_reflection_path_info_aebbb8213b85df2ec9452fc5c2ca9663a.html#aebbb8213b85df2ec9452fc5c2ca9663a) |
|  | Deprecated - always false. Occluded paths are not generated. [更多...](struct_ak_reflection_path_info_aebbb8213b85df2ec9452fc5c2ca9663a.html#aebbb8213b85df2ec9452fc5c2ca9663a) |
|  | |

## 详细描述

Structure for retrieving information about the indirect paths of a sound that have been calculated via the geometric reflections API. Useful for debug draw applications.

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [490](_ak_spatial_audio_types_8h_source.html#l00490) 行定义.