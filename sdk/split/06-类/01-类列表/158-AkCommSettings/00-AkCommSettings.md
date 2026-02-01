# AkCommSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_comm_settings-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkCommSettings结构体 参考

`#include <AkCommunication.h>`

|  |  |
| --- | --- |
| 类 | |
| struct | [Ports](struct_ak_comm_settings_1_1_ports.html) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | [AkCommSystem](struct_ak_comm_settings_ad1d3d1fd8c413bf647442ca1ff5b6875.html#ad1d3d1fd8c413bf647442ca1ff5b6875) { [AkCommSystem\_Socket](struct_ak_comm_settings_ad1d3d1fd8c413bf647442ca1ff5b6875.html#ad1d3d1fd8c413bf647442ca1ff5b6875a9a78442505c91710ffd66b5bbb7ea2cf), [AkCommSystem\_HTCS](struct_ak_comm_settings_ad1d3d1fd8c413bf647442ca1ff5b6875.html#ad1d3d1fd8c413bf647442ca1ff5b6875abfd1e78e422437f4302d8c15fd4840a2), [AkCommSystem\_Last](struct_ak_comm_settings_ad1d3d1fd8c413bf647442ca1ff5b6875.html#ad1d3d1fd8c413bf647442ca1ff5b6875a77d87d5d01a056d022514ea753f235fb) } |
|  | Allows selecting the communication system used to connect remotely the Authoring tool on the device. [更多...](struct_ak_comm_settings_ad1d3d1fd8c413bf647442ca1ff5b6875.html#ad1d3d1fd8c413bf647442ca1ff5b6875) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkCommSettings](struct_ak_comm_settings_a57e4269a66287a31573aa919119345ae.html#a57e4269a66287a31573aa919119345ae) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [Ports](struct_ak_comm_settings_1_1_ports.html) | [ports](struct_ak_comm_settings_a270a524ba5f6bad393b4de9b64a3981c.html#a270a524ba5f6bad393b4de9b64a3981c) |
|  | |
| [AkCommSystem](struct_ak_comm_settings_ad1d3d1fd8c413bf647442ca1ff5b6875.html#ad1d3d1fd8c413bf647442ca1ff5b6875) | [commSystem](struct_ak_comm_settings_a4e22ec59f4ec86035c7921f5a8eda76b.html#a4e22ec59f4ec86035c7921f5a8eda76b) |
|  | |
| bool | [bInitSystemLib](struct_ak_comm_settings_a0d7bc52a7ea135577b145c819c9c7760.html#a0d7bc52a7ea135577b145c819c9c7760) |
|  | |
| char | [szAppNetworkName](struct_ak_comm_settings_a72818ad4b565738ac55db8a5aa80299c.html#a72818ad4b565738ac55db8a5aa80299c) [[AK\_COMM\_SETTINGS\_MAX\_STRING\_SIZE](_ak_communication_8h_a3e84d6265701ceaef4eac64092bec3d6.html#a3e84d6265701ceaef4eac64092bec3d6)] |
|  | |
| char | [szCommProxyServerUrl](struct_ak_comm_settings_a13f5a6186a74496d320dcd02675447b4.html#a13f5a6186a74496d320dcd02675447b4) [[AK\_COMM\_SETTINGS\_MAX\_URL\_SIZE](_ak_communication_8h_a30507c06e3bdb32252d90713f50f5ab4.html#a30507c06e3bdb32252d90713f50f5ab4)] |
|  | Optional URL of Comm proxy server (only applicable for platforms incapable of acting as raw UDP/TCP servers) [更多...](struct_ak_comm_settings_a13f5a6186a74496d320dcd02675447b4.html#a13f5a6186a74496d320dcd02675447b4) |
|  | |

## 详细描述

Platform-independent initialization settings of communication module between the Wwise sound engine and authoring tool.

参见
:   - [AK::Comm::Init()](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8)

在文件 [AkCommunication.h](_ak_communication_8h_source.html) 第 [46](_ak_communication_8h_source.html#l00046) 行定义.