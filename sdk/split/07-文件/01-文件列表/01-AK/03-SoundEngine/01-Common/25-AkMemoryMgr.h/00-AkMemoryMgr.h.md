# AkMemoryMgr.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[枚举](#enum-members)

AkMemoryMgr.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/SoundEngine/Common/AkSoundEngineExport.h>`

[浏览源代码.](_ak_memory_mgr_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AK::MemoryMgr::CategoryStats](struct_a_k_1_1_memory_mgr_1_1_category_stats.html) |
|  | |
| struct | [AK::MemoryMgr::GlobalStats](struct_a_k_1_1_memory_mgr_1_1_global_stats.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::MemoryMgr](namespace_a_k_1_1_memory_mgr.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_MEMDEBUG](_ak_memory_mgr_8h_a65db4f89b8a435b213e4a494940a492d.html#a65db4f89b8a435b213e4a494940a492d) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AkMemID](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516) {     [AkMemID\_Object](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a57aafbdd3be55093215a3ad89e0db902), [AkMemID\_Event](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516aa1a8896cb69f45b7e1c5dc5171192f3a), [AkMemID\_Structure](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a5dd04efbde5be3b98157e17ac2a6a4d4), [AkMemID\_Media](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516ab2c92abb950a1f352ff322523d605312),     [AkMemID\_GameObject](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516aa8f0f6d38f4a629c21ce42ac5944fd15), [AkMemID\_Processing](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a0c6d546662db0bf99d2b8ad68d132474), [AkMemID\_ProcessingPlugin](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a9472ba08ba89770a537f8cdbc5785724), [AkMemID\_Streaming](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516ae2e003662ee9b306f5b7e4a43dbaeb1b),     [AkMemID\_StreamingIO](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a3080b97e18605ada1b7c2732ab18c322), [AkMemID\_SpatialAudio](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516aa0c9b46cbf0d7c4016eaf029a2da40a2), [AkMemID\_SpatialAudioGeometry](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516ab5a99966c22d680051f85c763ffa45ea), [AkMemID\_SpatialAudioPaths](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a0cfaea3f5c89a0b066bd28f0363ce47e),     [AkMemID\_GameSim](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a826ca514b3a5cbd13c95c5468bb3b031), [AkMemID\_MonitorQueue](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a7adb5755ff17d591746f2dfdeac2d761), [AkMemID\_Profiler](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516af31745e6d45df2870b9e2821f2cd93d1), [AkMemID\_FilePackage](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516ae62f54cb7a9d92a2cd820732d9c9cbba),     [AkMemID\_SoundEngine](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516ad2f78907168400d636558ef5d6ae4808), [AkMemID\_Integration](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a976b2c0ee55cb601e37177187156a48b), [AkMemID\_JobMgr](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516ad92fcf3d0d0c63e93a264faca8bc3f19), [AkMemID\_TempAudioRender](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a9944ff9ff55c7e60d9c46bd58bc80830),     [AkMemID\_BookmarkAlloc](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a27beea169410bcc72748974b57f0ede3), [AkMemID\_NUM](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a1f08c2242ab0892540ad61fc9cd4760e), [AkMemID\_MASK](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a0ac6db72c920af54b0384f752ff63a2b) = 0x1FFFFFFF, [AkMemType\_Media](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a4920e03d383120a5bf0a3aedaf69d836) = 0x20000000,     [AkMemType\_Device](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516a585615b8b0c683825310b81e6329a206) = 0x40000000, [AkMemType\_NoTrack](_ak_memory_mgr_8h_a3af3228fe8c3640b2d2be6d1102dd516.html#a3af3228fe8c3640b2d2be6d1102dd516ad88dff6ecda6f2dfdd0eb9658b25a66f) = 0x80000000   } |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| Initialization | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) bool | [AK::MemoryMgr::IsInitialized](namespace_a_k_1_1_memory_mgr_a91028bc94037785fa186b827f81c59c9.html#a91028bc94037785fa186b827f81c59c9) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::Term](namespace_a_k_1_1_memory_mgr_a3ec018c61b5dc7428cf51f35f290739e.html#a3ec018c61b5dc7428cf51f35f290739e) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::InitForThread](namespace_a_k_1_1_memory_mgr_a76b450a2f472f5d9bc61aa1c3ed9a722.html#a76b450a2f472f5d9bc61aa1c3ed9a722) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::TermForThread](namespace_a_k_1_1_memory_mgr_a3c47d8b70c74b631184ad9ea34c6f942.html#a3c47d8b70c74b631184ad9ea34c6f942) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::TrimForThread](namespace_a_k_1_1_memory_mgr_a325a7f2aa771d1f25e280441cb77151d.html#a325a7f2aa771d1f25e280441cb77151d) () |
|  | |
| Memory Allocation | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::dMalloc](namespace_a_k_1_1_memory_mgr_a157a010cab9d463be18a871c350bd226.html#a157a010cab9d463be18a871c350bd226) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, size\_t in\_uSize, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::Malloc](namespace_a_k_1_1_memory_mgr_a8727fb3eaaefd366474f802b0467b296.html#a8727fb3eaaefd366474f802b0467b296) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, size\_t in\_uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::dRealloc](namespace_a_k_1_1_memory_mgr_ada579cbaf74944b6fb35d31d352bff66.html#ada579cbaf74944b6fb35d31d352bff66) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pAlloc, size\_t in\_uSize, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::Realloc](namespace_a_k_1_1_memory_mgr_a3713e20d272952a685bf42419a1dd6d3.html#a3713e20d272952a685bf42419a1dd6d3) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pAlloc, size\_t in\_uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::dReallocAligned](namespace_a_k_1_1_memory_mgr_ae966f222f7169c58b4d8be9e938fbf87.html#ae966f222f7169c58b4d8be9e938fbf87) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pAlloc, size\_t in\_uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAlignment, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::ReallocAligned](namespace_a_k_1_1_memory_mgr_a98fd48e4adafff36f44d6bf9be73bd41.html#a98fd48e4adafff36f44d6bf9be73bd41) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pAlloc, size\_t in\_uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::Free](namespace_a_k_1_1_memory_mgr_a6ee20149a37b11b31589c6f23f46db65.html#a6ee20149a37b11b31589c6f23f46db65) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pMemAddress) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::dMalign](namespace_a_k_1_1_memory_mgr_a042b69a423f6f4ea43499898faf5ba22.html#a042b69a423f6f4ea43499898faf5ba22) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, size\_t in\_uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAlignment, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::Malign](namespace_a_k_1_1_memory_mgr_aeb57745b9cfdc88c9775e5bc504e9ab5.html#aeb57745b9cfdc88c9775e5bc504e9ab5) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, size\_t in\_uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAlignment) |
|  | |
| Memory Profiling | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::GetCategoryStats](namespace_a_k_1_1_memory_mgr_a4a00138319c6ee33a6a4c896cabcea34.html#a4a00138319c6ee33a6a4c896cabcea34) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, CategoryStats &out\_poolStats) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::GetGlobalStats](namespace_a_k_1_1_memory_mgr_a49ab92c52b9afa8e034863f2cdd2209e.html#a49ab92c52b9afa8e034863f2cdd2209e) (GlobalStats &out\_stats) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::StartProfileThreadUsage](namespace_a_k_1_1_memory_mgr_a83fc28efeaf65ff66ba6011d31f7db92.html#a83fc28efeaf65ff66ba6011d31f7db92) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [AK::MemoryMgr::StopProfileThreadUsage](namespace_a_k_1_1_memory_mgr_ac01c971988f35fbbdd2db5ed8b056aee.html#ac01c971988f35fbbdd2db5ed8b056aee) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::DumpToFile](namespace_a_k_1_1_memory_mgr_a4f48ed6707ab2f2341f4a81f1c6053d7.html#a4f48ed6707ab2f2341f4a81f1c6053d7) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*pszFilename) |
|  | |

## 详细描述

Memory Manager namespace.

在文件 [AkMemoryMgr.h](_ak_memory_mgr_8h_source.html) 中定义.