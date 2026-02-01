# AkReflectGameData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_reflect_game_data-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[Public 属性](#pub-attribs)

AkReflectGameData结构体 参考

Data structure sent by the game to an instance of the Reflect plug-in.
[更多...](struct_ak_reflect_game_data.html#details)

`#include <AkReflectGameData.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkReflectGameData](struct_ak_reflect_game_data_a44db375c81f806cd1c93a91ba2da885a.html#a44db375c81f806cd1c93a91ba2da885a) () |
|  | Default constructor. [更多...](struct_ak_reflect_game_data_a44db375c81f806cd1c93a91ba2da885a.html#a44db375c81f806cd1c93a91ba2da885a) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetSize](struct_ak_reflect_game_data_a9092162fa11340914f05afa50bcc11b4.html#a9092162fa11340914f05afa50bcc11b4) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumSources) |
|  | Helper function for computing the size required to allocate the [AkReflectGameData](struct_ak_reflect_game_data.html "Data structure sent by the game to an instance of the Reflect plug-in.") structure. [更多...](struct_ak_reflect_game_data_a9092162fa11340914f05afa50bcc11b4.html#a9092162fa11340914f05afa50bcc11b4) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [listenerID](struct_ak_reflect_game_data_ad4f628915a1e7854375a7311a5981ee1.html#ad4f628915a1e7854375a7311a5981ee1) |
|  | ID of the listener used to compute spatialization and distance evaluation from within the targeted Reflect plug-in instance. It needs to be one of the listeners that are listening to the game object associated with the targeted plug-in instance. See [AK::SoundEngine::SetListeners](namespace_a_k_1_1_sound_engine_a2f85a55c38afa2e0dbc6172a7bec91d1.html#a2f85a55c38afa2e0dbc6172a7bec91d1) and [AK::SoundEngine::SetGameObjectAuxSendValues](namespace_a_k_1_1_sound_engine_af960fca0239e219b9d08c2659fe9e5d4.html#af960fca0239e219b9d08c2659fe9e5d4). [更多...](struct_ak_reflect_game_data_ad4f628915a1e7854375a7311a5981ee1.html#ad4f628915a1e7854375a7311a5981ee1) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumImageSources](struct_ak_reflect_game_data_a4863372f7461accb18feb4df34dc19b2.html#a4863372f7461accb18feb4df34dc19b2) |
|  | Number of image sources passed in the variable array, below. [更多...](struct_ak_reflect_game_data_a4863372f7461accb18feb4df34dc19b2.html#a4863372f7461accb18feb4df34dc19b2) |
|  | |
| [AkReflectImageSource](struct_ak_reflect_image_source.html) | [arSources](struct_ak_reflect_game_data_a1f0f7292d2c7d392a57f42ed06b8376e.html#a1f0f7292d2c7d392a57f42ed06b8376e) [1] |
|  | Variable array of image sources. You should allocate storage for the structure by calling [AkReflectGameData::GetSize()](struct_ak_reflect_game_data_a9092162fa11340914f05afa50bcc11b4.html#a9092162fa11340914f05afa50bcc11b4 "Helper function for computing the size required to allocate the AkReflectGameData structure.") with the desired number of sources. [更多...](struct_ak_reflect_game_data_a1f0f7292d2c7d392a57f42ed06b8376e.html#a1f0f7292d2c7d392a57f42ed06b8376e) |
|  | |

## 详细描述

Data structure sent by the game to an instance of the Reflect plug-in.

在文件 [AkReflectGameData.h](_ak_reflect_game_data_8h_source.html) 第 [62](_ak_reflect_game_data_8h_source.html#l00062) 行定义.