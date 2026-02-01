# ConstIteratorEx

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkHashListBare](class_ak_hash_list_bare.html)
- [ConstIteratorEx](struct_ak_hash_list_bare_1_1_const_iterator_ex.html)

[所有成员列表](struct_ak_hash_list_bare_1_1_const_iterator_ex-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::ConstIteratorEx结构体 参考

`#include <AkHashList.h>`

类 AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::ConstIteratorEx 继承关系图:

![](../../../../images/struct_ak_hash_list_bare_1_1_const_iterator_ex.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| [ConstIteratorEx](struct_ak_hash_list_bare_1_1_const_iterator_ex.html) & | [operator++](struct_ak_hash_list_bare_1_1_const_iterator_ex_a669fa053fb10fda70aa8659f3d46fbd1.html#a669fa053fb10fda70aa8659f3d46fbd1) () |
|  | |
| - Public 成员函数 继承自 [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::ConstIterator](struct_ak_hash_list_bare_1_1_const_iterator.html) | |
| [ConstIterator](struct_ak_hash_list_bare_1_1_const_iterator.html) & | [operator++](struct_ak_hash_list_bare_1_1_const_iterator_a489093df76144ff53e4df0fc8caaaa6b.html#a489093df76144ff53e4df0fc8caaaa6b) () |
|  | |
| const T\_MAPSTRUCT \* | [operator\*](struct_ak_hash_list_bare_1_1_const_iterator_a12a921958dbd6d133982f94d021763f1.html#a12a921958dbd6d133982f94d021763f1) () |
|  | |
| const T\_MAPSTRUCT \* | [operator->](struct_ak_hash_list_bare_1_1_const_iterator_a2e900bc041a2059523596ef71bf73b52.html#a2e900bc041a2059523596ef71bf73b52) () const |
|  | |
| bool | [operator!=](struct_ak_hash_list_bare_1_1_const_iterator_a39acf10570d3b7f9697b4e3c0d39ad06.html#a39acf10570d3b7f9697b4e3c0d39ad06) (const [ConstIterator](struct_ak_hash_list_bare_1_1_const_iterator.html) &in\_rOp) const |
|  | |
| bool | [operator==](struct_ak_hash_list_bare_1_1_const_iterator_abce040c9e94b1c97a364541bbd583c27.html#abce040c9e94b1c97a364541bbd583c27) (const [ConstIterator](struct_ak_hash_list_bare_1_1_const_iterator.html) &in\_rOp) const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| T\_MAPSTRUCT \* | [pPrevItem](struct_ak_hash_list_bare_1_1_const_iterator_ex_ab561c495dd08f8818c1e7edd48360dad.html#ab561c495dd08f8818c1e7edd48360dad) |
|  | |
| - Public 属性 继承自 [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::ConstIterator](struct_ak_hash_list_bare_1_1_const_iterator.html) | |
| const [AkHashListBare](class_ak_hash_list_bare.html)< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY >::[HashTableArray](class_ak_array.html) \* | [pTable](struct_ak_hash_list_bare_1_1_const_iterator_afb2df8996a61d65b6250a165b7e129ce.html#afb2df8996a61d65b6250a165b7e129ce) |
|  | |
| [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) | [uiTable](struct_ak_hash_list_bare_1_1_const_iterator_ae64362a43b53ff9f4dc90aff38deeed6.html#ae64362a43b53ff9f4dc90aff38deeed6) |
|  | |
| T\_MAPSTRUCT \* | [pItem](struct_ak_hash_list_bare_1_1_const_iterator_a77cf482cad3ac145aaa329ba5e156983.html#a77cf482cad3ac145aaa329ba5e156983) |
|  | |

## 详细描述

### template<class T\_KEY, class T\_MAPSTRUCT, typename T\_ALLOC = ArrayPoolDefault, class KEY\_POLICY = AkDefaultHashListBarePolicy<T\_KEY, T\_MAPSTRUCT>, class LIST\_POLICY = AkDefaultHashListBarePolicy<T\_KEY, T\_MAPSTRUCT>> struct AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::ConstIteratorEx

在文件 [AkHashList.h](_ak_hash_list_8h_source.html) 第 [782](_ak_hash_list_8h_source.html#l00782) 行定义.