# AkCmd_SetObjectObstructionAndOcclusion

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_object_obstruction_and_occlusion-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetObjectObstructionAndOcclusion结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [emitterID](struct_ak_cmd___set_object_obstruction_and_occlusion_a2bee06a03558b282823ae1aebdf066b8.html#a2bee06a03558b282823ae1aebdf066b8) |
|  | Emitter Game Object ID [更多...](struct_ak_cmd___set_object_obstruction_and_occlusion_a2bee06a03558b282823ae1aebdf066b8.html#a2bee06a03558b282823ae1aebdf066b8) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [listenerID](struct_ak_cmd___set_object_obstruction_and_occlusion_a0724a568d10f4afac42787e3e7ecc4fb.html#a0724a568d10f4afac42787e3e7ecc4fb) |
|  | Listener Game Object ID [更多...](struct_ak_cmd___set_object_obstruction_and_occlusion_a0724a568d10f4afac42787e3e7ecc4fb.html#a0724a568d10f4afac42787e3e7ecc4fb) |
|  | |
| struct [AkObstructionOcclusionValues](struct_ak_obstruction_occlusion_values.html) | [value](struct_ak_cmd___set_object_obstruction_and_occlusion_abac9ea6b2e5e2476772546733840fe80.html#abac9ea6b2e5e2476772546733840fe80) |
|  | Obstruction and occlusion values [更多...](struct_ak_cmd___set_object_obstruction_and_occlusion_abac9ea6b2e5e2476772546733840fe80.html#abac9ea6b2e5e2476772546733840fe80) |
|  | |

## 详细描述

Sets a game object's obstruction and occlusion levels. If the game object as multiple positions, values are set for all positions. To assign a unique obstruction and occlusion value to each sound position, instead use AkCommand\_SetMultipleObstructionAndOcclusion. This function is used to affect how an object should be heard by a specific listener.

This command can fail for the following reasons:

- AK\_InvalidParameter: `emitterID` is not a valid game object ID or obstruction/occlusion values are outside the accepted range
- AK\_InsufficientMemory: Not enough memory to complete the operation
- AK\_IDNotFound: `emitterID` is not a registered game object ID.

参见
:   - [AkCommand\_SetObjectObstructionAndOcclusion](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdad108c7253238706e2a133e0408237b31 "See AkCmd_SetObjectObstructionAndOcclusion")
    - [声障、声笼及 Game-defined Auxiliary Sends](soundengine_obsocc.html)
    - [集成详情——环境和游戏定义的辅助发送](soundengine_environments.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [502](_ak_command_types_8h_source.html#l00502) 行定义.