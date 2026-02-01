# AkCmd_ResetBusConfig

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___reset_bus_config-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ResetBusConfig结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [busID](struct_ak_cmd___reset_bus_config_ab9a5ffb49a171859612395528858f562.html#ab9a5ffb49a171859612395528858f562) |
|  | Bus Short ID. [更多...](struct_ak_cmd___reset_bus_config_ab9a5ffb49a171859612395528858f562.html#ab9a5ffb49a171859612395528858f562) |
|  | |

## 详细描述

Resets the channel configuration for the specified bus.

|  |  |
| --- | --- |
|  | **备注:** You cannot change the configuration of the top-level bus. |

This command can fail for the following reasons:

- `AK_InvalidParameter` when `busID` is an invalid ID.
- `AK_IDNotFound` when the Bus ID is not present in the Init bank.
- `AK_NotCompatible` when the Bus ID refers to a top-level bus.

参见
:   - [AkCommand\_ResetBusConfig](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda3981d5be95b56289ecea8159627d88be "See AkCmd_ResetBusConfig")
    - [AK::SoundEngine::ResetBusConfig](namespace_a_k_1_1_sound_engine_a6d56f27f517874afd7efd14d5e1e5abb.html#a6d56f27f517874afd7efd14d5e1e5abb)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [970](_ak_command_types_8h_source.html#l00970) 行定义.