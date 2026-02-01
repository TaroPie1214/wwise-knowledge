# CAkRng

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_c_ak_rng-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[静态 Public 属性](#pub-static-attribs)

CAkRng类 参考

`#include <AkRng.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [CAkRng](class_c_ak_rng_a4c89f3a730bbebfe617f2d423fd8e4f3.html#a4c89f3a730bbebfe617f2d423fd8e4f3) ([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) uSeed) |
|  | Initialize using the specified seed [更多...](class_c_ak_rng_a4c89f3a730bbebfe617f2d423fd8e4f3.html#a4c89f3a730bbebfe617f2d423fd8e4f3) |
|  | |
| [CAkRng](class_c_ak_rng.html) & | [operator=](class_c_ak_rng_ab4159301363bdbfd497daf42515e8fc0.html#ab4159301363bdbfd497daf42515e8fc0) (const [CAkRng](class_c_ak_rng.html) &in\_other) |
|  | Initialize using the specified instance [更多...](class_c_ak_rng_ab4159301363bdbfd497daf42515e8fc0.html#ab4159301363bdbfd497daf42515e8fc0) |
|  | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [Seed](class_c_ak_rng_ae8a8935ab43c13c7a545f62eb1a5a45b.html#ae8a8935ab43c13c7a545f62eb1a5a45b) () const |
|  | Returns the current seed value of the RNG [更多...](class_c_ak_rng_ae8a8935ab43c13c7a545f62eb1a5a45b.html#ae8a8935ab43c13c7a545f62eb1a5a45b) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Peek](class_c_ak_rng_a8003b5a6f3e2dfd158340b3f730590c6.html#a8003b5a6f3e2dfd158340b3f730590c6) () const |
|  | Returns the next random number to be generated without advancing the RNG state [更多...](class_c_ak_rng_a8003b5a6f3e2dfd158340b3f730590c6.html#a8003b5a6f3e2dfd158340b3f730590c6) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Random](class_c_ak_rng_a151fe7c46d42fa6be12bc35ab75bd401.html#a151fe7c46d42fa6be12bc35ab75bd401) () |
|  | Returns a random 31-bit unsigned integer [更多...](class_c_ak_rng_a151fe7c46d42fa6be12bc35ab75bd401.html#a151fe7c46d42fa6be12bc35ab75bd401) |
|  | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [RandomInt](class_c_ak_rng_a4d353eb5fe124835614a850994ba8488.html#a4d353eb5fe124835614a850994ba8488) () |
|  | Returns a random 31-bit integer [更多...](class_c_ak_rng_a4d353eb5fe124835614a850994ba8488.html#a4d353eb5fe124835614a850994ba8488) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [RandomFloat](class_c_ak_rng_ae5fab1ba7576ef969d308520de815fb8.html#ae5fab1ba7576ef969d308520de815fb8) () |
|  | Returns a random float from 0.0 to 1.0 [更多...](class_c_ak_rng_ae5fab1ba7576ef969d308520de815fb8.html#ae5fab1ba7576ef969d308520de815fb8) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [Random](class_c_ak_rng_ae4e2d0b265568012366166666aa26e41.html#ae4e2d0b265568012366166666aa26e41) ([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) &io\_uSeed) |
|  | Returns a random 31-bit unsigned integer using provided seed [更多...](class_c_ak_rng_ae4e2d0b265568012366166666aa26e41.html#ae4e2d0b265568012366166666aa26e41) |
|  | |
| static [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [RandomInt](class_c_ak_rng_a69018b1343fda1f7ae5b5406fb17abca.html#a69018b1343fda1f7ae5b5406fb17abca) ([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) &io\_uSeed) |
|  | Returns a random 31-bit integer using provided seed [更多...](class_c_ak_rng_a69018b1343fda1f7ae5b5406fb17abca.html#a69018b1343fda1f7ae5b5406fb17abca) |
|  | |
| static [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [RandomFloat](class_c_ak_rng_a3cde751ddc61736e23506aaa9739ed4c.html#a3cde751ddc61736e23506aaa9739ed4c) ([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) &io\_uSeed) |
|  | |
| static [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Peek](class_c_ak_rng_ac26d65c30639f5b67d4a9b7034540533.html#ac26d65c30639f5b67d4a9b7034540533) ([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uSeed) |
|  | Returns the next random number to be generated without advancing the RNG state [更多...](class_c_ak_rng_ac26d65c30639f5b67d4a9b7034540533.html#ac26d65c30639f5b67d4a9b7034540533) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static constexpr [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [RANDOM\_A](class_c_ak_rng_a0bdefd170fc2b036de1f2967bfd8c6fd.html#a0bdefd170fc2b036de1f2967bfd8c6fd) = 6364136223846793005ULL |
|  | |
| static constexpr [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [RANDOM\_C](class_c_ak_rng_abb969faf0174fd790c8bd2923f435ff8.html#abb969faf0174fd790c8bd2923f435ff8) = 1 |
|  | |
| static constexpr [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [RANDOM\_MAX](class_c_ak_rng_a8e04b9d014adc145bcbf98392083c53a.html#a8e04b9d014adc145bcbf98392083c53a) = 0x7FFFFFFF |
|  | |

## 详细描述

A pseudorandom number generator appropriate for introducing randomness in DSP processing LCG with Newlib/Musl characteristics: 64-bit seed, 31-bit output (see <http://en.wikipedia.org/wiki/Linear_congruential_generator>) Warning: This RNG is not cryptographically secure! Do not use it as such!

在文件 [AkRng.h](_ak_rng_8h_source.html) 第 [34](_ak_rng_8h_source.html#l00034) 行定义.