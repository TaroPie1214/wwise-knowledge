# AkCmd_RemoveOutput

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___remove_output-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_RemoveOutput结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) | [outputDeviceID](struct_ak_cmd___remove_output_a79024afd99e9df87828b9ba0a3b4713d.html#a79024afd99e9df87828b9ba0a3b4713d) |
|  | ID of output device. This can be obtained from [AK\_SoundEngine\_GetOutputID](_ak_command_buffer_8h_abcca2351f34551ab1d705e13154b42d1.html#abcca2351f34551ab1d705e13154b42d1). Set to 0 for primary output. [更多...](struct_ak_cmd___remove_output_a79024afd99e9df87828b9ba0a3b4713d.html#a79024afd99e9df87828b9ba0a3b4713d) |
|  | |

## 详细描述

Removes one output added through [AkCmd\_AddOutput](struct_ak_cmd___add_output.html)

If a listener was associated with the device, you should consider unregistering the listener before adding this command so that Game Object/Listener routing is properly updated according to your game scenario.

参见
:   - [AkCommand\_RemoveOutput](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda6ac7a9a5ab95715129a8db52fc759d94 "See AkCmd_RemoveOutput")
    - [集成二路输出](integrating_secondary_outputs.html)
    - [AK::SoundEngine::RemoveOutput](namespace_a_k_1_1_sound_engine_a0932ed2a3669258ecc3bbe6448314020.html#a0932ed2a3669258ecc3bbe6448314020)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [894](_ak_command_types_8h_source.html#l00894) 行定义.