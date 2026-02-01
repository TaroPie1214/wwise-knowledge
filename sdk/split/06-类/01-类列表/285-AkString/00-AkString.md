# AkString

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_string-members.html) |
[Public 成员函数](#pub-methods)

AkString< TAlloc, T\_CHAR > 模板类 参考

`#include <AkString.h>`

类 AkString< TAlloc, T\_CHAR > 继承关系图:

![](../../../images/class_ak_string.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkString](class_ak_string_ad3fcd9a1747db3122c2a870e377a89e6.html#ad3fcd9a1747db3122c2a870e377a89e6) () |
|  | |
| template<typename T\_CHAR2 > | |
|  | [AkString](class_ak_string_ad7d17e45976f4b1e15efaaa992b63477.html#ad7d17e45976f4b1e15efaaa992b63477) (const T\_CHAR2 \*in\_pStr) |
|  | |
|  | [AkString](class_ak_string_ab8e590b92abec48c5dc41340870c3b68.html#ab8e590b92abec48c5dc41340870c3b68) (const [AkString](class_ak_string.html)< TAlloc, T\_CHAR > &in\_other) |
|  | |
| template<typename TAlloc2 , typename T\_CHAR2 > | |
|  | [AkString](class_ak_string_a6459a850f7727c7d7bc573e27b4b1db4.html#a6459a850f7727c7d7bc573e27b4b1db4) (const [AkString](class_ak_string.html)< TAlloc2, T\_CHAR2 > &in\_other) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AllocCopy](class_ak_string_a6ae1a86458017250ba597bf817816bf2.html#a6ae1a86458017250ba597bf817816bf2) () |
|  | |
| void | [Transfer](class_ak_string_a4717b301a9034d9b71bdd4226cedffde.html#a4717b301a9034d9b71bdd4226cedffde) ([AkString](class_ak_string.html)< TAlloc, T\_CHAR > &in\_from) |
|  | |
| const T\_CHAR \* | [Get](class_ak_string_ad854a6e407f13fdbcb5b828574503062.html#ad854a6e407f13fdbcb5b828574503062) () const |
|  | |
| [AkString](class_ak_string.html) & | [operator=](class_ak_string_acc49dbe04802e263c774655e3d31bcdb.html#acc49dbe04802e263c774655e3d31bcdb) (const [AkString](class_ak_string.html)< TAlloc, T\_CHAR > &in\_rhs) |
|  | |
| template<typename TAlloc2 , typename T\_CHAR2 > | |
| [AkString](class_ak_string.html) & | [operator=](class_ak_string_af0b928b0aba900b22ddfae9876e0145f.html#af0b928b0aba900b22ddfae9876e0145f) (const [AkString](class_ak_string.html)< TAlloc2, T\_CHAR2 > &in\_rhs) |
|  | |
| template<typename T\_CHAR2 > | |
| [AkString](class_ak_string.html) & | [operator=](class_ak_string_a8dcf0f7bed37e4cd99e1409c82be348e.html#a8dcf0f7bed37e4cd99e1409c82be348e) (const T\_CHAR2 \*in\_pStr) |
|  | |
| - Public 成员函数 继承自 [AkStringData< TAlloc, T\_CHAR >](class_ak_string_data.html) | |
|  | [AkStringData](class_ak_string_data_a03bf201c536ca05cd5acc64c3ce6ba04.html#a03bf201c536ca05cd5acc64c3ce6ba04) () |
|  | |
|  | [AkStringData](class_ak_string_data_aeda0f395d19fc2af5a6d1f2e0be6446e.html#aeda0f395d19fc2af5a6d1f2e0be6446e) (const T\_CHAR \*in\_pStr) |
|  | |
|  | [~AkStringData](class_ak_string_data_ac17da50222f224ed4f280c698b5583a5.html#ac17da50222f224ed4f280c698b5583a5) () |
|  | |
| void | [Term](class_ak_string_data_a307075dd442fcbd7014baf5300244455.html#a307075dd442fcbd7014baf5300244455) () |
|  | |
| void | [ClearReference](class_ak_string_data_ac6cbc85527dcbe050d83856fc0c3936f.html#ac6cbc85527dcbe050d83856fc0c3936f) () |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Protected 属性 继承自 [AkStringData< TAlloc, T\_CHAR >](class_ak_string_data.html) | |
| const T\_CHAR \* | [pStr](class_ak_string_data_a4ccedeabe08eac744e6d2a93e0727388.html#a4ccedeabe08eac744e6d2a93e0727388) |
|  | |
| bool | [bOwner](class_ak_string_data_aef3b9cbd81105c9ba135b88a0648381c.html#aef3b9cbd81105c9ba135b88a0648381c) |
|  | |

## 详细描述

### template<typename TAlloc, typename T\_CHAR> class AkString< TAlloc, T\_CHAR >

在文件 [AkString.h](_ak_string_8h_source.html) 第 [66](_ak_string_8h_source.html#l00066) 行定义.