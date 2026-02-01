# AkCmd_SA_SetGameObjectInRoom

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_game_object_in_room-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetGameObjectInRoom结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___set_game_object_in_room_a07943ede66ed4f74ea574e447b80b61e.html#a07943ede66ed4f74ea574e447b80b61e) |
|  | Game object ID [更多...](struct_ak_cmd___s_a___set_game_object_in_room_a07943ede66ed4f74ea574e447b80b61e.html#a07943ede66ed4f74ea574e447b80b61e) |
|  | |
| [AkRoomID](struct_ak_room_i_d.html) | [roomID](struct_ak_cmd___s_a___set_game_object_in_room_a854fa4226322d824c438b6a27f8fed1f.html#a854fa4226322d824c438b6a27f8fed1f) |
|  | RoomID that was passed to [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html) [更多...](struct_ak_cmd___s_a___set_game_object_in_room_a854fa4226322d824c438b6a27f8fed1f.html#a854fa4226322d824c438b6a27f8fed1f) |
|  | |

## 详细描述

Set the room that the game object is currently located in - usually the result of a containment test performed by the client. The room must have been registered with [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html). Setting the room for a game object provides the basis for the sound propagation service, and also sets which room's reverb aux bus to send to. The sound propagation service traces the path of the sound from the emitter to the listener, and calculates the diffraction as the sound passes through each portal. The portals are used to define the spatial location of the diffracted and reverberated audio.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` or `roomID` are not valid IDs.
- AK\_IDNotFound: Provided `gameObjectID` is not recognized as a registered game object.
- AK\_InsufficientMemory: Not enough memory to complete the operation.

参见
:   - [AkCommand\_SA\_SetGameObjectInRoom](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaac74bf305672b4e89a7a0ce7d6426099)
    - [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html)
    - [AkCmd\_SA\_RemoveRoom](struct_ak_cmd___s_a___remove_room.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1736](_ak_command_types_8h_source.html#l01736) 行定义.