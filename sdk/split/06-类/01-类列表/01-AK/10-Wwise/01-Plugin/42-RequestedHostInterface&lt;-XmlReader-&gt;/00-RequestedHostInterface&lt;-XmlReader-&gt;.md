# RequestedHostInterface&lt; XmlReader &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< XmlReader >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< XmlReader >类 参考

`#include <HostXml.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< XmlReader > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4_ad30065a0e1e0e8736167b494f4a2fa65.html#ad30065a0e1e0e8736167b494f4a2fa65) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150), false > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< XmlReader, false >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4_ad997b41806fb4df1cf9126e851389bff.html#ad997b41806fb4df1cf9126e851389bff) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150) ::Interface & | [g\_xmlTextReaderInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4_a32a42c8fc228d083337c9b70e194729f.html#a32a42c8fc228d083337c9b70e194729f) = HostInterfaceDefinition::g\_cppinterface |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< XmlReader, false >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [HostXml.h](_host_xml_8h_source.html) 第 [940](_host_xml_8h_source.html#l00940) 行定义.