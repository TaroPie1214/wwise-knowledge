# Using the Level Sequencer

|  |
| --- |
| Wwise Unreal Integration Documentation |

Using the Level Sequencer

The Unreal Engine's Sequence Editor is a cinematic editing tool. You can use it to add Tracks that modify certain Actor properties in a level.

Refer to the following topics for background information on the Sequencer:

- For instructions on how to create a Level Sequence, refer to [Sequencer Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview).
- For instructions on how to add Tracks to a Level Sequence, refer to the Adding Tracks section on the [Tracks](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine) page.

# Setting up Your Wwise Project

To ensure that Event lengths are properly represented in the AkAudioEvent Tracks, you must configure the Wwise project to estimate the duration of its audio Events and generate JSON metadata.

**To set up your Wwise project:**

1. Open the project in Wwise Authoring.
2. From the menu bar, click **Project > Project Settings**. The Project Settings dialog opens.
3. On the SoundBanks tab, enable the following options:
   - **Estimated Duration**
   - **Generate JSON Metadata**

![](../../../images/project_settings.png)

AkAudioEvent Track 所需的 Project Settings 配置

# Using Wwise Level Sequencer Tracks

The Wwise Integration adds two Tracks to the Sequencer:

- **WwiseGameParameter**, which sets Game Parameter values.
- **AkAudioEvent**, which posts Wwise Events.

You can add both of these Tracks as Master Tracks or associate them with Actors. When associated with Actors, they perform Wwise-related functions on the `UAkComponent` attached to the Actor. When created as Master Tracks, the **WwiseGameParameter** Track sets global Game Parameter values, and the **AkAudioEvent** Track posts Events on a dummy game object.

For **WwiseGameParameter** Tracks, you can modify Game Parameter curves with the built-in curve editor. To add key frames, place the cursor in the desired location and click **Add New Key** on the right side of the listed Track.

![](../../../images/wwisegameparameter_track_in_curve_editor.png)

A Wwise Game Parameter track in the Curve Editor view

