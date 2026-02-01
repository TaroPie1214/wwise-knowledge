# ToInterfaceClassImpl

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)
- [InterfaceInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html)
- [ToInterfaceClassImpl](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_to_interface_class_impl.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_to_interface_class_impl-members.html) |
[静态 Public 成员函数](#pub-static-methods)

AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType >::ToInterfaceClassImpl< bool > 模板结构体 参考

Casts the plug-in class to the requested interface class.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_to_interface_class_impl.html#details)

`#include <PluginInfoGenerator.h>`

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| constexpr static [InterfaceClass](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_acdbef4d83b4072eaa4acc434070aa062.html#acdbef4d83b4072eaa4acc434070aa062) \* | [Cast](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_to_interface_class_impl_a0c9498d0f80676ae7d7fe406ae6fb609.html#a0c9498d0f80676ae7d7fe406ae6fb609) (PluginT \*in\_plugin) |
|  | |

## 详细描述

### template<typename PluginT> template<InterfaceType in\_interfaceType> template<bool> struct AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType >::ToInterfaceClassImpl< bool >

Casts the plug-in class to the requested interface class.

|  |  |
| --- | --- |
|  | **备注:** This needs to be in a template, as the interface might not be castable. |

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [510](_plugin_info_generator_8h_source.html#l00510) 行定义.