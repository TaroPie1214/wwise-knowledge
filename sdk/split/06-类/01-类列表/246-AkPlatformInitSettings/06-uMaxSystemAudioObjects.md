# uMaxSystemAudioObjects

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkPlatformInitSettings](struct_ak_platform_init_settings.html)

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [bEnableAvxSupport](struct_ak_platform_init_settings_a97fc3435b5d2358610178443d6848daa.html#a97fc3435b5d2358610178443d6848daa) | | [threadBankManager](struct_ak_platform_init_settings_a1cd3a496ea65bcdb6ace3b43b211e25f.html#a1cd3a496ea65bcdb6ace3b43b211e25f) | | [threadLEngine](struct_ak_platform_init_settings_a85496f71f556e9c59d8af4b423e018ac.html#a85496f71f556e9c59d8af4b423e018ac) | | [threadMonitor](struct_ak_platform_init_settings_aceb6ec44ce21cff07374779bedacda14.html#aceb6ec44ce21cff07374779bedacda14) | | [threadOutputMgr](struct_ak_platform_init_settings_a5df73f6754e569b6764dae69980106f1.html#a5df73f6754e569b6764dae69980106f1) | | [uMaxSystemAudioObjects](struct_ak_platform_init_settings_a9633ca7ce97cec91909f48ca09e458bd.html#a9633ca7ce97cec91909f48ca09e458bd) | | [uNumRefillsInVoice](struct_ak_platform_init_settings_a953085ec90c00bf53ddafc8af700277d.html#a953085ec90c00bf53ddafc8af700277d) | | [uSampleRate](struct_ak_platform_init_settings_a2bf6f000f256b146d6cd36401a234b85.html#a2bf6f000f256b146d6cd36401a234b85) | | [◆](#a9633ca7ce97cec91909f48ca09e458bd)uMaxSystemAudioObjects |  | | --- | | [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) AkPlatformInitSettings::uMaxSystemAudioObjects |  Dictates how many [Microsoft](namespace_microsoft.html) Spatial Sound dynamic objects will be reserved by the System sink. On Windows, other running processes will be prevented from reserving these objects. Set to 0 to disable the use of System Audio Objects. Default is 128.  在文件 [AkWinSoundEngine.h](_ak_win_sound_engine_8h_source.html) 第 [57](_ak_win_sound_engine_8h_source.html#l00057) 行定义. |