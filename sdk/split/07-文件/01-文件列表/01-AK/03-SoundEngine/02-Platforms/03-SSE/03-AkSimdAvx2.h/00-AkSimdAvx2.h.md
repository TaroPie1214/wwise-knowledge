# AkSimdAvx2.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Platforms](dir_9707d8b0bea28caa964fded672ce5309.html)
- [SSE](dir_da34b873a1a3774f4dcbbd9479a5cb37.html)

[宏定义](#define-members)

AkSimdAvx2.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/SoundEngine/Platforms/SSE/AkSimd.h>`  
`#include <AK/SoundEngine/Platforms/SSE/AkSimdAvx.h>`

[浏览源代码.](_ak_simd_avx2_8h_source.html)

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [\_GATHER\_SIM\_FETCH](_ak_simd_avx2_8h_a5fd8e7b5f053c0d45434bbb4c18a2f09.html#a5fd8e7b5f053c0d45434bbb4c18a2f09)(\_x) |
|  | |
| #define | [\_GATHER\_SIM\_FETCH](_ak_simd_avx2_8h_a5fd8e7b5f053c0d45434bbb4c18a2f09.html#a5fd8e7b5f053c0d45434bbb4c18a2f09)(\_x) |
|  | |
| AKSIMD shuffling | |
| #define | [AKSIMD\_SHUFFLEB\_V8I32](_ak_simd_avx2_8h_a83376bb93ba210cb81a89d17af08157e.html#a83376bb93ba210cb81a89d17af08157e)(a, b)   \_mm256\_shuffle\_epi8(a, b) |
|  | |
| #define | [AKSIMD\_BLEND\_V16I16](_ak_simd_avx2_8h_a7d760eb72afba63c469996adfb6ba763.html#a7d760eb72afba63c469996adfb6ba763)(a, b, i)   \_mm256\_blend\_epi16(a, b, i) |
|  | |
| #define | [AKSIMD\_INSERT\_V2I128](_ak_simd_avx2_8h_ad063b3d4a7887244f9ce3c1699043543.html#ad063b3d4a7887244f9ce3c1699043543)(a, m128, idx)   \_mm256\_inserti128\_si256(a, m128, idx) |
|  | |
| #define | [AKSIMD\_PERMUTE\_2X128\_V8I32](_ak_simd_avx2_8h_aac56c1759af66622643bf3b0f870c663.html#aac56c1759af66622643bf3b0f870c663)(a, b, i)   \_mm256\_permute2x128\_si256(a, b, i) |
|  | |
| #define | [AKSIMD\_DEINTERLEAVELANES\_LO\_V8I32](_ak_simd_avx2_8h_a473c8fee1b50a405707d17a49cabe40b.html#a473c8fee1b50a405707d17a49cabe40b)(a, b)   [AKSIMD\_PERMUTE\_2X128\_V8I32](_ak_simd_avx2_8h_aac56c1759af66622643bf3b0f870c663.html#aac56c1759af66622643bf3b0f870c663)(a, b, AKSIMD\_PERMUTE128(2, 0)) |
|  | Selects the lower of each of the 128b lanes in a and b to be the result ( B A ), ( D C ) -> ( C A ) [更多...](_ak_simd_avx2_8h_a473c8fee1b50a405707d17a49cabe40b.html#a473c8fee1b50a405707d17a49cabe40b) |
|  | |
| #define | [AKSIMD\_DEINTERLEAVELANES\_HI\_V8I32](_ak_simd_avx2_8h_ade6587a0488db010074b2b67e7bdd9b1.html#ade6587a0488db010074b2b67e7bdd9b1)(a, b)   [AKSIMD\_PERMUTE\_2X128\_V8I32](_ak_simd_avx2_8h_aac56c1759af66622643bf3b0f870c663.html#aac56c1759af66622643bf3b0f870c663)(a, b, AKSIMD\_PERMUTE128(3, 1)) |
|  | Selects the higher of each of the 128b lanes in a and b to be the result ( B A ), ( D C) -> ( D B ) [更多...](_ak_simd_avx2_8h_ade6587a0488db010074b2b67e7bdd9b1.html#ade6587a0488db010074b2b67e7bdd9b1) |
|  | |
| #define | [AKSIMD\_PERMUTE\_4X64\_V8F32](_ak_simd_avx2_8h_a3aebf9527f76618da9dbe397b8602c22.html#a3aebf9527f76618da9dbe397b8602c22)(a, i)   \_mm256\_castpd\_ps(\_mm256\_permute4x64\_pd(\_mm256\_castps\_pd(a), i)) |
|  | |
| AKSIMD conversion | |
| #define | [AKSIMD\_CONVERT\_V8I16\_TO\_V8I32](_ak_simd_avx2_8h_abb80b762d3d967b8312fa2d320ad66e7.html#abb80b762d3d967b8312fa2d320ad66e7)(\_\_vec\_\_)   \_mm256\_cvtepi16\_epi32( (\_\_vec\_\_) ) |
|  | Converts the eight signed 16b integer values of a to signed 32-bit integer values [更多...](_ak_simd_avx2_8h_abb80b762d3d967b8312fa2d320ad66e7.html#abb80b762d3d967b8312fa2d320ad66e7) |
|  | |
| AKSIMD integer arithmetic | |
| #define | [AKSIMD\_ADD\_V8I32](_ak_simd_avx2_8h_a92240b2618adb0466919fd098a94a767.html#a92240b2618adb0466919fd098a94a767)(a, b)   \_mm256\_add\_epi32( a, b ) |
|  | Adds the eight integer values of a and b [更多...](_ak_simd_avx2_8h_a92240b2618adb0466919fd098a94a767.html#a92240b2618adb0466919fd098a94a767) |
|  | |
| #define | [AKSIMD\_CMPLT\_V8I32](_ak_simd_avx2_8h_a0bf3e61f0742d56afb9a0f4f4e9df3ee.html#a0bf3e61f0742d56afb9a0f4f4e9df3ee)(a, b)   \_mm256\_castsi256\_ps(\_mm256\_cmpgt\_epi32( b, a )) |
|  | |
| #define | [AKSIMD\_CMPGT\_V8I32](_ak_simd_avx2_8h_aad1c74aea36a9e45980a4ecae7561870.html#aad1c74aea36a9e45980a4ecae7561870)(a, b)   \_mm256\_castsi256\_ps(\_mm256\_cmpgt\_epi32( a, b )) |
|  | |
| #define | [AKSIMD\_OR\_V8I32](_ak_simd_avx2_8h_a8bc08d6f85af6a1afad74b45e67a71af.html#a8bc08d6f85af6a1afad74b45e67a71af)(a, b)   \_mm256\_or\_si256(a,b) |
|  | |
| #define | [AKSIMD\_XOR\_V8I32](_ak_simd_avx2_8h_a4fe2d9ea21ec3dcc84061ba6a01bee8d.html#a4fe2d9ea21ec3dcc84061ba6a01bee8d)(a, b)   \_mm256\_xor\_si256(a,b) |
|  | |
| #define | [AKSIMD\_SUB\_V8I32](_ak_simd_avx2_8h_a6c65d479f3743e94d47c430c7db18fea.html#a6c65d479f3743e94d47c430c7db18fea)(a, b)   \_mm256\_sub\_epi32(a,b) |
|  | |
| #define | [AKSIMD\_AND\_V8I32](_ak_simd_avx2_8h_a3c94736571c9bd8a1e2075b34253fd7f.html#a3c94736571c9bd8a1e2075b34253fd7f)(\_\_a\_\_, \_\_b\_\_)   \_mm256\_and\_si256( (\_\_a\_\_), (\_\_b\_\_) ) |
|  | |
| #define | [AKSIMD\_MULLO\_V8I32](_ak_simd_avx2_8h_ab44986077237ba7b31fa8725bb1c3ec6.html#ab44986077237ba7b31fa8725bb1c3ec6)(a, b)   \_mm256\_mullo\_epi32(a, b) |
|  | Multiplies each 32-bit int value of a by b and returns the lower 32b of the result (no overflow or clamp) [更多...](_ak_simd_avx2_8h_ab44986077237ba7b31fa8725bb1c3ec6.html#ab44986077237ba7b31fa8725bb1c3ec6) |
|  | |
| #define | [AKSIMD\_MULLO16\_V8I32](_ak_simd_avx2_8h_a97b33598411d17e1f90d369a689c7fef.html#a97b33598411d17e1f90d369a689c7fef)(a, b)   \_mm256\_mullo\_epi16(a, b) |
|  | Multiplies the low 16bits of a by b and stores it in V8I32 (no overflow) [更多...](_ak_simd_avx2_8h_a97b33598411d17e1f90d369a689c7fef.html#a97b33598411d17e1f90d369a689c7fef) |
|  | |
| #define | [AKSIMD\_SUB\_V16I16](_ak_simd_avx2_8h_a62a3a0ecab60ac31d5560dd84e92d2ea.html#a62a3a0ecab60ac31d5560dd84e92d2ea)(a, b)   \_mm256\_sub\_epi16( a, b ) |
|  | Subtracts each 16b integer of a by b [更多...](_ak_simd_avx2_8h_a62a3a0ecab60ac31d5560dd84e92d2ea.html#a62a3a0ecab60ac31d5560dd84e92d2ea) |
|  | |
| #define | [AKSIMD\_CMPGT\_V16I16](_ak_simd_avx2_8h_aa7b54e2d91e04a5bfa01175ea2c74b7b.html#aa7b54e2d91e04a5bfa01175ea2c74b7b)(\_\_a\_\_, \_\_b\_\_)   \_mm256\_cmpgt\_epi16( (\_\_a\_\_), (\_\_b\_\_) ) |
|  | |
| AKSIMD packing / unpacking | |
| #define | [AKSIMD\_UNPACKLO\_VECTOR16I16](_ak_simd_avx2_8h_a671fcffa08ee9bb5e6777bc3450a7925.html#a671fcffa08ee9bb5e6777bc3450a7925)(a, b)   \_mm256\_unpacklo\_epi16( a, b ) |
|  | |
| #define | [AKSIMD\_UNPACKHI\_VECTOR16I16](_ak_simd_avx2_8h_ae8c0dbb254b9fae1544e3eed5d2efef6.html#ae8c0dbb254b9fae1544e3eed5d2efef6)(a, b)   \_mm256\_unpackhi\_epi16( a, b ) |
|  | |
| #define | [AKSIMD\_PACKS\_V8I32](_ak_simd_avx2_8h_ab18e6aa052715512a1250a5a95e844c7.html#ab18e6aa052715512a1250a5a95e844c7)(a, b)   \_mm256\_packs\_epi32( a, b ) |
|  | |
| AKSIMD shifting | |
| #define | [AKSIMD\_SHIFTLEFT\_V8I32](_ak_simd_avx2_8h_aadb70b4f334aacfc72033e728670a250.html#aadb70b4f334aacfc72033e728670a250)(\_\_vec\_\_, \_\_shiftBy\_\_)    \_mm256\_slli\_epi32( (\_\_vec\_\_), (\_\_shiftBy\_\_) ) |
|  | |
| #define | [AKSIMD\_SHIFTLEFT16\_V8I32](_ak_simd_avx2_8h_a30ab216268ccf8afafee6870e7a53b1a.html#a30ab216268ccf8afafee6870e7a53b1a)(\_\_vec\_\_) |
|  | |
| #define | [AKSIMD\_SHIFTRIGHT\_V8I32](_ak_simd_avx2_8h_a94c86c6408230d88e37589f754422d37.html#a94c86c6408230d88e37589f754422d37)(\_\_vec\_\_, \_\_shiftBy\_\_)    \_mm256\_srli\_epi32( (\_\_vec\_\_), (\_\_shiftBy\_\_) ) |
|  | |
| #define | [AKSIMD\_SHIFTRIGHTARITH\_V8I32](_ak_simd_avx2_8h_a34c7e70fbf238437569890b284932366.html#a34c7e70fbf238437569890b284932366)(\_\_vec\_\_, \_\_shiftBy\_\_)    \_mm256\_srai\_epi32( (\_\_vec\_\_), (\_\_shiftBy\_\_) ) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| AKSIMD gather | |
| template<typename T , typename Function > | |
| static AKSIMD\_V8I32 | [AKSIMD\_GATHER\_EPI32](_ak_simd_avx2_8h_a1c9c31bad31ae443fd65d6b5d356773f.html#a1c9c31bad31ae443fd65d6b5d356773f) (const T \*\_\_restrict base\_ptr, Function expr) |
|  | |
| template<typename T , typename Function > | |
| static AKSIMD\_V8I32 | [AKSIMD\_GATHER\_EPI64](_ak_simd_avx2_8h_abb248de5401e00bca25e0f8d06ac7909.html#abb248de5401e00bca25e0f8d06ac7909) (const T \*base\_ptr, Function expr) |
|  | |
| template<typename T , typename Function > | |
| static AKSIMD\_V8F32 | [AKSIMD\_GATHER\_PS](_ak_simd_avx2_8h_af0fdbb1229fea30311d8b1f56c7cd86b.html#af0fdbb1229fea30311d8b1f56c7cd86b) (const T \*base\_ptr, Function expr) |
|  | |
| template<typename T , typename Function > | |
| static AKSIMD\_V4F64 | [AKSIMD\_GATHER\_PD](_ak_simd_avx2_8h_a138cc943b3037818afa5698bd65aaeae.html#a138cc943b3037818afa5698bd65aaeae) (const T \*base\_ptr, Function expr) |
|  | |

|  |  |
| --- | --- |
| AKSIMD arithmetic | |
| #define | [AKSIMD\_MADDSUB\_V8F32](_ak_simd_avx2_8h_a43515f38b353099e5e48bdfb63f19de8.html#a43515f38b353099e5e48bdfb63f19de8)(\_\_a\_\_, \_\_b\_\_, \_\_c\_\_)   \_mm256\_fmaddsub\_ps( (\_\_a\_\_), (\_\_b\_\_), (\_\_c\_\_) ) |
|  | Vector multiply-add-sub operation. [更多...](_ak_simd_avx2_8h_a43515f38b353099e5e48bdfb63f19de8.html#a43515f38b353099e5e48bdfb63f19de8) |
|  | |
| #define | [AKSIMD\_MSUBADD\_V8F32](_ak_simd_avx2_8h_a024a6e8d8e368ef91a5d3daa5d709b2b.html#a024a6e8d8e368ef91a5d3daa5d709b2b)(\_\_a\_\_, \_\_b\_\_, \_\_c\_\_)   \_mm256\_fmsubadd\_ps( (\_\_a\_\_), (\_\_b\_\_), (\_\_c\_\_) ) |
|  | |
| #define | [AKSIMD\_MADD\_V8F32](_ak_simd_avx2_8h_a7cc4c97ff53c67dff1161893ee68a5f4.html#a7cc4c97ff53c67dff1161893ee68a5f4)(\_\_a\_\_, \_\_b\_\_, \_\_c\_\_)   \_mm256\_fmadd\_ps( (\_\_a\_\_), (\_\_b\_\_) , (\_\_c\_\_) ) |
|  | Vector multiply-add operation. [更多...](_ak_simd_avx2_8h_a7cc4c97ff53c67dff1161893ee68a5f4.html#a7cc4c97ff53c67dff1161893ee68a5f4) |
|  | |
| #define | [AKSIMD\_MSUB\_V8F32](_ak_simd_avx2_8h_a65e57a66cc5273fab892414f2d5a9601.html#a65e57a66cc5273fab892414f2d5a9601)(\_\_a\_\_, \_\_b\_\_, \_\_c\_\_)   \_mm256\_fmsub\_ps( (\_\_a\_\_), (\_\_b\_\_) , (\_\_c\_\_) ) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) AKSIMD\_V8F32 | [AKSIMD\_COMPLEXMUL\_AVX2](_ak_simd_avx2_8h_a1bbf9fb463c635c40c5e5d6bfab069bc.html#a1bbf9fb463c635c40c5e5d6bfab069bc) (const AKSIMD\_V8F32 cIn1, const AKSIMD\_V8F32 cIn2) |
|  | |

## 详细描述

AKSIMD - AVX2 implementation

在文件 [AkSimdAvx2.h](_ak_simd_avx2_8h_source.html) 中定义.