# AkObject.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[宏定义](#define-members) |
[函数](#func-members)

AkObject.h 文件参考

`#include <AK/SoundEngine/Common/AkMemoryMgr.h>`

[浏览源代码.](_ak_object_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkPoolNewKey](struct_ak_pool_new_key.html) |
|  | Unique structure identifier for AkNew. [更多...](struct_ak_pool_new_key.html#details) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AkNew](_ak_object_8h_a3232c49fa8b5e6c07e7b49b8c45dac8b.html#a3232c49fa8b5e6c07e7b49b8c45dac8b)(\_pool, \_what)   new( ( \_pool ), [AkPoolNewKey](struct_ak_pool_new_key.html)() ) \_what |
|  | |
| #define | [AkAlloc](_ak_object_8h_a81a766551b19dc3e9dd2909d9db75c21.html#a81a766551b19dc3e9dd2909d9db75c21)(\_pool, \_size)   ( [AK::MemoryMgr::Malloc](namespace_a_k_1_1_memory_mgr_a8727fb3eaaefd366474f802b0467b296.html#a8727fb3eaaefd366474f802b0467b296)( ( \_pool ), \_size ) ) |
|  | |
| #define | [AkMalign](_ak_object_8h_a568392e5766ed6e2916c2bc86be8f258.html#a568392e5766ed6e2916c2bc86be8f258)(\_pool, \_size, \_align)   ( [AK::MemoryMgr::Malign](namespace_a_k_1_1_memory_mgr_aeb57745b9cfdc88c9775e5bc504e9ab5.html#aeb57745b9cfdc88c9775e5bc504e9ab5)( ( \_pool ), \_size, \_align ) ) |
|  | |
| #define | [AkNewAligned](_ak_object_8h_adc4fd9ae253acec45f1324fba30ebb3a.html#adc4fd9ae253acec45f1324fba30ebb3a)(\_pool, \_what, \_align)   new( ( \_pool ), [AkPoolNewKey](struct_ak_pool_new_key.html)(), ( \_align ) ) \_what |
|  | |
| #define | [AkRealloc](_ak_object_8h_ad15cb498600928fc9a63d2a4adda3490.html#ad15cb498600928fc9a63d2a4adda3490)(\_pool, \_pvmem, \_size)   ( [AK::MemoryMgr::Realloc](namespace_a_k_1_1_memory_mgr_a3713e20d272952a685bf42419a1dd6d3.html#a3713e20d272952a685bf42419a1dd6d3)( ( \_pool ), \_pvmem, \_size ) ) |
|  | |
| #define | [AkReallocAligned](_ak_object_8h_a075b63a4313277d88057619150cc503d.html#a075b63a4313277d88057619150cc503d)(\_pool, \_pvmem, \_size, \_align)   ( [AK::MemoryMgr::ReallocAligned](namespace_a_k_1_1_memory_mgr_a98fd48e4adafff36f44d6bf9be73bd41.html#a98fd48e4adafff36f44d6bf9be73bd41)( ( \_pool ), \_pvmem, \_size, \_align ) ) |
|  | |
| #define | [AkFree](_ak_object_8h_a1784988d683276fbd869d74a32edece8.html#a1784988d683276fbd869d74a32edece8)(\_pool, \_pvmem)   ( [AK::MemoryMgr::Free](namespace_a_k_1_1_memory_mgr_a6ee20149a37b11b31589c6f23f46db65.html#a6ee20149a37b11b31589c6f23f46db65)( ( \_pool ), ( \_pvmem ) ) ) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [operator new](_ak_object_8h_a7ef810d4ed6f6f822407c7da13fcd967.html#a7ef810d4ed6f6f822407c7da13fcd967) (size\_t size, [AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_PoolId, const [AkPoolNewKey](struct_ak_pool_new_key.html) &) throw () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [operator new](_ak_object_8h_a69c45660b40ef76d6a49366f0a84161b.html#a69c45660b40ef76d6a49366f0a84161b) (size\_t size, [AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_PoolId, const [AkPoolNewKey](struct_ak_pool_new_key.html) &, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_align) throw () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [operator delete](_ak_object_8h_ad43dbfb8bd0a5967eb6c2acc7da7335a.html#ad43dbfb8bd0a5967eb6c2acc7da7335a) (void \*, [AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696), const [AkPoolNewKey](struct_ak_pool_new_key.html) &) throw () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [operator delete](_ak_object_8h_a941979a41619e0cd49d0202c83887063.html#a941979a41619e0cd49d0202c83887063) (void \*, [AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696), const [AkPoolNewKey](struct_ak_pool_new_key.html) &, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)) throw () |
|  | |
| template<class T > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AkDelete](_ak_object_8h_a0e554314420ea8da3c2690e0fd56f259.html#a0e554314420ea8da3c2690e0fd56f259) ([AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) in\_PoolId, T \*in\_pObject) |
|  | |