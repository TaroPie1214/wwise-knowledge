# AkDbWeakString

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_db_weak_string-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AkDbWeakString< TAlloc, T\_CHAR > 模板类 参考

`#include <AkString.h>`

|  |  |
| --- | --- |
| Public 类型 | |
| typedef [AkDbString](class_ak_db_string.html)< TAlloc, T\_CHAR > | [\_String](class_ak_db_weak_string_a0aa7b801e9e286755138f867916d2237.html#a0aa7b801e9e286755138f867916d2237) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkDbWeakString](class_ak_db_weak_string_a4fa64d3dbbb2583fa5d6d9a48021fe1d.html#a4fa64d3dbbb2583fa5d6d9a48021fe1d) () |
|  | |
|  | [AkDbWeakString](class_ak_db_weak_string_aa02c21462c913b45dcdb28456a58852e.html#aa02c21462c913b45dcdb28456a58852e) (const [AkDbWeakString](class_ak_db_weak_string.html) &in\_rhs) |
|  | |
|  | [AkDbWeakString](class_ak_db_weak_string_a7dbb51843e429f7bf5bdbb1c30fa3d9b.html#a7dbb51843e429f7bf5bdbb1c30fa3d9b) (const [\_String](class_ak_db_weak_string_a0aa7b801e9e286755138f867916d2237.html#a0aa7b801e9e286755138f867916d2237) &in\_dbString) |
|  | |
| [AkDbWeakString](class_ak_db_weak_string.html) & | [operator=](class_ak_db_weak_string_a37ae6d0edb9a70d6eff3e41e35818404.html#a37ae6d0edb9a70d6eff3e41e35818404) (const [\_String](class_ak_db_weak_string_a0aa7b801e9e286755138f867916d2237.html#a0aa7b801e9e286755138f867916d2237) &in\_dbString) |
|  | |
| [AkDbWeakString](class_ak_db_weak_string.html) & | [operator=](class_ak_db_weak_string_abfb1ae1d7560fb97ab698413d7973d78.html#abfb1ae1d7560fb97ab698413d7973d78) (const [AkDbWeakString](class_ak_db_weak_string.html) &in\_rhs) |
|  | |
| const T\_CHAR \* | [Get](class_ak_db_weak_string_abc39ceab680cec90228d8a4ff533aedb.html#abc39ceab680cec90228d8a4ff533aedb) () const |
|  | |

## 详细描述

### template<typename TAlloc, typename T\_CHAR> class AkDbWeakString< TAlloc, T\_CHAR >

A [AkDbWeakString](class_ak_db_weak_string.html) always references a DbString. If the DbString content has been released then the [AkDbWeakString](class_ak_db_weak_string.html) will return a null value. A [AkDbWeakString](class_ak_db_weak_string.html) does not prevent the DbString content to be released.

在文件 [AkString.h](_ak_string_8h_source.html) 第 [510](_ak_string_8h_source.html#l00510) 行定义.