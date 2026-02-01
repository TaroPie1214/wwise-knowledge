# FNVHash

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [FNVHash](class_a_k_1_1_f_n_v_hash.html)

[所有成员列表](class_a_k_1_1_f_n_v_hash-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods)

AK::FNVHash< HashParams > 模板类 参考

`#include <AkFNVHash.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [FNVHash](class_a_k_1_1_f_n_v_hash_a9ee1906e8dbf95ff3b98708c1b755ecd.html#a9ee1906e8dbf95ff3b98708c1b755ecd) (typename HashParams::HashType in\_uBase=HashParams::s\_offsetBasis) |
|  | Constructor [更多...](class_a_k_1_1_f_n_v_hash_a9ee1906e8dbf95ff3b98708c1b755ecd.html#a9ee1906e8dbf95ff3b98708c1b755ecd) |
|  | |
| HashParams::HashType | [Compute](class_a_k_1_1_f_n_v_hash_a907841bf37541824958d382686b1fb1f.html#a907841bf37541824958d382686b1fb1f) (const void \*in\_pData, typename HashParams::SizeType in\_dataSize) |
|  | |
| HashParams::HashType | [Get](class_a_k_1_1_f_n_v_hash_a45e3387db9391c12c3d93e66ebe5755f.html#a45e3387db9391c12c3d93e66ebe5755f) () const |
|  | |
| template<typename T > | |
| HashParams::HashType | [Compute](class_a_k_1_1_f_n_v_hash_a9408dd90cf3836ce3ce39370638a144b.html#a9408dd90cf3836ce3ce39370638a144b) (const T &in\_pData) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static HashParams::HashType | [ComputeLowerCase](class_a_k_1_1_f_n_v_hash_ac5d8db171c7e49452ff88bed5359b705.html#ac5d8db171c7e49452ff88bed5359b705) (const char \*in\_pData) |
|  | |

## 详细描述

### template<class HashParams> class AK::FNVHash< HashParams >

在文件 [AkFNVHash.h](_ak_f_n_v_hash_8h_source.html) 第 [73](_ak_f_n_v_hash_8h_source.html#l00073) 行定义.