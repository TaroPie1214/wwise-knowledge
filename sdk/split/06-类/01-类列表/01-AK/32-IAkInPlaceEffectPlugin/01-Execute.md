# Execute

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkInPlaceEffectPlugin](class_a_k_1_1_i_ak_in_place_effect_plugin.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Execute](class_a_k_1_1_i_ak_in_place_effect_plugin_a4da7d07eeefbcc0dda9321f94ae99d99.html#a4da7d07eeefbcc0dda9321f94ae99d99) | | [TimeSkip](class_a_k_1_1_i_ak_in_place_effect_plugin_afc80cd74cb7eb9673f49443d0838a941.html#afc80cd74cb7eb9673f49443d0838a941) | | [◆](#a4da7d07eeefbcc0dda9321f94ae99d99)Execute() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual void AK::IAkInPlaceEffectPlugin::Execute | ( | [AkAudioBuffer](class_ak_audio_buffer.html) \* | *io\_pBuffer* | ) |  | | pure virtual |  Software effect plug-in DSP execution for in-place processing.   |  |  |  |  | | --- | --- | --- | --- | |  | **备注:** The effect should process all the input data (uValidFrames) as long as AK\_DataReady is passed in the eState field. When the input is finished (AK\_NoMoreData), the effect can output more sample than uValidFrames up to MaxFrames() if desired. All sample frames beyond uValidFrames are not initialized and it is the responsibility of the effect to do so when outputting an effect tail. The effect must notify the pipeline by updating uValidFrames if more frames are produced during the effect tail.  |  |  | | --- | --- | |  | **备注:** The effect will stop being called by the pipeline when AK\_NoMoreData is returned in the the eState field of the [AkAudioBuffer](class_ak_audio_buffer.html) structure. See [IAkInPlaceEffectPlugin::Execute](soundengine_plugins_effects.html#iakmonadiceffect_execute_general). | |   参数  |  |  | | --- | --- | | io\_pBuffer | In/Out audio buffer data structure (in-place processing) | |