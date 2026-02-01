# AkSimdTypes.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Platforms](dir_9707d8b0bea28caa964fded672ce5309.html)
- [arm\_neon](dir_cb8d730ec7448ade74b00880a1c0dd04.html)

[宏定义](#define-members)

AkSimdTypes.h 文件参考

`#include <arm_neon.h>`  
`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_platforms_2arm__neon_2_ak_simd_types_8h_source.html)

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AKSIMD\_ARCHMAXPREFETCHSIZE](_platforms_2arm__neon_2_ak_simd_types_8h_a87484f0fe32b8c8199e14efc937f699d.html#a87484f0fe32b8c8199e14efc937f699d)   (512) |
|  | Use this to control how much prefetching maximum is desirable (assuming 8-way cache)   [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_a87484f0fe32b8c8199e14efc937f699d.html#a87484f0fe32b8c8199e14efc937f699d) |
|  | |
| #define | [AKSIMD\_ARCHCACHELINESIZE](_platforms_2arm__neon_2_ak_simd_types_8h_a4b65a228692375fcda4587bfe3c5775d.html#a4b65a228692375fcda4587bfe3c5775d)   (64) |
|  | Assumed cache line width for architectures on this platform [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_a4b65a228692375fcda4587bfe3c5775d.html#a4b65a228692375fcda4587bfe3c5775d) |
|  | |
| #define | [AKSIMD\_PREFETCHMEMORY](_platforms_2arm__neon_2_ak_simd_types_8h_aca6c7c0477b808de201a0daac7904276.html#aca6c7c0477b808de201a0daac7904276)(\_\_offset\_\_, \_\_add\_\_) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| AKSIMD types | |
| typedef int32x4\_t | [AKSIMD\_V4I32](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) |
|  | Vector of 4 32-bit signed integers [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) |
|  | |
| typedef int16x8\_t | [AKSIMD\_V8I16](_platforms_2arm__neon_2_ak_simd_types_8h_a65adeed93686c08e9fa72d952cd068ad.html#a65adeed93686c08e9fa72d952cd068ad) |
|  | Vector of 8 16-bit signed integers [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_a65adeed93686c08e9fa72d952cd068ad.html#a65adeed93686c08e9fa72d952cd068ad) |
|  | |
| typedef int16x4\_t | [AKSIMD\_V4I16](_platforms_2arm__neon_2_ak_simd_types_8h_a2ecae44e08019e96a2a0260cb4b59cd4.html#a2ecae44e08019e96a2a0260cb4b59cd4) |
|  | Vector of 4 16-bit signed integers [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_a2ecae44e08019e96a2a0260cb4b59cd4.html#a2ecae44e08019e96a2a0260cb4b59cd4) |
|  | |
| typedef uint32x4\_t | [AKSIMD\_V4UI32](_platforms_2arm__neon_2_ak_simd_types_8h_aee5c28dd6d10cd5a172e0d470fddf802.html#aee5c28dd6d10cd5a172e0d470fddf802) |
|  | Vector of 4 32-bit unsigned signed integers [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_aee5c28dd6d10cd5a172e0d470fddf802.html#aee5c28dd6d10cd5a172e0d470fddf802) |
|  | |
| typedef uint32x2\_t | [AKSIMD\_V2UI32](_platforms_2arm__neon_2_ak_simd_types_8h_a8a65e68698c7a59856d6eca980e2df26.html#a8a65e68698c7a59856d6eca980e2df26) |
|  | Vector of 2 32-bit unsigned signed integers [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_a8a65e68698c7a59856d6eca980e2df26.html#a8a65e68698c7a59856d6eca980e2df26) |
|  | |
| typedef int32x2\_t | [AKSIMD\_V2I32](_platforms_2arm__neon_2_ak_simd_types_8h_abb8d5eb781f0c08b1e3a83404850a941.html#abb8d5eb781f0c08b1e3a83404850a941) |
|  | Vector of 2 32-bit signed integers [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_abb8d5eb781f0c08b1e3a83404850a941.html#abb8d5eb781f0c08b1e3a83404850a941) |
|  | |
| typedef float32\_t | [AKSIMD\_F32](_platforms_2arm__neon_2_ak_simd_types_8h_ae27adc42127f4118c629383f01ab180a.html#ae27adc42127f4118c629383f01ab180a) |
|  | 32-bit float [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_ae27adc42127f4118c629383f01ab180a.html#ae27adc42127f4118c629383f01ab180a) |
|  | |
| typedef float32x2\_t | [AKSIMD\_V2F32](_platforms_2arm__neon_2_ak_simd_types_8h_aed084494a3d562047bb740839f7faa91.html#aed084494a3d562047bb740839f7faa91) |
|  | Vector of 2 32-bit floats [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_aed084494a3d562047bb740839f7faa91.html#aed084494a3d562047bb740839f7faa91) |
|  | |
| typedef float32x4\_t | [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) |
|  | Vector of 4 32-bit floats [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) |
|  | |
| typedef uint32x4\_t | [AKSIMD\_V4COND](_platforms_2arm__neon_2_ak_simd_types_8h_afb7c86c28c820a1b36aa724954a752e9.html#afb7c86c28c820a1b36aa724954a752e9) |
|  | Vector of 4 comparison results [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_afb7c86c28c820a1b36aa724954a752e9.html#afb7c86c28c820a1b36aa724954a752e9) |
|  | |
| typedef uint32x4\_t | [AKSIMD\_V4ICOND](_platforms_2arm__neon_2_ak_simd_types_8h_a5095dff08818d6ae0e647eca24a132b0.html#a5095dff08818d6ae0e647eca24a132b0) |
|  | Vector of 4 comparison results [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_a5095dff08818d6ae0e647eca24a132b0.html#a5095dff08818d6ae0e647eca24a132b0) |
|  | |
| typedef uint32x4\_t | [AKSIMD\_V4FCOND](_platforms_2arm__neon_2_ak_simd_types_8h_ab894b0173109220b318636645106c231.html#ab894b0173109220b318636645106c231) |
|  | Vector of 4 comparison results [更多...](_platforms_2arm__neon_2_ak_simd_types_8h_ab894b0173109220b318636645106c231.html#ab894b0173109220b318636645106c231) |
|  | |

## 详细描述

AKSIMD - arm\_neon types definition

在文件 [AkSimdTypes.h](_platforms_2arm__neon_2_ak_simd_types_8h_source.html) 中定义.