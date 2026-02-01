# AkCmd_SA_SetMaxEmitterRoomAuxSends

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_max_emitter_room_aux_sends-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetMaxEmitterRoomAuxSends结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [maxEmitterRoomAuxSends](struct_ak_cmd___s_a___set_max_emitter_room_aux_sends_a479c68a9943b10842cd2588a4b9eb175.html#a479c68a9943b10842cd2588a4b9eb175) |
|  | The maximum number of room aux send connections. [更多...](struct_ak_cmd___s_a___set_max_emitter_room_aux_sends_a479c68a9943b10842cd2588a4b9eb175.html#a479c68a9943b10842cd2588a4b9eb175) |
|  | |

## 详细描述

Set the maximum number of game-defined auxiliary sends that can originate from a single emitter. Set to 1 to only allow emitters to send directly to their current room. Set to 0 to disable the limit.

参见
:   - [AkCommand\_SA\_SetMaxEmitterRoomAuxSends](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda9a691fd3b8c9725ae922cd41b8b9a980)
    - [AkSpatialAudioInitSettings::uMaxEmitterRoomAuxSends](struct_ak_spatial_audio_init_settings_a733e7d1ef6c4bf44af5bd55369ab4a3f.html#a733e7d1ef6c4bf44af5bd55369ab4a3f)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1883](_ak_command_types_8h_source.html#l01883) 行定义.