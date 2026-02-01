# PluginInfoGenerator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::PluginInfoGenerator< PluginT > 模板结构体 参考

C++ PluginInfo Generator.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html#details)

`#include <PluginInfoGenerator.h>`

|  |  |
| --- | --- |
| 类 | |
| struct | [GenerateConstructor](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor.html) |
|  | Generates the constructor for our particular type [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor.html#details) |
|  | |
| struct | [GenerateConstructorArray](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_array.html) |
|  | Recursively generates the constructors and interface pointer updater for all the Interfaces. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_array.html#details) |
|  | |
| struct | [InterfaceInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html) |
|  | Compile-time dictionary about a particular interface type. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : size\_t { [k\_interfaceCount](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a390f558f26449abdbabe58ca9a5a84f2.html#a390f558f26449abdbabe58ca9a5a84f2a3c52cbc1c3f938553941a366080c183b) = CountInterfaces() } |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_aaee359fa086569f963cdfeba37916af5.html#aaee359fa086569f963cdfeba37916af5) ([PluginRegistration](class_a_k_1_1_plugin_registration.html) \*in\_pluginRegistration, uint32\_t in\_pluginFlags=0) |
|  | |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_aaa855eb952f4fd32eb5c1552f60b0690.html#aaa855eb952f4fd32eb5c1552f60b0690) (const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) \*in\_companyID, const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) \*in\_pluginID, const [AkPluginType](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4) \*in\_pluginType, uint32\_t in\_pluginFlags=0) |
|  | |
|  | [~PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a03ae8fe30f2e26a7dc0b7a6f689e0f39.html#a03ae8fe30f2e26a7dc0b7a6f689e0f39) ()=default |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| template<InterfaceType in\_interface = (InterfaceType)(AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NUM - 1)> | |
| static constexpr size\_t | [CountInterfaces](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a11cb52429806de9a1c2854226b6fc7cb.html#a11cb52429806de9a1c2854226b6fc7cb) () |
|  | Count the number of interfaces we are currently using. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a11cb52429806de9a1c2854226b6fc7cb.html#a11cb52429806de9a1c2854226b6fc7cb) |
|  | |
| template<InterfaceType in\_interfaceType> | |
| static constexpr [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) | [GenerateInterface](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_af8d8160778bc3a90950e679897ade9b5.html#af8d8160778bc3a90950e679897ade9b5) () |
|  | Generates the InterfaceArrayItem for our particular type. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_af8d8160778bc3a90950e679897ade9b5.html#af8d8160778bc3a90950e679897ade9b5) |
|  | |
| template<InterfaceType in\_interfaceType> | |
| static constexpr void | [GenerateInterfaceArray](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a7a0ab158d89c7725bd7f85c8aa567b85.html#a7a0ab158d89c7725bd7f85c8aa567b85) ([InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) out\_interfaces[[k\_interfaceCount](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a390f558f26449abdbabe58ca9a5a84f2.html#a390f558f26449abdbabe58ca9a5a84f2a3c52cbc1c3f938553941a366080c183b)], int in\_count, [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c)) |
|  | Recursively generates an interface array of all the Interfaces pointers. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a7a0ab158d89c7725bd7f85c8aa567b85.html#a7a0ab158d89c7725bd7f85c8aa567b85) |
|  | |
| static constexpr [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) \* | [GenerateInterfaceArray](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a51ea4ef90b966cdee02219dda3b1a345.html#a51ea4ef90b966cdee02219dda3b1a345) ([InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) out\_interfaces[[k\_interfaceCount](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a390f558f26449abdbabe58ca9a5a84f2.html#a390f558f26449abdbabe58ca9a5a84f2a3c52cbc1c3f938553941a366080c183b)]) |
|  | |
| static [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) \* | [Instantiate](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a79fe388f6b6a4dc266cd968394debc74.html#a79fe388f6b6a4dc266cd968394debc74) ([PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823) \*in\_pluginInfo) |
|  | Plug-in instance constructor, as shared with the host. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a79fe388f6b6a4dc266cd968394debc74.html#a79fe388f6b6a4dc266cd968394debc74) |
|  | |
| static void | [Disembody](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_ad42434ff32b9b1a7777ae4f522901c78.html#ad42434ff32b9b1a7777ae4f522901c78) ([InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) \*in\_instance) |
|  | Plug-in instance destructor, as shared to the host. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_ad42434ff32b9b1a7777ae4f522901c78.html#ad42434ff32b9b1a7777ae4f522901c78) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) | [m\_interfaceArray](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a925f1378056ddb536cb9179084578971.html#a925f1378056ddb536cb9179084578971) [[k\_interfaceCount](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a390f558f26449abdbabe58ca9a5a84f2.html#a390f558f26449abdbabe58ca9a5a84f2a3c52cbc1c3f938553941a366080c183b)] |
|  | Array of all used interfaces for the plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_a925f1378056ddb536cb9179084578971.html#a925f1378056ddb536cb9179084578971) |
|  | |
| [PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823) | [m\_pluginInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_af7bbc597d8b2e45862d900cc784db7bd.html#af7bbc597d8b2e45862d900cc784db7bd) |
|  | The unique m\_pluginInfo used in the [ak\_wwise\_plugin\_container](structak__wwise__plugin__container.html "Root interface allowing a logical unit (variable, library) to contain more than one interface.") for that particular plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_af7bbc597d8b2e45862d900cc784db7bd.html#af7bbc597d8b2e45862d900cc784db7bd) |
|  | |

## 详细描述

### template<typename PluginT> struct AK.Wwise::Plugin::PluginInfoGenerator< PluginT >

C++ PluginInfo Generator.

Retrieves the list of plug-in interfaces required by a plug-in through derivation, and automatically creates a related [ak\_wwise\_plugin\_info](structak__wwise__plugin__info.html) structure.

Compared to a manually generated C version, the generated structure is done through a function that fills all the required data. Since it's a static global function called only once, and contains only value stores, the cost is, so far, quite minimal.

模板参数
:   |  |  |
    | --- | --- |
    | PluginT | The plug-in class that needs to be instantiated in order to use that plug-in. |

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [327](_plugin_info_generator_8h_source.html#l00327) 行定义.