# AkMixerInputMap

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_mixer_input_map-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AkMixerInputMap< KEY, USER\_DATA > 模板类 参考

[AkMixerInputMap](class_ak_mixer_input_map.html "AkMixerInputMap: Map of inputs (identified with AK::IAkMixerInputContext *) to user-defined blocks of..."): Map of inputs (identified with [AK::IAkMixerInputContext](class_a_k_1_1_i_ak_mixer_input_context.html "Interface to retrieve information about an input of a mix connection (for processing during the Speak...") \*) to user-defined blocks of data.
[更多...](class_ak_mixer_input_map.html#details)

`#include <AkMixerInputMap.h>`

类 AkMixerInputMap< KEY, USER\_DATA > 继承关系图:

![](../../../images/class_ak_mixer_input_map.png)

|  |  |
| --- | --- |
| Public 类型 | |
| typedef [AkArray](class_ak_array.html)< [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA >, const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > &, [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html) > | [BaseClass](class_ak_mixer_input_map_a8e79afd57e0ac98a70d00ca3d874045b.html#a8e79afd57e0ac98a70d00ca3d874045b) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| USER\_DATA \* | [Exists](class_ak_mixer_input_map_ad9acf848722f5fb49c1184fc89aff4a2.html#ad9acf848722f5fb49c1184fc89aff4a2) (KEY in\_key) |
|  | Returns the user data associated with given input context. Returns NULL if none found. [更多...](class_ak_mixer_input_map_ad9acf848722f5fb49c1184fc89aff4a2.html#ad9acf848722f5fb49c1184fc89aff4a2) |
|  | |
| USER\_DATA \* | [AddInput](class_ak_mixer_input_map_aa8e0ad3d5ecd8a24cc4c5011b4ffb1c9.html#aa8e0ad3d5ecd8a24cc4c5011b4ffb1c9) (KEY in\_key) |
|  | Adds an input with new user data. [更多...](class_ak_mixer_input_map_aa8e0ad3d5ecd8a24cc4c5011b4ffb1c9.html#aa8e0ad3d5ecd8a24cc4c5011b4ffb1c9) |
|  | |
| bool | [RemoveInput](class_ak_mixer_input_map_a0461595bdde4fe72fe828b94e741043a.html#a0461595bdde4fe72fe828b94e741043a) (KEY in\_key) |
|  | Removes an input and destroys its associated user data. [更多...](class_ak_mixer_input_map_a0461595bdde4fe72fe828b94e741043a.html#a0461595bdde4fe72fe828b94e741043a) |
|  | |
| [AkArray](class_ak_array.html)< [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA >, const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > &, [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html) >::Iterator | [EraseSwap](class_ak_mixer_input_map_ad839b271ff3a2213765456cefd569e5c.html#ad839b271ff3a2213765456cefd569e5c) (typename [AkArray](class_ak_array.html)< [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA >, const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > &, [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html) >::Iterator &in\_rIter) |
|  | Erase the specified iterator in the array. but it does not guarantee the ordering in the array. [更多...](class_ak_mixer_input_map_ad839b271ff3a2213765456cefd569e5c.html#ad839b271ff3a2213765456cefd569e5c) |
|  | |
| void | [Term](class_ak_mixer_input_map_acb435c00ea3ac90fe96f4367bdfd5e7e.html#acb435c00ea3ac90fe96f4367bdfd5e7e) () |
|  | Terminate array. [更多...](class_ak_mixer_input_map_acb435c00ea3ac90fe96f4367bdfd5e7e.html#acb435c00ea3ac90fe96f4367bdfd5e7e) |
|  | |
| [AkArray](class_ak_array.html)< [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA >, const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > &, [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html) >::Iterator | [FindEx](class_ak_mixer_input_map_af9cf13aca17ab1e543319727f4134f8b.html#af9cf13aca17ab1e543319727f4134f8b) (KEY in\_key) const |
|  | Finds an item in the array. [更多...](class_ak_mixer_input_map_af9cf13aca17ab1e543319727f4134f8b.html#af9cf13aca17ab1e543319727f4134f8b) |
|  | |
| void | [RemoveAll](class_ak_mixer_input_map_af37914978f7cff8b5e3b398954b993aa.html#af37914978f7cff8b5e3b398954b993aa) () |
|  | Removes and destroys all items in the array. [更多...](class_ak_mixer_input_map_af37914978f7cff8b5e3b398954b993aa.html#af37914978f7cff8b5e3b398954b993aa) |
|  | |
| - Public 成员函数 继承自 [AkArray< AkInputMapSlot< KEY, USER\_DATA >, const AkInputMapSlot< KEY, USER\_DATA > &, AkPluginArrayAllocator >](class_ak_array.html) | |
|  | [AkArray](class_ak_array_a0c26fb61c9eaf45c327359b26c076a8c.html#a0c26fb61c9eaf45c327359b26c076a8c) () |
|  | Constructor [更多...](class_ak_array_a0c26fb61c9eaf45c327359b26c076a8c.html#a0c26fb61c9eaf45c327359b26c076a8c) |
|  | |
|  | [~AkArray](class_ak_array_afec87243af25d7860ed91466e3cdacbe.html#afec87243af25d7860ed91466e3cdacbe) () |
|  | Destructor [更多...](class_ak_array_afec87243af25d7860ed91466e3cdacbe.html#afec87243af25d7860ed91466e3cdacbe) |
|  | |
| Iterator | [Begin](class_ak_array_a3586641c10c90cdcbd2c67edc5361309.html#a3586641c10c90cdcbd2c67edc5361309) () const |
|  | Returns the iterator to the first item of the array, will be [End()](class_ak_array_a8b3f475890ba0b28b1ee26ef26835789.html#a8b3f475890ba0b28b1ee26ef26835789 "Returns the iterator to the end of the array") if the array is empty. [更多...](class_ak_array_a3586641c10c90cdcbd2c67edc5361309.html#a3586641c10c90cdcbd2c67edc5361309) |
|  | |
| Iterator | [End](class_ak_array_a8b3f475890ba0b28b1ee26ef26835789.html#a8b3f475890ba0b28b1ee26ef26835789) () const |
|  | Returns the iterator to the end of the array [更多...](class_ak_array_a8b3f475890ba0b28b1ee26ef26835789.html#a8b3f475890ba0b28b1ee26ef26835789) |
|  | |
| Iterator | [FindEx](class_ak_array_a5e2ab9cb3de65d194b92bd2328a7d5b0.html#a5e2ab9cb3de65d194b92bd2328a7d5b0) (const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > & in\_Item) const |
|  | Returns the iterator th the specified item, will be [End()](class_ak_array_a8b3f475890ba0b28b1ee26ef26835789.html#a8b3f475890ba0b28b1ee26ef26835789 "Returns the iterator to the end of the array") if the item is not found [更多...](class_ak_array_a5e2ab9cb3de65d194b92bd2328a7d5b0.html#a5e2ab9cb3de65d194b92bd2328a7d5b0) |
|  | |
| Iterator | [BinarySearch](class_ak_array_a21687ba2fac7670b6ed2b84e4196ef73.html#a21687ba2fac7670b6ed2b84e4196ef73) (const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > & in\_Item) const |
|  | |
| Iterator | [Erase](class_ak_array_a83b57b37e09eddbe82c3bf75c32ef6c7.html#a83b57b37e09eddbe82c3bf75c32ef6c7) (Iterator &in\_rIter) |
|  | Erase the specified iterator from the array [更多...](class_ak_array_a83b57b37e09eddbe82c3bf75c32ef6c7.html#a83b57b37e09eddbe82c3bf75c32ef6c7) |
|  | |
| void | [Erase](class_ak_array_a2832494964d59bf4fcf373ef9559112d.html#a2832494964d59bf4fcf373ef9559112d) (unsigned int in\_uIndex) |
|  | Erase the item at the specified index [更多...](class_ak_array_a2832494964d59bf4fcf373ef9559112d.html#a2832494964d59bf4fcf373ef9559112d) |
|  | |
| Iterator | [EraseSwap](class_ak_array_afd392cabe6de69de5eb1da0370b1f07f.html#afd392cabe6de69de5eb1da0370b1f07f) (Iterator &in\_rIter) |
|  | |
| void | [EraseSwap](class_ak_array_ab251396f0afc650ce10e8dd20e4b50bc.html#ab251396f0afc650ce10e8dd20e4b50bc) (unsigned int in\_uIndex) |
|  | |
| bool | [IsGrowingAllowed](class_ak_array_a5b644b3d097409e680c656749fa03600.html#a5b644b3d097409e680c656749fa03600) () const |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Reserve](class_ak_array_ae86070a50fcf8a552ce9c2da01d6fceb.html#ae86070a50fcf8a552ce9c2da01d6fceb) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulReserve) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ReserveExtra](class_ak_array_a7a551d1cae004f9402cc86b660443359.html#a7a551d1cae004f9402cc86b660443359) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulReserve) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Reserved](class_ak_array_a4c95963cb0e4ee11693ddaedbc10d1b8.html#a4c95963cb0e4ee11693ddaedbc10d1b8) () const |
|  | |
| void | [Term](class_ak_array_a1c3e5d49f1d4abe0011e7214feef7ade.html#a1c3e5d49f1d4abe0011e7214feef7ade) () |
|  | Term the array. Must be called before destroying the object. [更多...](class_ak_array_a1c3e5d49f1d4abe0011e7214feef7ade.html#a1c3e5d49f1d4abe0011e7214feef7ade) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Length](class_ak_array_a4223a70f7c9d2f560916f69542c33e3a.html#a4223a70f7c9d2f560916f69542c33e3a) () const |
|  | Returns the numbers of items in the array. [更多...](class_ak_array_a4223a70f7c9d2f560916f69542c33e3a.html#a4223a70f7c9d2f560916f69542c33e3a) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > \* | [Data](class_ak_array_a1a6ecd142e90ea19673401efa6cbf1f8.html#a1a6ecd142e90ea19673401efa6cbf1f8) () const |
|  | Returns a pointer to the first item in the array. [更多...](class_ak_array_a1a6ecd142e90ea19673401efa6cbf1f8.html#a1a6ecd142e90ea19673401efa6cbf1f8) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [IsEmpty](class_ak_array_aa14dfd334e046b3ee6977f48836f6899.html#aa14dfd334e046b3ee6977f48836f6899) () const |
|  | Returns true if the number items in the array is 0, false otherwise. [更多...](class_ak_array_aa14dfd334e046b3ee6977f48836f6899.html#aa14dfd334e046b3ee6977f48836f6899) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > \* | [Exists](class_ak_array_a2cfbf1d25465b930c4693dd388eee33c.html#a2cfbf1d25465b930c4693dd388eee33c) (const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > & in\_Item) const |
|  | Returns a pointer to the specified item in the list if it exists, 0 if not found. [更多...](class_ak_array_a2cfbf1d25465b930c4693dd388eee33c.html#a2cfbf1d25465b930c4693dd388eee33c) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > \* | [AddLast](class_ak_array_a9cbeb53af564b1de4d3bc94027beb533.html#a9cbeb53af564b1de4d3bc94027beb533) () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > \* | [AddLast](class_ak_array_a7a7799c25db1d18246cca2046db160b5.html#a7a7799c25db1d18246cca2046db160b5) (const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > & in\_rItem) |
|  | Add an item in the array, and fills it with the provided item. [更多...](class_ak_array_a7a7799c25db1d18246cca2046db160b5.html#a7a7799c25db1d18246cca2046db160b5) |
|  | |
| [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > & | [Last](class_ak_array_a476b8f70171e81aa1e3073d87208e62b.html#a476b8f70171e81aa1e3073d87208e62b) () |
|  | Returns a reference to the last item in the array. [更多...](class_ak_array_a476b8f70171e81aa1e3073d87208e62b.html#a476b8f70171e81aa1e3073d87208e62b) |
|  | |
| void | [RemoveLast](class_ak_array_acda9d49b0ddacf7ee8abafba8171bc4e.html#acda9d49b0ddacf7ee8abafba8171bc4e) () |
|  | Removes the last item from the array. [更多...](class_ak_array_acda9d49b0ddacf7ee8abafba8171bc4e.html#acda9d49b0ddacf7ee8abafba8171bc4e) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Remove](class_ak_array_af2454266e7dfd060a3d09368d8fac6f9.html#af2454266e7dfd060a3d09368d8fac6f9) (const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > & in\_rItem) |
|  | Removes the specified item if found in the array. [更多...](class_ak_array_af2454266e7dfd060a3d09368d8fac6f9.html#af2454266e7dfd060a3d09368d8fac6f9) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [RemoveSwap](class_ak_array_a2c7b5f070faff28432bc83ee9fa9ce07.html#a2c7b5f070faff28432bc83ee9fa9ce07) (const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > & in\_rItem) |
|  | |
| void | [RemoveAll](class_ak_array_acc98dd3b5a2ffccce0d2d9b60f0145ac.html#acc98dd3b5a2ffccce0d2d9b60f0145ac) () |
|  | Removes all items in the array [更多...](class_ak_array_acc98dd3b5a2ffccce0d2d9b60f0145ac.html#acc98dd3b5a2ffccce0d2d9b60f0145ac) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > & | [operator[]](class_ak_array_a674ccbaa0196ab8a48960d12219e8931.html#a674ccbaa0196ab8a48960d12219e8931) (unsigned int uiIndex) const |
|  | Operator [], return a reference to the specified index. [更多...](class_ak_array_a674ccbaa0196ab8a48960d12219e8931.html#a674ccbaa0196ab8a48960d12219e8931) |
|  | |
| Iterator | [Insert](class_ak_array_a1bf66764d17c04dacf18952acf22af0f.html#a1bf66764d17c04dacf18952acf22af0f) (Iterator &in\_rIter) |
|  | |
| [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > \* | [Insert](class_ak_array_aeae936f0202dffcc69c0580586b8d0be.html#aeae936f0202dffcc69c0580586b8d0be) (unsigned int in\_uIndex) |
|  | |
| bool | [GrowArray](class_ak_array_a12d3d7f19cbe16983ceba659b6ec6474.html#a12d3d7f19cbe16983ceba659b6ec6474) () |
|  | |
| bool | [GrowArray](class_ak_array_a79d367ab3400d547014585c735b93771.html#a79d367ab3400d547014585c735b93771) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uGrowBy) |
|  | Resize the array. [更多...](class_ak_array_a79d367ab3400d547014585c735b93771.html#a79d367ab3400d547014585c735b93771) |
|  | |
| bool | [Resize](class_ak_array_add18c32b14499c44e681301e4b4f7fb8.html#add18c32b14499c44e681301e4b4f7fb8) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uiSize) |
|  | Resize the array to the specified size. [更多...](class_ak_array_add18c32b14499c44e681301e4b4f7fb8.html#add18c32b14499c44e681301e4b4f7fb8) |
|  | |
| void | [Transfer](class_ak_array_ae4431acbd7ac6c60412723903387198e.html#ae4431acbd7ac6c60412723903387198e) ([AkArray](class_ak_array.html)< [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA >, const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > &, [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html), [AkGrowByPolicy\_DEFAULT](_ak_array_8h_ae1e32c88be73da730ad49a610b04900d.html#ae1e32c88be73da730ad49a610b04900d), [AkAssignmentMovePolicy](struct_ak_assignment_move_policy.html)< [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > > > &in\_rSource) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Copy](class_ak_array_a8a436cce42c404496e6ebb19072581e6.html#a8a436cce42c404496e6ebb19072581e6) (const [AkArray](class_ak_array.html)< [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA >, const [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > &, [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html), [AkGrowByPolicy\_DEFAULT](_ak_array_8h_ae1e32c88be73da730ad49a610b04900d.html#ae1e32c88be73da730ad49a610b04900d), [AkAssignmentMovePolicy](struct_ak_assignment_move_policy.html)< [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > > > &in\_rSource) |
|  | |
| - Public 成员函数 继承自 [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html) | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [AkPluginArrayAllocator](class_ak_plugin_array_allocator_acfc9f0daec20881eee32d575db63e4d4.html#acfc9f0daec20881eee32d575db63e4d4) () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Init](class_ak_plugin_array_allocator_a3476c037658c433a50660b258231217e.html#a3476c037658c433a50660b258231217e) ([AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Protected 成员函数 继承自 [AkPluginArrayAllocator](class_ak_plugin_array_allocator.html) | |
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
| - Protected 属性 继承自 [AkArray< AkInputMapSlot< KEY, USER\_DATA >, const AkInputMapSlot< KEY, USER\_DATA > &, AkPluginArrayAllocator >](class_ak_array.html) | |
| [AkInputMapSlot](struct_ak_input_map_slot.html)< KEY, USER\_DATA > \* | [m\_pItems](class_ak_array_a28bd3309904f3d7ab56bfd18324f5f0d.html#a28bd3309904f3d7ab56bfd18324f5f0d) |
|  | pointer to the beginning of the array. [更多...](class_ak_array_a28bd3309904f3d7ab56bfd18324f5f0d.html#a28bd3309904f3d7ab56bfd18324f5f0d) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [m\_uLength](class_ak_array_a5a630b46b5edc621f279dc1ce1b51206.html#a5a630b46b5edc621f279dc1ce1b51206) |
|  | number of items in the array. [更多...](class_ak_array_a5a630b46b5edc621f279dc1ce1b51206.html#a5a630b46b5edc621f279dc1ce1b51206) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [m\_ulReserved](class_ak_array_a81f303d0cdf1fd2ee0325da15f215ca9.html#a81f303d0cdf1fd2ee0325da15f215ca9) |
|  | how many we can have at most (currently allocated). [更多...](class_ak_array_a81f303d0cdf1fd2ee0325da15f215ca9.html#a81f303d0cdf1fd2ee0325da15f215ca9) |
|  | |

## 详细描述

### template<class KEY, class USER\_DATA> class AkMixerInputMap< KEY, USER\_DATA >

[AkMixerInputMap](class_ak_mixer_input_map.html "AkMixerInputMap: Map of inputs (identified with AK::IAkMixerInputContext *) to user-defined blocks of..."): Map of inputs (identified with [AK::IAkMixerInputContext](class_a_k_1_1_i_ak_mixer_input_context.html "Interface to retrieve information about an input of a mix connection (for processing during the Speak...") \*) to user-defined blocks of data.

在文件 [AkMixerInputMap.h](_ak_mixer_input_map_8h_source.html) 第 [73](_ak_mixer_input_map_8h_source.html#l00073) 行定义.