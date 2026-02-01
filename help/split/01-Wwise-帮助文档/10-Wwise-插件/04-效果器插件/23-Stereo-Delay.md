# Stereo Delay

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > Stereo Delay

## Stereo Delay

Stereo Delay（立体声延迟）插件可用于创建各种延迟效果器，这些效果器可反馈至左右平面上的的其它声道。 它可以用于创建大型立体声效果器（大于实际对象）或信号可在两边弹跳的效果（如乒乓延迟）。

### Stereo Delay 属性

Stereo Delay 插件包含一系列属性，其中很多属性可实时编辑，并可使用 RTPC 映射至特定游戏参数。

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
| **Left/Right Delay Parameters（左/右延迟参数）** | |
| Input | This parameter determines which channel(s) will be used to feed the corresponding (left or right) delay line.  值：  - **Left/Right**:分别使用左声道或右声道（默认设置）。 - **Center**:中置声道（如果有中置）会向延迟线提供信息。 - **Left/Right + Center**：左/右信号将与中置声道下混，来向延迟线提供信息。 - **None**:延迟线输入为无声。  Default value: Right |
| Enable Feedback | 启用反馈。该参数确定延迟线的输出是否反馈到同一延迟线的输入。  Default value: false |
| Feedback | Gain applied to the feedback path before its re-injection into the same delay line input.  |  |  | | --- | --- | | [警告] | 警告 | | 使用高反馈增益可累积产生极高的信号电平，具体取决于输入信号内容。 这样声音听起来会很大，而且有可能会损坏设备。 |  Default value: -12  Range: -48 to 0  Units: dB |
| Enable Crossfeed | 启用交叉馈送 L/R。该参数决定延迟线的输出是否反馈到其它声道上延迟线的延迟长度输入。 左延迟输出可向右延迟输入提供信息，反之亦然。 该设置可创建乒乓类型的立体声延迟。  Default value: false |
| Crossfeed | 交叉馈送 L/R 增益。在反馈路径重新注入另一声道的延迟线输入之前，作用于此反馈路径的增益。  |  |  | | --- | --- | | [警告] | 警告 | | 使用高交叉馈送增益可累积产生极高的信号电平，具体取决于输入信号内容。这样声音听起来会很大，而且有可能会损坏设备。 |  Default value: -12  Range: -48 to 0  Units: dB |
| **Filters 参数** | |
| Filter Type | 确定可作用于湿声信号的滤波类型。 可以使用以下筛选器：  - **None** —— 禁用该滤波器。 - **Low Pass** —— 低通。从指定频率中提供高频率的固定斜率衰减。 低于该点，信号几乎不受影响，但高于截止频率点时，频率越高，衰减逐步增大。 - **High Pass** —— 高通。从指定频率中提供低频率的固定斜率衰减。 高于该点，信号几乎不受影响，而低于截止频率点时，频率越低，衰减逐步增大。 - **Band Pass** —— 带通。拒绝指定中心频率周围的所有频率。 中心周围的频率范围由 Q 进行控制。 - **Notch** —— 带阻。为指定频率范围的固定衰减提供一个不同的宽度。 中心周围的频率范围由 Q 进行控制。 - **Low Shelf** —— 低架。为指定范围的低频率提供增益/衰减。 此曲线类型也被称为 Bass Tone Control（低音控制）。 - **High Shelf** —— 高架。为指定范围的高频率提供增益/衰减。 此曲线类型也被称为 Treble Tone Control（高音控制）。 - **Peaking** —— 峰值。为指定频率范围的放大/衰减提供一个不变的宽度。 峰值周围的频率范围由 Q 进行控制。  Default value: None |
| Filter Gain | 增益。作用于湿声信号所选频带上的放大量。 增大此值将“增强”音频信号。 减小此值将“削减”或衰减音频信号。  |  |  | | --- | --- | | [备注] | 备注 | | 当选择了 Low Pass、High Pass、Notch 和 Band Pass 曲线时，Gain 控件不可用，因为这些滤波器类型的通带已经归一化为 0 dB。 |  Default value: 0  Range: -24 to 24  Units: dB |
| Filter Frequency | 评率。频谱中将受到增益影响的部分。  单位：Hz  Default value: 1000  Range: 20 to 20000  Units: Frequency |
| Filter Q Factor | 品质因数。中心频率周围将受增益变化影响的区域。 低 Q 值表示带宽范围较宽，相反，高 Q 值表示带宽范围较窄。  当选择了 Low Pass、High Pass、Low Shelf 和 High Shelf 曲线时，该控制不可用。  Default value: 1  Range: 0.1 to 20 |
| **Output Levels（输出电平）** | |
| Dry Level | 干声电平。作用于未处理信号的增益。  Default value: 0  Range: -96 to 24  Units: dB |
| Wet Level | 湿声。作用于延迟信号的增益。  Default value: 0  Range: -96 to 24  Units: dB |
| Front/Rear Balance | F/R 平衡。立体声效果器的前置/后置对比。 例如值为 -100 时仅在前置声道有湿声信号。 值为 0 时前置和后置扬声器中都会有湿声信号。 值为 100 时将仅在后置声道中有湿声信号。  Default value: -100  Range: -100 to 100 |

---