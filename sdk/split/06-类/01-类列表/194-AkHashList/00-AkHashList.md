# AkHashList

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_hash_list-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods) |
[Protected 属性](#pro-attribs)

AkHashList< T\_KEY, T\_ITEM, T\_ALLOC > 模板类 参考

`#include <AkHashList.h>`

类 AkHashList< T\_KEY, T\_ITEM, T\_ALLOC > 继承关系图:

![](../../../images/class_ak_hash_list.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [ConstIterator](struct_ak_hash_list_1_1_const_iterator.html) |
|  | |
| struct | [ConstIteratorEx](struct_ak_hash_list_1_1_const_iterator_ex.html) |
|  | |
| struct | [Item](struct_ak_hash_list_1_1_item.html) |
|  | |
| struct | [Iterator](struct_ak_hash_list_1_1_iterator.html) |
|  | |
| struct | [IteratorEx](struct_ak_hash_list_1_1_iterator_ex.html) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| typedef [AkArray](class_ak_array.html)< [Item](struct_ak_hash_list_1_1_item.html) \*, [Item](struct_ak_hash_list_1_1_item.html) \*, T\_ALLOC, [AkGrowByPolicy\_NoGrow](struct_ak_grow_by_policy___no_grow.html) > | [HashTableArray](class_ak_hash_list_ac85351466e0d949d8951813f0b5ca064.html#ac85351466e0d949d8951813f0b5ca064) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [Iterator](struct_ak_hash_list_1_1_iterator.html) | [Begin](class_ak_hash_list_ad52e9b8e65173711f3ecb8de5ee61da1.html#ad52e9b8e65173711f3ecb8de5ee61da1) () |
|  | |
| [ConstIterator](struct_ak_hash_list_1_1_const_iterator.html) | [Begin](class_ak_hash_list_a35aa8c4245ebd419763176a244443686.html#a35aa8c4245ebd419763176a244443686) () const |
|  | |
| [IteratorEx](struct_ak_hash_list_1_1_iterator_ex.html) | [BeginEx](class_ak_hash_list_a27a1f0e73052b2c0620e0343741bfefa.html#a27a1f0e73052b2c0620e0343741bfefa) () |
|  | |
| [ConstIteratorEx](struct_ak_hash_list_1_1_const_iterator_ex.html) | [BeginEx](class_ak_hash_list_ad0485a2f251eccf2e526f2e438ce4d59.html#ad0485a2f251eccf2e526f2e438ce4d59) () const |
|  | |
| [Iterator](struct_ak_hash_list_1_1_iterator.html) | [End](class_ak_hash_list_a379b577f8b65b605c4f2727d858e6f0f.html#a379b577f8b65b605c4f2727d858e6f0f) () |
|  | |
| [ConstIterator](struct_ak_hash_list_1_1_const_iterator.html) | [End](class_ak_hash_list_ae3911e5de46a249f2bfc4fbd1ef1e4a9.html#ae3911e5de46a249f2bfc4fbd1ef1e4a9) () const |
|  | |
| [IteratorEx](struct_ak_hash_list_1_1_iterator_ex.html) | [EndEx](class_ak_hash_list_a40e35b98d8c0446933ab566a8e42ecf7.html#a40e35b98d8c0446933ab566a8e42ecf7) () |
|  | |
| [ConstIterator](struct_ak_hash_list_1_1_const_iterator.html) | [EndEx](class_ak_hash_list_a5da7589d16ebe33029919b12aed7e0dc.html#a5da7589d16ebe33029919b12aed7e0dc) () const |
|  | |
| [IteratorEx](struct_ak_hash_list_1_1_iterator_ex.html) | [FindEx](class_ak_hash_list_a1907b9de7f8d3c584c376751986b89a9.html#a1907b9de7f8d3c584c376751986b89a9) (T\_KEY in\_Key) |
|  | |
| [ConstIteratorEx](struct_ak_hash_list_1_1_const_iterator_ex.html) | [FindEx](class_ak_hash_list_a430483a03b225b73984d6635784420d6.html#a430483a03b225b73984d6635784420d6) (T\_KEY in\_Key) const |
|  | |
|  | [AkHashList](class_ak_hash_list_a1639e9d09dcd918d663402288845af14.html#a1639e9d09dcd918d663402288845af14) () |
|  | |
|  | [~AkHashList](class_ak_hash_list_a55f04d4ac5ad0bca7e888d2e3504a271.html#a55f04d4ac5ad0bca7e888d2e3504a271) () |
|  | |
| void | [Term](class_ak_hash_list_a1202251fcebd89562b1b609e7c6214ec.html#a1202251fcebd89562b1b609e7c6214ec) () |
|  | |
| void | [RemoveAll](class_ak_hash_list_a97f26a6f23fdcb796fd7a0babc3bdb94.html#a97f26a6f23fdcb796fd7a0babc3bdb94) () |
|  | |
| T\_ITEM \* | [Exists](class_ak_hash_list_a114b642f2e8899819a8b70065aacac48.html#a114b642f2e8899819a8b70065aacac48) (T\_KEY in\_Key) |
|  | |
| T\_ITEM \* | [Set](class_ak_hash_list_a79a10ce2cacdfeadfee4bae6a5987e7e.html#a79a10ce2cacdfeadfee4bae6a5987e7e) ([Item](struct_ak_hash_list_1_1_item.html) \*in\_pItem) |
|  | |
| T\_ITEM \* | [Set](class_ak_hash_list_a1662ea40e98bab543b2a739ded85d616.html#a1662ea40e98bab543b2a739ded85d616) (T\_KEY in\_Key) |
|  | |
| T\_ITEM \* | [Set](class_ak_hash_list_aac5799e80ee624005690e6fecfd9bb7d.html#aac5799e80ee624005690e6fecfd9bb7d) (T\_KEY in\_Key, bool &out\_bWasAlreadyThere) |
|  | |
| void | [Unset](class_ak_hash_list_a84f92a8f2242cad615786a0b219f1346.html#a84f92a8f2242cad615786a0b219f1346) (T\_KEY in\_Key) |
|  | |
| [IteratorEx](struct_ak_hash_list_1_1_iterator_ex.html) | [Erase](class_ak_hash_list_ac10a4f996f5fd4fae210e64b9f7ca397.html#ac10a4f996f5fd4fae210e64b9f7ca397) (const [IteratorEx](struct_ak_hash_list_1_1_iterator_ex.html) &in\_rIter) |
|  | |
| void | [RemoveItem](class_ak_hash_list_a3cf5b22a7369ade3a98fc9ace00d94f4.html#a3cf5b22a7369ade3a98fc9ace00d94f4) ([AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) in\_uiTable, [Item](struct_ak_hash_list_1_1_item.html) \*in\_pItem, [Item](struct_ak_hash_list_1_1_item.html) \*in\_pPrevItem) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Length](class_ak_hash_list_ac38c86434791bfae6d9a838886e50d0d.html#ac38c86434791bfae6d9a838886e50d0d) () const |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Reserve](class_ak_hash_list_a7135fbdae4b5b8091e2ba72cd31f6bfb.html#a7135fbdae4b5b8091e2ba72cd31f6bfb) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumberOfEntires) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Resize](class_ak_hash_list_adaf78ec0e8cba8b3f520a5d1f239c057.html#adaf78ec0e8cba8b3f520a5d1f239c057) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uExpectedNumberOfEntires) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [HashSize](class_ak_hash_list_a86b4380d81f599f569ebc1e7c237ecd8.html#a86b4380d81f599f569ebc1e7c237ecd8) () const |
|  | |
| bool | [CheckSize](class_ak_hash_list_a108457650bcb423cfda415dae19251bb.html#a108457650bcb423cfda415dae19251bb) () |
|  | |
| void | [Transfer](class_ak_hash_list_adc989289e96b2e44fa693af8eec2ef58.html#adc989289e96b2e44fa693af8eec2ef58) ([AkHashList](class_ak_hash_list.html)< T\_KEY, T\_ITEM, T\_ALLOC > &in\_source) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| T\_ITEM \* | [ExistsInList](class_ak_hash_list_a5331e4cd5362e2af5efb0b3751469936.html#a5331e4cd5362e2af5efb0b3751469936) (T\_KEY in\_Key, [AkUIntPtr](_ak_numeral_types_8h_aba972f179e9ca267106fac77b6d3c78b.html#aba972f179e9ca267106fac77b6d3c78b) in\_uiTable) |
|  | |
| T\_ITEM \* | [CreateEntry](class_ak_hash_list_a9ca635e06eeadec90d7ffd198ed7ad42.html#a9ca635e06eeadec90d7ffd198ed7ad42) (T\_KEY in\_Key, [AkUIntPtr](_ak_numeral_types_8h_aba972f179e9ca267106fac77b6d3c78b.html#aba972f179e9ca267106fac77b6d3c78b) in\_uiTable) |
|  | |

|  |  |
| --- | --- |
| Protected 属性 | |
| [HashTableArray](class_ak_hash_list_ac85351466e0d949d8951813f0b5ca064.html#ac85351466e0d949d8951813f0b5ca064) | [m\_table](class_ak_hash_list_a8b088625d2719f35ce8f7e32a769e329.html#a8b088625d2719f35ce8f7e32a769e329) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [m\_uiSize](class_ak_hash_list_a683500f23e1a8573b420b43e6fcb58f2.html#a683500f23e1a8573b420b43e6fcb58f2) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 成员函数 继承自 [AkArrayAllocatorNoAlign< T\_MEMID >](struct_ak_array_allocator_no_align.html) | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [Alloc](struct_ak_array_allocator_no_align_a572d7f65fd546fce3dd949c48f2ba568.html#a572d7f65fd546fce3dd949c48f2ba568) (size\_t in\_uSize) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [ReAlloc](struct_ak_array_allocator_no_align_aac15f21c37c5da42bfa1db7060d2f30c.html#aac15f21c37c5da42bfa1db7060d2f30c) (void \*in\_pCurrent, size\_t in\_uOldSize, size\_t in\_uNewSize) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Free](struct_ak_array_allocator_no_align_a090f613bd8846bc436d4e9e562d5d8cc.html#a090f613bd8846bc436d4e9e562d5d8cc) (void \*in\_pAddress) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [TransferMem](struct_ak_array_allocator_no_align_a7dd951bf506402f04e0ea453da9bd8a0.html#a7dd951bf506402f04e0ea453da9bd8a0) (void \*&io\_pDest, [AkArrayAllocatorNoAlign](struct_ak_array_allocator_no_align.html)< T\_MEMID > in\_srcAlloc, void \*in\_pSrc) |
|  | |

## 详细描述

### template<class T\_KEY, class T\_ITEM, typename T\_ALLOC = ArrayPoolDefault> class AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >

在文件 [AkHashList.h](_ak_hash_list_8h_source.html) 第 [49](_ak_hash_list_8h_source.html#l00049) 行定义.