# Time Stretch

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > Time Stretch

## Time Stretch

Time Stretch 插件可在确保不影响音高的情况下调节音频信号的速度和时长。该插件即可用于时间拉伸，也可用于时间压缩，并且可以在播放过程中采用时变时间缩放比例。 该插件适用于单音和复音。

|  |  |
| --- | --- |
| [注意] | 注意 |
| 1. This Effect is not recommended for music objects because it can have a negative    effect on timing. Alternatively, you can use the [Pitch Shifter](https://www.audikinetic.com/library/edge/?source=Help&id=wwise_pitch_shifter_plug_in) plug-in for music objects. 2. Time compression below 50% is not recommended for streamed assets. Higher pitches    might cause source starvation due to higher throughput required. Time Stretching on the    other hand is not a problem for streaming assets. |

### Choosing the window size

选择 Window Size（窗口大小）参数是获取高品质结果的重要步骤。 虽然默认值 (2048) 对大部分内容而言效果都很好，但要获得最佳的时间缩放效果及尽可能小的副作用，则微调该参数十分必要。虽然窗口大小设置得大一点可获得更佳的频率分辨率，但时域分辨率会相应变得不太准确，因此会导致瞬态信号变模糊。 因此调整窗口大小参数要在时间分辨率和频率分辨率之间达到妥协。

理想的窗口大小设置取决于音频内容：具有大量瞬态成分（如击打声、鼓声和爆炸声）的信号使用较小窗口时效果更好，而具有稳定频率内容的谐波信号（如语音和乐器）可能使用较大窗口时效果最好，因为这样可以获得更为准确的频率分辨率。

当用较大的时间拉伸设置来大幅放慢信号时，通常需要使用较大的窗口大小参数值，因为当慢速播放声音时，频率分辨率问题会变得非常显著。

### Algorithm choice

Time Stretch 插件允许根据需要选用两种时间拉伸算法：Classic 模式（Wwise 2021.1 及更早版本）和 Transient Preserving 模式。Transient Preserving 模式允许进一步微调品质水准和立体声处理。

### Time Stretch properties

Time Stretch 插件包含一系列属性，其中很多都可以实时编辑并利用 RTPC 映射到特定的 Game Parameter（游戏参数）。

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
| **Time** | |
| Time Stretch | 时间拉伸。原始声音时长的百分比。 100% 对应于无时间拉伸，而 200% 则对应两倍时长。 同样的，时间压缩也可实现，使用 50% 会使声音的时长减半。 该值支持 RTPC（实时参数控制），并可以在播放过程中平滑更改，不会产生副作用。  单位：原始时长的百分比  Default value: 100  Range: 25 to 1600 |
| Time Stretch Random | 时间拉伸随机。对指定的时间拉伸因子做一个随机的偏置，偏置的范围是正负 Time Stretch Rando 的值。 这将对目标 voice（声部）的整个时长有效。 播放过程中接收到的 RTPC 仅会在下一次播放时考虑进来。  单位：原始时长的百分比  Default value: 0  Range: 0 to 200 |
| **Pitch** | |
| Pitch Shift | 移调。该参数指定音高将提升或降低的量（单位为音分）。 具体说来，+1200 音分向上移调一个八度，-1200 向下移调一个八度。 该值支持 RTPC（实时参数控制），并可以在播放过程中平滑更改，不会产生副作用。  单位：音分  Default value: 0  Range: -4800 to 4800 |
| Pitch Shift Random | 时间变换随机。对 Pitch Shift 量施加偏置，范围为正负 Pitch Shift 随机值。在应用 Pitch Shift 的整个期间内，此设置对声部都有影响。播放过程中接收到的 RTPC 仅会在下一次播放时考虑进来。  单位：音分  Default value: 0  Range: 0 to 4800 |
| **Quality** | |
| Window Size | 窗口大小。窗口大一些可改进频率分辨率，但会让瞬态信号变模糊。 因此该参数是时间分辨率和频率分辨率之间妥协的结果。 请参阅以上章节，了解如何选择该参数值的详情。  单位：采样帧  Default value: 2048  Range: 256 to 8192 |
| Stretch Mode | 拉伸模式。要使用哪种时间拉伸算法。  以下选项可用：  - **Classic**:Time Stretch 使用 Wwise 2021.1 及更早版本的算法。 - **Transient Preserving**:Time Stretch 使用改进算法。在选中此模式时，Quality Level 滑杆允许对算法的性能进行微调，Stereo Processing 控件允许改进对复杂立体声混音的处理。  Default value: Classic |
| Quality Level | 品质级别。允许在适当降低声音品质的情况下对改进时间拉伸算法的性能进行精细控制。此控件仅在将 Stretch Mode 设为 Transient Preserving 时可用。  在将 Quality Level 设为 100 时，将对声音的所有部分进行处理。随着级别的降低，算法的 CPU 需求会下降，但声音品质会受影响。确切来说，在向下调节品质滑杆时会引入轻微的底噪或相位偏移效应，因为算法会跳过输入声音频谱的部分区间来节省计算资源。  建议在 Performance Monitor 中查看 CPU % 值的同时微调此参数。  Default value: 100  Range: 0 to 100 |
| **Output** | |
| Output Gain | 增益。在执行动态压缩后作用于输出信号的增益量，可弥补潜在增益损失。  Default value: 0  Range: -24 to 24  Units: dB |
| Stereo Processing | 立体声处理。用来处理立体声输入的方式。此控件仅在将 Stretch Mode 设为 Transient Preserving 时可用。  以下选项可用：  - **Left Right**:正常处理立体声输入。 - **Center Cut**:在应用时间拉伸之前将立体声输入拆分为左中右三个分量。它们随后会被重构为左声道和右声道。Center Cut 处理仅适用于立体声（2 声道）输入。  相较于 Classic 模式，Transient Preserving 模式会对声音的相位产生更大的影响。Center Cut 选项允许更好地保有复杂的立体声混音。  Default value: Left Right |

---