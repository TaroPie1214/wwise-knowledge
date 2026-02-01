# AkCmd_SA_SetGeometryInstance

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_geometry_instance-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetGeometryInstance结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGeometryInstanceID](_ak_spatial_audio_types_8h_a825e3949bdcda8b78d677b95b60ca2f9.html#a825e3949bdcda8b78d677b95b60ca2f9) | [geometryInstanceID](struct_ak_cmd___s_a___set_geometry_instance_a9fb8adf2f11c99fa1eb5d12256db917c.html#a9fb8adf2f11c99fa1eb5d12256db917c) |
|  | Unique geometry set instance ID, chosen by client. [更多...](struct_ak_cmd___s_a___set_geometry_instance_a9fb8adf2f11c99fa1eb5d12256db917c.html#a9fb8adf2f11c99fa1eb5d12256db917c) |
|  | |
| struct [AkGeometryInstanceParams](struct_ak_geometry_instance_params.html) | [params](struct_ak_cmd___s_a___set_geometry_instance_aace130ea42f837700df48b94176fdec3.html#aace130ea42f837700df48b94176fdec3) |
|  | Geometry instance parameters to set. [更多...](struct_ak_cmd___s_a___set_geometry_instance_aace130ea42f837700df48b94176fdec3.html#aace130ea42f837700df48b94176fdec3) |
|  | |

## 详细描述

Add or update a geometry instance from the `SpatialAudio` module for geometric reflection and diffraction processing. A geometry instance is a unique instance of a geometry set with a specified transform (position, rotation and scale). It is necessary to create at least one geometry instance for each geometry set that is to be used for diffraction and reflection simulation. The ID (`geometryInstanceID`) must be unique amongst all geometry instances, including geometry instances referencing different geometry sets. The ID is chosen by the client in a manner similar to `AkGameObjectID's`. To update the transform of an existing geometry instance, call SetGeometryInstance again, passing the same `AkGeometryInstanceID`, with the updated transform.

This command can fail for the following reasons:

- AK\_InvalidParameter: `geometryInstanceID` or `params.GeometrySetID` are not valid IDs or `params.PositionAndOrientation` is not a valid transform.
- AK\_IDNotFound: The `GeometrySetID` does not refer to a registered geometry set.
- AK\_InsufficientMemory: Not enough memory to complete the operation.

参见
:   - [AkCommand\_SA\_SetGeometryInstance](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda68b96460ab326896fd8475d8917ea47b)
    - [AkGeometryInstanceParams](struct_ak_geometry_instance_params.html)
    - [AkCmd\_SA\_RemoveGeometryInstance](struct_ak_cmd___s_a___remove_geometry_instance.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1488](_ak_command_types_8h_source.html#l01488) 行定义.