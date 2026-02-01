# IAkPluginServiceHashTable

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceHashTable](class_a_k_1_1_i_ak_plugin_service_hash_table.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_hash_table-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginServiceHashTable类 参考abstract

`#include <IAkPluginHashTable.h>`

类 AK::IAkPluginServiceHashTable 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_hash_table.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [InitBase](class_a_k_1_1_i_ak_plugin_service_hash_table_ae424e69e8c1cd3e36c72c80d3786a36e.html#ae424e69e8c1cd3e36c72c80d3786a36e) ([AK::AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) > \*io\_pHashTable, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uInitialReserveCount, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uValueElementSize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uValueElementAlign)=0 |
|  | |
| virtual void | [Term](class_a_k_1_1_i_ak_plugin_service_hash_table_ac3c5159a2b68ed721ca9144154d4e050.html#ac3c5159a2b68ed721ca9144154d4e050) ([AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) > \*io\_pHashTable, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator)=0 |
|  | |
| virtual void | [Reset](class_a_k_1_1_i_ak_plugin_service_hash_table_a670988aad48a984b76c2efb4ba4bc671.html#a670988aad48a984b76c2efb4ba4bc671) ([AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) > \*io\_pHashTable)=0 |
|  | |
| virtual void \* | [AddKey](class_a_k_1_1_i_ak_plugin_service_hash_table_ac7048dd9905105fd4743dd5be1f58401.html#ac7048dd9905105fd4743dd5be1f58401) ([AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) > \*io\_pHashTable, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uKey)=0 |
|  | |
| virtual bool | [RemoveSlot](class_a_k_1_1_i_ak_plugin_service_hash_table_a433a14f892c33d678129db73e84d23e1.html#a433a14f892c33d678129db73e84d23e1) ([AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) > \*io\_pHashTable, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_iSlot)=0 |
|  | |
| virtual void | [RemoveKey](class_a_k_1_1_i_ak_plugin_service_hash_table_a2b56666f31f25472912f2bc4545a39f7.html#a2b56666f31f25472912f2bc4545a39f7) ([AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) > \*io\_pHashTable, [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uKey)=0 |
|  | |
| template<typename ValueType > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](class_a_k_1_1_i_ak_plugin_service_hash_table_a3972337ae9ebddbc15f098eb40bcd353.html#a3972337ae9ebddbc15f098eb40bcd353) ([AkHashTable](struct_a_k_1_1_ak_hash_table.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec), ValueType > \*io\_pHashTable, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uInitialReserveCount) |
|  | |
| template<typename KeyType , typename ValueType > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [TermValues](class_a_k_1_1_i_ak_plugin_service_hash_table_ae51ed5b51e41c02ed3d1a19fccb74601.html#ae51ed5b51e41c02ed3d1a19fccb74601) ([AkHashTable](struct_a_k_1_1_ak_hash_table.html)< KeyType, ValueType > \*io\_pHashTable, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator) |
|  | |
| template<typename KeyType , typename ValueType > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [AddKeyDefaultValue](class_a_k_1_1_i_ak_plugin_service_hash_table_a3e226f6ecdddd6f96e0329c078c6561f.html#a3e226f6ecdddd6f96e0329c078c6561f) ([AkHashTable](struct_a_k_1_1_ak_hash_table.html)< KeyType, ValueType > \*io\_pHashTable, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, KeyType in\_uKey) |
|  | |
| template<typename ValueType > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) ValueType \* | [AddKeyValue](class_a_k_1_1_i_ak_plugin_service_hash_table_ac940caf95a5b3b5f13d36d24452fe84f.html#ac940caf95a5b3b5f13d36d24452fe84f) ([AkHashTable](struct_a_k_1_1_ak_hash_table.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec), ValueType > \*io\_pHashTable, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uKey, ValueType \*in\_pNewValue) |
|  | |
| template<typename KeyType , typename ValueType > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [RemoveSlotValue](class_a_k_1_1_i_ak_plugin_service_hash_table_aae4423454df23ddd7a0328ab757e6534.html#aae4423454df23ddd7a0328ab757e6534) ([AkHashTable](struct_a_k_1_1_ak_hash_table.html)< KeyType, ValueType > \*io\_pHashTable, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_iSlotToRemove) |
|  | |
| template<typename KeyType , typename FuncType > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [RemoveIf](class_a_k_1_1_i_ak_plugin_service_hash_table_af99a07edc25e858f922666ff93b95138.html#af99a07edc25e858f922666ff93b95138) ([AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< KeyType > \*in\_pHashTable, FuncType in\_func) |
|  | |
| template<typename KeyType , typename ValueType , typename FuncType > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [RemoveIfValue](class_a_k_1_1_i_ak_plugin_service_hash_table_a2d2acdfa4f196c3dceced12caea02289.html#a2d2acdfa4f196c3dceced12caea02289) ([AkHashTable](struct_a_k_1_1_ak_hash_table.html)< KeyType, ValueType > \*in\_pHashTable, FuncType in\_func) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [GetFirstSlotByKey](class_a_k_1_1_i_ak_plugin_service_hash_table_a2187a6fe0c26fb9c5aa5f6a6bb76224f.html#a2187a6fe0c26fb9c5aa5f6a6bb76224f) ([AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) > \*in\_pHashTable, [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uKey) |
|  | |
| static [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [GetNextSlotByKey](class_a_k_1_1_i_ak_plugin_service_hash_table_afe5512383f0c4acd81f8ed7789d8a28a.html#afe5512383f0c4acd81f8ed7789d8a28a) ([AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html)< [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) > \*in\_pHashTable, [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uKey, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_iPreviousSlot) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServiceHashTable](class_a_k_1_1_i_ak_plugin_service_hash_table_a8e71a668b097ff15ca00f133eae6e649.html#a8e71a668b097ff15ca00f133eae6e649) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

## 详细描述

Interface for an open-addressed hash table (or key-value array). Relatively low-cost (O(1)) lookup, add, and removal by key. Typical use is to add values by key, and then using GetFirstSlotByKey (and GetNextSlotByKey, if keys are not guaranteed to be unique) to get a Slot into the [AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html), and then indexing [AkHashTableBase::pValues](struct_a_k_1_1_ak_hash_table_base_a220d8b552df2abe10b9460affeb97987.html#a220d8b552df2abe10b9460affeb97987) by the provided Slot.

Note that the [AkHashTableBase](struct_a_k_1_1_ak_hash_table_base.html) referred to is not inherently thread-safe, so appropriate protections will be required if the same hashTable is shared across multiple plug-in instances.

Some hash functions are provided in [AkMurMurHash.h](_ak_mur_mur_hash_8h.html) which can be used for key generation. In particular, this can be very useful for storing data on audio objects, or audio object channels, over time. Note that if indexing by object-channel is desired, GetObjectChannelHash is recommended to mitigate key-collisions from multiple channels of data. However, Audio Object IDs themselves are chaotic enough that they can be used directly.

在文件 [IAkPluginHashTable.h](_i_ak_plugin_hash_table_8h_source.html) 第 [57](_i_ak_plugin_hash_table_8h_source.html#l00057) 行定义.