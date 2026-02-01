# AkCmd_SetMultiplePositions

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_multiple_positions-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetMultiplePositions结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___set_multiple_positions_a57781856ff48fbbb8049356ce7c9e78a.html#a57781856ff48fbbb8049356ce7c9e78a) |
|  | Game Object ID [更多...](struct_ak_cmd___set_multiple_positions_a57781856ff48fbbb8049356ce7c9e78a.html#a57781856ff48fbbb8049356ce7c9e78a) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [flags](struct_ak_cmd___set_multiple_positions_a7590147529ce0f7baca55374ccf1fb44.html#a7590147529ce0f7baca55374ccf1fb44) |
|  | See [AkSetPositionFlags](_ak_enums_8h_aaafe24aa1ed71ba1433087d2f7018087.html#aaafe24aa1ed71ba1433087d2f7018087) [更多...](struct_ak_cmd___set_multiple_positions_a7590147529ce0f7baca55374ccf1fb44.html#a7590147529ce0f7baca55374ccf1fb44) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [multiPositionType](struct_ak_cmd___set_multiple_positions_a0eaa1c8adb80d26de4d64e447f973869.html#a0eaa1c8adb80d26de4d64e447f973869) |
|  | See [AkMultiPositionType](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1) [更多...](struct_ak_cmd___set_multiple_positions_a0eaa1c8adb80d26de4d64e447f973869.html#a0eaa1c8adb80d26de4d64e447f973869) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numPositions](struct_ak_cmd___set_multiple_positions_ad6d79211ad83babd3bec331564f2f63a.html#ad6d79211ad83babd3bec331564f2f63a) |
|  | Number of game positions [更多...](struct_ak_cmd___set_multiple_positions_ad6d79211ad83babd3bec331564f2f63a.html#ad6d79211ad83babd3bec331564f2f63a) |
|  | |

## 详细描述

Sets multiple positions to a single game object.

Setting multiple positions on a single game object is a way to simulate multiple emission sources while using the resources of only one voice. This can be used to simulate wall openings, area sounds, or multiple objects emitting the same sound in the same area.

|  |  |
| --- | --- |
|  | **备注:**  - Using this command with only one position is the same as using AkCommand\_SetPosition. - If a sound has diffraction enabled, it is treated as AkMultiPositionType\_MultiDirections. AkMultiPositionType\_MultiSources is not supported in this case. |

The Sound Engine expects an array of `AkChannelEmitter` objects after the command. For example:

```
auto cmd = (AkCmd_SetMultiplePositions*)AK_CommandBuffer_Add(buffer, AkCommand_SetMultiplePositions);
// Fill out the command...
cmd->numPositions = myPositions.size();
AK_CommandBuffer_AddArray(buffer, sizeof(AkChannelEmitter), myPositions.size(), myPositions.data());
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is outside the valid range, or `flags` are invalid, no positions were added after the command, or at least one position in the array is invalid
- AK\_IDNotFound: `gameObjectID` is not a registered game object ID.

参见
:   - [AkCommand\_SetMultiplePositions](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda5c97cb38cc9ea4849a512bfe412ffdf5 "See AkCmd_SetMultiplePositions")
    - [AK\_CommandBuffer\_AddArray](_ak_command_buffer_8h_a7512f07e3e8f24cf4ed15bebf3a6392e.html#a7512f07e3e8f24cf4ed15bebf3a6392e)
    - [集成详情——3D 位置](soundengine_3dpositions.html)
    - [为单个游戏对象设置多个位置](soundengine_3dpositions.html#soundengine_3dpositions_multiplepos)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [317](_ak_command_types_8h_source.html#l00317) 行定义.