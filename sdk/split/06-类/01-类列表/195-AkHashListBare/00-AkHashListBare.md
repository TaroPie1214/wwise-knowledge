# AkHashListBare

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_hash_list_bare-members.html) |
[类](#nested-classes) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods) |
[Protected 属性](#pro-attribs)

AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY > 模板类 参考

`#include <AkHashList.h>`

|  |  |
| --- | --- |
| 类 | |
| struct | [ConstIterator](struct_ak_hash_list_bare_1_1_const_iterator.html) |
|  | |
| struct | [ConstIteratorEx](struct_ak_hash_list_bare_1_1_const_iterator_ex.html) |
|  | |
| struct | [Iterator](struct_ak_hash_list_bare_1_1_iterator.html) |
|  | |
| struct | [IteratorEx](struct_ak_hash_list_bare_1_1_iterator_ex.html) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [Iterator](struct_ak_hash_list_bare_1_1_iterator.html) | [Begin](class_ak_hash_list_bare_adde5c6ff6fa518d5229d150f91cbac2f.html#adde5c6ff6fa518d5229d150f91cbac2f) () |
|  | |
| [ConstIterator](struct_ak_hash_list_bare_1_1_const_iterator.html) | [Begin](class_ak_hash_list_bare_af610c629a5c0f9b7a9a29816a92a6f88.html#af610c629a5c0f9b7a9a29816a92a6f88) () const |
|  | |
| [IteratorEx](struct_ak_hash_list_bare_1_1_iterator_ex.html) | [BeginEx](class_ak_hash_list_bare_a4b27faf42b8a9f049209f10d4992ff4c.html#a4b27faf42b8a9f049209f10d4992ff4c) () |
|  | |
| [ConstIteratorEx](struct_ak_hash_list_bare_1_1_const_iterator_ex.html) | [BeginEx](class_ak_hash_list_bare_adf95a8228edcd2c8c968e82ad8f589ba.html#adf95a8228edcd2c8c968e82ad8f589ba) () const |
|  | |
| [Iterator](struct_ak_hash_list_bare_1_1_iterator.html) | [End](class_ak_hash_list_bare_a6e3ba9b08f5707c288221e3b2cdf1b4b.html#a6e3ba9b08f5707c288221e3b2cdf1b4b) () |
|  | |
| [ConstIterator](struct_ak_hash_list_bare_1_1_const_iterator.html) | [End](class_ak_hash_list_bare_a0fa390f77772d083e3ad48eae2a9dd61.html#a0fa390f77772d083e3ad48eae2a9dd61) () const |
|  | |
| [IteratorEx](struct_ak_hash_list_bare_1_1_iterator_ex.html) | [FindEx](class_ak_hash_list_bare_a66f1d0dc090099f938a4c929d9762159.html#a66f1d0dc090099f938a4c929d9762159) (T\_KEY in\_Key) |
|  | |
| [ConstIteratorEx](struct_ak_hash_list_bare_1_1_const_iterator_ex.html) | [FindEx](class_ak_hash_list_bare_ab235b9c5c936c2dcf677a089398f8d91.html#ab235b9c5c936c2dcf677a089398f8d91) (T\_KEY in\_Key) const |
|  | |
|  | [AkHashListBare](class_ak_hash_list_bare_a785ca77712ef8e7985043ff03ed8d0bc.html#a785ca77712ef8e7985043ff03ed8d0bc) () |
|  | |
|  | [~AkHashListBare](class_ak_hash_list_bare_ad92bcb3801bdd459dd71f2a32e085000.html#ad92bcb3801bdd459dd71f2a32e085000) () |
|  | |
| bool | [Init](class_ak_hash_list_bare_adfde3a651d5a52bcc9fa04f0f2ad6a60.html#adfde3a651d5a52bcc9fa04f0f2ad6a60) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_iStartingSize) |
|  | |
| void | [Term](class_ak_hash_list_bare_a71807935b78ece7feaa86dc6f9b8bd07.html#a71807935b78ece7feaa86dc6f9b8bd07) () |
|  | |
| T\_MAPSTRUCT \* | [Exists](class_ak_hash_list_bare_a60bc01cdcb13ad25f157ed6895e1a187.html#a60bc01cdcb13ad25f157ed6895e1a187) (T\_KEY in\_Key) const |
|  | |
| bool | [Set](class_ak_hash_list_bare_a1dfbb2d3032c9854744bf8ea16d6bb86.html#a1dfbb2d3032c9854744bf8ea16d6bb86) (T\_MAPSTRUCT \*in\_pItem, bool &out\_exists) |
|  | |
| bool | [Set](class_ak_hash_list_bare_af4149a2e90cd5cba49e436aa80036f36.html#af4149a2e90cd5cba49e436aa80036f36) (T\_MAPSTRUCT \*in\_pItem) |
|  | |
| T\_MAPSTRUCT \* | [Unset](class_ak_hash_list_bare_abab3d4be6f1f6ee0b2a995a92d2e293c.html#abab3d4be6f1f6ee0b2a995a92d2e293c) (const T\_KEY &in\_Key) |
|  | |
| [IteratorEx](struct_ak_hash_list_bare_1_1_iterator_ex.html) | [Erase](class_ak_hash_list_bare_a0c5878a313a78e92e990c19c54a2e177.html#a0c5878a313a78e92e990c19c54a2e177) (const [IteratorEx](struct_ak_hash_list_bare_1_1_iterator_ex.html) &in\_rIter) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Length](class_ak_hash_list_bare_a902850394a97023a62d8f8c1c9ff0b7d.html#a902850394a97023a62d8f8c1c9ff0b7d) () const |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Reserve](class_ak_hash_list_bare_ab27db9a705fd841ec87448ed2edb9c28.html#ab27db9a705fd841ec87448ed2edb9c28) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumberOfEntires) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Resize](class_ak_hash_list_bare_abc7eff9621440bdce22c4df5f78d8f09.html#abc7eff9621440bdce22c4df5f78d8f09) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uExpectedNumberOfEntires) |
|  | |
| [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) | [HashSize](class_ak_hash_list_bare_a8af3f32797dbec4d7f7ed6835761a3c8.html#a8af3f32797dbec4d7f7ed6835761a3c8) () const |
|  | |
| bool | [CheckSize](class_ak_hash_list_bare_a4a0acec682c065a04b62878815bbe1f8.html#a4a0acec682c065a04b62878815bbe1f8) () |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| void | [RemoveItem](class_ak_hash_list_bare_a881a179b7116e3547f2a57c082135bed.html#a881a179b7116e3547f2a57c082135bed) ([AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) in\_uiTable, T\_MAPSTRUCT \*in\_pItem, T\_MAPSTRUCT \*in\_pPrevItem) |
|  | |
| T\_MAPSTRUCT \* | [ExistsInList](class_ak_hash_list_bare_a4e3422e740467dad3f7760bee401d262.html#a4e3422e740467dad3f7760bee401d262) (T\_KEY in\_Key, [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) in\_uiTable) const |
|  | |

|  |  |
| --- | --- |
| Protected 属性 | |
| [HashTableArray](class_ak_array.html) | [m\_table](class_ak_hash_list_bare_a98d2623f887dd2128801fd03f39aec0c.html#a98d2623f887dd2128801fd03f39aec0c) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [m\_uiSize](class_ak_hash_list_bare_aef3bff57d16cc093d3527ef723e9d3c7.html#aef3bff57d16cc093d3527ef723e9d3c7) |
|  | |

## 详细描述

### template<class T\_KEY, class T\_MAPSTRUCT, typename T\_ALLOC = ArrayPoolDefault, class KEY\_POLICY = AkDefaultHashListBarePolicy<T\_KEY, T\_MAPSTRUCT>, class LIST\_POLICY = AkDefaultHashListBarePolicy<T\_KEY, T\_MAPSTRUCT>> class AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >

在文件 [AkHashList.h](_ak_hash_list_8h_source.html) 第 [675](_ak_hash_list_8h_source.html#l00675) 行定义.