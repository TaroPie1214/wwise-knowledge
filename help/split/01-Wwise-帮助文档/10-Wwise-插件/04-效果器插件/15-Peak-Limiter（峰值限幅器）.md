# Peak Limiter（峰值限幅器）

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > Peak Limiter（峰值限幅器）

## Peak Limiter（峰值限幅器）

（请参阅下文的 [“Peak Limiter 属性”一节](15-Peak-Limiter（峰值限幅器）.md#wwise_peak_limiter_properties "Peak Limiter 属性")。）

Peak Limiter（峰值限幅器）插件效果器控制音频信号的动态范围。 实现方法是削弱对音频信号中暂时超出预定义信号峰值阈值的部分。要执行此处理，它利用预读时间（look-head time）检查信号峰值。 当音频信号恢复至可接受的值时，Peak Limiter 会停止削弱该信号。

|  |  |
| --- | --- |
| [注意] | 注意 |
| 预读时间会给输出信号带来延迟。 |

您可以使用 Peak Limiter 插件效果器限制音频信号的整体动态范围，并因此增加信号的总体可放大量。 您还可以使用它校平多个音频信号的增益，防止出现削波现象。 整体而言，这可以给人留下辨析度更高和冲击力更强的印象。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| To reduce clipping in your overall project, apply the Peak Limiter to the Main Audio Bus. |

下图显示了具有峰值 x 的音频信号。 如果不使用 Peak Limiter，则峰值 x 听起来将是一声突如其来的巨响。 图中的直线 c 表示音频信号的近似极限。 通过将 Peak Limiter 设置为直线 b 处的阈值，您可以消除最糟糕的超出音量，而不会对原始音频信号造成不利影响。

|  |
| --- |
|  |

比率系数确定当输入超出阈值时，峰值限幅器使用的动态压缩的程度。 例如，比率为 4 表示输入信号每超出阈值 4 dB，在输出信号中仅能观察到超出阈值 1 dB。

|  |
| --- |
|  |

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| The following are some general remarks on Wwise dynamic processing plug-ins:  - Compressor、Expander 或 Peak Limiter 插件中的 Ratio（比例）控件上不做插值（[RTPC](../../14-词汇表.md#glossary_rtpc "RTPC（实时参数控制）") 参数）。在播放期间更改此参数可能导致非常干净的信号中出现信号不连续。 - 具有[直流偏置](../../14-词汇表.md#glossary_dc_offset "DC Offset（直流偏置）")的声音可能改变压缩/扩展结果，因为旁链检测算法将发生大幅度偏移。在 Wwise 中使用声音之前应删除直流偏置。 - Compressor（压缩器）、Expander（扩展器）和 Peak limiter（峰值限幅器）是非线性音频处理。也就是说，处理顺序至关重要。例如，您在效果器之前或之后应用增益，结果将会有所不同。 - 对于第一个音频缓冲区，处理算法处于称为"非稳定"（non-steady）状态。因为[旁链](../../04-与游戏互动/05-使用-RTPC/08-Using-RTPCs-to-fine-tune-the-audio-mix.md "Using RTPCs to fine-tune the audio mix")估计信号功率时不清楚以前的情况，所以其在估计过程中可能有一小段时间内的信号功率估计是错误的（但前提是在声音开始播放时已使用了 Compressor）。解决此问题的方法（如果确实存在此问题）是以比率 1 启动 Compressor，一会儿之后再将其调为所需值。 - 如果 Compressor 应用某增益衰减并且突然被旁通了，则将会听到信号断续。一种可能的解决方案是在旁通效果器前将压缩比渐变为 1。 |

### Peak Limiter 属性

Peak Limiter 插件包含一系列属性，其中很多都可以实时编辑并利用 RTPC 映射到特定的 Game Parameter（游戏参数）。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 具有直流偏置的声音可能会改变 Peak Limiter 效果器的结果。 请确保先从音频文件中移除直流偏置后再在 Wwise 中应用 Peak Limiter。 |

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
| **Effect Settings** | |
| Threshold | 阈值。输入电平高于此电平时，Peak Limiter 压缩器将启用增益衰减。  单位：dB  Default value: 0  Range: -96.3 to 0 |
| Ratio | 比率。输入信号与超出阈值的输出信号之间的关系。 该值定义超出阈值的输出信号的斜率。  比率 4:1 表示输入信号每超出阈值 4 dB，在输出信号中仅保留 1 dB。  Default value: 10  Range: 1 to 50 |
| Look Ahead Time | 预读时间。用于检测即将出现的信号峰值的时间偏置。 该值正好等于 Peak Limiter 所引入的延迟。  单位：s  Default value: 0.01  Range: 0.001 to 0.02 |
| Release Time | 从输入电平低于阈值时起，到 Peak Limiter 停止增益衰减的时长。  单位：s  Default value: 0.1  Range: 0.001 to 0.5 |
| Output gain | 输出增益。在执行动态压缩步骤后作用于输出信号的增益量，动态压缩步骤用来补偿增益衰减过程会导致的潜在增益损失。  Default value: 0  Range: -24 to 24  Units: dB |
| Process LFE | 决定是否在 LFE 声道中处理效果。选中后，将在 LFE 声道中进行效果处理。如果未勾选该选项，则 LFE 声道不会受影响。  Default value: true |
| Channel Link | 声道链路。将相同的增益衰减作用于所有声道。 这通过对所有声道的信号提取均方根功率来实现。 设置阈值的方法是针对已链接的声道缩放功率（单位：dB）。  如果未勾选该选项，声道之间将不会共享信息，各个声道将独立应用效果器。  Default value: true |
| （VU 电平表） | 显示音频信号（包括输入电平、输出电平以及作用于信号峰值的增益衰减电平）不同电平的一系列电平表。  要启用 VU 电平表，必须点击 Wwise 工具栏中的 Start Capture 按钮。  The VU meters only work when the peak limiter effect has been applied to a bus in the Busses hierarchy. 对于 ShareSet 而言，必须在 Effect Editor 的“Shared by”列表中勾选该总线。 |
| Input | 输入。显示输入音频信号的电平。 |
| Gain Reduction | 增益衰减。显示作用于信号峰值的增益衰减量。 |
| Output | 输出。显示音频输出的电平。 |

---