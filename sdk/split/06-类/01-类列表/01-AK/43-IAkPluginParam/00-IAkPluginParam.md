# IAkPluginParam

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_param-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 属性](#pub-static-attribs) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginParam类 参考abstract

`#include <IAkPlugin.h>`

类 AK::IAkPluginParam 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_param.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html) \* | [Clone](class_a_k_1_1_i_ak_plugin_param_a606e850fa44ca597e0f1b9c6ad5f32cb.html#a606e850fa44ca597e0f1b9c6ad5f32cb) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](class_a_k_1_1_i_ak_plugin_param_ab432d055afc355a17121ac2afdcd5639.html#ab432d055afc355a17121ac2afdcd5639) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, const void \*in\_pParamsBlock, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uBlockSize)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Term](class_a_k_1_1_i_ak_plugin_param_ad558bb7f45851dc57b1bbf34ef74cd48.html#ad558bb7f45851dc57b1bbf34ef74cd48) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetParamsBlock](class_a_k_1_1_i_ak_plugin_param_ae186f2f0aa56fe0e52ab1c2218df2c7c.html#ae186f2f0aa56fe0e52ab1c2218df2c7c) (const void \*in\_pParamsBlock, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uBlockSize)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetParam](class_a_k_1_1_i_ak_plugin_param_ad47732326b85527316287e923d37a3e1.html#ad47732326b85527316287e923d37a3e1) ([AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_paramID, const void \*in\_pValue, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uParamSize)=0 |
|  | |

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static const [AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) | [ALL\_PLUGIN\_DATA\_ID](class_a_k_1_1_i_ak_plugin_param_a7d4422a73ca832f64edc0465e59be771.html#a7d4422a73ca832f64edc0465e59be771) = 0x7FFF |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginParam](class_a_k_1_1_i_ak_plugin_param_a53cabae3b0052b34f68c973344724e33.html#a53cabae3b0052b34f68c973344724e33) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_param_a53cabae3b0052b34f68c973344724e33.html#a53cabae3b0052b34f68c973344724e33) |
|  | |
| - Protected 成员函数 继承自 [AK::IAkRTPCSubscriber](class_a_k_1_1_i_ak_r_t_p_c_subscriber.html) | |
| virtual | [~IAkRTPCSubscriber](class_a_k_1_1_i_ak_r_t_p_c_subscriber_a4c061df60a4e69355ee377e9643e4a12.html#a4c061df60a4e69355ee377e9643e4a12) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_r_t_p_c_subscriber_a4c061df60a4e69355ee377e9643e4a12.html#a4c061df60a4e69355ee377e9643e4a12) |
|  | |

## 详细描述

Parameter node interface, managing access to an enclosed parameter structure.

|  |  |
| --- | --- |
|  | **备注:** The implementer of this interface should also expose a static creation function that will return a new parameter node instance when required (see [声音引擎插件概述](soundengine_plugins.html#se_plugins_overview)). |

参见
:   - [参数节点接口的实现](soundengine_plugins.html#shared_parameter_interface)

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [708](_i_ak_plugin_8h_source.html#l00708) 行定义.