# AkCmd_StopMIDIOnEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___stop_m_i_d_i_on_event-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_StopMIDIOnEvent结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___stop_m_i_d_i_on_event_af70c0e3415ce76ca2b5c0803d8253704.html#af70c0e3415ce76ca2b5c0803d8253704) |
|  | (optional) Target playing ID [更多...](struct_ak_cmd___stop_m_i_d_i_on_event_af70c0e3415ce76ca2b5c0803d8253704.html#af70c0e3415ce76ca2b5c0803d8253704) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [eventID](struct_ak_cmd___stop_m_i_d_i_on_event_a3c3065af06d25f815c8de375af5563a6.html#a3c3065af06d25f815c8de375af5563a6) |
|  | (optional) Unique ID of the Event [更多...](struct_ak_cmd___stop_m_i_d_i_on_event_a3c3065af06d25f815c8de375af5563a6.html#a3c3065af06d25f815c8de375af5563a6) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___stop_m_i_d_i_on_event_a516202f51bc07f30a49534d531a87f7c.html#a516202f51bc07f30a49534d531a87f7c) |
|  | (optional) Associated game object ID [更多...](struct_ak_cmd___stop_m_i_d_i_on_event_a516202f51bc07f30a49534d531a87f7c.html#a516202f51bc07f30a49534d531a87f7c) |
|  | |

## 详细描述

Stops MIDI notes on all nodes that are referenced in the specified event in an action of type Play, with the specified Game Object. Invalid parameters are interpreted as wildcards. For example, calling this function with `eventID` set to AK\_INVALID\_UNIQUE\_ID will stop all MIDI notes for Game Object `gameObjectID`.

参见
:   - [AkCommand\_PostMIDIOnEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdabb16fb8c53fb070bf174b991f33669b2 "See AkCmd_PostMIDIOnEvent")
    - `AK::SoundEngine::StopMIDIOnEvent`
    - `AK::SoundEngine::PostMIDIOnEvent`
    - [MIDI Event 序列 – Playing ID](soundengine_midi.html#soundengine_midi_event_playing_id)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [776](_ak_command_types_8h_source.html#l00776) 行定义.