# AkCmd_SA_SetGeometry

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_geometry-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetGeometry结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGeometrySetID](_ak_spatial_audio_types_8h_a4eccc0cc5fbd68160830c3201a8878a5.html#a4eccc0cc5fbd68160830c3201a8878a5) | [geometrySetID](struct_ak_cmd___s_a___set_geometry_a72a55c01087f349f2a41f21f3aae6a8b.html#a72a55c01087f349f2a41f21f3aae6a8b) |
|  | Unique geometry set ID, chosen by client. [更多...](struct_ak_cmd___s_a___set_geometry_a72a55c01087f349f2a41f21f3aae6a8b.html#a72a55c01087f349f2a41f21f3aae6a8b) |
|  | |

## 详细描述

Add or update a set of geometry from the `SpatialAudio` module for geometric reflection and diffraction processing. A geometry set is a logical set of vertices, triangles, and acoustic surfaces, which are referenced by the same `AkGeometrySetID`. The ID (`geometrySetID`) must be unique and is also chosen by the client in a manner similar to `AkGameObjectID's`. It is necessary to create at least one geometry instance for each geometry set that is to be used for diffraction and reflection simulation.

The Sound Engine expects geometry data to be added right after the command. Call AK\_CommandBuffer\_AddGeometry to add geometry data:

```
AkGeometryParams geoParams; // Initialize with valid triangles, vertices, surfaces...
auto cmd = (AkCmd_SA_SetGeometry*)AK_CommandBuffer_Add(buffer, AkCommand_SA_SetGeometry);
cmd->geometrySetID = myID;
AK_CommandBuffer_AddGeometry(buffer, &geoParams);
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `geometrySetID` is invalid, or missing geometry data after the command
- AK\_InsufficientMemory: Not enough memory to complete the operation

参见
:   - [AkGeometryParams](struct_ak_geometry_params.html)
    - [AkCommand\_SA\_SetGeometry](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdacf9e1e3901df98eef024523667c08107)
    - [AkCmd\_SA\_SetGeometryInstance](struct_ak_cmd___s_a___set_geometry_instance.html)
    - [AkCmd\_SA\_RemoveGeometry](struct_ak_cmd___s_a___remove_geometry.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1453](_ak_command_types_8h_source.html#l01453) 行定义.