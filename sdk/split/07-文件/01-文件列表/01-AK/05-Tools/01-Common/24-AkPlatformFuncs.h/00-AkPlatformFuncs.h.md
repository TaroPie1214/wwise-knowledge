# AkPlatformFuncs.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[命名空间](#namespaces) |
[宏定义](#define-members) |
[函数](#func-members)

AkPlatformFuncs.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/SoundEngine/Common/AkAtomicTypes.h>`  
`#include <AK/Tools/Win32/AkPlatformFuncs.h>`

[浏览源代码.](_common_2_ak_platform_funcs_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AKPLATFORM](namespace_a_k_p_l_a_t_f_o_r_m.html) |
|  | Platform-dependent helpers |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AkPrefetchZero](_common_2_ak_platform_funcs_8h_a948f8234e77c82826ef1427963ce79ff.html#a948f8234e77c82826ef1427963ce79ff)(\_\_\_Dest, \_\_\_Size) |
|  | |
| #define | [AkPrefetchZeroAligned](_common_2_ak_platform_funcs_8h_a9577f84ebe2c6dab4b4dbab32f093ab9.html#a9577f84ebe2c6dab4b4dbab32f093ab9)(\_\_\_Dest, \_\_\_Size) |
|  | |
| #define | [AkZeroMemAligned](_common_2_ak_platform_funcs_8h_a47d685aca03fd3503d34dddc2fa2f49f.html#a47d685aca03fd3503d34dddc2fa2f49f)(\_\_\_Dest, \_\_\_Size)   [AKPLATFORM::AkMemSet](namespace_a_k_p_l_a_t_f_o_r_m_afe598f5d7465d44a10e8414716fab233.html#afe598f5d7465d44a10e8414716fab233)(\_\_\_Dest, 0, \_\_\_Size); |
|  | |
| #define | [AkZeroMemLarge](_common_2_ak_platform_funcs_8h_ad253eddc87f890ca9677913bd66299b5.html#ad253eddc87f890ca9677913bd66299b5)(\_\_\_Dest, \_\_\_Size)   [AKPLATFORM::AkMemSet](namespace_a_k_p_l_a_t_f_o_r_m_afe598f5d7465d44a10e8414716fab233.html#afe598f5d7465d44a10e8414716fab233)(\_\_\_Dest, 0, \_\_\_Size); |
|  | |
| #define | [AkZeroMemSmall](_common_2_ak_platform_funcs_8h_a36b3303234948398066f358466a84e3c.html#a36b3303234948398066f358466a84e3c)(\_\_\_Dest, \_\_\_Size)   [AKPLATFORM::AkMemSet](namespace_a_k_p_l_a_t_f_o_r_m_afe598f5d7465d44a10e8414716fab233.html#afe598f5d7465d44a10e8414716fab233)(\_\_\_Dest, 0, \_\_\_Size); |
|  | |
| #define | [AK\_THREAD\_INIT\_CODE](_common_2_ak_platform_funcs_8h_a8edb6983a1b26c16e683dcc1e205af43.html#a8edb6983a1b26c16e683dcc1e205af43)(\_threadProperties) |
|  | |
| #define | [AK\_FORCE\_CRASH](_common_2_ak_platform_funcs_8h_a869402461ee413c74d903c6c592fa585.html#a869402461ee413c74d903c6c592fa585)   [AKPLATFORM::AkForceCrash](namespace_a_k_p_l_a_t_f_o_r_m_a45b900549b5f7cce202a6d9dce6a1b79.html#a45b900549b5f7cce202a6d9dce6a1b79)() |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AKPLATFORM::AkMemCpy](namespace_a_k_p_l_a_t_f_o_r_m_ad1c5908442668cc811569b8a35f37b15.html#ad1c5908442668cc811569b8a35f37b15) (void \*pDest, const void \*pSrc, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uSize) |
|  | Platform Independent Helper for memcpy/memmove/memset [更多...](namespace_a_k_p_l_a_t_f_o_r_m_ad1c5908442668cc811569b8a35f37b15.html#ad1c5908442668cc811569b8a35f37b15) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AKPLATFORM::AkMemMove](namespace_a_k_p_l_a_t_f_o_r_m_a0bee6a8bbd2d592ac1e98cd3c462902c.html#a0bee6a8bbd2d592ac1e98cd3c462902c) (void \*pDest, const void \*pSrc, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uSize) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AKPLATFORM::AkMemSet](namespace_a_k_p_l_a_t_f_o_r_m_afe598f5d7465d44a10e8414716fab233.html#afe598f5d7465d44a10e8414716fab233) (void \*pDest, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iVal, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uSize) |
|  | |
| bool | [AKPLATFORM::AkIsValidThread](namespace_a_k_p_l_a_t_f_o_r_m_ad134b612eb6398cdfc0b621f5733a7fd.html#ad134b612eb6398cdfc0b621f5733a7fd) ([AkThread](_platforms_2_windows_2_ak_types_8h_a7cd2d8431cd51231604a8fa348a800d5.html#a7cd2d8431cd51231604a8fa348a800d5) \*in\_pThread) |
|  | |
| void | [AKPLATFORM::AkCloseThread](namespace_a_k_p_l_a_t_f_o_r_m_a449572808868e3bb2eceb475fc783d10.html#a449572808868e3bb2eceb475fc783d10) ([AkThread](_platforms_2_windows_2_ak_types_8h_a7cd2d8431cd51231604a8fa348a800d5.html#a7cd2d8431cd51231604a8fa348a800d5) \*in\_pThread, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pMemAlloc) |
|  | |
| void | [AKPLATFORM::AkClearThread](namespace_a_k_p_l_a_t_f_o_r_m_ae2180cd2f5c38fe583e2f4a2d15fd307.html#ae2180cd2f5c38fe583e2f4a2d15fd307) ([AkThread](_platforms_2_windows_2_ak_types_8h_a7cd2d8431cd51231604a8fa348a800d5.html#a7cd2d8431cd51231604a8fa348a800d5) \*in\_pThread) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AKPLATFORM::AkCreateThread](namespace_a_k_p_l_a_t_f_o_r_m_a5adcd79bbae163c2404c5b1ac57a0334.html#a5adcd79bbae163c2404c5b1ac57a0334) ([AkThreadRoutine](_platforms_2_windows_2_ak_types_8h_a11f699a47a92db1df41d038c95267931.html#a11f699a47a92db1df41d038c95267931) pStartRoutine, void \*pParams, const [AkThreadProperties](struct_ak_thread_properties.html) &in\_threadProperties, [AkThread](_platforms_2_windows_2_ak_types_8h_a7cd2d8431cd51231604a8fa348a800d5.html#a7cd2d8431cd51231604a8fa348a800d5) \*out\_pThread, const char \*in\_szThreadName, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pMemAlloc) |
|  | |
| void | [AKPLATFORM::AkSleep](namespace_a_k_p_l_a_t_f_o_r_m_aacfeaa07eeeea022207bb97991cc6260.html#aacfeaa07eeeea022207bb97991cc6260) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulMilliseconds) |
|  | |
| void | [AKPLATFORM::AkWaitForSingleThread](namespace_a_k_p_l_a_t_f_o_r_m_a47c50557b984d84816b8ce172bba1684.html#a47c50557b984d84816b8ce172bba1684) ([AkThread](_platforms_2_windows_2_ak_types_8h_a7cd2d8431cd51231604a8fa348a800d5.html#a7cd2d8431cd51231604a8fa348a800d5) \*in\_pThread) |
|  | |
| [AkThreadID](_platforms_2_windows_2_ak_types_8h_a300efeb7dbe0b9bde253dd9b9bbcb6ee.html#a300efeb7dbe0b9bde253dd9b9bbcb6ee) | [AKPLATFORM::CurrentThread](namespace_a_k_p_l_a_t_f_o_r_m_ac05265e6bf8450c8872eb8278b1cfb78.html#ac05265e6bf8450c8872eb8278b1cfb78) () |
|  | |
| void | [AKPLATFORM::AkGetDefaultThreadProperties](namespace_a_k_p_l_a_t_f_o_r_m_af8ca5269595a1270425d165061ec182a.html#af8ca5269595a1270425d165061ec182a) ([AkThreadProperties](struct_ak_thread_properties.html) &out\_threadProperties) |
|  | |
| void | [AKPLATFORM::AkGetDefaultHighPriorityThreadProperties](namespace_a_k_p_l_a_t_f_o_r_m_a208b3cf7ce320617108e1e6105dfa007.html#a208b3cf7ce320617108e1e6105dfa007) ([AkThreadProperties](struct_ak_thread_properties.html) &out\_threadProperties) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AKPLATFORM::AkForceCrash](namespace_a_k_p_l_a_t_f_o_r_m_a45b900549b5f7cce202a6d9dce6a1b79.html#a45b900549b5f7cce202a6d9dce6a1b79) () |
|  | |

## 详细描述

Platform-dependent functions definition.

在文件 [AkPlatformFuncs.h](_common_2_ak_platform_funcs_8h_source.html) 中定义.