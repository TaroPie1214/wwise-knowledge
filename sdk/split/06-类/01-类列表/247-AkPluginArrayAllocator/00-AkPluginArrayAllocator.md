# AkPluginArrayAllocator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_plugin_array_allocator-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AkPluginArrayAllocator类 参考

`#include <IAkPluginMemAlloc.h>`

类 AkPluginArrayAllocator 继承关系图:

![](../../../images/class_ak_plugin_array_allocator.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [AkPluginArrayAllocator](class_ak_plugin_array_allocator_acfc9f0daec20881eee32d575db63e4d4.html#acfc9f0daec20881eee32d575db63e4d4) () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Init](class_ak_plugin_array_allocator_a3476c037658c433a50660b258231217e.html#a3476c037658c433a50660b258231217e) ([AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [Alloc](class_ak_plugin_array_allocator_a6209b00f54308f95db29f90884f64b2a.html#a6209b00f54308f95db29f90884f64b2a) (size\_t in\_uSize) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [ReAlloc](class_ak_plugin_array_allocator_a3ad1b79646ea08077c443461cdec2b83.html#a3ad1b79646ea08077c443461cdec2b83) (void \*in\_pCurrent, size\_t, size\_t in\_uNewSize) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Free](class_ak_plugin_array_allocator_a338c1e0cc8d0ebab2dc65668c227912c.html#a338c1e0cc8d0ebab2dc65668c227912c) (void \*in\_pAddress) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [TransferMem](class_ak_plugin_array_allocator_a7055e3322180145e8f4245f647ee84b6.html#a7055e3322180145e8f4245f647ee84b6) (void \*&io\_pDest, [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html) &in\_src, void \*in\_pSrc) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \* | [GetAllocator](class_ak_plugin_array_allocator_a834b30b9fd15c5344a2841c6ef907afe.html#a834b30b9fd15c5344a2841c6ef907afe) () |
|  | |

## 详细描述

Allocator for plugin-friendly arrays (see [AkArray](class_ak_array.html "Specific implementation of array")). Usage: Initialize the array with [Init(AK::IAkPluginMemAlloc\* in\_pAllocator)](class_ak_plugin_array_allocator_a3476c037658c433a50660b258231217e.html#a3476c037658c433a50660b258231217e), passing it the memory allocator received from the host. Then use normally.

在文件 [IAkPluginMemAlloc.h](_i_ak_plugin_mem_alloc_8h_source.html) 第 [197](_i_ak_plugin_mem_alloc_8h_source.html#l00197) 行定义.