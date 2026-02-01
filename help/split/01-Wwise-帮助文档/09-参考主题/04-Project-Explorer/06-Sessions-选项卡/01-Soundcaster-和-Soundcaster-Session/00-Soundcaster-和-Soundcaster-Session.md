# Soundcaster 和 Soundcaster Session

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Sessions 选项卡](../00-Sessions-选项卡.md) > Soundcaster 和 Soundcaster Session

### Soundcaster 和 Soundcaster Session

在 Wwise Soundcaster 中，您可以通过模拟来实时混音和播放音频和振动。这样您可以创建原型和概念验证，以及试验和测试您的想法。

利用 Soundcaster 控件，可快速更改、编辑和应用对象、Event、State、Switch、Trigger 和 RTPC 的属性，然后在 Wwise 和游戏中试听结果。当连接到游戏时，您可以播放与所选游戏对象关联的声音，并在游戏等环境中试听 State（举例而言）。如果愿意，您则还可以播放未转码文件。您已创建的各个 Soundcaster 布局都可作为 Project Explorer 的 Sessions 选项卡中的 Soundcaster 会话加以保存。Soundcaster 会话就像一个预置，其中包含模拟中所用到的 Wwise 对象和 Event。

| 界面元素 | 描述 |
| --- | --- |
| (Soundcaster Session Selector) | 声音选角器会话选择器。工程内当前存在的 Soundcaster 会话的列表。  所选 Soundcaster 会话的名称显示在相应字段中。 |
|  | 移除 Soundcaster 中的所有模块并停止所有播放。 |
| **Soundcaster 控件** | |
| |  | | --- | |  | | 停止所有 Soundcaster 模块的播放。 |
| |  | | --- | |  | | 暂停所有 Soundcaster 模块的播放。再次点击此按钮将恢复播放。 |
| (Transport Play Options) | 打开 Transport Play Options 菜单并显示以下选项：  - **Play Originals** 和 **Play Converted** - **Only Play Objects Included in Platform**  若选择 **Play Originals**，则播放原始未转码格式的声音。若选择 **Play Converted**，则播放转码版本的声音（如有）。  |  |  | | --- | --- | | [备注] | 备注 | | 在针对特定平台对某个音频文件做转码时，转码的目的是要满足该平台的特定硬件要求。因此，如果 Wwise 设计工具的运行平台不支持该文件类型，可能会无法播放这些转码文件。 |  若选择 **Only Play Objects Included in Platform**，则 Transport Control 中仅可播放所选平台中包含的声音。  默认值为 **Play Originals**，同时激活 **Only Play Objects Included in Platform**。若对这些值实施更改，则 Transport Play Options 按钮将显示为橙色。 |
| |  | | --- | |  |  (Delay) | 延迟。指示是否对 Event Action、Random Container 或 Sequence Container 应用了延迟。如果存在延迟，则此图标在延迟期间会变成蓝色。 |
| |  | | --- | |  |  (Fade) | 淡变。指示是否对 Event Action、Random Container 或 Sequence Container 应用了淡变。如果存在淡变，则此图标在淡变期间会变成蓝色。 |
| (Reset 菜单) | 打开 Reset 菜单并显示以下选项：  - **Reset All** 可将所有对象恢复到原始设置。 - **Reset All Random and Sequence Containers** 可清空已为对象触发的所有随机和序列动作。 - **Reset All Game Parameters** 可清空已为对象触发的所有游戏参数。 - **Reset All States** 可清空对象的所有 Set State 动作。 - **Reset All Switches** 可清空已为对象触发的所有 Set Switch 动作。 - **Reset All Set Mute** 可清空已为对象触发的所有静音动作。 - **Reset All Set Voice Pitch** 可清空已为对象触发的所有声部音高设置动作。 - **Reset All Set Voice Volume** 可清空已为对象触发的声部音量设置动作。 - **Reset All Set Bus Volume** 可清空已为对象触发的总线音量设置动作。 - **Reset All Set Voice Low-pass Filter** 可清空已为对象触发的所有低通滤波器动作。 - **Reset All Bypass Effect**  可清空已为对象触发的所有旁通效果动作。 - **Reset All Set Effect**（重置所有效果器设置）：清除所有已为对象触发的 Set Effect 动作。 - **Reset All Music Tracks Force Usage** 不再强制播放 Soundcaster 中的特定声轨。 - **Reset All Source Editor Play Cursors**（重置所有源编辑器播放光标）：清除 Source Editor 中手动触发的播放光标。 - **Reset Attenuation Preview**（重置衰减预览）：将对象上设置的距离、角度、声障、声笼、衍射和透射值重置为其默认值。 |
| **Game Syncs** | |
| States（状态） | |
|  | 若选中，则将显示工程中创建的所有 State Group 和 State，而非仅显示与加载到 Soundcaster 中的对象关联的 State 和 State Group。 |
| （状态组） | 状态组。与 Soundcaster 中对象关联的各个 State Group 的名称。 |
| （State） | 状态。与当前所选 State Group 关联的各个 State 的名称。 |
| **Switches（切换开关）** | |
|  | 切换开关。当选择了该选项时，将显示工程中已为 Soundcaster 内的对象创建的所有 Switch Group 和 Switch，而非仅仅显示与加载到 Soundcaster 中的对象相关联的 Switch 和 Switch Group。 |
| （Swtich Group） | 状态组。与 Soundcaster 中对象关联的各个 Switch Group 的名称。 |
| (Switch) | 切换开关。与 Switch Group 关联的各个 Switch 的名称。 |
| RTPC | |
|  | 当勾选该选项时，将显示工程中已创建的所有 RTPC ，而非仅仅显示与加载到 Soundcaster 中的对象关联的 RTPC。 |
| (Game Parameter Name) | 游戏参数名称。对象层级结构中各个 Game Parameter 的名称。 |
| (Value) | 值。在播放期间，可修改此 Game Parameter 值来试听 RTPC 效果。 |
| Triggers | |
|  | 在 Game Syncs 区域中显示与当前对象相关的所有触发器。 |
| (Trigger Name) | 触发器名称。与 Soundcaster 中的对象关联的触发器的列表。 |
|  | 调用对应 Stinger，从而在播放当前音乐对象的同时触发插播乐句。 |

