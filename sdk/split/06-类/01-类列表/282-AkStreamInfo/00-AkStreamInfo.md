# AkStreamInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_stream_info-members.html) |
[Public 属性](#pub-attribs)

AkStreamInfo结构体 参考

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) | [deviceID](struct_ak_stream_info_a3f5cd7cccaf0d10ab3994e1abee6e8ff.html#a3f5cd7cccaf0d10ab3994e1abee6e8ff) |
|  | Device ID [更多...](struct_ak_stream_info_a3f5cd7cccaf0d10ab3994e1abee6e8ff.html#a3f5cd7cccaf0d10ab3994e1abee6e8ff) |
|  | |
| const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \* | [pszName](struct_ak_stream_info_a1d84316be473795ac54b6da4cbc0adf5.html#a1d84316be473795ac54b6da4cbc0adf5) |
|  | User-defined stream name (specified through [AK::IAkStdStream::SetStreamName()](class_a_k_1_1_i_ak_std_stream_a95c36cbf662e531c10f90165de1fd576.html#a95c36cbf662e531c10f90165de1fd576) or [AK::IAkAutoStream::SetStreamName()](class_a_k_1_1_i_ak_auto_stream_aea3747ae927ba05ebdc9eabdabe3c0c1.html#aea3747ae927ba05ebdc9eabdabe3c0c1)) [更多...](struct_ak_stream_info_a1d84316be473795ac54b6da4cbc0adf5.html#a1d84316be473795ac54b6da4cbc0adf5) |
|  | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uSize](struct_ak_stream_info_aa350fbeb216793ac822d5521df98eccf.html#aa350fbeb216793ac822d5521df98eccf) |
|  | Total stream/file size in bytes [更多...](struct_ak_stream_info_aa350fbeb216793ac822d5521df98eccf.html#aa350fbeb216793ac822d5521df98eccf) |
|  | |
| bool | [bIsOpen](struct_ak_stream_info_ade9b563f0cfd607e6b7991862e3634b0.html#ade9b563f0cfd607e6b7991862e3634b0) |
|  | True when the file is open (implementations may defer file opening) [更多...](struct_ak_stream_info_ade9b563f0cfd607e6b7991862e3634b0.html#ade9b563f0cfd607e6b7991862e3634b0) |
|  | |
| bool | [bIsLanguageSpecific](struct_ak_stream_info_a6e1db16a374a9c600265f5817f680cee.html#a6e1db16a374a9c600265f5817f680cee) |
|  | True when the file was found in a language specific location [更多...](struct_ak_stream_info_a6e1db16a374a9c600265f5817f680cee.html#a6e1db16a374a9c600265f5817f680cee) |
|  | |

## 详细描述

Stream information.

参见
:   - [AK::IAkStdStream::GetInfo()](class_a_k_1_1_i_ak_std_stream_a744adfcaf87eb5bf4962dbf4556a6201.html#a744adfcaf87eb5bf4962dbf4556a6201)
    - [AK::IAkAutoStream::GetInfo()](class_a_k_1_1_i_ak_auto_stream_a345fdbb2d4551f048727bc66f58eb80f.html#a345fdbb2d4551f048727bc66f58eb80f)

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [84](_i_ak_stream_mgr_8h_source.html#l00084) 行定义.