# AkCmd_UnregisterGameObject

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___unregister_game_object-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_UnregisterGameObject结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___unregister_game_object_a482270577cd32760caf19a0ee1dec8ca.html#a482270577cd32760caf19a0ee1dec8ca) |
|  | ID of the game object to be unregistered. Valid range is [0 to 0xFFFFFFFFFFFFFFDF]. Use AK\_INVALID\_GAME\_OBJECT to unregister all game objects. [更多...](struct_ak_cmd___unregister_game_object_a482270577cd32760caf19a0ee1dec8ca.html#a482270577cd32760caf19a0ee1dec8ca) |
|  | |

## 详细描述

Unregisters the game object ID. No-op if the game object ID is not found. AK\_INVALID\_GAME\_OBJECT can be specified to unregister all game objects using a single command.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is outside the valid range.

参见
:   [AkCommand\_UnregisterGameObject](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda90baf8a9598a8ec1b5935193d903ff7d "See AkCmd_UnregisterGameObject")

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [199](_ak_command_types_8h_source.html#l00199) 行定义.