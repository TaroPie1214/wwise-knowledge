# AkCmd_SetRandomSeed

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_random_seed-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetRandomSeed结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [seedValue](struct_ak_cmd___set_random_seed_a80a6a5a6b7a90cab2c43144bdb27d92e.html#a80a6a5a6b7a90cab2c43144bdb27d92e) |
|  | Seed value to use for random number generation [更多...](struct_ak_cmd___set_random_seed_a80a6a5a6b7a90cab2c43144bdb27d92e.html#a80a6a5a6b7a90cab2c43144bdb27d92e) |
|  | |

## 详细描述

Sets the random seed value. Can be used to synchronize randomness across instances of the Sound Engine.

备注
:   This seeds the number generator used for all container randomization and the plug-in RNG; since it acts globally, this should be called right before any PostEvent call where randomness synchronization is required, and cannot guarantee similar results for continuous containers.

参见
:   - [AkCommand\_SetRandomSeed](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaaa8c84981c5163f6ac622e554b30b8f4 "See AkCmd_SetRandomSeed")
    - [AK::SoundEngine::SetRandomSeed](namespace_a_k_1_1_sound_engine_a78af1f6a2130a905d671ed372d7bd20e.html#a78af1f6a2130a905d671ed372d7bd20e)
    - [AK::IAkPluginServiceRNG](class_a_k_1_1_i_ak_plugin_service_r_n_g.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1218](_ak_command_types_8h_source.html#l01218) 行定义.