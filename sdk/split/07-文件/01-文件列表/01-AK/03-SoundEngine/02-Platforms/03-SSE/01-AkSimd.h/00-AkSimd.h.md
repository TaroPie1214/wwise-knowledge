# AkSimd.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Platforms](dir_9707d8b0bea28caa964fded672ce5309.html)
- [SSE](dir_da34b873a1a3774f4dcbbd9479a5cb37.html)

AkSimd.h 文件参考

`#include <AK/SoundEngine/Common/AkSimdTypes.h>`  
`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <xmmintrin.h>`  
`#include <smmintrin.h>`  
`#include <emmintrin.h>`

[浏览源代码.](_platforms_2_s_s_e_2_ak_simd_8h_source.html)

|  |  |
| --- | --- |
| 宏定义 | |
| Platform specific memory size alignment for allocation purposes | |
| #define | [AKSIMD\_ALIGNSIZE](_platforms_2_s_s_e_2_ak_simd_8h_a3d3b66234162b20984a289b91221edce.html#a3d3b66234162b20984a289b91221edce)(\_\_Size\_\_)   (((\_\_Size\_\_) + 15) & ~15) |
|  | |
| AKSIMD storing | |
| #define | [AKSIMD\_STORE\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a0b847f202de2519c5f11b305bcf6ddbf.html#a0b847f202de2519c5f11b305bcf6ddbf)(\_\_addr\_\_, \_\_vec\_\_)   \_mm\_storeu\_ps( ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)\*)(\_\_addr\_\_), (\_\_vec\_\_) ) |
|  | |
| #define | [AKSIMD\_STOREU\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a7385d0ac1aaac1a0f36ad2824fcafced.html#a7385d0ac1aaac1a0f36ad2824fcafced)(\_\_addr\_\_, \_\_vec\_\_)   \_mm\_storeu\_ps( ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)\*)(\_\_addr\_\_), (\_\_vec\_\_) ) |
|  | |
| #define | [AKSIMD\_STORE1\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_afe50fedb76aae89ee30100936c370190.html#afe50fedb76aae89ee30100936c370190)(\_\_addr\_\_, \_\_vec\_\_)   \_mm\_store\_ss( ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)\*)(\_\_addr\_\_), (\_\_vec\_\_) ) |
|  | |
| #define | [AKSIMD\_STORE1\_V2F64](_platforms_2_s_s_e_2_ak_simd_8h_a6e606216a5918612ae1013234dfc80a3.html#a6e606216a5918612ae1013234dfc80a3)(\_\_addr\_\_, \_\_vec\_\_)   \_mm\_store\_sd( ([AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e)\*)(\_\_addr\_\_), \_mm\_castps\_pd(\_\_vec\_\_) ) |
|  | |
| AKSIMD shuffling | |
| #define | [AKSIMD\_SHUFFLE](_platforms_2_s_s_e_2_ak_simd_8h_abad6d59ebb4b74aa95322a6293db519f.html#abad6d59ebb4b74aa95322a6293db519f)(fp3, fp2, fp1, fp0)   \_MM\_SHUFFLE( (fp3), (fp2), (fp1), (fp0) ) |
|  | |
| #define | [AKSIMD\_SHUFFLE\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a54594e2872b2c35c6310d02e554e17d1.html#a54594e2872b2c35c6310d02e554e17d1)(a, b, i)   \_mm\_shuffle\_ps( a, b, i ) |
|  | |
| #define | [AKSIMD\_SHUFFLE\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_aa301b336562543f29e156984bf6cc25c.html#aa301b336562543f29e156984bf6cc25c)(a, b, i)   \_mm\_castps\_si128(\_mm\_shuffle\_ps( \_mm\_castsi128\_ps(a), \_mm\_castsi128\_ps(b), i )) |
|  | |
| #define | [AKSIMD\_MOVEHL\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_ae390732f9187c4c5e0ef6625bef0149c.html#ae390732f9187c4c5e0ef6625bef0149c)(a, b)   \_mm\_movehl\_ps( a, b ) |
|  | |
| #define | [AKSIMD\_MOVELH\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_abdb3636c28f7b86dbbf9ccd83dd5f72c.html#abdb3636c28f7b86dbbf9ccd83dd5f72c)(a, b)   \_mm\_movelh\_ps( a, b ) |
|  | |
| #define | [AKSIMD\_SHUFFLE\_BADC](_platforms_2_s_s_e_2_ak_simd_8h_a3fb7b565678447c7c4cb10c1acb24639.html#a3fb7b565678447c7c4cb10c1acb24639)(\_\_a\_\_)   \_mm\_shuffle\_ps( (\_\_a\_\_), (\_\_a\_\_), \_MM\_SHUFFLE(2,3,0,1)) |
|  | Swap the 2 lower floats together and the 2 higher floats together.   [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a3fb7b565678447c7c4cb10c1acb24639.html#a3fb7b565678447c7c4cb10c1acb24639) |
|  | |
| #define | [AKSIMD\_SHUFFLE\_CDAB](_platforms_2_s_s_e_2_ak_simd_8h_a1f88f3d1e6d8249631d4a6e6ba15fae7.html#a1f88f3d1e6d8249631d4a6e6ba15fae7)(\_\_a\_\_)   \_mm\_shuffle\_ps( (\_\_a\_\_), (\_\_a\_\_), \_MM\_SHUFFLE(1,0,3,2)) |
|  | Swap the 2 lower floats with the 2 higher floats.   [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a1f88f3d1e6d8249631d4a6e6ba15fae7.html#a1f88f3d1e6d8249631d4a6e6ba15fae7) |
|  | |
| #define | [AKSIMD\_SHUFFLE\_BCDA](_platforms_2_s_s_e_2_ak_simd_8h_ac7af866f529cbb1653901a4448f37b95.html#ac7af866f529cbb1653901a4448f37b95)(\_\_a\_\_)   [AKSIMD\_SHUFFLE\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a54594e2872b2c35c6310d02e554e17d1.html#a54594e2872b2c35c6310d02e554e17d1)( (\_\_a\_\_), (\_\_a\_\_), \_MM\_SHUFFLE(0,3,2,1)) |
|  | Barrel-shift all floats by one. [更多...](_platforms_2_s_s_e_2_ak_simd_8h_ac7af866f529cbb1653901a4448f37b95.html#ac7af866f529cbb1653901a4448f37b95) |
|  | |
| #define | [AKSIMD\_DUP\_ODD](_platforms_2_s_s_e_2_ak_simd_8h_afcdf0cc52223e0d8d9026c22c8e3d54b.html#afcdf0cc52223e0d8d9026c22c8e3d54b)(\_\_vv)   [AKSIMD\_SHUFFLE\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a54594e2872b2c35c6310d02e554e17d1.html#a54594e2872b2c35c6310d02e554e17d1)(\_\_vv, \_\_vv, [AKSIMD\_SHUFFLE](_platforms_2_s_s_e_2_ak_simd_8h_abad6d59ebb4b74aa95322a6293db519f.html#abad6d59ebb4b74aa95322a6293db519f)(3,3,1,1)) |
|  | Duplicates the odd items into the even items (d c b a -> d d b b ) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_afcdf0cc52223e0d8d9026c22c8e3d54b.html#afcdf0cc52223e0d8d9026c22c8e3d54b) |
|  | |
| #define | [AKSIMD\_DUP\_EVEN](_platforms_2_s_s_e_2_ak_simd_8h_a38e9e11f3fc37f04ba4afe8ad79c7e0d.html#a38e9e11f3fc37f04ba4afe8ad79c7e0d)(\_\_vv)   [AKSIMD\_SHUFFLE\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a54594e2872b2c35c6310d02e554e17d1.html#a54594e2872b2c35c6310d02e554e17d1)(\_\_vv, \_\_vv, [AKSIMD\_SHUFFLE](_platforms_2_s_s_e_2_ak_simd_8h_abad6d59ebb4b74aa95322a6293db519f.html#abad6d59ebb4b74aa95322a6293db519f)(2,2,0,0)) |
|  | Duplicates the even items into the odd items (d c b a -> c c a a ) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a38e9e11f3fc37f04ba4afe8ad79c7e0d.html#a38e9e11f3fc37f04ba4afe8ad79c7e0d) |
|  | |
| AKSIMD cast | |
| #define | [AKSIMD\_CAST\_V2F64\_TO\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a5995c4f077bd1b3ac8da0f5957e2eb79.html#a5995c4f077bd1b3ac8da0f5957e2eb79)(\_\_vec\_\_)   \_mm\_castpd\_ps(\_\_vec\_\_) |
|  | |
| #define | [AKSIMD\_CAST\_V2F64\_TO\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a8d07d2801aa83b61501285ba301fe30e.html#a8d07d2801aa83b61501285ba301fe30e)(\_\_vec\_\_)   \_mm\_castpd\_si128(\_\_vec\_\_) |
|  | |
| #define | [AKSIMD\_CAST\_V4F32\_TO\_V2F64](_platforms_2_s_s_e_2_ak_simd_8h_a89e43df2cb020b1050f2e56815a07a2d.html#a89e43df2cb020b1050f2e56815a07a2d)(\_\_vec\_\_)   \_mm\_castps\_pd(\_\_vec\_\_) |
|  | |
| #define | [AKSIMD\_CAST\_V4F32\_TO\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a9c0fe7b5707191ad39fb7442b4d1a806.html#a9c0fe7b5707191ad39fb7442b4d1a806)(\_\_vec\_\_)   \_mm\_castps\_si128(\_\_vec\_\_) |
|  | |
| #define | [AKSIMD\_CAST\_V4I32\_TO\_V2F64](_platforms_2_s_s_e_2_ak_simd_8h_a2d1c9668d1aa444057606f71a5462243.html#a2d1c9668d1aa444057606f71a5462243)(\_\_vec\_\_)   \_mm\_castsi128\_pd(\_\_vec\_\_) |
|  | |
| #define | [AKSIMD\_CAST\_V4I32\_TO\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_acaf082ecb6defbf62043b74972ba5efc.html#acaf082ecb6defbf62043b74972ba5efc)(\_\_vec\_\_)   \_mm\_castsi128\_ps(\_\_vec\_\_) |
|  | |
| #define | [AKSIMD\_CAST\_V4COND\_TO\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_ae199ce79d53dadef32fafc1b38d1d358.html#ae199ce79d53dadef32fafc1b38d1d358)(\_\_vec\_\_)   (\_\_vec\_\_) |
|  | Cast vector of type AKSIMD\_V4COND to AKSIMD\_V4F32. [更多...](_platforms_2_s_s_e_2_ak_simd_8h_ae199ce79d53dadef32fafc1b38d1d358.html#ae199ce79d53dadef32fafc1b38d1d358) |
|  | |
| #define | [AKSIMD\_CAST\_V4F32\_TO\_V4COND](_platforms_2_s_s_e_2_ak_simd_8h_a0601230d41eb107ee09a9a24a5441115.html#a0601230d41eb107ee09a9a24a5441115)(\_\_vec\_\_)   (\_\_vec\_\_) |
|  | Cast vector of type AKSIMD\_V4F32 to AKSIMD\_V4COND. [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a0601230d41eb107ee09a9a24a5441115.html#a0601230d41eb107ee09a9a24a5441115) |
|  | |
| #define | [AKSIMD\_CAST\_V4COND\_TO\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a8b7d2aae8a4f20475d9cdfe76c1237ba.html#a8b7d2aae8a4f20475d9cdfe76c1237ba)(\_\_vec\_\_)   \_mm\_castps\_si128(\_\_vec\_\_) |
|  | Cast vector of type AKSIMD\_V4COND to AKSIMD\_V4I32. [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a8b7d2aae8a4f20475d9cdfe76c1237ba.html#a8b7d2aae8a4f20475d9cdfe76c1237ba) |
|  | |
| #define | [AKSIMD\_CAST\_V4I32\_TO\_V4COND](_platforms_2_s_s_e_2_ak_simd_8h_a788601f9e55d28c483a0bca73c88eea0.html#a788601f9e55d28c483a0bca73c88eea0)(\_\_vec\_\_)   \_mm\_castsi128\_ps(\_\_vec\_\_) |
|  | Cast vector of type AKSIMD\_V4I32 to AKSIMD\_V4COND. [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a788601f9e55d28c483a0bca73c88eea0.html#a788601f9e55d28c483a0bca73c88eea0) |
|  | |
| #define | [AKSIMD\_UNPACKLO\_VECTOR8I16](_platforms_2_s_s_e_2_ak_simd_8h_a24bda4bb8b1087307c5def6d53dfba33.html#a24bda4bb8b1087307c5def6d53dfba33)(a, b)   \_mm\_unpacklo\_epi16( a, b ) |
|  | |
| #define | [AKSIMD\_UNPACKHI\_VECTOR8I16](_platforms_2_s_s_e_2_ak_simd_8h_a31ee32f119f00336c0a31a34d74bc156.html#a31ee32f119f00336c0a31a34d74bc156)(a, b)   \_mm\_unpackhi\_epi16( a, b ) |
|  | |
| #define | [AKSIMD\_PACKS\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_adef16f41caa2c2cb55221a4bd873e3e1.html#adef16f41caa2c2cb55221a4bd873e3e1)(a, b)   \_mm\_packs\_epi32( a, b ) |
|  | |
| AKSIMD shifting | |
| #define | [AKSIMD\_SHIFTLEFT\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a8e838aafab18bfd8c850dfcc94b6ffbe.html#a8e838aafab18bfd8c850dfcc94b6ffbe)(\_\_vec\_\_, \_\_shiftBy\_\_)    \_mm\_slli\_epi32( (\_\_vec\_\_), (\_\_shiftBy\_\_) ) |
|  | |
| #define | [AKSIMD\_SHIFTRIGHT\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a7474e815f712eb877ee8da017f08fc0c.html#a7474e815f712eb877ee8da017f08fc0c)(\_\_vec\_\_, \_\_shiftBy\_\_)    \_mm\_srli\_epi32( (\_\_vec\_\_), (\_\_shiftBy\_\_) ) |
|  | |
| #define | [AKSIMD\_SHIFTRIGHTARITH\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_aa63c4a5285da3a8d172712987a7c11cc.html#aa63c4a5285da3a8d172712987a7c11cc)(\_\_vec\_\_, \_\_shiftBy\_\_)    \_mm\_srai\_epi32( (\_\_vec\_\_), (\_\_shiftBy\_\_) ) |
|  | |
| AKSIMD int16 helpers | |
| MMX | |
| #define | [AKSIMD\_LOAD\_V1I64\_LO](_platforms_2_s_s_e_2_ak_simd_8h_abbaf4b66f6ab214539111ed574925971.html#abbaf4b66f6ab214539111ed574925971)(\_\_addr\_\_)   \_mm\_loadl\_epi64(reinterpret\_cast<const \_\_m128i\*>(\_\_addr\_\_) ) |
|  | |

|  |  |
| --- | --- |
| AKSIMD loading / setting | |
| #define | [AKSIMD\_LOAD\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a15791b88970a4bf153baf3b2c5fdd7b3.html#a15791b88970a4bf153baf3b2c5fdd7b3)(\_\_addr\_\_)   \_mm\_loadu\_ps( ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)\*)(\_\_addr\_\_) ) |
|  | |
| #define | [AKSIMD\_LOADU\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_af609d443f16c557cc13ea2cc00b0663a.html#af609d443f16c557cc13ea2cc00b0663a)(\_\_addr\_\_)   \_mm\_loadu\_ps( (\_\_addr\_\_) ) |
|  | |
| #define | [AKSIMD\_LOAD1\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_af1cf5c9175a7cf2c20c32bfa3d212836.html#af1cf5c9175a7cf2c20c32bfa3d212836)(\_\_scalar\_\_)   \_mm\_load1\_ps( &(\_\_scalar\_\_) ) |
|  | |
| #define | [AKSIMD\_SET\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a321563e473cb073ca39c3c143965b1cc.html#a321563e473cb073ca39c3c143965b1cc)(\_\_scalar\_\_)   \_mm\_set\_ps1( (\_\_scalar\_\_) ) |
|  | |
| #define | [AKSIMD\_SETV\_V2F64](_platforms_2_s_s_e_2_ak_simd_8h_a545722951b9690e635b494a45b600122.html#a545722951b9690e635b494a45b600122)(\_b, \_a)   \_mm\_castpd\_ps(\_mm\_set\_pd( (\_b), (\_a) )) |
|  | Sets the two double-precision, floating-point values to in\_value [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a545722951b9690e635b494a45b600122.html#a545722951b9690e635b494a45b600122) |
|  | |
| #define | [AKSIMD\_SETV\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_ac4be9261ee652f07daf5e606ef701483.html#ac4be9261ee652f07daf5e606ef701483)(\_d, \_c, \_b, \_a)   \_mm\_set\_ps( (\_d), (\_c), (\_b), (\_a) ) |
|  | Populates the full vector with the 4 floating point elements provided [更多...](_platforms_2_s_s_e_2_ak_simd_8h_ac4be9261ee652f07daf5e606ef701483.html#ac4be9261ee652f07daf5e606ef701483) |
|  | |
| #define | [AKSIMD\_SETZERO\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_ae56ea5d25418beca1989831da9b7724b.html#ae56ea5d25418beca1989831da9b7724b)()   \_mm\_setzero\_ps() |
|  | |
| #define | [AKSIMD\_LOAD\_SS\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a8df8244f56591b01a0ac346c9df50785.html#a8df8244f56591b01a0ac346c9df50785)(\_\_addr\_\_)   \_mm\_load\_ss( (\_\_addr\_\_) ) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4COND](_platforms_2arm__neon_2_ak_simd_types_8h_afb7c86c28c820a1b36aa724954a752e9.html#afb7c86c28c820a1b36aa724954a752e9) | [AKSIMD\_SETMASK\_V4COND](_platforms_2_s_s_e_2_ak_simd_8h_af8ae284379e6bd9bf65f013956061b3c.html#af8ae284379e6bd9bf65f013956061b3c) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) x) |
|  | Populates the full vector with the mask[3:0], setting each to 0 or ~0 [更多...](_platforms_2_s_s_e_2_ak_simd_8h_af8ae284379e6bd9bf65f013956061b3c.html#af8ae284379e6bd9bf65f013956061b3c) |
|  | |

|  |  |
| --- | --- |
| AKSIMD arithmetic | |
| #define | [AKSIMD\_SUB\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_ad82fbc3549ab87fa77ef1295cfd8be83.html#ad82fbc3549ab87fa77ef1295cfd8be83)(a, b)   \_mm\_sub\_ps( a, b ) |
|  | |
| #define | [AKSIMD\_SUB\_SS\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_afe1d910f6386bbc88df1bfc899f36709.html#afe1d910f6386bbc88df1bfc899f36709)(a, b)   \_mm\_sub\_ss( a, b ) |
|  | |
| #define | [AKSIMD\_ADD\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a527b28a6e1b646e129026d5763872d1b.html#a527b28a6e1b646e129026d5763872d1b)(a, b)   \_mm\_add\_ps( a, b ) |
|  | |
| #define | [AKSIMD\_ADD\_SS\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a622b2910d28297d81d29fcddffb15312.html#a622b2910d28297d81d29fcddffb15312)(a, b)   \_mm\_add\_ss( a, b ) |
|  | |
| #define | [AKSIMD\_MUL\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_acd959b99b43089497cf0877ca5f19074.html#acd959b99b43089497cf0877ca5f19074)(a, b)   \_mm\_mul\_ps( a, b ) |
|  | |
| #define | [AKSIMD\_DIV\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a30bdf74bc313a5a0e2c3cfc35e8018c0.html#a30bdf74bc313a5a0e2c3cfc35e8018c0)(a, b)   \_mm\_div\_ps( a, b ) |
|  | |
| #define | [AKSIMD\_MUL\_SS\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a06b664123be406d9e9909324dfd4e53a.html#a06b664123be406d9e9909324dfd4e53a)(a, b)   \_mm\_mul\_ss( a, b ) |
|  | |
| #define | [AKSIMD\_MADD\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_abd7a28ad54ad320d0ec3aa1121790672.html#abd7a28ad54ad320d0ec3aa1121790672)(\_\_a\_\_, \_\_b\_\_, \_\_c\_\_)   \_mm\_add\_ps( \_mm\_mul\_ps( (\_\_a\_\_), (\_\_b\_\_) ), (\_\_c\_\_) ) |
|  | Vector multiply-add operation. (if we're targeting a platform or arch with FMA, (AVX2 implies FMA) using the fma intrinsics directly tends to be slightly more desirable) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_abd7a28ad54ad320d0ec3aa1121790672.html#abd7a28ad54ad320d0ec3aa1121790672) |
|  | |
| #define | [AKSIMD\_MSUB\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a84eaef96e7f29f69d919e4fed7f70ea6.html#a84eaef96e7f29f69d919e4fed7f70ea6)(\_\_a\_\_, \_\_b\_\_, \_\_c\_\_)   \_mm\_sub\_ps( \_mm\_mul\_ps( (\_\_a\_\_), (\_\_b\_\_) ), (\_\_c\_\_) ) |
|  | |
| #define | [AKSIMD\_LERP\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a75759baf4f8ddb8a4aa459fa6669986b.html#a75759baf4f8ddb8a4aa459fa6669986b)(\_alpha\_, \_\_a\_\_, \_\_b\_\_)   [AKSIMD\_MADD\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_abd7a28ad54ad320d0ec3aa1121790672.html#abd7a28ad54ad320d0ec3aa1121790672)(\_alpha\_, [AKSIMD\_SUB\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_ad82fbc3549ab87fa77ef1295cfd8be83.html#ad82fbc3549ab87fa77ef1295cfd8be83)(\_\_b\_\_, \_\_a\_\_), \_\_a\_\_) |
|  | |
| #define | [AKSIMD\_MADD\_SS\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_ac9c2e15c0528da93d259da7efdbc65e2.html#ac9c2e15c0528da93d259da7efdbc65e2)(\_\_a\_\_, \_\_b\_\_, \_\_c\_\_)   \_mm\_add\_ss( \_mm\_mul\_ss( (\_\_a\_\_), (\_\_b\_\_) ), (\_\_c\_\_) ) |
|  | Vector multiply-add operation. [更多...](_platforms_2_s_s_e_2_ak_simd_8h_ac9c2e15c0528da93d259da7efdbc65e2.html#ac9c2e15c0528da93d259da7efdbc65e2) |
|  | |
| #define | [AKSIMD\_MIN\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a864da7b025a78e9c7db212f397297517.html#a864da7b025a78e9c7db212f397297517)(a, b)   \_mm\_min\_ps( a, b ) |
|  | |
| #define | [AKSIMD\_MAX\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a3bb08ebaa3421ce57f2924a6c1bb438f.html#a3bb08ebaa3421ce57f2924a6c1bb438f)(a, b)   \_mm\_max\_ps( a, b ) |
|  | |
| #define | [AKSIMD\_ABS\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a6734058e458ce2f8fd7f765f971c0189.html#a6734058e458ce2f8fd7f765f971c0189)(a)   \_mm\_andnot\_ps(\_mm\_set1\_ps(-0.f), a) |
|  | Computes the absolute value [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a6734058e458ce2f8fd7f765f971c0189.html#a6734058e458ce2f8fd7f765f971c0189) |
|  | |
| #define | [AKSIMD\_NEG\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a14cd1f0d9deb47dba75ac4120e02bdf3.html#a14cd1f0d9deb47dba75ac4120e02bdf3)(\_\_a\_\_)   \_mm\_xor\_ps(\_mm\_set1\_ps(-0.f), \_\_a\_\_) |
|  | Changes the sign [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a14cd1f0d9deb47dba75ac4120e02bdf3.html#a14cd1f0d9deb47dba75ac4120e02bdf3) |
|  | |
| #define | [AKSIMD\_SQRT\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_ab3aeab164261e12fb00213875171effe.html#ab3aeab164261e12fb00213875171effe)(\_\_a\_\_)   \_mm\_sqrt\_ps( (\_\_a\_\_) ) |
|  | Vector square root aproximation (see \_mm\_sqrt\_ps) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_ab3aeab164261e12fb00213875171effe.html#ab3aeab164261e12fb00213875171effe) |
|  | |
| #define | [AKSIMD\_RSQRT\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a5d3cf1a02764e30ac17f53462db6c763.html#a5d3cf1a02764e30ac17f53462db6c763)(\_\_a\_\_)   \_mm\_rsqrt\_ps( (\_\_a\_\_) ) |
|  | Vector reciprocal square root approximation 1/sqrt(a), or equivalently, sqrt(1/a) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a5d3cf1a02764e30ac17f53462db6c763.html#a5d3cf1a02764e30ac17f53462db6c763) |
|  | |
| #define | [AKSIMD\_RECIP\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a0eae5f7b023e0d627b036f7ac0690541.html#a0eae5f7b023e0d627b036f7ac0690541)(\_\_a\_\_)   \_mm\_rcp\_ps(\_\_a\_\_) |
|  | Reciprocal of x (1/x) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a0eae5f7b023e0d627b036f7ac0690541.html#a0eae5f7b023e0d627b036f7ac0690541) |
|  | |
| #define | [AKSIMD\_XOR\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a5c04678e13876be6a8235f24ba6cffc2.html#a5c04678e13876be6a8235f24ba6cffc2)(a, b)   \_mm\_xor\_ps(a,b) |
|  | Binary xor for single-precision floating-point [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a5c04678e13876be6a8235f24ba6cffc2.html#a5c04678e13876be6a8235f24ba6cffc2) |
|  | |
| #define | [AKSIMD\_ADDSUB\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a43a48362c882f6fae179085d892ab984.html#a43a48362c882f6fae179085d892ab984)(a, b)   \_mm\_add\_ps( a, \_mm\_xor\_ps(b, [AKSIMD\_SETV\_V4F32](_platforms_2arm__neon_2_ak_simd_8h_ad7eb8b78e41f7f74240b857eb7bfa668.html#ad7eb8b78e41f7f74240b857eb7bfa668)(0.f, -0.f, 0.f, -0.f))) |
|  | |
| #define | [AKSIMD\_ASSERTFLUSHZEROMODE](_platforms_2_s_s_e_2_ak_simd_8h_aa5a19842f108ebcee2816c1570db01aa.html#aa5a19842f108ebcee2816c1570db01aa)   [AKASSERT](_ak_assert_8h_ac0e6cc4061c0a7c154a8c921a0af74cb.html#ac0e6cc4061c0a7c154a8c921a0af74cb)( \_MM\_GET\_FLUSH\_ZERO\_MODE() == \_MM\_FLUSH\_ZERO\_ON ) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [AKSIMD\_CEIL\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_add2da5c893111a2bacfe30051e27f18c.html#add2da5c893111a2bacfe30051e27f18c) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &x) |
|  | Rounds to upper value [更多...](_platforms_2_s_s_e_2_ak_simd_8h_add2da5c893111a2bacfe30051e27f18c.html#add2da5c893111a2bacfe30051e27f18c) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [AKSIMD\_HORIZONTALADD\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a9db1c0c1c362ae2bcfc695b87000e0b2.html#a9db1c0c1c362ae2bcfc695b87000e0b2) ([AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) vVec) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [AKSIMD\_DOTPRODUCT](_platforms_2_s_s_e_2_ak_simd_8h_a2c33f8540050a63130f154b49424341c.html#a2c33f8540050a63130f154b49424341c) ([AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &vVec, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &vfSigns) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [AKSIMD\_COMPLEXMUL\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a0f6fb310109170c03dec7f5dcaa36b2f.html#a0f6fb310109170c03dec7f5dcaa36b2f) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) vCIn1, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) vCIn2) |
|  | Cross-platform SIMD multiplication of 2 complex data elements with interleaved real and imaginary parts [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a0f6fb310109170c03dec7f5dcaa36b2f.html#a0f6fb310109170c03dec7f5dcaa36b2f) |
|  | |

|  |  |
| --- | --- |
| AKSIMD integer arithmetic | |
| #define | [AKSIMD\_ADD\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_abf03d2dfcf91801a0631143b71528742.html#abf03d2dfcf91801a0631143b71528742)(a, b)   \_mm\_add\_epi32( a, b ) |
|  | Adds the four integer values of a and b [更多...](_platforms_2_s_s_e_2_ak_simd_8h_abf03d2dfcf91801a0631143b71528742.html#abf03d2dfcf91801a0631143b71528742) |
|  | |
| #define | [AKSIMD\_CMPLT\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a6e70248280a0ffe4c106042e0b04b3aa.html#a6e70248280a0ffe4c106042e0b04b3aa)(a, b)   \_mm\_cmplt\_epi32(a,b) |
|  | |
| #define | [AKSIMD\_CMPGT\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a60c9536a78fef54ca58a12c8871ee31f.html#a60c9536a78fef54ca58a12c8871ee31f)(a, b)   \_mm\_cmpgt\_epi32(a,b) |
|  | |
| #define | [AKSIMD\_OR\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_abf37aaa27525f48d5a87fec58a8491a0.html#abf37aaa27525f48d5a87fec58a8491a0)(a, b)   \_mm\_or\_si128(a,b) |
|  | |
| #define | [AKSIMD\_XOR\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_ad9aacbff9d13a85e4ec321f4bf7dffdb.html#ad9aacbff9d13a85e4ec321f4bf7dffdb)(a, b)   \_mm\_xor\_si128(a,b) |
|  | |
| #define | [AKSIMD\_SUB\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a4ce64a7e62d4418301375810056477d1.html#a4ce64a7e62d4418301375810056477d1)(a, b)   \_mm\_sub\_epi32(a,b) |
|  | |
| #define | [AKSIMD\_NOT\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_ae56a981a8c10dd0316f167c731c5b404.html#ae56a981a8c10dd0316f167c731c5b404)(a)   \_mm\_xor\_si128(a,\_mm\_set1\_epi32(~0)) |
|  | |
| #define | [AKSIMD\_OR\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a8f194efb150fa1285368e3e131c68355.html#a8f194efb150fa1285368e3e131c68355)(a, b)   \_mm\_or\_ps(a,b) |
|  | |
| #define | [AKSIMD\_AND\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a02774e3d2baaa62bd6cf56efcdcc9d21.html#a02774e3d2baaa62bd6cf56efcdcc9d21)(a, b)   \_mm\_and\_ps(a,b) |
|  | |
| #define | [AKSIMD\_ANDNOT\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a6450599699dd60f15d0651fa6c641117.html#a6450599699dd60f15d0651fa6c641117)(a, b)   \_mm\_andnot\_ps(a,b) |
|  | |
| #define | [AKSIMD\_NOT\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_aa42871c340b45a8c0b4cf9a1fe447e22.html#aa42871c340b45a8c0b4cf9a1fe447e22)(a)   \_mm\_xor\_ps(a,\_mm\_castsi128\_ps(\_mm\_set1\_epi32(~0))) |
|  | |
| #define | [AKSIMD\_OR\_V4COND](_platforms_2_s_s_e_2_ak_simd_8h_a67003cf4a5afcb5e5daf3d6ac7528f31.html#a67003cf4a5afcb5e5daf3d6ac7528f31)(a, b)   \_mm\_or\_ps(a,b) |
|  | |
| #define | [AKSIMD\_AND\_V4COND](_platforms_2_s_s_e_2_ak_simd_8h_a8a9eb92448a2cffff03c078ba4eee8c2.html#a8a9eb92448a2cffff03c078ba4eee8c2)(a, b)   \_mm\_and\_ps(a,b) |
|  | |
| #define | [AKSIMD\_MULLO16\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a39bae0227ffdfc5419d07e7872f32250.html#a39bae0227ffdfc5419d07e7872f32250)(a, b)   \_mm\_mullo\_epi16(a, b) |
|  | Multiplies the low 16bits of a by b and stores it in V4I32 (no overflow) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a39bae0227ffdfc5419d07e7872f32250.html#a39bae0227ffdfc5419d07e7872f32250) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4I32](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) | [AKSIMD\_MULLO\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a0b75cf9ea098118dfda27d3f9bfa296b.html#a0b75cf9ea098118dfda27d3f9bfa296b) (const [AKSIMD\_V4I32](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) vIn1, const [AKSIMD\_V4I32](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) vIn2) |
|  | Multiplies the low 32bits of a by b and stores it in V4I32 (no overflow) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a0b75cf9ea098118dfda27d3f9bfa296b.html#a0b75cf9ea098118dfda27d3f9bfa296b) |
|  | |

|  |  |
| --- | --- |
| AKSIMD packing / unpacking | |
| #define | [AKSIMD\_UNPACKLO\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a981599570c2ae7a07beb166f0b8fbb5e.html#a981599570c2ae7a07beb166f0b8fbb5e)(a, b)   \_mm\_unpacklo\_ps( a, b ) |
|  | |
| #define | [AKSIMD\_UNPACKHI\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a306117fec82403ae81e2fe210721891c.html#a306117fec82403ae81e2fe210721891c)(a, b)   \_mm\_unpackhi\_ps( a, b ) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4I32X2](struct_a_k_s_i_m_d___v4_i32_x2.html) | [AKSIMD\_GATHER\_V4I32\_AND\_DEINTERLEAVE\_V4I32X2](_platforms_2_s_s_e_2_ak_simd_8h_a23d311b32983b852bc1858c760f58a61.html#a23d311b32983b852bc1858c760f58a61) ([AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) \*addr3, [AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) \*addr2, [AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) \*addr1, [AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) \*addr0) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4I32X4](struct_a_k_s_i_m_d___v4_i32_x4.html) | [AKSIMD\_GATHER\_V4I64\_AND\_DEINTERLEAVE\_V4I32X4](_platforms_2_s_s_e_2_ak_simd_8h_a8b94f378710ef5d79bea5613f1301737.html#a8b94f378710ef5d79bea5613f1301737) ([AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) \*addr3, [AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) \*addr2, [AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) \*addr1, [AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) \*addr0) |
|  | |

|  |  |
| --- | --- |
| AKSIMD vector comparison | |
| Apart from AKSIMD\_SEL\_GTEQ\_V4F32, these implementations are limited to a few platforms. | |
| #define | [AKSIMD\_CMP\_CTRLMASK](_platforms_2_s_s_e_2_ak_simd_8h_af991297bb81fc2948a67523422ab36db.html#af991297bb81fc2948a67523422ab36db)   \_\_m128 |
|  | |
| #define | [AKSIMD\_LTEQ\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_ab6542c96e1f13c5967704e508d25d9a5.html#ab6542c96e1f13c5967704e508d25d9a5)(\_\_a\_\_, \_\_b\_\_)   \_mm\_cmple\_ps( (\_\_a\_\_), (\_\_b\_\_) ) |
|  | Vector "<=" operation (see \_mm\_cmple\_ps) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_ab6542c96e1f13c5967704e508d25d9a5.html#ab6542c96e1f13c5967704e508d25d9a5) |
|  | |
| #define | [AKSIMD\_LT\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a36a26447b1a750a054054a7b6b41c1cf.html#a36a26447b1a750a054054a7b6b41c1cf)(\_\_a\_\_, \_\_b\_\_)   \_mm\_cmplt\_ps( (\_\_a\_\_), (\_\_b\_\_) ) |
|  | |
| #define | [AKSIMD\_GTEQ\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a62fdb36cb1e0892ce8aab44e1a1657ca.html#a62fdb36cb1e0892ce8aab44e1a1657ca)(\_\_a\_\_, \_\_b\_\_)   \_mm\_cmpge\_ps( (\_\_a\_\_), (\_\_b\_\_) ) |
|  | Vector ">=" operation (see \_mm\_cmple\_ps) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a62fdb36cb1e0892ce8aab44e1a1657ca.html#a62fdb36cb1e0892ce8aab44e1a1657ca) |
|  | |
| #define | [AKSIMD\_GT\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a58436c52736456e25c2f043c18d47c16.html#a58436c52736456e25c2f043c18d47c16)(\_\_a\_\_, \_\_b\_\_)   \_mm\_cmpgt\_ps( (\_\_a\_\_), (\_\_b\_\_) ) |
|  | |
| #define | [AKSIMD\_EQ\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a813380e9264d14960b42dee4354842e3.html#a813380e9264d14960b42dee4354842e3)(\_\_a\_\_, \_\_b\_\_)   \_mm\_cmpeq\_ps( (\_\_a\_\_), (\_\_b\_\_) ) |
|  | Vector "==" operation (see \_mm\_cmpeq\_ps) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a813380e9264d14960b42dee4354842e3.html#a813380e9264d14960b42dee4354842e3) |
|  | |
| #define | [AKSIMD\_EQ\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a3b224f702193db4b3b6c681ea5d981af.html#a3b224f702193db4b3b6c681ea5d981af)(\_\_a\_\_, \_\_b\_\_)   \_mm\_castsi128\_ps(\_mm\_cmpeq\_epi32( (\_\_a\_\_), (\_\_b\_\_) )) |
|  | |
| #define | [AKSIMD\_SEL\_GTEQ\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a095fb6c57646250efd8398aae62b6c92.html#a095fb6c57646250efd8398aae62b6c92)(\_\_a\_\_, \_\_b\_\_, \_\_cond1\_\_, \_\_cond2\_\_)   [AKSIMD\_VSEL\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a6fd3d8186775e03d62e5bc3ac157a9c3.html#a6fd3d8186775e03d62e5bc3ac157a9c3)( \_\_a\_\_, \_\_b\_\_, [AKSIMD\_GTEQ\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a62fdb36cb1e0892ce8aab44e1a1657ca.html#a62fdb36cb1e0892ce8aab44e1a1657ca)( \_\_cond1\_\_, \_\_cond2\_\_ ) ) |
|  | |
| #define | [AKSIMD\_SEL\_GTEZ\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a4a61cf345043716cd1da66e1ffc51162.html#a4a61cf345043716cd1da66e1ffc51162)(\_\_a\_\_, \_\_b\_\_, \_\_c\_\_)   [AKSIMD\_VSEL\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a6fd3d8186775e03d62e5bc3ac157a9c3.html#a6fd3d8186775e03d62e5bc3ac157a9c3)( (\_\_c\_\_), (\_\_b\_\_), [AKSIMD\_GTEQ\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a62fdb36cb1e0892ce8aab44e1a1657ca.html#a62fdb36cb1e0892ce8aab44e1a1657ca)( \_\_a\_\_, \_mm\_set1\_ps(0) ) ) |
|  | |
| #define | [AKSIMD\_SPLAT\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a9e79a040271121ad7c1faa6ceda39779.html#a9e79a040271121ad7c1faa6ceda39779)(var, idx)   [AKSIMD\_SHUFFLE\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a54594e2872b2c35c6310d02e554e17d1.html#a54594e2872b2c35c6310d02e554e17d1)(var,var, [AKSIMD\_SHUFFLE](_platforms_2_s_s_e_2_ak_simd_8h_abad6d59ebb4b74aa95322a6293db519f.html#abad6d59ebb4b74aa95322a6293db519f)(idx,idx,idx,idx)) |
|  | |
| #define | [AKSIMD\_MASK\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_af1b379f1920d2263f8bf802a6ee80506.html#af1b379f1920d2263f8bf802a6ee80506)(\_\_a\_\_)   \_mm\_movemask\_ps( \_\_a\_\_ ) |
|  | |
| #define | [AKSIMD\_TESTZERO\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_aee5b6249e8d04f9113ba4f45a72e3252.html#aee5b6249e8d04f9113ba4f45a72e3252)(\_\_a\_\_)   [AKSIMD\_TESTZERO\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_ad407bff1523faa8c3c6537604823e0a0.html#ad407bff1523faa8c3c6537604823e0a0)(\_mm\_castps\_si128(\_\_a\_\_)) |
|  | |
| #define | [AKSIMD\_TESTZERO\_V4COND](_platforms_2_s_s_e_2_ak_simd_8h_a34d6fc4d9abe6cc66d5f9cb6fcf56bc6.html#a34d6fc4d9abe6cc66d5f9cb6fcf56bc6)(\_\_a\_\_)   [AKSIMD\_TESTZERO\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_aee5b6249e8d04f9113ba4f45a72e3252.html#aee5b6249e8d04f9113ba4f45a72e3252)(\_\_a\_\_) |
|  | |
| #define | [AKSIMD\_TESTONES\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a4cec6791ba2c614771cc16430817db65.html#a4cec6791ba2c614771cc16430817db65)(\_\_a\_\_)   [AKSIMD\_TESTONES\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a861aa0814f16e5586af3e55e9fffa524.html#a861aa0814f16e5586af3e55e9fffa524)(\_mm\_castps\_si128(\_\_a\_\_)) |
|  | |
| #define | [AKSIMD\_TESTONES\_V4COND](_platforms_2_s_s_e_2_ak_simd_8h_a3b38e34062351da421a5c7bdd03dff62.html#a3b38e34062351da421a5c7bdd03dff62)(\_\_a\_\_)   [AKSIMD\_TESTONES\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a4cec6791ba2c614771cc16430817db65.html#a4cec6791ba2c614771cc16430817db65)(\_\_a\_\_) |
|  | |
| #define | [AKSIMD\_LOADU\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a3def10d2295ebe1376d1aa63166815e5.html#a3def10d2295ebe1376d1aa63166815e5)(\_\_addr\_\_)   \_mm\_loadu\_si128( (\_\_addr\_\_) ) |
|  | Loads unaligned 128-bit value (see \_mm\_loadu\_si128) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a3def10d2295ebe1376d1aa63166815e5.html#a3def10d2295ebe1376d1aa63166815e5) |
|  | |
| #define | [AKSIMD\_LOAD\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a1165dd0e842f030bb3215e4356863e26.html#a1165dd0e842f030bb3215e4356863e26)(\_\_addr\_\_)   \_mm\_loadu\_si128( (\_\_addr\_\_) ) |
|  | Loads aligned 128-bit value (see \_mm\_loadu\_si128) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a1165dd0e842f030bb3215e4356863e26.html#a1165dd0e842f030bb3215e4356863e26) |
|  | |
| #define | [AKSIMD\_SETZERO\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a05a655ed74acbe4ce1e7c1438a2f9a79.html#a05a655ed74acbe4ce1e7c1438a2f9a79)()   \_mm\_setzero\_si128() |
|  | Sets the four 32-bit integer values to zero (see \_mm\_setzero\_si128) [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a05a655ed74acbe4ce1e7c1438a2f9a79.html#a05a655ed74acbe4ce1e7c1438a2f9a79) |
|  | |
| #define | [AKSIMD\_SET\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a0ac4178aee1a8c6b41e163223b4f2241.html#a0ac4178aee1a8c6b41e163223b4f2241)(\_\_scalar\_\_)   \_mm\_set1\_epi32( (\_\_scalar\_\_) ) |
|  | |
| #define | [AKSIMD\_SET\_V16I8](_platforms_2_s_s_e_2_ak_simd_8h_a519cdde2f9b8573f597067b89786e911.html#a519cdde2f9b8573f597067b89786e911)(\_\_scalar\_\_)   \_mm\_set1\_epi8( (\_\_scalar\_\_) ) |
|  | |
| #define | [AKSIMD\_SETV\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_adf50fc9e781d109136e9255538e177ed.html#adf50fc9e781d109136e9255538e177ed)(\_d, \_c, \_b, \_a)   \_mm\_set\_epi32( (\_d), (\_c), (\_b), (\_a) ) |
|  | |
| #define | [AKSIMD\_SETV\_V2I64](_platforms_2_s_s_e_2_ak_simd_8h_a05e3df3e32447f4a1bb0418004c5af97.html#a05e3df3e32447f4a1bb0418004c5af97)(\_b, \_a)   \_mm\_set\_epi64x( (\_b), (\_a) ) |
|  | |
| #define | [AKSIMD\_INSERT\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a90637ba9a71177e4f8942c7b8b5dd1ca.html#a90637ba9a71177e4f8942c7b8b5dd1ca)(a, i, index)   \_mm\_insert\_epi32(a, i, index) |
|  | Sets the 32b integer i at the location specified by index in a [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a90637ba9a71177e4f8942c7b8b5dd1ca.html#a90637ba9a71177e4f8942c7b8b5dd1ca) |
|  | |
| #define | [AKSIMD\_INSERT\_V2I64](_platforms_2_s_s_e_2_ak_simd_8h_a49d9095b97a3051121408d8889c3a90d.html#a49d9095b97a3051121408d8889c3a90d)(a, i, index)   \_mm\_insert\_epi64(a, i, index) |
|  | Sets the 64b integer i at the location specified by index in a [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a49d9095b97a3051121408d8889c3a90d.html#a49d9095b97a3051121408d8889c3a90d) |
|  | |
| #define | [AKSIMD\_STORE\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a60b68a8942424d07ad83d314a738281f.html#a60b68a8942424d07ad83d314a738281f)(\_\_addr\_\_, \_\_vec\_\_)   \_mm\_storeu\_si128( (\_\_m128i\*)(\_\_addr\_\_), (\_\_vec\_\_) ) |
|  | |
| #define | [AKSIMD\_STOREU\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a17103230b5d8eab5d839a2c6db413511.html#a17103230b5d8eab5d839a2c6db413511)(\_\_addr\_\_, \_\_vec\_\_)   \_mm\_storeu\_si128( (\_\_m128i\*)(\_\_addr\_\_), (\_\_vec\_\_) ) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [AKSIMD\_VSEL\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a6fd3d8186775e03d62e5bc3ac157a9c3.html#a6fd3d8186775e03d62e5bc3ac157a9c3) ([AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) vA, [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) vB, [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) vMask) |
|  | Return a when control mask is 0, return b when control mask is non zero, control mask is in c and usually provided by above comparison operations [更多...](_platforms_2_s_s_e_2_ak_simd_8h_a6fd3d8186775e03d62e5bc3ac157a9c3.html#a6fd3d8186775e03d62e5bc3ac157a9c3) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [AKSIMD\_TESTZERO\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_ad407bff1523faa8c3c6537604823e0a0.html#ad407bff1523faa8c3c6537604823e0a0) ([AKSIMD\_V4I32](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) a) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [AKSIMD\_TESTONES\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a861aa0814f16e5586af3e55e9fffa524.html#a861aa0814f16e5586af3e55e9fffa524) ([AKSIMD\_V4I32](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) a) |
|  | |

|  |  |
| --- | --- |
| AKSIMD conversion | |
| #define | [AKSIMD\_CONVERT\_V4I32\_TO\_V4F32](_platforms_2_s_s_e_2_ak_simd_8h_a717dfec12d054b2301e9531a32f9dc69.html#a717dfec12d054b2301e9531a32f9dc69)(\_\_vec\_\_)   \_mm\_cvtepi32\_ps( (\_\_vec\_\_) ) |
|  | |
| #define | [AKSIMD\_ROUND\_V4F32\_TO\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_a2c5b3b1e5c889d5bb43777dd19d0aa1d.html#a2c5b3b1e5c889d5bb43777dd19d0aa1d)(\_\_vec\_\_)   \_mm\_cvtps\_epi32( (\_\_vec\_\_) ) |
|  | |
| #define | [AKSIMD\_TRUNCATE\_V4F32\_TO\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_acc068c1fb13c2240448986dc99a1285a.html#acc068c1fb13c2240448986dc99a1285a)(\_\_vec\_\_)   \_mm\_cvttps\_epi32( (\_\_vec\_\_) ) |
|  | |
| #define | [AKSIMD\_AND\_V4I32](_platforms_2_s_s_e_2_ak_simd_8h_ab256c6af68fab56f302a62267bd905cd.html#ab256c6af68fab56f302a62267bd905cd)(\_\_a\_\_, \_\_b\_\_)   \_mm\_and\_si128( (\_\_a\_\_), (\_\_b\_\_) ) |
|  | |
| #define | [AKSIMD\_CMPGT\_V8I16](_platforms_2_s_s_e_2_ak_simd_8h_ab57d46f959f2af8aca25a1e945210589.html#ab57d46f959f2af8aca25a1e945210589)(\_\_a\_\_, \_\_b\_\_)   \_mm\_cmpgt\_epi16( (\_\_a\_\_), (\_\_b\_\_) ) |
|  | |
| #define | [AKSIMD\_CONVERT\_V4F16\_TO\_V4F32\_LO](_platforms_2_s_s_e_2_ak_simd_8h_a1b7521e13ccf24522d83c2688d81ba8d.html#a1b7521e13ccf24522d83c2688d81ba8d)(\_\_vec\_\_)   [AKSIMD\_CONVERT\_V4F16\_TO\_V4F32\_HELPER](_platforms_2_s_s_e_2_ak_simd_8h_a8696abc9df18ce26a762fae27cc2c6dd.html#a8696abc9df18ce26a762fae27cc2c6dd)( \_mm\_unpacklo\_epi16(\_mm\_setzero\_si128(), \_\_vec\_\_)) |
|  | |
| #define | [AKSIMD\_CONVERT\_V4F16\_TO\_V4F32\_HI](_platforms_2_s_s_e_2_ak_simd_8h_a269d856d133d3a7e973516d3ee90ee23.html#a269d856d133d3a7e973516d3ee90ee23)(\_\_vec\_\_)   [AKSIMD\_CONVERT\_V4F16\_TO\_V4F32\_HELPER](_platforms_2_s_s_e_2_ak_simd_8h_a8696abc9df18ce26a762fae27cc2c6dd.html#a8696abc9df18ce26a762fae27cc2c6dd)( \_mm\_unpackhi\_epi16(\_mm\_setzero\_si128(), \_\_vec\_\_)) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [AKSIMD\_CONVERT\_V4F16\_TO\_V4F32\_HELPER](_platforms_2_s_s_e_2_ak_simd_8h_a8696abc9df18ce26a762fae27cc2c6dd.html#a8696abc9df18ce26a762fae27cc2c6dd) ([AKSIMD\_V4I32](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) vec) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4I32](_platforms_2arm__neon_2_ak_simd_types_8h_adb17cf12c601673ed735f7505bf30e5e.html#adb17cf12c601673ed735f7505bf30e5e) | [AKSIMD\_CONVERT\_V4F32\_TO\_V4F16](_platforms_2_s_s_e_2_ak_simd_8h_aeda52aa529192fa3633bf7ee1a8ac06b.html#aeda52aa529192fa3633bf7ee1a8ac06b) ([AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) vec) |
|  | |

## 详细描述

AKSIMD - SSE implementation

在文件 [AkSimd.h](_platforms_2_s_s_e_2_ak_simd_8h_source.html) 中定义.