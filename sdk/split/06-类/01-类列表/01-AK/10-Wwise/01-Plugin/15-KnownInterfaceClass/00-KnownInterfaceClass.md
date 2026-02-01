# KnownInterfaceClass

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [KnownInterfaceClass](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class-members.html) |
[Public 类型](#pub-types)

AK.Wwise::Plugin::KnownInterfaceClass< in\_interfaceType, in\_interfaceVersion > 模板结构体 参考

[PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Compile-time dictionary of known interface-version.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class.html#details)

`#include <PluginInfoGenerator.h>`

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Type](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class_ae9b7610a500dfee9a6997ce2b2717029.html#ae9b7610a500dfee9a6997ce2b2717029) = void |
|  | |
| using | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class_ad4211ca6d56b7cae0527e82ff48c474f.html#ad4211ca6d56b7cae0527e82ff48c474f) = void |
|  | |

## 详细描述

### template<InterfaceType in\_interfaceType, InterfaceVersion in\_interfaceVersion> struct AK.Wwise::Plugin::KnownInterfaceClass< in\_interfaceType, in\_interfaceVersion >

[PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Compile-time dictionary of known interface-version.

Used so we can ask a KnownInterfaceClass<in\_interface, in\_version> and receive which class and interface it points to.

模板参数
:   |  |  |
    | --- | --- |
    | in\_interfaceType |  |
    | in\_interfaceVersion |  |

参见
:   - [AK::Wwise::Plugin::PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [189](_plugin_info_generator_8h_source.html#l00189) 行定义.