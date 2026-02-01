# AkCmd_SA_RemoveGeometry

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___remove_geometry-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_RemoveGeometry结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGeometrySetID](_ak_spatial_audio_types_8h_a4eccc0cc5fbd68160830c3201a8878a5.html#a4eccc0cc5fbd68160830c3201a8878a5) | [geometrySetID](struct_ak_cmd___s_a___remove_geometry_aee87da85d240f1f346e9f3928883af80.html#aee87da85d240f1f346e9f3928883af80) |
|  | ID of geometry set to be removed. [更多...](struct_ak_cmd___s_a___remove_geometry_aee87da85d240f1f346e9f3928883af80.html#aee87da85d240f1f346e9f3928883af80) |
|  | |

## 详细描述

Remove a set of geometry to the SpatialAudio API. Calling `AK::SpatialAudio::RemoveGeometry` will remove all instances of the geometry from the scene.

This command can fail for the following reasons:

- AK\_InvalidParameter: `geometrySetID` is invalid
- AK\_IDNotFound: The ID passed does not correspond to a registered geometry set ID.

参见
:   - [AkCommand\_SA\_RemoveGeometry](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaa1851ceec5647ed78e07ffc63b039ca7)
    - [AkCmd\_SA\_SetGeometry](struct_ak_cmd___s_a___set_geometry.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1468](_ak_command_types_8h_source.html#l01468) 行定义.