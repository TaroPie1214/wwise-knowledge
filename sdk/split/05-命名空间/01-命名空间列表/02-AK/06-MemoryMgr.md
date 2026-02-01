# MemoryMgr

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [MemoryMgr](namespace_a_k_1_1_memory_mgr.html)

[类](#nested-classes) |
[函数](#func-members)

AK::MemoryMgr 命名空间参考

|  |  |
| --- | --- |
| 类 | |
| struct | [CategoryStats](struct_a_k_1_1_memory_mgr_1_1_category_stats.html) |
|  | |
| struct | [GlobalStats](struct_a_k_1_1_memory_mgr_1_1_global_stats.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](namespace_a_k_1_1_memory_mgr_a570a4ed4f667c187d21a821d846f4567.html#a570a4ed4f667c187d21a821d846f4567) ([AkMemSettings](struct_ak_mem_settings.html) \*in\_pSettings) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [GetDefaultSettings](namespace_a_k_1_1_memory_mgr_ada3c244e4c16e6863cec97eef039319b.html#ada3c244e4c16e6863cec97eef039319b) ([AkMemSettings](struct_ak_mem_settings.html) &out\_pMemSettings) |
|  | Obtain the default initialization settings for the default implementation of the Memory Manager. [更多...](namespace_a_k_1_1_memory_mgr_ada3c244e4c16e6863cec97eef039319b.html#ada3c244e4c16e6863cec97eef039319b) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [VerifyMemoryArenaIntegrity](namespace_a_k_1_1_memory_mgr_ae0e780ff8c6eb73541f5c4330460d6d5.html#ae0e780ff8c6eb73541f5c4330460d6d5) ([AkMemoryMgrArena](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4c) in\_eArena) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) AK::MemoryArena::AkMemoryArena \* | [GetMemoryArena](namespace_a_k_1_1_memory_mgr_af7d6a2b29b087da7a00a643d7e822136.html#af7d6a2b29b087da7a00a643d7e822136) ([AkMemoryMgrArena](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4c) in\_eArena) |
|  | Helper to fetch each the arena. Should only be used for debug purposes, e.g. profiling, stats, integrity checks. Returns null in AK\_OPTIMIZED builds [更多...](namespace_a_k_1_1_memory_mgr_af7d6a2b29b087da7a00a643d7e822136.html#af7d6a2b29b087da7a00a643d7e822136) |
|  | |
| Initialization | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) bool | [IsInitialized](namespace_a_k_1_1_memory_mgr_a91028bc94037785fa186b827f81c59c9.html#a91028bc94037785fa186b827f81c59c9) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [Term](namespace_a_k_1_1_memory_mgr_a3ec018c61b5dc7428cf51f35f290739e.html#a3ec018c61b5dc7428cf51f35f290739e) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [InitForThread](namespace_a_k_1_1_memory_mgr_a76b450a2f472f5d9bc61aa1c3ed9a722.html#a76b450a2f472f5d9bc61aa1c3ed9a722) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [TermForThread](namespace_a_k_1_1_memory_mgr_a3c47d8b70c74b631184ad9ea34c6f942.html#a3c47d8b70c74b631184ad9ea34c6f942) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [TrimForThread](namespace_a_k_1_1_memory_mgr_a325a7f2aa771d1f25e280441cb77151d.html#a325a7f2aa771d1f25e280441cb77151d) () |
|  | |
| Memory Allocation | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [dMalloc](namespace_a_k_1_1_memory_mgr_a157a010cab9d463be18a871c350bd226.html#a157a010cab9d463be18a871c350bd226) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, size\_t in\_uSize, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [Malloc](namespace_a_k_1_1_memory_mgr_a8727fb3eaaefd366474f802b0467b296.html#a8727fb3eaaefd366474f802b0467b296) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, size\_t in\_uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [dRealloc](namespace_a_k_1_1_memory_mgr_ada579cbaf74944b6fb35d31d352bff66.html#ada579cbaf74944b6fb35d31d352bff66) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pAlloc, size\_t in\_uSize, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [Realloc](namespace_a_k_1_1_memory_mgr_a3713e20d272952a685bf42419a1dd6d3.html#a3713e20d272952a685bf42419a1dd6d3) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pAlloc, size\_t in\_uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [dReallocAligned](namespace_a_k_1_1_memory_mgr_ae966f222f7169c58b4d8be9e938fbf87.html#ae966f222f7169c58b4d8be9e938fbf87) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pAlloc, size\_t in\_uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAlignment, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [ReallocAligned](namespace_a_k_1_1_memory_mgr_a98fd48e4adafff36f44d6bf9be73bd41.html#a98fd48e4adafff36f44d6bf9be73bd41) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pAlloc, size\_t in\_uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [Free](namespace_a_k_1_1_memory_mgr_a6ee20149a37b11b31589c6f23f46db65.html#a6ee20149a37b11b31589c6f23f46db65) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, void \*in\_pMemAddress) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [dMalign](namespace_a_k_1_1_memory_mgr_a042b69a423f6f4ea43499898faf5ba22.html#a042b69a423f6f4ea43499898faf5ba22) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, size\_t in\_uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAlignment, const char \*in\_pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [Malign](namespace_a_k_1_1_memory_mgr_aeb57745b9cfdc88c9775e5bc504e9ab5.html#aeb57745b9cfdc88c9775e5bc504e9ab5) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, size\_t in\_uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAlignment) |
|  | |
| Memory Profiling | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [GetCategoryStats](namespace_a_k_1_1_memory_mgr_a4a00138319c6ee33a6a4c896cabcea34.html#a4a00138319c6ee33a6a4c896cabcea34) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_poolId, [CategoryStats](struct_a_k_1_1_memory_mgr_1_1_category_stats.html) &out\_poolStats) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [GetGlobalStats](namespace_a_k_1_1_memory_mgr_a49ab92c52b9afa8e034863f2cdd2209e.html#a49ab92c52b9afa8e034863f2cdd2209e) ([GlobalStats](struct_a_k_1_1_memory_mgr_1_1_global_stats.html) &out\_stats) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [StartProfileThreadUsage](namespace_a_k_1_1_memory_mgr_a83fc28efeaf65ff66ba6011d31f7db92.html#a83fc28efeaf65ff66ba6011d31f7db92) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [StopProfileThreadUsage](namespace_a_k_1_1_memory_mgr_ac01c971988f35fbbdd2db5ed8b056aee.html#ac01c971988f35fbbdd2db5ed8b056aee) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [DumpToFile](namespace_a_k_1_1_memory_mgr_a4f48ed6707ab2f2341f4a81f1c6053d7.html#a4f48ed6707ab2f2341f4a81f1c6053d7) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*pszFilename) |
|  | |
| C runtime allocator functions for the default implementation of the Memory Manager. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkCrtAllocatorInitForThread](namespace_a_k_1_1_memory_mgr_a6645815e0697b791b60526a3f70fb42e.html#a6645815e0697b791b60526a3f70fb42e) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkCrtAllocatorTermForThread](namespace_a_k_1_1_memory_mgr_a1acb8811956fffa587e6863a184453b6.html#a1acb8811956fffa587e6863a184453b6) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkCrtAllocatorTrimForThread](namespace_a_k_1_1_memory_mgr_a5fd7cb4149c6283dc291167adfcb0c57.html#a5fd7cb4149c6283dc291167adfcb0c57) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AkCrtAllocatorMalloc](namespace_a_k_1_1_memory_mgr_ae603bbd092159b47cd0070f6dbf11be9.html#ae603bbd092159b47cd0070f6dbf11be9) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AkCrtAllocatorMalign](namespace_a_k_1_1_memory_mgr_adeea01e87516b1fd6a2e7f262a18a9b5.html#adeea01e87516b1fd6a2e7f262a18a9b5) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AkCrtAllocatorRealloc](namespace_a_k_1_1_memory_mgr_aae39b6273ae26c0b3d6605ac26d7adeb.html#aae39b6273ae26c0b3d6605ac26d7adeb) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AkCrtAllocatorReallocAligned](namespace_a_k_1_1_memory_mgr_a16101187acdf633d289538dfaa3b913d.html#a16101187acdf633d289538dfaa3b913d) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkCrtAllocatorFree](namespace_a_k_1_1_memory_mgr_aaec597f9a062c0277c28811f84c83724.html#aaec597f9a062c0277c28811f84c83724) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) size\_t | [AkCrtAllocatorTotalReservedMemorySize](namespace_a_k_1_1_memory_mgr_aff92f964019ac1ea61d57430236edd6b.html#aff92f964019ac1ea61d57430236edd6b) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) size\_t | [AkCrtAllocatorSizeOfMemory](namespace_a_k_1_1_memory_mgr_ab9323deb02481ceb94f84bccbf08d895.html#ab9323deb02481ceb94f84bccbf08d895) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolID, void \*pAddress) |
|  | |
| Stomp allocator functions for the default implementation of the Memory Manager. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkStompAllocatorInitForThread](namespace_a_k_1_1_memory_mgr_a60813ec48d84794f18fe9d538ac1612b.html#a60813ec48d84794f18fe9d538ac1612b) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkStompAllocatorTermForThread](namespace_a_k_1_1_memory_mgr_a0e2f31d6093b1fa65f6b14e5c6a13918.html#a0e2f31d6093b1fa65f6b14e5c6a13918) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkStompAllocatorTrimForThread](namespace_a_k_1_1_memory_mgr_a8abc3b6b89ddca48ee265b37dfbb1c4f.html#a8abc3b6b89ddca48ee265b37dfbb1c4f) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AkStompAllocatorMalloc](namespace_a_k_1_1_memory_mgr_a43fbf3ad60d633b36475d2f919701a8a.html#a43fbf3ad60d633b36475d2f919701a8a) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AkStompAllocatorMalign](namespace_a_k_1_1_memory_mgr_aabd0b3c83d2576c1a87ae10540adb85c.html#aabd0b3c83d2576c1a87ae10540adb85c) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AkStompAllocatorRealloc](namespace_a_k_1_1_memory_mgr_a69c4f38513f2b025194eb7e2233b4f1c.html#a69c4f38513f2b025194eb7e2233b4f1c) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void \* | [AkStompAllocatorReallocAligned](namespace_a_k_1_1_memory_mgr_a38d5d3251e080fd46a1800883c3509e0.html#a38d5d3251e080fd46a1800883c3509e0) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkStompAllocatorFree](namespace_a_k_1_1_memory_mgr_ad448a46dbeae0468e3353b8694946a2e.html#ad448a46dbeae0468e3353b8694946a2e) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) size\_t | [AkStompAllocatorTotalReservedMemorySize](namespace_a_k_1_1_memory_mgr_a831351e6c479450087177c959e900d43.html#a831351e6c479450087177c959e900d43) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) size\_t | [AkStompAllocatorSizeOfMemory](namespace_a_k_1_1_memory_mgr_a34852e9379c1054ab549296f542672d5.html#a34852e9379c1054ab549296f542672d5) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolID, void \*pAddress) |
|  | |
| Debug tool hooks for the default implementation of the Memory Manager. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AkMemDebugToolInit](namespace_a_k_1_1_memory_mgr_a03bbb450e12edc46538cd67bc88d29ca.html#a03bbb450e12edc46538cd67bc88d29ca) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkMemDebugToolTerm](namespace_a_k_1_1_memory_mgr_a1fa86e5ab43e65f0171678c15d448937.html#a1fa86e5ab43e65f0171678c15d448937) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkMemDebugToolMalloc](namespace_a_k_1_1_memory_mgr_aeec807c4109c4a85ce5d77544e9ba622.html#aeec807c4109c4a85ce5d77544e9ba622) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, void \*pAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkMemDebugToolMalign](namespace_a_k_1_1_memory_mgr_ad1fd2b4fbef6955a828e44a4801ff3a6.html#ad1fd2b4fbef6955a828e44a4801ff3a6) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment, void \*pAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkMemDebugToolRealloc](namespace_a_k_1_1_memory_mgr_ac86fd9348f79d90b88b2ca58b4fb4566.html#ac86fd9348f79d90b88b2ca58b4fb4566) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pOldAddress, size\_t uSize, void \*pNewAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkMemDebugToolReallocAligned](namespace_a_k_1_1_memory_mgr_aea32c7d9da9ec853d6470afa5ea21ff9.html#aea32c7d9da9ec853d6470afa5ea21ff9) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pOldAddress, size\_t uSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uAlignment, void \*pNewAddress, char const \*pszFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLine) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkMemDebugToolFree](namespace_a_k_1_1_memory_mgr_a41c07407be7e9088666fca72981df6b6.html#a41c07407be7e9088666fca72981df6b6) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) poolId, void \*pAddress) |
|  | |

## 详细描述

Memory Manager namespace.

备注
:   The functions in this namespace are thread-safe, unless stated otherwise.

参见
:   - [Memory Manager](memorymanager.html)