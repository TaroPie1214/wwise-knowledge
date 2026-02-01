# AkCmd_SetPosition

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_position-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetPosition结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___set_position_a1f4b90e273800cf602ad0bd814f06fbc.html#a1f4b90e273800cf602ad0bd814f06fbc) |
|  | Game Object ID [更多...](struct_ak_cmd___set_position_a1f4b90e273800cf602ad0bd814f06fbc.html#a1f4b90e273800cf602ad0bd814f06fbc) |
|  | |
| struct [AkWorldTransform](struct_ak_world_transform.html) | [position](struct_ak_cmd___set_position_a98b1a31b642e1f523e0ce0b3ae643ff3.html#a98b1a31b642e1f523e0ce0b3ae643ff3) |
|  | Game object position [更多...](struct_ak_cmd___set_position_a98b1a31b642e1f523e0ce0b3ae643ff3.html#a98b1a31b642e1f523e0ce0b3ae643ff3) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [flags](struct_ak_cmd___set_position_acc877e7e7c9563815c3cd36e5e06f5dd.html#acc877e7e7c9563815c3cd36e5e06f5dd) |
|  | See [AkSetPositionFlags](_ak_enums_8h_aaafe24aa1ed71ba1433087d2f7018087.html#aaafe24aa1ed71ba1433087d2f7018087) [更多...](struct_ak_cmd___set_position_acc877e7e7c9563815c3cd36e5e06f5dd.html#acc877e7e7c9563815c3cd36e5e06f5dd) |
|  | |

## 详细描述

Sets the position of a game object.

警告
:   The object's orientation vectors (position.orientationFront and position.orientationTop) must be normalized.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is outside the valid range, or position is not a valid transform.
- AK\_IDNotFound: `gameObjectID` is not a registered game object ID.

参见
:   - [AkCommand\_SetPosition](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdabd296114ddc48a2c39a7554dc94ae9cc "See AkCmd_SetPosition")
    - [集成详情——3D 位置](soundengine_3dpositions.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [285](_ak_command_types_8h_source.html#l00285) 行定义.