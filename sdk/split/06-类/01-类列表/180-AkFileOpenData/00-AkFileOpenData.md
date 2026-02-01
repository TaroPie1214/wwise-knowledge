# AkFileOpenData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_file_open_data-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkFileOpenData结构体 参考

`#include <IAkStreamMgr.h>`

类 AkFileOpenData 继承关系图:

![](../../../images/struct_ak_file_open_data.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
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

Contains parameters for the [IAkFileLocationResolver::Open()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc) call and related functions. Files can be designated with a file name or a file ID. Only one of the two members should be valid.

注解
:   pszFileName is stored on the stack and will be valid only through the function call.

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [188](_i_ak_stream_mgr_8h_source.html#l00188) 行定义.