# AkCmd_ReplaceOutput

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___replace_output-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ReplaceOutput结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) | [outputDeviceID](struct_ak_cmd___replace_output_a418f7f5f45cd9df453366f61dfbc97c2.html#a418f7f5f45cd9df453366f61dfbc97c2) |
|  | ID of output device to replace. This can be obtained from [AK\_SoundEngine\_GetOutputID](_ak_command_buffer_8h_abcca2351f34551ab1d705e13154b42d1.html#abcca2351f34551ab1d705e13154b42d1). Set to 0 to replace the primary output. [更多...](struct_ak_cmd___replace_output_a418f7f5f45cd9df453366f61dfbc97c2.html#a418f7f5f45cd9df453366f61dfbc97c2) |
|  | |
| struct [AkOutputSettings](struct_ak_output_settings.html) | [settings](struct_ak_cmd___replace_output_a25c677f4a88a04b1043eb564d44bde6f.html#a25c677f4a88a04b1043eb564d44bde6f) |
|  | Creation parameters for the new output. [AkOutputSettings](struct_ak_output_settings.html) [更多...](struct_ak_cmd___replace_output_a25c677f4a88a04b1043eb564d44bde6f.html#a25c677f4a88a04b1043eb564d44bde6f) |
|  | |

## 详细描述

Replaces an output device previously created during engine initialization or from [AkCmd\_AddOutput](struct_ak_cmd___add_output.html), with a new output device. In addition to simply removing one output device and adding a new one, the new output device will also be used on all of the master buses that the old output device was associated with, and preserve all listeners that were attached to the old output device.

This command can fail for the following reasons:

- `AK_InvalidParameter:` Out of range parameters or unsupported parameter combinations.
- `AK_IDNotFound:` The audioDeviceShareset on in\_settings doesn't exist. Possibly, the Init bank isn't loaded yet or was not updated with latest changes.
- `AK_InsufficientMemory:` Not enough memory to complete the operation.
- `AK_DeviceNotCompatible:` Request output settings are incompatible with current system. A dummy output was created instead.

参见
:   - [AkCommand\_ReplaceOutput](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda9b3a7bf26e01fa4633f070ee51fa8f68 "See AkCmd_ReplaceOutput")
    - [AK::SoundEngine::ReplaceOutput](namespace_a_k_1_1_sound_engine_a81521a4611d3891c499ec9c5eb421ac2.html#a81521a4611d3891c499ec9c5eb421ac2)
    - [集成二路输出](integrating_secondary_outputs.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [913](_ak_command_types_8h_source.html#l00913) 行定义.