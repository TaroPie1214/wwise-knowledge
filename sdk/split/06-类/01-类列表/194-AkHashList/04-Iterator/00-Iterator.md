# Iterator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkHashList](class_ak_hash_list.html)
- [Iterator](struct_ak_hash_list_1_1_iterator.html)

[所有成员列表](struct_ak_hash_list_1_1_iterator-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >::Iterator结构体 参考

`#include <AkHashList.h>`

类 AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >::Iterator 继承关系图:

![](../../../../images/struct_ak_hash_list_1_1_iterator.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| [Iterator](struct_ak_hash_list_1_1_iterator.html) & | [operator++](struct_ak_hash_list_1_1_iterator_a9b8285c3f5b5b58d54005778f8d11e05.html#a9b8285c3f5b5b58d54005778f8d11e05) () |
|  | |
| [MapStruct](struct_map_struct.html)< T\_KEY, T\_ITEM > & | [operator\*](struct_ak_hash_list_1_1_iterator_af3527c0206d79c4f279f91aea388683b.html#af3527c0206d79c4f279f91aea388683b) () |
|  | |
| [MapStruct](struct_map_struct.html)< T\_KEY, T\_ITEM > \* | [operator->](struct_ak_hash_list_1_1_iterator_a5d5395cac3bbf4519f3a0a8f7702f825.html#a5d5395cac3bbf4519f3a0a8f7702f825) () |
|  | |
| bool | [operator==](struct_ak_hash_list_1_1_iterator_add313714446b26580c90b29f8fddd5e6.html#add313714446b26580c90b29f8fddd5e6) (const [Iterator](struct_ak_hash_list_1_1_iterator.html) &in\_rOp) const |
|  | |
| bool | [operator!=](struct_ak_hash_list_1_1_iterator_a663af8a1c273ede005dd2627dfdb37ec.html#a663af8a1c273ede005dd2627dfdb37ec) (const [Iterator](struct_ak_hash_list_1_1_iterator.html) &in\_rOp) const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkHashList](class_ak_hash_list.html)< T\_KEY, T\_ITEM, T\_ALLOC >::[HashTableArray](class_ak_hash_list_ac85351466e0d949d8951813f0b5ca064.html#ac85351466e0d949d8951813f0b5ca064) \* | [pTable](struct_ak_hash_list_1_1_iterator_a9c251ea5c86f3fd215017ae8bd4db804.html#a9c251ea5c86f3fd215017ae8bd4db804) |
|  | |
| [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) | [uiTable](struct_ak_hash_list_1_1_iterator_ad74dadb1e714900f5ac5d2249ae36fe1.html#ad74dadb1e714900f5ac5d2249ae36fe1) |
|  | |
| [Item](struct_ak_hash_list_1_1_item.html) \* | [pItem](struct_ak_hash_list_1_1_iterator_ab62fe8fd6d362535f92bb390c1ba771a.html#ab62fe8fd6d362535f92bb390c1ba771a) |
|  | |

## 详细描述

### template<class T\_KEY, class T\_ITEM, typename T\_ALLOC = ArrayPoolDefault> struct AkHashList< T\_KEY, T\_ITEM, T\_ALLOC >::Iterator

在文件 [AkHashList.h](_ak_hash_list_8h_source.html) 第 [61](_ak_hash_list_8h_source.html#l00061) 行定义.