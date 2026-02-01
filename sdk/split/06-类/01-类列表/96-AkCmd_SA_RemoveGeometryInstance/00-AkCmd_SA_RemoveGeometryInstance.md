# AkCmd_SA_RemoveGeometryInstance

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___remove_geometry_instance-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_RemoveGeometryInstance结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGeometryInstanceID](_ak_spatial_audio_types_8h_a825e3949bdcda8b78d677b95b60ca2f9.html#a825e3949bdcda8b78d677b95b60ca2f9) | [geometryInstanceID](struct_ak_cmd___s_a___remove_geometry_instance_a4f754e33de4d58b7bfebf55ed77ccd05.html#a4f754e33de4d58b7bfebf55ed77ccd05) |
|  | ID of geometry set instance to be removed. [更多...](struct_ak_cmd___s_a___remove_geometry_instance_a4f754e33de4d58b7bfebf55ed77ccd05.html#a4f754e33de4d58b7bfebf55ed77ccd05) |
|  | |

## 详细描述

Remove a geometry instance from the SpatialAudio API.

This command can fail for the following reasons:

- AK\_InvalidParameter: `geometryInstanceID` is not valid.
- AK\_IDNotFound: `geometryInstanceID` does not refer to a registered geometry instance.

参见
:   - [AkCommand\_SA\_RemoveGeometryInstance](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda26c62f270a2d1afd6028ea5c71397cd7)
    - [AkCmd\_SA\_SetGeometryInstance](struct_ak_cmd___s_a___set_geometry_instance.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1503](_ak_command_types_8h_source.html#l01503) 行定义.