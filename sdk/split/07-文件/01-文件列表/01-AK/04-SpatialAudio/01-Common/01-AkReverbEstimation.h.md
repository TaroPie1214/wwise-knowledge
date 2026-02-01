# AkReverbEstimation.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SpatialAudio](dir_e8de1cf052ef123fb045439c856e4598.html)
- [Common](dir_63e2f66e68c54d3307d872c42bbe429e.html)

[命名空间](#namespaces)

AkReverbEstimation.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/SpatialAudio/Common/AkSpatialAudio.h>`  
`#include <AK/SoundEngine/Common/AkVirtualAcoustics.h>`

[浏览源代码.](_ak_reverb_estimation_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::SpatialAudio](namespace_a_k_1_1_spatial_audio.html) |
|  | Audiokinetic spatial audio namespace |
|  | |
|  | [AK::SpatialAudio::ReverbEstimation](namespace_a_k_1_1_spatial_audio_1_1_reverb_estimation.html) |
|  | Audiokinetic reverb estimation namespace |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| Reverb estimation. | |
| These functions can be used to estimate the reverb parameters of a physical environment, using its volume and surface area | |
| float | [AK::SpatialAudio::ReverbEstimation::CalculateSlope](namespace_a_k_1_1_spatial_audio_1_1_reverb_estimation_a9d4a5599a4776667eb346eec6052791e.html#a9d4a5599a4776667eb346eec6052791e) (const [AkAcousticTexture](struct_ak_acoustic_texture.html) &texture) |
|  | |
| void | [AK::SpatialAudio::ReverbEstimation::GetAverageAbsorptionValues](namespace_a_k_1_1_spatial_audio_1_1_reverb_estimation_a9269b16eedbf87eed9fdeb456c58709f.html#a9269b16eedbf87eed9fdeb456c58709f) ([AkAcousticTexture](struct_ak_acoustic_texture.html) \*in\_textures, float \*in\_surfaceAreas, int in\_numTextures, [AkAcousticTexture](struct_ak_acoustic_texture.html) &out\_average) |
|  | Calculate average absorption values using each of the textures in in\_textures, weighted by their corresponding surface area. [更多...](namespace_a_k_1_1_spatial_audio_1_1_reverb_estimation_a9269b16eedbf87eed9fdeb456c58709f.html#a9269b16eedbf87eed9fdeb456c58709f) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::SpatialAudio::ReverbEstimation::EstimateT60Decay](namespace_a_k_1_1_spatial_audio_1_1_reverb_estimation_aec6a508d25d6da739457f1eb6f0aac53.html#aec6a508d25d6da739457f1eb6f0aac53) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_volumeCubicMeters, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_surfaceAreaSquaredMeters, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_environmentAverageAbsorption, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_decayEstimate) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::SpatialAudio::ReverbEstimation::EstimateTimeToFirstReflection](namespace_a_k_1_1_spatial_audio_1_1_reverb_estimation_a58a735c2257525485f8be06920e19b82.html#a58a735c2257525485f8be06920e19b82) ([AkVector](struct_ak_vector.html) in\_environmentExtentMeters, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_timeToFirstReflectionMs, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_speedOfSound=343.0f) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AK::SpatialAudio::ReverbEstimation::EstimateHFDamping](namespace_a_k_1_1_spatial_audio_1_1_reverb_estimation_a2be1de76cd8b9ddf95217f06b02ebad6.html#a2be1de76cd8b9ddf95217f06b02ebad6) ([AkAcousticTexture](struct_ak_acoustic_texture.html) \*in\_textures, float \*in\_surfaceAreas, int in\_numTextures) |
|  | |

## 详细描述

Reverb parameter estimation.

在文件 [AkReverbEstimation.h](_ak_reverb_estimation_8h_source.html) 中定义.