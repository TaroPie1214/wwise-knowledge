# AkAuxSendValue

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_aux_send_value-members.html) |
[Public 属性](#pub-attribs)

AkAuxSendValue结构体 参考

Auxiliary bus sends information per game object per given auxiliary bus.
[更多...](struct_ak_aux_send_value.html#details)

`#include <AkSoundEngineTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [listenerID](struct_ak_aux_send_value_a185a87e879e5a602446b07252bdd8519.html#a185a87e879e5a602446b07252bdd8519) |
|  | Game object ID of the listener associated with this send. Use AK\_INVALID\_GAME\_OBJECT as a wildcard to set the auxiliary send to all connected listeners (see [AK::SoundEngine::SetListeners](namespace_a_k_1_1_sound_engine_a2f85a55c38afa2e0dbc6172a7bec91d1.html#a2f85a55c38afa2e0dbc6172a7bec91d1)). [更多...](struct_ak_aux_send_value_a185a87e879e5a602446b07252bdd8519.html#a185a87e879e5a602446b07252bdd8519) |
|  | |
| [AkAuxBusID](_ak_typedefs_8h_a90cfd84c4feec568941a46c13aa964e0.html#a90cfd84c4feec568941a46c13aa964e0) | [auxBusID](struct_ak_aux_send_value_a985acf05c92308c7569dd4a91a3e4256.html#a985acf05c92308c7569dd4a91a3e4256) |
|  | Auxiliary bus ID. [更多...](struct_ak_aux_send_value_a985acf05c92308c7569dd4a91a3e4256.html#a985acf05c92308c7569dd4a91a3e4256) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fControlValue](struct_ak_aux_send_value_a1e3fe0e1490d0e15af8a46d8ab4078f4.html#a1e3fe0e1490d0e15af8a46d8ab4078f4) |
|  | |

## 详细描述

Auxiliary bus sends information per game object per given auxiliary bus.

在文件 [AkSoundEngineTypes.h](_ak_sound_engine_types_8h_source.html) 第 [106](_ak_sound_engine_types_8h_source.html#l00106) 行定义.