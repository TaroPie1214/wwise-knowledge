# AkCmd_SA_SetEarlyReflectionsAuxSend

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_early_reflections_aux_send-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetEarlyReflectionsAuxSend结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___set_early_reflections_aux_send_a74156a51cdded833ad36bcd60c2a5302.html#a74156a51cdded833ad36bcd60c2a5302) |
|  | Game object ID [更多...](struct_ak_cmd___s_a___set_early_reflections_aux_send_a74156a51cdded833ad36bcd60c2a5302.html#a74156a51cdded833ad36bcd60c2a5302) |
|  | |
| [AkAuxBusID](_ak_typedefs_8h_a90cfd84c4feec568941a46c13aa964e0.html#a90cfd84c4feec568941a46c13aa964e0) | [auxBusID](struct_ak_cmd___s_a___set_early_reflections_aux_send_affd7e82369ffc7ae4f09bf6b624bcda8.html#affd7e82369ffc7ae4f09bf6b624bcda8) |
|  | Auxiliary bus ID. Applies only to sounds which have not specified an early reflection bus in the authoring tool. Set `AK_INVALID_AUX_ID` to set only the send volume. [更多...](struct_ak_cmd___s_a___set_early_reflections_aux_send_affd7e82369ffc7ae4f09bf6b624bcda8.html#affd7e82369ffc7ae4f09bf6b624bcda8) |
|  | |

## 详细描述

Set an early reflections auxiliary bus for a particular game object. Geometrical reflection calculation inside spatial audio is enabled for a game object if any sound playing on the game object has a valid early reflections aux bus specified in the authoring tool, or if an aux bus is specified via `AkCmd_SA_SetEarlyReflectionsAuxSend`. The `auxBusID` parameter of [AkCmd\_SA\_SetEarlyReflectionsAuxSend](struct_ak_cmd___s_a___set_early_reflections_aux_send.html) applies to sounds playing on the game object `gameObjectID` which have not specified an early reflection bus in the authoring tool - the parameter specified on individual sounds' reflection bus takes priority over the value passed in to `AkCmd_SA_SetEarlyReflectionsAuxSend`.

|  |  |
| --- | --- |
|  | **备注:** Users may apply this function to avoid duplicating sounds in the Containers hierarchy solely for the sake of specifying a unique early reflection bus, or in any situation where the same sound should be played on different game objects with different early reflection aux buses (the early reflection bus must be left blank in the authoring tool if the user intends to specify it through the API). |

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is invalid.
- AK\_IDNotFound: `gameObjectID` is not a registered game object.

参见
:   - [AkCommand\_SA\_SetEarlyReflectionsAuxSend](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda7d75744918d1479e1daf3e0649307928)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1803](_ak_command_types_8h_source.html#l01803) 行定义.