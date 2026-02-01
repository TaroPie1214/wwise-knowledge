# Event Action 列表

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Events 选项卡](../00-Events-选项卡.md) > [Event Editor](00-Event-Editor.md) > Event Action 列表

#### Event Action 列表

下表显示了 Wwise 中可用的不同 Action（动作）类型的完整列表。单击链接可查看与各个 Event Action 相关的参数。

|  |  |
| --- | --- |
| [Play](01-Event-Action-列表.md#bp1304732) |  |
| Stop | [Stop](01-Event-Action-列表.md#bp1304811), [Stop All](01-Event-Action-列表.md#bp1304876) |
| Pause | [Pause](01-Event-Action-列表.md#bp1305022), [Pause All](01-Event-Action-列表.md#bp1305118), [Resume](01-Event-Action-列表.md#bp1305304), [Resume All](01-Event-Action-列表.md#bp1305389) |
| [Break](01-Event-Action-列表.md#bp1304789) |  |
| Seek | [Seek](01-Event-Action-列表.md#bp1307910)、[SeekAll](01-Event-Action-列表.md#bp1308071) |
| [Post Event](01-Event-Action-列表.md#bp1404489) |  |
| Bus Volume | [Set Bus Volume](01-Event-Action-列表.md#set_bus_volume), [Reset Bus Volume](01-Event-Action-列表.md#reset_bus_volume), [Reset Bus Volume All](01-Event-Action-列表.md#reset_bus_volume_all) |
| Voice Volume（声部音量）。 | [Set Voice Volume](01-Event-Action-列表.md#bp1305913), [Reset Voice Volume](01-Event-Action-列表.md#bp1306039), [Reset Voice Volume All](01-Event-Action-列表.md#bp1306112) |
| Voice Pitch（声部音高） | [Set Voice Pitch](01-Event-Action-列表.md#bp1306605), [Reset Voice Pitch](01-Event-Action-列表.md#bp1306765), [Reset Voice Pitch All](01-Event-Action-列表.md#bp1306834) |
| Voice Low-pass Filter | [Set Voice Low-pass Filter](01-Event-Action-列表.md#bp1306981), [Reset Voice Low-pass Filter](01-Event-Action-列表.md#bp1307108), [Reset Voice Low-pass Filter All](01-Event-Action-列表.md#bp1307181) |
| Voice High-pass Filter（声部高通滤波器）。 | [Set Voice High-pass Filter](01-Event-Action-列表.md#bp1306981_1), [Reset Voice High-pass Filter](01-Event-Action-列表.md#bp1307108_1), [Reset Voice High-pass Filter All](01-Event-Action-列表.md#bp1307181_1) |
| Mute（静音） | [Mute](01-Event-Action-列表.md#bp1305621), [UnMute](01-Event-Action-列表.md#bp1305694), [UnMute All](01-Event-Action-列表.md#bp1305767) |
| Game Parameter（游戏参数） | [Set Game Parameter](01-Event-Action-列表.md#bp1405913)、[Reset Game Parameter](01-Event-Action-列表.md#bp1307039) |
| States（状态） | [Enable State](01-Event-Action-列表.md#bp1307396), [Disable State](01-Event-Action-列表.md#bp1307421), [Set State](01-Event-Action-列表.md#bp1307327) |
| [Set Switch](01-Event-Action-列表.md#bp1307446) |  |
| [Trigger （触发器）](01-Event-Action-列表.md#bp1307865) |  |
| Bypass Effect（旁通效果器） | [Enable Bypass](01-Event-Action-列表.md#bp1307514), [Disable Bypass](01-Event-Action-列表.md#bp1307595), [Reset Bypass Effect](01-Event-Action-列表.md#bp1307676), [Reset Bypass Effect All](01-Event-Action-列表.md#bp1307738) |
| [Release Envelope](01-Event-Action-列表.md#release_envelope) |  |
| [Reset Playlist](01-Event-Action-列表.md#reset_playlist) |  |
| Set Effect | [Set Effect](01-Event-Action-列表.md#event_action_set_effect)、[Reset Set Effect](01-Event-Action-列表.md#event_action_reset_set_effect)、[Reset Set Effect All](01-Event-Action-列表.md#event_action_reset_set_effect_all) |

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| 下表详细列出了各项 Action 属性。However, in the Event properties pane, the **Hide or Show Properties** shortcut menu option prompts the [“Object Property Settings”一节](../../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings") dialog where you can select which of these properties to hide or display. |

  

| Action 类型和属性 | 描述 |
| --- | --- |
| **Play** | 播放关联 Wwise 对象。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 范围。指定为哪些游戏对象应用 Action。  对于 Play 动作，Scope 始终为 Game Object。 |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Probability | 概率。概率值定义 Play Action 的执行概率。  单位：%  Default value: 100  Range: 0 to 100 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| **Stop** | 停止。停止关联 Wwise 对象的播放。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Stop All** | 全部停止。停止播放所有 Wwise 对象，但可添加[例外](00-Event-Editor.md#add_exceptions)。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| Resume State Transitions | 指定 Stop All 是否也包括恢复状态之间任何暂停的转换。  |  |  | | --- | --- | | [备注] | 备注 | | 只有当 Action Scope 设为 Global 时，此选项才可用。 |  Default value: true |
| Apply to Dynamic Sequences | 应用至动态序列。指定 Action 的 All 选项是否同时包含动态序列。这些动态序列 [需在 SDK 中编程以便配合 Dialogue Event 使用](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__dynamicdialogue.html) 。  Default value: true |
| **Pause** | 暂停。暂停关联 Wwise 对象的播放。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| Include Delayed Resume Actions | 是否暂停 Wwise 对象的延迟 Resume 动作。如果勾选该选项，则延迟了的 Resume 动作将会暂停。如果未勾选该选项，则延迟了的 Resume 动作将不会暂停，并且对象将在延迟周期结束之后恢复播放。  Default value: true |
| **Pause All** | 停止所有对象的播放，但可以添加[例外](00-Event-Editor.md#add_exceptions)。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| Apply to State Transitions | Specifies if the “All” of the Action also includes any Transitions between States for the Target.  |  |  | | --- | --- | | [备注] | 备注 | | 只有当 Action Scope 设为 Global 时，此选项才可用。 |  Default value: true |
| Apply to Dynamic Sequences | 应用至动态序列。指定 Action 的 All 选项是否同时包含动态序列。这些动态序列 [需在 SDK 中编程以便配合 Dialogue Event 使用](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__dynamicdialogue.html) 。  Default value: true |
| Include Delayed Resume Actions | 是否暂停 Wwise 对象的延迟 Resume 动作。如果勾选该选项，则延迟了的 Resume 动作将会暂停。如果未勾选该选项，则延迟了的 Resume 动作将不会暂停，并且对象将在延迟周期结束之后恢复播放。  Default value: true |
| **Resume** | 续播。恢复播放之前暂停的关联 Wwise 对象。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| Master Resume | Clears all pause actions applied to the associated Wwise 对象.  如果选中，应用于 Wwise 对象的所有暂停动作将被清除，导致 Wwise 对象恢复播放。如果未选中，则只清除一个暂停动作，保留其他暂停动作。  对象应用了多个暂停动作时，简单的恢复动作将无法恢复对象的播放。要强制播放，您必须使用 Master resume 选项。  Default value: false |
| **Resume All** | 全部继续。继续播放所有暂停的 Wwise 对象，但可添加[例外](00-Event-Editor.md#add_exceptions)。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| Apply to State Transitions | Specifies if the “All” of the Action also includes any Transitions between States for the Target.  |  |  | | --- | --- | | [备注] | 备注 | | 只有当 Action Scope 设为 Global 时，此选项才可用。 |  Default value: true |
| Apply to Dynamic Sequences | 应用至动态序列。指定 Action 的 All 选项是否同时包含动态序列。这些动态序列 [需在 SDK 中编程以便配合 Dialogue Event 使用](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__dynamicdialogue.html) 。  Default value: true |
| Master Resume | Clears all pause actions applied to the associated Wwise 对象.  如果选中，应用于 Wwise 对象的所有暂停动作将被清除，导致 Wwise 对象恢复播放。如果未选中，则只清除一个暂停动作，保留其他暂停动作。  对象应用了多个暂停动作时，简单的恢复动作将无法恢复对象的播放。要强制播放，您必须使用 Master resume 选项。  Default value: false |
| **Break** | 中断。停止播放循环声音、振动对象或连续容器，但允许当前对象播放完毕。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| **Seek** | 更改关联 Wwise 对象的播放位置。  此操作不会影响当前未播放的对象。  如需了解 Seek 事件动作相关备注和限制的完整列表，请参阅下文 [“Seek/SeekAll 备注和限制”一节](01-Event-Action-列表.md#seek_seekall_notes_and_restrictions "Seek/SeekAll 备注和限制") 部分。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Seek Type | 跳转位置使用什么类型的值。共有以下值可用：  - **Percent**（百分比，默认类型）：以声音总时长的百分比来表示跳转位置。 - **Time**:*Time*\*（时间）：以文件开始后的时间的绝对值来表示跳转位置，单位为秒。  Default value: Percent |
| Seek Percent | 以声音总时长的百分比来表示跳转位置。此时长会将循环考虑在内。例如，定位到自己循环两次的声音的 50% 会将光标置于第二次循环的开头。  无限循环的声音是一种例外情况，因为时长是无限的。在此类情况下，有效跳转位置的计算会以声音未循环来进行计算，然后通过考虑循环来应用。因此，不可能在无限循环声音的循环区域之后（“尾声部分”）进行跳转。  在音乐段落内进行定位时，定位是相对于 Entry Cue（开始提示）进行的并且对象持续时间由 Entry Cue 和 Exit Cue（退出提示）进行定义。因此，不可能在 Entry Cue 之前（Pre-Entry（预开始））或在 Exit Cue 之后（Post-Exit（退出后））进行定位。  单位：%  Default value: 0  Range: 0 to 100 |
| Seek Time | 以时间绝对值来表示跳转位置。此时长会将循环考虑在内。例如，跳转到自己循环两次的 10 秒声音的 10 秒处会将光标置于第二次循环的开头。  同样，不可能在无限循环声音的循环区域后（在结尾部分）进行定位。  在音乐段落内进行跳转时，跳转是相对于 Entry Cue 进行的。因此，不可能在 Entry Cue 之前（前导段）进行定跳转但是，可以使用此选项在 Exit Cue 之后（后尾段）进行跳转。  单位：s  Default value: 0  Range: 0 to 3600 |
| Seek To Nearest Marker | 将最近的标记点作为跳转位置。在标记导入到 Wwise 时将标记嵌入到波形文件中并予以保留。  在音乐段落内进行定位时，此选项旨在将有效的位置和 Segment Editor 中编写的最近的 Segment Custom Cue（段落自定义提示点）或 Segment Entry Cue（段落开始提示点）对齐。Exit Cue 将始终会被忽略。  Default value: false |
| **SeekAll** | 更改所有 Wwise 对象的播放位置，但可以添加[例外](00-Event-Editor.md#add_exceptions)。  此操作不会影响当前未播放的对象。  如需了解 SeekAll 事件动作相关备注和限制的完整列表，请参阅下文 [“Seek/SeekAll 备注和限制”一节](01-Event-Action-列表.md#seek_seekall_notes_and_restrictions "Seek/SeekAll 备注和限制")。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Seek Type | 跳转位置使用什么类型的值。共有以下值可用：  - **Percent**（百分比，默认类型）：以声音总时长的百分比来表示跳转位置。 - **Time**:*Time*\*（时间）：以文件开始后的时间的绝对值来表示跳转位置，单位为秒。  Default value: Percent |
| Seek Percent | 以声音总时长的百分比来表示跳转位置。此时长会将循环考虑在内。例如，定位到自己循环两次的声音的 50% 会将光标置于第二次循环的开头。  无限循环的声音是一种例外情况，因为时长是无限的。在此类情况下，有效跳转位置的计算会以声音未循环来进行计算，然后通过考虑循环来应用。因此，不可能在无限循环声音的循环区域之后（“尾声部分”）进行跳转。  在音乐段落内进行定位时，定位是相对于 Entry Cue（开始提示）进行的并且对象持续时间由 Entry Cue 和 Exit Cue（退出提示）进行定义。因此，不可能在 Entry Cue 之前（Pre-Entry（预开始））或在 Exit Cue 之后（Post-Exit（退出后））进行定位。  单位：%  Default value: 0  Range: 0 to 100 |
| Seek Time | 以时间绝对值来表示跳转位置。此时长会将循环考虑在内。例如，跳转到自己循环两次的 10 秒声音的 10 秒处会将光标置于第二次循环的开头。  同样，不可能在无限循环声音的循环区域后（在结尾部分）进行定位。  在音乐段落内进行跳转时，跳转是相对于 Entry Cue 进行的。因此，不可能在 Entry Cue 之前（前导段）进行定跳转但是，可以使用此选项在 Exit Cue 之后（后尾段）进行跳转。  单位：s  Default value: 0  Range: 0 to 3600 |
| Seek To Nearest Marker | 将最近的标记点作为跳转位置。在标记导入到 Wwise 时将标记嵌入到波形文件中并予以保留。  在音乐段落内进行定位时，此选项旨在将有效的位置和 Segment Editor 中编写的最近的 Segment Custom Cue（段落自定义提示点）或 Segment Entry Cue（段落开始提示点）对齐。Exit Cue 将始终会被忽略。  Default value: false |
| **Post Event** | 发送事件。从事件内触发别的事件。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 范围。指定为哪些游戏对象应用 Action。  对于 Post 动作，Scope 始终设为 Game Object。 |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| **Set Bus Volume** | 设置音量。更改关联 Wwise 总线的音量电平。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| Volume | Wwise 总线音量的变化。音量电平的变动方式，具体取决于值是绝对值，还是相对值。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +96。您可以通过直接输入值，或在编辑控件上移动鼠标来输入超出限制范围的值。 |  单位：dB  Default value: 0  Range: -200 to 200  Units: dB |
| Absolute/Relative | 绝对/相对。设置如何应用 Action：  - **Absolute**:直接使用指定值。 - **Relative**:目标值将按指定量增减。  Default value: Absolute |
| **Reset Bus Volume** | 重置音量。将关联 Wwise 总线的音量复位至其原始电平。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Reset Bus Volume All** | 重置所有音量。将所有 Wwise 总线的音量复位至其原始值, although [exceptions](00-Event-Editor.md#add_exceptions) can be added.。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Set Voice Volume （启用旁通）** | 设置音量。更改关联 Wwise 对象的音量电平。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| Volume | Wwise 总线音量的变化。音量电平的变动方式，具体取决于值是绝对值，还是相对值。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +96。您可以通过直接输入值，或在编辑控件上移动鼠标来输入超出限制范围的值。 |  单位：dB  Default value: 0  Range: -200 to 200  Units: dB |
| Absolute/Relative | 绝对/相对。设置如何应用 Action：  - **Absolute**:直接使用指定值。 - **Relative**:目标值将按指定量增减。  Default value: Absolute |
| **Reset Voice Volume** | 重置音量。将关联 Wwise 对象的音量复位至其原始电平。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Reset Voice Volume All** | 重置所有音量。将所有 Wwise 对象的音量复位至其原始值, although [exceptions](00-Event-Editor.md#add_exceptions) can be added.。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Set Voice Pitch** | 设置音高。更改关联 Wwise 对象的音高。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| Voice Pitch | 声部音高。音高的变化。  音高的修改方式，具体取决于值是绝对值，还是相对值。  Default value: 0  Range: -4800 to 4800 |
| Absolute/Relative | 绝对/相对。设置如何应用 Action：  - **Absolute**:直接使用指定值。 - **Relative**:目标值将按指定量增减。  Default value: Absolute |
| **Reset Voice Pitch** | 重置音高，将关联对象的音高复位至其原始值。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Reset Voice Pitch All** | 重置所有声部音高。将所有 Wwise 对象的音高恢复至其原始值，但可添加[例外](00-Event-Editor.md#add_exceptions)。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Set LPF** | 更改作用于关联 Wwise 对象的低通滤波器效果量。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| Low-Pass Filter | 低通滤波器。Wwise 对象 Low-Pass Filter 的变化量。低通滤波器的修改方式，具体取决于值是绝对值，还是相对值。  单位：%  Default value: 0  Range: -100 to 100 |
| Absolute/Relative | 绝对/相对。设置如何应用 Action：  - **Absolute**:直接使用指定值。 - **Relative**:目标值将按指定量增减。  Default value: Absolute |
| **Reset LPF** | 将作用于关联 Wwise 对象的低通滤波器效果量复位至其原始值。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Reset LPF All** | 将作用于所有 Wwise 对象的 Low-Pass Filter 效果量复位至其原始值，但可以添加[例外](00-Event-Editor.md#add_exceptions)。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Set HPF** | 设置高通滤波器。更改作用于关联 Wwise 对象的高通滤波器效果量。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| High-Pass Filter | Wwise对象High-Pass Filter 数值的变化。高通滤波器的修改方式，具体取决于值是绝对值，还是相对值。  Default value: 0  Range: -100 to 100 |
| Absolute/Relative | 绝对/相对。设置如何应用 Action：  - **Absolute**:直接使用指定值。 - **Relative**:目标值将按指定量增减。  Default value: Absolute |
| **Reset HPF** | 重置高通滤波器。将作用于关联 Wwise 对象的高通滤波器效果量复位至其原始值。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Reset HPF All** | 将应用于所有 Wwise 对象的高通滤波器数量恢复至其原始值, although [exceptions](00-Event-Editor.md#add_exceptions) can be added. |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **Mute（静音）** | 将关联 Wwise 对象静音。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| **UnMute** | 解除静音。将关联 Wwise 对象恢复为其“静音前”的原始音量电平。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| **UnMute All** | 将所有 Wwise 对象恢复为其原始“静音前”音量电平, although [exceptions](00-Event-Editor.md#add_exceptions) can be added. |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| **Set Game Parameter** | 更改游戏参数值。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-in Curve | 定义 Action 的淡入曲线形状。  Default value: Linear |
| Value | 值。Game Parameter 的目标值。值修改的方式，具体取决于值是绝对值还是相对值。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围是有限的。您可以通过直接输入值，或在编辑控件上移动鼠标来输入超出限制范围的值。 |  Default value: 0 |
| Absolute/Relative | 绝对/相对。设置如何应用 Action：  - **Absolute**:直接使用指定值。 - **Relative**:目标值将按指定量增减。  Default value: Absolute |
| Bypass Game Parameter Interpolation | 旁通游戏参数插值。该选项用于旁通 Game Parameter 的内部渐变。  Default value: false |
| **Reset Game Parameter** | 重置游戏参数。将 Game Parameter 值改回默认值。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Fade Time | Action 逐渐生效所需的时间。  渐变将在指定的延迟（如果存在）后开始。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Curve | 淡出曲线。用于定义 Action 如何淡出的曲线形状。  Default value: Linear |
| Bypass Game Parameter Interpolation | 旁通游戏参数插值。该选项用于旁通 Game Parameter 的内部渐变。  Default value: false |
| **Enable State** | 在应用 Disable State Action 后，为相关 Wwise 对象重新启用 State。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 范围。指定为哪些游戏对象应用 Action。  对于 Enable State 动作，Scope 始终设为 Global。 |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| **Disable State** | 为关联 Wwise 对象禁用状态。  |  |  | | --- | --- | | [技巧] | 技巧 | | 此功能基本上可以用 State 的 **None**（无）选项来替代。在很多情况下，将全局 State 目标更改为 **None** 更为简便；不过，有时仍需为特定 Wwise 对象调用 **Disable State** 事件动作。 | |
| Target | 目标。Action 的应用对象。 |
| Scope | 范围。指定为哪些游戏对象应用 Action。  对于 Disable State 动作，Scope 始终为 Global。 |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| **Set State** | 激活特定状态。  The State Group and State, selected in the Action Properties group, are displayed in the **Objects** column. |
| Target | 目标。Action 的应用对象。 |
| Scope | 范围。指定为哪些游戏对象应用 Action。  对于 Set State 动作，Scope 始终为 Global。 |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| **Set Switch** | 激活特定切换开关。  所选 Switch Group（切换开关组）和 Switch（切换开关）显示在 **Objects** 列中。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 范围。指定为哪些游戏对象应用 Action。  对于 Set Switch 动作，Scope 将始终为 Game Object。 |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| **Trigger （触发器）** | 调用 Trigger，以启动 Stinger。  所选 Trigger 显示在 Objects 列中。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| **Enable Bypass （启用旁通）** | 旁通作用于关联 Wwise 对象的效果器。  |  |  | | --- | --- | | [备注] | 备注 | | 只有使用同一范围选项（All 或者 Specific）时，Enable Bypass 和 Disable Bypass 动作才会相互影响。若针对效果器应用了 Enable/Disable Bypass 动作，必须使用相同范围的选项才能撤消该动作。 |  例如：使用选项 Specific 的 Enable Bypass 仅可使用带选项 Specific 的 Disable Bypass 进行撤消。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Bypass All | 全部旁通。决定是否旁通对象上插入的所有效果器。若选中复选框，则移除所有效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的所有效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| Bypass | 旁通。决定是否旁通所选效果器实例。若选中复选框，则移除效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的某些效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| **Disable Bypass** | 禁用旁通。取消 Effect 旁通设置，并将 Effect 重新应用于相关的 Wwise 对象。  |  |  | | --- | --- | | [备注] | 备注 | | 只有使用同一范围选项（All 或者 Specific）时，Enable Bypass 和 Disable Bypass 动作才会相互影响。若针对效果器应用了 Enable/Disable Bypass 动作，必须使用相同范围的选项才能撤消该动作。 |  例如：使用选项 Specific 的 Enable Bypass 仅可使用带选项 Specific 的 Disable Bypass 进行撤消。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Bypass All | 全部旁通。决定是否旁通对象上插入的所有效果器。若选中复选框，则移除所有效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的所有效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| Bypass | 旁通。决定是否旁通所选效果器实例。若选中复选框，则移除效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的某些效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| **Reset Bypass Effect** | 重置旁通效果器。将关联对象的旁通效果器选项复位至其原始设置。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Bypass All | 全部旁通。决定是否旁通对象上插入的所有效果器。若选中复选框，则移除所有效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的所有效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| Bypass | 旁通。决定是否旁通所选效果器实例。若选中复选框，则移除效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的某些效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| **Reset Bypass Effect All** | 将所有 Wwise 对象的旁通效果选项复位至其原始值，但可以添加[例外](00-Event-Editor.md#add_exceptions)。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Bypass All | 全部旁通。决定是否旁通对象上插入的所有效果器。若选中复选框，则移除所有效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的所有效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| Bypass | 旁通。决定是否旁通所选效果器实例。若选中复选框，则移除效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的某些效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| **Release Envelope** | 释音包络。使[包络调制器](../../05-ShareSets-选项卡/04-Modulator-Editor-视图/02-调制器包络.md "调制器包络")进入释音段，从而结束延音段。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| **Reset Playlist** | 重置播放列表。返回 [Sequence Container](../../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/02-Property-Editor-Random-Container-and-Sequence-Cont.md "Property Editor: Random Container and Sequence Container")（序列容器）播放列表的开头，而不播放下一对象。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 通过以下两个选项指定 Action 应用于哪些游戏对象：  - **Game object**，将事件动作作用于触发事件的游戏对象。 - **Global**，将事件动作作用于所有游戏对象。  Default value: Game Object |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| **Set Effect** | 设置效果器。覆盖指派给 Wwise 对象上的单个效果器插槽的效果器。  |  |  | | --- | --- | | [备注] | 备注 | | 被 "Set Effect" Action 覆盖的效果器可被 SDK 进一步覆盖。若在性能分析期间将效果器指派给了 Wwise 对象，则该效果器在优先级上高于被覆盖的效果器。 | |
| Target | 目标。Action 的应用对象。 |
| Scope | 范围。指定为哪些游戏对象应用 Action。  对于 "Set Effect" Action，Scope 始终为 Global。 |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Effect Slot | 效果器插槽。对象的效果器链中的位置。  |  |  | | --- | --- | | [备注] | 备注 | | 该值是从零开始的。也就是说，第一个 Effect Slot 的位置为 0。 |  Default value: 0  Range: 0 to 254 |
| Target Effect | 目标效果器。要指派给 [Target](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#assigning_objects_to_event_actions "将目标指派给 Event Action") 的效果器链的给定 [Effect Slot](../../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#applying_an_effect_shareset_to_an_object "将 Effect ShareSet 应用于 Wwise 对象") 的效果器。 |
| **Reset Set Effect** | 重置“设置效果器”。将被 "Set Effect" Action 覆盖的某个对象的给定效果器插槽重置。 |
| Target | 目标。Action 的应用对象。 |
| Scope | 范围。指定为哪些游戏对象应用 Action。  对于 "Set Effect" Action，Scope 始终为 Global。 |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Effect Slot | 效果器插槽。对象的效果器链中的位置。  |  |  | | --- | --- | | [备注] | 备注 | | 该值是从零开始的。也就是说，第一个 Effect Slot 的位置为 0。 |  Default value: 0  Range: 0 to 254 |
| **Reset Set Effect All** | 重置所有“设置效果器”。将被 "Set Effect" Action 覆盖的所有对象的给定效果器插槽重置。 |
| Scope | 范围。指定为哪些游戏对象应用 Action。  对于 "Set Effect" Action，Scope 始终为 Global。 |
| Delay | 延时，执行 Action 之前的时间量。  单位：s  Default value: 0  Range: 0 to 600 |
| Effect Slot | 效果器插槽。对象的效果器链中的位置。  |  |  | | --- | --- | | [备注] | 备注 | | 该值是从零开始的。也就是说，第一个 Effect Slot 的位置为 0。 |  Default value: 0  Range: 0 to 254 |

##### Seek/SeekAll 备注和限制

- 创建 Event 时，若要从第一个 Wwise 声音对象的特定位置开始播放，请在 Seek 动作之后添加 Play 动作。
- 在跳转时不执行任何音量淡入淡出，因此在声音播放期间进行跳转则可能导致爆音。
- Music Playlist Container（音乐播放列表容器）和振动对象不支持跳转。
- 当声音是插件源时，如果插件中实现了跳转，则跳转将由插件执行。当前，只有 [“Silence”一节](../../../../10-Wwise-插件/03-源插件/06-Silence/00-Silence.md "Silence") 支持跳转。
- 跳转仅适用于当前播放的声音。您不能使用此选项以在属于连续序列部分的对象之间跳转。
- 如果跳转位置大于声音长度，则声音将停止播放。
- 如果播放声音的其中一个上层对象是具有以下特殊过渡的连续（随机或序列）容器，则跳转将失败：

  - Trigger rate（触发率）
  - 交叉淡变（幅度）
  - 交叉淡变（功率）
  - 精确到采样点（只有在当前播放的声音是连续序列的第一个声音时，跳转才会对连续序列生效并做精确到采样点的过渡。）
- 跳转时间或百分比会将循环（和循环区域）考虑在内（请参阅“Seek percent”和“Seek time”参数的说明）。
- 在跳转之后，播放可能会因流播放延迟而延迟。在 Music Segment 这种情形中，此延迟等于段落的预读时间（请参阅音乐轨的属性）。段落的预读时间是所有采用流播放的子音轨中最大的流播放预读值。

**相关主题**

- [“创建新的 Event”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#creating_new_event "创建新的 Event")
- [“将 Action 添加到 Event”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#adding_actions_to_an_event "将 Action 添加到 Event")
- [“将目标指派给 Event Action”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#assigning_objects_to_event_actions "将目标指派给 Event Action")
- [“定义 Event Action 的作用域”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#defining_scope_of_an_event_action "定义 Event Action 的作用域")
- [“设置 Event Action 的属性”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#setting_properties_for_an_event_action "设置 Event Action 的属性")
- [“播放 Event”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#playing_back_an_event "播放 Event")
- [“重命名事件”一节](../../../../04-与游戏互动/01-管理-Event/03-处理-Event.md#renaming_an_event "重命名事件")
- [“从 Event 中移除 Action”一节](../../../../04-与游戏互动/01-管理-Event/03-处理-Event.md#removing_actions_from_an_event "从 Event 中移除 Action")
- [“替换指派给 Event Action 的目标”一节](../../../../04-与游戏互动/01-管理-Event/03-处理-Event.md#replacing_objects_assigned_to_event_actions "替换指派给 Event Action 的目标")
- [“删除 Event”一节](../../../../04-与游戏互动/01-管理-Event/03-处理-Event.md#deleting_events "删除 Event")

---