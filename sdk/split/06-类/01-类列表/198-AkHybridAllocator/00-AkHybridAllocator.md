# AkHybridAllocator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_hybrid_allocator-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 属性](#pub-static-attribs)

AkHybridAllocator< uBufferSizeBytes, uAlignmentSize, T\_MEMID > 模板结构体 参考

`#include <AkArray.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [Alloc](struct_ak_hybrid_allocator_a1ff2b3a402fef7f689f3cb1295b7a403.html#a1ff2b3a402fef7f689f3cb1295b7a403) (size\_t in\_uSize) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [ReAlloc](struct_ak_hybrid_allocator_a106615cf8376b78745803f9cf09a5e22.html#a106615cf8376b78745803f9cf09a5e22) (void \*in\_pCurrent, size\_t in\_uOldSize, size\_t in\_uNewSize) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Free](struct_ak_hybrid_allocator_ab2a89a40f3d3587bbf10b035ded41db9.html#ab2a89a40f3d3587bbf10b035ded41db9) (void \*in\_pAddress) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [TransferMem](struct_ak_hybrid_allocator_a2209f9967577a45d4f563f93fca05acd.html#a2209f9967577a45d4f563f93fca05acd) (void \*&io\_pDest, [AkHybridAllocator](struct_ak_hybrid_allocator.html)< uBufferSizeBytes, uAlignmentSize, T\_MEMID > &in\_srcAlloc, void \*in\_pSrc) |
|  | |
|  | [AK\_ALIGN](struct_ak_hybrid_allocator_ae2507e2abc2cc04bdcd13df262b50802.html#ae2507e2abc2cc04bdcd13df262b50802) (char m\_buffer[uBufferSizeBytes], uAlignmentSize) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [\_uBufferSizeBytes](struct_ak_hybrid_allocator_a3d5f7e66d2e608978e3dc30f431280d2.html#a3d5f7e66d2e608978e3dc30f431280d2) = uBufferSizeBytes |
|  | |

## 详细描述

### template<AkUInt32 uBufferSizeBytes, AkUInt8 uAlignmentSize = 1, AkMemID T\_MEMID = AkMemID\_Object> struct AkHybridAllocator< uBufferSizeBytes, uAlignmentSize, T\_MEMID >

在文件 [AkArray.h](_ak_array_8h_source.html) 第 [92](_ak_array_8h_source.html#l00092) 行定义.