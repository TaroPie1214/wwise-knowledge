# AkCmd_ResetRTPC

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___reset_r_t_p_c-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ResetRTPC结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkRtpcID](_ak_typedefs_8h_a77a3b6fec7d9181ef8e5bae2b37b80d0.html#a77a3b6fec7d9181ef8e5bae2b37b80d0) | [rtpcID](struct_ak_cmd___reset_r_t_p_c_ae03889d47e88df6fa3e24f52eaa57015.html#ae03889d47e88df6fa3e24f52eaa57015) |
|  | (optional) Game parameter ID; specify AK\_INVALID\_RTPC\_ID to reset all game parameters of a game object [更多...](struct_ak_cmd___reset_r_t_p_c_ae03889d47e88df6fa3e24f52eaa57015.html#ae03889d47e88df6fa3e24f52eaa57015) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___reset_r_t_p_c_a087c88fcd3b4215da36050e9b4a26833.html#a087c88fcd3b4215da36050e9b4a26833) |
|  | (optional) Game Object ID; specify AK\_INVALID\_GAME\_OBJECT for global scope or if using playingID [更多...](struct_ak_cmd___reset_r_t_p_c_a087c88fcd3b4215da36050e9b4a26833.html#a087c88fcd3b4215da36050e9b4a26833) |
|  | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___reset_r_t_p_c_acc1cc35ccbd91fa75c9bd9a014b7636a.html#acc1cc35ccbd91fa75c9bd9a014b7636a) |
|  | (optional) Playing ID; specify AK\_INVALID\_PLAYING for global scope or if using gameObjectID [更多...](struct_ak_cmd___reset_r_t_p_c_acc1cc35ccbd91fa75c9bd9a014b7636a.html#acc1cc35ccbd91fa75c9bd9a014b7636a) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [transitionTime](struct_ak_cmd___reset_r_t_p_c_aaf63b5a1fffe3696e991ec087fc2e2cf.html#aaf63b5a1fffe3696e991ec087fc2e2cf) |
|  | (optional) Duration during which the game parameter is interpolated towards in\_value, 0 for instant change [更多...](struct_ak_cmd___reset_r_t_p_c_aaf63b5a1fffe3696e991ec087fc2e2cf.html#aaf63b5a1fffe3696e991ec087fc2e2cf) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [fadeCurve](struct_ak_cmd___reset_r_t_p_c_a8c7f4f87473191559a423d08a98f386d.html#a8c7f4f87473191559a423d08a98f386d) |
|  | (optional) Curve type to be used for the game parameter interpolation, see [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) [更多...](struct_ak_cmd___reset_r_t_p_c_a8c7f4f87473191559a423d08a98f386d.html#a8c7f4f87473191559a423d08a98f386d) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [bypassInternalValueInterpolation](struct_ak_cmd___reset_r_t_p_c_abc595d003013b71c98d62aa7d5ed5fe9.html#abc595d003013b71c98d62aa7d5ed5fe9) |
|  | Not 0 if you want to bypass the internal "slew rate" or "over time filtering" specified by the sound designer. This is meant to be used when, for example, loading a level and you don't want the values to interpolate. [更多...](struct_ak_cmd___reset_r_t_p_c_abc595d003013b71c98d62aa7d5ed5fe9.html#abc595d003013b71c98d62aa7d5ed5fe9) |
|  | |

## 详细描述

Resets the value of the game parameter to its default value, as specified in the Wwise project. This command may reset a game parameter to its default value with global scope, game object scope, or playing ID scope. Playing ID scope supersedes both game object scope and global scope, and game object scope supersedes global scope. Game parameter values reset with a global scope are applied to all game objects that were not overridden at the game object scope or playing ID scope. To reset a game parameter value with global scope, `gameObjectID` must be set to `AK_INVALID_GAME_OBJECT` *and* `playingID` must be set to `AK_INVALID_PLAYING_ID`. To reset a game parameter value with object scope, `gameObjectID` must be set to a valid game object ID *and* `playingID` must be set to `AK_INVALID_PLAYING_ID`. Finally, to reset a game parameter value with playing ID scope, both `gameObjectID` *and* `playingID` must be provided. With this command, you may also reset the value of a game parameter over time. To do so, specify a non-zero value for `transitionTime`. At each audio frame, the game parameter value will be updated internally according to the interpolation curve.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` specified and is outside the valid range or `fadeCurve` is not a valid AkCurveInterpolation value.
- AK\_IDNotFound: `gameObjectID` is not a registered game object ID.

参见
:   [AkCommand\_ResetRTPC](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda6d3735e6380fd7a9c984dfd131175740 "See AkCmd_ResetRTPC")

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [265](_ak_command_types_8h_source.html#l00265) 行定义.