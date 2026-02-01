# RequestedHostInterface&lt; FrontendModel &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< FrontendModel >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< FrontendModel >类 参考

`#include <HostFrontendModel.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< FrontendModel > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4_a75d2de4f24814d36432cdfc4e60f854a.html#a75d2de4f24814d36432cdfc4e60f854a) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< FrontendModel, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4_a27e048c16f130f38db6bd3f96b0253a4.html#a27e048c16f130f38db6bd3f96b0253a4) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb) ::Interface & | [g\_frontendModelInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4_ae6db1f88379847865a0185d4fb792c30.html#ae6db1f88379847865a0185d4fb792c30) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| HostInterfaceDefinition::Instance & | [m\_frontendModel](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4_a43347228a10a3c5261e1377d2b9d5791.html#a43347228a10a3c5261e1377d2b9d5791) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< FrontendModel, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [HostFrontendModel.h](_host_frontend_model_8h_source.html) 第 [500](_host_frontend_model_8h_source.html#l00500) 行定义.