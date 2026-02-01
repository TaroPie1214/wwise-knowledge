# AkCmd_SetGameObjectAuxSendValues

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_game_object_aux_send_values-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetGameObjectAuxSendValues结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___set_game_object_aux_send_values_adff3e93f84a9c1605c7804c64fb5faf8.html#adff3e93f84a9c1605c7804c64fb5faf8) |
|  | Game Object ID. [更多...](struct_ak_cmd___set_game_object_aux_send_values_adff3e93f84a9c1605c7804c64fb5faf8.html#adff3e93f84a9c1605c7804c64fb5faf8) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numValues](struct_ak_cmd___set_game_object_aux_send_values_a5b8f021cf6cf9691182e10f46caf6dde.html#a5b8f021cf6cf9691182e10f46caf6dde) |
|  | Number of values. [更多...](struct_ak_cmd___set_game_object_aux_send_values_a5b8f021cf6cf9691182e10f46caf6dde.html#a5b8f021cf6cf9691182e10f46caf6dde) |
|  | |

## 详细描述

Sets the Auxiliary Busses to route the specified game object. To clear the game object's auxiliary sends, `numValues` must be 0.

The Sound Engine expects an array of `AkAuxSendValue` objects after the command. The number of items must correspond to the number of channels in `channelConfig`. For example:

```
AkAuxSendValue values[2]; // Initialize array as required
auto cmd = (AkCmd_SetGameObjectAuxSendValues*)AK_CommandBuffer_Add(buffer, AkCommand_SetGameObjectAuxSendValues);
cmd->numValues = 2;
AK_CommandBuffer_AddArray(buffer, sizeof(AkAuxSendValue), cmd->numValues, values);
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is outside the valid range, or incomplete array after the command.
- AK\_IDNotFound: `gameObjectID` is not a registered game object ID.

参见
:   - [AkCommand\_SetGameObjectAuxSendValues](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf61a2cd81ebb15c5cbaaeef537b500e2 "See AkCmd_SetGameObjectAuxSendValues")
    - [AK\_CommandBuffer\_AddArray](_ak_command_buffer_8h_a7512f07e3e8f24cf4ed15bebf3a6392e.html#a7512f07e3e8f24cf4ed15bebf3a6392e)
    - [集成详情——环境和游戏定义的辅助发送](soundengine_environments.html)
    - [动态发送到辅助总线。](soundengine_environments.html#soundengine_environments_dynamic_aux_bus_routing)
    - [使用 ID 或字符串（Unicode 或 ANSI）](soundengine_environments.html#soundengine_environments_id_vs_string)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [444](_ak_command_types_8h_source.html#l00444) 行定义.