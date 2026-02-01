# AkCmd_ResetGlobalValues

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___reset_global_values-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ResetGlobalValues结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [unused](struct_ak_cmd___reset_global_values_a245b81ba81d24b8b1efd8d4bbcc38495.html#a245b81ba81d24b8b1efd8d4bbcc38495) |
|  | |

## 详细描述

Resets all global changes made to the sound engine. This includes:

- States
- RTPCs in the global scope
- Changes made on sound object by Event Actions like Set Volume, Set Pitch, etc or equivalent API calls.
- Mute/solo status
- Effects set dynamically through SetEffect or a Set Effect Action.
- Random and Sequence containers histories (last played, etc)

  注解
  :   To reset Game Object specific values, use [AK::SoundEngine::UnregisterGameObj](namespace_a_k_1_1_sound_engine_af53445c959103c84ea50c17d665f254a.html#af53445c959103c84ea50c17d665f254a) or [AK::SoundEngine::UnregisterAllGameObj](namespace_a_k_1_1_sound_engine_a60be51486f9221e38962232911ef190a.html#a60be51486f9221e38962232911ef190a) then [AK::SoundEngine::RegisterGameObj](namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html#a895ed0f83a0dea8fc284491c0ee0152c) if the game object is still needed.

  参见
- [AK::SoundEngine::ResetGlobalValues](namespace_a_k_1_1_sound_engine_a532bfa9818dd773fcc34266fdc4006a2.html#a532bfa9818dd773fcc34266fdc4006a2)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [988](_ak_command_types_8h_source.html#l00988) 行定义.