| Soundcaster 模块 | |
| --- | --- |
| 界面元素 | 描述 |
| （标题栏） | 已作为 Soundcaster 模块而添加的工程元素的名称和图标。以下工程元素可添加到 Soundcaster 中：  **Event** |
| **Sound SFX（音效声）** |
| **Sound Voice（语音声）** |
| **Random Container （随机容器）** |
| **Sequence Container （序列容器）** |
| **Blend Container（混合容器）** |
| **Switch Container（切换容器）** |
| **Property Container** |
| **Audio Bus（音频总线）** |
| **Music Segment （音乐段落）** |
| **Music Playlist Container （音乐播放列表容器）** |
| **Music Switch Container（音乐切换容器）** |
| |  | | --- | |  | | 停止 Soundcaster 模块的播放。 |
| |  | | --- | |  | | 暂停 Soundcaster 模块的播放。暂停后，再次点击此按钮将恢复播放。 |
| |  | | --- | |  | | 播放所选 Soundcaster 模块。  Hold Shift while clicking Play to have Wwise play the loaded sound while bypassing its properties. That is, somewhat like a PFL (Pre-Fader Listen) found in some DAWs, Wwise will play the object without its hierarchical properties (including such things as volume, pitch, filters, delays, Effects, Auxiliary Sends, Attenuation Curves, RTPC curves, States, positioning, and bus routing), but with its source edits (such as fades, trims, and loop points) still intact.  |  |  | | --- | --- | | [警告] | 警告 | | If you use the Play - Bypass properties shortcut, the resulting sound might be uncomfortably loud or off-pitch. |  单击 Transport 的 Play 按钮会从播放光标的位置播放片段。当播放光标前进时单击 Play 按钮将添加新的播放光标，并从第一个播放光标的起始位置同时播放。 |
| (Delay) | 延迟。指示是否对 Event Action、Random Container 或 Sequence Container 应用了延迟。当存在延迟时，此图标在延迟期间变成蓝色。 |
| (Fade) | 淡变。指示是否对 Event Action、Random Container 或 Sequence Container 应用了淡变。如果存在淡变，则此图标在淡变期间会变成蓝色。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| Voice Volume（声部音量）。 | 对象输出到总线或发送至辅助总线之前的衰减（电平或振幅）。有关音量的详细信息，请参阅[“了解声部管线”一节](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线")。  默认值：0 范围：-400 至 400 单位：dB  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12 dB。您可以通过直接输入值或在编辑控件上移动鼠标来输入超出限制范围的值。 | |
| Voice Pitch | 声部音高。定义音频对象的播放速度。其中：  - 音高 0 = 正常速度。 - 音高 1,200 = 2 倍的速度。 - 音高 2,400 = 4 倍的速度。 - 音高 -1,200 = 0.5 倍的速度。 - 音高 -2,400 = 0.25 倍的速度  |  |  | | --- | --- | | [技巧] | 技巧 | | 1,200 音分相当于一个八度。 |  Default value: 0  Range: -2400 to 2400  Units: Cents |
| Voice Low-pass Filter | 声部低通滤波器。基于指定频率值针对高频进行衰减的递归滤波器。  此滤波器的单位表示低通滤波的百分比，其中 0 表示无低通滤波（信号不受影响）而 100 表示最大衰减。  有关更多详细信息，请参阅 [Wwise 中 LPF 和 HPF 值与截止频率的对应关系](../../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系") 页面。  单位：%  Default value: 0  Range: 0 to 100 |

---