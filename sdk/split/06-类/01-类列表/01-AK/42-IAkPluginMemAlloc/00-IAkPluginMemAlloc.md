# IAkPluginMemAlloc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_mem_alloc-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginMemAlloc类 参考abstract

`#include <IAkPluginMemAlloc.h>`

类 AK::IAkPluginMemAlloc 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_mem_alloc.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void \* | [Malloc](class_a_k_1_1_i_ak_plugin_mem_alloc_a9c088f25aa758b927fb47051756d678f.html#a9c088f25aa758b927fb47051756d678f) (size\_t in\_uSize, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine)=0 |
|  | |
| virtual void | [Free](class_a_k_1_1_i_ak_plugin_mem_alloc_ac86ca339952bc71a81c113007c9eff70.html#ac86ca339952bc71a81c113007c9eff70) (void \*in\_pMemAddress)=0 |
|  | |
| virtual void \* | [Malign](class_a_k_1_1_i_ak_plugin_mem_alloc_ac0a62d0ecaf499a8e970749f7dab997c.html#ac0a62d0ecaf499a8e970749f7dab997c) (size\_t in\_uSize, size\_t in\_uAlignment, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine)=0 |
|  | |
| virtual void \* | [Realloc](class_a_k_1_1_i_ak_plugin_mem_alloc_adcde8e2f3bae1737a56dffa292926033.html#adcde8e2f3bae1737a56dffa292926033) (void \*in\_pMemAddress, size\_t in\_uSize, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine)=0 |
|  | |
| virtual void \* | [ReallocAligned](class_a_k_1_1_i_ak_plugin_mem_alloc_a8a19e1e19531fe046b4f72ee623b27ad.html#a8a19e1e19531fe046b4f72ee623b27ad) (void \*in\_pMemAddress, size\_t in\_uSize, size\_t in\_uAlignment, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine)=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc_ababbb05767843f656995ee53b789c40a.html#ababbb05767843f656995ee53b789c40a) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_mem_alloc_ababbb05767843f656995ee53b789c40a.html#ababbb05767843f656995ee53b789c40a) |
|  | |

## 详细描述

Interface to memory allocation

|  |  |
| --- | --- |
|  | **注意:** SDK users should never call these function directly, but use memory allocation macros instead. |

参见
:   - [在音频插件中分配/取消分配内存](soundengine_plugins.html#fx_memory_alloc)

在文件 [IAkPluginMemAlloc.h](_i_ak_plugin_mem_alloc_8h_source.html) 第 [41](_i_ak_plugin_mem_alloc_8h_source.html#l00041) 行定义.