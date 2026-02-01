# AkArrayAllocatorAlignedSimd

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_array_allocator_aligned_simd-members.html) |
[Public 成员函数](#pub-methods)

AkArrayAllocatorAlignedSimd< T\_MEMID > 模板结构体 参考

`#include <AkArray.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [Alloc](struct_ak_array_allocator_aligned_simd_aa2efad3ec0066844384add2fb8cebc13.html#aa2efad3ec0066844384add2fb8cebc13) (size\_t in\_uSize) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [ReAlloc](struct_ak_array_allocator_aligned_simd_a533c6efbf63ba41495b069cd398ff0fc.html#a533c6efbf63ba41495b069cd398ff0fc) (void \*in\_pCurrent, size\_t in\_uOldSize, size\_t in\_uNewSize) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Free](struct_ak_array_allocator_aligned_simd_a20d651f917f82dac3c274070afac33ae.html#a20d651f917f82dac3c274070afac33ae) (void \*in\_pAddress) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [TransferMem](struct_ak_array_allocator_aligned_simd_ad053f6686701067b179677508a83d6ce.html#ad053f6686701067b179677508a83d6ce) (void \*&io\_pDest, [AkArrayAllocatorAlignedSimd](struct_ak_array_allocator_aligned_simd.html)< T\_MEMID > in\_srcAlloc, void \*in\_pSrc) |
|  | |

## 详细描述

### template<AkMemID T\_MEMID> struct AkArrayAllocatorAlignedSimd< T\_MEMID >

在文件 [AkArray.h](_ak_array_8h_source.html) 第 [63](_ak_array_8h_source.html#l00063) 行定义.