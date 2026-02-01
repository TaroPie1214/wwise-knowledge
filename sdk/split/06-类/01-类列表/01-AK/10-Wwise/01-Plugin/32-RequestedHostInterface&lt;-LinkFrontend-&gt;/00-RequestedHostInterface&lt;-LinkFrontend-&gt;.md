# RequestedHostInterface&lt; LinkFrontend &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< LinkFrontend >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_frontend_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_frontend_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< LinkFrontend >类 参考

`#include <PluginLinks.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< LinkFrontend > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_frontend_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_frontend_01_4_aeec4bce9ffac4f2311d8c1b45c526973.html#aeec4bce9ffac4f2311d8c1b45c526973) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [LinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_a54cf853c2d54b39672aa929f71b0c0c3.html#a54cf853c2d54b39672aa929f71b0c0c3), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< LinkFrontend, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [LinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_a54cf853c2d54b39672aa929f71b0c0c3.html#a54cf853c2d54b39672aa929f71b0c0c3) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_frontend_01_4_a94100e13a70baa0be3ce80ed8b9a46e8.html#a94100e13a70baa0be3ce80ed8b9a46e8) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [LinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_a54cf853c2d54b39672aa929f71b0c0c3.html#a54cf853c2d54b39672aa929f71b0c0c3) ::Interface & | [g\_frontendInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_frontend_01_4_ad791c74b2641b708e2952d234dbfc107.html#ad791c74b2641b708e2952d234dbfc107) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| [HostInterfaceDefinition::Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) & | [m\_frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_frontend_01_4_a4c094d10e3de939e24647b1323153758.html#a4c094d10e3de939e24647b1323153758) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< LinkFrontend, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [286](_plugin_links_8h_source.html#l00286) 行定义.