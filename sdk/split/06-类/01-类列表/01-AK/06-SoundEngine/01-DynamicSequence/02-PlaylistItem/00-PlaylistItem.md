# PlaylistItem

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [SoundEngine](namespace_a_k_1_1_sound_engine.html)
- [DynamicSequence](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence.html)
- [PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item.html)

[所有成员列表](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK::SoundEngine::DynamicSequence::PlaylistItem类 参考

`#include <AkDynamicSequence.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a1dd1b9c0ec759948da25abcc9112d147.html#a1dd1b9c0ec759948da25abcc9112d147) () |
|  | |
|  | [PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_ad1e3cf6288b76a1d8784ac989f1fc4e5.html#ad1e3cf6288b76a1d8784ac989f1fc4e5) (const [PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item.html) &in\_rCopy) |
|  | |
|  | [~PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a90f3f4acd15144380aae92701dccdb21.html#a90f3f4acd15144380aae92701dccdb21) () |
|  | |
| [PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item.html) & | [operator=](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a171594de8ac2285367f33ce61db2e7ba.html#a171594de8ac2285367f33ce61db2e7ba) (const [PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item.html) &in\_rCopy) |
|  | |
| bool | [operator==](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a267a331ee54a6aa39a5b78387d75e5bb.html#a267a331ee54a6aa39a5b78387d75e5bb) (const [PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item.html) &in\_rCopy) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetExternalSources](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_aa861de047bd7230b4f016de187d35f16.html#aa861de047bd7230b4f016de187d35f16) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_nExternalSrc, [AkExternalSourceInfo](struct_ak_external_source_info.html) \*in\_pExternalSrc) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [audioNodeID](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a897995cadbf6731404089f979633f681.html#a897995cadbf6731404089f979633f681) |
|  | Unique ID of Audio Node [更多...](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a897995cadbf6731404089f979633f681.html#a897995cadbf6731404089f979633f681) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [msDelay](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a34ebfc61b9997835249d82a627e5316c.html#a34ebfc61b9997835249d82a627e5316c) |
|  | Delay before playing this item, in milliseconds [更多...](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a34ebfc61b9997835249d82a627e5316c.html#a34ebfc61b9997835249d82a627e5316c) |
|  | |
| void \* | [pCustomInfo](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a81ccc1deaef45fcd73335ad14f881fcb.html#a81ccc1deaef45fcd73335ad14f881fcb) |
|  | Optional user data [更多...](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_a81ccc1deaef45fcd73335ad14f881fcb.html#a81ccc1deaef45fcd73335ad14f881fcb) |
|  | |
| [AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) | [pExternalSrcs](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item_ad591aa0bacda2c2f7c7e7d6a41ddf2c4.html#ad591aa0bacda2c2f7c7e7d6a41ddf2c4) |
|  | |

## 详细描述

[Playlist](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist.html) Item for Dynamic Sequence [Playlist](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist.html).

参见
:   - [AK::SoundEngine::DynamicSequence::Playlist](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist.html)
    - [AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)
    - [集成 External Source](integrating_external_sources.html)

在文件 [AkDynamicSequence.h](_ak_dynamic_sequence_8h_source.html) 第 [46](_ak_dynamic_sequence_8h_source.html#l00046) 行定义.