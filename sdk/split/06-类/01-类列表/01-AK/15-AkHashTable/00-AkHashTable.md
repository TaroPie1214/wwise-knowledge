# AkHashTable

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [AkHashTable](struct_a_k_1_1_ak_hash_table.html)

[所有成员列表](struct_a_k_1_1_ak_hash_table-members.html) |
[Public 成员函数](#pub-methods)

AK::AkHashTable< KeyType, ValueType > 模板结构体 参考

`#include <AkHashTableTypes.h>`

类 AK::AkHashTable< KeyType, ValueType > 继承关系图:

![](../../../../images/struct_a_k_1_1_ak_hash_table.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| KeyType | [KeyAt](struct_a_k_1_1_ak_hash_table_afa483e63e5333dbe4f0242865fed925c.html#afa483e63e5333dbe4f0242865fed925c) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uSlot) const |
|  | |
| ValueType \* | [ValueData](struct_a_k_1_1_ak_hash_table_a287574db57ca9d8e44fdb6e20be89d04.html#a287574db57ca9d8e44fdb6e20be89d04) () |
|  | |
| const ValueType \* | [ValueData](struct_a_k_1_1_ak_hash_table_a20ff4d1fdca5bee828f6f774cf24bd9f.html#a20ff4d1fdca5bee828f6f774cf24bd9f) () const |
|  | |
| ValueType & | [ValueAt](struct_a_k_1_1_ak_hash_table_af2c43395012ad844876c291e211d49c9.html#af2c43395012ad844876c291e211d49c9) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uSlot) |
|  | |
| const ValueType & | [ValueAt](struct_a_k_1_1_ak_hash_table_a2ae06f29164fef3d4dbd61b33d4b0d97.html#a2ae06f29164fef3d4dbd61b33d4b0d97) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uSlot) const |
|  | |
| - Public 成员函数 继承自 [AK::AkHashTableBase< KeyType >](struct_a_k_1_1_ak_hash_table_base.html) | |
|  | [AkHashTableBase](struct_a_k_1_1_ak_hash_table_base_affecf0ee6e8d833cba75749c40d0add1.html#affecf0ee6e8d833cba75749c40d0add1) () |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 属性 继承自 [AK::AkHashTableBase< KeyType >](struct_a_k_1_1_ak_hash_table_base.html) | |
| KeyType \* | [pKeys](struct_a_k_1_1_ak_hash_table_base_ae60323725e01c40d0c548d0608d32efc.html#ae60323725e01c40d0c548d0608d32efc) |
|  | |
| bool \* | [pbSlotOccupied](struct_a_k_1_1_ak_hash_table_base_a091265372c298d4bbff4bf3af2dc37a6.html#a091265372c298d4bbff4bf3af2dc37a6) |
|  | |
| void \* | [pValues](struct_a_k_1_1_ak_hash_table_base_a220d8b552df2abe10b9460affeb97987.html#a220d8b552df2abe10b9460affeb97987) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumReservedEntries](struct_a_k_1_1_ak_hash_table_base_a49ea451199605326540f0f2d1e8e81a6.html#a49ea451199605326540f0f2d1e8e81a6) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumUsedEntries](struct_a_k_1_1_ak_hash_table_base_a9962878cb69fae1717f2eb3423cb7a79.html#a9962878cb69fae1717f2eb3423cb7a79) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [uValueElementSize](struct_a_k_1_1_ak_hash_table_base_abd7f42e1328a3f9b2eb903a3a0b2c517.html#abd7f42e1328a3f9b2eb903a3a0b2c517) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [uValueElementAlign](struct_a_k_1_1_ak_hash_table_base_ae9ee625cc39adda2b81571bccca0b39f.html#ae9ee625cc39adda2b81571bccca0b39f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxLoadFactor](struct_a_k_1_1_ak_hash_table_base_ac912f5e234706b0fb85c7f52e04f1485.html#ac912f5e234706b0fb85c7f52e04f1485) |
|  | |
| - 静态 Public 属性 继承自 [AK::AkHashTableBase< KeyType >](struct_a_k_1_1_ak_hash_table_base.html) | |
| static const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [kDefaultMaxLoadFactor](struct_a_k_1_1_ak_hash_table_base_acbfd1b61dde29099005b6c8a3f0c460f.html#acbfd1b61dde29099005b6c8a3f0c460f) = 28 |
|  | |

## 详细描述

### template<typename KeyType, typename ValueType> struct AK::AkHashTable< KeyType, ValueType >

在文件 [AkHashTableTypes.h](_ak_hash_table_types_8h_source.html) 第 [56](_ak_hash_table_types_8h_source.html#l00056) 行定义.