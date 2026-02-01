# AkSet.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[类型定义](#typedef-members) |
[枚举](#enum-members) |
[函数](#func-members)

AkSet.h 文件参考

`#include <AK/Tools/Common/AkKeyArray.h>`  
`#include "AK/SoundEngine/Common/IAkPluginMemAlloc.h"`

[浏览源代码.](_ak_set_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkSetGetKey< T >](struct_ak_set_get_key.html) |
|  | |
| class | [AkSet< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy >](class_ak_set.html) |
|  | |
| class | [AkBookmarkSet< T, TMovePolicy, TComparePolicy >](class_ak_bookmark_set.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AkSet](class_ak_set.html)< [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc), [ArrayPoolDefault](_ak_array_8h_a6d1995f92ec49c35784181225575438f.html#a6d1995f92ec49c35784181225575438f) > | [AkUniqueIDSet](_ak_set_8h_a6829125da7c5537eacefe74765dcbf7d.html#a6829125da7c5537eacefe74765dcbf7d) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AkSetType](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546e) { [SetType\_Inclusion](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546ea900113ca6f53350456b0cfb9ad0c70e8), [SetType\_Exclusion](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546ead2efae98bf2504b9c317ece9f2fbdc03) } |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| template<typename T , class U\_POOL = ArrayPoolDefault, class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkDisjoint](_ak_set_8h_a93f242be5040cd729ebd0c1a6a597a87.html#a93f242be5040cd729ebd0c1a6a597a87) (const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_A, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkIntersect](_ak_set_8h_a0cfc7eedd292b5d7212aaadf5d9bf54e.html#a0cfc7eedd292b5d7212aaadf5d9bf54e) (const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_A, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkIsSubset](_ak_set_8h_ab7771a1c98af35de43a62c398a45a3df.html#ab7771a1c98af35de43a62c398a45a3df) (const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_A, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkCountIntersection](_ak_set_8h_adced28c4ecf1f27b9f49ebd3a32abc7f.html#adced28c4ecf1f27b9f49ebd3a32abc7f) (const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_A, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkSubtraction](_ak_set_8h_afb6a51ce8a6d0fbc9c2b033eb0557a2f.html#afb6a51ce8a6d0fbc9c2b033eb0557a2f) ([AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_A, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkIntersection](_ak_set_8h_ab7b42b72f413fd7ed51c87391fcff279.html#ab7b42b72f413fd7ed51c87391fcff279) ([AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_A, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkIntersection](_ak_set_8h_adbd65c260407d0fd7b1e4a89afd4176c.html#adbd65c260407d0fd7b1e4a89afd4176c) ([AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &out\_res, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_A, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkUnion](_ak_set_8h_ae67052a5b2e873e9be61169b7d7c3e22.html#ae67052a5b2e873e9be61169b7d7c3e22) ([AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &io\_A, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkIntersect](_ak_set_8h_a7d7ac1a2d4c988ca461a2d873a8106fa.html#a7d7ac1a2d4c988ca461a2d873a8106fa) (const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_A, [AkSetType](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546e) in\_typeA, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B, [AkSetType](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546e) in\_typeB) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkContains](_ak_set_8h_ad44b52a7951cc067e7f022bc6225e2b2.html#ad44b52a7951cc067e7f022bc6225e2b2) (const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_Set, [AkSetType](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546e) in\_type, T in\_item) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkSubtraction](_ak_set_8h_a017ff356d259bcb0471fdc8671de695a.html#a017ff356d259bcb0471fdc8671de695a) ([AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_A, [AkSetType](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546e) in\_typeA, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B, [AkSetType](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546e) in\_typeB) |
|  | |
| template<typename T , class U\_POOL , class uGrowBy , class TMovePolicy , class TComparePolicy > | |
| static bool | [AkUnion](_ak_set_8h_a983590cb64c222d079503fdf3b0c0c1e.html#a983590cb64c222d079503fdf3b0c0c1e) ([AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &io\_A, [AkSetType](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546e) &io\_typeA, const [AkSet](class_ak_set.html)< T, U\_POOL, uGrowBy, TMovePolicy, TComparePolicy > &in\_B, [AkSetType](_ak_set_8h_a72fcdc17f16750967d9a4ee5d106546e.html#a72fcdc17f16750967d9a4ee5d106546e) in\_typeB) |
|  | |