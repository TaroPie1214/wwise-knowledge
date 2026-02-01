# RequestedHostInterface&lt; LinkBackend &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< LinkBackend >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_backend_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_backend_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< LinkBackend >类 参考

`#include <PluginLinks.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< LinkBackend > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_backend_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_backend_01_4_a1490ef0dd16a106c3e1d0a355e2603ac.html#a1490ef0dd16a106c3e1d0a355e2603ac) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [LinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_a3b9372eb28f4ed69d52c8b253b7542fd.html#a3b9372eb28f4ed69d52c8b253b7542fd), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< LinkBackend, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [LinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_a3b9372eb28f4ed69d52c8b253b7542fd.html#a3b9372eb28f4ed69d52c8b253b7542fd) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_backend_01_4_abac3bc463ae5b2d0acd4908085a7d991.html#abac3bc463ae5b2d0acd4908085a7d991) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [LinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_a3b9372eb28f4ed69d52c8b253b7542fd.html#a3b9372eb28f4ed69d52c8b253b7542fd) ::Interface & | [g\_backendInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_backend_01_4_a5747f969d7aab1c9ed03cb8a2ac82594.html#a5747f969d7aab1c9ed03cb8a2ac82594) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| HostInterfaceDefinition::Instance & | [m\_backend](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_backend_01_4_a1ac0a4e980ca1209417d20a2f435ce47.html#a1ac0a4e980ca1209417d20a2f435ce47) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< LinkBackend, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [285](_plugin_links_8h_source.html#l00285) 行定义.