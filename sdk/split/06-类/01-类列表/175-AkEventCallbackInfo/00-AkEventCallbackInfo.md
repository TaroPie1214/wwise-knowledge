# AkEventCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_event_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkEventCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjID](struct_ak_event_callback_info_a59805fe0bb72c75ed2c34b17aa6aa3e0.html#a59805fe0bb72c75ed2c34b17aa6aa3e0) |
|  | Game object ID [更多...](struct_ak_event_callback_info_a59805fe0bb72c75ed2c34b17aa6aa3e0.html#a59805fe0bb72c75ed2c34b17aa6aa3e0) |
|  | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_event_callback_info_a40697ff0b1574c42ca2db43d60669fc5.html#a40697ff0b1574c42ca2db43d60669fc5) |
|  | Playing ID of Event, returned by [PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) [更多...](struct_ak_event_callback_info_a40697ff0b1574c42ca2db43d60669fc5.html#a40697ff0b1574c42ca2db43d60669fc5) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [eventID](struct_ak_event_callback_info_a9f58cb33a32d7a8efbc7439c7f8fa65d.html#a9f58cb33a32d7a8efbc7439c7f8fa65d) |
|  | Unique ID of Event, passed to [PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) [更多...](struct_ak_event_callback_info_a9f58cb33a32d7a8efbc7439c7f8fa65d.html#a9f58cb33a32d7a8efbc7439c7f8fa65d) |
|  | |

## 详细描述

Callback information structure corresponding to [AK\_EndOfEvent](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a5ad7a62bfb83e7450cc685b3e51f767a), [AK\_MusicPlayStarted](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732aa1e3e1e198f859e3dad76009eec3ee29) and [AK\_Starvation](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a392e9c2615d919f2bf9005cf250fef45).

参见
:   - [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)
    - [集成详情——事件](soundengine_events.html)

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [158](_ak_callback_types_8h_source.html#l00158) 行定义.