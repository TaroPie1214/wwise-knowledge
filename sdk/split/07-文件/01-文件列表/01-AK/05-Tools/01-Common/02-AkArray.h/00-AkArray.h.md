# AkArray.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[宏定义](#define-members) |
[类型定义](#typedef-members)

AkArray.h 文件参考

`#include <AK/Tools/Common/AkObject.h>`  
`#include <AK/Tools/Common/AkPlacementNew.h>`  
`#include <AK/Tools/Common/AkAssert.h>`  
`#include <AK/Tools/Common/AkPlatformFuncs.h>`  
`#include <utility>`

[浏览源代码.](_ak_array_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkArrayAllocatorNoAlign< T\_MEMID >](struct_ak_array_allocator_no_align.html) |
|  | |
| struct | [AkArrayAllocatorAlignedSimd< T\_MEMID >](struct_ak_array_allocator_aligned_simd.html) |
|  | |
| struct | [AkHybridAllocator< uBufferSizeBytes, uAlignmentSize, T\_MEMID >](struct_ak_hybrid_allocator.html) |
|  | |
| struct | [AkAssignmentMovePolicy< T >](struct_ak_assignment_move_policy.html) |
|  | |
| struct | [AkStdMovePolicy](struct_ak_std_move_policy.html) |
|  | |
| struct | [AkTrivialStdMovePolicy](struct_ak_trivial_std_move_policy.html) |
|  | |
| struct | [AkTransferMovePolicy< T >](struct_ak_transfer_move_policy.html) |
|  | |
| struct | [AkGrowByPolicy\_Legacy](struct_ak_grow_by_policy___legacy.html) |
|  | |
| struct | [AkGrowByPolicy\_NoGrow](struct_ak_grow_by_policy___no_grow.html) |
|  | |
| struct | [AkGrowByPolicy\_Hybrid< uCount >](struct_ak_grow_by_policy___hybrid.html) |
|  | |
| struct | [AkGrowByPolicy\_Proportional](struct_ak_grow_by_policy___proportional.html) |
|  | |
| class | [AkArray< T, ARG\_T, TAlloc, TGrowBy, TMovePolicy >](class_ak_array.html) |
|  | Specific implementation of array [更多...](class_ak_array.html#details) |
|  | |
| struct | [AkArray< T, ARG\_T, TAlloc, TGrowBy, TMovePolicy >::Iterator](struct_ak_array_1_1_iterator.html) |
|  | [Iterator](struct_ak_array_1_1_iterator.html "Iterator") [更多...](struct_ak_array_1_1_iterator.html#details) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AkGrowByPolicy\_DEFAULT](_ak_array_8h_ae1e32c88be73da730ad49a610b04900d.html#ae1e32c88be73da730ad49a610b04900d)   [AkGrowByPolicy\_Proportional](struct_ak_grow_by_policy___proportional.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| template<class T , AkUInt32 uCount = 1, AkMemID MemID = AkMemID\_Object> | |
| using | [AkSmallArrayAllocator](_ak_array_8h_a453f9d567f65675f027af5559df23914.html#a453f9d567f65675f027af5559df23914) = [AkHybridAllocator](struct_ak_hybrid_allocator.html)< sizeof(T) \*uCount, alignof(T), MemID > |
|  | |
| typedef [AkArrayAllocatorNoAlign](struct_ak_array_allocator_no_align.html)< [AkMemID\_Object](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a57aafbdd3be55093215a3ad89e0db902) > | [ArrayPoolDefault](_ak_array_8h_a6d1995f92ec49c35784181225575438f.html#a6d1995f92ec49c35784181225575438f) |
|  | |
| typedef [AkArrayAllocatorNoAlign](struct_ak_array_allocator_no_align.html)< [AkMemID\_Processing](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a0c6d546662db0bf99d2b8ad68d132474) > | [ArrayPoolLEngineDefault](_ak_array_8h_aa264686fd2168b95012127cd18bff802.html#aa264686fd2168b95012127cd18bff802) |
|  | |
| typedef [AkArrayAllocatorNoAlign](struct_ak_array_allocator_no_align.html)< [AkMemID\_Profiler](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516af31745e6d45df2870b9e2821f2cd93d1) > | [ArrayPoolProfiler](_ak_array_8h_a499ea20bd430826c59c108965440c340.html#a499ea20bd430826c59c108965440c340) |
|  | |
| typedef [AkArrayAllocatorAlignedSimd](struct_ak_array_allocator_aligned_simd.html)< [AkMemID\_Processing](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a0c6d546662db0bf99d2b8ad68d132474) > | [ArrayPoolLEngineDefaultAlignedSimd](_ak_array_8h_a47a2f80352bcdfb03629f1f59a30d59e.html#a47a2f80352bcdfb03629f1f59a30d59e) |
|  | |