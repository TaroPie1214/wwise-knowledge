# IAkFileLocationResolver

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [StreamMgr](namespace_a_k_1_1_stream_mgr.html)
- [IAkFileLocationResolver](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver.html)

[所有成员列表](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::StreamMgr::IAkFileLocationResolver类 参考

`#include <AkStreamMgrModule.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetNextPreferredDevice](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver_a5c7515d84fe8b7ce1e1c06690447673d.html#a5c7515d84fe8b7ce1e1c06690447673d) ([AkAsyncFileOpenData](struct_ak_async_file_open_data.html) &in\_FileOpen, [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) &io\_idDevice) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkFileLocationResolver](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver_aa43e723e440d9a298fbdcacf59bbf019.html#aa43e723e440d9a298fbdcacf59bbf019) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver_aa43e723e440d9a298fbdcacf59bbf019.html#aa43e723e440d9a298fbdcacf59bbf019) |
|  | |

## 详细描述

File location resolver interface. There is one and only one File Location Resolver that is registered to the Stream Manager (using [AK::StreamMgr::SetFileLocationResolver()](namespace_a_k_1_1_stream_mgr_ab5c2340963ac5ff81e49969b74ef2520.html#ab5c2340963ac5ff81e49969b74ef2520)). Its purpose is to resolve a file name or ID to a streaming device (I/O hook) that can handle the file. When your Low-Level I/O submodule uses a single device, you should create a standalone I/O hook which implements one of the I/O hooks defined above, as well as the File Location Resolver. You then register this object to the Stream Manager as the File Location Resolver. If you wish to create multiple devices, then you should have a separate object that implements [AK::StreamMgr::IAkFileLocationResolver](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver.html) and registers to the Stream Manager as such. This object will be used to dispatch the file open request to the appropriate device. The strategy you will use to select the correct device is up to you to implement. There is a built-in mechanism of chaining devices through [GetNextPreferredDevice()](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver_a5c7515d84fe8b7ce1e1c06690447673d.html#a5c7515d84fe8b7ce1e1c06690447673d). If a device can't open a file GetNextPreferredDevice will be called again to get the next device to check.

在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [379](_ak_stream_mgr_module_8h_source.html#l00379) 行定义.