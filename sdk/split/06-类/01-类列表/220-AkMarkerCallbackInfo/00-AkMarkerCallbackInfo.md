# AkMarkerCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_marker_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkMarkerCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uIdentifier](struct_ak_marker_callback_info_aa7748e167a3ef098db4d9bb88be3489c.html#aa7748e167a3ef098db4d9bb88be3489c) |
|  | Cue point identifier [更多...](struct_ak_marker_callback_info_aa7748e167a3ef098db4d9bb88be3489c.html#aa7748e167a3ef098db4d9bb88be3489c) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPosition](struct_ak_marker_callback_info_a3cee8ac29ebb9b0bb14d27317da99535.html#a3cee8ac29ebb9b0bb14d27317da99535) |
|  | Position in the cue point (unit: sample frames) [更多...](struct_ak_marker_callback_info_a3cee8ac29ebb9b0bb14d27317da99535.html#a3cee8ac29ebb9b0bb14d27317da99535) |
|  | |
| const char \* | [strLabel](struct_ak_marker_callback_info_a170f3dc5b73d97dcedfc3f94d258ace2.html#a170f3dc5b73d97dcedfc3f94d258ace2) |
|  | Label of the marker (null-terminated) [更多...](struct_ak_marker_callback_info_a170f3dc5b73d97dcedfc3f94d258ace2.html#a170f3dc5b73d97dcedfc3f94d258ace2) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uLabelSize](struct_ak_marker_callback_info_a6fd9819cd571fafcf79fd0667722c4dd.html#a6fd9819cd571fafcf79fd0667722c4dd) |
|  | Size of the label string (including the terminating null character) [更多...](struct_ak_marker_callback_info_a6fd9819cd571fafcf79fd0667722c4dd.html#a6fd9819cd571fafcf79fd0667722c4dd) |
|  | |

## 详细描述

Callback information structure corresponding to [AK\_Marker](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ad3d6fcbeb177c536da8eb74d0f132827).

参见
:   - [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)
    - [集成详情——事件](soundengine_events.html)
    - [集成 Marker](soundengine_markers.html)

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [179](_ak_callback_types_8h_source.html#l00179) 行定义.