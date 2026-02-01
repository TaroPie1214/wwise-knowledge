# AkKeyDataPtrStruct

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_key_data_ptr_struct-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[Public 属性](#pub-attribs)

AkKeyDataPtrStruct< T\_KEY, T\_DATA, T\_ALLOC > 模板结构体 参考

`#include <AkKeyDef.h>`

类 AkKeyDataPtrStruct< T\_KEY, T\_DATA, T\_ALLOC > 继承关系图:

![](../../../images/struct_ak_key_data_ptr_struct.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkKeyDataPtrStruct](struct_ak_key_data_ptr_struct_a42d22d529f22dc838551fd5db6aea850.html#a42d22d529f22dc838551fd5db6aea850) () |
|  | |
|  | [AkKeyDataPtrStruct](struct_ak_key_data_ptr_struct_ae65999f65c0c63ab6c3422e7fb3b8a09.html#ae65999f65c0c63ab6c3422e7fb3b8a09) (T\_KEY in\_key) |
|  | |
| bool | [operator==](struct_ak_key_data_ptr_struct_a04bafdde6c5edecdecc961b09d2dce8c.html#a04bafdde6c5edecdecc961b09d2dce8c) (const [AkKeyDataPtrStruct](struct_ak_key_data_ptr_struct.html)< T\_KEY, T\_DATA > &in\_Op) const |
|  | |
| bool | [AllocData](struct_ak_key_data_ptr_struct_a0c1ea457fed9d7bd3c1d73c354dbed65.html#a0c1ea457fed9d7bd3c1d73c354dbed65) () |
|  | |
| void | [FreeData](struct_ak_key_data_ptr_struct_a3ed41d02a5156c0b3cbdb0732d14b899.html#a3ed41d02a5156c0b3cbdb0732d14b899) () |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T\_KEY & | [Get](struct_ak_key_data_ptr_struct_af01ba8ec1b161cc673e8a718e536d667.html#af01ba8ec1b161cc673e8a718e536d667) ([AkKeyDataPtrStruct](struct_ak_key_data_ptr_struct.html)< T\_KEY, T\_DATA > &in\_val) |
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

|  |  |
| --- | --- |
| Public 属性 | |
| T\_KEY | [key](struct_ak_key_data_ptr_struct_a5bc1260d9d2956e2780222ac59659d97.html#a5bc1260d9d2956e2780222ac59659d97) |
|  | |
| T\_DATA \* | [pData](struct_ak_key_data_ptr_struct_aa38935d06bc334b5fbcb48d45a98bf3f.html#aa38935d06bc334b5fbcb48d45a98bf3f) |
|  | |

## 详细描述

### template<typename T\_KEY, typename T\_DATA, class T\_ALLOC = ArrayPoolDefault> struct AkKeyDataPtrStruct< T\_KEY, T\_DATA, T\_ALLOC >

在文件 [AkKeyDef.h](_ak_key_def_8h_source.html) 第 [55](_ak_key_def_8h_source.html#l00055) 行定义.