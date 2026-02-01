# Instrument

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Instrument](namespace_a_k_1_1_instrument.html)

[类](#nested-classes) |
[类型定义](#typedef-members) |
[变量](#var-members)

AK::Instrument 命名空间参考

|  |  |
| --- | --- |
| 类 | |
| class | [Scope](class_a_k_1_1_instrument_1_1_scope.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef void \*(\* | [PushTimerFunc](namespace_a_k_1_1_instrument_a737fc9eef47768e98caec23231dccefd.html#a737fc9eef47768e98caec23231dccefd)) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) in\_uPluginID, const char \*in\_pszZoneName) |
|  | |
| typedef void(\* | [PopTimerFunc](namespace_a_k_1_1_instrument_a0c015e6db21c1577fe36728135cdfe66.html#a0c015e6db21c1577fe36728135cdfe66)) (void \*in\_pToken) |
|  | |
| typedef void(\* | [PostMarkerFunc](namespace_a_k_1_1_instrument_a0f011312f47c5cc3bc989bb2de67b59f.html#a0f011312f47c5cc3bc989bb2de67b59f)) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) in\_uPluginID, const char \*in\_pszMarkerName) |
|  | |
| typedef void(\* | [PostMetaMarkerFunc](namespace_a_k_1_1_instrument_a9790dde9ce51c438ed6ab17be5727886.html#a9790dde9ce51c438ed6ab17be5727886)) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) in\_uPluginID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uMetadata) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| [PushTimerFunc](namespace_a_k_1_1_instrument_a737fc9eef47768e98caec23231dccefd.html#a737fc9eef47768e98caec23231dccefd) | [g\_fnPushTimer](namespace_a_k_1_1_instrument_a4d6354879e83de9f73cbc5bd3e96343a.html#a4d6354879e83de9f73cbc5bd3e96343a) |
|  | |
| [PopTimerFunc](namespace_a_k_1_1_instrument_a0c015e6db21c1577fe36728135cdfe66.html#a0c015e6db21c1577fe36728135cdfe66) | [g\_fnPopTimer](namespace_a_k_1_1_instrument_ad0bf380e63872033d2f2ab0a2b352e2a.html#ad0bf380e63872033d2f2ab0a2b352e2a) |
|  | |
| [PostMarkerFunc](namespace_a_k_1_1_instrument_a0f011312f47c5cc3bc989bb2de67b59f.html#a0f011312f47c5cc3bc989bb2de67b59f) | [g\_fnPostMarker](namespace_a_k_1_1_instrument_aa777c6d77bb5c34e43c405e38bc80af8.html#aa777c6d77bb5c34e43c405e38bc80af8) |
|  | |
| [PostMetaMarkerFunc](namespace_a_k_1_1_instrument_a9790dde9ce51c438ed6ab17be5727886.html#a9790dde9ce51c438ed6ab17be5727886) | [g\_fnPostMetaMarker](namespace_a_k_1_1_instrument_a75981354356e161bf785b5aa0e6ce070.html#a75981354356e161bf785b5aa0e6ce070) |
|  | |