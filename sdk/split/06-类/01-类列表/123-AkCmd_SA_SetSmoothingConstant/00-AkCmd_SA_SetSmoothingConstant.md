# AkCmd_SA_SetSmoothingConstant

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_smoothing_constant-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetSmoothingConstant结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [smoothingConstantMs](struct_ak_cmd___s_a___set_smoothing_constant_a413479b7b7e67815d9161cbd12f7e228.html#a413479b7b7e67815d9161cbd12f7e228) |
|  | Smoothing constant (ms) [更多...](struct_ak_cmd___s_a___set_smoothing_constant_a413479b7b7e67815d9161cbd12f7e228.html#a413479b7b7e67815d9161cbd12f7e228) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___set_smoothing_constant_a4b75050dba2ab938fcab809caa4aaaa3.html#a4b75050dba2ab938fcab809caa4aaaa3) |
|  | Game Object ID. Set `AK_INVALID_GAME_OBJECT` to set the global smoothing constant, affecting all Spatial Audio Emitters and Rooms. [更多...](struct_ak_cmd___s_a___set_smoothing_constant_a4b75050dba2ab938fcab809caa4aaaa3.html#a4b75050dba2ab938fcab809caa4aaaa3) |
|  | |

## 详细描述

[[Experimental](spatial_audio_experimental.html)] Enable parameter smoothing on the diffraction paths output from the Acoustics Engine, either globally or for a specific game object. Set `smoothingConstantMs` to a value greater than 0 to define the time constant (in milliseconds) for parameter smoothing.

This command can fail for the following reasons:

- AK\_IDNotFound: `gameObjectID` is specified but is not a registered game object.

参见
:   - [AkCommand\_SA\_SetSmoothingConstant](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda74f7939f2b23c98a42c66d8154760b1c)
    - [AkSpatialAudioInitSettings::fSmoothingConstantMs](struct_ak_spatial_audio_init_settings_a406bea3f65e5fef84954eb2603b8ecd0.html#a406bea3f65e5fef84954eb2603b8ecd0)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1914](_ak_command_types_8h_source.html#l01914) 行定义.