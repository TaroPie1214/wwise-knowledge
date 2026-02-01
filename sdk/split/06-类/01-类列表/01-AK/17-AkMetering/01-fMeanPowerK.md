# fMeanPowerK

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [AkMetering](struct_a_k_1_1_ak_metering.html)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [fMeanPowerK](struct_a_k_1_1_ak_metering_a4fbf7a87a580a2653bd90196c16f58c5.html#a4fbf7a87a580a2653bd90196c16f58c5) | | [peak](struct_a_k_1_1_ak_metering_a954f2565f746bb389d4e0a3ee6f42668.html#a954f2565f746bb389d4e0a3ee6f42668) | | [rms](struct_a_k_1_1_ak_metering_ad074a15a5d85663056aec3bb87ada2b0.html#ad074a15a5d85663056aec3bb87ada2b0) | | [truePeak](struct_a_k_1_1_ak_metering_afb41ff18e6678d0c573b83e14d5ab61a.html#afb41ff18e6678d0c573b83e14d5ab61a) | | [◆](#a4fbf7a87a580a2653bd90196c16f58c5)fMeanPowerK |  | | --- | | [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) AK::AkMetering::fMeanPowerK |  Mean k-weighted power value in this frame, used to compute loudness (as defined by ITU-R BS.1770). Total linear k-weighted power of all channels. 0 if AK\_EnableBusMeter\_KPower is not set (see IAkMixerPluginContext::SetMeteringFlags() or [AK::SoundEngine::RegisterBusMeteringCallback()](namespace_a_k_1_1_sound_engine_a4935dbc8c375c82c03475a1dbde37a51.html#a4935dbc8c375c82c03475a1dbde37a51)).  在文件 [AkCommonDefs.h](_ak_common_defs_8h_source.html) 第 [208](_ak_common_defs_8h_source.html#l00208) 行定义. |