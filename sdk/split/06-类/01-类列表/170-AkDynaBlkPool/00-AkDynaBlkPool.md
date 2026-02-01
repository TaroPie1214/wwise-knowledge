# AkDynaBlkPool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_dyna_blk_pool-members.html) |
[Public 成员函数](#pub-methods)

AkDynaBlkPool< T, uPoolChunkSize, TAlloc > 模板类 参考

`#include <AkDynaBlkPool.h>`

类 AkDynaBlkPool< T, uPoolChunkSize, TAlloc > 继承关系图:

![](../../../images/class_ak_dyna_blk_pool.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [~AkDynaBlkPool](class_ak_dyna_blk_pool_a118d6f3edf4ed7f30907403c4f2d55cc.html#a118d6f3edf4ed7f30907403c4f2d55cc) () |
|  | |
| T \* | [New](class_ak_dyna_blk_pool_aaa715a4146b04c8f12f78db1abff3f62.html#aaa715a4146b04c8f12f78db1abff3f62) () |
|  | |
| template<typename A1 > | |
| T \* | [New](class_ak_dyna_blk_pool_a754eca71d9eb1c0fa712c0369e72aa28.html#a754eca71d9eb1c0fa712c0369e72aa28) (A1 a1) |
|  | |
| template<typename A1 , typename A2 > | |
| T \* | [New](class_ak_dyna_blk_pool_aeb0961db0dc1d8a933d64c1e9cfa458a.html#aeb0961db0dc1d8a933d64c1e9cfa458a) (A1 a1, A2 a2) |
|  | |
| template<typename A1 , typename A2 , typename A3 > | |
| T \* | [New](class_ak_dyna_blk_pool_a32a230e7aa98250a6113808050743a38.html#a32a230e7aa98250a6113808050743a38) (A1 a1, A2 a2, A3 a3) |
|  | |
| template<typename A1 , typename A2 , typename A3 , typename A4 > | |
| T \* | [New](class_ak_dyna_blk_pool_a55ccba871acbc9b55893d76c620c132a.html#a55ccba871acbc9b55893d76c620c132a) (A1 a1, A2 a2, A3 a3, A4 a4) |
|  | |
| void | [Delete](class_ak_dyna_blk_pool_aa4b9bbb42d629e2701abfc98a2eccc61.html#aa4b9bbb42d629e2701abfc98a2eccc61) (T \*ptr) |
|  | |
| void | [Transfer](class_ak_dyna_blk_pool_acbaa93b4f6ef637531722ac21d726214.html#acbaa93b4f6ef637531722ac21d726214) ([AkDynaBlkPool](class_ak_dyna_blk_pool.html)< T, uPoolChunkSize, TAlloc > &in\_src) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 成员函数 继承自 [AkArrayAllocatorNoAlign< T\_MEMID >](struct_ak_array_allocator_no_align.html) | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [Alloc](struct_ak_array_allocator_no_align_a572d7f65fd546fce3dd949c48f2ba568.html#a572d7f65fd546fce3dd949c48f2ba568) (size\_t in\_uSize) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [ReAlloc](struct_ak_array_allocator_no_align_aac15f21c37c5da42bfa1db7060d2f30c.html#aac15f21c37c5da42bfa1db7060d2f30c) (void \*in\_pCurrent, size\_t in\_uOldSize, size\_t in\_uNewSize) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Free](struct_ak_array_allocator_no_align_a090f613bd8846bc436d4e9e562d5d8cc.html#a090f613bd8846bc436d4e9e562d5d8cc) (void \*in\_pAddress) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [TransferMem](struct_ak_array_allocator_no_align_a7dd951bf506402f04e0ea453da9bd8a0.html#a7dd951bf506402f04e0ea453da9bd8a0) (void \*&io\_pDest, [AkArrayAllocatorNoAlign](struct_ak_array_allocator_no_align.html)< T\_MEMID > in\_srcAlloc, void \*in\_pSrc) |
|  | |

## 详细描述

### template<typename T, AkUInt32 uPoolChunkSize, class TAlloc = ArrayPoolDefault> class AkDynaBlkPool< T, uPoolChunkSize, TAlloc >

在文件 [AkDynaBlkPool.h](_ak_dyna_blk_pool_8h_source.html) 第 [67](_ak_dyna_blk_pool_8h_source.html#l00067) 行定义.