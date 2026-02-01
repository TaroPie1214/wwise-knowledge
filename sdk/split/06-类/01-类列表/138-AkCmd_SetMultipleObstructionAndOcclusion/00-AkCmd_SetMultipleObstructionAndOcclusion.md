# AkCmd_SetMultipleObstructionAndOcclusion

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_multiple_obstruction_and_occlusion-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetMultipleObstructionAndOcclusion结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [emitterID](struct_ak_cmd___set_multiple_obstruction_and_occlusion_ac22836a19006d174c155b8e94c60d48f.html#ac22836a19006d174c155b8e94c60d48f) |
|  | Emitter Game Object ID [更多...](struct_ak_cmd___set_multiple_obstruction_and_occlusion_ac22836a19006d174c155b8e94c60d48f.html#ac22836a19006d174c155b8e94c60d48f) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [listenerID](struct_ak_cmd___set_multiple_obstruction_and_occlusion_a8d0c8d86f3b0eeefeb759132679ea15b.html#a8d0c8d86f3b0eeefeb759132679ea15b) |
|  | Listener Game Object ID [更多...](struct_ak_cmd___set_multiple_obstruction_and_occlusion_a8d0c8d86f3b0eeefeb759132679ea15b.html#a8d0c8d86f3b0eeefeb759132679ea15b) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numValues](struct_ak_cmd___set_multiple_obstruction_and_occlusion_aac48de3beba7df910f0091ab86cd02f6.html#aac48de3beba7df910f0091ab86cd02f6) |
|  | Number of values [更多...](struct_ak_cmd___set_multiple_obstruction_and_occlusion_aac48de3beba7df910f0091ab86cd02f6.html#aac48de3beba7df910f0091ab86cd02f6) |
|  | |

## 详细描述

Sets a game object's obstruction and occlusion value for objects with multiple positions. This command differs from AkCommand\_SetObjectObstructionAndOcclusion as a list of obstruction/occlusion pair is provided and each obstruction/occlusion pair will affect the corresponding position defined at the same index.

|  |  |
| --- | --- |
|  | **备注:** In the case the number of obstruction/occlusion pairs is smaller than the number of positions, remaining positions' obstruction/occlusion values are set to 0.0. |

The Sound Engine expects an array of `AkObstructionOcclusionValues` objects after the command. The number of items must correspond to the value of `numValues`. For example:

```
AkObstructionOcclusionValues values[2]; // Initialize array as required
auto cmd = (AkCmd_SetMultipleObstructionAndOcclusion*)AK_CommandBuffer_Add(buffer, AkCommand_SetMultipleObstructionAndOcclusion);
cmd->numValues = 2;
AK_CommandBuffer_AddArray(buffer, sizeof(AkObstructionOcclusionValues), cmd->numValues, values);
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `emitterID` is not a valid game object ID, incomplete array after the command, or obstruction/occlusion values are outside the accepted range
- AK\_InsufficientMemory: Not enough memory to complete the operation
- AK\_IDNotFound: `emitterID` is not a registered game object ID.

参见
:   - [AkCommand\_SetMultipleObstructionAndOcclusion](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdadd3a1055f0c89a3c9f1b9a253b162569 "See AkCmd_SetMultipleObstructionAndOcclusion")
    - [AK\_CommandBuffer\_AddArray](_ak_command_buffer_8h_a7512f07e3e8f24cf4ed15bebf3a6392e.html#a7512f07e3e8f24cf4ed15bebf3a6392e)
    - [声障、声笼及 Game-defined Auxiliary Sends](soundengine_obsocc.html)
    - [集成详情——环境和游戏定义的辅助发送](soundengine_environments.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [533](_ak_command_types_8h_source.html#l00533) 行定义.