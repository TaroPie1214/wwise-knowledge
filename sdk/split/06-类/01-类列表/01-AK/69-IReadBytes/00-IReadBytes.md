# IReadBytes

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IReadBytes](class_a_k_1_1_i_read_bytes.html)

[所有成员列表](class_a_k_1_1_i_read_bytes-members.html)

AK::IReadBytes类 参考abstract

`#include <IBytes.h>`

类 AK::IReadBytes 继承关系图:

![](../../../../images/class_a_k_1_1_i_read_bytes.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| Interface | |
| virtual bool | [ReadBytes](class_a_k_1_1_i_read_bytes_a9814c15733b485b2b0443b2097b8ce91.html#a9814c15733b485b2b0443b2097b8ce91) (void \*in\_pData, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_cRead)=0 |
|  | |
| Helpers | |
| template<class T > | |
| bool | [Read](class_a_k_1_1_i_read_bytes_a965ac2f82d5cecf138e0a00e48eb57b6.html#a965ac2f82d5cecf138e0a00e48eb57b6) (T &out\_data) |
|  | |
| template<> |
| bool | [Read](class_a_k_1_1_i_read_bytes_af309b2ebf268abdbe56a7f2c7416c94b.html#af309b2ebf268abdbe56a7f2c7416c94b) (bool &out\_data) |
|  | |
| template<class T > | |
| T | [Read](class_a_k_1_1_i_read_bytes_a9c5de86288182bdc144ca72f40957fb9.html#a9c5de86288182bdc144ca72f40957fb9) () |
|  | |

## 详细描述

Generic binary input interface.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

在文件 [IBytes.h](_i_bytes_8h_source.html) 第 [42](_i_bytes_8h_source.html#l00042) 行定义.