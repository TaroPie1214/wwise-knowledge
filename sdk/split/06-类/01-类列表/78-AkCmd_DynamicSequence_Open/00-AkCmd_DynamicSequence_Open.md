# AkCmd_DynamicSequence_Open

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___dynamic_sequence___open-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_DynamicSequence\_Open结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___dynamic_sequence___open_a4136a4b32b062d10dc8575331c68f993.html#a4136a4b32b062d10dc8575331c68f993) |
|  | Unique ID that will be associated with this playback. Use [AK\_SoundEngine\_GeneratePlayingID()](_ak_command_buffer_8h_a4d75a81be7be245c1e49cea34e32bfc3.html#a4d75a81be7be245c1e49cea34e32bfc3) to generate a new unique playing ID. [更多...](struct_ak_cmd___dynamic_sequence___open_a4136a4b32b062d10dc8575331c68f993.html#a4136a4b32b062d10dc8575331c68f993) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___dynamic_sequence___open_abaa1ab91e4d7bdcdca8ce17ec00976b0.html#abaa1ab91e4d7bdcdca8ce17ec00976b0) |
|  | (optional) Associated game object ID [更多...](struct_ak_cmd___dynamic_sequence___open_abaa1ab91e4d7bdcdca8ce17ec00976b0.html#abaa1ab91e4d7bdcdca8ce17ec00976b0) |
|  | |
| [AkDynamicSequenceType\_t](_ak_enums_8h_a3f2b80ecdcdeadbde77431a113bfcbdc.html#a3f2b80ecdcdeadbde77431a113bfcbdc) | [type](struct_ak_cmd___dynamic_sequence___open_a85eab2a6135d43dccc94de0bc9e35950.html#a85eab2a6135d43dccc94de0bc9e35950) |
|  | Type: see [AkDynamicSequenceType](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7b) [更多...](struct_ak_cmd___dynamic_sequence___open_a85eab2a6135d43dccc94de0bc9e35950.html#a85eab2a6135d43dccc94de0bc9e35950) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [flags](struct_ak_cmd___dynamic_sequence___open_a8d615a6bed1c8556df7527e4a240282c.html#a8d615a6bed1c8556df7527e4a240282c) |
|  | Bitmask: see [AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732) [更多...](struct_ak_cmd___dynamic_sequence___open_a8d615a6bed1c8556df7527e4a240282c.html#a8d615a6bed1c8556df7527e4a240282c) |
|  | |
| [AkEventCallbackFunc](_ak_callback_types_8h_a276c9e8420fee177debd0838b664d7c7.html#a276c9e8420fee177debd0838b664d7c7) | [callback](struct_ak_cmd___dynamic_sequence___open_a70fe41a9992494eda3ac16d46f7358de.html#a70fe41a9992494eda3ac16d46f7358de) |
|  | Callback function [更多...](struct_ak_cmd___dynamic_sequence___open_a70fe41a9992494eda3ac16d46f7358de.html#a70fe41a9992494eda3ac16d46f7358de) |
|  | |
| void \* | [callbackCookie](struct_ak_cmd___dynamic_sequence___open_afa21e4ee8df9e591576c5fa21c999329.html#afa21e4ee8df9e591576c5fa21c999329) |
|  | Callback cookie [更多...](struct_ak_cmd___dynamic_sequence___open_afa21e4ee8df9e591576c5fa21c999329.html#afa21e4ee8df9e591576c5fa21c999329) |
|  | |

## 详细描述

Open a new Dynamic Sequence.

If `AK_DynamicSequenceSelect` bit is set in `flags`, the dynamic sequence uses the callback for determining the next item to play. If this bit is not set, then the dynamic sequence uses the Playlist to determine the next item to play (C++-only API).

This command can fail for the following reasons:

- AK\_InvalidParameter: `playingID` is an invalid ID or `type` is not a valid dynamic sequence type.
- AK\_InsufficientMemory: Not enough memory to process the command.
- AK\_IDNotFound: `gameObjectID` was specified but is not registered.
- AK\_ResourceInUse: `playingID` was already used for a previous entry.

参见
:   - [AkCommand\_DynamicSequence\_Open](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda716005c85cf0d59989839e210ac0accc "See AkCmd_DynamicSequence_Open")
    - [AK::SoundEngine::DynamicSequence::Open](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [797](_ak_command_types_8h_source.html#l00797) 行定义.