# AkCmd_PostMIDIOnEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___post_m_i_d_i_on_event-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_PostMIDIOnEvent结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___post_m_i_d_i_on_event_a8b74913a69b50cf3e2dbf0077a60fcbc.html#a8b74913a69b50cf3e2dbf0077a60fcbc) |
|  | Unique ID that will be associated with this playback. Use [AK\_SoundEngine\_GeneratePlayingID()](_ak_command_buffer_8h_a4d75a81be7be245c1e49cea34e32bfc3.html#a4d75a81be7be245c1e49cea34e32bfc3) to generate a new unique playing ID. [更多...](struct_ak_cmd___post_m_i_d_i_on_event_a8b74913a69b50cf3e2dbf0077a60fcbc.html#a8b74913a69b50cf3e2dbf0077a60fcbc) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [eventID](struct_ak_cmd___post_m_i_d_i_on_event_a051ea3ac9daffe885394fdf9546a635b.html#a051ea3ac9daffe885394fdf9546a635b) |
|  | Unique ID of the Event [更多...](struct_ak_cmd___post_m_i_d_i_on_event_a051ea3ac9daffe885394fdf9546a635b.html#a051ea3ac9daffe885394fdf9546a635b) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___post_m_i_d_i_on_event_ae6a9b32a534bb9a37015146d09d9a90f.html#ae6a9b32a534bb9a37015146d09d9a90f) |
|  | Associated game object ID [更多...](struct_ak_cmd___post_m_i_d_i_on_event_ae6a9b32a534bb9a37015146d09d9a90f.html#ae6a9b32a534bb9a37015146d09d9a90f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [flags](struct_ak_cmd___post_m_i_d_i_on_event_abdf2eb7150a0fa4a1869f335a6d54880.html#abdf2eb7150a0fa4a1869f335a6d54880) |
|  | Bitmask: see [AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732) [更多...](struct_ak_cmd___post_m_i_d_i_on_event_abdf2eb7150a0fa4a1869f335a6d54880.html#abdf2eb7150a0fa4a1869f335a6d54880) |
|  | |
| [AkEventCallbackFunc](_ak_callback_types_8h_a276c9e8420fee177debd0838b664d7c7.html#a276c9e8420fee177debd0838b664d7c7) | [callback](struct_ak_cmd___post_m_i_d_i_on_event_a40c814ca30976705f55ae5caf66d35cc.html#a40c814ca30976705f55ae5caf66d35cc) |
|  | (optional) Callback function [更多...](struct_ak_cmd___post_m_i_d_i_on_event_a40c814ca30976705f55ae5caf66d35cc.html#a40c814ca30976705f55ae5caf66d35cc) |
|  | |
| void \* | [callbackCookie](struct_ak_cmd___post_m_i_d_i_on_event_a27010e39f0479875a08cfac5554a592d.html#a27010e39f0479875a08cfac5554a592d) |
|  | (optional) Callback cookie [更多...](struct_ak_cmd___post_m_i_d_i_on_event_a27010e39f0479875a08cfac5554a592d.html#a27010e39f0479875a08cfac5554a592d) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [isOffsetAbsolute](struct_ak_cmd___post_m_i_d_i_on_event_a65ac029dd87f02065a9f2767e1248749.html#a65ac029dd87f02065a9f2767e1248749) |
|  | Set to true when [AkMIDIPost::uOffset](struct_ak_m_i_d_i_post_a946b9b31a3345afd96983129151751e9.html#a946b9b31a3345afd96983129151751e9 "Frame offset (in samples) for MIDI event post") are absolute, false when relative to current frame [更多...](struct_ak_cmd___post_m_i_d_i_on_event_a65ac029dd87f02065a9f2767e1248749.html#a65ac029dd87f02065a9f2767e1248749) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [isNewSequence](struct_ak_cmd___post_m_i_d_i_on_event_a52b912bf0cb55bf0b678699e55f16a3e.html#a52b912bf0cb55bf0b678699e55f16a3e) |
|  | When set, a new sequence identified by `playingID` will be created for these MIDI posts. When unset, MIDI events will be added to an existing sequence specified by `playingID`. [更多...](struct_ak_cmd___post_m_i_d_i_on_event_a52b912bf0cb55bf0b678699e55f16a3e.html#a52b912bf0cb55bf0b678699e55f16a3e) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numMidiPosts](struct_ak_cmd___post_m_i_d_i_on_event_a0d96d07ea31db250304b1f2456af052a.html#a0d96d07ea31db250304b1f2456af052a) |
|  | Number of MIDI Events to post [更多...](struct_ak_cmd___post_m_i_d_i_on_event_a0d96d07ea31db250304b1f2456af052a.html#a0d96d07ea31db250304b1f2456af052a) |
|  | |

## 详细描述

Executes a number of MIDI Events on all nodes that are referenced in the specified Event in an Action of type Play. The time at which a MIDI Event is posted is determined by `is_offset_absolute`. If false, each MIDI event will be posted in `AkMIDIPost::uOffset` samples from the start of the current frame. If true, each MIDI event will be posted at the absolute time `AkMIDIPost::uOffset` samples. To obtain the current absolute time, see `AK::SoundEngine::GetSampleTick`. The duration of a sample can be determined from the sound engine's audio settings, via a call to `AK::SoundEngine::GetAudioSettings`.

The Sound Engine expects an array of `AkMIDIPost` objects after the command. The number of items must correspond to the value of `numMidiPosts`. For example:

```
AkMIDIPost values[2]; // Initialize array as required
auto cmd = (AkCmd_PostMIDIOnEvent*)AK_CommandBuffer_Add(buffer, AkCommand_PostMIDIOnEvent);
cmd->numMidiPosts = 2;
AK_CommandBuffer_AddArray(buffer, sizeof(AkMIDIPost), cmd->numMidiPosts, values);
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `playingID`, `eventID` is an invalid ID, or incomplete array after the command.
- AK\_InsufficientMemory: Not enough memory to process the command.
- AK\_IDNotFound: `eventID` not found or `gameObjectID` is specified and not registered, or `playingID` was not found when adding MIDI posts to an existing sequence.
- AK\_PartialSuccess: When connected to the Wwise Profiler, command has been delayed to a later frame until Wwise synchronizes the event.

参见
:   - [AkCommand\_PostMIDIOnEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdabb16fb8c53fb070bf174b991f33669b2 "See AkCmd_PostMIDIOnEvent")
    - [AK\_CommandBuffer\_AddArray](_ak_command_buffer_8h_a7512f07e3e8f24cf4ed15bebf3a6392e.html#a7512f07e3e8f24cf4ed15bebf3a6392e)
    - `AK::SoundEngine::PostMIDIOnEvent`
    - `AK::SoundEngine::StopMIDIOnEvent`
    - `AK::SoundEngine::GetAudioSettings`
    - `AK::SoundEngine::GetSampleTick`
    - [MIDI Event 序列 – Playing ID](soundengine_midi.html#soundengine_midi_event_playing_id)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [753](_ak_command_types_8h_source.html#l00753) 行定义.