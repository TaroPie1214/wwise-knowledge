# MsgContext

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Monitor](namespace_a_k_1_1_monitor.html)
- [MsgContext](struct_a_k_1_1_monitor_1_1_msg_context.html)

[所有成员列表](struct_a_k_1_1_monitor_1_1_msg_context-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK::Monitor::MsgContext结构体 参考

`#include <AkMonitorError.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [MsgContext](struct_a_k_1_1_monitor_1_1_msg_context_a0e3e25e67c483365b9293fc5bf81f373.html#a0e3e25e67c483365b9293fc5bf81f373) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) pId=[AK\_INVALID\_PLAYING\_ID](_ak_constants_8h_a5141397d9cce5d9656f58931596d8360.html#a5141397d9cce5d9656f58931596d8360), [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) goId=[AK\_INVALID\_GAME\_OBJECT](_ak_constants_8h_a82290a98a9cf7901722a69a590aeee34.html#a82290a98a9cf7901722a69a590aeee34), [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) nodeId=[AK\_INVALID\_UNIQUE\_ID](_ak_constants_8h_aa512c62662d05d5b50dd08792ed254ec.html#aa512c62662d05d5b50dd08792ed254ec), bool isBus=false) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [in\_playingID](struct_a_k_1_1_monitor_1_1_msg_context_a81ddf0b01439ef4d74ac5926e6efc3e7.html#a81ddf0b01439ef4d74ac5926e6efc3e7) |
|  | Related Playing ID if applicable [更多...](struct_a_k_1_1_monitor_1_1_msg_context_a81ddf0b01439ef4d74ac5926e6efc3e7.html#a81ddf0b01439ef4d74ac5926e6efc3e7) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [in\_gameObjID](struct_a_k_1_1_monitor_1_1_msg_context_a1ed993d720e5d959f442ead3d0712a41.html#a1ed993d720e5d959f442ead3d0712a41) |
|  | Related Game Object ID if applicable, AK\_INVALID\_GAME\_OBJECT otherwise [更多...](struct_a_k_1_1_monitor_1_1_msg_context_a1ed993d720e5d959f442ead3d0712a41.html#a1ed993d720e5d959f442ead3d0712a41) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [in\_soundID](struct_a_k_1_1_monitor_1_1_msg_context_ae7fd1273ca9491a414518318067d58da.html#ae7fd1273ca9491a414518318067d58da) |
|  | Related Audio Node ID if applicable, AK\_INVALID\_UNIQUE\_ID otherwise [更多...](struct_a_k_1_1_monitor_1_1_msg_context_ae7fd1273ca9491a414518318067d58da.html#ae7fd1273ca9491a414518318067d58da) |
|  | |
| bool | [in\_bIsBus](struct_a_k_1_1_monitor_1_1_msg_context_a385064b3f1b154f3b36e8a9ea7943b89.html#a385064b3f1b154f3b36e8a9ea7943b89) |
|  | true if in\_audioNodeID is a bus [更多...](struct_a_k_1_1_monitor_1_1_msg_context_a385064b3f1b154f3b36e8a9ea7943b89.html#a385064b3f1b154f3b36e8a9ea7943b89) |
|  | |

## 详细描述

在文件 [AkMonitorError.h](_ak_monitor_error_8h_source.html) 第 [45](_ak_monitor_error_8h_source.html#l00045) 行定义.