# IteratorEx

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkHashListBare](class_ak_hash_list_bare.html)
- [IteratorEx](struct_ak_hash_list_bare_1_1_iterator_ex.html)

[所有成员列表](struct_ak_hash_list_bare_1_1_iterator_ex-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::IteratorEx结构体 参考

`#include <AkHashList.h>`

类 AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::IteratorEx 继承关系图:

![](../../../../images/struct_ak_hash_list_bare_1_1_iterator_ex.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| [IteratorEx](struct_ak_hash_list_bare_1_1_iterator_ex.html) & | [operator++](struct_ak_hash_list_bare_1_1_iterator_ex_a62b8ff85b25f6f4c41ee48d78e83857d.html#a62b8ff85b25f6f4c41ee48d78e83857d) () |
|  | |
| - Public 成员函数 继承自 [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::Iterator](struct_ak_hash_list_bare_1_1_iterator.html) | |
| [Iterator](struct_ak_hash_list_bare_1_1_iterator.html) & | [operator++](struct_ak_hash_list_bare_1_1_iterator_afb9b5e3d576c4655da7ca992f6beb2e6.html#afb9b5e3d576c4655da7ca992f6beb2e6) () |
|  | |
| T\_MAPSTRUCT \* | [operator\*](struct_ak_hash_list_bare_1_1_iterator_a1c62f048ff2697dcfd14deb35f570397.html#a1c62f048ff2697dcfd14deb35f570397) () |
|  | |
| T\_MAPSTRUCT \* | [operator->](struct_ak_hash_list_bare_1_1_iterator_a7a1e95a72a19b84eea3d9871cbab1d28.html#a7a1e95a72a19b84eea3d9871cbab1d28) () |
|  | |
| bool | [operator!=](struct_ak_hash_list_bare_1_1_iterator_aff28bb098116918e4f4c7ee8c7ea9efd.html#aff28bb098116918e4f4c7ee8c7ea9efd) (const [Iterator](struct_ak_hash_list_bare_1_1_iterator.html) &in\_rOp) const |
|  | |
| bool | [operator==](struct_ak_hash_list_bare_1_1_iterator_a5d28e3e43b4418c90806f4d8f1557105.html#a5d28e3e43b4418c90806f4d8f1557105) (const [Iterator](struct_ak_hash_list_bare_1_1_iterator.html) &in\_rOp) const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| T\_MAPSTRUCT \* | [pPrevItem](struct_ak_hash_list_bare_1_1_iterator_ex_a1cc7082fbcdd3ccf4adfc1830e3c32f7.html#a1cc7082fbcdd3ccf4adfc1830e3c32f7) |
|  | |
| - Public 属性 继承自 [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::Iterator](struct_ak_hash_list_bare_1_1_iterator.html) | |
| [AkHashListBare](class_ak_hash_list_bare.html)< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::[HashTableArray](class_ak_array.html) \* | [pTable](struct_ak_hash_list_bare_1_1_iterator_a849cf0e06c7631011f81636faf982b0d.html#a849cf0e06c7631011f81636faf982b0d) |
|  | |
| [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) | [uiTable](struct_ak_hash_list_bare_1_1_iterator_a12bda837bb9a959de0eb186360ccd4bc.html#a12bda837bb9a959de0eb186360ccd4bc) |
|  | |
| T\_MAPSTRUCT \* | [pItem](struct_ak_hash_list_bare_1_1_iterator_a4575039a11c9b0a32319796c400f9520.html#a4575039a11c9b0a32319796c400f9520) |
|  | |

## 详细描述

### template<class T\_KEY, class T\_MAPSTRUCT, typename T\_ALLOC = ArrayPoolDefault, class KEY\_POLICY = AkDefaultHashListBarePolicy<T\_KEY, T\_MAPSTRUCT>, class LIST\_POLICY = AkDefaultHashListBarePolicy<T\_KEY, T\_MAPSTRUCT>> struct AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY, LIST\_POLICY >::IteratorEx

在文件 [AkHashList.h](_ak_hash_list_8h_source.html) 第 [761](_ak_hash_list_8h_source.html#l00761) 行定义.