# IWriteBuffer

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IWriteBuffer](class_a_k_1_1_i_write_buffer.html)

[所有成员列表](class_a_k_1_1_i_write_buffer-members.html)

AK::IWriteBuffer类 参考abstract

`#include <IBytes.h>`

类 AK::IWriteBuffer 继承关系图:

![](../../../../images/class_a_k_1_1_i_write_buffer.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| Interface | |
| virtual [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [Count](class_a_k_1_1_i_write_buffer_abc9d16f8fe01b6eb79d711a89479fa49.html#abc9d16f8fe01b6eb79d711a89479fa49) () const =0 |
|  | |
| virtual [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \* | [Bytes](class_a_k_1_1_i_write_buffer_a1a06bb04b2220a87e4fe884c0976c492.html#a1a06bb04b2220a87e4fe884c0976c492) () const =0 |
|  | |
| virtual void | [SetCount](class_a_k_1_1_i_write_buffer_a700f970559de7a7fffbfcb3733795bd4.html#a700f970559de7a7fffbfcb3733795bd4) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes)=0 |
|  | Set number of bytes written. [更多...](class_a_k_1_1_i_write_buffer_a700f970559de7a7fffbfcb3733795bd4.html#a700f970559de7a7fffbfcb3733795bd4) |
|  | |
| virtual bool | [Reserve](class_a_k_1_1_i_write_buffer_af373354271f43349ace63c66e10ef435.html#af373354271f43349ace63c66e10ef435) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes)=0 |
|  | |
| virtual void | [Clear](class_a_k_1_1_i_write_buffer_a4ed5f91d532f3ef23d54d87c9b1eadf2.html#a4ed5f91d532f3ef23d54d87c9b1eadf2) ()=0 |
|  | Clear the buffer contents. [更多...](class_a_k_1_1_i_write_buffer_a4ed5f91d532f3ef23d54d87c9b1eadf2.html#a4ed5f91d532f3ef23d54d87c9b1eadf2) |
|  | |
| virtual [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \* | [Detach](class_a_k_1_1_i_write_buffer_a724bb9c88f699319d86a33ce285797da.html#a724bb9c88f699319d86a33ce285797da) ()=0 |
|  | Return pointer to buffer and clear internal pointer. [更多...](class_a_k_1_1_i_write_buffer_a724bb9c88f699319d86a33ce285797da.html#a724bb9c88f699319d86a33ce285797da) |
|  | |
| - Public 成员函数 继承自 [AK::IWriteBytes](class_a_k_1_1_i_write_bytes.html) | |
| virtual bool | [WriteBytes](class_a_k_1_1_i_write_bytes_af52b6e689172d6ec3ac9288012436d65.html#af52b6e689172d6ec3ac9288012436d65) (const void \*in\_pData, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_cWritten)=0 |
|  | |
| template<class T > | |
| bool | [Write](class_a_k_1_1_i_write_bytes_a4db16f8c3735f39903277bd1cd24d9e1.html#a4db16f8c3735f39903277bd1cd24d9e1) (const T &in\_data) |
|  | |
| template<> |
| bool | [Write](class_a_k_1_1_i_write_bytes_a94945a17afde7c787007c6d04f2ca92f.html#a94945a17afde7c787007c6d04f2ca92f) (const bool &in\_data) |
|  | |

## 详细描述

Generic memory buffer interface.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

在文件 [IBytes.h](_i_bytes_8h_source.html) 第 [158](_i_bytes_8h_source.html#l00158) 行定义.