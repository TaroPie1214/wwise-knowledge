# WriteBytesCount

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [WriteBytesCount](class_a_k_1_1_write_bytes_count.html)

[所有成员列表](class_a_k_1_1_write_bytes_count-members.html) |
[Public 成员函数](#pub-methods)

AK::WriteBytesCount类 参考

`#include <AkBytesCount.h>`

类 AK::WriteBytesCount 继承关系图:

![](../../../../images/class_a_k_1_1_write_bytes_count.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [WriteBytesCount](class_a_k_1_1_write_bytes_count_aa6f459472381f5bb40a4c58e0fb463d6.html#aa6f459472381f5bb40a4c58e0fb463d6) () |
|  | |
| virtual | [~WriteBytesCount](class_a_k_1_1_write_bytes_count_a598ce62168d28ddff233e55f9b3af10a.html#a598ce62168d28ddff233e55f9b3af10a) () |
|  | |
| virtual bool | [WriteBytes](class_a_k_1_1_write_bytes_count_ab2b1cc4f5c9162b371504fff9b9a775c.html#ab2b1cc4f5c9162b371504fff9b9a775c) (const void \*in\_pData, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_cWritten) |
|  | |
| virtual bool | [Reserve](class_a_k_1_1_write_bytes_count_a1cdb7fef13d0d136702c46bf37068ca3.html#a1cdb7fef13d0d136702c46bf37068ca3) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes) |
|  | |
| virtual [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [Count](class_a_k_1_1_write_bytes_count_a1b8dcb9178c0abd9cfb53a7e76bf5668.html#a1b8dcb9178c0abd9cfb53a7e76bf5668) () const |
|  | |
| virtual void | [SetCount](class_a_k_1_1_write_bytes_count_abdffee28036f54266dd70099cc130205.html#abdffee28036f54266dd70099cc130205) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes) |
|  | Set number of bytes written. [更多...](class_a_k_1_1_write_bytes_count_abdffee28036f54266dd70099cc130205.html#abdffee28036f54266dd70099cc130205) |
|  | |
| virtual [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \* | [Bytes](class_a_k_1_1_write_bytes_count_a03b1e0c3adf53bcdc8284e4994a65e0e.html#a03b1e0c3adf53bcdc8284e4994a65e0e) () const |
|  | |
| virtual [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \* | [Detach](class_a_k_1_1_write_bytes_count_a041313a9296e6f2a8d9c2baf3664bf43.html#a041313a9296e6f2a8d9c2baf3664bf43) () |
|  | Return pointer to buffer and clear internal pointer. [更多...](class_a_k_1_1_write_bytes_count_a041313a9296e6f2a8d9c2baf3664bf43.html#a041313a9296e6f2a8d9c2baf3664bf43) |
|  | |
| virtual void | [Clear](class_a_k_1_1_write_bytes_count_a60e473934239363c079a37ec6ab5bd2c.html#a60e473934239363c079a37ec6ab5bd2c) () |
|  | Clear the buffer contents. [更多...](class_a_k_1_1_write_bytes_count_a60e473934239363c079a37ec6ab5bd2c.html#a60e473934239363c079a37ec6ab5bd2c) |
|  | |
| template<class T > | |
| bool | [Write](class_a_k_1_1_write_bytes_count_a069e278d8e7d214dc4ead78c78610081.html#a069e278d8e7d214dc4ead78c78610081) (const T &in\_data) |
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

在文件 [AkBytesCount.h](_ak_bytes_count_8h_source.html) 第 [76](_ak_bytes_count_8h_source.html#l00076) 行定义.