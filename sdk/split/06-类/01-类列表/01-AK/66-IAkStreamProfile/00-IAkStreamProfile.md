# IAkStreamProfile

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkStreamProfile](class_a_k_1_1_i_ak_stream_profile.html)

[所有成员列表](class_a_k_1_1_i_ak_stream_profile-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkStreamProfile类 参考abstract

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [GetStreamRecord](class_a_k_1_1_i_ak_stream_profile_a7498cfb30b654484f4e2e6c8551a33a8.html#a7498cfb30b654484f4e2e6c8551a33a8) ([AkStreamRecord](struct_ak_stream_record.html) &out\_streamRecord)=0 |
|  | |
| virtual void | [GetStreamData](class_a_k_1_1_i_ak_stream_profile_a166b66baf10ba7473d002e77be2b8d18.html#a166b66baf10ba7473d002e77be2b8d18) ([AkStreamData](struct_ak_stream_data.html) &out\_streamData)=0 |
|  | |
| virtual bool | [IsNew](class_a_k_1_1_i_ak_stream_profile_a417ca1dc7e43aaf09a8179c901cd48b5.html#a417ca1dc7e43aaf09a8179c901cd48b5) ()=0 |
|  | |
| virtual void | [ClearNew](class_a_k_1_1_i_ak_stream_profile_a9b044746082a474b911738bfe6a07548.html#a9b044746082a474b911738bfe6a07548) ()=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkStreamProfile](class_a_k_1_1_i_ak_stream_profile_a3de7b7c4732e2016dd26dd80fe6cf20e.html#a3de7b7c4732e2016dd26dd80fe6cf20e) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_stream_profile_a3de7b7c4732e2016dd26dd80fe6cf20e.html#a3de7b7c4732e2016dd26dd80fe6cf20e) |
|  | |

## 详细描述

Profiling interface of streams.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [244](_i_ak_stream_mgr_8h_source.html#l00244) 行定义.