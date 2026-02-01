# IWriteBytes

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IWriteBytes](class_a_k_1_1_i_write_bytes.html)

[所有成员列表](class_a_k_1_1_i_write_bytes-members.html)

AK::IWriteBytes类 参考abstract

`#include <IBytes.h>`

类 AK::IWriteBytes 继承关系图:

![](../../../../images/class_a_k_1_1_i_write_bytes.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| Interface | |
| virtual bool | [WriteBytes](class_a_k_1_1_i_write_bytes_af52b6e689172d6ec3ac9288012436d65.html#af52b6e689172d6ec3ac9288012436d65) (const void \*in\_pData, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_cWritten)=0 |
|  | |
| Helpers | |
| template<class T > | |
| bool | [Write](class_a_k_1_1_i_write_bytes_a4db16f8c3735f39903277bd1cd24d9e1.html#a4db16f8c3735f39903277bd1cd24d9e1) (const T &in\_data) |
|  | |
| template<> |
| bool | [Write](class_a_k_1_1_i_write_bytes_a94945a17afde7c787007c6d04f2ca92f.html#a94945a17afde7c787007c6d04f2ca92f) (const bool &in\_data) |
|  | |

## 详细描述

Generic binary output interface.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

在文件 [IBytes.h](_i_bytes_8h_source.html) 第 [110](_i_bytes_8h_source.html#l00110) 行定义.