# 快速入门示例集成——MIDI

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

快速入门示例集成——MIDI

# MIDI 集成示例

MIDI 事件通过调用 [AK::SoundEngine::PostMIDIOnEvent()](namespace_a_k_1_1_sound_engine_ab24b5dc8bd4d1adbdc6aa5c98d94d946.html#ab24b5dc8bd4d1adbdc6aa5c98d94d946) 函数进行发布。以下代码显示有关下列的示例：

- 设置初始 MIDI 参数，
- 使用事件名称（音频设计师对事件的命名）或者“Wwise\_IDs.h”中定义的事件 ID（Wwise 生成的头文件）发布 MIDI 事件。

#include "Wwise\_IDs.h" // 由 Wwise 生成的 ID

// 在声音引擎初始化后，注册全局回调函数。

// 确保在处理消息队列之前注册回调；

// 这将确保新发布的 MIDI 事件在当前帧期间

// 得到处理（即我们退出回调函数后立即处理）。

[AK::SoundEngine::RegisterGlobalCallback](namespace_a_k_1_1_sound_engine_ade293d3ed101fe494ead6dffb1c682fb.html#ade293d3ed101fe494ead6dffb1c682fb)( &MIDICallback, [AkGlobalCallbackLocation\_PreProcessMessageQueueForRender](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676a75a5fe904855d596a5652cca9025ee41) )

// 获取声音引擎音频设置。这些设置在确定一个音频帧的

// 等效时间时是必须用到的。

[AkAudioSettings](struct_ak_audio_settings.html) audioSettings;

[AK::SoundEngine::GetAudioSettings](namespace_a_k_1_1_sound_engine_a1ecadb91731d6cabe36603fa419b6715.html#a1ecadb91731d6cabe36603fa419b6715)( audioSettings );

(...)

// 用于发布 MIDI 事件的回调函数。

void MIDICallback( bool in\_bLastCall )

{

// 如需要，发布 MIDI 事件。

// 格外小心，确保此代码对线程是安全的。

// 对于此例，假设我们需要对同一音符发布 note-on

// 和 note-off 事件。

[AkMIDIPost](struct_ak_m_i_d_i_post.html) aPosts[2];

const [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) byNote = 60;

const [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) byChan = 0; // 值域 0-15 映射到 MIDI 通道值域 1-16。

const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uOnSamples = 0; // 音符将从当前帧的开头开始。

const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uOffSamples = uOnOffset + audioSettings.[uNumSamplesPerFrame](struct_ak_audio_settings_a2f27fe7b83e9c83ff7fc16b3160b669f.html#a2f27fe7b83e9c83ff7fc16b3160b669f) / 2;

// 音符将在一帧当中结束。

// Note-on

[AkMIDIPost](struct_ak_m_i_d_i_post.html)& noteOn = aPosts[0];

noteOn.byType = [AK\_MIDI\_EVENT\_TYPE\_NOTE\_ON](_ak_midi_types_8h_ab12db90c72e49a3514ad0e77b296fa5e.html#ab12db90c72e49a3514ad0e77b296fa5e);

noteOn.byChan = byChan;

noteOn.NoteOnOff.byNote = byNote;

noteOn.NoteOnOff.byVelocity = 72; // 随机力度

noteOn.[uOffset](struct_ak_m_i_d_i_post_a946b9b31a3345afd96983129151751e9.html#a946b9b31a3345afd96983129151751e9) = uOnSamples;

// Note-off

[AkMIDIPost](struct_ak_m_i_d_i_post.html)& noteOff = aPosts[1];

noteOff.byType = [AK\_MIDI\_EVENT\_TYPE\_NOTE\_OFF](_ak_midi_types_8h_a4e80b2ac02932beebf56df69d409b072.html#a4e80b2ac02932beebf56df69d409b072);

noteOff.byChan = byChan;

noteOff.NoteOnOff.byNote = byNote;

noteOff.NoteOnOff.byVelocity = 0; // not used for note-off

noteOff.[uOffset](struct_ak_m_i_d_i_post_a946b9b31a3345afd96983129151751e9.html#a946b9b31a3345afd96983129151751e9) = uOffSamples;

[AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) eventID = [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)( "MIDIEventName" );

[AK::SoundEngine::PostMIDIOnEvent](namespace_a_k_1_1_sound_engine_ab24b5dc8bd4d1adbdc6aa5c98d94d946.html#ab24b5dc8bd4d1adbdc6aa5c98d94d946)( eventID, REGISTERED\_MIDI\_GAME\_OBJECT, aPosts, 2 );

}

请参阅 [集成详情——事件](soundengine_events.html) 了解有关事件的更多信息。 请参阅 [集成详情——MIDI](soundengine_midi.html) 了解有关 MIDI 的更多信息。

[AK\_MIDI\_EVENT\_TYPE\_NOTE\_ON](_ak_midi_types_8h_ab12db90c72e49a3514ad0e77b296fa5e.html#ab12db90c72e49a3514ad0e77b296fa5e)

#define AK\_MIDI\_EVENT\_TYPE\_NOTE\_ON

**Definition:** [AkMidiTypes.h:54](_ak_midi_types_8h_source.html#l00054)

[AK::SoundEngine::RegisterGlobalCallback](namespace_a_k_1_1_sound_engine_ade293d3ed101fe494ead6dffb1c682fb.html#ade293d3ed101fe494ead6dffb1c682fb)

AKSOUNDENGINE\_API AKRESULT RegisterGlobalCallback(AkGlobalCallbackFunc in\_pCallback, AkUInt32 in\_eLocation=AkGlobalCallbackLocation\_BeginRender, void \*in\_pCookie=NULL, AkPluginType in\_eType=AkPluginTypeNone, AkUInt32 in\_ulCompanyID=0, AkUInt32 in\_ulPluginID=0)

[AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270)

uint8\_t AkUInt8

Unsigned 8-bit integer

**Definition:** [AkNumeralTypes.h:34](_ak_numeral_types_8h_source.html#l00034)

[AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc)

AkUInt32 AkUniqueID

Unique 32-bit ID

**Definition:** [AkTypedefs.h:31](_ak_typedefs_8h_source.html#l00031)

[AkAudioSettings](struct_ak_audio_settings.html)

Configured audio settings

**Definition:** [AkSoundEngineTypes.h:51](_ak_sound_engine_types_8h_source.html#l00050)

[AK::SoundEngine::PostMIDIOnEvent](namespace_a_k_1_1_sound_engine_ab24b5dc8bd4d1adbdc6aa5c98d94d946.html#ab24b5dc8bd4d1adbdc6aa5c98d94d946)

AKSOUNDENGINE\_API AkPlayingID PostMIDIOnEvent(AkUniqueID in\_eventID, AkGameObjectID in\_gameObjectID, AkMIDIPost \*in\_pPosts, AkUInt16 in\_uNumPosts, bool in\_bAbsoluteOffsets=false, AkUInt32 in\_uFlags=0, AkCallbackFunc in\_pfnCallback=NULL, void \*in\_pCookie=NULL, AkPlayingID in\_playingID=AK\_INVALID\_PLAYING\_ID)

[AK::SoundEngine::GetAudioSettings](namespace_a_k_1_1_sound_engine_a1ecadb91731d6cabe36603fa419b6715.html#a1ecadb91731d6cabe36603fa419b6715)

AKSOUNDENGINE\_API AKRESULT GetAudioSettings(AkAudioSettings &out\_audioSettings)

[AkAudioSettings::uNumSamplesPerFrame](struct_ak_audio_settings_a2f27fe7b83e9c83ff7fc16b3160b669f.html#a2f27fe7b83e9c83ff7fc16b3160b669f)

AkUInt32 uNumSamplesPerFrame

Number of samples per audio frame (256, 512, 1024 or 2048).

**Definition:** [AkSoundEngineTypes.h:52](_ak_sound_engine_types_8h_source.html#l00052)

[AkGlobalCallbackLocation\_PreProcessMessageQueueForRender](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676a75a5fe904855d596a5652cca9025ee41)

@ AkGlobalCallbackLocation\_PreProcessMessageQueueForRender

Start of frame rendering, before having processed game messages.

**Definition:** [AkCallbackTypes.h:114](_ak_callback_types_8h_source.html#l00114)

[AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)

AKSOUNDENGINE\_API AkUInt32 GetIDFromString(const char \*in\_pszString)

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AkMIDIPost](struct_ak_m_i_d_i_post.html)

**Definition:** [AkMidiTypes.h:235](_ak_midi_types_8h_source.html#l00234)

[AK\_MIDI\_EVENT\_TYPE\_NOTE\_OFF](_ak_midi_types_8h_a4e80b2ac02932beebf56df69d409b072.html#a4e80b2ac02932beebf56df69d409b072)

#define AK\_MIDI\_EVENT\_TYPE\_NOTE\_OFF

**Definition:** [AkMidiTypes.h:53](_ak_midi_types_8h_source.html#l00053)

[AkMIDIPost::uOffset](struct_ak_m_i_d_i_post_a946b9b31a3345afd96983129151751e9.html#a946b9b31a3345afd96983129151751e9)

AkUInt64 uOffset

Frame offset (in samples) for MIDI event post

**Definition:** [AkMidiTypes.h:237](_ak_midi_types_8h_source.html#l00237)