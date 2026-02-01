# AkCmd_SA_RemoveReverbZone

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___remove_reverb_zone-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_RemoveReverbZone结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkRoomID](struct_ak_room_i_d.html) | [reverbZoneRoomID](struct_ak_cmd___s_a___remove_reverb_zone_a2f90016e68ce1b81d5dfb9279416b3a9.html#a2f90016e68ce1b81d5dfb9279416b3a9) |
|  | ID of the Room which has been specified as a Reverb Zone. [更多...](struct_ak_cmd___s_a___remove_reverb_zone_a2f90016e68ce1b81d5dfb9279416b3a9.html#a2f90016e68ce1b81d5dfb9279416b3a9) |
|  | |

## 详细描述

Remove a Reverb Zone from its parent. It will no longer be possible for sound to propagate between the two rooms, unless they are explicitly connected with a Portal.

This command can fail for the following reasons:

- AK\_InvalidParameter: `reverbZoneRoomID` is not a valid room ID
- AK\_IDNotFound: Provided `reverbZoneRoomID` is not recognized as a registered room ID.

参见
:   - [AkCommand\_SA\_RemoveReverbZone](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda85cefe1c9b0727657556423a3b0cbde4)
    - [AkCmd\_SA\_SetReverbZone](struct_ak_cmd___s_a___set_reverb_zone.html)
    - [AkCmd\_SA\_RemoveRoom](struct_ak_cmd___s_a___remove_room.html)
    - [AkCmd\_SA\_RemoveReverbZone](struct_ak_cmd___s_a___remove_reverb_zone.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1717](_ak_command_types_8h_source.html#l01717) 行定义.