# AkWinSoundEngine.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Platforms](dir_9707d8b0bea28caa964fded672ce5309.html)
- [Windows](dir_cb4788f46f1673a960402c6d809f92c5.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[函数](#func-members)

AkWinSoundEngine.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/Tools/Common/AkPlatformFuncs.h>`

[浏览源代码.](_ak_win_sound_engine_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkPlatformInitSettings](struct_ak_platform_init_settings.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK::GetDeviceID](namespace_a_k_a84b3896b7b5b223c72b5ea826fae6bd8.html#a84b3896b7b5b223c72b5ea826fae6bd8) (IMMDevice \*in\_pDevice) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK::GetDeviceIDFromName](namespace_a_k_a8609f19bc85d9ea8266c2fdd79ac5084.html#a8609f19bc85d9ea8266c2fdd79ac5084) (wchar\_t \*in\_szToken) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) const wchar\_t \* | [AK::GetWindowsDeviceName](namespace_a_k_a5ce827d21b248fbf326b46c75d080c21.html#a5ce827d21b248fbf326b46c75d080c21) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) index, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uDeviceID, [AkAudioDeviceState](_ak_enums_8h_a3095a5c69f4c12a6362aaa77cd1ac476.html#a3095a5c69f4c12a6362aaa77cd1ac476) uDeviceStateMask=[AkDeviceState\_All](_ak_enums_8h_a3095a5c69f4c12a6362aaa77cd1ac476.html#a3095a5c69f4c12a6362aaa77cd1ac476a73ec2f6470842e3962dd08c5e7468d1a)) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK::GetWindowsDeviceCount](namespace_a_k_adc935e72c08f3108e358888ba0622ccd.html#adc935e72c08f3108e358888ba0622ccd) ([AkAudioDeviceState](_ak_enums_8h_a3095a5c69f4c12a6362aaa77cd1ac476.html#a3095a5c69f4c12a6362aaa77cd1ac476) uDeviceStateMask=[AkDeviceState\_All](_ak_enums_8h_a3095a5c69f4c12a6362aaa77cd1ac476.html#a3095a5c69f4c12a6362aaa77cd1ac476a73ec2f6470842e3962dd08c5e7468d1a)) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) bool | [AK::GetWindowsDevice](namespace_a_k_ab02747c480440f19f08d2ef1199ce4f6.html#ab02747c480440f19f08d2ef1199ce4f6) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_index, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uDeviceID, IMMDevice \*\*out\_ppDevice, [AkAudioDeviceState](_ak_enums_8h_a3095a5c69f4c12a6362aaa77cd1ac476.html#a3095a5c69f4c12a6362aaa77cd1ac476) uDeviceStateMask=[AkDeviceState\_All](_ak_enums_8h_a3095a5c69f4c12a6362aaa77cd1ac476.html#a3095a5c69f4c12a6362aaa77cd1ac476a73ec2f6470842e3962dd08c5e7468d1a)) |
|  | |

## 详细描述

Main Sound Engine interface, specific WIN32.

在文件 [AkWinSoundEngine.h](_ak_win_sound_engine_8h_source.html) 中定义.