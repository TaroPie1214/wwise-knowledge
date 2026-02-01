# IAkPluginServiceTempAlloc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceTempAlloc](class_a_k_1_1_i_ak_plugin_service_temp_alloc.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_temp_alloc-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods) |
[友元](#friends)

AK::IAkPluginServiceTempAlloc类 参考abstract

`#include <IAkPluginTempAlloc.h>`

类 AK::IAkPluginServiceTempAlloc 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_temp_alloc.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \* | [GetTempAllocAudioRenderCurrent](class_a_k_1_1_i_ak_plugin_service_temp_alloc_ab1d37190b846c523dafc05f37ae07fa0.html#ab1d37190b846c523dafc05f37ae07fa0) ()=0 |
|  | |
| virtual [IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \* | [GetBookmarkAlloc](class_a_k_1_1_i_ak_plugin_service_temp_alloc_ad02e25ba8d8217ceb2a669e4817bf5d1.html#ad02e25ba8d8217ceb2a669e4817bf5d1) ()=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServiceTempAlloc](class_a_k_1_1_i_ak_plugin_service_temp_alloc_ab8d6949fbfc9d9a393adaaf90cc3518e.html#ab8d6949fbfc9d9a393adaaf90cc3518e) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

|  |  |
| --- | --- |
| 友元 | |
| struct | [PluginBookmarkAllocRegion](class_a_k_1_1_i_ak_plugin_service_temp_alloc_a5f30a979482edb1145a991d9131ed329.html#a5f30a979482edb1145a991d9131ed329) |
|  | |

## 详细描述

Interface for performing extremely-fast zero-fragmentation temporary allocations, e.g. allocations that exist for one or two ticks, or allocations that exist for a single stack frame. These use the existing [TempAlloc](namespace_a_k_1_1_temp_alloc.html) infrastructure in the core soundengine, whose behaviour and allocation characteristics are defined in the [MemoryMgr](namespace_a_k_1_1_memory_mgr.html) initialization settings.

For temporary allocations, types and lifetimes can be specified for mallocations – or reallocs. These allocations will only persist for the given soundengine tick (Lifetime\_CurrentTick) and be destroyed at the beginning of the next tick, or will persist for two soundengine ticks.

For bookmark allocations, you need to mark the start of a bookmark-allocation Region and perform allocations that persist until the bookmark-allocation region is closed. A struct, "PluginBookmarkAllocRegion" has been provided to help with that.

Because these allocations are guaranteed to be destroyed collectively and simultaneously as a part of their respective system, there is no fragmentation incurred by this, and no 'free' function is available. Also, these allocations are also extremely fast, with no multi-threading contention in most cases, and the total overhead of each alloc measured on the order of dozens of cycles.

参见
:   - [调节 Bookmark Allocator 内存](goingfurther_optimizingmempools_reducing_memory.html#goingfurther_optimizingmempools_bookmarkalloc)

在文件 [IAkPluginTempAlloc.h](_i_ak_plugin_temp_alloc_8h_source.html) 第 [59](_i_ak_plugin_temp_alloc_8h_source.html#l00059) 行定义.