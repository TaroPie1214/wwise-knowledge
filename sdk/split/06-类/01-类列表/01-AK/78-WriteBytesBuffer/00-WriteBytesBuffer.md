# WriteBytesBuffer

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [WriteBytesBuffer](class_a_k_1_1_write_bytes_buffer.html)

[所有成员列表](class_a_k_1_1_write_bytes_buffer-members.html) |
[Public 成员函数](#pub-methods)

AK::WriteBytesBuffer类 参考

`#include <AkBytesMem.h>`

类 AK::WriteBytesBuffer 继承关系图:

![](../../../../images/class_a_k_1_1_write_bytes_buffer.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [WriteBytesBuffer](class_a_k_1_1_write_bytes_buffer_a61483e8c323a0c6f501c8a3185f1f4ae.html#a61483e8c323a0c6f501c8a3185f1f4ae) () |
|  | |
| virtual | [~WriteBytesBuffer](class_a_k_1_1_write_bytes_buffer_a8c0ddf82d656af6d40c19d7b9789caa7.html#a8c0ddf82d656af6d40c19d7b9789caa7) () |
|  | |
| void | [SetBuffer](class_a_k_1_1_write_bytes_buffer_af26b0a98112c3ace3b116e84dc9e95fc.html#af26b0a98112c3ace3b116e84dc9e95fc) ([AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*in\_pBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cSize) |
|  | |
| virtual bool | [WriteBytes](class_a_k_1_1_write_bytes_buffer_a0cc916c7a9fc72b18b43d8a5e8b1bba8.html#a0cc916c7a9fc72b18b43d8a5e8b1bba8) (const void \*in\_pData, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_cWritten) |
|  | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [GetPos](class_a_k_1_1_write_bytes_buffer_a546c536ae76c9916ff4b2ecf922ab93f.html#a546c536ae76c9916ff4b2ecf922ab93f) () const |
|  | |
| void | [Clear](class_a_k_1_1_write_bytes_buffer_a140ceeed9b53f13ce66a5237ed93ea43.html#a140ceeed9b53f13ce66a5237ed93ea43) () |
|  | |
| - Public 成员函数 继承自 [AK::IWriteBytes](class_a_k_1_1_i_write_bytes.html) | |
| template<class T > | |
| bool | [Write](class_a_k_1_1_i_write_bytes_a4db16f8c3735f39903277bd1cd24d9e1.html#a4db16f8c3735f39903277bd1cd24d9e1) (const T &in\_data) |
|  | |
| template<> |
| bool | [Write](class_a_k_1_1_i_write_bytes_a94945a17afde7c787007c6d04f2ca92f.html#a94945a17afde7c787007c6d04f2ca92f) (const bool &in\_data) |
|  | |

## 详细描述

在文件 [AkBytesMem.h](_ak_bytes_mem_8h_source.html) 第 [165](_ak_bytes_mem_8h_source.html#l00165) 行定义.