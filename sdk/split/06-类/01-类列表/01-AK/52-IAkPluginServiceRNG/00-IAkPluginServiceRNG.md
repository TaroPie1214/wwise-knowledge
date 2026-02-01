# IAkPluginServiceRNG

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceRNG](class_a_k_1_1_i_ak_plugin_service_r_n_g.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_r_n_g-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginServiceRNG类 参考abstract

`#include <IAkPlugin.h>`

类 AK::IAkPluginServiceRNG 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_r_n_g.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [RandomSeed](class_a_k_1_1_i_ak_plugin_service_r_n_g_a1f71793e4249802c70337bbedaa312ed.html#a1f71793e4249802c70337bbedaa312ed) () const =0 |
|  | |
| virtual [CAkRng](class_c_ak_rng.html) | [CreateRNG](class_a_k_1_1_i_ak_plugin_service_r_n_g_ae267909ad06df7f0f2c2c1b138e5864e.html#ae267909ad06df7f0f2c2c1b138e5864e) () const =0 |
|  | Advances the internal PRNG seed, and returns a random number generator suitable for DSP processing [更多...](class_a_k_1_1_i_ak_plugin_service_r_n_g_ae267909ad06df7f0f2c2c1b138e5864e.html#ae267909ad06df7f0f2c2c1b138e5864e) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServiceRNG](class_a_k_1_1_i_ak_plugin_service_r_n_g_ab19a8cefe9bfbbb9d530f13cae6b6d50.html#ab19a8cefe9bfbbb9d530f13cae6b6d50) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

## 详细描述

Interface for the services related to generating pseudorandom numbers

参见
:   - `AK::SoundEngine::SetRandomSeed()`
    - `CAkRng`

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1855](_i_ak_plugin_8h_source.html#l01855) 行定义.