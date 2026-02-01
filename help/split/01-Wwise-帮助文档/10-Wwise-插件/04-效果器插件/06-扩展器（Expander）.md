# 扩展器（Expander）

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > 扩展器（Expander）

## 扩展器（Expander）

（请参阅下文的 [“Expander properties”一节](06-扩展器（Expander）.md#expander_plug_in_properties "Expander properties")。）

Expander（扩展器）插件通过减弱输入信号低于预定义阈值的任意部分来扩大信号的动态范围。 当信号很弱并低于阈值时，扩展器开始降低信号的增益。当信号等于或高于阈值时，不对信号应用增益衰减。

比率因子决定当输入低于阈值时的动态扩展范围。 例如，比率 4 表示输入信号每低于阈值 4 dB，输出信号中仅会保留 1 dB。

|  |
| --- |
|  |

要在增益衰减区和无增益衰减区之间提供平滑的过渡，您可以指定 attack （起音）属性和 release（释音）属性的时间。 Attack 时间是指当输入低于阈值时增益衰减所花费的时间。 Release 时间是指当不再做增益衰减时，信号恢复至阈值电平所花费的时间。

|  |
| --- |
|  |

Expander 插件包含一系列属性，其中很多属性可实时编辑，并可使用 RTPC 映射至特定游戏参数。

您可以使用 Expander 插件减少不需要的背景噪音。 例如，您可能需要减少低音背景噪声（如嘶嘶声)，以使其它声音听得更清楚。 在某些情况下，您可以通过设置高扩展率（超过 10:1）将声音从输出信号中完全清除。 这一高比率被称为噪声门，因为对于增益已降到该范围的声音，此门将对这些声音关闭。

|  |  |
| --- | --- |
| [注意] | 注意 |
| 具有直流偏置的声音可能会改变 Expander 效果器的结果。 请确保先从音频文件中移除直流偏置后再在 Wwise 中应用 Expander Effect。 您可以在导入音频文件前移除直流偏置，也可以在 Wwise 中对音频文件做转码时移除。 |

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| The following are some general remarks on Wwise dynamic processing plug-ins:  - Compressor、Expander 或 Peak Limiter 插件中的 Ratio（比例）控件上不做插值（[RTPC](../../14-词汇表.md#glossary_rtpc "RTPC（实时参数控制）") 参数）。在播放期间更改此参数可能导致非常干净的信号中出现信号不连续。 - 具有[直流偏置](../../14-词汇表.md#glossary_dc_offset "DC Offset（直流偏置）")的声音可能改变压缩/扩展结果，因为旁链检测算法将发生大幅度偏移。在 Wwise 中使用声音之前应删除直流偏置。 - Compressor（压缩器）、Expander（扩展器）和 Peak limiter（峰值限幅器）是非线性音频处理。也就是说，处理顺序至关重要。例如，您在效果器之前或之后应用增益，结果将会有所不同。 - 对于第一个音频缓冲区，处理算法处于称为"非稳定"（non-steady）状态。因为[旁链](../../04-与游戏互动/05-使用-RTPC/08-Using-RTPCs-to-fine-tune-the-audio-mix.md "Using RTPCs to fine-tune the audio mix")估计信号功率时不清楚以前的情况，所以其在估计过程中可能有一小段时间内的信号功率估计是错误的（但前提是在声音开始播放时已使用了 Compressor）。解决此问题的方法（如果确实存在此问题）是以比率 1 启动 Compressor，一会儿之后再将其调为所需值。 - 如果 Compressor 应用某增益衰减并且突然被旁通了，则将会听到信号断续。一种可能的解决方案是在旁通效果器前将压缩比渐变为 1。 |

### Using Expander on an Audio Objects bus

“将线性效果器（如 [“Parametric EQ（参数均衡器）”一节](14-Parametric-EQ（参数均衡器）.md "Parametric EQ（参数均衡器）")）分别应用于多个 Audio Object”跟“将其统一应用于这些对象的下混”并无区别。然而，对大多数非线性效果器（如 Compressor 或 Expander）来说并非如此。不过，Expander 插件比较特殊，它属于对象处理器插件。在将 Expander 插入到 Audio Object（音频对象）总线上时会产生以下结果：

- 无论有多少个 Audio Object 输出到该总线，都只会针对每个总线实例将效果器实例化一次。
- 它可以通过作用于内部下混来实现对多个 Audio Object 的统一扩展，同时保留各个 Audio Object 而不对其实施下混。
- 所有 Audio Object 都会应用增益衰减。
- 在 Channel Linked 模式下，会实施隐式扩展。所以，Channel Link 选项并不起作用。

有关更多详细信息，请参阅 [“结合 Audio Object 使用效果器”一节](../../05-使用声音和振动来提升游戏体验/04-管理效果器/01-结合-Audio-Object-使用效果器.md "结合 Audio Object 使用效果器") 章节。

### Using Expander with a Sidechain Mix

By default, when no Sidechain Mix is specified as a Sidechain Input, the Expander Effect analyzes the input audio signal to evaluate how to modify the signal’s gain, apply that modification to the input audio signal, and use that as the output audio for the Effect. However, when a Sidechain Mix is specified as a Sidechain Input, the analysis instead receives the Sidechain Mix audio signal, uses that to evaluate the desired gain modification of the input audio signal, applies that modification to the input audio signal, and uses that as the output audio for the Effect.

有关详细信息，请参阅[“Using Sidechain Mixes with Effects”一节](../../05-使用声音和振动来提升游戏体验/04-管理效果器/04-Using-Sidechain-Mixes-with-Effects.md "Using Sidechain Mixes with Effects")。

### Expander properties

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
| Threshold | 阈值。指定一个点，低于该点时 Expander 开始处理信号，并应用增益衰减。  单位：dB  Default value: -40  Range: -96.3 to 0 |
| Ratio | 比率。表示已应用的扩展量。 比率为 2:1 表示低于阈值的输出电平部分将进一步减少，减幅是输入值的两倍。 当比率等于和高于 10:1 将创建一个噪声门。  Default value: 3  Range: 1 to 50 |
| Attack Time | 启动时间。指当输入低于阈值时增益衰减所花费的时间。  单位：s  Default value: 0.1  Range: 0 to 2 |
| Release Time | 释放时间。指不再应用增益衰减时信号恢复至阈值电平所花费的时间。  单位：s  Default value: 0.01  Range: 0 to 2 |
| Output Gain | 输出增益。动态扩展后作用于输出电平的增益。  Default value: 0  Range: -24 to 24  Units: dB |
| Process LFE | 决定是否在 LFE 声道中处理效果。选中后，将在 LFE 声道中进行效果处理。如果未勾选该选项，则 LFE 声道不会受影响。  Default value: true |
| Channel Link | 声道链路。将相同的增益衰减作用于所有声道。 这通过对所有声道的信号提取均方根功率来实现。 设置阈值的方法是针对已链接的声道缩放功率（单位：dB）。  如果未勾选该选项，声道之间将不会共享信息，各个声道将独立应用效果器。  Default value: true |
| Sidechain Mix | 旁链压缩混音。该 Sidechain Mix 将用作触发 Expander 工作的依据。  |  |  | | --- | --- | | [备注] | 备注 | | 若未设置，则将输入信号作为触发依据。 | |
| Sidechain Mix Scope | 旁链压缩混音作用域。旁链压缩混音的作用域，可为 Global 或 Game Object。  Default value: Global |

---