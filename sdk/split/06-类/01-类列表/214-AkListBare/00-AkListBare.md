# AkListBare

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_list_bare-members.html) |
[类](#nested-classes) |
[Public 成员函数](#pub-methods) |
[Protected 属性](#pro-attribs)

AkListBare< T, U\_NEXTITEM, COUNT\_POLICY, LAST\_POLICY > 模板类 参考

Implementation of List Bare.
[更多...](class_ak_list_bare.html#details)

`#include <AkListBare.h>`

类 AkListBare< T, U\_NEXTITEM, COUNT\_POLICY, LAST\_POLICY > 继承关系图:

![](../../../images/class_ak_list_bare.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Iterator](struct_ak_list_bare_1_1_iterator.html) |
|  | [Iterator](struct_ak_list_bare_1_1_iterator.html "Iterator."). [更多...](struct_ak_list_bare_1_1_iterator.html#details) |
|  | |
| struct | [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) | [Erase](class_ak_list_bare_a421a2455c303e5c68da8cd9b4f6ceef4.html#a421a2455c303e5c68da8cd9b4f6ceef4) (const [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) &in\_rIter) |
|  | Erase item. [更多...](class_ak_list_bare_a421a2455c303e5c68da8cd9b4f6ceef4.html#a421a2455c303e5c68da8cd9b4f6ceef4) |
|  | |
| [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) | [Insert](class_ak_list_bare_ac1d669343a70a862063aba70352a2b02.html#ac1d669343a70a862063aba70352a2b02) (const [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) &in\_rIter, T \*in\_pItem) |
|  | Insert item. [更多...](class_ak_list_bare_ac1d669343a70a862063aba70352a2b02.html#ac1d669343a70a862063aba70352a2b02) |
|  | |
| [Iterator](struct_ak_list_bare_1_1_iterator.html) | [End](class_ak_list_bare_abee0902b77bd212900c0d2a6da4b42be.html#abee0902b77bd212900c0d2a6da4b42be) () const |
|  | End condition. [更多...](class_ak_list_bare_abee0902b77bd212900c0d2a6da4b42be.html#abee0902b77bd212900c0d2a6da4b42be) |
|  | |
| [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) | [BeginEx](class_ak_list_bare_a6bfce524076fb933a7f901afff1d41b7.html#a6bfce524076fb933a7f901afff1d41b7) () |
|  | Get [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) at beginning. [更多...](class_ak_list_bare_a6bfce524076fb933a7f901afff1d41b7.html#a6bfce524076fb933a7f901afff1d41b7) |
|  | |
| [Iterator](struct_ak_list_bare_1_1_iterator.html) | [Begin](class_ak_list_bare_a1d42b43870be3eaad786451e6d012774.html#a1d42b43870be3eaad786451e6d012774) () const |
|  | Get [Iterator](struct_ak_list_bare_1_1_iterator.html "Iterator.") at beginning. [更多...](class_ak_list_bare_a1d42b43870be3eaad786451e6d012774.html#a1d42b43870be3eaad786451e6d012774) |
|  | |
| [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) | [FindEx](class_ak_list_bare_ae27e974c2928853d0d4839c42c7b48dd.html#ae27e974c2928853d0d4839c42c7b48dd) (T \*in\_pItem) |
|  | Get [Iterator](struct_ak_list_bare_1_1_iterator.html "Iterator.") from item. [更多...](class_ak_list_bare_ae27e974c2928853d0d4839c42c7b48dd.html#ae27e974c2928853d0d4839c42c7b48dd) |
|  | |
|  | [AkListBare](class_ak_list_bare_a4c5efadb568069e4e1ce22146c6070d7.html#a4c5efadb568069e4e1ce22146c6070d7) () |
|  | Constructor. [更多...](class_ak_list_bare_a4c5efadb568069e4e1ce22146c6070d7.html#a4c5efadb568069e4e1ce22146c6070d7) |
|  | |
|  | [~AkListBare](class_ak_list_bare_a8feb3dc74cdfecc400fa9cb975ab5575.html#a8feb3dc74cdfecc400fa9cb975ab5575) () |
|  | Destructor. [更多...](class_ak_list_bare_a8feb3dc74cdfecc400fa9cb975ab5575.html#a8feb3dc74cdfecc400fa9cb975ab5575) |
|  | |
| void | [Term](class_ak_list_bare_a0f8b38d5752a8ee2c8c4b0bfa2c4a7b3.html#a0f8b38d5752a8ee2c8c4b0bfa2c4a7b3) () |
|  | Terminate. [更多...](class_ak_list_bare_a0f8b38d5752a8ee2c8c4b0bfa2c4a7b3.html#a0f8b38d5752a8ee2c8c4b0bfa2c4a7b3) |
|  | |
| void | [AddFirst](class_ak_list_bare_a8be1984b23edf5ea4e4f8814969dc5d8.html#a8be1984b23edf5ea4e4f8814969dc5d8) (T \*in\_pItem) |
|  | Add element at the beginning of list. [更多...](class_ak_list_bare_a8be1984b23edf5ea4e4f8814969dc5d8.html#a8be1984b23edf5ea4e4f8814969dc5d8) |
|  | |
| void | [AddLast](class_ak_list_bare_ae7e622ace5a76dc196cfeef34974b43c.html#ae7e622ace5a76dc196cfeef34974b43c) (T \*in\_pItem) |
|  | Add element at the end of list. [更多...](class_ak_list_bare_ae7e622ace5a76dc196cfeef34974b43c.html#ae7e622ace5a76dc196cfeef34974b43c) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Remove](class_ak_list_bare_adcdd2e307860eb45843f84b3f68c358b.html#adcdd2e307860eb45843f84b3f68c358b) (T \*in\_pItem) |
|  | Remove an element. [更多...](class_ak_list_bare_adcdd2e307860eb45843f84b3f68c358b.html#adcdd2e307860eb45843f84b3f68c358b) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [RemoveFirst](class_ak_list_bare_a17d3b4993799862a1c883b5e08040e99.html#a17d3b4993799862a1c883b5e08040e99) () |
|  | Remove the first element. [更多...](class_ak_list_bare_a17d3b4993799862a1c883b5e08040e99.html#a17d3b4993799862a1c883b5e08040e99) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [RemoveAll](class_ak_list_bare_aeb9b40c21be73f04a8976515d21f14f7.html#aeb9b40c21be73f04a8976515d21f14f7) () |
|  | Remove all elements. [更多...](class_ak_list_bare_aeb9b40c21be73f04a8976515d21f14f7.html#aeb9b40c21be73f04a8976515d21f14f7) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T \* | [First](class_ak_list_bare_a56d47d502d782af5caeb57c8bbef33fb.html#a56d47d502d782af5caeb57c8bbef33fb) () |
|  | Get first element. [更多...](class_ak_list_bare_a56d47d502d782af5caeb57c8bbef33fb.html#a56d47d502d782af5caeb57c8bbef33fb) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [IsEmpty](class_ak_list_bare_a9e435cf73393a789d7292a9810cdb72e.html#a9e435cf73393a789d7292a9810cdb72e) () const |
|  | Empty condition. [更多...](class_ak_list_bare_a9e435cf73393a789d7292a9810cdb72e.html#a9e435cf73393a789d7292a9810cdb72e) |
|  | |
| void | [RemoveItem](class_ak_list_bare_ab1650d11da65848b47d9ff5a088a7d56.html#ab1650d11da65848b47d9ff5a088a7d56) (T \*in\_pItem, T \*in\_pPrevItem) |
|  | Remove an element. [更多...](class_ak_list_bare_ab1650d11da65848b47d9ff5a088a7d56.html#ab1650d11da65848b47d9ff5a088a7d56) |
|  | |
| void | [AddItem](class_ak_list_bare_a641ac438e43df107500ae763d269fc75.html#a641ac438e43df107500ae763d269fc75) (T \*in\_pItem, T \*in\_pNextItem, T \*in\_pPrevItem) |
|  | Add an element. [更多...](class_ak_list_bare_a641ac438e43df107500ae763d269fc75.html#a641ac438e43df107500ae763d269fc75) |
|  | |
| void | [Transfer](class_ak_list_bare_a19b84234e28a59deb4bc8adfadbff5d1.html#a19b84234e28a59deb4bc8adfadbff5d1) ([AkListBare](class_ak_list_bare.html)< T, U\_NEXTITEM, COUNT\_POLICY, LAST\_POLICY > &in\_src) |
|  | |
| - Public 成员函数 继承自 [AkLastPolicyWithLast< T >](class_ak_last_policy_with_last.html) | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T \* | [Last](class_ak_last_policy_with_last_a46fcbabc609e3d24abd305fdcb296d41.html#a46fcbabc609e3d24abd305fdcb296d41) () |
|  | Get last element. [更多...](class_ak_last_policy_with_last_a46fcbabc609e3d24abd305fdcb296d41.html#a46fcbabc609e3d24abd305fdcb296d41) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) const T \* | [Last](class_ak_last_policy_with_last_a97897fc2ff7552f02c538eea9fe8d2d5.html#a97897fc2ff7552f02c538eea9fe8d2d5) () const |
|  | |

|  |  |
| --- | --- |
| Protected 属性 | |
| T \* | [m\_pFirst](class_ak_list_bare_aef39fd5a34102e0996a0ac44b8150266.html#aef39fd5a34102e0996a0ac44b8150266) |
|  | top of list [更多...](class_ak_list_bare_aef39fd5a34102e0996a0ac44b8150266.html#aef39fd5a34102e0996a0ac44b8150266) |
|  | |
| - Protected 属性 继承自 [AkLastPolicyWithLast< T >](class_ak_last_policy_with_last.html) | |
| T \* | [m\_pLast](class_ak_last_policy_with_last_a955a4a5db2f04d2ab858ed883223b259.html#a955a4a5db2f04d2ab858ed883223b259) |
|  | bottom of list [更多...](class_ak_last_policy_with_last_a955a4a5db2f04d2ab858ed883223b259.html#a955a4a5db2f04d2ab858ed883223b259) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Protected 成员函数 继承自 [AkCountPolicyNoCount< T >](class_ak_count_policy_no_count.html) | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [ResetCount](class_ak_count_policy_no_count_a83bc9422f710d915135ebdd51152aa49.html#a83bc9422f710d915135ebdd51152aa49) (T \*) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [IncrementCount](class_ak_count_policy_no_count_a41957418694743bc3bb1147dbe8e9299.html#a41957418694743bc3bb1147dbe8e9299) (T \*) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [DecrementCount](class_ak_count_policy_no_count_a3ee57f38e9f0e9eed8f9d2b043b54226.html#a3ee57f38e9f0e9eed8f9d2b043b54226) (T \*) |
|  | |
| - Protected 成员函数 继承自 [AkLastPolicyWithLast< T >](class_ak_last_policy_with_last.html) | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [AkLastPolicyWithLast](class_ak_last_policy_with_last_a9e3d4aef05bc5dc0da5d96ee0795f350.html#a9e3d4aef05bc5dc0da5d96ee0795f350) () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [UpdateLast](class_ak_last_policy_with_last_ad4012f3f3e325e3d654b2e6c68de60ed.html#ad4012f3f3e325e3d654b2e6c68de60ed) (T \*in\_pLast) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetLast](class_ak_last_policy_with_last_a4f651c8dff13c3cb6f41e5e462160520.html#a4f651c8dff13c3cb6f41e5e462160520) (T \*in\_pLast) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [RemoveItem](class_ak_last_policy_with_last_a7231e2e7a73477844302ffd508110782.html#a7231e2e7a73477844302ffd508110782) (T \*in\_pItem, T \*in\_pPrevItem) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AddItem](class_ak_last_policy_with_last_a08c26b7ee2366f354531652682c366e3.html#a08c26b7ee2366f354531652682c366e3) (T \*in\_pItem, T \*in\_pNextItem) |
|  | |

## 详细描述

### template<class T, template< class > class U\_NEXTITEM = AkListBareNextItem, template< class > class COUNT\_POLICY = AkCountPolicyNoCount, template< class > class LAST\_POLICY = AkLastPolicyWithLast> class AkListBare< T, U\_NEXTITEM, COUNT\_POLICY, LAST\_POLICY >

Implementation of List Bare.

在文件 [AkListBare.h](_ak_list_bare_8h_source.html) 第 [164](_ak_list_bare_8h_source.html#l00164) 行定义.