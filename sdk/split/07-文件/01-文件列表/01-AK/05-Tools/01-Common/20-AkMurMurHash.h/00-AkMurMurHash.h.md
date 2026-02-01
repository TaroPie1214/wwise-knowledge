# AkMurMurHash.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[宏定义](#define-members) |
[函数](#func-members)

AkMurMurHash.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/Tools/Common/AkBitFuncs.h>`

[浏览源代码.](_ak_mur_mur_hash_8h_source.html)

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [MURMUR3\_SEED](_ak_mur_mur_hash_8h_a85a6127bce4471398b6f1e498115c8a1.html#a85a6127bce4471398b6f1e498115c8a1)   ( 0x41545731 ) |
|  | |
| #define | [MURMUR3\_C1](_ak_mur_mur_hash_8h_ac9b59e30c247c7e0516dc2e4db2e6e2b.html#ac9b59e30c247c7e0516dc2e4db2e6e2b)   ( 0xcc9e2d51 ) |
|  | |
| #define | [MURMUR3\_C2](_ak_mur_mur_hash_8h_a24f6396ca9661a4ba9729792c8af95e9.html#a24f6396ca9661a4ba9729792c8af95e9)   ( 0x1b873593 ) |
|  | |
| #define | [MURMUR3\_C3](_ak_mur_mur_hash_8h_ad39e46abec339daf2c32d31be4ddfdfa.html#ad39e46abec339daf2c32d31be4ddfdfa)   ( 0xe6546b64 ) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkHashMurMurMix32](_ak_mur_mur_hash_8h_abcacf2bd82383d55f0a8da3b2447fe2c.html#abcacf2bd82383d55f0a8da3b2447fe2c) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uValue) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [AkHashMurMurMix64](_ak_mur_mur_hash_8h_a25348196cbc00868b2dc8892baabf549.html#a25348196cbc00868b2dc8892baabf549) ([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) uValue) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AkHashMurMur32](_ak_mur_mur_hash_8h_a8e71a4340bebbc11940b77ac5954c854.html#a8e71a4340bebbc11940b77ac5954c854) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) \*pHash, const void \*pData, size\_t uSize) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkHashMurMurMixExtra32](_ak_mur_mur_hash_8h_aa5fde2003647c8f61a8420c2e1167bea.html#aa5fde2003647c8f61a8420c2e1167bea) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uHash, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uExtraValue) |
|  | |