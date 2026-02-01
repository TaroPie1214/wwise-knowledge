# Interface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [PropertyDisplayName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name.html)
- [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::PropertyDisplayName::Interface结构体 参考

The C interface, fulfilled by your plug-in.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface.html#details)

`#include <PropertyDisplayName.h>`

类 AK.Wwise::Plugin::V1::PropertyDisplayName::Interface 继承关系图:

![](../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface_a4af6cffdf006e956be57d34496da0285.html#a4af6cffdf006e956be57d34496da0285) = [PropertyDisplayName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name.html) |
|  | |
| - Public 类型 继承自 [ak\_wwise\_plugin\_property\_display\_name\_v1](structak__wwise__plugin__property__display__name__v1.html) | |
| using | [Instance](structak__wwise__plugin__property__display__name__v1_ab4b234d53a8cb1cdd6e34a8371ec8b66.html#ab4b234d53a8cb1cdd6e34a8371ec8b66) = [ak\_wwise\_plugin\_property\_display\_name\_instance\_v1](structak__wwise__plugin__property__display__name__instance__v1.html) |
|  | Base instance type for providing display names to properties. [更多...](structak__wwise__plugin__property__display__name__v1_ab4b234d53a8cb1cdd6e34a8371ec8b66.html#ab4b234d53a8cb1cdd6e34a8371ec8b66) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface_af17310fb9f87defcb36ecb6754d36b0b.html#af17310fb9f87defcb36ecb6754d36b0b) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_property\_display\_name\_v1](structak__wwise__plugin__property__display__name__v1.html) | |
|  | [ak\_wwise\_plugin\_property\_display\_name\_v1](structak__wwise__plugin__property__display__name__v1_ad875bef563a55bf1c98749f88ab4dd93.html#ad875bef563a55bf1c98749f88ab4dd93) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_a7d1ff21fd409fc7363077edecb25a85d.html#a7d1ff21fd409fc7363077edecb25a85d) (decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9)) in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_aef726120a06d869829ad6ec67df4f2a4.html#aef726120a06d869829ad6ec67df4f2a4) () |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_acefd1ca37e4c88b6c792ec43953d3f9c.html#acefd1ca37e4c88b6c792ec43953d3f9c) (std::underlying\_type< decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9))>::type in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_property\_display\_name\_v1](structak__wwise__plugin__property__display__name__v1.html) | |
| bool(\* | [DisplayNameForProp](structak__wwise__plugin__property__display__name__v1_add7852506c1637fb1feb6e69871d5e5b.html#add7852506c1637fb1feb6e69871d5e5b) )(const struct [ak\_wwise\_plugin\_property\_display\_name\_instance\_v1](structak__wwise__plugin__property__display__name__instance__v1.html) \*in\_this, const char \*in\_pszPropertyName, char \*out\_pszDisplayName, uint32\_t in\_unCharCount) |
|  | Gets the user-friendly name of the specified property. [更多...](structak__wwise__plugin__property__display__name__v1_add7852506c1637fb1feb6e69871d5e5b.html#add7852506c1637fb1feb6e69871d5e5b) |
|  | |
| bool(\* | [DisplayNamesForPropValues](structak__wwise__plugin__property__display__name__v1_a6bfeb020b507e914b82a00d894b7601b.html#a6bfeb020b507e914b82a00d894b7601b) )(const struct [ak\_wwise\_plugin\_property\_display\_name\_instance\_v1](structak__wwise__plugin__property__display__name__instance__v1.html) \*in\_this, const char \*in\_pszPropertyName, char \*out\_pszValuesName, uint32\_t in\_unCharCount) |
|  | Get the user-friendly names of possible values for the specified property. [更多...](structak__wwise__plugin__property__display__name__v1_a6bfeb020b507e914b82a00d894b7601b.html#a6bfeb020b507e914b82a00d894b7601b) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

The C interface, fulfilled by your plug-in.

在文件 [PropertyDisplayName.h](_property_display_name_8h_source.html) 第 [164](_property_display_name_8h_source.html#l00164) 行定义.