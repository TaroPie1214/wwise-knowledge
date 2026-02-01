# ObjectPool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [ObjectPool](class_a_k_1_1_object_pool.html)

[所有成员列表](class_a_k_1_1_object_pool-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[静态 Public 属性](#pub-static-attribs) |
[友元](#friends)

AK::ObjectPool< T, AllocatorType, LockType > 模板类 参考

An object pool of N reusable objects with one allocation.
[更多...](class_a_k_1_1_object_pool.html#details)

`#include <AkObjectPool.h>`

类 AK::ObjectPool< T, AllocatorType, LockType > 继承关系图:

![](../../../../images/class_a_k_1_1_object_pool.png)

|  |  |
| --- | --- |
| 类 | |
| union | [DataType](union_a_k_1_1_object_pool_1_1_data_type.html) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| using | [ValueType](class_a_k_1_1_object_pool_a4aa6fde6a154c29177c4f911400c2651.html#a4aa6fde6a154c29177c4f911400c2651) = T |
|  | |
| using | [SizeType](class_a_k_1_1_object_pool_a551d26b3bb09c7bad453cc0715beb65e.html#a551d26b3bb09c7bad453cc0715beb65e) = [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ObjectPool](class_a_k_1_1_object_pool_aa6e584903d61a50521090add2cb5113d.html#aa6e584903d61a50521090add2cb5113d) ()=default |
|  | |
|  | [ObjectPool](class_a_k_1_1_object_pool_a06034082691096e7b82fb16e4aaa6264.html#a06034082691096e7b82fb16e4aaa6264) (const [ObjectPool](class_a_k_1_1_object_pool.html) &)=delete |
|  | |
|  | [ObjectPool](class_a_k_1_1_object_pool_a24678463c14e7b22fb7a2403900f4364.html#a24678463c14e7b22fb7a2403900f4364) ([ObjectPool](class_a_k_1_1_object_pool.html) &&)=delete |
|  | |
|  | [~ObjectPool](class_a_k_1_1_object_pool_a85fc45eec73cfc6b2ffa503b943f0b13.html#a85fc45eec73cfc6b2ffa503b943f0b13) () |
|  | |
| [ObjectPool](class_a_k_1_1_object_pool.html) & | [operator=](class_a_k_1_1_object_pool_a30501c58aa89fd63c2fa4a320750486e.html#a30501c58aa89fd63c2fa4a320750486e) (const [ObjectPool](class_a_k_1_1_object_pool.html) &)=delete |
|  | |
| [ObjectPool](class_a_k_1_1_object_pool.html) & | [operator=](class_a_k_1_1_object_pool_ad2c29e54c7a451ee1a9974fa8bb12f43.html#ad2c29e54c7a451ee1a9974fa8bb12f43) ([ObjectPool](class_a_k_1_1_object_pool.html) &&)=delete |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](class_a_k_1_1_object_pool_a808833886b75207072ce599a3d180c1f.html#a808833886b75207072ce599a3d180c1f) ([SizeType](class_a_k_1_1_object_pool_a551d26b3bb09c7bad453cc0715beb65e.html#a551d26b3bb09c7bad453cc0715beb65e) count) |
|  | |
| void | [Term](class_a_k_1_1_object_pool_abc1ba97c0a68fcb4e64a4e00d59b64d3.html#abc1ba97c0a68fcb4e64a4e00d59b64d3) () |
|  | |
| [AK\_NODISCARD](_ak_platforms_8h_afdad98a324f1b63271ac05b0730074de.html#afdad98a324f1b63271ac05b0730074de) [SizeType](class_a_k_1_1_object_pool_a551d26b3bb09c7bad453cc0715beb65e.html#a551d26b3bb09c7bad453cc0715beb65e) | [Size](class_a_k_1_1_object_pool_ab7d50c2a8c38b7d92c8a9a10857ca124.html#ab7d50c2a8c38b7d92c8a9a10857ca124) () const |
|  | |
| [AK\_NODISCARD](_ak_platforms_8h_afdad98a324f1b63271ac05b0730074de.html#afdad98a324f1b63271ac05b0730074de) [SizeType](class_a_k_1_1_object_pool_a551d26b3bb09c7bad453cc0715beb65e.html#a551d26b3bb09c7bad453cc0715beb65e) | [Capacity](class_a_k_1_1_object_pool_a6e36f53d508071b0be075c7bd92b15c1.html#a6e36f53d508071b0be075c7bd92b15c1) () const |
|  | |
| [AK\_NODISCARD](_ak_platforms_8h_afdad98a324f1b63271ac05b0730074de.html#afdad98a324f1b63271ac05b0730074de) bool | [IsFull](class_a_k_1_1_object_pool_a4c7a0981ca800be7c953399dbf1dac58.html#a4c7a0981ca800be7c953399dbf1dac58) () const |
|  | |
| [AK\_NODISCARD](_ak_platforms_8h_afdad98a324f1b63271ac05b0730074de.html#afdad98a324f1b63271ac05b0730074de) bool | [IsEmpty](class_a_k_1_1_object_pool_abe277cd17b164b855b2059eb2701ef71.html#abe277cd17b164b855b2059eb2701ef71) () const |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Deallocate](class_a_k_1_1_object_pool_a7978bffb37a2a133f82c31a03b0a0bd4.html#a7978bffb37a2a133f82c31a03b0a0bd4) ([ValueType](class_a_k_1_1_object_pool_a4aa6fde6a154c29177c4f911400c2651.html#a4aa6fde6a154c29177c4f911400c2651) \*data) |
|  | |
| void | [Clear](class_a_k_1_1_object_pool_a02ab2dcc99715b6053c0bd92bc4867b3.html#a02ab2dcc99715b6053c0bd92bc4867b3) () |
|  | |
|  | |
| [AK\_NODISCARD](_ak_platforms_8h_afdad98a324f1b63271ac05b0730074de.html#afdad98a324f1b63271ac05b0730074de) [ValueType](class_a_k_1_1_object_pool_a4aa6fde6a154c29177c4f911400c2651.html#a4aa6fde6a154c29177c4f911400c2651) \* | [Allocate](class_a_k_1_1_object_pool_aa93fbdda70c41d1f6b17ac448bff61a2.html#aa93fbdda70c41d1f6b17ac448bff61a2) () |
|  | |
| [AK\_NODISCARD](_ak_platforms_8h_afdad98a324f1b63271ac05b0730074de.html#afdad98a324f1b63271ac05b0730074de) [ValueType](class_a_k_1_1_object_pool_a4aa6fde6a154c29177c4f911400c2651.html#a4aa6fde6a154c29177c4f911400c2651) \* | [AllocateZeroFilled](class_a_k_1_1_object_pool_adaa9ab3f8942187b5712ad22ebd1b693.html#adaa9ab3f8942187b5712ad22ebd1b693) () |
|  | Initialize memory before returning. [更多...](class_a_k_1_1_object_pool_adaa9ab3f8942187b5712ad22ebd1b693.html#adaa9ab3f8942187b5712ad22ebd1b693) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static constexpr [SizeType](class_a_k_1_1_object_pool_a551d26b3bb09c7bad453cc0715beb65e.html#a551d26b3bb09c7bad453cc0715beb65e) | [kInvalidIndex](class_a_k_1_1_object_pool_af8949e1516f74959ce27e31c0b6b5033.html#af8949e1516f74959ce27e31c0b6b5033) = ([SizeType](class_a_k_1_1_object_pool_a551d26b3bb09c7bad453cc0715beb65e.html#a551d26b3bb09c7bad453cc0715beb65e))-1 |
|  | |

|  |  |
| --- | --- |
| 友元 | |
| struct | [UnitTest::ObjectPoolHelper](class_a_k_1_1_object_pool_a78d42eb48b2c3b0d5ebbaae91144b548.html#a78d42eb48b2c3b0d5ebbaae91144b548) |
|  | |

## 详细描述

### template<typename T, typename AllocatorType = ObjectPoolDefaultAllocator<>, typename LockType = ObjectPoolDefaultLockType> class AK::ObjectPool< T, AllocatorType, LockType >

An object pool of N reusable objects with one allocation.

在文件 [AkObjectPool.h](_ak_object_pool_8h_source.html) 第 [60](_ak_object_pool_8h_source.html#l00060) 行定义.