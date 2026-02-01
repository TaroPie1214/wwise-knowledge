# IAkProcessorFeatures

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkProcessorFeatures](class_a_k_1_1_i_ak_processor_features.html)

[所有成员列表](class_a_k_1_1_i_ak_processor_features-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkProcessorFeatures类 参考abstract

`#include <IAkProcessorFeatures.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual bool | [GetSIMDSupport](class_a_k_1_1_i_ak_processor_features_a5dab631fc5196a65cc6b05433b35ae1f.html#a5dab631fc5196a65cc6b05433b35ae1f) ([AkSIMDProcessorSupport](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5c) in\_eSIMD)=0 |
|  | Query for specific SIMD instruction set support. See AkSIMDProcessorSupport for options. [更多...](class_a_k_1_1_i_ak_processor_features_a5dab631fc5196a65cc6b05433b35ae1f.html#a5dab631fc5196a65cc6b05433b35ae1f) |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetCacheSize](class_a_k_1_1_i_ak_processor_features_a056dfd4be668d3e023c808aaf90d8f40.html#a056dfd4be668d3e023c808aaf90d8f40) ()=0 |
|  | Query L2 cache size to optimize prefetching techniques where necessary. [更多...](class_a_k_1_1_i_ak_processor_features_a056dfd4be668d3e023c808aaf90d8f40.html#a056dfd4be668d3e023c808aaf90d8f40) |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetCacheLineSize](class_a_k_1_1_i_ak_processor_features_a87320aa0cd6962c85755138103662712.html#a87320aa0cd6962c85755138103662712) ()=0 |
|  | Query cache line size to optimize prefetching techniques where necessary. [更多...](class_a_k_1_1_i_ak_processor_features_a87320aa0cd6962c85755138103662712.html#a87320aa0cd6962c85755138103662712) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkProcessorFeatures](class_a_k_1_1_i_ak_processor_features_aeff3060a06a0319f7c0591483d59416e.html#aeff3060a06a0319f7c0591483d59416e) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_processor_features_aeff3060a06a0319f7c0591483d59416e.html#aeff3060a06a0319f7c0591483d59416e) |
|  | |

## 详细描述

Runtime processor supported features detection interface. Allows to query specific processor features to chose optimal implementation.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

在文件 [IAkProcessorFeatures.h](_i_ak_processor_features_8h_source.html) 第 [56](_i_ak_processor_features_8h_source.html#l00056) 行定义.