# AkHashList.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[函数](#func-members) |
[变量](#var-members)

AkHashList.h 文件参考

`#include <AK/Tools/Common/AkArray.h>`  
`#include <AK/Tools/Common/AkKeyDef.h>`  
`#include <AK/Tools/Common/AkPlacementNew.h>`

[浏览源代码.](_ak_hash_list_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >](class_ak_hash_list.html) |
|  | |
| struct | [AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >::Item](struct_ak_hash_list_1_1_item.html) |
|  | |
| struct | [AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >::Iterator](struct_ak_hash_list_1_1_iterator.html) |
|  | |
| struct | [AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >::ConstIterator](struct_ak_hash_list_1_1_const_iterator.html) |
|  | |
| struct | [AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >::IteratorEx](struct_ak_hash_list_1_1_iterator_ex.html) |
|  | |
| struct | [AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >::ConstIteratorEx](struct_ak_hash_list_1_1_const_iterator_ex.html) |
|  | |
| struct | [AkHashListBareMemberPolicy< T\_KEY, T\_MAPSTRUCT >](struct_ak_hash_list_bare_member_policy.html) |
|  | |
| struct | [AkHashListBareFuncPolicy< T\_KEY, T\_MAPSTRUCT >](struct_ak_hash_list_bare_func_policy.html) |
|  | |
| class | [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >](class_ak_hash_list_bare.html) |
|  | |
| struct | [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::Iterator](struct_ak_hash_list_bare_1_1_iterator.html) |
|  | |
| struct | [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::ConstIterator](struct_ak_hash_list_bare_1_1_const_iterator.html) |
|  | |
| struct | [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::IteratorEx](struct_ak_hash_list_bare_1_1_iterator_ex.html) |
|  | |
| struct | [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::ConstIteratorEx](struct_ak_hash_list_bare_1_1_const_iterator_ex.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_HASH\_SIZE\_VERY\_SMALL](_ak_hash_list_8h_a93553137c136e12e13b27283b317e1e5.html#a93553137c136e12e13b27283b317e1e5)   11 |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) |
|  | |
| template<class T\_KEY , class T\_MAPSTRUCT > | |
| using | [AkDefaultHashListBarePolicy](_ak_hash_list_8h_add6e5990e83597cd7194b237de2f1c96.html#add6e5990e83597cd7194b237de2f1c96) = [AkHashListBareMemberPolicy](struct_ak_hash_list_bare_member_policy.html)< T\_KEY, T\_MAPSTRUCT > |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| template<class T\_KEY > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) | [AkHash](_ak_hash_list_8h_a8b7677c6a6fa728a10f13d34e85335af.html#a8b7677c6a6fa728a10f13d34e85335af) (T\_KEY in\_key) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| const [AK\_SELECTANY](_ak_platforms_8h_aace42721bf834d460bc43bf1c87c7c67.html#aace42721bf834d460bc43bf1c87c7c67) [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) | [kHashSizes](_ak_hash_list_8h_a0217cf461cf5b442bd30c557fe4a9a6e.html#a0217cf461cf5b442bd30c557fe4a9a6e) [] = { 29, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741 } |
|  | |
| constexpr size\_t | [kNumHashSizes](_ak_hash_list_8h_a6d37fff280ec5e5d2eba03dcbe3c40dd.html#a6d37fff280ec5e5d2eba03dcbe3c40dd) = sizeof([kHashSizes](_ak_hash_list_8h_a0217cf461cf5b442bd30c557fe4a9a6e.html#a0217cf461cf5b442bd30c557fe4a9a6e)) / sizeof([kHashSizes](_ak_hash_list_8h_a0217cf461cf5b442bd30c557fe4a9a6e.html#a0217cf461cf5b442bd30c557fe4a9a6e)[0]) |
|  | |
| constexpr [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [kHashTableGrowthFactor](_ak_hash_list_8h_ac75bd58235b536b2a2b8fdeaac1d117b.html#ac75bd58235b536b2a2b8fdeaac1d117b) = 0.9f |
|  | |