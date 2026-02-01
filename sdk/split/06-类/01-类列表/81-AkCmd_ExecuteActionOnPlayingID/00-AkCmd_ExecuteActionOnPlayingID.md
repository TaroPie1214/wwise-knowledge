# AkCmd_ExecuteActionOnPlayingID

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___execute_action_on_playing_i_d-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ExecuteActionOnPlayingID结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [actionType](struct_ak_cmd___execute_action_on_playing_i_d_af8e44cb16ad2a5b9f21f9dbea0036f56.html#af8e44cb16ad2a5b9f21f9dbea0036f56) |
|  | See [AkActionOnEventType](_ak_enums_8h_a536475347778ba280b5fa1a605390989.html#a536475347778ba280b5fa1a605390989) [更多...](struct_ak_cmd___execute_action_on_playing_i_d_af8e44cb16ad2a5b9f21f9dbea0036f56.html#af8e44cb16ad2a5b9f21f9dbea0036f56) |
|  | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___execute_action_on_playing_i_d_afec00e1451c227428ce5269a9ca51d4c.html#afec00e1451c227428ce5269a9ca51d4c) |
|  | Playing ID (must be the playing ID for a previously-posted event) [更多...](struct_ak_cmd___execute_action_on_playing_i_d_afec00e1451c227428ce5269a9ca51d4c.html#afec00e1451c227428ce5269a9ca51d4c) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [transitionTime](struct_ak_cmd___execute_action_on_playing_i_d_a3e4741c33210e5932e545120c0e51fc9.html#a3e4741c33210e5932e545120c0e51fc9) |
|  | (optional) Duration of transition in milliseconds [更多...](struct_ak_cmd___execute_action_on_playing_i_d_a3e4741c33210e5932e545120c0e51fc9.html#a3e4741c33210e5932e545120c0e51fc9) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [fadeCurve](struct_ak_cmd___execute_action_on_playing_i_d_a6fc7e9382b46aba1a7cb50e2fc0fc2b4.html#a6fc7e9382b46aba1a7cb50e2fc0fc2b4) |
|  | (optional) Curve type to be used for the game parameter interpolation, see [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) [更多...](struct_ak_cmd___execute_action_on_playing_i_d_a6fc7e9382b46aba1a7cb50e2fc0fc2b4.html#a6fc7e9382b46aba1a7cb50e2fc0fc2b4) |
|  | |

## 详细描述

Executes an Action on the content associated to the specified playing ID.

This command can fail for the following reasons:

- AK\_InvalidParameter: `playingID`, `actionType` or `fadeCurve` is invalid.

参见
:   - `AkActionOnEventType`
    - `AkCommand_ExecuteActionOnPlayingID`

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [604](_ak_command_types_8h_source.html#l00604) 行定义.