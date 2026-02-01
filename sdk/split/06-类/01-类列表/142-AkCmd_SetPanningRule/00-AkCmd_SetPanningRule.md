# AkCmd_SetPanningRule

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_panning_rule-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetPanningRule结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPanningRule\_t](_ak_enums_8h_a97cfffbf7bff03a9439cfa99ce9871d0.html#a97cfffbf7bff03a9439cfa99ce9871d0) | [panningRule](struct_ak_cmd___set_panning_rule_a8808ae10b74260859b7fe2665946bbfb.html#a8808ae10b74260859b7fe2665946bbfb) |
|  | Panning rule. [更多...](struct_ak_cmd___set_panning_rule_a8808ae10b74260859b7fe2665946bbfb.html#a8808ae10b74260859b7fe2665946bbfb) |
|  | |
| [AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) | [outputID](struct_ak_cmd___set_panning_rule_aac1b47600f4e5122fdf121a851c305d2.html#aac1b47600f4e5122fdf121a851c305d2) |
|  | Output ID to set the panning rule on. This can be obtained from [AK\_SoundEngine\_GetOutputID](_ak_command_buffer_8h_abcca2351f34551ab1d705e13154b42d1.html#abcca2351f34551ab1d705e13154b42d1). Set to 0 for primary output. [更多...](struct_ak_cmd___set_panning_rule_aac1b47600f4e5122fdf121a851c305d2.html#aac1b47600f4e5122fdf121a851c305d2) |
|  | |

## 详细描述

Sets the panning rule of the specified output.

This may be changed anytime once the sound engine is initialized.

|  |  |
| --- | --- |
|  | **备注:** The specified panning rule will only impact the sound if the processing format is downmixing to Stereo in the mixing process. It will not impact the output if the audio stays in 5.1 until the end, for example. |

This command can fail for the following reasons:

- `AK_InvalidParameter` when panningRule is not one of the values in the enum `AkPanningRule`.

参见
:   - [AkCommand\_SetPanningRule](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaa7648b9699df4a9a1eadc038bd091b20 "See AkCmd_SetPanningRule")
    - [AK::SoundEngine::SetPanningRule](namespace_a_k_1_1_sound_engine_a3e61f70b39d53dd7b8350f2696d9c59e.html#a3e61f70b39d53dd7b8350f2696d9c59e)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1078](_ak_command_types_8h_source.html#l01078) 行定义.