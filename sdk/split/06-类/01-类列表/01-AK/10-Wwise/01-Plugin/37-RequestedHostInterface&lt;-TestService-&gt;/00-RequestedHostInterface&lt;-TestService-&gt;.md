# RequestedHostInterface&lt; TestService &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< TestService >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_test_service_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_test_service_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< TestService >类 参考

`#include <TestService.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< TestService > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_test_service_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_test_service_01_4_a569584156c28bb17b349b19295d4d80e.html#a569584156c28bb17b349b19295d4d80e) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [TestService](namespace_a_k_1_1_wwise_1_1_plugin_a49755cf687541087df2007b0303785de.html#a49755cf687541087df2007b0303785de), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< TestService, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [TestService](namespace_a_k_1_1_wwise_1_1_plugin_a49755cf687541087df2007b0303785de.html#a49755cf687541087df2007b0303785de) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_test_service_01_4_a2480da46e882b15e7f41091405827961.html#a2480da46e882b15e7f41091405827961) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [TestService](namespace_a_k_1_1_wwise_1_1_plugin_a49755cf687541087df2007b0303785de.html#a49755cf687541087df2007b0303785de) ::Interface & | [g\_testServiceInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_test_service_01_4_aa959610c6dfe236f8b8f2bcd03df7fb9.html#aa959610c6dfe236f8b8f2bcd03df7fb9) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| [HostInterfaceDefinition::Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) & | [m\_testService](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_test_service_01_4_abdf952f528d11a289f5db2dcc6051f8e.html#abdf952f528d11a289f5db2dcc6051f8e) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< TestService, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [TestService.h](_test_service_8h_source.html) 第 [116](_test_service_8h_source.html#l00116) 行定义.