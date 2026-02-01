# Effect Editor - McDSP ML1 Mastering Limiter Effect plug-in

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [合作伙伴插件](../00-合作伙伴插件.md) > [McDSP ML1 Mastering Limiter 插件](00-McDSP-ML1-Mastering-Limiter-插件.md) > Effect Editor - McDSP ML1 Mastering Limiter Effect plug-in

## Effect Editor - McDSP ML1 Mastering Limiter Effect plug-in

Effect Editor 会显示与 McDSP ML1 Mastering Limiter 插件有关的所有属性。

有关 McDSP ML1 Mastering Limiter 插件的概述，请参阅[*McDSP ML1 Mastering Limiter 插件*](00-McDSP-ML1-Mastering-Limiter-插件.md "McDSP ML1 Mastering Limiter 插件")。有关详细信息，请参阅 [McDSP 网站](https://mcdsp.com/plugin-index/ml4000/)。请注意：Wwise 实现的 McDSP ML1 Mastering 效果器可能与其网站上讨论的效果器略有不同。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Audiokinetic 的 McDSP ML1 Mastering Limiter 版本中使用的算法与 ProTools 略有不同。这些变化旨在满足以下特定条件：在处理过载的输入信号（最多 +12 dB）时，让输出中产生大量的削波失真。 |

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
| Ceiling | 上限。指定最大输出信号电平。  默认值：0 滑杆范围：-36 至 0  单位：dB |
| Thresh | 阈值。限幅器开始检测输入信号峰值时所要达到的信号电平。Ceiling 和 Threshold 之差是限幅器的最大补偿增益。  默认值：0 滑杆范围：-36 至 0  单位：dB |
| Knee | 拐点。指定限幅动作过渡，其中 0 产生一个正常的硬拐点，而 100 产生一个软拐点。  Knee 控件修改限幅器的增益结构，以减少失真，同时最大限度地提高输出电平。增大 Knee 控件将向限幅响应曲线添加软拐点。  默认值：0 滑杆范围：0 至 100  单位：百分比 |
| Release（释音） | 释音。限幅器从削减信号峰值中恢复的速率。释音时间越短，整体输出信号电平越高。  默认值：10 滑杆范围：1 至 5,000  单位：毫秒 |
| Mode | 模式。二次检测的类型，用于产生各种限幅类型，以适合各种输入信号和应用。您有以下选项：  - **Clean** —— 清晰模式。最透明的限幅器模式。信号电平将以最少的可测量失真量进行调整。 - **Soft** —— 软模式。略响于 Clean 模式，但也非常透明。 - **Smart** —— 智能模式。智能限幅会最大限度地减少信号失真，同时信号电平增加量比 Soft 模式多。 - **Dynamic** —— 动态模式。比 Smart 模式更响，并且在某些条件下会增加一点压缩造成的泵动突变效应。 - **Loud** —— 响亮模式。尽可能响，同时保持信号失真最小。 - **Crush** —— 强压模式。响于 Loud 模式，信号有些失真。 |
| （VU 电平表） | 显示音频信号（包括输入电平、输出电平以及作用于信号峰值的增益衰减电平）不同电平的一系列电平表。  要启用 VU 电平表，必须点击 Wwise 工具栏中的 Start Capture 按钮。  The VU meters only work when the ML1 effect has been applied to a bus in the Busses hierarchy. 对于 ShareSet 而言，必须在 Effect Editor 的 Shared by 列表中选中该总线。  |  |  | | --- | --- | | [备注] | 备注 | | 只有在立体声总线中使用该效果器时，电平表左右声道才是真实读数。对于所有其他配置来说，右声道将不使用，由左声道显示峰值。 | |
| In | 输入。显示输入音频信号的电平。 |
| GR | 增益衰减。显示作用于信号峰值的增益衰减量。 |
| Out | 输出。显示音频输出的电平。 |

---