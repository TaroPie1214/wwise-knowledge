# IAkProcessorFeatures.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[枚举](#enum-members)

IAkProcessorFeatures.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_i_ak_processor_features_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AK::IAkProcessorFeatures](class_a_k_1_1_i_ak_processor_features.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AK::AkSIMDProcessorSupport](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5c) {     [AK::AK\_SIMD\_SSE](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5caf5634c63e36cb39f0e8f2e01c1632df7) = 1<<0, [AK::AK\_SIMD\_SSE2](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5ca1f6f46bb22e80ff020f4b52c84571bfb) = 1<<1, [AK::AK\_SIMD\_SSE3](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5cad22ffc7d38dbcbaf9cdb5883bb37df1c) = 1<<2, [AK::AK\_SIMD\_SSSE3](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5ca8644ab1d1e7634ea60b4595d31b3391e) = 1<<3,     [AK::AK\_SIMD\_SSE41](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5caac3a9bd021d768d1a3c0e11cf460b3b5) = 1<<4, [AK::AK\_SIMD\_AVX](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5ca731521285223fc2a4028ca4479c7ee8d) = 1<<5, [AK::AK\_SIMD\_F16C](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5ca19aed2148535d6b4f84f55e8331c8939) = 1<<6, [AK::AK\_SIMD\_AVX2](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5cabf2734dd93274122b766de64369153bb) = 1<<7   } |
|  | SIMD instruction sets. [更多...](namespace_a_k_a84e4cdf72cca5ed7c8e890cedab91a5c.html#a84e4cdf72cca5ed7c8e890cedab91a5c) |
|  | |

## 详细描述

Runtime processor supported features detection interface.

在文件 [IAkProcessorFeatures.h](_i_ak_processor_features_8h_source.html) 中定义.