# Voice Explorer

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [Profiler 视图](00-Profiler-视图.md) > Voice Explorer

## Voice Explorer

Voice Explorer 会依据性能分析捕获会话中的当前时间光标来显示正在播放的声部。同时按照正在播放的实例来组织声部，每发送一次 Event 都对应一个正在播放的实例。比如，在针对同一 Event 调用 **PostEvent** 两次时，会在 Voice Explorer 中生成两个正在播放的实例。Voice Explorer 提供有多个组织选项，方便按照 Game Object、Event Name 和 Event Target 进行分行。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 您可以通过在以下某个视图的时间线上单击来快速更改性能分析器时间光标的位置：Voice Monitor、Performance Monitor、Game Sync Monitor。在 Wwise 工具栏中单击 **LIVE** 来与最新数据同步。 |

| 筛选器工具栏 | |
| --- | --- |
| This view includes a filtering toolbar, which allows you to reduce the amount of information displayed in the view so you can focus on specific elements. 有关更多详细信息，请参阅 [“在性能分析视图中筛选数据”一节](../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/03-在性能分析视图中筛选数据.md "在性能分析视图中筛选数据") 章节。 | |
|  | |
|  | **Unlink Filter**：禁止在多个筛选器视图之间同步。 |
|  | **Text Filter**：通过指定文本来筛选内容。系统会将您所指定的字词与内容中所含名称或字符串的开头进行匹配。键入的字词越多，显示的结果越细化。匹配项不区分大小写。有关高级用法的信息，请参阅“[“使用性能分析器筛选器表达式”一节](../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/04-使用性能分析器筛选器表达式.md "使用性能分析器筛选器表达式")”。 |
|  | **Object Filter**：通过指定 Wwise 对象来筛选内容。系统会将您所指定的 Wwise 工程对象与视图中的内容进行匹配。同时，还会依据对象关系（如父子对象关系和输出总线关系）对内容进行匹配。 |
|  | **Browse Object Filter**：显示 Project Explorer 浏览器，以便选择所要筛选的对象。 |
|  | **Mute/Solo Filtering**：若启用，则从结果中排除激活了 Mute 的对象，而只显示激活了 Solo 的对象。 |
|  | **Options**：显示其他操作。 |

| 界面元素 | 描述 |
| --- | --- |
| 视图选项 | - **Toggle Game Object visibility**：按照 Game Object 和正在播放的实例组织并列出声部。 - **Toggle Event visibility**：按照 Event 和正在播放的实例组织并列出声部。 - **Toggle Event Target visibility**：按照 Event Target 和正在播放的实例组织并列出声部。 |
| 声部列表 | 按照正在播放的实例组织并列出正在播放的声部。各列因视图选项而异。  属性列：    - **Mute/Solo**：将 Game Object、Target 或 Sound 对象设为 Mute 或 Solo 状态。 - **Game Object**：在调用 PostEvent 时指定的游戏对象（只有在**没有**激活 Toggle Game Object visibility 选项时才会显示）。 - **Event**：产生声音的 Event 的名称（只有在**没有**激活 Toggle Event visibility 选项时才会显示）。 - **Target**：产生声音的 Event Target 的名称（只有在**没有**激活 Toggle Event Target visibility 选项时才会显示）。 - **Name**：Game Object、Event、Target 或 Sound 对象的名称。 - **ID**：Game Object ID、Event ID、Target ID 或 Sound ID。 - **Bus**：输出总线的名称。 - **Listener**：与游戏对象关联的听者。 |

**相关主题**

- [“使用 Voice Inspector 分析声部”一节](../../07-完善工程/06-性能分析/10-使用-Voice-Inspector-分析声部.md "使用 Voice Inspector 分析声部")

---