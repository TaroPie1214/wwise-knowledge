# AkIOTransferInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_i_o_transfer_info-members.html) |
[Public 属性](#pub-attribs)

AkIOTransferInfo结构体 参考

`#include <AkStreamMgrModule.h>`

类 AkIOTransferInfo 继承关系图:

![](../../../images/struct_ak_i_o_transfer_info.png)

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uFilePosition](struct_ak_i_o_transfer_info_ab515df6bcdda3433afe9d76ceb5d9416.html#ab515df6bcdda3433afe9d76ceb5d9416) |
|  | File offset where transfer should begin. [更多...](struct_ak_i_o_transfer_info_ab515df6bcdda3433afe9d76ceb5d9416.html#ab515df6bcdda3433afe9d76ceb5d9416) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uBufferSize](struct_ak_i_o_transfer_info_ac8fce2c6f48a29670eb68c22069a8bd0.html#ac8fce2c6f48a29670eb68c22069a8bd0) |
|  | Size of the buffer in which the I/O hook can write to. [更多...](struct_ak_i_o_transfer_info_ac8fce2c6f48a29670eb68c22069a8bd0.html#ac8fce2c6f48a29670eb68c22069a8bd0) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uRequestedSize](struct_ak_i_o_transfer_info_adb325c6f758d33f21fc37e7fcc81ab6c.html#adb325c6f758d33f21fc37e7fcc81ab6c) |
|  | Exact number of requested bytes for this transfer. Always equal to or smaller than uBufferSize. [更多...](struct_ak_i_o_transfer_info_adb325c6f758d33f21fc37e7fcc81ab6c.html#adb325c6f758d33f21fc37e7fcc81ab6c) |
|  | |

## 详细描述

Structure for synchronous transfers handshaking with the Low-Level I/O. Used with blocking I/O hooks.

参见
:   [AK::StreamMgr::IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook.html)

在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [92](_ak_stream_mgr_module_8h_source.html#l00092) 行定义.