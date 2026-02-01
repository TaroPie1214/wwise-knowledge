# Free

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Mallocator](class_a_k_1_1_wwise_1_1_mallocator.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Free](class_a_k_1_1_wwise_1_1_mallocator_a642cb0d20450fe6fb88f3e954b8306da.html#a642cb0d20450fe6fb88f3e954b8306da) | | [Malign](class_a_k_1_1_wwise_1_1_mallocator_a2836df222c69be7e427e46398c346a3f.html#a2836df222c69be7e427e46398c346a3f) | | [Malloc](class_a_k_1_1_wwise_1_1_mallocator_a7b6c51c73554f1f56787fd6ce5a0fac6.html#a7b6c51c73554f1f56787fd6ce5a0fac6) | | [Realloc](class_a_k_1_1_wwise_1_1_mallocator_a81450889d62616bd2938fb438c0f0648.html#a81450889d62616bd2938fb438c0f0648) | | [ReallocAligned](class_a_k_1_1_wwise_1_1_mallocator_aa4b93a4c117a59361704883d501491a6.html#aa4b93a4c117a59361704883d501491a6) | | [◆](#a642cb0d20450fe6fb88f3e954b8306da)Free() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual void AK.Wwise::Mallocator::Free | ( | void \* | *in\_pMemAddress* | ) |  | | inlineoverridevirtual |  Free allocated memory.  参见  - [在音频插件中分配/取消分配内存](soundengine_plugins.html#fx_memory_alloc)  参数  |  |  | | --- | --- | | in\_pMemAddress | Allocated memory start address |  实现了 [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc_ac86ca339952bc71a81c113007c9eff70.html#ac86ca339952bc71a81c113007c9eff70).  在文件 [AkAllocator.h](_ak_allocator_8h_source.html) 第 [58](_ak_allocator_8h_source.html#l00058) 行定义. |