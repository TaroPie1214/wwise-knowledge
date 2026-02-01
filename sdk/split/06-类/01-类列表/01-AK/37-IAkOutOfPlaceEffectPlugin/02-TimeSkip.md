# TimeSkip

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkOutOfPlaceEffectPlugin](class_a_k_1_1_i_ak_out_of_place_effect_plugin.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Execute](class_a_k_1_1_i_ak_out_of_place_effect_plugin_afcf5d07295a19209f16538044ac64fef.html#afcf5d07295a19209f16538044ac64fef) | | [TimeSkip](class_a_k_1_1_i_ak_out_of_place_effect_plugin_a8727a7d95bca7d9a5a7ec21a934d7fb9.html#a8727a7d95bca7d9a5a7ec21a934d7fb9) | | [◆](#a8727a7d95bca7d9a5a7ec21a934d7fb9)TimeSkip() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) AK::IAkOutOfPlaceEffectPlugin::TimeSkip | ( | [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) & | *io\_uFrames* | ) |  | | pure virtual |  Skips execution of some frames, when the voice is virtual playing from elapsed time. This can be used to simulate processing that would have taken place (e.g. update internal state). Return AK\_DataReady or AK\_NoMoreData, depending if there would be audio output or not at that point.  参数  |  |  | | --- | --- | | io\_uFrames | Number of frames the audio processing should advance. The output value should be the number of frames that would be consumed to output the number of frames this parameter has at the input of the function. | |