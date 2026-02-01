# AkCmd_SetDistanceProbe

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_distance_probe-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetDistanceProbe结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___set_distance_probe_a27c16704fc74b5fe92b0f0e84478de43.html#a27c16704fc74b5fe92b0f0e84478de43) |
|  | Game Object ID [更多...](struct_ak_cmd___set_distance_probe_a27c16704fc74b5fe92b0f0e84478de43.html#a27c16704fc74b5fe92b0f0e84478de43) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [distanceProbeID](struct_ak_cmd___set_distance_probe_ab668f5a6252f61c6ff3f49a356f33d94.html#ab668f5a6252f61c6ff3f49a356f33d94) |
|  | Probe Game Object ID [更多...](struct_ak_cmd___set_distance_probe_ab668f5a6252f61c6ff3f49a356f33d94.html#ab668f5a6252f61c6ff3f49a356f33d94) |
|  | |

## 详细描述

Use the position of a separate game object for distance calculations for a specified listener. When this command is executed, Wwise calculates distance attenuation and filtering based on the distance between the distance probe Game Object (`distanceProbeID`) and the emitter Game Object's position. In third-person perspective applications, the distance probe Game Object may be set to the player character's position, and the listener Game Object's position to that of the camera. In this scenario, attenuation is based on the distance between the character and the sound, whereas panning, spatialization, and spread and focus calculations are base on the camera. Both Game Objects, `gameObjectID` and `distanceProbeID` must have been previously registered. To clear the distance probe, and revert to using the listener position for distance calculations, set `distanceProbeID` to `AK_INVALID_GAME_OBJECT`.

|  |  |
| --- | --- |
|  | **备注:** If the distance probe Game Object is assigned multiple positions, then the first position is used for distance calculations by the listener. |

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is not a valid game object ID.
- AK\_IDNotFound: `gameObjectID` is not a registered game object or `distanceProbeID` is specified and not a registered game object.
- AK\_InsufficientMemory: Not enough memory to complete the operation.

参见
:   [AkCommand\_SetDistanceProbe](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda2a961fd1d14bca560cbf82c84a95a0b3 "See AkCmd_SetDistanceProbe")

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [558](_ak_command_types_8h_source.html#l00558) 行定义.