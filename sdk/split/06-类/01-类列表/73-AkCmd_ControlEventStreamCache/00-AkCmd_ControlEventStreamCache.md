# AkCmd_ControlEventStreamCache

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___control_event_stream_cache-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ControlEventStreamCache结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [eventID](struct_ak_cmd___control_event_stream_cache_aa384c41eaf390179640b059de1c5132a.html#aa384c41eaf390179640b059de1c5132a) |
|  | ID of event. Stream caching state will be updated for all streaming files referenced by this event. [更多...](struct_ak_cmd___control_event_stream_cache_aa384c41eaf390179640b059de1c5132a.html#aa384c41eaf390179640b059de1c5132a) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [isCached](struct_ak_cmd___control_event_stream_cache_ac7a389107fa3db2b2709f15cfff2c2af.html#ac7a389107fa3db2b2709f15cfff2c2af) |
|  | Activate or de-activate stream caching. When false, any cache buffers previously associated with the event are released. [更多...](struct_ak_cmd___control_event_stream_cache_ac7a389107fa3db2b2709f15cfff2c2af.html#ac7a389107fa3db2b2709f15cfff2c2af) |
|  | |
| [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) | [activePriority](struct_ak_cmd___control_event_stream_cache_a485dab1c5cafc7b29079c200ec66b072.html#a485dab1c5cafc7b29079c200ec66b072) |
|  | Priority of active stream caching I/O [更多...](struct_ak_cmd___control_event_stream_cache_a485dab1c5cafc7b29079c200ec66b072.html#a485dab1c5cafc7b29079c200ec66b072) |
|  | |
| [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) | [inactivePriority](struct_ak_cmd___control_event_stream_cache_ae349b4ce9d3215d711ae4551be99b12f.html#ae349b4ce9d3215d711ae4551be99b12f) |
|  | Priority of inactive stream caching I/O [更多...](struct_ak_cmd___control_event_stream_cache_ae349b4ce9d3215d711ae4551be99b12f.html#ae349b4ce9d3215d711ae4551be99b12f) |
|  | |

## 详细描述

Allows streaming the first part of all streamed files referenced by an Event into a cache buffer.

Caching streams are serviced when no other streams require the available bandwidth. The files will remain cached until a command disables caching, or a higher priority pinned file needs the space and the limit set by `uMaxCachePinnedBytes` is exceeded.

备注
:   The amount of data from the start of the file that will be pinned to cache is determined by the prefetch size. The prefetch size is set via the authoring tool and stored in the sound banks.
:   It is possible to override the prefetch size stored in the sound bank via the low level IO. For more information see `AK::StreamMgr::IAkLowLevelIOHook::BatchOpen()` and `AkFileSystemFlags`.
:   If this function is called additional times with the same event, then the priority of the caching streams are updated. Note however that priority is passed down to the stream manager on a file-by-file basis, and if another event is pinned to cache that references the same file but with a different priority, then the first priority will be updated with the most recent value.
:   If the event references files that are chosen based on a State Group (via a switch container), all files in all states will be cached. Those in the current active state will get cached with active priority, while all other files will get cached with inactive priority.
:   `inactivePriority` is only relevant for events that reference switch containers that are assigned to State Groups. This parameter is ignored for all other events, including events that only reference switch containers that are assigned to Switch Groups. Files that are chosen based on a Switch Group have a different switch value per game object, and are all effectively considered active by the pin-to-cache system.

This command can fail for the following reasons:

- `AK_InvalidParameter` if `eventID` is invalid
- `AK_IDNotFound` if `eventID` refers to an unknown event

参见
:   - [AkCommand\_ControlEventStreamCache](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaad5c3276c6f28ec03634c9744edfeb7d "See AkCmd_ControlEventStreamCache")
    - [AK::SoundEngine::PinEventInStreamCache](namespace_a_k_1_1_sound_engine_ae98b64113d2b9bd2e63adef8cee96805.html#ae98b64113d2b9bd2e63adef8cee96805)
    - [AK::SoundEngine::UnpinEventInStreamCache](namespace_a_k_1_1_sound_engine_a09d2491e7ad56454b3720f182b09549a.html#a09d2491e7ad56454b3720f182b09549a)
    - [AK::SoundEngine::GetBufferStatusForPinnedEvent](namespace_a_k_1_1_sound_engine_a3e077eddb929881cd5369fd3e6bba5d7.html#a3e077eddb929881cd5369fd3e6bba5d7)
    - [AK::StreamMgr::IAkLowLevelIOHook::BatchOpen](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a0abfde848b599b5e5b8e8ed63dc8b555.html#a0abfde848b599b5e5b8e8ed63dc8b555)
    - [AkFileSystemFlags](struct_ak_file_system_flags.html "File system flags for file descriptors mapping.")

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1249](_ak_command_types_8h_source.html#l01249) 行定义.