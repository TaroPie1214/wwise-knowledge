# AkCmd_SA_SetRoom

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_room-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetRoom结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkRoomID](struct_ak_room_i_d.html) | [roomID](struct_ak_cmd___s_a___set_room_a06273d903c3387f942bfd44649b93f8c.html#a06273d903c3387f942bfd44649b93f8c) |
|  | Unique room ID, chosen by the client. [更多...](struct_ak_cmd___s_a___set_room_a06273d903c3387f942bfd44649b93f8c.html#a06273d903c3387f942bfd44649b93f8c) |
|  | |
| struct [AkRoomParams](struct_ak_room_params.html) | [params](struct_ak_cmd___s_a___set_room_a907ce6b39d17effacd962bc2ca77b19a.html#a907ce6b39d17effacd962bc2ca77b19a) |
|  | Parameter for the room. [更多...](struct_ak_cmd___s_a___set_room_a907ce6b39d17effacd962bc2ca77b19a.html#a907ce6b39d17effacd962bc2ca77b19a) |
|  | |

## 详细描述

Add or update a room. Rooms are used to connect portals and define an orientation for oriented reverbs. This function may be called multiple times with the same ID to update the parameters of the room.

|  |  |
| --- | --- |
|  | **警告:** The ID (`roomID`) must be chosen in the same manner as `AkGameObjectID's`, as they are in the same ID-space. The spatial audio lib manages the registration/unregistration of internal game objects for rooms that use these IDs and, therefore, must not collide. Also, the room ID must not be in the reserved range (AkUInt64)(-32) to (AkUInt64)(-2) inclusively. You may, however, explicitly add the default room ID `AK_OUTDOORS_ROOM_ID` (-1) in order to customize its [AkRoomParams](struct_ak_room_params.html "Parameters passed to SetRoom"), to provide a valid auxiliary bus, for example. |

Optionally, you can associate a name to the room for profiling purposes. Call AK\_CommandBuffer\_AddString after adding the command to attach a name to the room:

```
auto cmd = (AkCmd_SA_SetRoom*)AK_CommandBuffer_Add(buffer, AkCommand_SA_SetRoom);
// Fill command...
AK_CommandBuffer_AddString(buffer, "Bedroom 1");
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `roomID` is outside the valid range
- AK\_InsufficientMemory: Not enough memory to complete the operation.

参见
:   - [AkCommand\_SA\_SetRoom](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdabd09c21c56c233f2e066d563ef805e60)
    - [AK\_CommandBuffer\_AddString](_ak_command_buffer_8h_a6b6d59f7fb356dc8f2ed3488e3bf0392.html#a6b6d59f7fb356dc8f2ed3488e3bf0392)
    - [AkRoomID](struct_ak_room_i_d.html)
    - [AkRoomParams](struct_ak_room_params.html)
    - [AkCmd\_SA\_RemoveRoom](struct_ak_cmd___s_a___remove_room.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1530](_ak_command_types_8h_source.html#l01530) 行定义.