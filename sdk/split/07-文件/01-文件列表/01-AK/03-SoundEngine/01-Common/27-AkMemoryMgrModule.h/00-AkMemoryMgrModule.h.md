# AkMemoryMgrModule.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[函数](#func-members)

AkMemoryMgrModule.h 文件参考

`#include <AK/SoundEngine/Common/AkMemoryMgr.h>`  
`#include <AK/SoundEngine/Common/AkTempAllocDefs.h>`  
`#include <AK/SoundEngine/Common/AkMemoryArenaTypes.h>`  
`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_ak_memory_mgr_module_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkMemSettings](struct_ak_mem_settings.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::MemoryArena](namespace_a_k_1_1_memory_arena.html) |
|  | |
|  | [AK::MemoryMgr](namespace_a_k_1_1_memory_mgr.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::MemoryMgr::Init](namespace_a_k_1_1_memory_mgr_a570a4ed4f667c187d21a821d846f4567.html#a570a4ed4f667c187d21a821d846f4567) ([AkMemSettings](struct_ak_mem_settings.html) \*in\_pSettings) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::GetDefaultSettings](namespace_a_k_1_1_memory_mgr_ada3c244e4c16e6863cec97eef039319b.html#ada3c244e4c16e6863cec97eef039319b) ([AkMemSettings](struct_ak_mem_settings.html) &out\_pMemSettings) |
|  | Obtain the default initialization settings for the default implementation of the Memory Manager. [更多...](namespace_a_k_1_1_memory_mgr_ada3c244e4c16e6863cec97eef039319b.html#ada3c244e4c16e6863cec97eef039319b) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::VerifyMemoryArenaIntegrity](namespace_a_k_1_1_memory_mgr_ae0e780ff8c6eb73541f5c4330460d6d5.html#ae0e780ff8c6eb73541f5c4330460d6d5) ([AkMemoryMgrArena](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4c) in\_eArena) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) AK::MemoryArena::AkMemoryArena \* | [AK::MemoryMgr::GetMemoryArena](namespace_a_k_1_1_memory_mgr_af7d6a2b29b087da7a00a643d7e822136.html#af7d6a2b29b087da7a00a643d7e822136) ([AkMemoryMgrArena](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4c) in\_eArena) |
|  | Helper to fetch each the arena. Should only be used for debug purposes, e.g. profiling, stats, integrity checks. Returns null in AK\_OPTIMIZED builds [更多...](namespace_a_k_1_1_memory_mgr_af7d6a2b29b087da7a00a643d7e822136.html#af7d6a2b29b087da7a00a643d7e822136) |
|  | |
| C runtime allocator functions for the default implementation of the Memory Manager. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkCrtAllocatorInitForThread](namespace_a_k_1_1_memory_mgr_a6645815e0697b791b60526a3f70fb42e.html#a6645815e0697b791b60526a3f70fb42e) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkCrtAllocatorTermForThread](namespace_a_k_1_1_memory_mgr_a1acb8811956fffa587e6863a184453b6.html#a1acb8811956fffa587e6863a184453b6) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkCrtAllocatorTrimForThread](namespace_a_k_1_1_memory_mgr_a5fd7cb4149c6283dc291167adfcb0c57.html#a5fd7cb4149c6283dc291167adfcb0c57) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::AkCrtAllocatorMalloc](namespace_a_k_1_1_memory_mgr_ae603bbd092159b47cd0070f6dbf11be9.html#ae603bbd092159b47cd0070f6dbf11be9) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::AkCrtAllocatorMalign](namespace_a_k_1_1_memory_mgr_adeea01e87516b1fd6a2e7f262a18a9b5.html#adeea01e87516b1fd6a2e7f262a18a9b5) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::AkCrtAllocatorRealloc](namespace_a_k_1_1_memory_mgr_aae39b6273ae26c0b3d6605ac26d7adeb.html#aae39b6273ae26c0b3d6605ac26d7adeb) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::AkCrtAllocatorReallocAligned](namespace_a_k_1_1_memory_mgr_a16101187acdf633d289538dfaa3b913d.html#a16101187acdf633d289538dfaa3b913d) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkCrtAllocatorFree](namespace_a_k_1_1_memory_mgr_aaec597f9a062c0277c28811f84c83724.html#aaec597f9a062c0277c28811f84c83724) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) size\_t | [AK::MemoryMgr::AkCrtAllocatorTotalReservedMemorySize](namespace_a_k_1_1_memory_mgr_aff92f964019ac1ea61d57430236edd6b.html#aff92f964019ac1ea61d57430236edd6b) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) size\_t | [AK::MemoryMgr::AkCrtAllocatorSizeOfMemory](namespace_a_k_1_1_memory_mgr_ab9323deb02481ceb94f84bccbf08d895.html#ab9323deb02481ceb94f84bccbf08d895) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolID, void \*pAddress) |
|  | |
| Stomp allocator functions for the default implementation of the Memory Manager. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkStompAllocatorInitForThread](namespace_a_k_1_1_memory_mgr_a60813ec48d84794f18fe9d538ac1612b.html#a60813ec48d84794f18fe9d538ac1612b) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkStompAllocatorTermForThread](namespace_a_k_1_1_memory_mgr_a0e2f31d6093b1fa65f6b14e5c6a13918.html#a0e2f31d6093b1fa65f6b14e5c6a13918) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkStompAllocatorTrimForThread](namespace_a_k_1_1_memory_mgr_a8abc3b6b89ddca48ee265b37dfbb1c4f.html#a8abc3b6b89ddca48ee265b37dfbb1c4f) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::AkStompAllocatorMalloc](namespace_a_k_1_1_memory_mgr_a43fbf3ad60d633b36475d2f919701a8a.html#a43fbf3ad60d633b36475d2f919701a8a) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::AkStompAllocatorMalign](namespace_a_k_1_1_memory_mgr_aabd0b3c83d2576c1a87ae10540adb85c.html#aabd0b3c83d2576c1a87ae10540adb85c) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::AkStompAllocatorRealloc](namespace_a_k_1_1_memory_mgr_a69c4f38513f2b025194eb7e2233b4f1c.html#a69c4f38513f2b025194eb7e2233b4f1c) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AK::MemoryMgr::AkStompAllocatorReallocAligned](namespace_a_k_1_1_memory_mgr_a38d5d3251e080fd46a1800883c3509e0.html#a38d5d3251e080fd46a1800883c3509e0) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkStompAllocatorFree](namespace_a_k_1_1_memory_mgr_ad448a46dbeae0468e3353b8694946a2e.html#ad448a46dbeae0468e3353b8694946a2e) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) size\_t | [AK::MemoryMgr::AkStompAllocatorTotalReservedMemorySize](namespace_a_k_1_1_memory_mgr_a831351e6c479450087177c959e900d43.html#a831351e6c479450087177c959e900d43) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) size\_t | [AK::MemoryMgr::AkStompAllocatorSizeOfMemory](namespace_a_k_1_1_memory_mgr_a34852e9379c1054ab549296f542672d5.html#a34852e9379c1054ab549296f542672d5) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolID, void \*pAddress) |
|  | |
| Debug tool hooks for the default implementation of the Memory Manager. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::MemoryMgr::AkMemDebugToolInit](namespace_a_k_1_1_memory_mgr_a03bbb450e12edc46538cd67bc88d29ca.html#a03bbb450e12edc46538cd67bc88d29ca) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkMemDebugToolTerm](namespace_a_k_1_1_memory_mgr_a1fa86e5ab43e65f0171678c15d448937.html#a1fa86e5ab43e65f0171678c15d448937) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkMemDebugToolMalloc](namespace_a_k_1_1_memory_mgr_aeec807c4109c4a85ce5d77544e9ba622.html#aeec807c4109c4a85ce5d77544e9ba622) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, void \*pAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkMemDebugToolMalign](namespace_a_k_1_1_memory_mgr_ad1fd2b4fbef6955a828e44a4801ff3a6.html#ad1fd2b4fbef6955a828e44a4801ff3a6) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment, void \*pAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkMemDebugToolRealloc](namespace_a_k_1_1_memory_mgr_ac86fd9348f79d90b88b2ca58b4fb4566.html#ac86fd9348f79d90b88b2ca58b4fb4566) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pOldAddress, size\_t uSize, void \*pNewAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkMemDebugToolReallocAligned](namespace_a_k_1_1_memory_mgr_aea32c7d9da9ec853d6470afa5ea21ff9.html#aea32c7d9da9ec853d6470afa5ea21ff9) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pOldAddress, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment, void \*pNewAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::MemoryMgr::AkMemDebugToolFree](namespace_a_k_1_1_memory_mgr_a41c07407be7e9088666fca72981df6b6.html#a41c07407be7e9088666fca72981df6b6) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress) |
|  | |

|  |  |
| --- | --- |
| Audiokinetic Memory Manager's implementation-specific definitions. | |
| #define | [AK\_CRT\_ALLOCATOR\_SUPPORTED](_ak_memory_mgr_module_8h_aa979b5c3b17ccf0686b9b919fb13d48f.html#aa979b5c3b17ccf0686b9b919fb13d48f) |
|  | |
| #define | [AK\_STOMP\_ALLOCATOR\_SUPPORTED](_ak_memory_mgr_module_8h_a6224438c55f276bf74224430ddd96986.html#a6224438c55f276bf74224430ddd96986) |
|  | |
| enum | [AkMemoryMgrArena](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4c) {     [AkMemoryMgrArena\_Primary](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4cada4fb0aaa502bf0b4481e825e20127be) = 0, [AkMemoryMgrArena\_Media](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4caf034292470314618cda8b900728cf644), [AkMemoryMgrArena\_Profiler](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4ca08ef70af1290299d43fafa826b9de574), [AkMemoryMgrArena\_Device](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4caf31ccab25cd476a2a56382d14f370537),     [AkMemoryMgrArena\_NUM](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4ca6d04cd32dae8081d7af43611f5f67ab6)   } |
|  | |
| typedef void(\* | [AkMemInitForThread](_ak_memory_mgr_module_8h_a8eb2200ee7ce4f8fd9163c4ef920c660.html#a8eb2200ee7ce4f8fd9163c4ef920c660)) () |
|  | |
| typedef void(\* | [AkMemTermForThread](_ak_memory_mgr_module_8h_a382c6e27bfdb1ef0f86f27469242ff31.html#a382c6e27bfdb1ef0f86f27469242ff31)) () |
|  | |
| typedef void(\* | [AkMemTrimForThread](_ak_memory_mgr_module_8h_a18902debaee9178ca56951d96c11cdee.html#a18902debaee9178ca56951d96c11cdee)) () |
|  | |
| typedef void \*(\* | [AkMemMalloc](_ak_memory_mgr_module_8h_a029efc97dac467b5a32c05f5a98a0be9.html#a029efc97dac467b5a32c05f5a98a0be9)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize) |
|  | |
| typedef void \*(\* | [AkMemMalign](_ak_memory_mgr_module_8h_aee41c8e4dcb40ccf365164f92833520a.html#aee41c8e4dcb40ccf365164f92833520a)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| typedef void \*(\* | [AkMemRealloc](_ak_memory_mgr_module_8h_a5953a53e49ecf87aa7b27c16d772d41a.html#a5953a53e49ecf87aa7b27c16d772d41a)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize) |
|  | |
| typedef void \*(\* | [AkMemReallocAligned](_ak_memory_mgr_module_8h_a86749afaecf1e9e68d6f8a3b62499b87.html#a86749afaecf1e9e68d6f8a3b62499b87)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| typedef void(\* | [AkMemFree](_ak_memory_mgr_module_8h_ac6982afe3d12d5af12af319d7c80d411.html#ac6982afe3d12d5af12af319d7c80d411)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress) |
|  | |
| typedef size\_t(\* | [AkMemTotalReservedMemorySize](_ak_memory_mgr_module_8h_ad18caa43a0995ec341bd0100d2424ac5.html#ad18caa43a0995ec341bd0100d2424ac5)) () |
|  | |
| typedef size\_t(\* | [AkMemSizeOfMemory](_ak_memory_mgr_module_8h_a7226b7b4a72db37bae1e2c5e0998adf2.html#a7226b7b4a72db37bae1e2c5e0998adf2)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress) |
|  | |
| typedef void(\* | [AkMemDebugMalloc](_ak_memory_mgr_module_8h_a868d7cb6a8696f0254f572959fa8058f.html#a868d7cb6a8696f0254f572959fa8058f)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, void \*pAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| typedef void(\* | [AkMemDebugMalign](_ak_memory_mgr_module_8h_a0007c7fcd5e73e862d2338123ec46d97.html#a0007c7fcd5e73e862d2338123ec46d97)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment, void \*pAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| typedef void(\* | [AkMemDebugRealloc](_ak_memory_mgr_module_8h_ae82460c988c5e6eb441b905447fa8fc9.html#ae82460c988c5e6eb441b905447fa8fc9)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pOldAddress, size\_t uSize, void \*pNewAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| typedef void(\* | [AkMemDebugReallocAligned](_ak_memory_mgr_module_8h_abea2c80bd6bfbcfd82ffcfe3ca3ffea4.html#abea2c80bd6bfbcfd82ffcfe3ca3ffea4)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pOldAddress, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment, void \*pNewAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| typedef void(\* | [AkMemDebugFree](_ak_memory_mgr_module_8h_aac6a537e02b9f4d99c0de1cba128f70c.html#aac6a537e02b9f4d99c0de1cba128f70c)) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress) |
|  | |

## 详细描述

Audiokinetic's definitions and factory of overridable Memory Manager module.

在文件 [AkMemoryMgrModule.h](_ak_memory_mgr_module_8h_source.html) 中定义.