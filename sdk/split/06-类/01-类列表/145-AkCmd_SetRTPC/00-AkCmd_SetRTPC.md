# AkCmd_SetRTPC

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_r_t_p_c-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetRTPC结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkRtpcID](_ak_typedefs_8h_a77a3b6fec7d9181ef8e5bae2b37b80d0.html#a77a3b6fec7d9181ef8e5bae2b37b80d0) | [rtpcID](struct_ak_cmd___set_r_t_p_c_a71e3883d6dfdbf8479dbe4601e4858c3.html#a71e3883d6dfdbf8479dbe4601e4858c3) |
|  | Game parameter ID [更多...](struct_ak_cmd___set_r_t_p_c_a71e3883d6dfdbf8479dbe4601e4858c3.html#a71e3883d6dfdbf8479dbe4601e4858c3) |
|  | |
| [AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140) | [rtpcValue](struct_ak_cmd___set_r_t_p_c_a1675d3bcf513f2adb6a75f79f74dec15.html#a1675d3bcf513f2adb6a75f79f74dec15) |
|  | Value to set [更多...](struct_ak_cmd___set_r_t_p_c_a1675d3bcf513f2adb6a75f79f74dec15.html#a1675d3bcf513f2adb6a75f79f74dec15) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___set_r_t_p_c_ac60a5a93956f8c25d8df7b93f53f21ee.html#ac60a5a93956f8c25d8df7b93f53f21ee) |
|  | (optional) Game Object ID; specify AK\_INVALID\_GAME\_OBJECT for global scope or if using playingID [更多...](struct_ak_cmd___set_r_t_p_c_ac60a5a93956f8c25d8df7b93f53f21ee.html#ac60a5a93956f8c25d8df7b93f53f21ee) |
|  | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___set_r_t_p_c_ae48a267c5cb6554add7cf65a5fab5821.html#ae48a267c5cb6554add7cf65a5fab5821) |
|  | (optional) Playing ID; specify AK\_INVALID\_PLAYING for global scope or if using gameObjectID [更多...](struct_ak_cmd___set_r_t_p_c_ae48a267c5cb6554add7cf65a5fab5821.html#ae48a267c5cb6554add7cf65a5fab5821) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [transitionTime](struct_ak_cmd___set_r_t_p_c_ac2f730124467eefcfcb7235329694118.html#ac2f730124467eefcfcb7235329694118) |
|  | (optional) Duration during which the game parameter is interpolated towards in\_value, 0 for instant change [更多...](struct_ak_cmd___set_r_t_p_c_ac2f730124467eefcfcb7235329694118.html#ac2f730124467eefcfcb7235329694118) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [fadeCurve](struct_ak_cmd___set_r_t_p_c_ab2f0f52a4c5f6c4e35723f2497473965.html#ab2f0f52a4c5f6c4e35723f2497473965) |
|  | (optional) Curve type to be used for the game parameter interpolation, see [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) [更多...](struct_ak_cmd___set_r_t_p_c_ab2f0f52a4c5f6c4e35723f2497473965.html#ab2f0f52a4c5f6c4e35723f2497473965) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [bypassInternalValueInterpolation](struct_ak_cmd___set_r_t_p_c_af3eff3bce584957a4a7128b9620a4bce.html#af3eff3bce584957a4a7128b9620a4bce) |
|  | Not 0 if you want to bypass the internal "slew rate" or "over time filtering" specified by the sound designer. This is meant to be used when, for example, loading a level and you don't want the values to interpolate. [更多...](struct_ak_cmd___set_r_t_p_c_af3eff3bce584957a4a7128b9620a4bce.html#af3eff3bce584957a4a7128b9620a4bce) |
|  | |

## 详细描述

Sets the value of a real-time parameter control. This command may set a game parameter value with global scope, game object scope, or playing ID scope. Playing ID scope supersedes both game object scope and global scope, and game object scope supersedes global scope. (Once a value is set for a specific playing ID, it will not be affected by changes at the game object scope or global scope. Similarly, a value set at the game object scope will not be affected by a global scope change.) Game parameter values set with a global scope are applied to all game objects that not yet registered, or already registered but not overridden with a value with game object or playing id scope. To set a game parameter value with global scope, `gameObjectID` must be set to `AK_INVALID_GAME_OBJECT` *and* `playingID` must be set to `AK_INVALID_PLAYING_ID`. To set a game parameter value with object scope, `gameObjectID` must be set to a valid game object ID *and* `playingID` must be set to `AK_INVALID_PLAYING_ID`. Finally, to set a game parameter value with playing ID scope, both `gameObjectID` *and* `playingID` must be provided. With this command, you may also change the value of a game parameter over time. To do so, specify a non-zero value for `transitionTime`. At each audio frame, the game parameter value will be updated internally according to the interpolation curve.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` specified and is outside the valid range or `fadeCurve` is not a valid AkCurveInterpolation value.
- AK\_IDNotFound: `gameObjectID` is not a registered game object ID.

参见
:   [AkCommand\_SetRTPC](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda95aa5709b8fff06b947d3eda020b1189 "See AkCmd_SetRTPC")

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [236](_ak_command_types_8h_source.html#l00236) 行定义.