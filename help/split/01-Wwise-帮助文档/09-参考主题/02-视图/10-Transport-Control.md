# Transport Control

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [视图](00-视图.md) > Transport Control

## Transport Control

When you select a Wwise object, it is loaded into the Transport Control where you can
audition it. Selectable objects are sounds, containers, Music Segments and Containers, and
Events (not Dialogue Events). With them, you can:

- Audition an imported but unconverted version of a file. 请参阅 [“Using original audio files during playback”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/01-Setting-playback-properties.md#using_original_audio_files_during_playback "Using original audio files during playback")。
- Specify objects to audition based on platform. 请参阅 [“Including or excluding audio and motion content for playback”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/01-Setting-playback-properties.md#including_excluding_audio_and_motion_content_for_playback "Including or excluding audio and motion content for playback")。
- Use the [“Playback Control area”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/00-认识-Transport-Control-视图.md#playback_control_area "Playback Control area") to monitor the playback of fades and delays.
- Audition any applied States, Switches, and RTPCs. 请参阅[“Using game syncs during playback”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/04-Using-game-syncs-during-playback.md "Using game syncs during playback")

The Transport Control is a [view](../../02-入门/04-个性化您的工作空间/01-处理视图/00-处理视图.md "处理视图") you can open by selecting
**Views** > **Transport Control** (Shift+T) from the menu bar.
Some layouts include the Transport Control by default. They are listed in [“处理布局”一节](../../02-入门/04-个性化您的工作空间/02-处理布局/00-处理布局.md "处理布局").

The Transport Control title bar displays the name and icon of a selected object.

To learn more about the Transport Control, see [*认识 Transport Control 视图*](../../08-使用-Wwise/05-认识-Transport-Control-视图/00-认识-Transport-Control-视图.md "认识 Transport Control 视图").

| 界面元素 | 描述 |
| --- | --- |
| **Transport Control** | |
| (Name) | 名称。已加载到 Transport Control 的 Wwise 对象的名称和图标。以下 Wwise 对象可加载到 Transport Control 中：  **Event** |
| **Sound SFX（音效声）** |
| **Sound Voice（语音声）** |
| **Random Container （随机容器）** |
| **Sequence Container （序列容器）** |
| **Blend Container（混合容器）** |
| **Switch Container（切换容器）** |
| **Music Segment （音乐段落）** |
| **Music Playlist Container （音乐播放列表容器）** |
| **Music Switch Container（音乐切换容器）** |
| (固定/取消固定) | 固定。当选中该选项时，当前加载的对象会锁定在 Transport Control 中，而且即使 Property Editor 中有其它对象，新对象也不会加载。 |
|  | 停止播放。 |
|  | 暂停播放。再次点击此按钮将恢复播放。 |
|  | 播放加载到 Transport Control 中的对象。  Hold Shift while clicking Play to have Wwise play the loaded sound while bypassing its properties. That is, somewhat like a PFL (Pre-Fader Listen) found in some DAWs, Wwise will play the object without its hierarchical properties (including such things as volume, pitch, filters, delays, Effects, Auxiliary Sends, Attenuation Curves, RTPC curves, States, positioning, and bus routing), but with its source edits (such as fades, trims, and loop points) still intact.  |  |  | | --- | --- | | [警告] | 警告 | | If you use the Play - Bypass properties shortcut, the resulting sound might be uncomfortably loud or off-pitch. |  单击 Transport 的 Play 按钮会从播放光标的位置播放片段。当播放光标前进时单击 Play 按钮将添加新的播放光标，并从第一个播放光标的起始位置同时播放。 |
| (Transport Play Options) | 打开 Transport Play Options 菜单并显示以下选项：  - **Play Originals** 和 **Play Converted** - **Only Play Objects Included in   Platform**  若选择 **Play Originals**，则播放原始未转码格式的声音。若选择 **Play Converted**，则播放转码版本的声音（如有）。  |  |  | | --- | --- | | [备注] | 备注 | | 在针对特定平台对某个音频文件做转码时，转码的目的是要满足该平台的特定硬件要求。因此，如果 Wwise 设计工具的运行平台不支持该文件类型，可能会无法播放这些转码文件。 |  若选择 **Only Play Objects Included in Platform**，则 Transport Control 中仅可播放所选平台中包含的声音。  默认值为 **Play Originals**，同时激活 **Only Play Objects Included in Platform**。若对这些值实施更改，则 Transport Play Options 按钮将显示为橙色。 |
| (Delay) | 延迟。指示是否对 Event Action、Random Container 或 Sequence Container 应用了延迟。若应用了延迟，则此图标在延迟期间会变为橙色。 |
| (Fade) | 淡变。指示是否对 Event Action、Random Container 或 Sequence Container 应用了淡变。若应用了淡变，则此图标在淡变期间会变为橙色。 |
| (Reset 菜单) | 打开 Reset 菜单并显示以下选项：  - **Reset All** 可将所有对象恢复到原始设置。 - **Reset All Random and Sequence Containers** 可清空已为对象触发的所有随机和序列动作。 - **Reset All Game Parameters** 可清空已为对象触发的所有游戏参数。 - **Reset All States** 可清空对象的所有 Set State 动作。 - **Reset All Switches** 可清空已为对象触发的所有 Set Switch 动作。 - **Reset All Set Mute** 可清空已为对象触发的所有静音动作。 - **Reset All Set Voice Pitch** 可清空已为对象触发的所有声部音高设置动作。 - **Reset All Set Voice Volume** 可清空已为对象触发的声部音量设置动作。 - **Reset All Set Bus Volume** 可清空已为对象触发的总线音量设置动作。 - **Reset All Set Voice Low-pass Filter** 可清空已为对象触发的所有低通滤波器动作。 - **Reset All Bypass Effect**  可清空已为对象触发的所有旁通效果动作。 - **Reset All Set Effect**（重置所有效果器设置）：清除所有已为对象触发的 Set Effect 动作。 - **Reset All Music Tracks Force Usage** 不再强制播放 Soundcaster 中的特定声轨。 - **Reset All Source Editor Play Cursors**（重置所有源编辑器播放光标）：清除 Source Editor 中手动触发的播放光标。 - **Reset Attenuation Preview**（重置衰减预览）：将对象上设置的距离、角度、声障、声笼、衍射和透射值重置为其默认值。 |
| **Game Syncs** | |
|  | 游戏同步器。显示所有与当前对象关联的 State Group 和 State。 |
| （状态组） | 状态组。分配给当前对象的各个 State Group 的名称。 |
| （State） | 状态。在播放期间可以修改的相应 State 的列表。 |
|  | 显示与当前对象关联的所有 Switch Group 和 Switch。 |
| （Swtich Group） | 切换开关组。与当前对象关联的各个 Switch Group 的名称。 |
| (Switch) | 切换开关。在播放期间可以改动的相应 Switch 的列表。 |
|  | 在 Game Syncs 区域中显示指派给当前对象的所有 Game Parameter。 |
| (Game Parameter Name) | 分配给当前对象的各个 Game Parameter 的名称。 |
| (Value) | 各 Game Parameter 值，可在播放并试听 RTPC 效果时修改。 |
|  | 在 Game Syncs 区域中显示与当前对象相关的所有触发器。 |
| (Trigger Name) | 触发器名称。与 Soundcaster 中的对象关联的触发器的列表。 |
|  | 调用对应 Stinger，从而在播放当前音乐对象的同时触发插播乐句。 |

**相关主题**

- [“Setting playback properties”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/01-Setting-playback-properties.md "Setting playback properties")
- [“Using original audio files during playback”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/01-Setting-playback-properties.md#using_original_audio_files_during_playback "Using original audio files during playback")
- [“Including or excluding audio and motion content for playback”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/01-Setting-playback-properties.md#including_excluding_audio_and_motion_content_for_playback "Including or excluding audio and motion content for playback")
- [“重置 Transport Control”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/01-Setting-playback-properties.md#resetting_in_transport_control "重置 Transport Control")
- [“Pinning objects in the Transport Control”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/02-Pinning-objects-in-the-Transport-Control.md "Pinning objects in the Transport Control")
- [“Playing, pausing, or stopping content”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/03-Playing,-pausing,-or-stopping-content.md "Playing, pausing, or stopping content")
- [“Enabling States during playback”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/04-Using-game-syncs-during-playback.md#using_game_syncs_during_playback_enabling_states_during_playback "Enabling States during playback")
- [“Assigning Switches during playback”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/04-Using-game-syncs-during-playback.md#using_game_syncs_during_playback_assigning_switches_during_playback "Assigning Switches during playback")
- [“Changing game parameter values during playback”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/04-Using-game-syncs-during-playback.md#changing_game_parameter_values_during_playback "Changing game parameter values during playback")
- [“Calling Triggers during playback”一节](../../08-使用-Wwise/05-认识-Transport-Control-视图/04-Using-game-syncs-during-playback.md#calling_triggers_during_playback "Calling Triggers during playback")

---