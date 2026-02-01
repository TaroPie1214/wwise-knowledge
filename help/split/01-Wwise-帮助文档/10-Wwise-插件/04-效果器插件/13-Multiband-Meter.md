# Multiband Meter

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > Multiband Meter

## Multiband Meter

The Multiband Meter Effect is similar to the Meter Effect, but meters multiple frequency bands of the audio signal in one effect, and drives values for multiple game parameters. The Multiband Meter provides enhanced control over the frequency space of a mix, which you can use to implement advanced forms of side-chaining with RTPCs.

The Effect performs the following steps:

1. Downmixes the input audio signal into a single channel of data.
2. Performs a fullband measurement of the level of the audio signal.
3. Runs a bank of parallel Butterworth high-pass and low-pass filters to split the audio signal into multiple frequency bands.
4. Measures the level of each filtered audio signal.

It is also possible to monitor the filtered audio signals when Wwise is connected to the sound engine. Typically, the Multiband Meter Effect does not modify the output audio signal in any way. However, when one of the **Listen** check boxes is set, the output audio of the Multiband Meter Effect is replaced with one of the filtered audio signals used for the metering process. This is intended to be used for debugging purposes, in order to review which portion of the audio signal is being metered.

### Multiband Meter properties

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。效果器实例的名称。  效果器实例是一组效果器属性设置。它们可以是两种类型之一：自定义或共享集。自定义实例只能由一个对象使用，然而共享集可在多个对象之间共享。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |
| Notes | 备注。Effect 的其它信息。 |
| Metering | 电平测量。指示当前正在测量电平的对象的名称。 |
|  | 允许浏览其他要测量电平的对象。  |  |  | | --- | --- | | [备注] | 备注 | | 只有对于包含 VU 电平表的效果器，Effect Editor 中才会显示电平测量界面元素。 | |
|  | 设置 Effect Editor 中选定标签页的显示方式。默认情况下，整体面板中仅显示一个选定标签页。不过，您可以通过单击分隔器按钮将面板沿横向或纵向一分为二，显示两个不同的标签页。当前所选选项将以高亮背景色显示。  |  |  | | --- | --- | | [备注] | 备注 | | 无法同时在两个面板中显示同一标签页。若选中的标签页已在另一面板中显示，则另一面板将自动显示另一标签页。 | |

|  |  |
| --- | --- |
| Mode | 电平计量模式。 该插件可设置为跟踪峰值或 RMS。  - **Peak**:将电平表设为 Peak 模式。这样对瞬态的反应会更灵敏。 - **RMS**:将电平表设为 RMS 模式。这样一般对语音处理比较好。  Default value: RMS |
| Scope | - **Global**:将电平表设为作用于适用 Wwise 音频元素（总线、容器、Music Segment 等等）的所有输入，并将所述元素的多个游戏对象实例统一视为一个整体的游戏对象。 - **Game Object**:电平表将应用到每个游戏对象的输入信号。  Default value: Global |
| Infinite Hold | 无限保持。若启用，则将输出值无限期保持在启用该选项后监控到的最高电平。也就是说，输出值只会增大而不会减小。  在启用此选项时，Hold 属性值不起作用。  Default value: false |
| Apply Downstream Volume | 应用下游音量。启用后，电平表将显示在上层对象层级中作用的音量增益。 比如，若 Main Audio Bus 的音量增大 10，子级 Audio Bus 的音量减小 15，则其所有子对象将沿用 -5 的累计增益。虽然增益始终都能听到，但除非启用此选项，否则电平表不会显示。  Default value: false |
| **Per-Band Properties and Dynamics** | |
| **Output Game Parameter** | |
|  | When set, the output value is sent to this Game Parameter based on the playing instance's Scope, either a specific Game Object or globally.  |  |  | | --- | --- | | [技巧] | 技巧 | | 请确保所选 Game Parameter 的范围大于输出值范围。有关 Game Parameter 范围设置的详细信息，请参阅 [“Game Parameter Property Editor”一节](../../09-参考主题/04-Project-Explorer/04-Game-Syncs-选项卡/03-Game-Parameters/01-Game-Parameter-Property-Editor/00-Game-Parameter-Property-Editor.md "Game Parameter Property Editor")。 | |
| Low Freq | 高频截止。定义所要测量的频率范围的下限。为方便进行测量，系统会在此频率点执行高通滤波器处理。  单位：Hz  Default value: 800  Range: 20 to 20000  Units: Frequency |
| Low Roll-off | 高频滚降。定义所要测量的频率范围的滚降。值越高，计量范围附近的滚降越陡峭。  单位：dB/八度  Default value: 24 dB/Oct |
| High-Freq | 高频截止。定义所要测量的频率范围的上限。为方便进行测量，系统会在此频率点执行低通滤波。  单位：Hz  Default value: 16000  Range: 20 to 20000  Units: Frequency |
| High Roll-off | 高频滚降。定义所要测量的频率范围的滚降。值越高，计量范围附近的滚降越陡峭。  单位：dB/八度  Default value: Disabled |
| Attack | 启动时间。当监视电平超出当前输出值时，输出值升高 10 分贝所花费的时间。  单位：s  Default value: 0.0  Range: 0 to 10 |
| Hold | 保持。输出值从监控到的电平低于当前输出值时开始降低所花的时间。  在启用 Infinite Hold 时，此属性不起作用。  单位：s  Default value: 0  Range: 0 to 10 |
| Release | 释放时间。当监视电平低于当前输出值时，输出值降低 10 分贝所花费的时间。  单位：s  Default value: 0.1  Range: 0 to 10 |
| Min | 最小输出值。  Default value: -48  Range: -96.3 to 0 |
| Max | 最大输出值。  Default value: 0  Range: -96.3 to 12 |
| Listen | 监听。若选中，则将效果器的输出音频信号替换为当前针对给定频段测量的滤波音频信号。您可以据此进行调试来精准判定当前针对给定频段分析的音频内容。  同一时间只能监听一个频段。此属性不会一直起作用，只有在连接到正在运行的声音引擎实例时才会生效。 |

---