# AkDeviceDescription

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_device_description-members.html) |
[Public 属性](#pub-attribs)

AkDeviceDescription结构体 参考

`#include <AkSoundEngineTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [idDevice](struct_ak_device_description_a5e1be4d07a51040ccc6ff04a38e7d47c.html#a5e1be4d07a51040ccc6ff04a38e7d47c) |
|  | Device ID for Wwise. This is the same as what is returned from [AK::GetDeviceID](namespace_a_k_a84b3896b7b5b223c72b5ea826fae6bd8.html#a84b3896b7b5b223c72b5ea826fae6bd8) and [AK::GetDeviceIDFromName](namespace_a_k_a8609f19bc85d9ea8266c2fdd79ac5084.html#a8609f19bc85d9ea8266c2fdd79ac5084). Use it to specify the main device in AkPlatformInitSettings.idAudioDevice or in AK::SoundEngine::AddSecondaryOutput. [更多...](struct_ak_device_description_a5e1be4d07a51040ccc6ff04a38e7d47c.html#a5e1be4d07a51040ccc6ff04a38e7d47c) |
|  | |
| [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) | [deviceName](struct_ak_device_description_a92fab106652fec366709aaee87383e5f.html#a92fab106652fec366709aaee87383e5f) [[AK\_MAX\_PATH](_platforms_2_windows_2_ak_types_8h_ac1096fa0921ee445f47e145c167eab4b.html#ac1096fa0921ee445f47e145c167eab4b)] |
|  | The user-friendly name for the device. [更多...](struct_ak_device_description_a92fab106652fec366709aaee87383e5f.html#a92fab106652fec366709aaee87383e5f) |
|  | |
| enum [AkAudioDeviceState](_ak_enums_8h_a3095a5c69f4c12a6362aaa77cd1ac476.html#a3095a5c69f4c12a6362aaa77cd1ac476) | [deviceStateMask](struct_ak_device_description_ac0acc1661266c664aae7d9fd983315eb.html#ac0acc1661266c664aae7d9fd983315eb) |
|  | Bitmask used to filter the device based on their state. [更多...](struct_ak_device_description_ac0acc1661266c664aae7d9fd983315eb.html#ac0acc1661266c664aae7d9fd983315eb) |
|  | |
| bool | [isDefaultDevice](struct_ak_device_description_aff286ff755788f1997fc4bf34846824f.html#aff286ff755788f1997fc4bf34846824f) |
|  | Identify default device. Always false when not supported. [更多...](struct_ak_device_description_aff286ff755788f1997fc4bf34846824f.html#aff286ff755788f1997fc4bf34846824f) |
|  | |

## 详细描述

在文件 [AkSoundEngineTypes.h](_ak_sound_engine_types_8h_source.html) 第 [56](_ak_sound_engine_types_8h_source.html#l00056) 行定义.