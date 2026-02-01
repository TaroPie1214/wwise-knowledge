# AkSimd.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[宏定义](#define-members) |
[函数](#func-members)

AkSimd.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/SoundEngine/Platforms/SSE/AkSimd.h>`

[浏览源代码.](_common_2_ak_simd_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AKSIMD\_DECLARE\_V4F32\_TYPE](struct_a_k_s_i_m_d___d_e_c_l_a_r_e___v4_f32___t_y_p_e.html) |
|  | |
| struct | [AKSIMD\_DECLARE\_V4I32\_TYPE](struct_a_k_s_i_m_d___d_e_c_l_a_r_e___v4_i32___t_y_p_e.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AKSIMD\_GETELEMENT\_V4F32](_common_2_ak_simd_8h_abe80011c99c25d443c6142ecaa071a00.html#abe80011c99c25d443c6142ecaa071a00)(\_\_vName, \_\_num\_\_)   (([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)\*)&(\_\_vName))[(\_\_num\_\_)] |
|  | Get the element at index **num** in vector \_\_vName [更多...](_common_2_ak_simd_8h_abe80011c99c25d443c6142ecaa071a00.html#abe80011c99c25d443c6142ecaa071a00) |
|  | |
| #define | [AKSIMD\_GETELEMENT\_V2F32](_common_2_ak_simd_8h_a5fcf3dd4c127fa196ee0a3f40c5c2c8b.html#a5fcf3dd4c127fa196ee0a3f40c5c2c8b)(\_\_vName, \_\_num\_\_)   (([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)\*)&(\_\_vName))[(\_\_num\_\_)] |
|  | |
| #define | [AKSIMD\_GETELEMENT\_V2F64](_common_2_ak_simd_8h_af58727926d47080100cb6f5712dc1a24.html#af58727926d47080100cb6f5712dc1a24)(\_\_vName, \_\_num\_\_)   (([AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e)\*)&(\_\_vName))[(\_\_num\_\_)] |
|  | |
| #define | [AKSIMD\_GETELEMENT\_V4I32](_common_2_ak_simd_8h_a0f6ebe0e17fa4f40dca4cd49bf729e4f.html#a0f6ebe0e17fa4f40dca4cd49bf729e4f)(\_\_vName, \_\_num\_\_)   (([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154)\*)&(\_\_vName))[(\_\_num\_\_)] |
|  | |
| #define | [AKSIMD\_GETELEMENT\_V2I64](_common_2_ak_simd_8h_a4291905609bada882dff75cbaf577159.html#a4291905609bada882dff75cbaf577159)(\_\_vName, \_\_num\_\_)   (([AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c)\*)&(\_\_vName))[(\_\_num\_\_)] |
|  | |
| #define | [AKSIMD\_ASSERTFLUSHZEROMODE](_common_2_ak_simd_8h_aa5a19842f108ebcee2816c1570db01aa.html#aa5a19842f108ebcee2816c1570db01aa) |
|  | |
| #define | [AKSIMD\_SETVR\_V2F64](_common_2_ak_simd_8h_ad01aa01d1bc3fa0f6386f872a52b36f4.html#ad01aa01d1bc3fa0f6386f872a52b36f4)(\_a, \_b)   [AKSIMD\_SETV\_V2F64](_platforms_2arm__neon_2_ak_simd_8h_aeebc9cf982c5140cd825e48ec311ddb6.html#aeebc9cf982c5140cd825e48ec311ddb6)( (\_b), (\_a) ) |
|  | |
| #define | [AKSIMD\_SETVR\_V4F32](_common_2_ak_simd_8h_a578a6baf49fcd42398f880e35c69b267.html#a578a6baf49fcd42398f880e35c69b267)(\_a, \_b, \_c, \_d)   [AKSIMD\_SETV\_V4F32](_platforms_2arm__neon_2_ak_simd_8h_ad7eb8b78e41f7f74240b857eb7bfa668.html#ad7eb8b78e41f7f74240b857eb7bfa668)( (\_d), (\_c), (\_b), (\_a) ) |
|  | |
| #define | [AKSIMD\_SETVR\_V2I64](_common_2_ak_simd_8h_acd0a2f7fabd14f9695f8cc705fdfffb2.html#acd0a2f7fabd14f9695f8cc705fdfffb2)(\_a, \_b)   [AKSIMD\_SETV\_V2I64](_platforms_2arm__neon_2_ak_simd_8h_a1605ad05a00b4b577c8519019016c507.html#a1605ad05a00b4b577c8519019016c507)( (\_b), (\_a) ) |
|  | |
| #define | [AKSIMD\_SETVR\_V4I32](_common_2_ak_simd_8h_af9cd5e61a8136ae0f663524f61d3fbbd.html#af9cd5e61a8136ae0f663524f61d3fbbd)(\_a, \_b, \_c, \_d)   [AKSIMD\_SETV\_V4I32](_platforms_2arm__neon_2_ak_simd_8h_a797aa36ad77174f722c09e57af1dd869.html#a797aa36ad77174f722c09e57af1dd869)( (\_d), (\_c), (\_b), (\_a) ) |
|  | |
| #define | [AKSIMD\_DECLARE\_V4F32](_common_2_ak_simd_8h_a738e06a53d5871b09bfc6b6cd09f0f56.html#a738e06a53d5871b09bfc6b6cd09f0f56)(\_x, \_a, \_b, \_c, \_d)   [AKSIMD\_DECLARE\_V4F32\_TYPE](struct_a_k_s_i_m_d___d_e_c_l_a_r_e___v4_f32___t_y_p_e.html) \_x = { \_a, \_b, \_c, \_d }; |
|  | |
| #define | [AKSIMD\_DECLARE\_V4I32](_common_2_ak_simd_8h_ad71177e8ea3d9718c38ec407df659682.html#ad71177e8ea3d9718c38ec407df659682)(\_x, \_a, \_b, \_c, \_d)   [AKSIMD\_DECLARE\_V4I32\_TYPE](struct_a_k_s_i_m_d___d_e_c_l_a_r_e___v4_i32___t_y_p_e.html) \_x = { \_a, \_b, \_c, \_d }; |
|  | |
| #define | [AKSIMD\_SETELEMENT\_V4F32](_common_2_ak_simd_8h_a9a279e95fe547edb5bf7e95b1074ae9e.html#a9a279e95fe547edb5bf7e95b1074ae9e)(\_\_vName\_\_, \_\_num\_\_, \_\_value\_\_)   ( [AKSIMD\_GETELEMENT\_V4F32](_common_2_ak_simd_8h_abe80011c99c25d443c6142ecaa071a00.html#abe80011c99c25d443c6142ecaa071a00)( \_\_vName\_\_, \_\_num\_\_ ) = (\_\_value\_\_) ) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AKSIMD\_TRANSPOSE4X4\_V4F32](_common_2_ak_simd_8h_a271ab947b875950a04494ae23261d7da.html#a271ab947b875950a04494ae23261d7da) ([AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &A, [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &B, [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &C, [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &D) |
|  | |

## 详细描述

Simd definitions.

在文件 [AkSimd.h](_common_2_ak_simd_8h_source.html) 中定义.