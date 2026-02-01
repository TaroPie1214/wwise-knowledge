# AkMusicSyncCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_music_sync_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkMusicSyncCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkSegmentInfo](struct_ak_segment_info.html) | [segmentInfo](struct_ak_music_sync_callback_info_a7a07c175194882ea39365bfd223da0a4.html#a7a07c175194882ea39365bfd223da0a4) |
|  | Segment information corresponding to the segment triggering this callback. [更多...](struct_ak_music_sync_callback_info_a7a07c175194882ea39365bfd223da0a4.html#a7a07c175194882ea39365bfd223da0a4) |
|  | |
| enum [AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732) | [musicSyncType](struct_ak_music_sync_callback_info_ae414e6cf2d393635bf302a2fbc51d8cb.html#ae414e6cf2d393635bf302a2fbc51d8cb) |
|  | Would be either [AK\_MusicSyncEntry](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ab29d1a78a0f92336b1c155548bc88d72), [AK\_MusicSyncBeat](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a62d1f7986a64a7e9980ff82bd7ae9ba4), [AK\_MusicSyncBar](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ad7d4cc2283a63337542d49c70e55d9ca), [AK\_MusicSyncExit](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732aa92ff2f82ed7a651772e1f3f1d31c76e), [AK\_MusicSyncGrid](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a474f5b9582617f8a4f744e7d47dfa155), [AK\_MusicSyncPoint](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732afde5b3e18578530b70f6e1241a552253) or [AK\_MusicSyncUserCue](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ac827761a64b0d02303ea7eaa98240392). [更多...](struct_ak_music_sync_callback_info_ae414e6cf2d393635bf302a2fbc51d8cb.html#ae414e6cf2d393635bf302a2fbc51d8cb) |
|  | |
| const char \* | [pszUserCueName](struct_ak_music_sync_callback_info_a9b40a5060b9b0ae34c3a4e750d791407.html#a9b40a5060b9b0ae34c3a4e750d791407) |
|  | Cue name (UTF-8 string). Set for notifications AK\_MusicSyncUserCue. NULL if cue has no name. [更多...](struct_ak_music_sync_callback_info_a9b40a5060b9b0ae34c3a4e750d791407.html#a9b40a5060b9b0ae34c3a4e750d791407) |
|  | |

## 详细描述

Callback information structure corresponding to [AK\_MusicSyncEntry](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ab29d1a78a0f92336b1c155548bc88d72), [AK\_MusicSyncBeat](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a62d1f7986a64a7e9980ff82bd7ae9ba4), [AK\_MusicSyncBar](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ad7d4cc2283a63337542d49c70e55d9ca), [AK\_MusicSyncExit](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732aa92ff2f82ed7a651772e1f3f1d31c76e), [AK\_MusicSyncGrid](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a474f5b9582617f8a4f744e7d47dfa155), [AK\_MusicSyncPoint](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732afde5b3e18578530b70f6e1241a552253) and [AK\_MusicSyncUserCue](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ac827761a64b0d02303ea7eaa98240392). If you need the Tempo, you can compute it using the fBeatDuration Tempo (beats per minute) = 60/fBeatDuration

参见
:   - [集成详情——事件](soundengine_events.html)
    - [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)
    - [集成详情——音乐回调](soundengine_music_callbacks.html)

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [263](_ak_callback_types_8h_source.html#l00263) 行定义.