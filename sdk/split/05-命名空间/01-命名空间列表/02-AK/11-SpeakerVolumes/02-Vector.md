# Vector

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [SpeakerVolumes](namespace_a_k_1_1_speaker_volumes.html)
- [Vector](namespace_a_k_1_1_speaker_volumes_1_1_vector.html)

[函数](#func-members)

AK::SpeakerVolumes::Vector 命名空间参考

Volume vector services.
[更多...](namespace_a_k_1_1_speaker_volumes_1_1_vector.html#details)

|  |  |
| --- | --- |
| 函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Copy](namespace_a_k_1_1_speaker_volumes_1_1_vector_ae64d6962cea2c02e873cd35d9d43963e.html#ae64d6962cea2c02e873cd35d9d43963e) ([VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) in\_pVolumesDst, [ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064) in\_pVolumesSrc, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Copy](namespace_a_k_1_1_speaker_volumes_1_1_vector_a90cb923c3c948857ae7ab0262c70b9a0.html#a90cb923c3c948857ae7ab0262c70b9a0) ([VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) in\_pVolumesDst, [ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064) in\_pVolumesSrc, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fGain) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Zero](namespace_a_k_1_1_speaker_volumes_1_1_vector_ab3e9493d57989853867861ac6422c67e.html#ab3e9493d57989853867861ac6422c67e) ([VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) in\_pVolumes, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Add](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5d7c7363ea441cdeae6cdbad1a0879dd.html#a5d7c7363ea441cdeae6cdbad1a0879dd) ([VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) in\_pVolumesDst, [ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064) in\_pVolumesSrc, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [L1Norm](namespace_a_k_1_1_speaker_volumes_1_1_vector_ae58908e47c161e2e48103455262f9e91.html#ae58908e47c161e2e48103455262f9e91) ([ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064) io\_pVolumes, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Mul](namespace_a_k_1_1_speaker_volumes_1_1_vector_af91fae5dc1aab3a3755c213f4978a92c.html#af91fae5dc1aab3a3755c213f4978a92c) ([VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) in\_pVolumesDst, const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fVol, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Mul](namespace_a_k_1_1_speaker_volumes_1_1_vector_afcb84c662659928bfd56d88ca16dd5c4.html#afcb84c662659928bfd56d88ca16dd5c4) ([VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) in\_pVolumesDst, [ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064) in\_pVolumesSrc, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*in\_pVolumesDst, const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*in\_pVolumesSrc, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*in\_pVolumesDst, const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*in\_pVolumesSrc, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | |

## 详细描述

Volume vector services.