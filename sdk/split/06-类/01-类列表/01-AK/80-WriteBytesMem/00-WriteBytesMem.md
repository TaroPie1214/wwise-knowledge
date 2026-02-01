# WriteBytesMem

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [WriteBytesMem](class_a_k_1_1_write_bytes_mem.html)

[所有成员列表](class_a_k_1_1_write_bytes_mem-members.html) |
[Public 成员函数](#pub-methods)

AK::WriteBytesMem类 参考

`#include <AkBytesMem.h>`

类 AK::WriteBytesMem 继承关系图:

![](../../../../images/class_a_k_1_1_write_bytes_mem.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [WriteBytesMem](class_a_k_1_1_write_bytes_mem_ab3c85f363a67f03ec052224234e56712.html#ab3c85f363a67f03ec052224234e56712) () |
|  | |
| virtual | [~WriteBytesMem](class_a_k_1_1_write_bytes_mem_a5ea7c5e7150b04df8845c7c2f2a829d7.html#a5ea7c5e7150b04df8845c7c2f2a829d7) () |
|  | |
| virtual bool | [WriteBytes](class_a_k_1_1_write_bytes_mem_af688769e2ff35b29b6f3c701a3188eab.html#af688769e2ff35b29b6f3c701a3188eab) (const void \*in\_pData, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_cWritten) |
|  | |
| virtual bool | [Reserve](class_a_k_1_1_write_bytes_mem_a268e5f7c52bcf40b763890ed973b6aaf.html#a268e5f7c52bcf40b763890ed973b6aaf) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes) |
|  | |
| virtual [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [Count](class_a_k_1_1_write_bytes_mem_ad29701e9a024af88407806e2d04fae53.html#ad29701e9a024af88407806e2d04fae53) () const |
|  | |
| virtual void | [SetCount](class_a_k_1_1_write_bytes_mem_a705a731905a23bc641e2358892422c8b.html#a705a731905a23bc641e2358892422c8b) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes) |
|  | Set number of bytes written. [更多...](class_a_k_1_1_write_bytes_mem_a705a731905a23bc641e2358892422c8b.html#a705a731905a23bc641e2358892422c8b) |
|  | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [Size](class_a_k_1_1_write_bytes_mem_a9112d52534636aece82dd5efe8c25264.html#a9112d52534636aece82dd5efe8c25264) () const |
|  | |
| virtual [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \* | [Bytes](class_a_k_1_1_write_bytes_mem_a476ebac81f222ce28cd23186949066f5.html#a476ebac81f222ce28cd23186949066f5) () const |
|  | |
| virtual [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \* | [Detach](class_a_k_1_1_write_bytes_mem_ac64744966b0ff49ba5691612980a34fe.html#ac64744966b0ff49ba5691612980a34fe) () |
|  | Return pointer to buffer and clear internal pointer. [更多...](class_a_k_1_1_write_bytes_mem_ac64744966b0ff49ba5691612980a34fe.html#ac64744966b0ff49ba5691612980a34fe) |
|  | |
| virtual void | [Clear](class_a_k_1_1_write_bytes_mem_a8da303526bad0ef3266004042fcc7cbb.html#a8da303526bad0ef3266004042fcc7cbb) () |
|  | Clear the buffer contents. [更多...](class_a_k_1_1_write_bytes_mem_a8da303526bad0ef3266004042fcc7cbb.html#a8da303526bad0ef3266004042fcc7cbb) |
|  | |
| void | [SetMemPool](class_a_k_1_1_write_bytes_mem_aa088736b0e3716c9dac935f2a1d40a59.html#aa088736b0e3716c9dac935f2a1d40a59) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_pool) |
|  | |
| bool | [HasValidMemPool](class_a_k_1_1_write_bytes_mem_a73888eed9a7c8c48dafea6935bcc810f.html#a73888eed9a7c8c48dafea6935bcc810f) () |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \* | [GetWritePtr](class_a_k_1_1_write_bytes_mem_ab43d16c6b8478419e66cc8f57f53cc96.html#ab43d16c6b8478419e66cc8f57f53cc96) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes) |
|  | |
| template<class T > | |
| T \* | [GetWritePtr](class_a_k_1_1_write_bytes_mem_a6fa1608a00d5aac566854c0bf9b3f1be.html#a6fa1608a00d5aac566854c0bf9b3f1be) () |
|  | |
| template<class T > | |
| bool | [Write](class_a_k_1_1_write_bytes_mem_a0879e273ffa6e0f1eed4115d4f116f1c.html#a0879e273ffa6e0f1eed4115d4f116f1c) (const T &in\_data) |
|  | |
| Interface | |
| - Public 成员函数 继承自 [AK::IWriteBytes](class_a_k_1_1_i_write_bytes.html) | |
| template<class T > | |
| bool | [Write](class_a_k_1_1_i_write_bytes_a4db16f8c3735f39903277bd1cd24d9e1.html#a4db16f8c3735f39903277bd1cd24d9e1) (const T &in\_data) |
|  | |
| template<> |
| bool | [Write](class_a_k_1_1_i_write_bytes_a94945a17afde7c787007c6d04f2ca92f.html#a94945a17afde7c787007c6d04f2ca92f) (const bool &in\_data) |
|  | |

## 详细描述

在文件 [AkBytesMem.h](_ak_bytes_mem_8h_source.html) 第 [77](_ak_bytes_mem_8h_source.html#l00077) 行定义.