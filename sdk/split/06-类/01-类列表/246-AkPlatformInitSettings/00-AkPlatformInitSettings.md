# AkPlatformInitSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_platform_init_settings-members.html) |
[Public 属性](#pub-attribs)

AkPlatformInitSettings结构体 参考

`#include <AkWinSoundEngine.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkThreadProperties](struct_ak_thread_properties.html) | [threadLEngine](struct_ak_platform_init_settings_a85496f71f556e9c59d8af4b423e018ac.html#a85496f71f556e9c59d8af4b423e018ac) |
|  | Lower engine threading properties [更多...](struct_ak_platform_init_settings_a85496f71f556e9c59d8af4b423e018ac.html#a85496f71f556e9c59d8af4b423e018ac) |
|  | |
| [AkThreadProperties](struct_ak_thread_properties.html) | [threadOutputMgr](struct_ak_platform_init_settings_a5df73f6754e569b6764dae69980106f1.html#a5df73f6754e569b6764dae69980106f1) |
|  | Ouput thread threading properties [更多...](struct_ak_platform_init_settings_a5df73f6754e569b6764dae69980106f1.html#a5df73f6754e569b6764dae69980106f1) |
|  | |
| [AkThreadProperties](struct_ak_thread_properties.html) | [threadBankManager](struct_ak_platform_init_settings_a1cd3a496ea65bcdb6ace3b43b211e25f.html#a1cd3a496ea65bcdb6ace3b43b211e25f) |
|  | Bank manager threading properties (its default priority is AK\_THREAD\_PRIORITY\_NORMAL) [更多...](struct_ak_platform_init_settings_a1cd3a496ea65bcdb6ace3b43b211e25f.html#a1cd3a496ea65bcdb6ace3b43b211e25f) |
|  | |
| [AkThreadProperties](struct_ak_thread_properties.html) | [threadMonitor](struct_ak_platform_init_settings_aceb6ec44ce21cff07374779bedacda14.html#aceb6ec44ce21cff07374779bedacda14) |
|  | Monitor threading properties (its default priority is AK\_THREAD\_PRIORITY\_ABOVENORMAL). This parameter is not used in Release build. [更多...](struct_ak_platform_init_settings_aceb6ec44ce21cff07374779bedacda14.html#aceb6ec44ce21cff07374779bedacda14) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [uNumRefillsInVoice](struct_ak_platform_init_settings_a953085ec90c00bf53ddafc8af700277d.html#a953085ec90c00bf53ddafc8af700277d) |
|  | Number of refill buffers in voice buffer. 2 == double-buffered, defaults to 4. [更多...](struct_ak_platform_init_settings_a953085ec90c00bf53ddafc8af700277d.html#a953085ec90c00bf53ddafc8af700277d) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uSampleRate](struct_ak_platform_init_settings_a2bf6f000f256b146d6cd36401a234b85.html#a2bf6f000f256b146d6cd36401a234b85) |
|  | Sampling Rate. Default is 48000 Hz. Use 24000hz for low quality. Any positive reasonable sample rate is supported. However be careful setting a custom value. Using an odd or really low sample rate may result in malfunctionning sound engine. [更多...](struct_ak_platform_init_settings_a2bf6f000f256b146d6cd36401a234b85.html#a2bf6f000f256b146d6cd36401a234b85) |
|  | |
| bool | [bEnableAvxSupport](struct_ak_platform_init_settings_a97fc3435b5d2358610178443d6848daa.html#a97fc3435b5d2358610178443d6848daa) |
|  | Enables run-time detection of AVX and AVX2 SIMD support in the engine and plug-ins. [更多...](struct_ak_platform_init_settings_a97fc3435b5d2358610178443d6848daa.html#a97fc3435b5d2358610178443d6848daa) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxSystemAudioObjects](struct_ak_platform_init_settings_a9633ca7ce97cec91909f48ca09e458bd.html#a9633ca7ce97cec91909f48ca09e458bd) |
|  | Dictates how many [Microsoft](namespace_microsoft.html) Spatial Sound dynamic objects will be reserved by the System sink. On Windows, other running processes will be prevented from reserving these objects. Set to 0 to disable the use of System Audio Objects. Default is 128. [更多...](struct_ak_platform_init_settings_a9633ca7ce97cec91909f48ca09e458bd.html#a9633ca7ce97cec91909f48ca09e458bd) |
|  | |

## 详细描述

Platform specific initialization settings

参见
:   [AK::SoundEngine::Init](namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a9a26da64092b97243844df77cbcdbf5f)
:   [AK::SoundEngine::GetDefaultPlatformInitSettings](namespace_a_k_1_1_sound_engine_aecdb9cd8f2d7f461ef1a58f5f5f5725d.html#aecdb9cd8f2d7f461ef1a58f5f5f5725d)

在文件 [AkWinSoundEngine.h](_ak_win_sound_engine_8h_source.html) 第 [42](_ak_win_sound_engine_8h_source.html#l00042) 行定义.