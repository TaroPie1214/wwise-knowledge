# 集成详情——MIDI

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

集成详情——MIDI

# 简介

SDK API 提供向声音引擎发送 MIDI 事件的功能。可能发送的 MIDI 事件的类型有：

- Note-On（音符开启）事件。
- Note-Off（音符关闭）事件。
- 以及 CC（持续控制器）事件。

要 MIDI 事件产生声音，则这些事件必须有目标合成器。The synthesizer is a collection of Wwise objects created by the Wwise user in the project's Containers hierarchy. Note-on events will typically play the targeted Container object or one of its descendants. If played, the Container object will stop once it has:

- 如果没有设置循环，在播放到对象源的末尾时，
- 或者相应 Note-Off 事件（相同音符和通道）发送到同一目标。

# 把 MIDI 事件集成到游戏中

[AK::SoundEngine::PostMIDIOnEvent](namespace_a_k_1_1_sound_engine_ab24b5dc8bd4d1adbdc6aa5c98d94d946.html#ab24b5dc8bd4d1adbdc6aa5c98d94d946) "PostMIDIOnEvent" 函数对声音引擎中的 MIDI 事件排队。此函数使用以下项目作为变量：

- MIDI 事件。
- Event ID。
- Game Object ID。
- Playing ID。

声音引擎将已发送的 MIDI 事件分组成序列。每个序列通过以下项目标识：

- Game Object ID；函数参数，
- Playing ID；函数参数，
- Wwise 对象 ID；从对应于事件 ID 的事件中的播放动作的目标对象获取。 请参阅 [集成 Event](integrating_elements_events.html) 了解有关事件的更多详情。

因此，可同时向多个目标发送相同 MIDI 事件。例如，假设我们有：

- 事件 EV1，它有针对 Wwise 对象 W0 和 W1 的播放动作，
- 事件 EV2，它有针对 Wwise 对象 W0 的播放动作。

如果我们把 "ME1" MIDI Event 发送到 "GO" Game Object 上的 "EV1" Wwise Event，声音引擎会将 "ME1" MIDI Event 添加到 "W0-GO-PID1" 和 "W1-GO-PID1" MIDI 序列。其中，PID1 为 PostMIDIOnEvent 返回的 Playing ID。 倘若我们再把 "ME2" MIDI Event 发送到 "EV2" Wwise Event，声音引擎会将 "ME2" MIDI Event 添加到 "W0-GO-PID2" MIDI 序列。

调用 [AK::SoundEngine::PostMIDIOnEvent](namespace_a_k_1_1_sound_engine_ab24b5dc8bd4d1adbdc6aa5c98d94d946.html#ab24b5dc8bd4d1adbdc6aa5c98d94d946) 将把 MIDI 事件添加到 MIDI 序列中。 然而，在调用 [AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1) 函数之前不会执行任何处理。每次调用 [AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1) 都会处理消息队列，可能产生任意数量的音频帧；具体帧数量取决于距上次调用 RenderAudio 以来已走过的时间。RenderAudio 每处理一帧，声音引擎就会使所有 MIDI 序列前进一帧。

# MIDI Event 时机

MIDI Event 的执行时机由以下因素决定：

- 添加到队列中的时机（通过 PostMIDIOnEvent）
- Event 的成员 [AkMIDIPost::uOffset](struct_ak_m_i_d_i_post_a946b9b31a3345afd96983129151751e9.html#a946b9b31a3345afd96983129151751e9 "Frame offset (in samples) for MIDI event post")
- 提供给 PostMIDIOnEvent 调用的 in\_bAbsoluteOffsets 参数

若 in\_bAbsoluteOffsets 为 false，则在从声音引擎的消息队列读取 PostMIDIOnEvent 消息之后隔 uOffset 个样本再执行 MIDI Event（参见 [更新 MIDI 序列](soundengine_midi.html#soundengine_midi_update_sequence) 章节）。 若 in\_bAbsoluteOffsets 为 true，则以绝对时间为准隔 uOffset 个样本再执行 MIDI Event。可通过调用 [AK::SoundEngine::GetSampleTick](namespace_a_k_1_1_sound_engine_ac688bf2d1ae6f2009e7cde602a753b6b.html#ac688bf2d1ae6f2009e7cde602a753b6b) 来获取当前绝对时间。

|  |  |
| --- | --- |
|  | **备注:** 可通过调用 [AK::SoundEngine::GetAudioSettings](namespace_a_k_1_1_sound_engine_a1ecadb91731d6cabe36603fa419b6715.html#a1ecadb91731d6cabe36603fa419b6715) 来获取声音引擎的音频设置并由此确定样本的时长。 |

# MIDI Event 序列 – Playing ID

通过调用 PostMIDIOnEvent 可将发送的所有 MIDI Event 添加到 MIDI 序列中。如前所述，MIDI 序列可通过以下方式识别：

- Playing ID，
- Game Object ID，
- Event ID。 在首次调用 PostMIDIOnEvent 时为序列创建 Playing ID，并将 in\_playingID 设为 AK\_INVALID\_PLAYING\_ID。在后续调用 PostMIDIOnEvent 时使用该 Playing ID 将 MIDI Event 添加到序列中。顺序如下：
- 在首次调用 PostMIDIOnEvent 时创建 MIDI 序列，并将 in\_playingID 函数参数设为 AK\_INVALID\_PLAYING\_ID。函数返回 "PID" Playing ID。
- 在后续调用 PostMIDIOnEvent 时将 Event 添加到序列中，并将 in\_playingID 函数参数设为 PID。

可通过 PostMIDIOnEvent 返回的 Playing ID 确定是否将 Event 发送到了预定序列。若返回的 Playing ID：

- 与 in\_playingID 匹配，则表示将 Event 添加到了预定序列。
- 与 in\_playingID 不匹配，则表示将 Event 添加到新建序列。
- 为AK\_INVALID\_PLAYING\_ID，则表示出现了错误，未将 Event 添加到任何序列。

若满足以下条件，则创建与指定序列不同的新序列：

- 序列 (Playing ID) 不存在。
- 使用不同的 Game Object 或 Event 创建了序列。
- 序列已不存在（已执行所有 MIDI Event 并终止播放所有声音）。

# 更新 MIDI 序列

声音引擎在应用程序设定的时间播放 MIDI 序列非常重要。有两种方式向声音引擎发送 MIDI 序列。

如果整个 MIDI 序列为已知，并且知道 MIDI 序列的时序不会改变，则调用一次 [AK::SoundEngine::PostMIDIOnEvent](namespace_a_k_1_1_sound_engine_ab24b5dc8bd4d1adbdc6aa5c98d94d946.html#ab24b5dc8bd4d1adbdc6aa5c98d94d946) 可发送整个 MIDI 序列。

然而，如果不是这样，则必须每帧更新一次 MIDI 序列。在应用程序中可随时随地调用 [AK::SoundEngine::PostMIDIOnEvent](namespace_a_k_1_1_sound_engine_ab24b5dc8bd4d1adbdc6aa5c98d94d946.html#ab24b5dc8bd4d1adbdc6aa5c98d94d946) 函数。 然而，在除主音频线程之外的线程中调用此函数可能会导致同步问题。调用 [AK::SoundEngine::PostMIDIOnEvent](namespace_a_k_1_1_sound_engine_ab24b5dc8bd4d1adbdc6aa5c98d94d946.html#ab24b5dc8bd4d1adbdc6aa5c98d94d946) 只会发送声音引擎消息队列中的事件。消息队列在调用 [AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1) 期间处理，此类调用中可能会处理任意数量的音频帧。 为了确保正确同步，建议应用程序按照以下方式注册一个全局回调函数：

- AK::SoundEngine::RegisterGlobalCallback( &MyCallbackFunction, AkGlobalCallbackLocation\_PreProcessMessageQueueForRender );

声音引擎将在每个音频帧上调用这个注册了的函数。应用程序可使用回调函数跟踪声音引擎处理的音频帧。 因此，在回调函数中发送 MIDI 事件将确保正确同步。

# 停止 MIDI 序列

调用 [AK::SoundEngine::StopMIDIOnEvent](namespace_a_k_1_1_sound_engine_acce4adb3c2bbd018ef375c85379949e3.html#acce4adb3c2bbd018ef375c85379949e3) "StopMIDIOnEvent" 函数可停止 MIDI 序列。函数接收 Playing ID、Event ID 和 Game Object ID 作为参数。 所有这些参数都可设为无效值来充当通配符。因此，若所有参数均被设为无效值，则将停止所有 MIDI 序列。

调用此函数将清空 MIDI 序列，并停止任何正在播放的声音。

有关集成 MIDI 的示例，请参阅 [快速入门示例集成——MIDI](quickstart_sample_integration_midi.html) 。