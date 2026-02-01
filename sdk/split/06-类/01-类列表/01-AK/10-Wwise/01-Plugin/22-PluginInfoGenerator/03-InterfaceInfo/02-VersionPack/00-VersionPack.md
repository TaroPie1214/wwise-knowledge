# VersionPack

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)
- [InterfaceInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html)
- [VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack-members.html) |
[静态 Public 成员函数](#pub-static-methods)

AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType >::VersionPack< in\_versions > 模板结构体 参考

Compile-time container of version numbers.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html#details)

`#include <PluginInfoGenerator.h>`

类 AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType >::VersionPack< in\_versions > 继承关系图:

![](../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.png)

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static constexpr uint32\_t | [GetLatest](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack_affd94260b3874205287fe65f888db24f.html#affd94260b3874205287fe65f888db24f) () |
|  | Get the latest version stored in the container. Assumes the container is sorted in ascending order. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack_affd94260b3874205287fe65f888db24f.html#affd94260b3874205287fe65f888db24f) |
|  | |

## 详细描述

### template<typename PluginT> template<InterfaceType in\_interfaceType> template<uint32\_t... in\_versions> struct AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType >::VersionPack< in\_versions >

Compile-time container of version numbers.

模板参数
:   |  |  |
    | --- | --- |
    | in\_versions,... | [Version](class_a_k_1_1_wwise_1_1_version.html) numbers to store in the container in ascending order. |

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [351](_plugin_info_generator_8h_source.html#l00351) 行定义.