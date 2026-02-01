# Execute

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkInPlaceObjectPlugin](class_a_k_1_1_i_ak_in_place_object_plugin.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Execute](class_a_k_1_1_i_ak_in_place_object_plugin_a5a99693f1b77d56fed6eb36c43ff013f.html#a5a99693f1b77d56fed6eb36c43ff013f) | | [◆](#a5a99693f1b77d56fed6eb36c43ff013f)Execute() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual void AK::IAkInPlaceObjectPlugin::Execute | ( | const [AkAudioObjects](struct_ak_audio_objects.html) & | *io\_objects* | ) |  | | pure virtual |  In-place object processor plug-in DSP execution.   |  |  | | --- | --- | |  | **备注:** The effect should process all the input data (uValidFrames) of each input object in in\_pObjectsIn as long as AK\_DataReady is passed in their corresponding eState field. When an input object is finished (eState is AK\_NoMoreData), the effect can output more samples than uValidFrames, up to MaxFrames() if desired. The effect must notify the pipeline by updating uValidFrames of a given object if more frames are produced, and by setting its eState to AK\_DataReady as long as more samples will be produced. |   .  参见  [AK::IAkEffectPlugin::Init](class_a_k_1_1_i_ak_effect_plugin_ae5a44837c4adddf6ff58fab57453b020.html#ae5a44837c4adddf6ff58fab57453b020).  参数  |  |  | | --- | --- | | io\_objects | Input/Output objects and object buffers. | |