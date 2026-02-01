# AkAsyncIOTransferInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_async_i_o_transfer_info-members.html) |
[Public 属性](#pub-attribs)

AkAsyncIOTransferInfo结构体 参考

`#include <AkStreamMgrModule.h>`

类 AkAsyncIOTransferInfo 继承关系图:

![](../../../images/struct_ak_async_i_o_transfer_info.png)

|  |  |
| --- | --- |
| Public 属性 | |
| void \* | [pBuffer](struct_ak_async_i_o_transfer_info_a4c91e8b16c716d670d085378ba491972.html#a4c91e8b16c716d670d085378ba491972) |
|  | Buffer for data transfer. [更多...](struct_ak_async_i_o_transfer_info_a4c91e8b16c716d670d085378ba491972.html#a4c91e8b16c716d670d085378ba491972) |
|  | |
| [AkIOCallback](_ak_stream_mgr_module_8h_a3e66cb4516ec856e0b7d3f6ba45994e0.html#a3e66cb4516ec856e0b7d3f6ba45994e0) | [pCallback](struct_ak_async_i_o_transfer_info_a8f13284daf01c3ab2eb4c7d0b56281e9.html#a8f13284daf01c3ab2eb4c7d0b56281e9) |
|  | Callback function used to notify the high-level device when the transfer is complete. [更多...](struct_ak_async_i_o_transfer_info_a8f13284daf01c3ab2eb4c7d0b56281e9.html#a8f13284daf01c3ab2eb4c7d0b56281e9) |
|  | |
| void \* | [pCookie](struct_ak_async_i_o_transfer_info_ac201fa9f294c35412856eba76e588a50.html#ac201fa9f294c35412856eba76e588a50) |
|  | Reserved. The I/O device uses this cookie to retrieve the owner of the transfer. [更多...](struct_ak_async_i_o_transfer_info_ac201fa9f294c35412856eba76e588a50.html#ac201fa9f294c35412856eba76e588a50) |
|  | |
| void \* | [pUserData](struct_ak_async_i_o_transfer_info_aa60eb75eb65fa725caacfbb00f84289d.html#aa60eb75eb65fa725caacfbb00f84289d) |
|  | Custom user data.   [更多...](struct_ak_async_i_o_transfer_info_aa60eb75eb65fa725caacfbb00f84289d.html#aa60eb75eb65fa725caacfbb00f84289d) |
|  | |
| - Public 属性 继承自 [AkIOTransferInfo](struct_ak_i_o_transfer_info.html) | |
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

Structure for asynchronous transfers handshaking with the Low-Level I/O. Extends [AkIOTransferInfo](struct_ak_i_o_transfer_info.html).

参见
:   - [AK::StreamMgr::IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook.html)
    - [AkIOTransferInfo](struct_ak_i_o_transfer_info.html)
    - AkAIOCallback

在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [119](_ak_stream_mgr_module_8h_source.html#l00119) 行定义.