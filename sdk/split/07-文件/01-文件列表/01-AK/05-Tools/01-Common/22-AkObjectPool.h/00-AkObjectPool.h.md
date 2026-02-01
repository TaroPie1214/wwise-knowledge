# AkObjectPool.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members)

AkObjectPool.h 文件参考

`#include <AK/SoundEngine/Common/AkMemoryMgr.h>`  
`#include <AK/Tools/Common/AkAssert.h>`  
`#include <AK/Tools/Common/AkArray.h>`

[浏览源代码.](_ak_object_pool_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AK::ObjectPoolNoLock](struct_a_k_1_1_object_pool_no_lock.html) |
|  | |
| class | [AK::ObjectPool< T, AllocatorType, LockType >](class_a_k_1_1_object_pool.html) |
|  | An object pool of N reusable objects with one allocation. [更多...](class_a_k_1_1_object_pool.html#details) |
|  | |
| union | [AK::ObjectPool< T, AllocatorType, LockType >::DataType](union_a_k_1_1_object_pool_1_1_data_type.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_OBJECT\_POOL\_EXTRA\_SAFETY](_ak_object_pool_8h_a2bf426355465e84d6422898f5cf40116.html#a2bf426355465e84d6422898f5cf40116) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| template<AkMemID T\_MEMID = AkMemID\_Object> | |
| using | [AK::ObjectPoolDefaultAllocator](namespace_a_k_a49f274d9208c11d970455f216941da35.html#a49f274d9208c11d970455f216941da35) = [AkArrayAllocatorNoAlign](struct_ak_array_allocator_no_align.html)< T\_MEMID > |
|  | |
| using | [AK::ObjectPoolDefaultLockType](namespace_a_k_a0ef5c3d8da87adc2dcd94c3db68696fe.html#a0ef5c3d8da87adc2dcd94c3db68696fe) = ObjectPoolNoLock |
|  | |