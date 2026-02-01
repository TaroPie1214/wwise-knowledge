# Parametric EQ（参数均衡器）

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > Parametric EQ（参数均衡器）

## Parametric EQ（参数均衡器）

为了增强声音，有时需要创建能够影响音频信号频率分量的效果器。通过使用 Parametric EQ 插件，您可以应用各种滤波器塑造声音频谱。

Parametric EQ 包含一系列属性，可用于为音频环境创建各种效果。许多这些属性还可使用 RTPC 映射至游戏参数。 In addition, you have the flexibility of working in up to eight frequency bands where you can apply different properties to each band.

Parametric EQ 可作为 Object Processor（对象处理器）来使用。也就是说，它只会针对每条总线实例化一次，而不会针对每条总线上的每个 Audio Object（音频对象）实例化一次。这样做只是出于性能上的考虑，并不会影响信号处理的结果。有关详细信息，请参阅[“结合 Audio Object 使用效果器”一节](../../05-使用声音和振动来提升游戏体验/04-管理效果器/01-结合-Audio-Object-使用效果器.md "结合 Audio Object 使用效果器")。

### Parametric EQ Graph

The Parametric EQ plug-in contains a graph that displays the frequency response of the EQ's processing. When editing the Parametric EQ, the graph displays the frequency response of each band as individual curves as well as a curve of the frequency response of all bands accumulated together. When profiling, the graph displays an additional curve of the accumulated frequency response of all bands including any changes to properties from RTPCs and any contributions made from the Dynamic Gain.

The graph can also be used to edit certain the properties of each band. You can enable or disable each band by double-clicking their respective control point. The control points can be dragged horizontally to control the Frequency of each band. Depending on the band's filter type, you can also drag the control points vertically to control the Gain or Q of each band. You can use the mouse wheel to zoom the graph in and out vertically, which can be used to make fine-tuned adjustments to each band.

### Parametric EQ Dynamics

In addition to being able to dynamically adjust properties of the Parametric EQ effect through RTPCs, the effect can also dynamically adjust the Gain of each band based on an audio signal.

When Dynamics are enabled for any band, the Parametric EQ effect either reads the specified Sidechain Mix or it uses the input audio signal itself as the Dynamics Input signal. The Dynamics Input is mixed down to a single channel of audio, run through a filter-bank based on the properties of the bands which have Dynamics enabled, and then the root mean square of each filtered band of the Dynamics Input is metered. The metered value of each band of the Dynamics Input is used to calculate a new Dynamic Gain, based on the Dynamics Threshold and Range specified for the band. Finally, this Dynamic Gain is added to whatever the Gain of the specified band is set to.

To monitor the processing for the Dynamics Input, expand the splitter to the right to view the Dynamics Input and Dynamics Gain meters. The Dynamics Input meter shows the metered result of each filtered band of the Dynamics Input. The Dynamics Gain meter shows the calculated Dynamic Gain being applied to each band.

With these Dynamics features, you can use the Parametric EQ as a dynamic EQ such as those used in some DAWs. For example, you can use these features to correct the volume of specific bands of audio when they get too loud, perform frequency-based ducking across different portions of your audio mix, or automatically apply other adjustments in order to improve the overall clarity of your mix.

### Soloing Bands

The Parametric EQ effect allows for specific bands of audio to be listened to when profiling the sound engine.

You can click the **Solo Band** button to enable a different operating mode for the Parametric EQ effect. When Solo Band is active, the effect applies a filter on the input audio based on the properties of the active band to isolate just the portion of the audio affected by the active band and uses that as the output audio of the effect. For example, when soloing a band configured as a Low Shelf filtered with a cut-off frequency of 500Hz, the output audio is isolated to just the portion of the input audio at 500Hz and lower, and not apply any other processing to the signal. This can be used to inform what portion of the audio mix is affected by each band in the EQ.

Similarly, you can click the **Solo Band Dynamics Input** button to listen to one of the filtered bands of the Dynamics Input in isolation from all other processing. When Solo Band Dynamics Input is active, the effect applies a filter on the Dynamic Input audio, and uses that as the output audio of the effect. This shows what audio is driving each band of the Dynamics Input.

When the Solo Band is active, note that all other audio rendering in the sound engine is still active, as this only affects the audio processing of the Parametric EQ effect. To listen to one of the bands of audio in isolation of your entire mix, other audio busses might need to be muted or other effects might need to be bypassed.

