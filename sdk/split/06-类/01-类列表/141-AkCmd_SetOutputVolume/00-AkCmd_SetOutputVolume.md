# AkCmd_SetOutputVolume

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_output_volume-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetOutputVolume结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) | [outputID](struct_ak_cmd___set_output_volume_ac2ade2e21803ad4a76a4204ba4f5fa4f.html#ac2ade2e21803ad4a76a4204ba4f5fa4f) |
|  | Output ID to set the volume on. This can be obtained from [AK\_SoundEngine\_GetOutputID](_ak_command_buffer_8h_abcca2351f34551ab1d705e13154b42d1.html#abcca2351f34551ab1d705e13154b42d1). Set to 0 for primary output. [更多...](struct_ak_cmd___set_output_volume_ac2ade2e21803ad4a76a4204ba4f5fa4f.html#ac2ade2e21803ad4a76a4204ba4f5fa4f) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [volume](struct_ak_cmd___set_output_volume_a6368b52e95810b605f06ff91d294b5ed.html#a6368b52e95810b605f06ff91d294b5ed) |
|  | Volume (0.0 = Muted, 1.0 = Volume max). [更多...](struct_ak_cmd___set_output_volume_a6368b52e95810b605f06ff91d294b5ed.html#a6368b52e95810b605f06ff91d294b5ed) |
|  | |

## 详细描述

Sets the volume of a output device.

This command will fail if the value specified was NaN or Inf.

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1057](_ak_command_types_8h_source.html#l01057) 行定义.