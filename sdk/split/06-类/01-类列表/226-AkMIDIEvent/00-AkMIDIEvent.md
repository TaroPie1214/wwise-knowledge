# AkMIDIEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_m_i_d_i_event-members.html) |
[Public 属性](#pub-attribs)

AkMIDIEvent结构体 参考

`#include <AkMidiTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [byType](struct_ak_m_i_d_i_event_a78c8c7dc4351862a52e78fcdf84e1dc2.html#a78c8c7dc4351862a52e78fcdf84e1dc2) |
|  | See AK\_MIDI\_EVENT\_TYPE\_\* pre-processor definitions [更多...](struct_ak_m_i_d_i_event_a78c8c7dc4351862a52e78fcdf84e1dc2.html#a78c8c7dc4351862a52e78fcdf84e1dc2) |
|  | |
| [AkMidiChannelNo](_ak_midi_types_8h_a04087ee2bce0372883d5e328c7314639.html#a04087ee2bce0372883d5e328c7314639) | [byChan](struct_ak_m_i_d_i_event_a52b225e8dcec974e4953f1eae8bd2708.html#a52b225e8dcec974e4953f1eae8bd2708) |
|  | |
| union { |
| struct [AkMIDIGen](struct_ak_m_i_d_i_gen.html)   [Gen](struct_ak_m_i_d_i_event_a2b4ef1cf58170a4039e496366c17598b.html#a2b4ef1cf58170a4039e496366c17598b) |
|  | |
| struct [AkMIDICC](struct_ak_m_i_d_i_c_c.html)   [Cc](struct_ak_m_i_d_i_event_a61501416ac4d281cdafc919ada42064f.html#a61501416ac4d281cdafc919ada42064f) |
|  | |
| struct [AkMIDINote](struct_ak_m_i_d_i_note.html)   [NoteOnOff](struct_ak_m_i_d_i_event_ab3c3b016e51551674a24bc401717953e.html#ab3c3b016e51551674a24bc401717953e) |
|  | |
| struct [AkMIDIPitchbend](struct_ak_m_i_d_i_pitchbend.html)   [PitchBend](struct_ak_m_i_d_i_event_ab15028cce5879f6686abf8b48c22042a.html#ab15028cce5879f6686abf8b48c22042a) |
|  | |
| struct [AkMIDINoteAftertouch](struct_ak_m_i_d_i_note_aftertouch.html)   [NoteAftertouch](struct_ak_m_i_d_i_event_ad88ec3414d3eb608eb6a4c49925e0a87.html#ad88ec3414d3eb608eb6a4c49925e0a87) |
|  | |
| struct [AkMIDIChannelAftertouch](struct_ak_m_i_d_i_channel_aftertouch.html)   [ChanAftertouch](struct_ak_m_i_d_i_event_a49c16d1b3efaafbe0385d45953ee4c2e.html#a49c16d1b3efaafbe0385d45953ee4c2e) |
|  | |
| struct [AkMIDIProgramChange](struct_ak_m_i_d_i_program_change.html)   [ProgramChange](struct_ak_m_i_d_i_event_a6374cb5aa38e9b4a1968e38ef2af2e94.html#a6374cb5aa38e9b4a1968e38ef2af2e94) |
|  | |
| struct [AkMIDIWwiseCmd](struct_ak_m_i_d_i_wwise_cmd.html)   [WwiseCmd](struct_ak_m_i_d_i_event_ad1f77db13f43feeac85df7bd155ede49.html#ad1f77db13f43feeac85df7bd155ede49) |
|  | |
| }; |  |
|  | |

## 详细描述

在文件 [AkMidiTypes.h](_ak_midi_types_8h_source.html) 第 [216](_ak_midi_types_8h_source.html#l00216) 行定义.