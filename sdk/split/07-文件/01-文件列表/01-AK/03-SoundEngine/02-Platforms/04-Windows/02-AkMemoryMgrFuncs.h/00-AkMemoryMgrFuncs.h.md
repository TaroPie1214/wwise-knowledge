# AkMemoryMgrFuncs.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Platforms](dir_9707d8b0bea28caa964fded672ce5309.html)
- [Windows](dir_cb4788f46f1673a960402c6d809f92c5.html)

[命名空间](#namespaces) |
[宏定义](#define-members) |
[函数](#func-members)

AkMemoryMgrFuncs.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <cstdlib>`

[浏览源代码.](_platforms_2_windows_2_ak_memory_mgr_funcs_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
|  | [AKPLATFORM](namespace_a_k_p_l_a_t_f_o_r_m.html) |
|  | Platform-dependent helpers |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_VM\_PAGE\_SIZE](_platforms_2_windows_2_ak_memory_mgr_funcs_8h_a8fc741e47cf2e6ab246ea0c51ceabb4d.html#a8fc741e47cf2e6ab246ea0c51ceabb4d)   (16\*1024) |
|  | |
| #define | [AK\_VM\_HUGE\_PAGE\_SIZE](_platforms_2_windows_2_ak_memory_mgr_funcs_8h_a94fc9c438bc473d802157d78bf0a4fc8.html#a94fc9c438bc473d802157d78bf0a4fc8)   (2\*1024\*1024) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [AKPLATFORM::AllocSpan](namespace_a_k_p_l_a_t_f_o_r_m_a8607b18eaea4aa3fdfa581caee18970a.html#a8607b18eaea4aa3fdfa581caee18970a) (size\_t size, size\_t \*out\_userData) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AKPLATFORM::FreeSpan](namespace_a_k_p_l_a_t_f_o_r_m_a9bb64f59357062f99eb67c179ab1daba.html#a9bb64f59357062f99eb67c179ab1daba) (void \*address, size\_t size, size\_t in\_userData) |
|  | |