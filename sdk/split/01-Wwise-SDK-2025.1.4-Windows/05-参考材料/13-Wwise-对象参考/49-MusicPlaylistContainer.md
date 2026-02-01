# MusicPlaylistContainer

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

MusicPlaylistContainer

- **Plugin ID**: 34
- **Class ID**: 2228240

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **3DPosition** | 3D Position | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Emitter | | 1 | Emitter with Automation | | 2 | Listener with Automation | | true | None | false |
| **3DSpatialization** | 3D Spatialization | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | Position | | 2 | Position + Orientation | | true | None | false |
| **Attenuation** | Attenuation | Reference |  | **可能的类型：**   |  | | --- | | Attenuation | | true |  |  |
| **AttenuationDistanceScaling** | Distance Scaling % | Real32 | 1 | [ 0.01 , 100 ] | true | Multiplicative | false |
| **BelowThresholdBehavior** | Virtual Voice Behavior | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Continue to play | | 1 | Kill voice | | 2 | Send to virtual voice | | 3 | Kill if finite else virtual | | true | None | false |
| **BypassEffect** | Bypass All Effects | bool | false | None | true | Boolean | true |
| **CenterPercentage** | Center % | int32 | 0 | [ 0 , 100 ] | true | Exclusive | true |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **Conversion** | Conversion Settings | Reference |  | **可能的类型：**   |  | | --- | | Conversion | | true |  |  |
| **Effects** | Effects | List |  | **可能的类型：**   |  | | --- | | EffectSlot | |  |  |  |
| **EnableAttenuation** | Enable Attenuation | bool | true | None | true | Boolean | false |
| **EnableDiffraction** | Diffraction and Transmission | bool | false | None | true | None | false |
| **EnableLoudnessNormalization** | Enable Loudness Normalization | bool | false | None | true | None | false |
| **GameAuxSendDSF** | Game-Defined Auxiliary Sends DSF | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **GameAuxSendHPF** | Game-Defined Auxiliary Sends HPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **GameAuxSendLPF** | Game-Defined Auxiliary Sends LPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **GameAuxSendVolume** | Game-Defined Auxiliary Sends Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **GridFrequencyPreset** | Grid Frequency | int16 | 50 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 50 | 4 Bars | | 51 | 2 Bars | | 52 | 1 Bar | | 53 | Beat | | 54 | 1/1 (whole note) | | 55 | 1/2 (half note) | | 56 | 1/4 (quarter note) | | 57 | 1/8 (eighth note) | | 64 | 1/16 | | 67 | 1/32 | | 58 | 1/2 triplet | | 59 | 1/4 triplet | | 60 | 1/8 triplet | | 65 | 1/16 triplet | | 68 | 1/32 triplet | | 61 | 1/2 dotted | | 62 | 1/4 dotted | | 63 | 1/8 dotted | | 66 | 1/16 dotted | | 69 | 1/32 dotted | | true | None | false |
| **GridOffsetCustom** | Grid Offset Custom | Real64 | 0 | [ 0 , 99999 ] | true | None | false |
| **GridOffsetPreset** | Grid Offset | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | No | | 1 | Custom | | 50 | 4 Bars | | 51 | 2 Bars | | 52 | 1 Bar | | 53 | Beat | | 54 | 1/1 (whole note) | | 55 | 1/2 (half note) | | 56 | 1/4 (quarter note) | | 57 | 1/8 (eighth note) | | 64 | 1/16 | | 67 | 1/32 | | 58 | 1/2 triplet | | 59 | 1/4 triplet | | 60 | 1/8 triplet | | 65 | 1/16 triplet | | 68 | 1/32 triplet | | 61 | 1/2 dotted | | 62 | 1/4 dotted | | 63 | 1/8 dotted | | 66 | 1/16 dotted | | 69 | 1/32 dotted | | true | None | false |
| **HdrActiveRange** | HDR Active Range | Real64 | 12 | [ 0 , 96 ] | true | Exclusive | true |
| **HdrEnableEnvelope** | Enable Envelope Tracking | bool | false | None | true | None | false |
| **HdrEnvelopeSensitivity** | HDR Envelope Sensitivity | Real64 | 20 | [ 0 , 100 ] | true | None | false |
| **Highpass** | Voice HPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **HoldEmitterPositionOrientation** | Hold Emitter Position and Orientation | bool | false | None | true | None | false |
| **HoldListenerOrientation** | Hold Listener Orientation | bool | false | None | true | None | false |
| **IgnoreParentMaxSoundInstance** | Ignore Parent Playback Limit | bool | false | None | true | None | false |
| **Inclusion** | Inclusion | bool | true | None | true | None | true |
| **IsGlobalLimit** | Limitation Scope | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Game object | | 1 | Global | | true | None | false |
| **ListenerRelativeRouting** | Listener Relative Routing | bool | true | None | true | None | false |
| **LoudnessNormalizationTarget** | Loudness Normalization Target | Real64 | -23 | [ -96 , 0 ] | true | None | false |
| **LoudnessNormalizationType** | Loudness Normalization Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Integrated | | 1 | Momentary Max | | true | None | false |
| **Lowpass** | Voice LPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **MakeUpGain** | Make-Up Gain | Real64 | 0 | [ -96 , 96 ] | true | Additive | true |
| **MaxReachedBehavior** | If Priority Equal | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Discard oldest | | 1 | Discard newest | | true | None | false |
| **MaxSoundPerInstance** | Sound Instance Limit | int16 | 50 | [ 1 , 1000 ] | true | Exclusive | true |
| **Metadata** | Metadata | List |  | **可能的类型：**   |  | | --- | | MetadataSlot | |  |  |  |
| **MidiTarget** | MIDI Target | Reference |  | **可能的类型：**   |  | | --- | | RandomSequenceContainer | | SwitchContainer | | BlendContainer | | Sound | | true |  |  |
| **MidiTempoSource** | MIDI Clip Tempo Source | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Hierarchy | | 1 | File | | true | None | false |
| **OutputBus** | Output Bus | Reference |  | **可能的类型：**   |  | | --- | | Bus |     **不得为 Null** | true |  |  |
| **OutputBusDualshelf** | Output Bus DSF | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **OutputBusHighpass** | Output Bus HPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **OutputBusLowpass** | Output Bus LPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **OutputBusVolume** | Output Bus Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **OverLimitBehavior** | If Limit Reached | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Kill voice | | 1 | Use virtual voice settings | | true | None | false |
| **OverrideAnalysis** | Override Loudness Normalization | bool | false | None | true | None | false |
| **OverrideClockSettings** | Override Clock Settings | bool | false | None | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **OverrideConversion** | Override Conversion Settings | bool | false | None | true | None | false |
| **OverrideEarlyReflections** | Override Early Reflections Send | bool | false | None | true | None | false |
| **OverrideEffect** | Override Effects | bool | false | None | true | None | false |
| **OverrideGameAuxSends** | Override Game-Defined Auxiliary Sends | bool | false | None | true | None | false |
| **OverrideHdrEnvelope** | Override HDR Envelope | bool | false | None | true | None | false |
| **OverrideMetadata** | Override Metadata | bool | false | None | true | None | false |
| **OverrideMidiTarget** | Override MIDI Target | bool | false | None | true | None | false |
| **OverrideMidiTempo** | Override MIDI Clip Tempo | bool | false | None | true | None | false |
| **OverrideOutput** | Override Output Bus | bool | 0 | None | true | None | false |
| **OverridePositioning** | Override Positioning | bool | false | None | true | None | false |
| **OverridePriority** | Override Priority | bool | false | None | true | None | false |
| **OverrideUserAuxSends** | Override User-Defined Auxiliary Sends | bool | false | None | true | None | false |
| **OverrideVirtualVoice** | Override Virtual Voice | bool | false | None | true | None | false |
| **PlaybackSpeed** | Playback Speed | Real64 | 1 | [ 0.25 , 4 ] | true | Multiplicative | true |
| **PlaylistRoot** | Playlist Root | Reference |  | **可能的类型：**   |  | | --- | | MusicPlaylistItem |     **不得为 Null** | false |  |  |
| **Priority** | Priority | int16 | 50 | [ 0 , 100 ] | true | Additive | true |
| **PriorityDistanceFactor** | Use Offset Priority | bool | false | None | true | None | false |
| **PriorityDistanceOffset** | Offset at Max Distance | int16 | -10 | [ -100 , 100 ] | true | None | true |
| **RTPC** | RTPC | List |  | **可能的类型：**   |  | | --- | | RTPC | |  |  |  |
| **ReflectionsAuxSend** | Early Reflections Auxiliary Send | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **ReflectionsVolume** | Early Reflections Send Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **SpeakerPanning** | Speaker Panning | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Direct Assignment | | 1 | Balance-Fade | | 2 | Steering | | true | None | false |
| **SpeakerPanning3DSpatializationMix** | Speaker Panning / 3D Spatialization Mix | int32 | 100 | [ 0 , 100 ] | true | Exclusive | false |
| **Stingers** | Music Stingers | List |  | **可能的类型：**   |  | | --- | | MusicStinger | |  |  |  |
| **Tempo** | Tempo | Real64 | 120 | [ 1 , 400 ] | true | None | false |
| **TimeSignatureLower** | Time Signature Lower | int16 | 4 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 | 1 | | 2 | 2 | | 4 | 4 | | 8 | 8 | | 16 | 16 | | 32 | 32 | | true | None | false |
| **TimeSignatureUpper** | Time Signature Upper | int16 | 4 | [ 1 , 64 ] | true | None | false |
| **TransitionRoot** | Transition Root | Reference |  | **可能的类型：**   |  | | --- | | MusicTransition |     **不得为 Null** | false |  |  |
| **UseGameAuxSends** | Use Game-Defined Auxiliary Sends | bool | false | None | true | None | false |
| **UseMaxSoundPerInstance** | Limit Sound Instances | bool | false | None | true | None | true |
| **UserAuxSend0** | User-Defined Auxiliary Send 0 | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **UserAuxSend1** | User-Defined Auxiliary Send 1 | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **UserAuxSend2** | User-Defined Auxiliary Send 2 | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **UserAuxSend3** | User-Defined Auxiliary Send 3 | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **UserAuxSendHPF0** | User-Defined Auxiliary HPF 0 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendHPF1** | User-Defined Auxiliary HPF 1 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendHPF2** | User-Defined Auxiliary HPF 2 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendHPF3** | User-Defined Auxiliary HPF 3 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendLPF0** | User-Defined Auxiliary LPF 0 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendLPF1** | User-Defined Auxiliary LPF 1 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendLPF2** | User-Defined Auxiliary LPF 2 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendLPF3** | User-Defined Auxiliary LPF 3 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendVolume0** | User-Defined Auxiliary Send Volume 0 | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **UserAuxSendVolume1** | User-Defined Auxiliary Send Volume 1 | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **UserAuxSendVolume2** | User-Defined Auxiliary Send Volume 2 | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **UserAuxSendVolume3** | User-Defined Auxiliary Send Volume 3 | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **VirtualVoiceQueueBehavior** | On Return to Physical Voice | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Play from beginning | | 1 | Play from elapsed time | | 2 | Resume | | true | None | false |
| **Volume** | Voice Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |