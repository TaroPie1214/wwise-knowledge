# GenerateConstructorArray

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)
- [GenerateConstructorArray](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_array.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_array-members.html) |
[静态 Public 成员函数](#pub-static-methods)

AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::GenerateConstructorArray< in\_interfaceType > 模板结构体 参考

Recursively generates the constructors and interface pointer updater for all the Interfaces.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_array.html#details)

`#include <PluginInfoGenerator.h>`

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static void | [UpdateCInterface](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_array_a19bb378df5109f19b98b9e456530803d.html#a19bb378df5109f19b98b9e456530803d) (const [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) in\_original[[k\_interfaceCount](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a390f558f26449abdbabe58ca9a5a84f2.html#a390f558f26449abdbabe58ca9a5a84f2a3c52cbc1c3f938553941a366080c183b)], int in\_count=0) |
|  | |
| static void | [Constructor](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_array_ad2cef532f375e41968bb6ce5296ca8c5.html#ad2cef532f375e41968bb6ce5296ca8c5) ([InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) out\_interfaces[[k\_interfaceCount](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a390f558f26449abdbabe58ca9a5a84f2.html#a390f558f26449abdbabe58ca9a5a84f2a3c52cbc1c3f938553941a366080c183b)], const [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) in\_original[[k\_interfaceCount](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a390f558f26449abdbabe58ca9a5a84f2.html#a390f558f26449abdbabe58ca9a5a84f2a3c52cbc1c3f938553941a366080c183b)], PluginT \*in\_instance, int in\_count=0) |
|  | |

## 详细描述

### template<typename PluginT> template<InterfaceType in\_interfaceType = (InterfaceType)(AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_UNKNOWN + 1)> struct AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::GenerateConstructorArray< in\_interfaceType >

Recursively generates the constructors and interface pointer updater for all the Interfaces.

模板参数
:   |  |  |
    | --- | --- |
    | in\_interfaceType | The current interface being processed. They are processed recursively from max to 0 |

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [657](_plugin_info_generator_8h_source.html#l00657) 行定义.