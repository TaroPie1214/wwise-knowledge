# AkDynaBlkPool.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[宏定义](#define-members)

AkDynaBlkPool.h 文件参考

`#include <AK/Tools/Common/AkAssert.h>`  
`#include <AK/Tools/Common/AkListBareLight.h>`  
`#include <AK/Tools/Common/AkPlacementNew.h>`

[浏览源代码.](_ak_dyna_blk_pool_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AkDynaBlkPool< T, uPoolChunkSize, TAlloc >](class_ak_dyna_blk_pool.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [STATS\_ALLOC](_ak_dyna_blk_pool_8h_ab55c7e4f4235fbbe513a1cbe956f8e98.html#ab55c7e4f4235fbbe513a1cbe956f8e98)() |
|  | |
| #define | [STATS\_NEWCHUNK](_ak_dyna_blk_pool_8h_a9d317ca8cb6e954fb47e512b9ca61abc.html#a9d317ca8cb6e954fb47e512b9ca61abc)() |
|  | |
| #define | [STATS\_FREE](_ak_dyna_blk_pool_8h_aeca972a624608f5b696979e8b9ae6cc4.html#aeca972a624608f5b696979e8b9ae6cc4)() |
|  | |
| #define | [STATS\_DELCHUNK](_ak_dyna_blk_pool_8h_a9099d409dd8dcdd24ea2f01c3e08a63b.html#a9099d409dd8dcdd24ea2f01c3e08a63b)() |
|  | |
| #define | [SCRUB\_NEW\_CHUNK](_ak_dyna_blk_pool_8h_a919381255f625a948f7d4f6ca2c45235.html#a919381255f625a948f7d4f6ca2c45235)() |
|  | |
| #define | [SCRUB\_NEW\_ALLOC](_ak_dyna_blk_pool_8h_a81cb49a28bd734af8077e9a5d8683540.html#a81cb49a28bd734af8077e9a5d8683540)(pItem) |
|  | |
| #define | [SCRUB\_FREE\_BLOCK](_ak_dyna_blk_pool_8h_aeeee8235bd052e4ef2f312e11076fc8d.html#aeeee8235bd052e4ef2f312e11076fc8d)(pObj) |
|  | |