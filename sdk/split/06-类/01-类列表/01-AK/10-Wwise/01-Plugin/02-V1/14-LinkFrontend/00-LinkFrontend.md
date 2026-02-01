# LinkFrontend

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [LinkFrontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::LinkFrontend类 参考

Host API to retrieve a link to the plug-in's frontend interfaces.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend.html#details)

`#include <PluginLinks.h>`

类 AK.Wwise::Plugin::V1::LinkFrontend 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a6be64318771e26f029360ef25f3ef89a.html#a6be64318771e26f029360ef25f3ef89aa0f662146efb970708ae902d85b32f04e) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LINK\_FRONTEND } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a6be64318771e26f029360ef25f3ef89a.html#a6be64318771e26f029360ef25f3ef89a) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a9542478cc50ddee8c2d2039ccb8fd21d.html#a9542478cc50ddee8c2d2039ccb8fd21da43acd9ca07d8f8e688ac497f8e3d3e07) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a9542478cc50ddee8c2d2039ccb8fd21d.html#a9542478cc50ddee8c2d2039ccb8fd21d) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a6dca6f5baad734afa720a7343f9368fc.html#a6dca6f5baad734afa720a7343f9368fc) = [CLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ae46b0c1760947987e45c7c736fafbc57.html#ae46b0c1760947987e45c7c736fafbc57) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a050f59682dfcaea2cef7dd6a9d2f59a3.html#a050f59682dfcaea2cef7dd6a9d2f59a3) = [CLinkFrontend::Instance](structak__wwise__plugin__link__frontend__v1_ae5416fd3b28a4ef2810238b2c85267d7.html#ae5416fd3b28a4ef2810238b2c85267d7) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CLinkFrontend >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CLinkFrontend >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_aff9067bc56d00cc3f5362d072df8337b.html#aff9067bc56d00cc3f5362d072df8337b) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [ak\_wwise\_plugin\_frontend\_instance](structak__wwise__plugin__frontend__instance.html) \*\* | [GetArray](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_ab086d0ff5868bf672988ba5c4058fb24.html#ab086d0ff5868bf672988ba5c4058fb24) (int \*out\_count) const |
|  | Retrieves an array of the plug-in's frontend instances. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_ab086d0ff5868bf672988ba5c4058fb24.html#ab086d0ff5868bf672988ba5c4058fb24) |
|  | |
| template<typename Frontend = ak\_wwise\_plugin\_frontend\_instance, typename Functor > | |
| void | [ForEach](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a8ad177ae489502dd73244cd09b511459.html#a8ad177ae489502dd73244cd09b511459) (Functor in\_operation) const |
|  | Applies a function on each plug-in's frontend instances. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a8ad177ae489502dd73244cd09b511459.html#a8ad177ae489502dd73244cd09b511459) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CLinkFrontend >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

Host API to retrieve a link to the plug-in's frontend interfaces.

Useful for the Backend when there are special properties that don't use property sets.

在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [194](_plugin_links_8h_source.html#l00194) 行定义.