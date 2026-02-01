# IAkLowLevelIOHook

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [StreamMgr](namespace_a_k_1_1_stream_mgr.html)
- [IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook.html)

[所有成员列表](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook-members.html) |
[类](#nested-classes) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::StreamMgr::IAkLowLevelIOHook类 参考abstract

`#include <AkStreamMgrModule.h>`

|  |  |
| --- | --- |
| 类 | |
| struct | [BatchIoTransferItem](struct_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_1_1_batch_io_transfer_item.html) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Close](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a7a50a7a5fa624691d7bb7608753dc096.html#a7a50a7a5fa624691d7bb7608753dc096) ([AkFileDesc](struct_ak_file_desc.html) \*in\_pFileDesc)=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetBlockSize](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a5018552d455ddc2a95b727fc543aac9e.html#a5018552d455ddc2a95b727fc543aac9e) ([AkFileDesc](struct_ak_file_desc.html) &in\_fileDesc)=0 |
|  | |
| virtual void | [GetDeviceDesc](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a06860cb1211c2ebd5c49f4429cc66a0b.html#a06860cb1211c2ebd5c49f4429cc66a0b) ([AkDeviceDesc](struct_ak_device_desc.html) &out\_deviceDesc)=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetDeviceData](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a885d39fdd78da3748f78e176615fb6ea.html#a885d39fdd78da3748f78e176615fb6ea) ()=0 |
|  | |
| virtual void | [BatchOpen](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a0abfde848b599b5e5b8e8ed63dc8b555.html#a0abfde848b599b5e5b8e8ed63dc8b555) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumFiles, [AkAsyncFileOpenData](struct_ak_async_file_open_data.html) \*\*in\_ppItems)=0 |
|  | |
| virtual void | [BatchRead](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a9bc325405bc17c0a5105d0a53981b186.html#a9bc325405bc17c0a5105d0a53981b186) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumTransfers, [BatchIoTransferItem](struct_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_1_1_batch_io_transfer_item.html) \*in\_pTransferItems)=0 |
|  | |
| virtual void | [BatchWrite](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a8f5041a24e395784437a62cdd2140505.html#a8f5041a24e395784437a62cdd2140505) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumTransfers, [BatchIoTransferItem](struct_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_1_1_batch_io_transfer_item.html) \*in\_pTransferItems)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [OutputSearchedPaths](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a40d53d28e4c8942d23ba011f1222d29a.html#a40d53d28e4c8942d23ba011f1222d29a) ([AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) in\_result, const [AkFileOpenData](struct_ak_file_open_data.html) &in\_FileOpen, [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_searchedPath, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_pathSize) |
|  | This function is called to provide information when file related errors occur. The base paths known by this IO hook should be returned in out\_searchedPath. [更多...](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a40d53d28e4c8942d23ba011f1222d29a.html#a40d53d28e4c8942d23ba011f1222d29a) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a35a38687a6a0fc6431c8dc8317f2434f.html#a35a38687a6a0fc6431c8dc8317f2434f) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a35a38687a6a0fc6431c8dc8317f2434f.html#a35a38687a6a0fc6431c8dc8317f2434f) |
|  | |

## 详细描述

Interface for batched deferred low-level I/O transfers. This I/O transfer handshaking method is preferred when you want to hook I/O to your own I/O streaming technology, and you want to submit multiple I/O requests in one call, so as to allow for better opportunities for CPU and I/O performance. All operations in this interface will be happening in the device's own thread, separate from the main audio thread. Also, it is assumed that all operations are asynchronous although immediate resolution is also supported. You may queue them into your own system, and even use the heuristics passed down to this level for your convenience. Note that the requests are always sent in the order that the Stream Manager considers to be the most appropriate. You may receive less than [AkDeviceSettings::uMaxConcurrentIO](struct_ak_device_settings_af49f8b3af816b58296e952b20de2d7a3.html#af49f8b3af816b58296e952b20de2d7a3 "Maximum number of transfers that can be sent simultaneously to the Low-Level I/O.") at any given time. The number of concurrent transfers depends on the number of streams running in the high-level streaming device, and on its target buffering length and granularity. Your advantage at this level is to be aware of file placement, so you may try to re-order requests in order to minimize seeking on disk. Calls to [BatchRead()](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a9bc325405bc17c0a5105d0a53981b186.html#a9bc325405bc17c0a5105d0a53981b186)/BatchWrite() should return as soon as possible. You need to call [AkAsyncIOTransferInfo::pCallback](struct_ak_async_i_o_transfer_info_a8f13284daf01c3ab2eb4c7d0b56281e9.html#a8f13284daf01c3ab2eb4c7d0b56281e9 "Callback function used to notify the high-level device when the transfer is complete.") for all individual items in a transfer batch. Cancel() is provided in order to inform you that the streaming device will flush this transfer upon completion. You may implement it or not. In all cases, you must call the callback.

在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [244](_ak_stream_mgr_module_8h_source.html#l00244) 行定义.