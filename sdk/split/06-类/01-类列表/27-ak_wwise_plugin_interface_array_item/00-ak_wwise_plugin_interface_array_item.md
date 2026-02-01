# ak_wwise_plugin_interface_array_item

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__interface__array__item-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_interface\_array\_item结构体 参考

A single instantiatable plug-in interface.
[更多...](structak__wwise__plugin__interface__array__item.html#details)

`#include <PluginInterfaceArrayItem.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| constexpr | [ak\_wwise\_plugin\_interface\_array\_item](structak__wwise__plugin__interface__array__item_a09e22596e6d7c6be56d459c2ee65ca61.html#a09e22596e6d7c6be56d459c2ee65ca61) (ak\_wwise\_plugin\_interface\_ptr in\_interface=nullptr, ak\_wwise\_plugin\_instance\_ptr in\_instance=nullptr) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| ak\_wwise\_plugin\_interface\_ptr | [m\_interface](structak__wwise__plugin__interface__array__item_a78d9a47edf55398b0200865a0a65a1be.html#a78d9a47edf55398b0200865a0a65a1be) |
|  | The interface. Should be identical for every instance of this DLL. [更多...](structak__wwise__plugin__interface__array__item_a78d9a47edf55398b0200865a0a65a1be.html#a78d9a47edf55398b0200865a0a65a1be) |
|  | |
| ak\_wwise\_plugin\_instance\_ptr | [m\_instance](structak__wwise__plugin__interface__array__item_ae41e9a25b8ba472d3f90deb9ec1ca0d6.html#ae41e9a25b8ba472d3f90deb9ec1ca0d6) |
|  | That particular instance. [更多...](structak__wwise__plugin__interface__array__item_ae41e9a25b8ba472d3f90deb9ec1ca0d6.html#ae41e9a25b8ba472d3f90deb9ec1ca0d6) |
|  | |

## 详细描述

A single instantiatable plug-in interface.

The goal of the [ak\_wwise\_plugin\_interface\_array\_item](structak__wwise__plugin__interface__array__item.html "A single instantiatable plug-in interface.") is to provide both the static m\_interface, as well as the dynamic m\_instance

在文件 [PluginInterfaceArrayItem.h](_plugin_interface_array_item_8h_source.html) 第 [43](_plugin_interface_array_item_8h_source.html#l00043) 行定义.