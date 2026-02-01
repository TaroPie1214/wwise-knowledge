# AkCmd_SA_SetDiffractionOrder

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_diffraction_order-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetDiffractionOrder结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [diffractionOrder](struct_ak_cmd___s_a___set_diffraction_order_a0e445a121cc36e3c29202e9f5084a9d8.html#a0e445a121cc36e3c29202e9f5084a9d8) |
|  | Number of diffraction edges to consider in path calculations. Valid range [0,8] [更多...](struct_ak_cmd___s_a___set_diffraction_order_a0e445a121cc36e3c29202e9f5084a9d8.html#a0e445a121cc36e3c29202e9f5084a9d8) |
|  | |
| bool | [updatePaths](struct_ak_cmd___s_a___set_diffraction_order_a67cf6a9410d5c8cc3123e2568f2745fc.html#a67cf6a9410d5c8cc3123e2568f2745fc) |
|  | Set to true to clear existing diffraction paths and to force the re-computation of new paths. If false, existing paths will remain and new paths will be computed when the emitter or listener moves. [更多...](struct_ak_cmd___s_a___set_diffraction_order_a67cf6a9410d5c8cc3123e2568f2745fc.html#a67cf6a9410d5c8cc3123e2568f2745fc) |
|  | |

## 详细描述

Set the diffraction order for geometric path calculation. The diffraction order indicates the number of edges a sound can diffract around. A higher number requires more CPU resources but results in paths found around more complex geometry. Set to 0 to globally disable geometric diffraction processing.

This command can fail for the following reasons:

- AK\_InvalidParameter: `diffractionOrder` is not in the accepted range.

参见
:   - [AkCommand\_SA\_SetDiffractionOrder](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda3c84762eb77d1612fbccfbaf56a9ed26)
    - [AkSpatialAudioInitSettings::uMaxDiffractionOrder](struct_ak_spatial_audio_init_settings_a0e01d0d34659de40a8d84d93e05dfeab.html#a0e01d0d34659de40a8d84d93e05dfeab)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1863](_ak_command_types_8h_source.html#l01863) 行定义.