# AkCmd_SetScalingFactor

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_scaling_factor-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetScalingFactor结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___set_scaling_factor_a50bc0a6344e4f02f7dfd6a308e156827.html#a50bc0a6344e4f02f7dfd6a308e156827) |
|  | Game Object ID [更多...](struct_ak_cmd___set_scaling_factor_a50bc0a6344e4f02f7dfd6a308e156827.html#a50bc0a6344e4f02f7dfd6a308e156827) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [scalingFactor](struct_ak_cmd___set_scaling_factor_a212e88ad93a28e84633db2dbf82432ef.html#a212e88ad93a28e84633db2dbf82432ef) |
|  | Scaling factor [更多...](struct_ak_cmd___set_scaling_factor_a212e88ad93a28e84633db2dbf82432ef.html#a212e88ad93a28e84633db2dbf82432ef) |
|  | |

## 详细描述

Sets the scaling factor of a Game Object. Modifies the attenuation computations on this Game Object to simulate sounds with a larger or smaller area of effect.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is not a valid game object ID or `scalingFactor` is outside the valid range.
- AK\_IDNotFound: `gameObjectID` is not a registered game object ID.

参见
:   [AkCommand\_SetScalingFactor](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf4f3a64d5fd69388c71ac9da5876898e "See AkCmd_SetScalingFactor")

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [482](_ak_command_types_8h_source.html#l00482) 行定义.