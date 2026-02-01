# AkSpeakerVolumeMatrixCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_speaker_volume_matrix_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkSpeakerVolumeMatrixCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkSpeakerVolumesMatrixPtr](_ak_typedefs_8h_afcd81d4c2e56d86764346716eca7fe4c.html#afcd81d4c2e56d86764346716eca7fe4c) | [pVolumes](struct_ak_speaker_volume_matrix_callback_info_a8939707c798dfb3687a80a00db8a8c74.html#a8939707c798dfb3687a80a00db8a8c74) |
|  | Pointer to volume matrix describing the contribution of each source channel to destination channels. Use methods of [AK::SpeakerVolumes::Matrix](namespace_a_k_1_1_speaker_volumes_1_1_matrix.html "Volume matrix (multi-in/multi-out channel configurations) services.") to interpret them. [更多...](struct_ak_speaker_volume_matrix_callback_info_a8939707c798dfb3687a80a00db8a8c74.html#a8939707c798dfb3687a80a00db8a8c74) |
|  | |
| struct [AkChannelConfig](struct_ak_channel_config.html) | [inputConfig](struct_ak_speaker_volume_matrix_callback_info_a30e81ba08ad7b60f475ab431af67587f.html#a30e81ba08ad7b60f475ab431af67587f) |
|  | Channel configuration of the voice/bus. [更多...](struct_ak_speaker_volume_matrix_callback_info_a30e81ba08ad7b60f475ab431af67587f.html#a30e81ba08ad7b60f475ab431af67587f) |
|  | |
| struct [AkChannelConfig](struct_ak_channel_config.html) | [outputConfig](struct_ak_speaker_volume_matrix_callback_info_afd0b0f3ada00da404ddf2f3a8d269017.html#afd0b0f3ada00da404ddf2f3a8d269017) |
|  | Channel configuration of the output bus. [更多...](struct_ak_speaker_volume_matrix_callback_info_afd0b0f3ada00da404ddf2f3a8d269017.html#afd0b0f3ada00da404ddf2f3a8d269017) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \* | [pfBaseVolume](struct_ak_speaker_volume_matrix_callback_info_a98f33fbc94ccda839e1069f549ded36e.html#a98f33fbc94ccda839e1069f549ded36e) |
|  | Base volume, common to all channels. [更多...](struct_ak_speaker_volume_matrix_callback_info_a98f33fbc94ccda839e1069f549ded36e.html#a98f33fbc94ccda839e1069f549ded36e) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \* | [pfEmitterListenerVolume](struct_ak_speaker_volume_matrix_callback_info_a1e3f15191739f523ec8955e7e025cf7c.html#a1e3f15191739f523ec8955e7e025cf7c) |
|  | Emitter-listener pair-specific gain. When there are multiple emitter-listener pairs, this volume is set to that of the loudest pair, and the relative gain of other pairs is applied directly on the channel volume matrix pVolumes. [更多...](struct_ak_speaker_volume_matrix_callback_info_a1e3f15191739f523ec8955e7e025cf7c.html#a1e3f15191739f523ec8955e7e025cf7c) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [mixConnectionGameObjId](struct_ak_speaker_volume_matrix_callback_info_ac33a3cdea27f81d741802dfd73e44d7c.html#ac33a3cdea27f81d741802dfd73e44d7c) |
|  | Game Object ID of the mix connection [更多...](struct_ak_speaker_volume_matrix_callback_info_ac33a3cdea27f81d741802dfd73e44d7c.html#ac33a3cdea27f81d741802dfd73e44d7c) |
|  | |
| [AkMixerInputContextPtr](_ak_callback_types_8h_ab4f4becf2477fc5b3afc41da781a50bd.html#ab4f4becf2477fc5b3afc41da781a50bd) | [pContext](struct_ak_speaker_volume_matrix_callback_info_a6930688e64bad2ce4019fc4c19de7962.html#a6930688e64bad2ce4019fc4c19de7962) |
|  | Context of the current voice/bus about to be mixed into the output bus with specified base volume and volume matrix. [更多...](struct_ak_speaker_volume_matrix_callback_info_a6930688e64bad2ce4019fc4c19de7962.html#a6930688e64bad2ce4019fc4c19de7962) |
|  | |
| [AkMixerPluginContextPtr](_ak_callback_types_8h_a9cea4525427dbee2eb129300d2cff556.html#a9cea4525427dbee2eb129300d2cff556) | [pMixerContext](struct_ak_speaker_volume_matrix_callback_info_ac1e8922ff3762c07e99ba3acb98f0bb5.html#ac1e8922ff3762c07e99ba3acb98f0bb5) |
|  | Output mixing bus context. Use it to access a few useful panning and mixing services, as well as the ID of the output bus. NULL if pContext is the Main Audio Bus. [更多...](struct_ak_speaker_volume_matrix_callback_info_ac1e8922ff3762c07e99ba3acb98f0bb5.html#ac1e8922ff3762c07e99ba3acb98f0bb5) |
|  | |

## 详细描述

Callback information structure corresponding to [AK\_SpeakerVolumeMatrix](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a398dd4133debe48731389d00ac8335fe), and passed to callbacks registered in [RegisterBusVolumeCallback()](namespace_a_k_1_1_sound_engine_adc878481e54793302e90f59d1c90202f.html#adc878481e54793302e90f59d1c90202f) or [PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) with AK\_SpeakerVolumeMatrix. These callbacks are called at every audio frame for every connection from an input (voice or bus) to an output bus (standard or auxiliary), at the point when an input signal is about to be mixed into a mixing bus, but just before having been scaled in accordance to volumes authored in Wwise. The volumes are passed via this structure as pointers because they can be modified in the callbacks. They are factored into two linear values ([0..1]): a common base value (pfBaseVolume), that is channel-agnostic and represents the collapsed gain of all volume changes in Wwise (sliders, actions, RTPC, attenuations, ...), and a matrix of gains per input/output channel, which depends on spatialization. Use the methods of AK\_SpeakerVolumes\_Matrix, defined in [AK/SoundEngine/Common/AkSpeakerVolumes.h](_ak_speaker_volumes_8h.html), to perform operations on them. Access each input channel of the volumes matrix with [AK\_SpeakerVolumes\_Matrix\_GetChannel()](_ak_speaker_volumes_8h_a08a63637dabc48bf55d41c9126ac22d0.html#a08a63637dabc48bf55d41c9126ac22d0), passing it the input and output channel configuration. Then, you may access each element of the output vector using the standard bracket [] operator. See [AK/SoundEngine/Common/AkSpeakerVolumes.h](_ak_speaker_volumes_8h.html) for more details. It is crucial that the processing done in the callback be lightweight and non-blocking.

参见
:   - [使用 Speaker Matrix Callback 定制高级混音](goingfurther_speakermatrixcallback.html)
    - [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)
    - [集成详情——事件](soundengine_events.html)
    - [AK::SoundEngine::RegisterBusVolumeCallback()](namespace_a_k_1_1_sound_engine_adc878481e54793302e90f59d1c90202f.html#adc878481e54793302e90f59d1c90202f)

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [226](_ak_callback_types_8h_source.html#l00226) 行定义.