# AkCmd_RegisterGameObject

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___register_game_object-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_RegisterGameObject结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___register_game_object_a26cf8b895f9d1edfd3151b5455dc54e5.html#a26cf8b895f9d1edfd3151b5455dc54e5) |
|  | ID of the game object to be registered. Valid range is [0 to 0xFFFFFFFFFFFFFFDF]. [更多...](struct_ak_cmd___register_game_object_a26cf8b895f9d1edfd3151b5455dc54e5.html#a26cf8b895f9d1edfd3151b5455dc54e5) |
|  | |

## 详细描述

Registers a game object ID.

Optionally, you can associate a name to the game object for profiling purposes. Call AK\_CommandBuffer\_AddString after adding the command to attach a name to the game object:

```
auto cmd = (AkCmd_RegisterGameObject*)AK_CommandBuffer_Add(buffer, AkCommand_RegisterGameObject);
cmd->gameObjectID = 100;
AK_CommandBuffer_AddString(buffer, "Player Emitter");
```

If the ID was already registered, its name is updated.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is outside the valid range.
- AK\_InsufficientMemory: Game object could not be registered due to a memory allocation failure

参见
:   [AkCommand\_RegisterGameObject](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdafa6120328cdb73a0745a5777863dc0d4 "See AkCmd_RegisterGameObject")

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [187](_ak_command_types_8h_source.html#l00187) 行定义.