# IAkPluginServiceMixer

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceMixer](class_a_k_1_1_i_ak_plugin_service_mixer.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_mixer-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginServiceMixer类 参考abstract

Interface for the "Mixer" plug-in service, to handle mixing together of signals, or applying simple transforms
[更多...](class_a_k_1_1_i_ak_plugin_service_mixer.html#details)

`#include <IAkPlugin.h>`

类 AK::IAkPluginServiceMixer 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_mixer.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [MixNinNChannels](class_a_k_1_1_i_ak_plugin_service_mixer_ad6e7845e97312743d2a9e73aa1efb60d.html#ad6e7845e97312743d2a9e73aa1efb60d) ([AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pInputBuffer, [AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pMixBuffer, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fPrevGain, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fNextGain, [AK::SpeakerVolumes::ConstMatrixPtr](namespace_a_k_1_1_speaker_volumes_ab18a1b6d7ea27c2c3760092d577d0a80.html#ab18a1b6d7ea27c2c3760092d577d0a80) in\_mxPrevVolumes, [AK::SpeakerVolumes::ConstMatrixPtr](namespace_a_k_1_1_speaker_volumes_ab18a1b6d7ea27c2c3760092d577d0a80.html#ab18a1b6d7ea27c2c3760092d577d0a80) in\_mxNextVolumes)=0 |
|  | N to N channels mix [更多...](class_a_k_1_1_i_ak_plugin_service_mixer_ad6e7845e97312743d2a9e73aa1efb60d.html#ad6e7845e97312743d2a9e73aa1efb60d) |
|  | |
| virtual void | [Mix1inNChannels](class_a_k_1_1_i_ak_plugin_service_mixer_ab58149c13bfa05aec79c5b1299d85acc.html#ab58149c13bfa05aec79c5b1299d85acc) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*[AK\_RESTRICT](_platforms_2_windows_2_ak_types_8h_ab66f3fb84361798a69b92a110f8a14cf.html#ab66f3fb84361798a69b92a110f8a14cf) in\_pInChannel, [AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pMixBuffer, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fPrevGain, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fNextGain, [AK::SpeakerVolumes::ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064) in\_vPrevVolumes, [AK::SpeakerVolumes::ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064) in\_vNextVolumes)=0 |
|  | 1 to N channels mix [更多...](class_a_k_1_1_i_ak_plugin_service_mixer_ab58149c13bfa05aec79c5b1299d85acc.html#ab58149c13bfa05aec79c5b1299d85acc) |
|  | |
| virtual void | [MixChannel](class_a_k_1_1_i_ak_plugin_service_mixer_aeb49ac7c9b1335514afa3db3c978ba22.html#aeb49ac7c9b1335514afa3db3c978ba22) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*[AK\_RESTRICT](_platforms_2_windows_2_ak_types_8h_ab66f3fb84361798a69b92a110f8a14cf.html#ab66f3fb84361798a69b92a110f8a14cf) in\_pInBuffer, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*[AK\_RESTRICT](_platforms_2_windows_2_ak_types_8h_ab66f3fb84361798a69b92a110f8a14cf.html#ab66f3fb84361798a69b92a110f8a14cf) in\_pOutBuffer, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fPrevGain, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fNextGain, [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) in\_uNumFrames)=0 |
|  | Single channel mix [更多...](class_a_k_1_1_i_ak_plugin_service_mixer_aeb49ac7c9b1335514afa3db3c978ba22.html#aeb49ac7c9b1335514afa3db3c978ba22) |
|  | |
| virtual void | [ApplyGainAndInterleave](class_a_k_1_1_i_ak_plugin_service_mixer_a472726d5f39ab39123004df5b84238df.html#a472726d5f39ab39123004df5b84238df) ([AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pInputBuffer, [AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pOutputBuffer, [AkRamp](struct_ak_ramp.html) in\_gain, bool in\_convertToInt16) const =0 |
|  | |
| virtual void | [ApplyGain](class_a_k_1_1_i_ak_plugin_service_mixer_a95fa86eafb55d2a64f9150d31ad70a61.html#a95fa86eafb55d2a64f9150d31ad70a61) ([AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pInputBuffer, [AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pOutputBuffer, [AkRamp](struct_ak_ramp.html) in\_gain, bool in\_convertToInt16) const =0 |
|  | |
| virtual void | [ProcessBiquadFilter](class_a_k_1_1_i_ak_plugin_service_mixer_a63fdf841a2e936d56a216db3a5f3789d.html#a63fdf841a2e936d56a216db3a5f3789d) ([AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pInputBuffer, [AkAudioBuffer](class_ak_audio_buffer.html) \*io\_pOutputBuffer, [AK::AkBiquadCoefficients](struct_a_k_1_1_ak_biquad_coefficients.html) \*in\_pCoefs, [AK::AkBiquadMemories](struct_a_k_1_1_ak_biquad_memories.html) \*io\_pMemories, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumSamples)=0 |
|  | |
| virtual void | [ProcessInterpBiquadFilter](class_a_k_1_1_i_ak_plugin_service_mixer_a7ee1fcef7af61ce90721b5296abddfb4.html#a7ee1fcef7af61ce90721b5296abddfb4) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*\*in\_ppInputData, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*\*io\_ppOutputData, [AK::AkBiquadCoefficients](struct_a_k_1_1_ak_biquad_coefficients.html) \*\*in\_ppCoefs, [AK::AkBiquadMemories](struct_a_k_1_1_ak_biquad_memories.html) \*\*io\_ppMemories, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) \*in\_pNumSamplesPerInterpStage, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumInterpStages, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels)=0 |
|  | |
| virtual void | [ProcessPairedBiquadFilter](class_a_k_1_1_i_ak_plugin_service_mixer_a94bbfd469703fbdf25bdaf123ccc4fec.html#a94bbfd469703fbdf25bdaf123ccc4fec) ([AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pInputBuffer, [AkAudioBuffer](class_ak_audio_buffer.html) \*io\_pOutputBuffer, [AK::AkBiquadCoefficients](struct_a_k_1_1_ak_biquad_coefficients.html) \*in\_pCoefs1, [AK::AkBiquadMemories](struct_a_k_1_1_ak_biquad_memories.html) \*io\_pMemories1, [AK::AkBiquadCoefficients](struct_a_k_1_1_ak_biquad_coefficients.html) \*in\_pCoefs2, [AK::AkBiquadMemories](struct_a_k_1_1_ak_biquad_memories.html) \*io\_pMemories2, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumSamples)=0 |
|  | |
| virtual void | [ProcessPairedInterpBiquadFilter](class_a_k_1_1_i_ak_plugin_service_mixer_a219e287bcfacd57b97c811f1487ff78f.html#a219e287bcfacd57b97c811f1487ff78f) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*\*in\_ppInputData, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*\*io\_ppOutputData, [AK::AkBiquadCoefficients](struct_a_k_1_1_ak_biquad_coefficients.html) \*\*in\_ppCoefs1, [AK::AkBiquadMemories](struct_a_k_1_1_ak_biquad_memories.html) \*\*io\_ppMemories1, [AK::AkBiquadCoefficients](struct_a_k_1_1_ak_biquad_coefficients.html) \*\*in\_ppCoefs2, [AK::AkBiquadMemories](struct_a_k_1_1_ak_biquad_memories.html) \*\*io\_ppMemories2, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) \*in\_pNumSamplesPerInterpStage, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumInterpStages, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels)=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServiceMixer](class_a_k_1_1_i_ak_plugin_service_mixer_a8d06351592584d03baf22ff62d1d6da0.html#a8d06351592584d03baf22ff62d1d6da0) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

## 详细描述

Interface for the "Mixer" plug-in service, to handle mixing together of signals, or applying simple transforms

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1740](_i_ak_plugin_8h_source.html#l01740) 行定义.