# AkCmd_SeekOnEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___seek_on_event-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SeekOnEvent结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [eventID](struct_ak_cmd___seek_on_event_afbc9daea47a41aeb2cc5e8ac711e6bf5.html#afbc9daea47a41aeb2cc5e8ac711e6bf5) |
|  | Unique ID of the event [更多...](struct_ak_cmd___seek_on_event_afbc9daea47a41aeb2cc5e8ac711e6bf5.html#afbc9daea47a41aeb2cc5e8ac711e6bf5) |
|  | |
| union { |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24)   [absolute](struct_ak_cmd___seek_on_event_a98a27c1aae44b41a624dd379d34f6d12.html#a98a27c1aae44b41a624dd379d34f6d12) |
|  | Desired position where playback should restart, in milliseconds [更多...](union_ak_cmd___seek_on_event_1_1_0d0_af1ea87860071155798f0ae377d7d458a.html#af1ea87860071155798f0ae377d7d458a) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)   [relative](struct_ak_cmd___seek_on_event_ab787a29f42bdda72a743f8f9473f5bd8.html#ab787a29f42bdda72a743f8f9473f5bd8) |
|  | Desired position where playback should restart, expressed in a percentage of the file's total duration, between 0 and 1.f (see note above about infinite looping sounds) [更多...](union_ak_cmd___seek_on_event_1_1_0d0_ac4a0c6439244777ee1c71e9035d31b00.html#ac4a0c6439244777ee1c71e9035d31b00) |
|  | |
| } | [position](struct_ak_cmd___seek_on_event_a75de97aaa8049590b9e731998ac63f06.html#a75de97aaa8049590b9e731998ac63f06) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___seek_on_event_a784ec6c25cf840d10a2ff591a2ff4b45.html#a784ec6c25cf840d10a2ff591a2ff4b45) |
|  | (optional) Associated game object ID; use AK\_INVALID\_GAME\_OBJECT to affect all game objects [更多...](struct_ak_cmd___seek_on_event_a784ec6c25cf840d10a2ff591a2ff4b45.html#a784ec6c25cf840d10a2ff591a2ff4b45) |
|  | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___seek_on_event_ab62ba11bd5c2daaef7f9bafe77f0cded.html#ab62ba11bd5c2daaef7f9bafe77f0cded) |
|  | (optional) Specify the playing ID for the seek to be applied to. Will result in the seek happening only on active actions of the playing ID. Let it be AK\_INVALID\_PLAYING\_ID to seek on all active actions of this event ID. [更多...](struct_ak_cmd___seek_on_event_ab62ba11bd5c2daaef7f9bafe77f0cded.html#ab62ba11bd5c2daaef7f9bafe77f0cded) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [isPositionRelative](struct_ak_cmd___seek_on_event_a68aac39e928795a640a5bf19fb5afe9a.html#a68aac39e928795a640a5bf19fb5afe9a) |
|  | Determines whether the position should be interpreted as absolute (milliseconds) or relative (%). [更多...](struct_ak_cmd___seek_on_event_a68aac39e928795a640a5bf19fb5afe9a.html#a68aac39e928795a640a5bf19fb5afe9a) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [seekToNearestMarker](struct_ak_cmd___seek_on_event_a2afd8091bdbf75b384ee0a5a1a47bf83.html#a2afd8091bdbf75b384ee0a5a1a47bf83) |
|  | If non-zero, the final seeking position will be made equal to the nearest marker (see note above) [更多...](struct_ak_cmd___seek_on_event_a2afd8091bdbf75b384ee0a5a1a47bf83.html#a2afd8091bdbf75b384ee0a5a1a47bf83) |
|  | |

## 详细描述

Seeks inside all playing objects that are referenced in Play Actions of the specified Event.

Notes:

- This works with all objects of the Containers hierarchy, including Music Segments and Music Switch Containers.
- There is a restriction with sounds that play within a continuous sequence. Seeking is ignored if one of their ancestors is a continuous (random or sequence) container with crossfade or trigger rate transitions. Seeking is also ignored with sample-accurate transitions, unless the sound that is currently playing is the first sound of the sequence.
- Seeking is also ignored with voices that can go virtual with "From Beginning" behavior.
- Sounds/segments are stopped if `position` is greater than their duration.
- `position` is clamped internally to the beginning of the sound/segment.
- If the option "Seek to nearest marker" is used, the seeking position snaps to the nearest marker. With objects of the Containers hierarchy, markers are embedded in wave files by an external wave editor. Note that looping regions ("sampler loop") are not considered as markers. Also, the "add file name marker" of the conversion settings dialog adds a marker at the beginning of the file, which is considered when seeking to nearest marker. In the case of interactive music objects (Music Segments, Music Switch Containers, and Music Playlist Containers), user (wave) markers are ignored: seeking occurs to the nearest segment cue (authored in the segment editor), including the Entry Cue, but excluding the Exit Cue.
- This method posts a command in the sound engine queue, thus seeking will not occur before the audio thread consumes it (after a call to [RenderAudio()](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1)).

Notes specific to Music Segments:

- With Music Segments, `position` is relative to the Entry Cue, in milliseconds. Use a negative value to seek within the Pre-Entry.
- Music segments cannot be looped. You may want to listen to the AK\_EndOfEvent notification in order to restart them if required.
- In order to restart at the correct location, with all their tracks synchronized, Music Segments take the "look-ahead time" property of their streamed tracks into account for seeking. Consequently, the resulting position after a call to [SeekOnEvent()](namespace_a_k_1_1_sound_engine_a33010f3ba82a8838bb2f4283ee2ee9d7.html#a33010f3ba82a8838bb2f4283ee2ee9d7) might be earlier than the value that was passed to the method. Use `AK::MusicEngine::GetPlayingSegmentInfo()` to query the exact position of a segment. Also, the segment will be silent during that time (so that it restarts precisely at the position that you specified). `AK::MusicEngine::GetPlayingSegmentInfo()` also informs you about the remaining look-ahead time.

Notes specific to Music Switch Containers:

- Seeking triggers a music transition towards the current (or target) segment. This transition is subject to the container's transition rule that matches the current and defined in the container, so the moment when seeking occurs depends on the rule's "Exit At" property. On the other hand, the starting position in the target segment depends on both the desired seeking position and the rule's "Sync To" property.
- If the specified time is greater than the destination segment's length, the modulo is taken.

This command can fail for the following reasons:

- AK\_InvalidParameter: `eventID` is invalid or relative position is not in the valid range.
- AK\_IDNotFound: Event was not found, or `gameObjectID` is specified but not a registered game object.

参见
:   - `AkCommand_SeekOnEvent`
    - `AK::SoundEngine::SeekOnEvent()`
    - `AK::SoundEngine::GetSourcePlayPosition()`
    - `AK::MusicEngine::GetPlayingSegmentInfo()`

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [661](_ak_command_types_8h_source.html#l00661) 行定义.