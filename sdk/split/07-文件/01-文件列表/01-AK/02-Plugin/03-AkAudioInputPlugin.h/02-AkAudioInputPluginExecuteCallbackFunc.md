# AkAudioInputPluginExecuteCallbackFunc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Plugin](dir_815d3776a7d381c10e5f611b84aea7f6.html)
- [AkAudioInputPlugin.h](_ak_audio_input_plugin_8h.html)

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AkAudioInputPluginExecuteCallbackFunc](_ak_audio_input_plugin_8h_a27b5a1a19c611de4eb85beb4e5fbb698.html#a27b5a1a19c611de4eb85beb4e5fbb698) | | [AkAudioInputPluginGetFormatCallbackFunc](_ak_audio_input_plugin_8h_aad871e20a8b120f2b436d22157ac7187.html#aad871e20a8b120f2b436d22157ac7187) | | [AkAudioInputPluginGetGainCallbackFunc](_ak_audio_input_plugin_8h_ab5446c97a0cd566cc2102b63b9d71fc0.html#ab5446c97a0cd566cc2102b63b9d71fc0) | | [AKSOURCEID\_AUDIOINPUT](_ak_audio_input_plugin_8h_aa9252725f05a55ad219fb562238ea08c.html#aa9252725f05a55ad219fb562238ea08c) | | [SetAudioInputCallbacks](_ak_audio_input_plugin_8h_a8af9a8fca59e66e75f68b987e3f48db7.html#a8af9a8fca59e66e75f68b987e3f48db7) | | [◆](#a27b5a1a19c611de4eb85beb4e5fbb698)AkAudioInputPluginExecuteCallbackFunc |  | | --- | | typedef void( \* AkAudioInputPluginExecuteCallbackFunc) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkAudioBuffer](class_ak_audio_buffer.html) \*io\_pBufferOut) |  Callback requesting for new data for playback.  参数  |  |  | | --- | --- | | in\_playingID | Playing ID (same that was returned from the PostEvent call) | | io\_pBufferOut | Buffer to fill |  备注  See IntegrationDemo sample for a sample on how to implement it.  在文件 [AkAudioInputPlugin.h](_ak_audio_input_plugin_8h_source.html) 第 [55](_ak_audio_input_plugin_8h_source.html#l00055) 行定义. |