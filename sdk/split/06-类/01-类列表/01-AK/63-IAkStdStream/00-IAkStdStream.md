# IAkStdStream

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkStdStream](class_a_k_1_1_i_ak_std_stream.html)

[所有成员列表](class_a_k_1_1_i_ak_std_stream-members.html) |
[Protected 成员函数](#pro-methods)

AK::IAkStdStream类 参考abstract

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| Stream management and settings. | |
| virtual void | [Destroy](class_a_k_1_1_i_ak_std_stream_aaa6bca57f4a01a98dff95f68b1320403.html#aaa6bca57f4a01a98dff95f68b1320403) ()=0 |
|  | |
| virtual void | [GetInfo](class_a_k_1_1_i_ak_std_stream_a744adfcaf87eb5bf4962dbf4556a6201.html#a744adfcaf87eb5bf4962dbf4556a6201) ([AkStreamInfo](struct_ak_stream_info.html) &out\_info)=0 |
|  | |
| virtual void \* | [GetFileDescriptor](class_a_k_1_1_i_ak_std_stream_a261f081bbf442b301c975175e900401a.html#a261f081bbf442b301c975175e900401a) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetStreamName](class_a_k_1_1_i_ak_std_stream_a95c36cbf662e531c10f90165de1fd576.html#a95c36cbf662e531c10f90165de1fd576) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszStreamName)=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetBlockSize](class_a_k_1_1_i_ak_std_stream_a1121f1b371a613e020d38b99e65e7a2b.html#a1121f1b371a613e020d38b99e65e7a2b) ()=0 |
|  | |
| I/O operations. | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Read](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d) (void \*in\_pBuffer, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uReqSize, bool in\_bWait, [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) in\_priority, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fDeadline, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uSize)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Write](class_a_k_1_1_i_ak_std_stream_af983e5aec5edd20b88a6b01e466d8779.html#af983e5aec5edd20b88a6b01e466d8779) (void \*in\_pBuffer, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uReqSize, bool in\_bWait, [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) in\_priority, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fDeadline, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uSize)=0 |
|  | |
| virtual [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [GetPosition](class_a_k_1_1_i_ak_std_stream_a7d43a89fb7bc5db13285a2669ec912fa.html#a7d43a89fb7bc5db13285a2669ec912fa) (bool \*out\_pbEndOfStream)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetPosition](class_a_k_1_1_i_ak_std_stream_a5d0c3c6c525a882d89558b1aae485360.html#a5d0c3c6c525a882d89558b1aae485360) ([AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) in\_iMoveOffset, [AkMoveMethod](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865) in\_eMoveMethod)=0 |
|  | |
| virtual void | [Cancel](class_a_k_1_1_i_ak_std_stream_a12c0a90ec223f7d03d265094b0319c88.html#a12c0a90ec223f7d03d265094b0319c88) ()=0 |
|  | |
| Access to data and status. | |
| virtual void \* | [GetData](class_a_k_1_1_i_ak_std_stream_ac5726fc41a0e0f9f05d262a85b200909.html#ac5726fc41a0e0f9f05d262a85b200909) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uSize)=0 |
|  | |
| virtual [AkStmStatus](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307) | [GetStatus](class_a_k_1_1_i_ak_std_stream_a165ff91b84857e73891f7943261ba275.html#a165ff91b84857e73891f7943261ba275) ()=0 |
|  | |
| virtual [AkStmStatus](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307) | [WaitForPendingOperation](class_a_k_1_1_i_ak_std_stream_ac1dbc6c6e84ef70c877544545c45007b.html#ac1dbc6c6e84ef70c877544545c45007b) ()=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkStdStream](class_a_k_1_1_i_ak_std_stream_a0c759af7c12b920b958b0937ad5e1867.html#a0c759af7c12b920b958b0937ad5e1867) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_std_stream_a0c759af7c12b920b958b0937ad5e1867.html#a0c759af7c12b920b958b0937ad5e1867) |
|  | |

## 详细描述

Interface of standard streams. Used as a handle to a standard stream. Has methods for stream control. Obtained through the Stream Manager's [AK::IAkStreamMgr::CreateStd()](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6) method.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [383](_i_ak_stream_mgr_8h_source.html#l00383) 行定义.