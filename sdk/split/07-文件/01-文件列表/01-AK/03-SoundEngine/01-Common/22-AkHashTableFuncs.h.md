# AkHashTableFuncs.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[命名空间](#namespaces) |
[函数](#func-members)

AkHashTableFuncs.h 文件参考

`#include <AK/SoundEngine/Common/AkHashTableTypes.h>`  
`#include <AK/Tools/Common/AkBitFuncs.h>`

[浏览源代码.](_ak_hash_table_funcs_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::HashTable](namespace_a_k_1_1_hash_table.html) |
|  | |
|  | [AK::HashTable::Internal](namespace_a_k_1_1_hash_table_1_1_internal.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AK::HashTable::Internal::IdealPos](namespace_a_k_1_1_hash_table_1_1_internal_a3fcf5f0480e1b1e5f7d38eb40c5884b4.html#a3fcf5f0480e1b1e5f7d38eb40c5884b4) (KeyType uKey, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iEntriesMask) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AK::HashTable::Internal::DistanceFromIdealPos](namespace_a_k_1_1_hash_table_1_1_internal_a4d541f80ffc5fd764459afa2c1f64be9.html#a4d541f80ffc5fd764459afa2c1f64be9) ([AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iSlot, KeyType uKey, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iEntriesMask) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AK::HashTable::Internal::LinearProbe](namespace_a_k_1_1_hash_table_1_1_internal_ac859a976e20919ad2f3b8e6180df3a9f.html#ac859a976e20919ad2f3b8e6180df3a9f) (const KeyType \*pKeys, const bool \*pbSlotOccupied, KeyType uKey, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iSlot, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uNumEntries) |
|  | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AK::HashTable::Internal::OccupiedProbe](namespace_a_k_1_1_hash_table_1_1_internal_a6f56f65e68e40dabf172a547a3aeb8ab.html#a6f56f65e68e40dabf172a547a3aeb8ab) (const bool \*pbSlotOccupied, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iSlot, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iNumEntries) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AK::HashTable::GetFirstSlotForKey](namespace_a_k_1_1_hash_table_ab9789c231d0735875283ce8bb5996e83.html#ab9789c231d0735875283ce8bb5996e83) (const AkHashTableBase< KeyType > \*pHashTable, KeyType uKey) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AK::HashTable::GetNextSlotForKey](namespace_a_k_1_1_hash_table_ad3f4e7781c7ef2de6b0c4d9d1c0f5b1b.html#ad3f4e7781c7ef2de6b0c4d9d1c0f5b1b) (const AkHashTableBase< KeyType > \*pHashTable, KeyType uKey, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iPreviousSlot) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AK::HashTable::GetFirstActiveSlot](namespace_a_k_1_1_hash_table_a4503d36f93ee060e51c96b963452f9b4.html#a4503d36f93ee060e51c96b963452f9b4) (const AkHashTableBase< KeyType > \*pHashTable) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AK::HashTable::GetNextActiveSlot](namespace_a_k_1_1_hash_table_a85aeb41beffb5612e9d0c3d6c6bbcc3e.html#a85aeb41beffb5612e9d0c3d6c6bbcc3e) (const AkHashTableBase< KeyType > \*pHashTable, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iPreviousSlot) |
|  | |
| template<typename KeyType , typename FuncType > | |
| void | [AK::HashTable::ForEachSlot](namespace_a_k_1_1_hash_table_a9eda4405296b8c26fe3c0b9ced4a63d5.html#a9eda4405296b8c26fe3c0b9ced4a63d5) (const AkHashTableBase< KeyType > \*in\_pHashTable, FuncType in\_func) |
|  | |