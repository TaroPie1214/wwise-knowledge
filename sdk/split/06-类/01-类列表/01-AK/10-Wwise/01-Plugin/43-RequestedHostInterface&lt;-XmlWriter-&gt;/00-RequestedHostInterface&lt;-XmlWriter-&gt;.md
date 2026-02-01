# RequestedHostInterface&lt; XmlWriter &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< XmlWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_writer_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_writer_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< XmlWriter >类 参考

`#include <HostXml.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< XmlWriter > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_writer_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_writer_01_4_af12c3231db9201558330d88936a8dd3f.html#af12c3231db9201558330d88936a8dd3f) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [XmlWriter](namespace_a_k_1_1_wwise_1_1_plugin_a3917bff28ad1858f6fca96f72f064792.html#a3917bff28ad1858f6fca96f72f064792), false > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< XmlWriter, false >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [XmlWriter](namespace_a_k_1_1_wwise_1_1_plugin_a3917bff28ad1858f6fca96f72f064792.html#a3917bff28ad1858f6fca96f72f064792) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_writer_01_4_aebfa760e215925ef9532e8d358440daa.html#aebfa760e215925ef9532e8d358440daa) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [XmlWriter](namespace_a_k_1_1_wwise_1_1_plugin_a3917bff28ad1858f6fca96f72f064792.html#a3917bff28ad1858f6fca96f72f064792) ::Interface & | [g\_xmlTextWriterInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_writer_01_4_a20847f4288590959978cc9991eed86fd.html#a20847f4288590959978cc9991eed86fd) = HostInterfaceDefinition::g\_cppinterface |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< XmlWriter, false >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [HostXml.h](_host_xml_8h_source.html) 第 [941](_host_xml_8h_source.html#l00941) 行定义.