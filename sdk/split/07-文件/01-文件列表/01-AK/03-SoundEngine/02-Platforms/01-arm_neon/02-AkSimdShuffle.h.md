# AkSimdShuffle.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Platforms](dir_9707d8b0bea28caa964fded672ce5309.html)
- [arm\_neon](dir_cb8d730ec7448ade74b00880a1c0dd04.html)

[命名空间](#namespaces) |
[函数](#func-members)

AkSimdShuffle.h 文件参考

[浏览源代码.](_ak_simd_shuffle_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
|  | [\_AKSIMD\_LOCAL](namespace___a_k_s_i_m_d___l_o_c_a_l.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| template<int zyxw> | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32](namespace___a_k_s_i_m_d___l_o_c_a_l_a7770d8f223bdb0822ab48ad1f56b96b1.html#a7770d8f223bdb0822ab48ad1f56b96b1) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &a, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &b) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(0, 0, 0, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a862764c1f1065a4c5c0c3b8103faa7af.html#a862764c1f1065a4c5c0c3b8103faa7af) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(0, 0, 3, 3)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a0e9a6e7b2ebb774b41c52f4722d3e00d.html#a0e9a6e7b2ebb774b41c52f4722d3e00d) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(0, 1, 0, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_ae868ea5508124d9e284125ce85abe2a4.html#ae868ea5508124d9e284125ce85abe2a4) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(0, 1, 3, 2)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a344e4873a1d4bf28a2895ff63dd4f2e0.html#a344e4873a1d4bf28a2895ff63dd4f2e0) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(0, 3, 1, 2)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a437c684c324bcc81a6c5a2744255cb81.html#a437c684c324bcc81a6c5a2744255cb81) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(0, 3, 2, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a2866003f8130a0d34dd0def356bf00d2.html#a2866003f8130a0d34dd0def356bf00d2) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &a, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &b) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(1, 0, 1, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_ae533c32eb006018dd6d330a91598478d.html#ae533c32eb006018dd6d330a91598478d) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(1, 0, 2, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_ad815f9217ec3a12f78f79f7f5cb4d957.html#ad815f9217ec3a12f78f79f7f5cb4d957) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(1, 0, 3, 2)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a2a23682ab7d0aa606c6f3188a1775356.html#a2a23682ab7d0aa606c6f3188a1775356) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(1, 1, 1, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_aa269686d346f5b567921f9a640d2ccdc.html#aa269686d346f5b567921f9a640d2ccdc) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(1, 3, 0, 2)>](namespace___a_k_s_i_m_d___l_o_c_a_l_ac3deebbf93d72c46a09aec13b63aff32.html#ac3deebbf93d72c46a09aec13b63aff32) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 0, 0, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_ae03636af254e1310a59e5fc6d861fc4a.html#ae03636af254e1310a59e5fc6d861fc4a) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 0, 2, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a671c284ad6ad7262910dccdd1c79da73.html#a671c284ad6ad7262910dccdd1c79da73) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 0, 2, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a9cf29f71eac364daccb61e1cebee1363.html#a9cf29f71eac364daccb61e1cebee1363) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 0, 3, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a967def5f7bd6cce206398fa7fbd3267a.html#a967def5f7bd6cce206398fa7fbd3267a) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 0, 3, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_ac300d11c1715b06bfcc2572713fba58d.html#ac300d11c1715b06bfcc2572713fba58d) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 1, 2, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_acafe8ae52d65633f183dcd8469b94ad4.html#acafe8ae52d65633f183dcd8469b94ad4) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 1, 3, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a81822a6a5ccc5519cb639573d35fce21.html#a81822a6a5ccc5519cb639573d35fce21) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 1, 3, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a38c4e518ab9d93099bb85f029e0a3919.html#a38c4e518ab9d93099bb85f029e0a3919) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 2, 0, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_ab68a7ff0042a293e2ef78caa397a51d9.html#ab68a7ff0042a293e2ef78caa397a51d9) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 2, 2, 2)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a561f42fdac46b88d5c991ca021459051.html#a561f42fdac46b88d5c991ca021459051) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 3, 0, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a3d0409f92cb5eb7b691fef33a7ddc1c4.html#a3d0409f92cb5eb7b691fef33a7ddc1c4) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(2, 3, 2, 3)>](namespace___a_k_s_i_m_d___l_o_c_a_l_ac50263d7efedc4710a4f6397c52b522c.html#ac50263d7efedc4710a4f6397c52b522c) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 0, 2, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a4ae33bf68562a402650caff9a645e5a4.html#a4ae33bf68562a402650caff9a645e5a4) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 0, 2, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a8da20494acb08b85c5819a39bab07dff.html#a8da20494acb08b85c5819a39bab07dff) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 0, 3, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_abba9a78469e65e236415ef5f183f2c9f.html#abba9a78469e65e236415ef5f183f2c9f) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 1, 2, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a8bc19596313bea5836840d47c92acced.html#a8bc19596313bea5836840d47c92acced) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 1, 2, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a9f055db345a6dab3d3981c3369036329.html#a9f055db345a6dab3d3981c3369036329) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 1, 3, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_add9a317766c5ac457ff97cd7d1001438.html#add9a317766c5ac457ff97cd7d1001438) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 1, 3, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a5c9ef712c10a35955953831a565a77ab.html#a5c9ef712c10a35955953831a565a77ab) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 2, 1, 0)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a1be250bc7dc2fa9b88ba73280fcc7fc7.html#a1be250bc7dc2fa9b88ba73280fcc7fc7) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 2, 3, 2)>](namespace___a_k_s_i_m_d___l_o_c_a_l_af2c2d8fbb11b14c77add906af764d679.html#af2c2d8fbb11b14c77add906af764d679) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 3, 1, 1)>](namespace___a_k_s_i_m_d___l_o_c_a_l_a362431809b21a31a5b5a36c4d2709586.html#a362431809b21a31a5b5a36c4d2709586) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |
| template<> |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) | [\_AKSIMD\_LOCAL::SHUFFLE\_V4F32< AKSIMD\_SHUFFLE(3, 3, 3, 3)>](namespace___a_k_s_i_m_d___l_o_c_a_l_ac83bfdbbe847b1c771f80f58ddc69c9c.html#ac83bfdbbe847b1c771f80f58ddc69c9c) (const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &xyzw, const [AKSIMD\_V4F32](_platforms_2arm__neon_2_ak_simd_types_8h_a3b875ede86d9b294cff47d890c9ae3ef.html#a3b875ede86d9b294cff47d890c9ae3ef) &abcd) |
|  | |

## 详细描述

\_AKSIMD\_LOCAL::SHUFFLE\_V4F32<zyxw>(a, b) - arm\_neon implementation

在文件 [AkSimdShuffle.h](_ak_simd_shuffle_8h_source.html) 中定义.