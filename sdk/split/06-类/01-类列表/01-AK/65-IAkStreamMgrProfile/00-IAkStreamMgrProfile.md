# IAkStreamMgrProfile

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkStreamMgrProfile](class_a_k_1_1_i_ak_stream_mgr_profile.html)

[所有成员列表](class_a_k_1_1_i_ak_stream_mgr_profile-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkStreamMgrProfile类 参考abstract

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [StartMonitoring](class_a_k_1_1_i_ak_stream_mgr_profile_a66cae38e39771bef15100d112feab413.html#a66cae38e39771bef15100d112feab413) ()=0 |
|  | |
| virtual void | [StopMonitoring](class_a_k_1_1_i_ak_stream_mgr_profile_a32895a4a3fae7449e2c73d7bc7ffc3a6.html#a32895a4a3fae7449e2c73d7bc7ffc3a6) ()=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetNumDevices](class_a_k_1_1_i_ak_stream_mgr_profile_a7260fd56a4eac4e8cf299ed92ed658e5.html#a7260fd56a4eac4e8cf299ed92ed658e5) ()=0 |
|  | |
| virtual [IAkDeviceProfile](class_a_k_1_1_i_ak_device_profile.html) \* | [GetDeviceProfile](class_a_k_1_1_i_ak_stream_mgr_profile_ac8280a0212698611fcc5f4b173c21832.html#ac8280a0212698611fcc5f4b173c21832) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uDeviceIndex)=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkStreamMgrProfile](class_a_k_1_1_i_ak_stream_mgr_profile_a94a400d58854ab89784956eb99ebb86b.html#a94a400d58854ab89784956eb99ebb86b) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_stream_mgr_profile_a94a400d58854ab89784956eb99ebb86b.html#a94a400d58854ab89784956eb99ebb86b) |
|  | |

## 详细描述

Profiling interface of the Stream Manager.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [340](_i_ak_stream_mgr_8h_source.html#l00340) 行定义.