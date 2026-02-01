# AkInstrument.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[变量](#var-members)

AkInstrument.h 文件参考

`#include <AK/SoundEngine/Common/AkCommonDefs.h>`  
`#include <AK/Tools/Common/AkAssert.h>`

[浏览源代码.](_ak_instrument_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AK::Instrument::Scope](class_a_k_1_1_instrument_1_1_scope.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::Instrument](namespace_a_k_1_1_instrument.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_INSTRUMENT\_BEGIN](_ak_instrument_8h_ae37bc915cac8ae64ba260d5ec4558fee.html#ae37bc915cac8ae64ba260d5ec4558fee)(\_plugin\_id\_, \_zone\_name\_)   ([AK::Instrument::g\_fnPushTimer](namespace_a_k_1_1_instrument_a4d6354879e83de9f73cbc5bd3e96343a.html#a4d6354879e83de9f73cbc5bd3e96343a)(\_plugin\_id\_, \_zone\_name\_)) |
|  | |
| #define | [AK\_INSTRUMENT\_END](_ak_instrument_8h_a96088112e8415d065ac15f0939b96b2b.html#a96088112e8415d065ac15f0939b96b2b)(\_\_token\_\_)   ([AK::Instrument::g\_fnPopTimer](namespace_a_k_1_1_instrument_ad0bf380e63872033d2f2ab0a2b352e2a.html#ad0bf380e63872033d2f2ab0a2b352e2a)(\_\_token\_\_)) |
|  | |
| #define | [AK\_INSTRUMENT\_MARKER](_ak_instrument_8h_aeab71ae33e14db55ac13e0bd8df7d001.html#aeab71ae33e14db55ac13e0bd8df7d001)(\_plugin\_id\_, \_marker\_name\_)   ([AK::Instrument::g\_fnPostMarker](namespace_a_k_1_1_instrument_aa777c6d77bb5c34e43c405e38bc80af8.html#aa777c6d77bb5c34e43c405e38bc80af8)(\_plugin\_id\_, \_marker\_name\_)) |
|  | |
| #define | [AK\_INSTRUMENT\_MARKER\_PROFILINGID](_ak_instrument_8h_a106b2266075b2a72725301785f637e90.html#a106b2266075b2a72725301785f637e90)(\_profilingid\_)   ([AK::Instrument::g\_fnPostMarker](namespace_a_k_1_1_instrument_aa777c6d77bb5c34e43c405e38bc80af8.html#aa777c6d77bb5c34e43c405e38bc80af8)([AKMAKECLASSID](_ak_common_defs_8h_ac73a5e1e4a45a0aeea1b11b08ba93516.html#ac73a5e1e4a45a0aeea1b11b08ba93516)( [AkPluginTypeNone](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4a8b439dd9d1761adf9912d02734a74bcd), [AKCOMPANYID\_AUDIOKINETIC](_ak_constants_8h_a807adbb4abc6856ff54fa2010e7f6a0f.html#a807adbb4abc6856ff54fa2010e7f6a0f), \_profilingid\_ ), nullptr)) |
|  | |
| #define | [AK\_INSTRUMENT\_METAMARKER](_ak_instrument_8h_aa231ffac244555f4d91301f2d866b47b.html#aa231ffac244555f4d91301f2d866b47b)(\_plugin\_id\_, \_metadata\_)   ([AK::Instrument::g\_fnPostMetaMarker](namespace_a_k_1_1_instrument_a75981354356e161bf785b5aa0e6ce070.html#a75981354356e161bf785b5aa0e6ce070)(\_plugin\_id\_, \_metadata\_)) |
|  | |
| #define | [AK\_INSTRUMENT\_CONCAT\_INNER](_ak_instrument_8h_a66b1d62e3d3035a1758843ac3c769e36.html#a66b1d62e3d3035a1758843ac3c769e36)(\_base\_, \_counter\_)   \_base\_ ## \_counter\_ |
|  | |
| #define | [AK\_INSTRUMENT\_CONCAT](_ak_instrument_8h_a4d3c29b432e1919289fa01380543d5f4.html#a4d3c29b432e1919289fa01380543d5f4)(\_base\_, \_counter\_)   [AK\_INSTRUMENT\_CONCAT\_INNER](_ak_instrument_8h_a66b1d62e3d3035a1758843ac3c769e36.html#a66b1d62e3d3035a1758843ac3c769e36)(\_base\_, \_counter\_) |
|  | |
| #define | [AK\_INSTRUMENT\_SCOPE](_ak_instrument_8h_a03a63ce8dce30a5215c4e5beace1fe9d.html#a03a63ce8dce30a5215c4e5beace1fe9d)(\_zone\_name\_)    [AK::Instrument::Scope](class_a_k_1_1_instrument_1_1_scope.html) [AK\_INSTRUMENT\_CONCAT](_ak_instrument_8h_a4d3c29b432e1919289fa01380543d5f4.html#a4d3c29b432e1919289fa01380543d5f4)(\_akInstrumentScope\_, \_\_LINE\_\_)(0, \_zone\_name\_) |
|  | |
| #define | [AK\_INSTRUMENT\_SCOPE\_ID](_ak_instrument_8h_a4ae24e7988a5ebdefbf5f75a254336ab.html#a4ae24e7988a5ebdefbf5f75a254336ab)(\_plugin\_id\_, \_zone\_name\_)    [AK::Instrument::Scope](class_a_k_1_1_instrument_1_1_scope.html) [AK\_INSTRUMENT\_CONCAT](_ak_instrument_8h_a4d3c29b432e1919289fa01380543d5f4.html#a4d3c29b432e1919289fa01380543d5f4)(\_akInstrumentScope\_, \_\_LINE\_\_)(\_plugin\_id\_, \_zone\_name\_) |
|  | |
| #define | [AK\_INSTRUMENT\_SCOPE\_PROFILINGID](_ak_instrument_8h_a8f2268e3785049353af0dd5b31237b81.html#a8f2268e3785049353af0dd5b31237b81)(\_profilingid\_)    [AK::Instrument::Scope](class_a_k_1_1_instrument_1_1_scope.html) [AK\_INSTRUMENT\_CONCAT](_ak_instrument_8h_a4d3c29b432e1919289fa01380543d5f4.html#a4d3c29b432e1919289fa01380543d5f4)(\_akInstrumentScope\_, \_\_LINE\_\_)([AKMAKECLASSID](_ak_common_defs_8h_ac73a5e1e4a45a0aeea1b11b08ba93516.html#ac73a5e1e4a45a0aeea1b11b08ba93516)( [AkPluginTypeNone](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4a8b439dd9d1761adf9912d02734a74bcd), [AKCOMPANYID\_AUDIOKINETIC](_ak_constants_8h_a807adbb4abc6856ff54fa2010e7f6a0f.html#a807adbb4abc6856ff54fa2010e7f6a0f), \_profilingid\_ ), nullptr) |
|  | |
| #define | [AK\_INSTRUMENT\_THREAD\_START](_ak_instrument_8h_a4267b9fea38693fbb38a425a2e93669c.html#a4267b9fea38693fbb38a425a2e93669c)(\_thread\_name\_) |
|  | |
| #define | [AK\_INSTRUMENT\_BEGIN\_C](_ak_instrument_8h_a6113adb4ca0af1d57c114a53e5b9f15a.html#a6113adb4ca0af1d57c114a53e5b9f15a)(\_plugin\_id\_, \_color\_, \_zone\_name\_)   [AK\_INSTRUMENT\_BEGIN](_ak_instrument_8h_ae37bc915cac8ae64ba260d5ec4558fee.html#ae37bc915cac8ae64ba260d5ec4558fee)(\_plugin\_id\_, \_zone\_name\_) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef void \*(\* | [AK::Instrument::PushTimerFunc](namespace_a_k_1_1_instrument_a737fc9eef47768e98caec23231dccefd.html#a737fc9eef47768e98caec23231dccefd)) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) in\_uPluginID, const char \*in\_pszZoneName) |
|  | |
| typedef void(\* | [AK::Instrument::PopTimerFunc](namespace_a_k_1_1_instrument_a0c015e6db21c1577fe36728135cdfe66.html#a0c015e6db21c1577fe36728135cdfe66)) (void \*in\_pToken) |
|  | |
| typedef void(\* | [AK::Instrument::PostMarkerFunc](namespace_a_k_1_1_instrument_a0f011312f47c5cc3bc989bb2de67b59f.html#a0f011312f47c5cc3bc989bb2de67b59f)) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) in\_uPluginID, const char \*in\_pszMarkerName) |
|  | |
| typedef void(\* | [AK::Instrument::PostMetaMarkerFunc](namespace_a_k_1_1_instrument_a9790dde9ce51c438ed6ab17be5727886.html#a9790dde9ce51c438ed6ab17be5727886)) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) in\_uPluginID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uMetadata) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| PushTimerFunc | [AK::Instrument::g\_fnPushTimer](namespace_a_k_1_1_instrument_a4d6354879e83de9f73cbc5bd3e96343a.html#a4d6354879e83de9f73cbc5bd3e96343a) |
|  | |
| PopTimerFunc | [AK::Instrument::g\_fnPopTimer](namespace_a_k_1_1_instrument_ad0bf380e63872033d2f2ab0a2b352e2a.html#ad0bf380e63872033d2f2ab0a2b352e2a) |
|  | |
| PostMarkerFunc | [AK::Instrument::g\_fnPostMarker](namespace_a_k_1_1_instrument_aa777c6d77bb5c34e43c405e38bc80af8.html#aa777c6d77bb5c34e43c405e38bc80af8) |
|  | |
| PostMetaMarkerFunc | [AK::Instrument::g\_fnPostMetaMarker](namespace_a_k_1_1_instrument_a75981354356e161bf785b5aa0e6ce070.html#a75981354356e161bf785b5aa0e6ce070) |
|  | |