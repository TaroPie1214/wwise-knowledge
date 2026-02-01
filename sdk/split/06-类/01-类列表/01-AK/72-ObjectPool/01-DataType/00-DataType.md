# DataType

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [ObjectPool](class_a_k_1_1_object_pool.html)
- [DataType](union_a_k_1_1_object_pool_1_1_data_type.html)

[所有成员列表](union_a_k_1_1_object_pool_1_1_data_type-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK::ObjectPool< T, AllocatorType, LockType >::DataType联合体 参考

`#include <AkObjectPool.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| [ValueType](class_a_k_1_1_object_pool_a4aa6fde6a154c29177c4f911400c2651.html#a4aa6fde6a154c29177c4f911400c2651) & | [Data](union_a_k_1_1_object_pool_1_1_data_type_aa9ad651965e5b1dbcaab5d3215fe80e9.html#aa9ad651965e5b1dbcaab5d3215fe80e9) () |
|  | |
| const [ValueType](class_a_k_1_1_object_pool_a4aa6fde6a154c29177c4f911400c2651.html#a4aa6fde6a154c29177c4f911400c2651) & | [Data](union_a_k_1_1_object_pool_1_1_data_type_a22a092cfc7a94e9af357e3a726890b06.html#a22a092cfc7a94e9af357e3a726890b06) () const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| uint8\_t | [data](union_a_k_1_1_object_pool_1_1_data_type_a2743b93469ff4e133f10ba61938e84d1.html#a2743b93469ff4e133f10ba61938e84d1) [sizeof([ValueType](class_a_k_1_1_object_pool_a4aa6fde6a154c29177c4f911400c2651.html#a4aa6fde6a154c29177c4f911400c2651))] |
|  | |
| [SizeType](class_a_k_1_1_object_pool_a551d26b3bb09c7bad453cc0715beb65e.html#a551d26b3bb09c7bad453cc0715beb65e) | [next](union_a_k_1_1_object_pool_1_1_data_type_a48720c92d1783a80d5eb59cf1d2847f9.html#a48720c92d1783a80d5eb59cf1d2847f9) |
|  | |

## 详细描述

### template<typename T, typename AllocatorType = ObjectPoolDefaultAllocator<>, typename LockType = ObjectPoolDefaultLockType> union AK::ObjectPool< T, AllocatorType, LockType >::DataType

在文件 [AkObjectPool.h](_ak_object_pool_8h_source.html) 第 [67](_ak_object_pool_8h_source.html#l00067) 行定义.