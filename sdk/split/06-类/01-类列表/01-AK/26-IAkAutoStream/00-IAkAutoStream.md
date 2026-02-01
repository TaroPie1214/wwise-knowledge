# IAkAutoStream

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkAutoStream](class_a_k_1_1_i_ak_auto_stream.html)

[所有成员列表](class_a_k_1_1_i_ak_auto_stream-members.html) |
[Protected 成员函数](#pro-methods)

AK::IAkAutoStream类 参考abstract

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| Stream management, settings access, and run-time change. | |
| virtual void | [Destroy](class_a_k_1_1_i_ak_auto_stream_a7371eb45a24988fc3d5372bc15c77db7.html#a7371eb45a24988fc3d5372bc15c77db7) ()=0 |
|  | |
| virtual void | [GetInfo](class_a_k_1_1_i_ak_auto_stream_a345fdbb2d4551f048727bc66f58eb80f.html#a345fdbb2d4551f048727bc66f58eb80f) ([AkStreamInfo](struct_ak_stream_info.html) &out\_info)=0 |
|  | |
| virtual void \* | [GetFileDescriptor](class_a_k_1_1_i_ak_auto_stream_a3908927522de508f8ea5d0d1a4cd5101.html#a3908927522de508f8ea5d0d1a4cd5101) ()=0 |
|  | |
| virtual void | [GetHeuristics](class_a_k_1_1_i_ak_auto_stream_a8017b864cb413b545e685b2fa1acfe65.html#a8017b864cb413b545e685b2fa1acfe65) ([AkAutoStmHeuristics](struct_ak_auto_stm_heuristics.html) &out\_heuristics)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetHeuristics](class_a_k_1_1_i_ak_auto_stream_a0991f4a2b25e6c2fcf5fc4e04cfeaebc.html#a0991f4a2b25e6c2fcf5fc4e04cfeaebc) (const [AkAutoStmHeuristics](struct_ak_auto_stm_heuristics.html) &in\_heuristics)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetMinimalBufferSize](class_a_k_1_1_i_ak_auto_stream_aa6578f7625c60b34b014fff484561feb.html#aa6578f7625c60b34b014fff484561feb) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uMinBufferSize)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetStreamName](class_a_k_1_1_i_ak_auto_stream_aea3747ae927ba05ebdc9eabdabe3c0c1.html#aea3747ae927ba05ebdc9eabdabe3c0c1) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszStreamName)=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetBlockSize](class_a_k_1_1_i_ak_auto_stream_a6869aba1d6b9301a3f59468166a8fb7c.html#a6869aba1d6b9301a3f59468166a8fb7c) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [QueryBufferingStatus](class_a_k_1_1_i_ak_auto_stream_a34793515f3d57ed32f4622173d010100.html#a34793515f3d57ed32f4622173d010100) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uNumBytesAvailable)=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetNominalBuffering](class_a_k_1_1_i_ak_auto_stream_a3e65a6d3795b3440c408ef89ecbfc069.html#a3e65a6d3795b3440c408ef89ecbfc069) ()=0 |
|  | |
| Stream operations. | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Start](class_a_k_1_1_i_ak_auto_stream_ae9d58aa42a893863f8fe85a5ee45d638.html#ae9d58aa42a893863f8fe85a5ee45d638) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Stop](class_a_k_1_1_i_ak_auto_stream_ad1b80ad36a23b15e96f697685f710b1f.html#ad1b80ad36a23b15e96f697685f710b1f) ()=0 |
|  | |
| virtual [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [GetPosition](class_a_k_1_1_i_ak_auto_stream_ae7fa6bd56c493b906e294618b47be39e.html#ae7fa6bd56c493b906e294618b47be39e) (bool \*out\_pbEndOfStream)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetPosition](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38) ([AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) in\_iMoveOffset, [AkMoveMethod](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865) in\_eMoveMethod)=0 |
|  | |
| Data/status access. | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetBuffer](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) (void \*&out\_pBuffer, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uSize, bool in\_bWait)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ReleaseBuffer](class_a_k_1_1_i_ak_auto_stream_a4676200056afb266b730f25d5262d2c8.html#a4676200056afb266b730f25d5262d2c8) ()=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkAutoStream](class_a_k_1_1_i_ak_auto_stream_a75a6472667063a0b8724107ab99440a8.html#a75a6472667063a0b8724107ab99440a8) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_auto_stream_a75a6472667063a0b8724107ab99440a8.html#a75a6472667063a0b8724107ab99440a8) |
|  | |

## 详细描述

Interface of automatic streams. It is used as a handle to a stream, I/O operations are triggered from here. Obtained through the Stream Manager's [AK::IAkStreamMgr::CreateAuto()](class_a_k_1_1_i_ak_stream_mgr_afe30a576bd859ff4e9b60a3f8e1710fb.html#afe30a576bd859ff4e9b60a3f8e1710fb) method.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

参见
:   - [流播放/流管理器](streamingdevicemanager.html)

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [521](_i_ak_stream_mgr_8h_source.html#l00521) 行定义.