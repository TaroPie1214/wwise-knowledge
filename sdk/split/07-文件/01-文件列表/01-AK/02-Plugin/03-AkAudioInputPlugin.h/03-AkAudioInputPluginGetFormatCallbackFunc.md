# AkAudioInputPluginGetFormatCallbackFunc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Plugin](dir_815d3776a7d381c10e5f611b84aea7f6.html)
- [AkAudioInputPlugin.h](_ak_audio_input_plugin_8h.html)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AkAudioInputPluginExecuteCallbackFunc](_ak_audio_input_plugin_8h_a27b5a1a19c611de4eb85beb4e5fbb698.html#a27b5a1a19c611de4eb85beb4e5fbb698) | | [AkAudioInputPluginGetFormatCallbackFunc](_ak_audio_input_plugin_8h_aad871e20a8b120f2b436d22157ac7187.html#aad871e20a8b120f2b436d22157ac7187) | | [AkAudioInputPluginGetGainCallbackFunc](_ak_audio_input_plugin_8h_ab5446c97a0cd566cc2102b63b9d71fc0.html#ab5446c97a0cd566cc2102b63b9d71fc0) | | [AKSOURCEID\_AUDIOINPUT](_ak_audio_input_plugin_8h_aa9252725f05a55ad219fb562238ea08c.html#aa9252725f05a55ad219fb562238ea08c) | | [SetAudioInputCallbacks](_ak_audio_input_plugin_8h_a8af9a8fca59e66e75f68b987e3f48db7.html#a8af9a8fca59e66e75f68b987e3f48db7) | | [◆](#aad871e20a8b120f2b436d22157ac7187)AkAudioInputPluginGetFormatCallbackFunc |  | | --- | | typedef void( \* AkAudioInputPluginGetFormatCallbackFunc) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkAudioFormat](struct_ak_audio_format.html) &io\_AudioFormat) |  Callback requesting for the [AkAudioFormat](struct_ak_audio_format.html "Defines the parameters of an audio buffer format.") to use for the plug-in instance. See the Source Input plugin documentation to learn more about the valid formats.  参见  [创建声音引擎源插件](soundengine_plugins_source.html)  在文件 [AkAudioInputPlugin.h](_ak_audio_input_plugin_8h_source.html) 第 [40](_ak_audio_input_plugin_8h_source.html#l00040) 行定义. |