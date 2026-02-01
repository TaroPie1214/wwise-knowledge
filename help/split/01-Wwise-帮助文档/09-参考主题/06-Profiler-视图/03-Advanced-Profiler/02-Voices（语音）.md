# Voices（语音）

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Voices（语音）

### Voices（语音）

Advanced Profiler — Voice（声部）选项卡显示有关声音引擎在任一时刻管理的各个声部或播放实例的信息。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 为了使振动对象显示在 Voices 选项卡中，您需要在电脑上安装适当的振动设备驱动程序。 |

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| **Game Object** 、 **Target** 、 **Wwise Object** 和 **Bus** 列均显示相应的 Mute 和 Solo 按钮（如 [“Busses”一节](03-Busses.md "Busses") 选项卡文档中所述）。但请注意，游戏对象将对 Wwise 对象产生特殊的影响。如果游戏对象被静音，则其关联的所有 Wwise 对象都将会静音。如果游戏对象被独奏，那么只有其相关的 Wwise 对象可能会播放；这是由它们自身的 Mute 和 Solo 设置决定的。 |

| 筛选器工具栏 | |
| --- | --- |
| This view includes a filtering toolbar, which allows you to reduce the amount of information displayed in the view so you can focus on specific elements. 有关更多详细信息，请参阅 [“在性能分析视图中筛选数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/03-在性能分析视图中筛选数据.md "在性能分析视图中筛选数据") 章节。 | |
|  | |
|  | **Unlink Filter**：禁止在多个筛选器视图之间同步。 |
|  | **Text Filter**：通过指定文本来筛选内容。系统会将您所指定的字词与内容中所含名称或字符串的开头进行匹配。键入的字词越多，显示的结果越细化。匹配项不区分大小写。有关高级用法的信息，请参阅“[“使用性能分析器筛选器表达式”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/04-使用性能分析器筛选器表达式.md "使用性能分析器筛选器表达式")”。 |
|  | **Object Filter**：通过指定 Wwise 对象来筛选内容。系统会将您所指定的 Wwise 工程对象与视图中的内容进行匹配。同时，还会依据对象关系（如父子对象关系和输出总线关系）对内容进行匹配。 |
|  | **Browse Object Filter**：显示 Project Explorer 浏览器，以便选择所要筛选的对象。 |
|  | **Mute/Solo Filtering**：若启用，则从结果中排除激活了 Mute 的对象，而只显示激活了 Solo 的对象。 |
|  | **Options**：显示其他操作。 |

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Game Object | 与对象关联的游戏对象的名称。  |  |  | | --- | --- | | [技巧] | 技巧 | | 列出所有游戏对象，例如在Advanced Profiler的[“Capture Log”一节](../01-Capture-Log/00-Capture-Log.md "Capture Log")或[“Voices（语音）”一节](02-Voices（语音）.md "Voices（语音）")和[“Voices Graph 选项卡”一节](01-Voices-Graph-选项卡.md "Voices Graph 选项卡")选项卡中，有一个特定的快捷菜单，其中包含以下选项：  - **Mute Game Object**：将该游戏对象关联的所有音频对象静音。 - **Unmute Game Object**：为该游戏对象关联的所有音频对象取消静音。 - **Solo Game Object**：间接地将其他游戏对象关联的所有音频对象静音。 - **Unsolo Game Object**：为其他游戏对象关联的所有音频对象取消静音。 - **Search Game Object in Voice Graph**：打开 Advanced Profiler 的 [“Voices Graph 选项卡”一节](01-Voices-Graph-选项卡.md "Voices Graph 选项卡") 选项卡，将其 Filter 设置为指定的游戏对象。 | |
| Event | 触发了目标播放行为的事件名称。 |
| Target | 事件播放的目标对象。目标的播放已触发 Wwise 对象的播放。 |
| Wwise Object | Wwise 对象。声音引擎播放的对象名称。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| Bus | 总线。输出对象的总线的名称。 |
| Voice Volume（声部音量）。 | 声部音量。工程层级结构中定义的声部电平。该值的影响因素包括层级结构中所有父对象和总线的音量电平、状态、RTPC 和 Set Voice Volume 动作。 |
| Panning Volumes | 声像摆位音量。在声部被混入第一条混音总线的各个声道时声部的输出电平。此值严格表示各个声道的空间化增益。  有关声道顺序的说明，请参阅[“了解总线配置”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。 |
| Game-Defined Auxiliary Send Volume（游戏定义的辅助发送音量） | 游戏定义的辅助发送值偏置，以 dB 为单位。 |
| Total Volume | Volume of the voice plus the contributions from all mixing bus gains of the signal path, from the voice down to the Main Audio Bus inclusively. 当存在多条信号路径时，例如要使用辅助发送时，采取所有路径音量中的最大值。Total Volume 会与 Volume Threshold 计算评估，以用来决定是否转换到虚声部。它几乎包含 Wwise 中的所有音量偏置，但不包括那些属于归一化和补偿增益的偏置（请参见下方的 Normalization / Make-Up Gain 列）。 |
| Normalization / Make-Up Gain | 归一化／补偿增益。音量增益已作用于音频源，独立于 Wwise 中的其它逻辑音量。它来自补偿增益属性、响度归一化和局部音量偏置（音频源的补偿增益）。它不包含在 Total Volume 中，因此针对音量阈值评估声部时会予以忽略。它对 HDR 透明，并且 **Voice Monitor** 也不会予以考虑。  有关详细信息，请参阅[“HDR 和 Wwise 声部管线”一节](../../../07-完善工程/01-管理输出/09-使用-HDR/04-HDR-和-Wwise-声部管线.md "HDR 和 Wwise 声部管线")。 |
| Device | 设备。声音的传播媒介（比如，系统的主音频输出使用 **Main**，而 PS4、PS5、Xbox One 和 Xbox Series X 上的背景音乐扬声器则使用 **Background**）。 |
| Voice LPF | 声部低通滤波器。LPF 真正作用于主声部管线，此值包含 Base LPF、Occlusion（声笼） LPF 和声锥及距离衰减 LPF。 |
| Voice HPF | 声部 HPF。HPF 真正作用于主声部管线，此值包含 Base HPF、Occlusion HPF 和声锥及距离衰减 HPF。 |
| Priority | 优先级。优先级定义了同一个层级结构中各个对象的相对重要性。 |
| Virtual | 虚拟。表明对象正位于虚声部列表中。 |
| Over Limit | 超出上限。表明对象因为其播放实例数超过其节点播放数限幅器之一的限制而变成了虚对象。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

---