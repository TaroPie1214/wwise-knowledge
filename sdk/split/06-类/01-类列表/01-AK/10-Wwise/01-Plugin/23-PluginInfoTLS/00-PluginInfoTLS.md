# PluginInfoTLS

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PluginInfoTLS](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_t_l_s.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_t_l_s-members.html) |
[静态 Public 属性](#pub-static-attribs)

AK.Wwise::Plugin::PluginInfoTLS< bool > 模板结构体 参考

The interface information of the plug-in currently being instantiated.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_t_l_s.html#details)

`#include <PluginInfoGenerator.h>`

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static thread\_local [PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823) \* | [tls\_pluginInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_t_l_s_aa3641d2255c40ea69b81ff483715f014.html#aa3641d2255c40ea69b81ff483715f014) = nullptr |
|  | |

## 详细描述

### template<bool = false> struct AK.Wwise::Plugin::PluginInfoTLS< bool >

The interface information of the plug-in currently being instantiated.

When the host calls the Instantiate of the plug-in, [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator.") will automatically set this thread variable to the provided `in_pluginInfo`. This allows the interfaces to bind themselves without having to pass this parameter throughout the constructor.

|  |  |
| --- | --- |
|  | **警告:** This variable is only set up during instantiation. |

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [62](_plugin_info_generator_8h_source.html#l00062) 行定义.