# AkCmd_MuteBackgroundMusic

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___mute_background_music-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_MuteBackgroundMusic结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [isMuted](struct_ak_cmd___mute_background_music_a8efd4386b5947b41aa3908b137786019.html#a8efd4386b5947b41aa3908b137786019) |
|  | Whether to mute BGM busses. [更多...](struct_ak_cmd___mute_background_music_a8efd4386b5947b41aa3908b137786019.html#a8efd4386b5947b41aa3908b137786019) |
|  | |

## 详细描述

Mutes/Unmutes the busses tagged as background music.

This is automatically called for platforms that have user-music support. This command is provided to give the same behavior on platforms that don't have user-music support.

参见
:   - [AkCommand\_MuteBackgroundMusic](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda43238d249fbfc13a76ae8b2ed1eb3208 "See AkCmd_MuteBackgroundMusic")
    - [AK::SoundEngine::MuteBackgroundMusic](namespace_a_k_1_1_sound_engine_a90d1061ab02e2cfd6197a2ff704008ba.html#a90d1061ab02e2cfd6197a2ff704008ba)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1289](_ak_command_types_8h_source.html#l01289) 行定义.