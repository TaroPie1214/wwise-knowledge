# ReadBytesMem

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [ReadBytesMem](class_a_k_1_1_read_bytes_mem.html)

[所有成员列表](class_a_k_1_1_read_bytes_mem-members.html) |
[Public 成员函数](#pub-methods)

AK::ReadBytesMem类 参考

`#include <AkBytesMem.h>`

类 AK::ReadBytesMem 继承关系图:

![](../../../../images/class_a_k_1_1_read_bytes_mem.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ReadBytesMem](class_a_k_1_1_read_bytes_mem_af1ded7dd2c858bfd14044cee78c31fbc.html#af1ded7dd2c858bfd14044cee78c31fbc) () |
|  | |
|  | [ReadBytesMem](class_a_k_1_1_read_bytes_mem_ae073fc0e4b7df8be320db0bac20b0d9f.html#ae073fc0e4b7df8be320db0bac20b0d9f) (const void \*in\_pBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes) |
|  | |
| virtual | [~ReadBytesMem](class_a_k_1_1_read_bytes_mem_af3740e323266ef21d33516fead7ca50f.html#af3740e323266ef21d33516fead7ca50f) () |
|  | |
| virtual bool | [ReadBytes](class_a_k_1_1_read_bytes_mem_a76acdbe78ec318c6447db6f103d3634e.html#a76acdbe78ec318c6447db6f103d3634e) (void \*in\_pData, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_cRead) |
|  | |
| void | [Attach](class_a_k_1_1_read_bytes_mem_a00798e5ae9dbbb17a3521dd4a5962a5b.html#a00798e5ae9dbbb17a3521dd4a5962a5b) (const void \*in\_pBytes, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_cBytes) |
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

在文件 [AkBytesMem.h](_ak_bytes_mem_8h_source.html) 第 [41](_ak_bytes_mem_8h_source.html#l00041) 行定义.