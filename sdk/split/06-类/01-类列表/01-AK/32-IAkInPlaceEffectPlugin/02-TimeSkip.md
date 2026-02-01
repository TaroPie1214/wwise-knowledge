# TimeSkip

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkInPlaceEffectPlugin](class_a_k_1_1_i_ak_in_place_effect_plugin.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Execute](class_a_k_1_1_i_ak_in_place_effect_plugin_a4da7d07eeefbcc0dda9321f94ae99d99.html#a4da7d07eeefbcc0dda9321f94ae99d99) | | [TimeSkip](class_a_k_1_1_i_ak_in_place_effect_plugin_afc80cd74cb7eb9673f49443d0838a941.html#afc80cd74cb7eb9673f49443d0838a941) | | [◆](#afc80cd74cb7eb9673f49443d0838a941)TimeSkip() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) AK::IAkInPlaceEffectPlugin::TimeSkip | ( | [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | *in\_uFrames* | ) |  | | pure virtual |  Skips execution of some frames, when the voice is virtual playing from elapsed time. This can be used to simulate processing that would have taken place (e.g. update internal state). Return AK\_DataReady or AK\_NoMoreData, depending if there would be audio output or not at that point.  参数  |  |  | | --- | --- | | in\_uFrames | Number of frames the audio processing should advance. | |