### Parametric EQ 属性

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
| Enable | 启用。决定是否激活给定频段并做相应处理。  Default value: false |
| Type | 类型。决定给定频段应用哪种滤波器：  - **Low Pass Flat** —— 低通。从指定频率中提供高频率的固定斜率衰减。 在低于该点时，信号具有平坦的频率响应；但在截止频率点以上，频率越高衰减得越厉害。衰减的速率可通过 Rolloff 属性来控制。 - **High Pass Flat** —— 高通。从指定频率中提供低频率的固定斜率衰减。 在高于该点时，信号具有平坦的频率响应；但在截止频率点以下，频率越低衰减得越厉害。衰减的速率可通过 Rolloff 属性来控制。 - **Low Pass Q** – 从给定频率开始对高频成分实施衰减。藉此，可基于 Q 值在截止频率处调高音量；在截止频率点以下，频率越高衰减越厉害。衰减的速率可通过 Rolloff 属性来控制。 - **High Pass Q** – 从给定频率开始对低频成分实施衰减。藉此，可基于 Q 值在截止频率处调高音量；在截止频率点以下，频率越低衰减越厉害。衰减的速率可通过 Rolloff 属性来控制。 - **Band Pass** —— 带通。拒绝指定中心频率周围的所有频率。 中心周围的频率范围由 Q 进行控制。 - **Notch** —— 带阻。为指定频率范围的固定衰减提供一个不同的宽度。 中心周围的频率范围由 Q 进行控制。 - **Low Shelf** —— 低架。为指定范围的低频率提供增益/衰减。 此曲线类型也被称为 Bass Tone Control（低音控制）。 - **High Shelf** —— 高架。为指定范围的高频率提供增益/衰减。 此曲线类型也被称为 Treble Tone Control（高音控制）。 - **Peaking** —— 峰值。为指定频率范围的放大/衰减提供一个不变的宽度。 峰值周围的频率范围由 Q 进行控制。  Default value: Peaking |
| Gain | 增益。定义将给定频段的音频信号放大多少。  在选择 Low Pass Flat、High Pass Flat、Low Pass Q、High Pass Q、Notch 或 Band Pass 曲线时，Gain 控件不可用，因为这些滤波器类型会将通带归一化为 0 dB 或其独立于 Gain 运作。  Default value: 0  Range: -24 to 24  Units: dB |
| Frequency | 频率。定义在给定频段受滤波器影响的频谱部分。  Default value: 9000  Range: 20 to 20000  Units: Frequency |
| Quality Factor | 品质因数。定义对给定频段来说中心频率附近受增益变化影响的区间。对于 Band Pass、Peaking 和 Notch 滤波器，在设置较低的 Q 值时带宽较宽，在设置较高的 Q 值时带宽较窄。对于 Low Pass Q 和 High Pass Q 滤波器，在设置较低的 Q 值时会在截止频率附近调低滤波器的音量，在设置较高的 Q 值时会在截止频率附近调高滤波器的音量。  在将 Filter Type 设为 Low Pass、High Pass、Low Shelf 或 High Shelf 时，此控件不可用。  Default value: 1  Range: 0.025 to 100 |
| Rolloff | 滚降。定义给定频段的滤波器在截止频率以上的衰减速率。  Rolloff 属性仅在将给定频段的滤波器类型设为 Low Pass Flat、High Pass Flat、Low Pass Q 或 High Pass Q 时可用。  单位：dB/八度  Default value: 12 dB/oct |
| Dynamics Enable | 动态启用。决定是否激活对给定频段的 Gain 的动态调整。跟其他 Dynamics 属性一样，此属性仅在将给定频段的 Filter Type 设为 Low Shelf、High Shelf 或 Peaking 时可用。  Default value: false |
| Dynamics Threshold | 动态阈值。定义经过频段滤波后的 Dynamics Input 的电平超过多少即开始在给定频段应用 Dynamic Gain。  Default value: 0  Range: -60 to 24 |
| Dynamics Range | 动态范围。定义 Dynamic Gain 最多可在给定频段应用多大的增益偏置。若此值为负，则 Dynamic Gain 也将为负，对给定频段起到压缩的作用。若此值为正，则 Dynamic Gain 也将为正，对给定频段起到扩展的作用。  Default value: 0  Range: -30 to 30 |
| Dynamics Attack | 动态起音。定义在 Dynamics Input 测得音量升高到给定频段的阈值以上时 Dynamic Gain 达到目标值需要多长时间。  单位：s  Default value: 0.1  Range: 0 to 2 |
| Dynamics Release | 动态释音。定义在 Dynamics Input 测得音量降低到给定频段的阈值以下时 Dynamic Gain 趋于零需要多长时间。  单位：s  Default value: 0.1  Range: 0 to 2 |
| Output Gain | 输出增益。Parametric EQ 效果器的总体输出电平。  Default value: 0  Range: -24 to 24  Units: dB |
| Num Bands | 频段数目。定义效果器有多少个可用频段。在设为较低数值时能以比禁用频段还要好一点的效果降低 CPU 和内存成本。  Default value: 3  Range: 1 to 8 |
| Process LFE | 决定是否在 LFE 声道中处理效果。选中后，将在 LFE 声道中进行效果处理。如果未勾选该选项，则 LFE 声道不会受影响。  Default value: true |
| Sidechain Mix Source | 旁链压缩混音来源。指向用于 Dynamics Input 的 Sidechain Mix 对象。若未指定 Sidechain Mix，则将效果器的输入音频用作 Dynamics Input。 |
| Sidechain Mix Scope | 旁链压缩混音作用域。定义从 Sidechain Mix 接收音频时 Sidechain Mix Scope 的 ID。  在将 Scope 设为 Global 时，Sidechain Mix Scope 的 ID 为 0。  在将 Scope 设为 Game Object 时，Sidechain Mix Scope 的 ID 为与 Bus 或 Voice 绑定的 Game Object ID。  Default value: Global |

---