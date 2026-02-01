# AkCmd_SA_SetAdjacentRoomBleed

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_adjacent_room_bleed-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetAdjacentRoomBleed结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [adjacentRoomBleed](struct_ak_cmd___s_a___set_adjacent_room_bleed_a46aa6cc8b74d1328fc60a34fbc3d7d4f.html#a46aa6cc8b74d1328fc60a34fbc3d7d4f) |
|  | |

## 详细描述

Set a global scaling factor that manipulates reverb send values. [AK::SpatialAudio::SetAdjacentRoomBleed](namespace_a_k_1_1_spatial_audio_acfd8b560df7015bbf1a2c747d4444d3a.html#acfd8b560df7015bbf1a2c747d4444d3a) affects the proportion of audio sent to adjacent rooms and to the emitter's current room. It updates the initialization setting specified in [AkSpatialAudioInitSettings::fAdjacentRoomBleed](struct_ak_spatial_audio_init_settings_ab75b8c41dbd117179bf344a469c7f5b1.html#ab75b8c41dbd117179bf344a469c7f5b1). This value is multiplied by [AkPortalParams::AdjacentRoomBleed](struct_ak_portal_params_a8cca592e2a38f8719b6e5a03eddecb07.html#a8cca592e2a38f8719b6e5a03eddecb07), which is used to scale reverb bleed for individual portals. When calculating reverb send amounts, each portal's aperture is multiplied by fAdjacentRoomBleed, which alters its perceived size:

- 1.0 (default): Maintains portals at their true geometric sizes (no scaling).
- > 1.0: Increases the perceived size of all portals, which increases bleed into adjacent rooms.
- < 1.0: Decreases the perceived size of all portals, which reduces bleed into adjacent rooms. Valid range: (0.0 - infinity) Note: Values close to 0 might cause abrupt portal transitions.

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1835](_ak_command_types_8h_source.html#l01835) 行定义.