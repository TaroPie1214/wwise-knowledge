# OnFrameEnd

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkSinkPluginBase](class_a_k_1_1_i_ak_sink_plugin_base.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetSinkPluginType](class_a_k_1_1_i_ak_sink_plugin_base_ad440b6790f9c09050efea27facecba21.html#ad440b6790f9c09050efea27facecba21) | | [Init](class_a_k_1_1_i_ak_sink_plugin_base_ab13c519292782b8e485912cb85506f25.html#ab13c519292782b8e485912cb85506f25) | | [IsDataNeeded](class_a_k_1_1_i_ak_sink_plugin_base_a80d001f02f2c602683951e51a795954e.html#a80d001f02f2c602683951e51a795954e) | | [IsStarved](class_a_k_1_1_i_ak_sink_plugin_base_a857a107760429d52b05741e31967d82f.html#a857a107760429d52b05741e31967d82f) | | [OnFrameEnd](class_a_k_1_1_i_ak_sink_plugin_base_af7035e026261662fb26bc747eaee77af.html#af7035e026261662fb26bc747eaee77af) | | [ResetStarved](class_a_k_1_1_i_ak_sink_plugin_base_ae63b9e00dbba73aaa35912bc82fd0e3f.html#ae63b9e00dbba73aaa35912bc82fd0e3f) | | [◆](#af7035e026261662fb26bc747eaee77af)OnFrameEnd() |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | virtual void AK::IAkSinkPluginBase::OnFrameEnd | ( |  | ) |  | | pure virtual |  Called at the end of the audio frame. If no Consume calls were made prior to OnFrameEnd, this means no audio was sent to the device. Assume silence.  参见  - [AK::IAkSinkPlugin::Consume()](class_a_k_1_1_i_ak_sink_plugin_a72ea6266f695a0672ee0af6eaca81342.html#a72ea6266f695a0672ee0af6eaca81342) |