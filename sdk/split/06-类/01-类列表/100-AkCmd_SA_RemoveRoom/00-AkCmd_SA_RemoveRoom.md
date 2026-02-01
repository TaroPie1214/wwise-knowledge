# AkCmd_SA_RemoveRoom

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___remove_room-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_RemoveRoom结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkRoomID](struct_ak_room_i_d.html) | [roomID](struct_ak_cmd___s_a___remove_room_a36d5146cd4ebdb17baadca6ccdb814c7.html#a36d5146cd4ebdb17baadca6ccdb814c7) |
|  | Room ID that was specified by [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html). [更多...](struct_ak_cmd___s_a___remove_room_a36d5146cd4ebdb17baadca6ccdb814c7.html#a36d5146cd4ebdb17baadca6ccdb814c7) |
|  | |

## 详细描述

Remove a room.

This command can fail for the following reasons:

- AK\_InvalidParameter: `roomID` is outside the valid range
- AK\_IDNotFound: Provided `roomID` is not recognized as a registered portal ID.

参见
:   - [AkCommand\_SA\_RemoveRoom](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdae0c715a7f738173db9f1bcd37527e46f)
    - [AkRoomID](struct_ak_room_i_d.html)
    - [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1546](_ak_command_types_8h_source.html#l01546) 行定义.