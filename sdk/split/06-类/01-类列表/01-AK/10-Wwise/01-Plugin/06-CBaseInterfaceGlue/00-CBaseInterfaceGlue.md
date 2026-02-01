# CBaseInterfaceGlue

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [CBaseInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue-members.html) |
[Public 类型](#pub-types) |
[静态 Public 属性](#pub-static-attribs)

AK.Wwise::Plugin::CBaseInterfaceGlue< CInterface > 模板类 参考

[PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): For each plug-in interface type, provides a single static instance used throughout this plug-in container.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html#details)

`#include <PluginInfoGenerator.h>`

类 AK.Wwise::Plugin::CBaseInterfaceGlue< CInterface > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = CInterface |
|  | |

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) = nullptr |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

### template<typename CInterface> class AK.Wwise::Plugin::CBaseInterfaceGlue< CInterface >

[PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): For each plug-in interface type, provides a single static instance used throughout this plug-in container.

This uses a C++ template principle where you can define a static variable inside a templated class, and you can have the compiler generate one unique static instance for each individual templated class.

Also, having a class outer shell means the static member can reside in a header and be instantiated in that same header without the linker refusing multiple definitions.

模板参数
:   |  |  |
    | --- | --- |
    | CInterface | Which interface (In C) |

参见
:   - [AK::Wwise::Plugin::PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [85](_plugin_info_generator_8h_source.html#l00085) 行定义.