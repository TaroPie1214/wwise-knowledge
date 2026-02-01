# AkString.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[函数](#func-members)

AkString.h 文件参考

`#include <AK/Tools/Common/AkFNVHash.h>`  
`#include <AK/Tools/Common/AkHashList.h>`  
`#include <AK/Tools/Common/AkPlacementNew.h>`

[浏览源代码.](_ak_string_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AkStringData< TAlloc, T\_CHAR >](class_ak_string_data.html) |
|  | |
| class | [AkStringImpl< TAlloc, T\_CHAR >](class_ak_string_impl.html) |
|  | |
| class | [AkString< TAlloc, T\_CHAR >](class_ak_string.html) |
|  | |
| class | [AkStringImpl< TAlloc, char >](class_ak_string_impl_3_01_t_alloc_00_01char_01_4.html) |
|  | |
| class | [AkDbString< TAlloc, T\_CHAR >](class_ak_db_string.html) |
|  | |
| struct | [AkDbString< TAlloc, T\_CHAR >::Entry](struct_ak_db_string_1_1_entry.html) |
|  | |
| struct | [AkDbString< TAlloc, T\_CHAR >::Instance](struct_ak_db_string_1_1_instance.html) |
|  | |
| class | [AkDbWeakString< TAlloc, T\_CHAR >](class_ak_db_weak_string.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| template<typename TAlloc , typename T\_CHAR > | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkHash](_ak_string_8h_a7c3ff67c7058525887c96c017419456b.html#a7c3ff67c7058525887c96c017419456b) (const [AkString](class_ak_string.html)< TAlloc, T\_CHAR > &in\_str) |
|  | |