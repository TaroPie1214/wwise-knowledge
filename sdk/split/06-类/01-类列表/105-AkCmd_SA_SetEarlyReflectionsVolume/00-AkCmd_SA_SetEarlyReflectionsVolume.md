# AkCmd_SA_SetEarlyReflectionsVolume

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_early_reflections_volume-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetEarlyReflectionsVolume结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___set_early_reflections_volume_a6f4fb6ee5dcd28991aeea779a1d2afc0.html#a6f4fb6ee5dcd28991aeea779a1d2afc0) |
|  | Game object ID [更多...](struct_ak_cmd___s_a___set_early_reflections_volume_a6f4fb6ee5dcd28991aeea779a1d2afc0.html#a6f4fb6ee5dcd28991aeea779a1d2afc0) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [volume](struct_ak_cmd___s_a___set_early_reflections_volume_a02211cde1d2e278bf606f9ad77fcfab5.html#a02211cde1d2e278bf606f9ad77fcfab5) |
|  | Send volume (linear) for auxiliary send. Set 0.f to disable reflection processing. Valid range 0.f-1.f. [更多...](struct_ak_cmd___s_a___set_early_reflections_volume_a02211cde1d2e278bf606f9ad77fcfab5.html#a02211cde1d2e278bf606f9ad77fcfab5) |
|  | |

## 详细描述

Set an early reflections send volume for a particular game object. The `volume` parameter is used to control the volume of the early reflections send. It is combined with the early reflections volume specified in the authoring tool, and is applied to all sounds playing on the game object. Setting `volume` to 0.f will disable all reflection processing for this game object.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is invalid.
- AK\_IDNotFound: `gameObjectID` is specified but is not a registered game object.

参见
:   - [AkCommand\_SA\_SetEarlyReflectionsVolume](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaedcd8ce98045d86fac9ece68985e80b4)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1820](_ak_command_types_8h_source.html#l01820) 行定义.