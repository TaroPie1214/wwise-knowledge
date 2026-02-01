# AkFifoQueue

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_fifo_queue-members.html) |
[Public 成员函数](#pub-methods)

AkFifoQueue< T, TDEFAULT, TAlloc > 模板结构体 参考

`#include <AkFifoQueue.h>`

类 AkFifoQueue< T, TDEFAULT, TAlloc > 继承关系图:

![](../../../images/struct_ak_fifo_queue.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkFifoQueue](struct_ak_fifo_queue_a10df635c81ffe4f8f141b3780407da4e.html#a10df635c81ffe4f8f141b3780407da4e) () |
|  | |
|  | [~AkFifoQueue](struct_ak_fifo_queue_a3fe4ed6d383be37b071ace71f83a67ff.html#a3fe4ed6d383be37b071ace71f83a67ff) () |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](struct_ak_fifo_queue_a0063b8407d823b9ffc497007cae92d49.html#a0063b8407d823b9ffc497007cae92d49) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uMaxEntries) |
|  | |
| void | [Term](struct_ak_fifo_queue_a64ef6b5d61b2009e9c41a0928763b5af.html#a64ef6b5d61b2009e9c41a0928763b5af) () |
|  | |
| [AK\_NODISCARD](_ak_platforms_8h_afdad98a324f1b63271ac05b0730074de.html#afdad98a324f1b63271ac05b0730074de) bool | [Enqueue](struct_ak_fifo_queue_a9534ca2568a6a3170a5c762617eca803.html#a9534ca2568a6a3170a5c762617eca803) (T in\_value) |
|  | |
| bool | [Dequeue](struct_ak_fifo_queue_a088fbbb4403b4a6c5f7b97b62d511c79.html#a088fbbb4403b4a6c5f7b97b62d511c79) (T &io\_value) |
|  | |
| bool | [Empty](struct_ak_fifo_queue_ae21a45080f08643b7cdbe76d28e916cf.html#ae21a45080f08643b7cdbe76d28e916cf) () |
|  | Checks if there is a value available to be dequeued [更多...](struct_ak_fifo_queue_ae21a45080f08643b7cdbe76d28e916cf.html#ae21a45080f08643b7cdbe76d28e916cf) |
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

### template<typename T, T TDEFAULT, class TAlloc = ArrayPoolDefault> struct AkFifoQueue< T, TDEFAULT, TAlloc >

[AkFifoQueue](struct_ak_fifo_queue.html) is a lock-less, thread-safe, multi-producer-multi-consumer queue data structure. It is designed to hold copyable values.

在文件 [AkFifoQueue.h](_ak_fifo_queue_8h_source.html) 第 [37](_ak_fifo_queue_8h_source.html#l00037) 行定义.