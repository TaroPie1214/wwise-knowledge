# CBaseInstanceGlue

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [CBaseInstanceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue-members.html) |
[Public 类型](#pub-types)

AK.Wwise::Plugin::CBaseInstanceGlue< CInterface, CInstance > 模板类 参考

[PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Associates an existing C Interface with a variable that can be used. Derives from the instance that uses it.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html#details)

`#include <PluginInfoGenerator.h>`

类 AK.Wwise::Plugin::CBaseInstanceGlue< CInterface, CInstance > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = CInstance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CInterface >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = CInterface |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CInterface >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) = nullptr |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

### template<typename CInterface, typename CInstance = typename CInterface::Instance> class AK.Wwise::Plugin::CBaseInstanceGlue< CInterface, CInstance >

[PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Associates an existing C Interface with a variable that can be used. Derives from the instance that uses it.

模板参数
:   |  |  |
    | --- | --- |
    | CInterface | The C Interface that needs to be instantiated into a CInstance. |
    | CInstance | The C Instance that will be instantiated. Automatically derived from the CInterface::Instance typedef. |

参见
:   - [AK::Wwise::Plugin::PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [103](_plugin_info_generator_8h_source.html#l00103) 行定义.