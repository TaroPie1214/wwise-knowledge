# GenerateConstructor

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)
- [GenerateConstructor](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor-members.html) |
[静态 Public 成员函数](#pub-static-methods)

AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::GenerateConstructor< in\_interfaceType > 模板结构体 参考

Generates the constructor for our particular type
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor.html#details)

`#include <PluginInfoGenerator.h>`

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static void | [UpdateCInterface](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_a1593fdd0a69c7a0d025274cdc94f2c07.html#a1593fdd0a69c7a0d025274cdc94f2c07) (const [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) &in\_original) |
|  | |
| static void | [Constructor](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_a465536111144d2b2a87647a15c602f35.html#a465536111144d2b2a87647a15c602f35) ([InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) &out\_interface, const [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) &in\_original, PluginT \*in\_instance) |
|  | |

## 详细描述

### template<typename PluginT> template<InterfaceType in\_interfaceType> struct AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::GenerateConstructor< in\_interfaceType >

Generates the constructor for our particular type

模板参数
:   |  |  |
    | --- | --- |
    | in\_interfaceType | Interface ID |

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [624](_plugin_info_generator_8h_source.html#l00624) 行定义.