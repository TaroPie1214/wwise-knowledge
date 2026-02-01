# Voices Graph 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Voices Graph 选项卡

### Voices Graph 选项卡

声部图。Advanced Profiler — Voices Graph 选项卡实时显示底层声音引擎管理的声部或播放实例用到的经过优化的总线层级结构。

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
| 视图 | 单击 **View** 选择按钮来显示或隐藏视图中的以下元素：  - **Game Objects**：在视图中显示或隐藏游戏对象。 - **Events**:：在 Graph 视图中显示或隐藏事件。 - **Targets**：在视图中显示或隐藏目标。  目标是指事件要播放的目标对象，目标对象播放时会触发其子音源。在目标为 Random Container 时，启用此选项将同时显示作为事件目标的 Random Container 及其播放的源对象。 - **Virtual Voices**：在视图中显示或隐藏虚声部。 - **Devices**：在视图中显示或隐藏最终输出设备。 - **Volumes**：在视图中显示或隐藏音量值。 - **LPF**：在视图中显示或隐藏 LPF 值。 - **HPF**：在视图中显示或隐藏 HPF 值。 - **DSF**: Displays or hides the DSF values in the graph view. |
| 坐标图视图 | 显示声音引擎生成的各个声部的结构和内容。有关更多信息，请参阅以下 [“坐标图视图”一节](01-Voices-Graph-选项卡.md#graph_view "坐标图视图") 部分。 |

#### 坐标图视图

游戏中所播放的各元素的信息将显示在图表中。这些元素基本上都是各种类型的 Wwise 对象，它们会根据前后关系从左到右进行排列，从游戏对象开始，接下来是事件及其目标（如 Container、State 和 Switch），然后到声音和音乐对象，最后是总线结构输出。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 您可以单击图表中的任何元素，在 Property Editor 中打开它。 |

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| 坐标图中不显示 Not Mixing 状态的总线。有关各种处理状态的详细信息，请参阅[“了解总线图标和处理状态”一节](../../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态")章节。 |

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| 为了使振动对象的总线层级结构恰当地显示在 Voices 选项卡中，您需要在电脑上安装适当的振动设备驱动程序。 |

结构中每个元素之间的关系用线条来表示，并且包含元素信息。For example, hovering over or clicking on an object highlights its entire path: parent objects, child objects, and connection lines. 音频对象和 Auxiliary Bus（辅助总线）之间由虚线连接。红色虚线表示延迟。在音量输出旁边，会以毫秒为单位显示延迟量。

|  |
| --- |
|  |

如果 Auxiliary Bus 在当前音频帧中正在进行混音，那么后续到达的辅助发送信号就会出现延迟。Wwise 必须等待下一个音频帧，才能将新的辅助发送信号进行混音。为了避免这种情况，请勿向更低层级的 Auxiliary Bus 进行辅助发送。

![](../../../../../images/AP_Effect_Graph_Example1.png)

|  |  |
| --- | --- |
|  | The large light grey box (BP\_WaterGush\_01\_Spigot4\_3...) represents the Game Object that is associated with the Event (Fountain\_Splash\_02) and Sound SFX (Fountain Splash 02). |
|  | The blue boxes represent the Event (Fountain\_Splash\_02) and the Sound SFX (Fountain Splash 02) objects. Numbers and icons indicate the relative volume level in decibels, low-pass filter (0-100), and high pass filter (0-100). |
|  | The large light grey box represents the Listener Game Object (PlayerCameraManager\_2147...) that is associated with the Busses and their applied effects. Numbers and icons indicate the relative volume level in decibels. |
|  | The yellow box (AK Convolution Reverb) beneath the Bus (AkReverbZone\_4) represents the Effect applied on the Bus. Numbers and icons indicate the relative volume level in decibels. |
|  | Click the small grey circle to view the volume and amount of latency in milliseconds applied to this connection. |

Voice Graph 选项卡中的数据仅在各个捕获周期收集一次。但是，您可以使用 Performance/Voice Monitor 中的时间光标来浏览不同时间段的数据。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 列出所有游戏对象，例如在Advanced Profiler的[“Capture Log”一节](../01-Capture-Log/00-Capture-Log.md "Capture Log")或[“Voices（语音）”一节](02-Voices（语音）.md "Voices（语音）")和[“Voices Graph 选项卡”一节](01-Voices-Graph-选项卡.md "Voices Graph 选项卡")选项卡中，有一个特定的快捷菜单，其中包含以下选项：  - **Mute Game Object**：将该游戏对象关联的所有音频对象静音。 - **Unmute Game Object**：为该游戏对象关联的所有音频对象取消静音。 - **Solo Game Object**：间接地将其他游戏对象关联的所有音频对象静音。 - **Unsolo Game Object**：为其他游戏对象关联的所有音频对象取消静音。 - **Search Game Object in Voice Graph**：打开 Advanced Profiler 的 [“Voices Graph 选项卡”一节](01-Voices-Graph-选项卡.md "Voices Graph 选项卡") 选项卡，将其 Filter 设置为指定的游戏对象。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

---