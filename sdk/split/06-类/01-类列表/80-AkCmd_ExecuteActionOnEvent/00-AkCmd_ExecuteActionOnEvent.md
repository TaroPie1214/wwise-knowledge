# AkCmd_ExecuteActionOnEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___execute_action_on_event-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ExecuteActionOnEvent结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [eventID](struct_ak_cmd___execute_action_on_event_ac1a0850e3ba7fd87b57ba70ffb1ab2b3.html#ac1a0850e3ba7fd87b57ba70ffb1ab2b3) |
|  | ID of event [更多...](struct_ak_cmd___execute_action_on_event_ac1a0850e3ba7fd87b57ba70ffb1ab2b3.html#ac1a0850e3ba7fd87b57ba70ffb1ab2b3) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___execute_action_on_event_a170a9cdd8aa96c2653fb4c6c6d88be53.html#a170a9cdd8aa96c2653fb4c6c6d88be53) |
|  | (optional) Game Object ID (can be invalid) [更多...](struct_ak_cmd___execute_action_on_event_a170a9cdd8aa96c2653fb4c6c6d88be53.html#a170a9cdd8aa96c2653fb4c6c6d88be53) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [transitionTime](struct_ak_cmd___execute_action_on_event_aa63688df2a9b15b4cd4de23ce32d34e7.html#aa63688df2a9b15b4cd4de23ce32d34e7) |
|  | (optional) Duration of transition in milliseconds [更多...](struct_ak_cmd___execute_action_on_event_aa63688df2a9b15b4cd4de23ce32d34e7.html#aa63688df2a9b15b4cd4de23ce32d34e7) |
|  | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___execute_action_on_event_aad1b90325a2b4f889b2e821bf4ac5855.html#aad1b90325a2b4f889b2e821bf4ac5855) |
|  | (optional) Limit scope to specified playing ID. [更多...](struct_ak_cmd___execute_action_on_event_aad1b90325a2b4f889b2e821bf4ac5855.html#aad1b90325a2b4f889b2e821bf4ac5855) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [fadeCurve](struct_ak_cmd___execute_action_on_event_a8bf1021c4962eac9d6e4825930c1f3fc.html#a8bf1021c4962eac9d6e4825930c1f3fc) |
|  | (optional) Curve type to be used for the game parameter interpolation, see [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) [更多...](struct_ak_cmd___execute_action_on_event_a8bf1021c4962eac9d6e4825930c1f3fc.html#a8bf1021c4962eac9d6e4825930c1f3fc) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [actionType](struct_ak_cmd___execute_action_on_event_a7be1ea4003173373ab3c2ee38a8c885c.html#a7be1ea4003173373ab3c2ee38a8c885c) |
|  | See [AkActionOnEventType](_ak_enums_8h_a536475347778ba280b5fa1a605390989.html#a536475347778ba280b5fa1a605390989) [更多...](struct_ak_cmd___execute_action_on_event_a7be1ea4003173373ab3c2ee38a8c885c.html#a7be1ea4003173373ab3c2ee38a8c885c) |
|  | |

## 详细描述

Executes an action on all nodes that are referenced in the specified event in an action of type play.

This command can fail for the following reasons:

- AK\_InvalidParameter: `eventID` is invalid, `actionType` is not a valid action or `fadeCurve` is not a valid AkCurveInterpolation value.
- AK\_IDNotFound: Event was not found or `gameObjectID` is specified but not a registered game object.

参见
:   - `AkActionOnEventType`
    - `AkCommand_ExecuteActionOnEvent`

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [586](_ak_command_types_8h_source.html#l00586) 行定义.