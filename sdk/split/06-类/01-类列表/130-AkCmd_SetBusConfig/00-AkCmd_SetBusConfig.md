# AkCmd_SetBusConfig

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_bus_config-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetBusConfig结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [busID](struct_ak_cmd___set_bus_config_a75eae8eb183242b9ba3ab1293be8cff1.html#a75eae8eb183242b9ba3ab1293be8cff1) |
|  | Bus Short ID. [更多...](struct_ak_cmd___set_bus_config_a75eae8eb183242b9ba3ab1293be8cff1.html#a75eae8eb183242b9ba3ab1293be8cff1) |
|  | |
| struct [AkChannelConfig](struct_ak_channel_config.html) | [channelConfig](struct_ak_cmd___set_bus_config_a2ee10ce8af5930df0dc22b11f1a91196.html#a2ee10ce8af5930df0dc22b11f1a91196) |
|  | Desired channel configuration. An invalid configuration (from default constructor) means "as parent". [更多...](struct_ak_cmd___set_bus_config_a2ee10ce8af5930df0dc22b11f1a91196.html#a2ee10ce8af5930df0dc22b11f1a91196) |
|  | |

## 详细描述

Forces channel configuration for the specified bus.

|  |  |
| --- | --- |
|  | **备注:** You cannot change the configuration of the top-level bus. |

This command can fail for the following reasons:

- `AK_InvalidParameter` when `busID` is an invalid ID.
- `AK_IDNotFound` when the Bus ID is not present in the Init bank.
- `AK_NotCompatible` when the Bus ID refers to a top-level bus.

参见
:   - [AkCommand\_SetBusConfig](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda357393637deca3073f1069c487ec2f35 "See AkCmd_SetBusConfig")
    - [AK::SoundEngine::SetBusConfig](namespace_a_k_1_1_sound_engine_aa4da48bc7fe7adc10f42272f62fd33fe.html#aa4da48bc7fe7adc10f42272f62fd33fe)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [952](_ak_command_types_8h_source.html#l00952) 行定义.