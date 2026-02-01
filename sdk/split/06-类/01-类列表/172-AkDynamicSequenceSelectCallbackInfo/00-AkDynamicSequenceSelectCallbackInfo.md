# AkDynamicSequenceSelectCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_dynamic_sequence_select_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkDynamicSequenceSelectCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [audioNodeID](struct_ak_dynamic_sequence_select_callback_info_af51458175921854e7dfdcd3b985430dc.html#af51458175921854e7dfdcd3b985430dc) |
|  | Unique ID of Audio Node (can be resolved using [AK::SoundEngine::DynamicDialogue](namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue.html) API). Set to AK\_INVALID\_UNIQUE\_ID to signal that no item is available to play. [更多...](struct_ak_dynamic_sequence_select_callback_info_af51458175921854e7dfdcd3b985430dc.html#af51458175921854e7dfdcd3b985430dc) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [msDelay](struct_ak_dynamic_sequence_select_callback_info_a72e7fb977569fcd088ed6ebe5aa81030.html#a72e7fb977569fcd088ed6ebe5aa81030) |
|  | Delay before playing this item, in milliseconds [更多...](struct_ak_dynamic_sequence_select_callback_info_a72e7fb977569fcd088ed6ebe5aa81030.html#a72e7fb977569fcd088ed6ebe5aa81030) |
|  | |
| void \* | [pCustomInfo](struct_ak_dynamic_sequence_select_callback_info_a86a044254a24ef01cc0010174f9defb8.html#a86a044254a24ef01cc0010174f9defb8) |
|  | Optional user data [更多...](struct_ak_dynamic_sequence_select_callback_info_a86a044254a24ef01cc0010174f9defb8.html#a86a044254a24ef01cc0010174f9defb8) |
|  | |
| [AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) | [arExternalSources](struct_ak_dynamic_sequence_select_callback_info_a922b1a4a0f65269beb665b505c98419f.html#a922b1a4a0f65269beb665b505c98419f) |
|  | Optional external sources. Use API described in [AkExternalSourceArray.h](_ak_external_source_array_8h.html) to add required external sources to play the next item. [更多...](struct_ak_dynamic_sequence_select_callback_info_a922b1a4a0f65269beb665b505c98419f.html#a922b1a4a0f65269beb665b505c98419f) |
|  | |

## 详细描述

Callback information structure corresponding to [AK\_DynamicSequenceSelect](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a5711d007422c8abda1cfc88174a56d11). Called when a dynamic sequence must select its next item to play. The callee is expected to fill out the information contained in this structure. If there is no item available to play, the callee must set `audioNodeID` to `AK_INVALID_UNIQUE_ID`. This will cause the dynamic sequence to stop. Use `AK::SoundEngine::DynamicSequence::Play` to start playback again.

|  |  |
| --- | --- |
|  | **警告:** When opening a dynamic sequence with the callback flag `AK_DynamicSequenceSelect`, the callback is the ONLY way to determine the next item to play. `AK::SoundEngine::DynamicSequence::LockPlaylist` always returns `NULL` for dynamic sequences opened with `AK_DynamicSequenceSelect`. |

参见
:   - [AK::SoundEngine::DynamicSequence::Open()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc)
    - [集成详情——动态对白](soundengine_dynamicdialogue.html)

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [327](_ak_callback_types_8h_source.html#l00327) 行定义.