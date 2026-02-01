# AkAsyncFileOpenData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_async_file_open_data-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkAsyncFileOpenData结构体 参考

`#include <AkStreamMgrModule.h>`

类 AkAsyncFileOpenData 继承关系图:

![](../../../images/struct_ak_async_file_open_data.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [~AkAsyncFileOpenData](struct_ak_async_file_open_data_a8daba8e6af18c288722745332bcc82e0.html#a8daba8e6af18c288722745332bcc82e0) () |
|  | |
|  | [AkAsyncFileOpenData](struct_ak_async_file_open_data_a511935d72bff752c1f3a432463cb4f8a.html#a511935d72bff752c1f3a432463cb4f8a) (const [AkFileOpenData](struct_ak_file_open_data.html) &in\_copy) |
|  | |
|  | [AkAsyncFileOpenData](struct_ak_async_file_open_data_ad9f23895ee09b801b8ecf24bb9e2faea.html#ad9f23895ee09b801b8ecf24bb9e2faea) (const [AkAsyncFileOpenData](struct_ak_async_file_open_data.html) &in\_copy) |
|  | |
|  | [AkAsyncFileOpenData](struct_ak_async_file_open_data_a920b83ca6b7d391a474a4841284ee5fa.html#a920b83ca6b7d391a474a4841284ee5fa) () |
|  | |
|  | [AkAsyncFileOpenData](struct_ak_async_file_open_data_ac773bad9685141246e322b4bc8e3e3e3.html#ac773bad9685141246e322b4bc8e3e3e3) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszFileName, [AkOpenMode](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7) in\_eOpenMode=[AK\_OpenModeRead](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab35230305828a2d0aee87a3190ff661f), [AkFileSystemFlags](struct_ak_file_system_flags.html) \*in\_pFlags=NULL) |
|  | |
|  | [AkAsyncFileOpenData](struct_ak_async_file_open_data_afffa0a77d6c9fe0d295c0a518ce29c89.html#afffa0a77d6c9fe0d295c0a518ce29c89) ([AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) in\_idFile, [AkOpenMode](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7) in\_eOpenMode=[AK\_OpenModeRead](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab35230305828a2d0aee87a3190ff661f), [AkFileSystemFlags](struct_ak_file_system_flags.html) \*in\_pFlags=NULL) |
|  | Functions used to manage optional stream name. The name will be used when sending stream information to the Wwise profiler. [更多...](struct_ak_async_file_open_data_afffa0a77d6c9fe0d295c0a518ce29c89.html#afffa0a77d6c9fe0d295c0a518ce29c89) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetStreamName](struct_ak_async_file_open_data_a9e2352c2e0e3336eafab76c92b29f759.html#a9e2352c2e0e3336eafab76c92b29f759) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszStreamName) |
|  | |
| const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \* | [GetStreamName](struct_ak_async_file_open_data_ac0542f7f79105f4f3a3e9c4d0d7ed0bc.html#ac0542f7f79105f4f3a3e9c4d0d7ed0bc) () const |
|  | |
| - Public 成员函数 继承自 [AkFileOpenData](struct_ak_file_open_data.html) | |
|  | [AkFileOpenData](struct_ak_file_open_data_ac79aeff11cb4f4a41d1e50693c3c99a5.html#ac79aeff11cb4f4a41d1e50693c3c99a5) () |
|  | |
|  | [AkFileOpenData](struct_ak_file_open_data_a1cfc1486ccff8e67cb414a7b3309cea0.html#a1cfc1486ccff8e67cb414a7b3309cea0) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszFileName, [AkOpenMode](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7) in\_eOpenMode=[AK\_OpenModeRead](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab35230305828a2d0aee87a3190ff661f), [AkFileSystemFlags](struct_ak_file_system_flags.html) \*in\_pFlags=NULL) |
|  | |
|  | [AkFileOpenData](struct_ak_file_open_data_aae542ccaec59bf6edb117063ed845dc8.html#aae542ccaec59bf6edb117063ed845dc8) ([AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) in\_idFile, [AkOpenMode](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7) in\_eOpenMode=[AK\_OpenModeRead](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab35230305828a2d0aee87a3190ff661f), [AkFileSystemFlags](struct_ak_file_system_flags.html) \*in\_pFlags=NULL) |
|  | |
|  | [AkFileOpenData](struct_ak_file_open_data_a794e9f2871d3e28a86dca7aecf2d9a2b.html#a794e9f2871d3e28a86dca7aecf2d9a2b) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszFileName, [AkFileSystemFlags](struct_ak_file_system_flags.html) \*in\_pFlags) |
|  | |
|  | [AkFileOpenData](struct_ak_file_open_data_a2db0e84a8f70a2186e9308e4be92fa0f.html#a2db0e84a8f70a2186e9308e4be92fa0f) ([AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) in\_idFile, [AkFileSystemFlags](struct_ak_file_system_flags.html) \*in\_pFlags) |
|  | |
| bool | [IsValid](struct_ak_file_open_data_a1619d223cc8f240670565971b1dc1f20.html#a1619d223cc8f240670565971b1dc1f20) () const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkFileOpenCallback](_ak_stream_mgr_module_8h_ae00967344e3fcd553d8cdf391ec7081e.html#ae00967344e3fcd553d8cdf391ec7081e) | [pCallback](struct_ak_async_file_open_data_a723b3d53794fc8c325d51c455a586229.html#a723b3d53794fc8c325d51c455a586229) |
|  | Callback function used to notify the high-level device when Open is done [更多...](struct_ak_async_file_open_data_a723b3d53794fc8c325d51c455a586229.html#a723b3d53794fc8c325d51c455a586229) |
|  | |
| void \* | [pCookie](struct_ak_async_file_open_data_a97743485d9534d61987aacb96c57704f.html#a97743485d9534d61987aacb96c57704f) |
|  | Reserved. Pass this unchanged to the callback function. The I/O device uses this cookie to retrieve the owner of the transfer. [更多...](struct_ak_async_file_open_data_a97743485d9534d61987aacb96c57704f.html#a97743485d9534d61987aacb96c57704f) |
|  | |
| [AkFileDesc](struct_ak_file_desc.html) \* | [pFileDesc](struct_ak_async_file_open_data_ae3694e2a2a9f90364b3f865cc84627e5.html#ae3694e2a2a9f90364b3f865cc84627e5) |
|  | File Descriptor to fill once the Open operation is complete. [更多...](struct_ak_async_file_open_data_ae3694e2a2a9f90364b3f865cc84627e5.html#ae3694e2a2a9f90364b3f865cc84627e5) |
|  | |
| void \* | [pCustomData](struct_ak_async_file_open_data_a496f8e8982ec35bd71d1734c151311c3.html#a496f8e8982ec35bd71d1734c151311c3) |
|  | Convenience pointer for the IO hook implementer. Useful for additional data used in asynchronous implementations, for example. [更多...](struct_ak_async_file_open_data_a496f8e8982ec35bd71d1734c151311c3.html#a496f8e8982ec35bd71d1734c151311c3) |
|  | |
| - Public 属性 继承自 [AkFileOpenData](struct_ak_file_open_data.html) | |
| const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \* | [pszFileName](struct_ak_file_open_data_a18974496890d6480cbb45a5dd772c525.html#a18974496890d6480cbb45a5dd772c525) |
|  | File name. Only one of pszFileName or fileID should be valid (pszFileName null while fileID is not AK\_INVALID\_FILE\_ID, or vice versa) [更多...](struct_ak_file_open_data_a18974496890d6480cbb45a5dd772c525.html#a18974496890d6480cbb45a5dd772c525) |
|  | |
| [AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) | [fileID](struct_ak_file_open_data_adde8223afb125eee82420b3314f944a3.html#adde8223afb125eee82420b3314f944a3) |
|  | File ID. Only one of pszFileName or fileID should be valid (pszFileName null while fileID is not AK\_INVALID\_FILE\_ID, or vice versa) [更多...](struct_ak_file_open_data_adde8223afb125eee82420b3314f944a3.html#adde8223afb125eee82420b3314f944a3) |
|  | |
| [AkFileSystemFlags](struct_ak_file_system_flags.html) \* | [pFlags](struct_ak_file_open_data_a41c41a23a7d7f4fa298c5400329b685a.html#a41c41a23a7d7f4fa298c5400329b685a) |
|  | Flags for opening, null when unused [更多...](struct_ak_file_open_data_a41c41a23a7d7f4fa298c5400329b685a.html#a41c41a23a7d7f4fa298c5400329b685a) |
|  | |
| [AkOpenMode](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7) | [eOpenMode](struct_ak_file_open_data_aca6d02f7cc6b7c13a240defcfeb7bbb0.html#aca6d02f7cc6b7c13a240defcfeb7bbb0) |
|  | Open mode. [更多...](struct_ak_file_open_data_aca6d02f7cc6b7c13a240defcfeb7bbb0.html#aca6d02f7cc6b7c13a240defcfeb7bbb0) |
|  | |

## 详细描述

Structure used by Low Level IO Hooks (IAkLowLevelIOHook) to pass and retreive information on files to be opened by the IO hook. Please see [AK::StreamMgr::IAkLowLevelIOHook::BatchOpen](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a0abfde848b599b5e5b8e8ed63dc8b555.html#a0abfde848b599b5e5b8e8ed63dc8b555) for more information about the sementics of the Open operation.

参见
:   - [AkFileOpenData](struct_ak_file_open_data.html)
    - [AK::StreamMgr::IAkLowLevelIOHook::BatchOpen](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a0abfde848b599b5e5b8e8ed63dc8b555.html#a0abfde848b599b5e5b8e8ed63dc8b555)

在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [143](_ak_stream_mgr_module_8h_source.html#l00143) 行定义.