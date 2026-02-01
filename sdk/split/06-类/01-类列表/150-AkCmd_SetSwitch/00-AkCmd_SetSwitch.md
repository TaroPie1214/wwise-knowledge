# AkCmd_SetSwitch

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_switch-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetSwitch结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkSwitchGroupID](_ak_typedefs_8h_a2b8749ca2320f1ee1c4ebe6b7cf1db26.html#a2b8749ca2320f1ee1c4ebe6b7cf1db26) | [switchGroupID](struct_ak_cmd___set_switch_a2de494a018264b3140b0bfd22ebce1e9.html#a2de494a018264b3140b0bfd22ebce1e9) |
|  | ID of the Switch Group [更多...](struct_ak_cmd___set_switch_a2de494a018264b3140b0bfd22ebce1e9.html#a2de494a018264b3140b0bfd22ebce1e9) |
|  | |
| [AkSwitchStateID](_ak_typedefs_8h_abcf085b986c625421604d4fc0acd7f1e.html#abcf085b986c625421604d4fc0acd7f1e) | [switchID](struct_ak_cmd___set_switch_ab75b8c09e8c49ba64d8752bbba4c21b3.html#ab75b8c09e8c49ba64d8752bbba4c21b3) |
|  | ID of the Switch [更多...](struct_ak_cmd___set_switch_ab75b8c09e8c49ba64d8752bbba4c21b3.html#ab75b8c09e8c49ba64d8752bbba4c21b3) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___set_switch_a6ea5136ade5294b9e607457f282cd7b9.html#a6ea5136ade5294b9e607457f282cd7b9) |
|  | Associated game object ID. Must be specified. [更多...](struct_ak_cmd___set_switch_a6ea5136ade5294b9e607457f282cd7b9.html#a6ea5136ade5294b9e607457f282cd7b9) |
|  | |

## 详细描述

Sets the State of a Switch Group for a particular game object.

This command can fail for the following reason:

- AK\_InvalidParameter: `switchGroupID` is not valid or `gameObjectID` is not valid
- AK\_IDNotFound: `gameObjectID` is not a registered game object

参见
:   - [集成详情——切换开关](soundengine_switch.html)
    - [AkCommand\_SetSwitch](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda91fc7767a8843230844ea1945fab2ae2 "See AkCmd_SetSwitch")
    - `AK::SoundEngine::SetSwitch()`

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [700](_ak_command_types_8h_source.html#l00700) 行定义.