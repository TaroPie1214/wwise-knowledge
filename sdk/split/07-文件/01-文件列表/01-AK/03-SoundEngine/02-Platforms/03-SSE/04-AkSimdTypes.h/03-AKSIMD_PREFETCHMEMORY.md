# AKSIMD_PREFETCHMEMORY

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Platforms](dir_9707d8b0bea28caa964fded672ce5309.html)
- [SSE](dir_da34b873a1a3774f4dcbbd9479a5cb37.html)
- [AkSimdTypes.h](_platforms_2_s_s_e_2_ak_simd_types_8h.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AKSIMD\_ARCHCACHELINESIZE](_platforms_2_s_s_e_2_ak_simd_types_8h_a4b65a228692375fcda4587bfe3c5775d.html#a4b65a228692375fcda4587bfe3c5775d) | | [AKSIMD\_ARCHMAXPREFETCHSIZE](_platforms_2_s_s_e_2_ak_simd_types_8h_a87484f0fe32b8c8199e14efc937f699d.html#a87484f0fe32b8c8199e14efc937f699d) | | [AKSIMD\_F32](_platforms_2_s_s_e_2_ak_simd_types_8h_ac4d03b95a9a438d5566864e194443234.html#ac4d03b95a9a438d5566864e194443234) | | [AKSIMD\_PREFETCHMEMORY](_platforms_2_s_s_e_2_ak_simd_types_8h_aca6c7c0477b808de201a0daac7904276.html#aca6c7c0477b808de201a0daac7904276) | | [AKSIMD\_V4COND](_platforms_2_s_s_e_2_ak_simd_types_8h_a7ecb9968c67e1e8b5abcbf00d93df7d6.html#a7ecb9968c67e1e8b5abcbf00d93df7d6) | | [AKSIMD\_V4F32](_platforms_2_s_s_e_2_ak_simd_types_8h_a3bf07ac162476e7accdd8c3feb89d4b7.html#a3bf07ac162476e7accdd8c3feb89d4b7) | | [AKSIMD\_V4FCOND](_platforms_2_s_s_e_2_ak_simd_types_8h_ad34bacf31a0de57bc28048e3584aaf3a.html#ad34bacf31a0de57bc28048e3584aaf3a) | | [AKSIMD\_V4I32](_platforms_2_s_s_e_2_ak_simd_types_8h_a1bd246c4f4f698f7b0aae0baa7f8f8d3.html#a1bd246c4f4f698f7b0aae0baa7f8f8d3) | | [AKSIMD\_V4ICOND](_platforms_2_s_s_e_2_ak_simd_types_8h_a76e0e71c4bf0a7f95b95f7c1ce75505e.html#a76e0e71c4bf0a7f95b95f7c1ce75505e) | | [◆](#aca6c7c0477b808de201a0daac7904276)AKSIMD\_PREFETCHMEMORY |  |  |  |  | | --- | --- | --- | --- | | #define AKSIMD\_PREFETCHMEMORY | ( |  | \_\_offset\_\_, | |  |  |  | \_\_add\_\_ | |  | ) |  | \_mm\_prefetch(((char \*)(\_\_add\_\_))+(\_\_offset\_\_), \_MM\_HINT\_NTA ) |  Cross-platform memory prefetch of effective address assuming non-temporal data  在文件 [AkSimdTypes.h](_platforms_2_s_s_e_2_ak_simd_types_8h_source.html) 第 [44](_platforms_2_s_s_e_2_ak_simd_types_8h_source.html#l00044) 行定义. |