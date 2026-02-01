# AkRingBuffer

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_ring_buffer-members.html) |
[Public 成员函数](#pub-methods)

AkRingBuffer< T, TAlloc > 模板类 参考

`#include <AkRingBuffer.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkRingBuffer](class_ak_ring_buffer_a567777f7d958fb355cc9db2cf7bfcf37.html#a567777f7d958fb355cc9db2cf7bfcf37) () |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](class_ak_ring_buffer_af5b84256d2e464d1eaffce5c3c7fcdc4.html#af5b84256d2e464d1eaffce5c3c7fcdc4) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) nbItems) |
|  | |
| void | [Term](class_ak_ring_buffer_ab82ce3e4af0d26883ffe606c7961b476.html#ab82ce3e4af0d26883ffe606c7961b476) () |
|  | |
| void | [Reset](class_ak_ring_buffer_a85530e69c4c6507e3a568bb51083fc0e.html#a85530e69c4c6507e3a568bb51083fc0e) () |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetWriteIndex](class_ak_ring_buffer_acb3d1b6dbc900ddc5b9b337af119f800.html#acb3d1b6dbc900ddc5b9b337af119f800) () const |
|  | |
| T \* | [GetWritePtr](class_ak_ring_buffer_a0046b8b33583e7686c73afdd2ea1ae2b.html#a0046b8b33583e7686c73afdd2ea1ae2b) () |
|  | |
| void | [IncrementWriteIndex](class_ak_ring_buffer_a233151f5390f42dfbdc39d4d559fb62d.html#a233151f5390f42dfbdc39d4d559fb62d) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) nbItems) |
|  | |
| void | [WriteDataToRing](class_ak_ring_buffer_a8587ec0505843d107686964f9e59d08a.html#a8587ec0505843d107686964f9e59d08a) (T \*in\_pDest, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_nbItems) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetReadIndex](class_ak_ring_buffer_afce19d4a2467be8df7a79ab489cf7932.html#afce19d4a2467be8df7a79ab489cf7932) () const |
|  | |
| const T \* | [GetReadPtr](class_ak_ring_buffer_afea1d4824b219fd8e7071cc436c872ea.html#afea1d4824b219fd8e7071cc436c872ea) () const |
|  | |
| const T \* | [Peek](class_ak_ring_buffer_a88e8c0fff7b0e978f7d868d55b56bae7.html#a88e8c0fff7b0e978f7d868d55b56bae7) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uOffset) const |
|  | |
| void | [IncrementReadIndex](class_ak_ring_buffer_a18eebcc592ee19621e48c2cd3e810567.html#a18eebcc592ee19621e48c2cd3e810567) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) nbItems) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetNbReadableItems](class_ak_ring_buffer_aaef27a0bcd749f179ed561d7a3bbaf7c.html#aaef27a0bcd749f179ed561d7a3bbaf7c) () const |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetNbWritableItems](class_ak_ring_buffer_aa365e9cd8ee6891b24aec7ffd3943093.html#aa365e9cd8ee6891b24aec7ffd3943093) () const |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Size](class_ak_ring_buffer_aa2a2c2c097311ac691a96cde15ea10ae.html#aa2a2c2c097311ac691a96cde15ea10ae) () const |
|  | |
| void | [ReadDataFromRing](class_ak_ring_buffer_a3b264d7bc0dc1ca8db8296e799ac4de4.html#a3b264d7bc0dc1ca8db8296e799ac4de4) (T \*in\_pSrc, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_nbItems) |
|  | |
| bool | [Grow](class_ak_ring_buffer_afac29b0a4de89044aa8602ba3152bd1e.html#afac29b0a4de89044aa8602ba3152bd1e) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uGrowBy) |
|  | |

## 详细描述

### template<class T, class TAlloc = AkRingBufferAllocatorDefault> class AkRingBuffer< T, TAlloc >

在文件 [AkRingBuffer.h](_ak_ring_buffer_8h_source.html) 第 [68](_ak_ring_buffer_8h_source.html#l00068) 行定义.