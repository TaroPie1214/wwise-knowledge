# ak_wwise_plugin_cpp_base_instance

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__cpp__base__instance-members.html) |
[Public 成员函数](#pub-methods)

ak\_wwise\_plugin\_cpp\_base\_instance结构体 参考

[Global](group__global.html)

Generic base for all plug-in instances in C++
[更多...](structak__wwise__plugin__cpp__base__instance.html#details)

`#include <PluginInstanceTypes.h>`

类 ak\_wwise\_plugin\_cpp\_base\_instance 继承关系图:

![](../../../images/structak__wwise__plugin__cpp__base__instance.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

Generic base for all plug-in instances in C++

警告
:   This base differs from the [ak\_wwise\_plugin\_base\_instance](structak__wwise__plugin__base__instance.html "Generic base for all plug-in instances. In C++, this is derived. In C, they are equivalent.") because C++ classes have a virtual table as their first member. To distinguish between the C and C++ versions, you must use a static\_cast operation instead of a reinterpret\_cast or a C-style cast. Therefore, we recommend that you instantiate a plug-in in C++, and then return C pointers to the instance structures located at their base address.

As such, it is expected to instantiate a plug-in in C++, and return C pointers back to the instance structures with a different base address.

在文件 [PluginInstanceTypes.h](_plugin_instance_types_8h_source.html) 第 [67](_plugin_instance_types_8h_source.html#l00067) 行定义.