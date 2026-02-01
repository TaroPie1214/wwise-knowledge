# ReadBytesSkip

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [ReadBytesSkip](class_a_k_1_1_read_bytes_skip.html)

[所有成员列表](class_a_k_1_1_read_bytes_skip-members.html) |
[Public 成员函数](#pub-methods)

AK::ReadBytesSkip类 参考

`#include <AkBytesCount.h>`

类 AK::ReadBytesSkip 继承关系图:

![](../../../../images/class_a_k_1_1_read_bytes_skip.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ReadBytesSkip](class_a_k_1_1_read_bytes_skip_a6d9cbd328542519937c67c78604f4875.html#a6d9cbd328542519937c67c78604f4875) () |
|  | |
|  | [ReadBytesSkip](class_a_k_1_1_read_bytes_skip_a96764f8fae5b7ee1fefb8277a247bdc3.html#a96764f8fae5b7ee1fefb8277a247bdc3) (const void \*in\_pBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes) |
|  | |
| virtual | [~ReadBytesSkip](class_a_k_1_1_read_bytes_skip_a8ed6bd6bca6d26557f985bf7747afbb6.html#a8ed6bd6bca6d26557f985bf7747afbb6) () |
|  | |
| virtual bool | [ReadBytes](class_a_k_1_1_read_bytes_skip_ae7b81d58afc301b7c43b235700218364.html#ae7b81d58afc301b7c43b235700218364) (void \*in\_pData, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_cRead) |
|  | |
| void | [Attach](class_a_k_1_1_read_bytes_skip_ab3b5c0b84b3f39c40d38530211165cc7.html#ab3b5c0b84b3f39c40d38530211165cc7) (const void \*in\_pBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes) |
|  | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [Count](class_a_k_1_1_read_bytes_skip_a09fa448730362dd3de9004979b521098.html#a09fa448730362dd3de9004979b521098) () |
|  | |
| - Public 成员函数 继承自 [AK::IReadBytes](class_a_k_1_1_i_read_bytes.html) | |
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

在文件 [AkBytesCount.h](_ak_bytes_count_8h_source.html) 第 [41](_ak_bytes_count_8h_source.html#l00041) 行定义.