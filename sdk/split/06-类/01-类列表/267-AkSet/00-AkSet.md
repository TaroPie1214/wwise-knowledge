# AkSet

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_set-members.html) |
[Public 成员函数](#pub-methods)

AkSet< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > 模板类 参考

`#include <AkSet.h>`

类 AkSet< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > 继承关系图:

![](../../../images/class_ak_set.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| bool | [Contains](class_ak_set_aeff89e507ded2323aba77f4fbf4ebcf6.html#aeff89e507ded2323aba77f4fbf4ebcf6) (T in\_item) const |
|  | |
| - Public 成员函数 继承自 [AkSortedKeyArray< T, T, ArrayPoolDefault, AkSetGetKey< T >, AkGrowByPolicy\_DEFAULT, AkAssignmentMovePolicy< T >, AkDefaultSortedKeyCompare< T > >](class_ak_sorted_key_array.html) | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [Lesser](class_ak_sorted_key_array_ac9337ead7da9db3539a48436823529bf.html#ac9337ead7da9db3539a48436823529bf) (const T &a, const T &b) const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [Equal](class_ak_sorted_key_array_ab1fb5a606831f88a7fcbe7851961644d.html#ab1fb5a606831f88a7fcbe7851961644d) (const T &a, const T &b) const |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetIndex](class_ak_sorted_key_array_aa8fc7ccdbd40c39e2b06b372496cde94.html#aa8fc7ccdbd40c39e2b06b372496cde94) (T \*in\_pItem) const |
|  | |
| T \* | [Exists](class_ak_sorted_key_array_a37325585cbaab4c08039bf03025bacec.html#a37325585cbaab4c08039bf03025bacec) (T in\_key) const |
|  | |
| T \* | [Add](class_ak_sorted_key_array_aba211b8dad101c066dc6811cb2d477e1.html#aba211b8dad101c066dc6811cb2d477e1) (T in\_key) |
|  | |
| T \* | [AddNoSetKey](class_ak_sorted_key_array_a094841aa29d007b7e75dd29b089608d3.html#a094841aa29d007b7e75dd29b089608d3) (T in\_key) |
|  | |
| T \* | [AddNoSetKey](class_ak_sorted_key_array_a3c2db41b7ea6c0143a5f25c9baac50c2.html#a3c2db41b7ea6c0143a5f25c9baac50c2) (T in\_key, bool &out\_bFound) |
|  | |
| T \* | [Set](class_ak_sorted_key_array_ad9cd0f49cead55898c0713d4326c2ee5.html#ad9cd0f49cead55898c0713d4326c2ee5) (T in\_key) |
|  | |
| T \* | [Set](class_ak_sorted_key_array_aaa5e71c7de37bc9618e809d066dd9162.html#aaa5e71c7de37bc9618e809d066dd9162) (T in\_key, bool &out\_bExists) |
|  | |
| bool | [Unset](class_ak_sorted_key_array_abbd71ea649f2abcddda01ef0bb62d428.html#abbd71ea649f2abcddda01ef0bb62d428) (T in\_key) |
|  | |
| bool | [SortedUpdate](class_ak_sorted_key_array_afa252d5aa59b60e8ece68607b960fa33.html#afa252d5aa59b60e8ece68607b960fa33) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_numUpdates, const T\_UPDATE \*in\_pUpdates, FN\_EXISTS in\_fnExists, FN\_NEW in\_fnNew, FN\_OLD in\_fnOld) |
|  | |
| void | [Reorder](class_ak_sorted_key_array_a890a39352434136ebcdea1d424fd4831.html#a890a39352434136ebcdea1d424fd4831) (T in\_OldKey, T in\_NewKey, const T &in\_item) |
|  | |
| void | [ReSortArray](class_ak_sorted_key_array_a2fa8617bbcffca57503527c46e3f1ca0.html#a2fa8617bbcffca57503527c46e3f1ca0) () |
|  | |
| T \* | [BinarySearch](class_ak_sorted_key_array_a506112b0af11a501a519c15951e8ba0d.html#a506112b0af11a501a519c15951e8ba0d) (T in\_key, bool &out\_bFound) const |
|  | |
| T \* | [LowerBounds](class_ak_sorted_key_array_a4920948338a03ef7785139a2558d86b3.html#a4920948338a03ef7785139a2558d86b3) (T in\_key) const |
|  | |
| T \* | [LowerBounds](class_ak_sorted_key_array_ac75c1dc238b96a90c662ca8c7aa5c3b1.html#ac75c1dc238b96a90c662ca8c7aa5c3b1) (T in\_key, [Iterator](class_ak_sorted_key_array_a3cf521df7596b95e5456d39798a4b393.html#a3cf521df7596b95e5456d39798a4b393) in\_from, [Iterator](class_ak_sorted_key_array_a3cf521df7596b95e5456d39798a4b393.html#a3cf521df7596b95e5456d39798a4b393) in\_to) const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Swap](class_ak_sorted_key_array_a071c81517a31f192cf4af8f60628cc28.html#a071c81517a31f192cf4af8f60628cc28) (T \*in\_ItemA, T \*in\_ItemB) |
|  | |
| - Public 成员函数 继承自 [AkArray< T, const T &, ArrayPoolDefault, AkGrowByPolicy\_DEFAULT, AkAssignmentMovePolicy< T > >](class_ak_array.html) | |
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
| Iterator | [FindEx](class_ak_array_a5e2ab9cb3de65d194b92bd2328a7d5b0.html#a5e2ab9cb3de65d194b92bd2328a7d5b0) (const T & in\_Item) const |
|  | Returns the iterator th the specified item, will be [End()](class_ak_array_a8b3f475890ba0b28b1ee26ef26835789.html#a8b3f475890ba0b28b1ee26ef26835789 "Returns the iterator to the end of the array") if the item is not found [更多...](class_ak_array_a5e2ab9cb3de65d194b92bd2328a7d5b0.html#a5e2ab9cb3de65d194b92bd2328a7d5b0) |
|  | |
| Iterator | [BinarySearch](class_ak_array_a21687ba2fac7670b6ed2b84e4196ef73.html#a21687ba2fac7670b6ed2b84e4196ef73) (const T & in\_Item) const |
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
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T \* | [Data](class_ak_array_a1a6ecd142e90ea19673401efa6cbf1f8.html#a1a6ecd142e90ea19673401efa6cbf1f8) () const |
|  | Returns a pointer to the first item in the array. [更多...](class_ak_array_a1a6ecd142e90ea19673401efa6cbf1f8.html#a1a6ecd142e90ea19673401efa6cbf1f8) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [IsEmpty](class_ak_array_aa14dfd334e046b3ee6977f48836f6899.html#aa14dfd334e046b3ee6977f48836f6899) () const |
|  | Returns true if the number items in the array is 0, false otherwise. [更多...](class_ak_array_aa14dfd334e046b3ee6977f48836f6899.html#aa14dfd334e046b3ee6977f48836f6899) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T \* | [Exists](class_ak_array_a2cfbf1d25465b930c4693dd388eee33c.html#a2cfbf1d25465b930c4693dd388eee33c) (const T & in\_Item) const |
|  | Returns a pointer to the specified item in the list if it exists, 0 if not found. [更多...](class_ak_array_a2cfbf1d25465b930c4693dd388eee33c.html#a2cfbf1d25465b930c4693dd388eee33c) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T \* | [AddLast](class_ak_array_a9cbeb53af564b1de4d3bc94027beb533.html#a9cbeb53af564b1de4d3bc94027beb533) () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T \* | [AddLast](class_ak_array_a7a7799c25db1d18246cca2046db160b5.html#a7a7799c25db1d18246cca2046db160b5) (const T & in\_rItem) |
|  | Add an item in the array, and fills it with the provided item. [更多...](class_ak_array_a7a7799c25db1d18246cca2046db160b5.html#a7a7799c25db1d18246cca2046db160b5) |
|  | |
| T & | [Last](class_ak_array_a476b8f70171e81aa1e3073d87208e62b.html#a476b8f70171e81aa1e3073d87208e62b) () |
|  | Returns a reference to the last item in the array. [更多...](class_ak_array_a476b8f70171e81aa1e3073d87208e62b.html#a476b8f70171e81aa1e3073d87208e62b) |
|  | |
| void | [RemoveLast](class_ak_array_acda9d49b0ddacf7ee8abafba8171bc4e.html#acda9d49b0ddacf7ee8abafba8171bc4e) () |
|  | Removes the last item from the array. [更多...](class_ak_array_acda9d49b0ddacf7ee8abafba8171bc4e.html#acda9d49b0ddacf7ee8abafba8171bc4e) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Remove](class_ak_array_af2454266e7dfd060a3d09368d8fac6f9.html#af2454266e7dfd060a3d09368d8fac6f9) (const T & in\_rItem) |
|  | Removes the specified item if found in the array. [更多...](class_ak_array_af2454266e7dfd060a3d09368d8fac6f9.html#af2454266e7dfd060a3d09368d8fac6f9) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [RemoveSwap](class_ak_array_a2c7b5f070faff28432bc83ee9fa9ce07.html#a2c7b5f070faff28432bc83ee9fa9ce07) (const T & in\_rItem) |
|  | |
| void | [RemoveAll](class_ak_array_acc98dd3b5a2ffccce0d2d9b60f0145ac.html#acc98dd3b5a2ffccce0d2d9b60f0145ac) () |
|  | Removes all items in the array [更多...](class_ak_array_acc98dd3b5a2ffccce0d2d9b60f0145ac.html#acc98dd3b5a2ffccce0d2d9b60f0145ac) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T & | [operator[]](class_ak_array_a674ccbaa0196ab8a48960d12219e8931.html#a674ccbaa0196ab8a48960d12219e8931) (unsigned int uiIndex) const |
|  | Operator [], return a reference to the specified index. [更多...](class_ak_array_a674ccbaa0196ab8a48960d12219e8931.html#a674ccbaa0196ab8a48960d12219e8931) |
|  | |
| Iterator | [Insert](class_ak_array_a1bf66764d17c04dacf18952acf22af0f.html#a1bf66764d17c04dacf18952acf22af0f) (Iterator &in\_rIter) |
|  | |
| T \* | [Insert](class_ak_array_aeae936f0202dffcc69c0580586b8d0be.html#aeae936f0202dffcc69c0580586b8d0be) (unsigned int in\_uIndex) |
|  | |
| bool | [GrowArray](class_ak_array_a12d3d7f19cbe16983ceba659b6ec6474.html#a12d3d7f19cbe16983ceba659b6ec6474) () |
|  | |
| bool | [GrowArray](class_ak_array_a79d367ab3400d547014585c735b93771.html#a79d367ab3400d547014585c735b93771) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uGrowBy) |
|  | Resize the array. [更多...](class_ak_array_a79d367ab3400d547014585c735b93771.html#a79d367ab3400d547014585c735b93771) |
|  | |
| bool | [Resize](class_ak_array_add18c32b14499c44e681301e4b4f7fb8.html#add18c32b14499c44e681301e4b4f7fb8) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uiSize) |
|  | Resize the array to the specified size. [更多...](class_ak_array_add18c32b14499c44e681301e4b4f7fb8.html#add18c32b14499c44e681301e4b4f7fb8) |
|  | |
| void | [Transfer](class_ak_array_ae4431acbd7ac6c60412723903387198e.html#ae4431acbd7ac6c60412723903387198e) ([AkArray](class_ak_array.html)< T, const T &, [ArrayPoolDefault](_ak_array_8h_a6d1995f92ec49c35784181225575438f.html#a6d1995f92ec49c35784181225575438f), [AkGrowByPolicy\_DEFAULT](_ak_array_8h_ae1e32c88be73da730ad49a610b04900d.html#ae1e32c88be73da730ad49a610b04900d), [AkAssignmentMovePolicy](struct_ak_assignment_move_policy.html)< T > > &in\_rSource) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Copy](class_ak_array_a8a436cce42c404496e6ebb19072581e6.html#a8a436cce42c404496e6ebb19072581e6) (const [AkArray](class_ak_array.html)< T, const T &, [ArrayPoolDefault](_ak_array_8h_a6d1995f92ec49c35784181225575438f.html#a6d1995f92ec49c35784181225575438f), [AkGrowByPolicy\_DEFAULT](_ak_array_8h_ae1e32c88be73da730ad49a610b04900d.html#ae1e32c88be73da730ad49a610b04900d), [AkAssignmentMovePolicy](struct_ak_assignment_move_policy.html)< T > > &in\_rSource) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 类型 继承自 [AkSortedKeyArray< T, T, ArrayPoolDefault, AkSetGetKey< T >, AkGrowByPolicy\_DEFAULT, AkAssignmentMovePolicy< T >, AkDefaultSortedKeyCompare< T > >](class_ak_sorted_key_array.html) | |
| using | [base](class_ak_sorted_key_array_a59c4d194dbb3c0e988e96ba10c181503.html#a59c4d194dbb3c0e988e96ba10c181503) = [AkArray](class_ak_array.html)< T, const T &, [ArrayPoolDefault](_ak_array_8h_a6d1995f92ec49c35784181225575438f.html#a6d1995f92ec49c35784181225575438f), [AkGrowByPolicy\_DEFAULT](_ak_array_8h_ae1e32c88be73da730ad49a610b04900d.html#ae1e32c88be73da730ad49a610b04900d), [AkAssignmentMovePolicy](struct_ak_assignment_move_policy.html)< T > > |
|  | |
| using | [Iterator](class_ak_sorted_key_array_a3cf521df7596b95e5456d39798a4b393.html#a3cf521df7596b95e5456d39798a4b393) = typename base::Iterator |
|  | |
| - 静态 Public 成员函数 继承自 [AkArrayAllocatorNoAlign< T\_MEMID >](struct_ak_array_allocator_no_align.html) | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [Alloc](struct_ak_array_allocator_no_align_a572d7f65fd546fce3dd949c48f2ba568.html#a572d7f65fd546fce3dd949c48f2ba568) (size\_t in\_uSize) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [ReAlloc](struct_ak_array_allocator_no_align_aac15f21c37c5da42bfa1db7060d2f30c.html#aac15f21c37c5da42bfa1db7060d2f30c) (void \*in\_pCurrent, size\_t in\_uOldSize, size\_t in\_uNewSize) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Free](struct_ak_array_allocator_no_align_a090f613bd8846bc436d4e9e562d5d8cc.html#a090f613bd8846bc436d4e9e562d5d8cc) (void \*in\_pAddress) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [TransferMem](struct_ak_array_allocator_no_align_a7dd951bf506402f04e0ea453da9bd8a0.html#a7dd951bf506402f04e0ea453da9bd8a0) (void \*&io\_pDest, [AkArrayAllocatorNoAlign](struct_ak_array_allocator_no_align.html)< T\_MEMID > in\_srcAlloc, void \*in\_pSrc) |
|  | |
| - Protected 属性 继承自 [AkArray< T, const T &, ArrayPoolDefault, AkGrowByPolicy\_DEFAULT, AkAssignmentMovePolicy< T > >](class_ak_array.html) | |
| T \* | [m\_pItems](class_ak_array_a28bd3309904f3d7ab56bfd18324f5f0d.html#a28bd3309904f3d7ab56bfd18324f5f0d) |
|  | pointer to the beginning of the array. [更多...](class_ak_array_a28bd3309904f3d7ab56bfd18324f5f0d.html#a28bd3309904f3d7ab56bfd18324f5f0d) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [m\_uLength](class_ak_array_a5a630b46b5edc621f279dc1ce1b51206.html#a5a630b46b5edc621f279dc1ce1b51206) |
|  | number of items in the array. [更多...](class_ak_array_a5a630b46b5edc621f279dc1ce1b51206.html#a5a630b46b5edc621f279dc1ce1b51206) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [m\_ulReserved](class_ak_array_a81f303d0cdf1fd2ee0325da15f215ca9.html#a81f303d0cdf1fd2ee0325da15f215ca9) |
|  | how many we can have at most (currently allocated). [更多...](class_ak_array_a81f303d0cdf1fd2ee0325da15f215ca9.html#a81f303d0cdf1fd2ee0325da15f215ca9) |
|  | |

## 详细描述

### template<typename T, class U\_POOL = ArrayPoolDefault, class uGrowBy = AkGrowByPolicy\_DEFAULT, class TMovePolicy = AkAssignmentMovePolicy<T>, class TComparePolicy = AkDefaultSortedKeyCompare<T>> class AkSet< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy >

在文件 [AkSet.h](_ak_set_8h_source.html) 第 [57](_ak_set_8h_source.html#l00057) 行定义.