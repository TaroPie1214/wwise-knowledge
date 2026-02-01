# Sidechain Send

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > Sidechain Send

## Sidechain Send

The Sidechain Send Effect sends an input audio signal to a Sidechain Mix.

When a Sidechain Mix is specified on the plug-in, the input audio signal is downmixed or upmixed to match the Sidechain Mix’s channel configuration, then sent to the Sidechain Mix. Other Effects can then receive the audio signal of the Sidechain Mix as a part of their audio processing.
You can only use Sidechain Send Effects on Audio and Auxiliary Busses, not on Voices.
The Sidechain Send effect is not an Object Processor and if the Sidechain Mix has a multi-channel configuration, the Effect might not correctly mix down audio objects with positioning data to the destination Sidechain Mix. Therefore, we recommend that you do not use the Sidechain Send effect on a Bus that operates in an Audio Objects configuration.
For more information on the Sidechain Mix system, see [“Using Sidechain Mixes with Effects”一节](../../05-使用声音和振动来提升游戏体验/04-管理效果器/04-Using-Sidechain-Mixes-with-Effects.md "Using Sidechain Mixes with Effects").

### Sidechain Send properties

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
| Sidechain Mix Destination | 旁链压缩混音目标。指向用于接收输入音频信号的 Sidechain Mix ShareSet。 |
| Scope | 作用域。定义从 Sidechain Mix 接收音频时 Sidechain Mix Scope 的 ID。  在将 Scope 设为 Global 时，Sidechain Mix Scope 的 ID 为 0。  在将 Scope 设为 Game Object 时，Sidechain Mix Scope 的 ID 为与 Bus 绑定的 Game Object ID。  Default value: Global |
| Volume | 音量。定义为调节输出音频而向 Sidechain Mix 所接收音频信号应用的增益。  默认值：0  取值范围：-96.3 ~ 24  单位：dB  Default value: 0  Range: -200 to 200  Units: dB |
| Delay Output | 延迟输出。若启用，则效果器的输出音频将延迟一个音频处理周期（约 10.6 ms）。不过，具体延迟时长可能会因声音引擎配置而有所不同。  您可以利用此延迟来将经过效果器处理的音频信号与读取 Sidechain Mix 的其他效果器精准同步。  Default value: false |

---