# Free

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Free](class_a_k_1_1_i_ak_plugin_mem_alloc_ac86ca339952bc71a81c113007c9eff70.html#ac86ca339952bc71a81c113007c9eff70) | | [Malign](class_a_k_1_1_i_ak_plugin_mem_alloc_ac0a62d0ecaf499a8e970749f7dab997c.html#ac0a62d0ecaf499a8e970749f7dab997c) | | [Malloc](class_a_k_1_1_i_ak_plugin_mem_alloc_a9c088f25aa758b927fb47051756d678f.html#a9c088f25aa758b927fb47051756d678f) | | [Realloc](class_a_k_1_1_i_ak_plugin_mem_alloc_adcde8e2f3bae1737a56dffa292926033.html#adcde8e2f3bae1737a56dffa292926033) | | [ReallocAligned](class_a_k_1_1_i_ak_plugin_mem_alloc_a8a19e1e19531fe046b4f72ee623b27ad.html#a8a19e1e19531fe046b4f72ee623b27ad) | | [~IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc_ababbb05767843f656995ee53b789c40a.html#ababbb05767843f656995ee53b789c40a) | | [◆](#ac86ca339952bc71a81c113007c9eff70)Free() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual void AK::IAkPluginMemAlloc::Free | ( | void \* | *in\_pMemAddress* | ) |  | | pure virtual |  Free allocated memory.  参见  - [在音频插件中分配/取消分配内存](soundengine_plugins.html#fx_memory_alloc)  参数  |  |  | | --- | --- | | in\_pMemAddress | Allocated memory start address |  在 [AK.Wwise::Mallocator](class_a_k_1_1_wwise_1_1_mallocator_a642cb0d20450fe6fb88f3e954b8306da.html#a642cb0d20450fe6fb88f3e954b8306da) 内被实现.  被这些函数引用 [AK\_PLUGIN\_DELETE()](_i_ak_plugin_mem_alloc_8h_source.html#l00178) , 以及 [AK.Wwise::SafeAllocator< T >::~SafeAllocator()](_ak_allocator_8h_source.html#l00114). |