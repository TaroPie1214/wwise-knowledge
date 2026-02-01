# RequestedHostInterface&lt; UndoManager &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< UndoManager >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_undo_manager_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_undo_manager_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< UndoManager >类 参考

`#include <HostUndoManager.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< UndoManager > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_undo_manager_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_undo_manager_01_4_ab058aceead79032bf0e260691ae9672f.html#ab058aceead79032bf0e260691ae9672f) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [UndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< UndoManager, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [UndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_undo_manager_01_4_a12df9f867524479b55b95f8abe4c88dd.html#a12df9f867524479b55b95f8abe4c88dd) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [UndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b) ::Interface & | [g\_undoManagerInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_undo_manager_01_4_a8e7a650a373d62d7dfd2d28f0513388a.html#a8e7a650a373d62d7dfd2d28f0513388a) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| [HostInterfaceDefinition::Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) & | [m\_undoManager](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_undo_manager_01_4_a5b98a895b8ecce8487b89066715690aa.html#a5b98a895b8ecce8487b89066715690aa) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< UndoManager, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [HostUndoManager.h](_host_undo_manager_8h_source.html) 第 [653](_host_undo_manager_8h_source.html#l00653) 行定义.