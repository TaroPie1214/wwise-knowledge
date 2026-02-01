# Game Sync Monitor

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [Profiler 视图](00-Profiler-视图.md) > Game Sync Monitor

## Game Sync Monitor

Game Sync Monitor（游戏同步器监控器）会追踪 Game Parameter（游戏参数）、Modulator（即 LFO、Envelope 和 Time）和 MIDI 参数的 RTPC 值随时间的变化。有关如何设置 RTPC 值的详细信息，请参阅[集成详情 – RTPC](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_rtpc.html) 章节。

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
|  | **Group by Game Object**（按游戏对象分组）：将 Name 列中内容相同的多个行归为单个行并显示通用名称。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。识别 RTPC 或游戏对象（如选中 **Group by Game Object**）。 |
| Game Object | 游戏对象。识别与 RTPC 值关联的游戏对象（比如  [`AK::SoundEngine::SetRTPCValue`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html) 中指定的游戏对象）。 |
| Playing ID | 播放 ID。识别与 RTPC 值关联的播放 ID。您可以为通过调用  [`AK::SoundEngine::SetRTPCValueByPlayingID`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a7caeef1dde89425615aa37085469015a.html) 设置的 RTPC 值填充此字段，也可为 MIDI Target 上作用域为 Voice（声部）的调制器填充此字段。有关调制器作用域的详细信息，请参阅“[“Modulator Editor 视图”一节](../04-Project-Explorer/05-ShareSets-选项卡/04-Modulator-Editor-视图/00-Modulator-Editor-视图.md "Modulator Editor 视图")”章节。 |
| MIDI Target | Identifies the target node in the Containers hierarchy to which the associated MIDI Event was routed. 您可以为特定于 MIDI Target 的 RTPC 值填充此字段。比如，MIDI Target 上的 MIDI 参数（音符、力度和频率）或调制器。有关 MIDI Target 的详细信息，请参阅“[“理解 MIDI 内容和 MIDI 目标”一节](../../06-创建互动音乐/05-处理-MIDI.md#understanding_midi_content_and_midi_target "理解 MIDI 内容和 MIDI 目标")”和“[“MIDI category: music objects”一节](../04-Project-Explorer/01-Audio-tab/04-Containers-hierarchy-music-objects/05-Common-tabs-and-categories-music-objects/04-MIDI-category-music-objects.md "MIDI category: music objects")”章节。 |
| Pipeline ID | 管线 ID。识别要将 RTPC 值应用于哪个声部或总线实例。您可以为调制器作用域为 Note or Event（音符或事件）的 MIDI Target 填充此字段。Pipeline ID 对应于 Voice Explorer（声部资源管理器）和 Voice Inspector（声部检视器）中的 Target ID（目标 ID）或 Sound ID（声音 ID）。此列的快捷菜单可用于在 Voice Explorer 或 Voice Inspector 中显示对应条目。有关所述视图的详细信息，请参阅“[“Voice Explorer”一节](10-Voice-Explorer.md "Voice Explorer")”章节。 |
| Value | 值。显示 RTPC 的当前值。 |

---