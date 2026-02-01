# IAkDeviceProfile

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkDeviceProfile](class_a_k_1_1_i_ak_device_profile.html)

[所有成员列表](class_a_k_1_1_i_ak_device_profile-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkDeviceProfile类 参考abstract

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [OnProfileStart](class_a_k_1_1_i_ak_device_profile_a3236d31fe8ae07db691b938e976383a0.html#a3236d31fe8ae07db691b938e976383a0) ()=0 |
|  | Notify device when monitor sampling starts. [更多...](class_a_k_1_1_i_ak_device_profile_a3236d31fe8ae07db691b938e976383a0.html#a3236d31fe8ae07db691b938e976383a0) |
|  | |
| virtual void | [OnProfileEnd](class_a_k_1_1_i_ak_device_profile_adde969b88c91969f6a8dd198009ebd3a.html#adde969b88c91969f6a8dd198009ebd3a) ()=0 |
|  | Notify device when monitor sampling ends. [更多...](class_a_k_1_1_i_ak_device_profile_adde969b88c91969f6a8dd198009ebd3a.html#adde969b88c91969f6a8dd198009ebd3a) |
|  | |
| virtual void | [GetDesc](class_a_k_1_1_i_ak_device_profile_ac6156ee5993860f06ad8cc7b2e9c480a.html#ac6156ee5993860f06ad8cc7b2e9c480a) ([AkDeviceDesc](struct_ak_device_desc.html) &out\_deviceDesc)=0 |
|  | |
| virtual void | [GetData](class_a_k_1_1_i_ak_device_profile_ad60791b20a2111308512afd80cb43db8.html#ad60791b20a2111308512afd80cb43db8) ([AkDeviceData](struct_ak_device_data.html) &out\_deviceData)=0 |
|  | |
| virtual bool | [IsNew](class_a_k_1_1_i_ak_device_profile_a252a93df3b2655a3abcfc5f361953621.html#a252a93df3b2655a3abcfc5f361953621) ()=0 |
|  | |
| virtual void | [ClearNew](class_a_k_1_1_i_ak_device_profile_a868838cddbbf8f9f741bf75b906b3874.html#a868838cddbbf8f9f741bf75b906b3874) ()=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetNumStreams](class_a_k_1_1_i_ak_device_profile_a06f29f706cb2dcf7ae39c9327959b435.html#a06f29f706cb2dcf7ae39c9327959b435) ()=0 |
|  | |
| virtual [IAkStreamProfile](class_a_k_1_1_i_ak_stream_profile.html) \* | [GetStreamProfile](class_a_k_1_1_i_ak_device_profile_a02f8de69c4bf444085cbaf0433bd825a.html#a02f8de69c4bf444085cbaf0433bd825a) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uStreamIndex)=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkDeviceProfile](class_a_k_1_1_i_ak_device_profile_ab6407bfdc2db7e687db6a575205dc965.html#ab6407bfdc2db7e687db6a575205dc965) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_device_profile_ab6407bfdc2db7e687db6a575205dc965.html#ab6407bfdc2db7e687db6a575205dc965) |
|  | |

## 详细描述

Profiling interface of high-level I/O devices.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [282](_i_ak_stream_mgr_8h_source.html#l00282) 行定义.