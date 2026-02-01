# AkSimdTypes.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Platforms](dir_9707d8b0bea28caa964fded672ce5309.html)
- [SSE](dir_da34b873a1a3774f4dcbbd9479a5cb37.html)

[类](#nested-classes)

AkSimdTypes.h 文件参考

`#include <xmmintrin.h>`  
`#include <emmintrin.h>`

[浏览源代码.](_platforms_2_s_s_e_2_ak_simd_types_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AKSIMD\_V4I32X2](struct_a_k_s_i_m_d___v4_i32_x2.html) |
|  | |
| struct | [AKSIMD\_V4I32X4](struct_a_k_s_i_m_d___v4_i32_x4.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| Platform specific defines for prefetching | |
| #define | [AKSIMD\_ARCHCACHELINESIZE](_platforms_2_s_s_e_2_ak_simd_types_8h_a4b65a228692375fcda4587bfe3c5775d.html#a4b65a228692375fcda4587bfe3c5775d)   (64) |
|  | Assumed cache line width for architectures on this platform [更多...](_platforms_2_s_s_e_2_ak_simd_types_8h_a4b65a228692375fcda4587bfe3c5775d.html#a4b65a228692375fcda4587bfe3c5775d) |
|  | |
| #define | [AKSIMD\_ARCHMAXPREFETCHSIZE](_platforms_2_s_s_e_2_ak_simd_types_8h_a87484f0fe32b8c8199e14efc937f699d.html#a87484f0fe32b8c8199e14efc937f699d)   (512) |
|  | |
| #define | [AKSIMD\_PREFETCHMEMORY](_platforms_2_s_s_e_2_ak_simd_types_8h_aca6c7c0477b808de201a0daac7904276.html#aca6c7c0477b808de201a0daac7904276)(\_\_offset\_\_, \_\_add\_\_)   \_mm\_prefetch(((char \*)(\_\_add\_\_))+(\_\_offset\_\_), \_MM\_HINT\_NTA ) |
|  | Cross-platform memory prefetch of effective address assuming non-temporal data [更多...](_platforms_2_s_s_e_2_ak_simd_types_8h_aca6c7c0477b808de201a0daac7904276.html#aca6c7c0477b808de201a0daac7904276) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| AKSIMD types | |
| typedef float | [AKSIMD\_F32](_platforms_2_s_s_e_2_ak_simd_types_8h_ac4d03b95a9a438d5566864e194443234.html#ac4d03b95a9a438d5566864e194443234) |
|  | 32-bit float [更多...](_platforms_2_s_s_e_2_ak_simd_types_8h_ac4d03b95a9a438d5566864e194443234.html#ac4d03b95a9a438d5566864e194443234) |
|  | |
| typedef \_\_m128 | [AKSIMD\_V4F32](_platforms_2_s_s_e_2_ak_simd_types_8h_a3bf07ac162476e7accdd8c3feb89d4b7.html#a3bf07ac162476e7accdd8c3feb89d4b7) |
|  | Vector of 4 32-bit floats [更多...](_platforms_2_s_s_e_2_ak_simd_types_8h_a3bf07ac162476e7accdd8c3feb89d4b7.html#a3bf07ac162476e7accdd8c3feb89d4b7) |
|  | |
| typedef [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [AKSIMD\_V4COND](_platforms_2_s_s_e_2_ak_simd_types_8h_a7ecb9968c67e1e8b5abcbf00d93df7d6.html#a7ecb9968c67e1e8b5abcbf00d93df7d6) |
|  | Vector of 4 comparison results [更多...](_platforms_2_s_s_e_2_ak_simd_types_8h_a7ecb9968c67e1e8b5abcbf00d93df7d6.html#a7ecb9968c67e1e8b5abcbf00d93df7d6) |
|  | |
| typedef [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [AKSIMD\_V4FCOND](_platforms_2_s_s_e_2_ak_simd_types_8h_ad34bacf31a0de57bc28048e3584aaf3a.html#ad34bacf31a0de57bc28048e3584aaf3a) |
|  | Vector of 4 comparison results [更多...](_platforms_2_s_s_e_2_ak_simd_types_8h_ad34bacf31a0de57bc28048e3584aaf3a.html#ad34bacf31a0de57bc28048e3584aaf3a) |
|  | |
| typedef \_\_m128i | [AKSIMD\_V4I32](_platforms_2_s_s_e_2_ak_simd_types_8h_a1bd246c4f4f698f7b0aae0baa7f8f8d3.html#a1bd246c4f4f698f7b0aae0baa7f8f8d3) |
|  | Vector of 4 32-bit signed integers [更多...](_platforms_2_s_s_e_2_ak_simd_types_8h_a1bd246c4f4f698f7b0aae0baa7f8f8d3.html#a1bd246c4f4f698f7b0aae0baa7f8f8d3) |
|  | |
| typedef [AKSIMD\_V4I32](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) | [AKSIMD\_V4ICOND](_platforms_2_s_s_e_2_ak_simd_types_8h_a76e0e71c4bf0a7f95b95f7c1ce75505e.html#a76e0e71c4bf0a7f95b95f7c1ce75505e) |
|  | |

## 详细描述

AKSIMD - SSE types definitions

在文件 [AkSimdTypes.h](_platforms_2_s_s_e_2_ak_simd_types_8h_source.html) 中定义.