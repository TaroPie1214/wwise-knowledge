# Ports

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkCommSettings](struct_ak_comm_settings.html)
- [Ports](struct_ak_comm_settings_1_1_ports.html)

[所有成员列表](struct_ak_comm_settings_1_1_ports-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkCommSettings::Ports结构体 参考

`#include <AkCommunication.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Ports](struct_ak_comm_settings_1_1_ports_a04376f3823460eb29d46983ba40bf3c3.html#a04376f3823460eb29d46983ba40bf3c3) () |
|  | Constructor [更多...](struct_ak_comm_settings_1_1_ports_a04376f3823460eb29d46983ba40bf3c3.html#a04376f3823460eb29d46983ba40bf3c3) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [uDiscoveryBroadcast](struct_ak_comm_settings_1_1_ports_ac18f3080b45b5eba2634527d5d27e75c.html#ac18f3080b45b5eba2634527d5d27e75c) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [uCommand](struct_ak_comm_settings_1_1_ports_a2980cfef40f976dd403f8f48c0789265.html#a2980cfef40f976dd403f8f48c0789265) |
|  | |

## 详细描述

[Ports](struct_ak_comm_settings_1_1_ports.html) used for communication between the Wwise authoring application and your game. All of these ports are opened in the game when Wwise communication is enabled.

参见
:   - [通信端口](workingwithsdks_initialization.html#initialization_comm_ports)
    - [AK::Comm::GetDefaultInitSettings()](namespace_a_k_1_1_comm_a3280f8b7ad6261d8b2a4bdf39c234fa7.html#a3280f8b7ad6261d8b2a4bdf39c234fa7)
    - [AK::Comm::Init()](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8)

在文件 [AkCommunication.h](_ak_communication_8h_source.html) 第 [62](_ak_communication_8h_source.html#l00062) 行定义.