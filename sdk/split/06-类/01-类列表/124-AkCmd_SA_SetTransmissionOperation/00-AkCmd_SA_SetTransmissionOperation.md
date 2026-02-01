# AkCmd_SA_SetTransmissionOperation

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_transmission_operation-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetTransmissionOperation结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [operation](struct_ak_cmd___s_a___set_transmission_operation_a776b99c90dac0a7cd71aba3b6dc91ed8.html#a776b99c90dac0a7cd71aba3b6dc91ed8) |
|  | The operation to be used on all transmission paths. Possible values are listed in the [AkTransmissionOperation](_ak_spatial_audio_types_8h_aa15f2f697dced35d82fcc58bc437cfb8.html#aa15f2f697dced35d82fcc58bc437cfb8) enum. [更多...](struct_ak_cmd___s_a___set_transmission_operation_a776b99c90dac0a7cd71aba3b6dc91ed8.html#a776b99c90dac0a7cd71aba3b6dc91ed8) |
|  | |

## 详细描述

Set the operation used to calculate transmission loss on a direct path between emitter and listener.

This command can fail for the following reasons:

- AK\_InvalidParameter: `operation` is not within the accepted range.

参见
:   - [AkCommand\_SA\_SetTransmissionOperation](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda92a149b06115f44168c4471d091445b2)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1927](_ak_command_types_8h_source.html#l01927) 行定义.