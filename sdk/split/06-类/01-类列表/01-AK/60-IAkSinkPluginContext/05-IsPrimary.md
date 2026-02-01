# IsPrimary

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkSinkPluginContext](class_a_k_1_1_i_ak_sink_plugin_context.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ComputePositioning](class_a_k_1_1_i_ak_sink_plugin_context_acd63722fe98287b2a61f5fe161d9042b.html#acd63722fe98287b2a61f5fe161d9042b) | | [GetNumRefillsInVoice](class_a_k_1_1_i_ak_sink_plugin_context_adfdd36812a616fe5c028b610e3bbf8a6.html#adfdd36812a616fe5c028b610e3bbf8a6) | | [GetPanningRule](class_a_k_1_1_i_ak_sink_plugin_context_a96a5371f48fcb34ba6fd2e9fddee8bf5.html#a96a5371f48fcb34ba6fd2e9fddee8bf5) | | [IsPrimary](class_a_k_1_1_i_ak_sink_plugin_context_a5d58583faf36a78c237f2f761c8594d3.html#a5d58583faf36a78c237f2f761c8594d3) | | [SetOutputDeviceInfoCustomData](class_a_k_1_1_i_ak_sink_plugin_context_ae772afa489bbda9f1f328309c0d9b25a.html#ae772afa489bbda9f1f328309c0d9b25a) | | [SignalAudioThread](class_a_k_1_1_i_ak_sink_plugin_context_ad0efd9efdaa789dc4d1bde887119272b.html#ad0efd9efdaa789dc4d1bde887119272b) | | [~IAkSinkPluginContext](class_a_k_1_1_i_ak_sink_plugin_context_a8cb48fd2e25d49e0c8cc16411e91bf37.html#a8cb48fd2e25d49e0c8cc16411e91bf37) | | [◆](#a5d58583faf36a78c237f2f761c8594d3)IsPrimary() |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | virtual bool AK::IAkSinkPluginContext::IsPrimary | ( |  | ) |  | | pure virtual |  Query if the sink plugin is instantiated on the main output device (primary tree).  返回  True if the sink plugin is instantiated on the main output device (primary tree), false otherwise.  参见  - [AK::IAkSinkPlugin::IsDataNeeded()](class_a_k_1_1_i_ak_sink_plugin_base_a80d001f02f2c602683951e51a795954e.html#a80d001f02f2c602683951e51a795954e) - [AK::IAkSinkPlugin::Consume()](class_a_k_1_1_i_ak_sink_plugin_a72ea6266f695a0672ee0af6eaca81342.html#a72ea6266f695a0672ee0af6eaca81342) |