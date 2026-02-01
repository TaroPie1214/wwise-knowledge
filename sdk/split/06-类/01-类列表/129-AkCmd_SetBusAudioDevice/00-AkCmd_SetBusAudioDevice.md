# AkCmd_SetBusAudioDevice

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_bus_audio_device-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetBusAudioDevice结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [busID](struct_ak_cmd___set_bus_audio_device_a55357730854fa1f1f8206e45e0ff930a.html#a55357730854fa1f1f8206e45e0ff930a) |
|  | ID of the master bus [更多...](struct_ak_cmd___set_bus_audio_device_a55357730854fa1f1f8206e45e0ff930a.html#a55357730854fa1f1f8206e45e0ff930a) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [audioDeviceSharesetID](struct_ak_cmd___set_bus_audio_device_a1c8f64a1f39ae94e07b5c8c3438a95c0.html#a1c8f64a1f39ae94e07b5c8c3438a95c0) |
|  | ID of Audio Device shareset to become the new destination output of the master bus. [更多...](struct_ak_cmd___set_bus_audio_device_a1c8f64a1f39ae94e07b5c8c3438a95c0.html#a1c8f64a1f39ae94e07b5c8c3438a95c0) |
|  | |

## 详细描述

Sets the Audio Device to which a master bus outputs.

This overrides the setting in the Wwise project. Can only be set on top-level busses.

|  |  |
| --- | --- |
|  | **备注:** This command is useful only if used before the creation of an output, at the beginning of the sound engine setup. Once active outputs using this Bus have been created, it is imperative to use [AkCmd\_ReplaceOutput](struct_ak_cmd___replace_output.html) instead to change the type of output. |

This command can fail for the following reasons:

- `AK_InvalidParameter` when `busID` or `outputDeviceID` are invalid IDs.
- `AK_IDNotFound` when either the Bus ID or the Device ID are not present in the Init bank or when the specified bus is not a top-level bus.

参见
:   - [AkCommand\_SetBusAudioDevice](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda3a6b55b2d0117c80d088f6e8c0fa0e05 "See AkCmd_SetBusAudioDevice")
    - [AK::SoundEngine::SetBusDevice](namespace_a_k_1_1_sound_engine_adf34d8d0405ddb7d10b4c5c63db13e5b.html#adf34d8d0405ddb7d10b4c5c63db13e5b)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [934](_ak_command_types_8h_source.html#l00934) 行定义.