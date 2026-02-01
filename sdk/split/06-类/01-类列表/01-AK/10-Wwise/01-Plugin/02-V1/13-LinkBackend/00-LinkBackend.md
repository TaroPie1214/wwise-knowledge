# LinkBackend

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [LinkBackend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::LinkBackend类 参考

Host API to retrieve a link to the plug-in's backend instance.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend.html#details)

`#include <PluginLinks.h>`

类 AK.Wwise::Plugin::V1::LinkBackend 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a6c692de8c64dcb10bde7924209ccaeae.html#a6c692de8c64dcb10bde7924209ccaeaea884c130b088dda2f4d3c700941990442) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LINK\_BACKEND } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a6c692de8c64dcb10bde7924209ccaeae.html#a6c692de8c64dcb10bde7924209ccaeae) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_af4ef15139e990e25d076a4e161faac0f.html#af4ef15139e990e25d076a4e161faac0fa8eddcb53470eb84eda677d0f41c10350) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_af4ef15139e990e25d076a4e161faac0f.html#af4ef15139e990e25d076a4e161faac0f) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_ac7654e4696f2c587f1e6ddf792beff54.html#ac7654e4696f2c587f1e6ddf792beff54) = [CLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_aaa3fe7d7e70babc8d8aa9e0b88171ae6.html#aaa3fe7d7e70babc8d8aa9e0b88171ae6) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a3ade782d64961bbae9f35532fd29d601.html#a3ade782d64961bbae9f35532fd29d601) = [CLinkBackend::Instance](structak__wwise__plugin__link__backend__v1_a2712f50d873479cc047f2b5938fe290e.html#a2712f50d873479cc047f2b5938fe290e) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CLinkBackend >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CLinkBackend >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_acac65e4a746e5104e04b138a7889d3c5.html#acac65e4a746e5104e04b138a7889d3c5) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [ak\_wwise\_plugin\_backend\_instance](structak__wwise__plugin__backend__instance.html) \* | [Get](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a60fcc8ce01bfeccf062a985258c95c78.html#a60fcc8ce01bfeccf062a985258c95c78) () const |
|  | Retrieves a link to the plug-in's backend instance. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a60fcc8ce01bfeccf062a985258c95c78.html#a60fcc8ce01bfeccf062a985258c95c78) |
|  | |
| template<typename Backend > | |
| Backend \* | [As](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a20ab757948a2d67eaea35ec525a5a3dd.html#a20ab757948a2d67eaea35ec525a5a3dd) () |
|  | Retrieves a link to the plug-in's backend instance, casted as your C++ Backend class type. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a20ab757948a2d67eaea35ec525a5a3dd.html#a20ab757948a2d67eaea35ec525a5a3dd) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CLinkBackend >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

Host API to retrieve a link to the plug-in's backend instance.

Useful for the [Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html "Frontend plug-in API for Audio plug-ins.") (GUI) when a special function must be called to get a value, or update elements.

在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [135](_plugin_links_8h_source.html#l00135) 行定义.