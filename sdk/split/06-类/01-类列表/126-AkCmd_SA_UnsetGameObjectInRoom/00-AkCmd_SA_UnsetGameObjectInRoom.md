# AkCmd_SA_UnsetGameObjectInRoom

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___unset_game_object_in_room-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_UnsetGameObjectInRoom结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___unset_game_object_in_room_a9405074ea7fc5b5db5bf460e28a9a073.html#a9405074ea7fc5b5db5bf460e28a9a073) |
|  | Game object ID [更多...](struct_ak_cmd___s_a___unset_game_object_in_room_a9405074ea7fc5b5db5bf460e28a9a073.html#a9405074ea7fc5b5db5bf460e28a9a073) |
|  | |

## 详细描述

Unset the room that the game object is currently located in. When a game object has not been explicitly assigned to a room with [AkCmd\_SA\_SetGameObjectInRoom](struct_ak_cmd___s_a___set_game_object_in_room.html), the room is automatically computed.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is not valid.
- AK\_IDNotFound: Provided `gameObjectID` is not recognized as a registered game object.
- AK\_InsufficientMemory: Not enough memory to complete the operation.

参见
:   - [AkCommand\_SA\_UnsetGameObjectInRoom](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdad33ecf98c98456b2f85a0080ad816aa8)
    - [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html)
    - [AkCmd\_SA\_RemoveRoom](struct_ak_cmd___s_a___remove_room.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1754](_ak_command_types_8h_source.html#l01754) 行定义.