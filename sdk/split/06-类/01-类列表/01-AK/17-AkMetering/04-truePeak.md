# truePeak

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [AkMetering](struct_a_k_1_1_ak_metering.html)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [fMeanPowerK](struct_a_k_1_1_ak_metering_a4fbf7a87a580a2653bd90196c16f58c5.html#a4fbf7a87a580a2653bd90196c16f58c5) | | [peak](struct_a_k_1_1_ak_metering_a954f2565f746bb389d4e0a3ee6f42668.html#a954f2565f746bb389d4e0a3ee6f42668) | | [rms](struct_a_k_1_1_ak_metering_ad074a15a5d85663056aec3bb87ada2b0.html#ad074a15a5d85663056aec3bb87ada2b0) | | [truePeak](struct_a_k_1_1_ak_metering_afb41ff18e6678d0c573b83e14d5ab61a.html#afb41ff18e6678d0c573b83e14d5ab61a) | | [◆](#afb41ff18e6678d0c573b83e14d5ab61a)truePeak |  | | --- | | [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) AK::AkMetering::truePeak |  True peak of each channel (as defined by ITU-R BS.1770) in this frame. Vector of linear true peak levels, corresponding to each channel. NULL if AK\_EnableBusMeter\_TruePeak is not set (see IAkMixerPluginContext::SetMeteringFlags() or [AK::SoundEngine::RegisterBusMeteringCallback()](namespace_a_k_1_1_sound_engine_a4935dbc8c375c82c03475a1dbde37a51.html#a4935dbc8c375c82c03475a1dbde37a51)).  在文件 [AkCommonDefs.h](_ak_common_defs_8h_source.html) 第 [200](_ak_common_defs_8h_source.html#l00200) 行定义. |