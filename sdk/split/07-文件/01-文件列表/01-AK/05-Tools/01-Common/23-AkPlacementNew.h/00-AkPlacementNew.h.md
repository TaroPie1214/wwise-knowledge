# AkPlacementNew.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[宏定义](#define-members) |
[函数](#func-members)

AkPlacementNew.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_ak_placement_new_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkPlacementNewKey](struct_ak_placement_new_key.html) |
|  | Unique structure identifier for AkPlacementNew. [更多...](struct_ak_placement_new_key.html#details) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AkPlacementNew](_ak_placement_new_8h_a13ef391d918971bbd3233ce29988ea52.html#a13ef391d918971bbd3233ce29988ea52)(\_memory)   ::new( \_memory, [AkPlacementNewKey](struct_ak_placement_new_key.html)() ) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [operator new](_ak_placement_new_8h_a1e84f55611a9891e88306198d79ba96e.html#a1e84f55611a9891e88306198d79ba96e) (size\_t, void \*memory, const [AkPlacementNewKey](struct_ak_placement_new_key.html) &) throw () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [operator delete](_ak_placement_new_8h_a3c2d0d16501b113b24cbacf5b859d618.html#a3c2d0d16501b113b24cbacf5b859d618) (void \*, void \*, const [AkPlacementNewKey](struct_ak_placement_new_key.html) &) throw () |
|  | |