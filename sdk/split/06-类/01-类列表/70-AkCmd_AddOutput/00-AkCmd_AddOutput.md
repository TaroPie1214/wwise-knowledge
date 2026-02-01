# AkCmd_AddOutput

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___add_output-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_AddOutput结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkOutputSettings](struct_ak_output_settings.html) | [settings](struct_ak_cmd___add_output_a29131216a41bfed0df65a268dc1df861.html#a29131216a41bfed0df65a268dc1df861) |
|  | Creation parameters for this output. [AkOutputSettings](struct_ak_output_settings.html) [更多...](struct_ak_cmd___add_output_a29131216a41bfed0df65a268dc1df861.html#a29131216a41bfed0df65a268dc1df861) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numListenerIDs](struct_ak_cmd___add_output_a2e9b1038480805703c2b5fa8ae327550.html#a2e9b1038480805703c2b5fa8ae327550) |
|  | The number of listener IDs that follow the command. [更多...](struct_ak_cmd___add_output_a2e9b1038480805703c2b5fa8ae327550.html#a2e9b1038480805703c2b5fa8ae327550) |
|  | |

## 详细描述

Adds an output to the sound engine. Use this to add controller-attached headphones, controller speakers, DVR output, etc.   
The `settings` parameter contains an Audio Device shareset to specify the output plugin to use and a device ID to specify the instance, if necessary (e.g. which game controller).

The Sound Engine can accept an array of `AkGameObjectID` objects after the command. These objects correspond to listener IDs attached to the output device. When specified, only the sounds routed to game objects linked to those listeners will play in this device. It is necessary to have separate listeners if multiple devices of the same type can coexist (e.g. controller speakers).

To attach listener IDs to the device being added:

```
auto cmd = (AkCmd_AddOutput*)AK_CommandBuffer_Add(buffer, AkCommand_AddOutput);
// Fill out the command...
cmd->numListenerIDs = mylistenerArray.size();
AK_CommandBuffer_AddArray(buffer, sizeof(AkGameObjectID), mylistenerArray.size(), mylistenerArray.data());
```

When `numListenerIDs` is 0, sound routing simply obey the associations between Master Busses and Audio Devices setup in the Wwise Project.

This command can fail for the following reasons:

- `AK_InvalidParameter:` Out of range parameters or unsupported parameter combinations.
- `AK_IDNotFound:` The audioDeviceShareset in `settings` doesn't exist. Possibly, the Init bank isn't loaded yet or was not updated with latest changes.
- `AK_InsufficientMemory:` Not enough memory to complete the operation.
- `AK_DeviceNotCompatible:` Request output settings are incompatible with current system. A dummy output was created instead.

参见
:   - [AkCommand\_AddOutput](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda3254436f52efd13b0a86d9176b751196 "See AkCmd_AddOutput")
    - [AK::SoundEngine::AddOutput](namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html#a15ab79f954a307902f529d8ccde8ad48)
    - [集成二路输出](integrating_secondary_outputs.html)
    - [默认 Wwise Audio Device](default_audio_devices.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [879](_ak_command_types_8h_source.html#l00879) 行定义.