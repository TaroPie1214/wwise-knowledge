# AkRingBuffer.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[类型定义](#typedef-members)

AkRingBuffer.h 文件参考

`#include <AK/SoundEngine/Common/AkAtomic.h>`  
`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/Tools/Common/AkObject.h>`  
`#include <AK/Tools/Common/AkPlatformFuncs.h>`

[浏览源代码.](_ak_ring_buffer_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkRingBufferAllocatorNoAlign< T\_MEMID >](struct_ak_ring_buffer_allocator_no_align.html) |
|  | |
| struct | [AkRingBufferAllocatorAligned< T\_MEMID >](struct_ak_ring_buffer_allocator_aligned.html) |
|  | |
| class | [AkRingBuffer< T, TAlloc >](class_ak_ring_buffer.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AkRingBufferAllocatorNoAlign](struct_ak_ring_buffer_allocator_no_align.html)< [AkMemID\_Object](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a57aafbdd3be55093215a3ad89e0db902) > | [AkRingBufferAllocatorDefault](_ak_ring_buffer_8h_a1151cceae6a5e28b4218f2580ef76f5c.html#a1151cceae6a5e28b4218f2580ef76f5c) |
|  | |
| typedef [AkRingBufferAllocatorNoAlign](struct_ak_ring_buffer_allocator_no_align.html)< [AkMemID\_Processing](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a0c6d546662db0bf99d2b8ad68d132474) > | [AkRingBufferAllocatorLEngine](_ak_ring_buffer_8h_ae130a0e6ee1d387e3e92c8d8a69c455b.html#ae130a0e6ee1d387e3e92c8d8a69c455b) |
|  | |
| typedef [AkRingBufferAllocatorAligned](struct_ak_ring_buffer_allocator_aligned.html)< [AkMemID\_Processing](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a0c6d546662db0bf99d2b8ad68d132474) > | [AkRingBufferAllocatorLEngineAligned](_ak_ring_buffer_8h_a3c7c771c75d09306998ffcb3c4726eb3.html#a3c7c771c75d09306998ffcb3c4726eb3) |
|  | |