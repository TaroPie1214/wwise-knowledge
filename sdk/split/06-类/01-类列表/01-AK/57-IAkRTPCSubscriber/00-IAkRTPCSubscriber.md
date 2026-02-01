# IAkRTPCSubscriber

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkRTPCSubscriber](class_a_k_1_1_i_ak_r_t_p_c_subscriber.html)

[所有成员列表](class_a_k_1_1_i_ak_r_t_p_c_subscriber-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkRTPCSubscriber类 参考abstract

`#include <IAkRTPCSubscriber.h>`

类 AK::IAkRTPCSubscriber 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_r_t_p_c_subscriber.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetParam](class_a_k_1_1_i_ak_r_t_p_c_subscriber_a93a2b097a6e34482c7381f388e500ff0.html#a93a2b097a6e34482c7381f388e500ff0) ([AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_paramID, const void \*in\_pParam, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uParamSize)=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkRTPCSubscriber](class_a_k_1_1_i_ak_r_t_p_c_subscriber_a4c061df60a4e69355ee377e9643e4a12.html#a4c061df60a4e69355ee377e9643e4a12) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_r_t_p_c_subscriber_a4c061df60a4e69355ee377e9643e4a12.html#a4c061df60a4e69355ee377e9643e4a12) |
|  | |

## 详细描述

Real-Time Parameter Control Subscriber interface. This interface must be implemented by every [AK::IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html) implementation, allowing real-time editing with [Wwise](namespace_a_k_1_1_wwise.html) and in-game RTPC control.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

参见
:   - [AK::IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html)

在文件 [IAkRTPCSubscriber.h](_i_ak_r_t_p_c_subscriber_8h_source.html) 第 [47](_i_ak_r_t_p_c_subscriber_8h_source.html#l00047) 行定义.