# HashTable

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [HashTable](namespace_a_k_1_1_hash_table.html)

[命名空间](#namespaces) |
[函数](#func-members)

AK::HashTable 命名空间参考

|  |  |
| --- | --- |
| 命名空间 | |
|  | [Internal](namespace_a_k_1_1_hash_table_1_1_internal.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [GetFirstSlotForKey](namespace_a_k_1_1_hash_table_ab9789c231d0735875283ce8bb5996e83.html#ab9789c231d0735875283ce8bb5996e83) (const [AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< KeyType > \*pHashTable, KeyType uKey) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [GetNextSlotForKey](namespace_a_k_1_1_hash_table_ad3f4e7781c7ef2de6b0c4d9d1c0f5b1b.html#ad3f4e7781c7ef2de6b0c4d9d1c0f5b1b) (const [AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< KeyType > \*pHashTable, KeyType uKey, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iPreviousSlot) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [GetFirstActiveSlot](namespace_a_k_1_1_hash_table_a4503d36f93ee060e51c96b963452f9b4.html#a4503d36f93ee060e51c96b963452f9b4) (const [AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< KeyType > \*pHashTable) |
|  | |
| template<typename KeyType > | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [GetNextActiveSlot](namespace_a_k_1_1_hash_table_a85aeb41beffb5612e9d0c3d6c6bbcc3e.html#a85aeb41beffb5612e9d0c3d6c6bbcc3e) (const [AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< KeyType > \*pHashTable, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) iPreviousSlot) |
|  | |
| template<typename KeyType , typename FuncType > | |
| void | [ForEachSlot](namespace_a_k_1_1_hash_table_a9eda4405296b8c26fe3c0b9ced4a63d5.html#a9eda4405296b8c26fe3c0b9ced4a63d5) (const [AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< KeyType > \*in\_pHashTable, FuncType in\_func) |
|  | |