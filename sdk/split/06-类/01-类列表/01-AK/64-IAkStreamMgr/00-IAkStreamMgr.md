# IAkStreamMgr

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html)

[所有成员列表](class_a_k_1_1_i_ak_stream_mgr-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkStreamMgr类 参考abstract

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [Destroy](class_a_k_1_1_i_ak_stream_mgr_ab846904b7ad95752193cf0e9a288ea8a.html#ab846904b7ad95752193cf0e9a288ea8a) ()=0 |
|  | |
| Profiling. | |
| virtual [IAkStreamMgrProfile](class_a_k_1_1_i_ak_stream_mgr_profile.html) \* | [GetStreamMgrProfile](class_a_k_1_1_i_ak_stream_mgr_abce23f619236db5f03364d9447caec71.html#abce23f619236db5f03364d9447caec71) ()=0 |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static [IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html) \* | [Get](class_a_k_1_1_i_ak_stream_mgr_ac650db9915bd06d5eebc1852e0d0cd6e.html#ac650db9915bd06d5eebc1852e0d0cd6e) () |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr_a7cc382f272e80f165577d9214bcca85c.html#a7cc382f272e80f165577d9214bcca85c) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_stream_mgr_a7cc382f272e80f165577d9214bcca85c.html#a7cc382f272e80f165577d9214bcca85c) |
|  | |

|  |  |
| --- | --- |
| Stream creation interface. | |
| static [IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html) \* | [m\_pStreamMgr](class_a_k_1_1_i_ak_stream_mgr_a85c6043c1a45f13b7df2f05729248b1f.html#a85c6043c1a45f13b7df2f05729248b1f) |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [CreateStd](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6) (const [AkFileOpenData](struct_ak_file_open_data.html) &in\_FileOpen, [IAkStdStream](class_a_k_1_1_i_ak_std_stream.html) \*&out\_pStream, bool in\_bSyncOpen)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [CreateAuto](class_a_k_1_1_i_ak_stream_mgr_afe30a576bd859ff4e9b60a3f8e1710fb.html#afe30a576bd859ff4e9b60a3f8e1710fb) (const [AkFileOpenData](struct_ak_file_open_data.html) &in\_FileOpen, const [AkAutoStmHeuristics](struct_ak_auto_stm_heuristics.html) &in\_heuristics, [AkAutoStmBufSettings](struct_ak_auto_stm_buf_settings.html) \*in\_pBufferSettings, [IAkAutoStream](class_a_k_1_1_i_ak_auto_stream.html) \*&out\_pStream, bool in\_bSyncOpen, bool in\_bCaching=false)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [CreateAuto](class_a_k_1_1_i_ak_stream_mgr_a53253493732377e022adf3c82547bbd5.html#a53253493732377e022adf3c82547bbd5) (void \*in\_pBuffer, [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uSize, const [AkAutoStmHeuristics](struct_ak_auto_stm_heuristics.html) &in\_heuristics, [IAkAutoStream](class_a_k_1_1_i_ak_auto_stream.html) \*&out\_pStream)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [PinFileInCache](class_a_k_1_1_i_ak_stream_mgr_a702436773924b830729f94d609c62fc2.html#a702436773924b830729f94d609c62fc2) ([AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) in\_fileID, [AkFileSystemFlags](struct_ak_file_system_flags.html) \*in\_pFSFlags, [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) in\_uPriority)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [UnpinFileInCache](class_a_k_1_1_i_ak_stream_mgr_a47ee7a0b872d4703f64f0184097e6fed.html#a47ee7a0b872d4703f64f0184097e6fed) ([AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) in\_fileID, [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) in\_uPriority)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [UpdateCachingPriority](class_a_k_1_1_i_ak_stream_mgr_a959a8794ecf971eece797fabc0a7a4c9.html#a959a8794ecf971eece797fabc0a7a4c9) ([AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) in\_fileID, [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) in\_uPriority, [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) in\_uOldPriority)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetBufferStatusForPinnedFile](class_a_k_1_1_i_ak_stream_mgr_a98e0b89d39648ac3353537996d7767e2.html#a98e0b89d39648ac3353537996d7767e2) ([AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) in\_fileID, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_fPercentBuffered, bool &out\_bCacheFull)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [RelocateMemoryStream](class_a_k_1_1_i_ak_stream_mgr_a48995fb54560d607a9c1482a1922b2d1.html#a48995fb54560d607a9c1482a1922b2d1) ([IAkAutoStream](class_a_k_1_1_i_ak_auto_stream.html) \*in\_pStream, [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*in\_pNewStart)=0 |
|  | Make a memory stream point to a new area in memory, otherwise keeping the exact same state. [更多...](class_a_k_1_1_i_ak_stream_mgr_a48995fb54560d607a9c1482a1922b2d1.html#a48995fb54560d607a9c1482a1922b2d1) |
|  | |

## 详细描述

Interface of the Stream Manager.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [687](_i_ak_stream_mgr_8h_source.html#l00687) 行定义.