|  |  |
| --- | --- |
|  | **注記：** The values in this curve represent the Game Parameters sent to Wwise through SetRTPC. They are not the values in the [RTPC graph](https://www.audiokinetic.com/en/library/edge/?source=Help&id=mapping_values_in_rtpc_graph) itself, but are instead the input to the RTPC graph as defined in your Wwise project. |

For **AkAudioEvent** Tracks, you can add [`AkAudioEvent`](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent)  sections. To do so, place the cursor at the desired location and click **AkAudioEvent** on the right side of the listed Track. Alternatively, you can drag [`AkAudioEvent`](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent)  assets from the Content Browser directly onto an **AkAudioEvent** Track.

![](../../../images/adding_akaudioevents.png)

将AkAudioEvent Section 添加到 AkAudioEvent Track

# Displaying Waveforms for Wwise Events

Unreal Integration 使用 Wwise Authoring API (WAAPI) 扩展 Sequencer 功能。For more information about WAAPI and its use in the Unreal integration, refer to [Wwise Authoring API (WAAPI)](using_features_waapi.html). When Unreal is connected to the Wwise Authoring tool through WAAPI, AkAudioEvent sections can display waveforms for Wwise events. When Wwise Authoring is not open, or the Unreal integration is not connected to WAAPI, the AkAudioEvent sections only display the Event name.

## Viewing AkAudioEvent Section Waveforms

**AkAudioEvent** Section 针对包含 Audio Source 的 Event 显示音频波形。The waveform in an **AkAudioEvent** section shows the audio data for the longest Audio Source contained in the Wwise Event. In the following example, a Wwise Event called "Play\_Sound" contains three Audio Sources: "Layer\_1", "Layer\_2", and "Layer\_3".

![](../../../images/sequencer_example_event.png)

示例 – Wwise Event 包含三个 Audio Source

If an **AkAudioEvent** section is added and its Event property is set to "Play\_Sound", then the longest of the three Audio Sources is displayed within the section. Note that the waveform might be followed by empty space if the Wwise Event lasts longer than the longest Audio Source that it contains. In this example, because the "Play\_Sound" Event has two delayed play actions (for "Layer\_2" and "Layer\_3"), it lasts longer than the "Layer\_1" audio source that it contains. 波形后面的空白区指示了 SoundBank 生成期间计算得出的 Wwise Event 的最大预计时长（参见 [Setting up Your Wwise Project](using_features_sequencer.html#wwise_project_setup) 章节）。

![](../../../images/sequencer_example_event_section.png)

示例 – Sequencer 中的 AkAudioEvent Section

If the length of the **AkAudioEvent** section exceeds the maximum estimated duration of the Wwise Event, the section contains either a flat white line or repeating diagonal lines. 白色直线表示禁用了 **Retrigger** 属性。斜线组表示启用了 **Retrigger** 属性。The **Retrigger** property determines whether Wwise events are retriggered in the Sequencer after they finish (refer to [AkAudioEvent Section 属性](using_features_sequencer.html#wwise_level_sequencer_event_section_properties)).

![](../../../images/sequencer_example_retrigger_enablement.png)

Sequencer 中有两个 **AkAudioEvent** Section 。Retrigger is enabled in the 'Retrigger' section and disabled in the 'No\_Retrigger' section.

## Fixing "Out of Sync" Waveforms

If you change the content of an Event in the Wwise Project, for example by changing the source file of its corresponding SFX or voice, and those changes are not reflected in the generated SoundBanks, any **AkAudioEvent** sections for that event are marked as "out of sync". The waveform is displayed in red, and an asterisk is appended to the name of the AkAudioEvent section. Warnings are also printed to the output log when Events are triggered from "out of sync" sections.

![](../../../images/sequencer_example_dirty_section.png)

示例 – Out of Sync AkAudioEvent Section

To ensure that **AkAudioEvent** sections remain synchronized with the Wwise project, there are options to save the project and regenerate SoundBanks directly from the Sequencer. To synchronise all of the sections in an **AkAudioEvent** track, open the track's context menu (right click) and click **Save Wwise project and refresh all sections** (see [AkAudioEvent Track 上下文菜单选项](using_features_sequencer.html#wwise_level_sequencer_event_track_context_menu)).

# Scrubbing Tracks

The Sequencer integration supports scrubbing forwards and backwards over **AkAudioEvent** tracks. Drag the Sequencer playhead over **AkAudioEvent** sections to hear scrub snippets. To change the length of these scrub snippets, right-click the **AkAudioEvent** section and in the context menu, click **Scrub Tail Length Ms**. Refer to [AkAudioEvent Section 属性](using_features_sequencer.html#wwise_level_sequencer_event_section_properties) for more details.

# AkAudioEvent Track 上下文菜单选项

From the **AkAudioEvent** track, right-click to open a context menu that includes the following Audiokinetic-specific option:

- **Save Wwise project and refresh all sections**: Saves the Wwise project in Wwise Authoring and regenerates SoundBanks for all AkAudioEvent sections in the Sequencer track. The section waveforms are then updated.

# AkAudioEvent Section 上下文菜单选项

From the **AkAudioEvent** section on the track, right-click to open a context menu that includes the following Audiokinetic-specific option:

- **Match section length to Wwise event length**: Matches the length of the section in the Sequencer track to the duration of the Wwise Event.

## AkAudioEvent Section 属性

The property list in the context menu includes the following Wwise-specific section properties:

- **Ak Audio Event**：针对所选 Section 列出 AkAudioEvent 的以下可编辑属性：
  - **Event:** Audiokinetic Event. Open this list to create a new Audiokinetic Event, or drag in an existing event from the Content Browser or from the [Wwise Browser](features_editor_wwise_browser.html)
  - **Retrigger Event**: When enabled, the Wwise event in the Section is retriggered when the Sequence plays beyond the end of the event. Disabled by default.
  - **Scrub Tail Length Ms**: Sets the duration in milliseconds of the scrub snippets that are played when scrubbing over the sequence. Default is 100ms.
  - **Max Source Duration**：显示 Wwise Event 中所含的最长 Audio Source 的时长（只读）。
  - **Stop at Section End**: Clear this box to keep the Event playing when the end of the section is reached. 该项默认设为启用状态。

# Known Issues and Limitations

In general, we recommend that you use very simple AkAudioEvent sections in the Level Sequencer, such as a simple Play action on a Sound SFX. Avoid more complex Wwise Events such as those that contain delayed actions, Seek actions, or which reference Random Containers, Sequence Containers, and other non-deterministic objects. If you do use such Events, divide them into simpler events for optimal use in the Level Sequencer.

Scrubbing and playing from cursor does not work as expected on Events with delayed actions or that contain infinitely looping sounds.

## Play In Editor 限制

If a level sequence is played from the Sequencer editor window while Unreal is running in Play in Editor (PIE) mode, any AkAudioEvent tracks that are associated with game objects do not trigger events. To hear AkAudioEvent tracks that are bound to game objects, you must trigger the level sequence from the Game World.

## Replication Limitations

**AkAudioEvent** and **WwiseGameParameter** tracks are triggered only on the server and are not replicated to clients.