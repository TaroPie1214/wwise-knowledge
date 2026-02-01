# Internal

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [HashTable](namespace_a_k_1_1_hash_table.html)
- [Internal](namespace_a_k_1_1_hash_table_1_1_internal.html)

[函数](#func-members)

AK::HashTable::Internal 命名空间参考

|  |  |
| --- | --- |
| 函数 | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [IdealPos](namespace_a_k_1_1_hash_table_1_1_internal_a3fcf5f0480e1b1e5f7d38eb40c5884b4.html#a3fcf5f0480e1b1e5f7d38eb40c5884b4) (KeyType uKey, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iEntriesMask) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [DistanceFromIdealPos](namespace_a_k_1_1_hash_table_1_1_internal_a4d541f80ffc5fd764459afa2c1f64be9.html#a4d541f80ffc5fd764459afa2c1f64be9) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iSlot, KeyType uKey, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iEntriesMask) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [LinearProbe](namespace_a_k_1_1_hash_table_1_1_internal_ac859a976e20919ad2f3b8e6180df3a9f.html#ac859a976e20919ad2f3b8e6180df3a9f) (const KeyType \*pKeys, const bool \*pbSlotOccupied, KeyType uKey, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iSlot, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uNumEntries) |
|  | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [OccupiedProbe](namespace_a_k_1_1_hash_table_1_1_internal_a6f56f65e68e40dabf172a547a3aeb8ab.html#a6f56f65e68e40dabf172a547a3aeb8ab) (const bool \*pbSlotOccupied, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iSlot, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iNumEntries) |
|  | |