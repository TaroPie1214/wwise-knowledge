# Mallocator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Mallocator](class_a_k_1_1_wwise_1_1_mallocator.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_mallocator-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::Mallocator类 参考

`#include <AkAllocator.h>`

类 AK.Wwise::Mallocator 继承关系图:

![](../../../../../images/class_a_k_1_1_wwise_1_1_mallocator.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void \* | [Malloc](class_a_k_1_1_wwise_1_1_mallocator_a7b6c51c73554f1f56787fd6ce5a0fac6.html#a7b6c51c73554f1f56787fd6ce5a0fac6) (size\_t in\_uSize, const char \*, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)) override |
|  | |
| virtual void | [Free](class_a_k_1_1_wwise_1_1_mallocator_a642cb0d20450fe6fb88f3e954b8306da.html#a642cb0d20450fe6fb88f3e954b8306da) (void \*in\_pMemAddress) override |
|  | |
| virtual void \* | [Malign](class_a_k_1_1_wwise_1_1_mallocator_a2836df222c69be7e427e46398c346a3f.html#a2836df222c69be7e427e46398c346a3f) (size\_t in\_uSize, size\_t in\_uAlignment, const char \*, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)) override |
|  | |
| virtual void \* | [Realloc](class_a_k_1_1_wwise_1_1_mallocator_a81450889d62616bd2938fb438c0f0648.html#a81450889d62616bd2938fb438c0f0648) (void \*in\_pMemAddress, size\_t in\_uSize, const char \*, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)) override |
|  | |
| virtual void \* | [ReallocAligned](class_a_k_1_1_wwise_1_1_mallocator_aa4b93a4c117a59361704883d501491a6.html#aa4b93a4c117a59361704883d501491a6) (void \*in\_pMemAddress, size\_t in\_uSize, size\_t in\_uAlignment, const char \*, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)) override |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Protected 成员函数 继承自 [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) | |
| virtual | [~IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc_ababbb05767843f656995ee53b789c40a.html#ababbb05767843f656995ee53b789c40a) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_mem_alloc_ababbb05767843f656995ee53b789c40a.html#ababbb05767843f656995ee53b789c40a) |
|  | |

## 详细描述

在文件 [AkAllocator.h](_ak_allocator_8h_source.html) 第 [45](_ak_allocator_8h_source.html#l00045) 行定义.