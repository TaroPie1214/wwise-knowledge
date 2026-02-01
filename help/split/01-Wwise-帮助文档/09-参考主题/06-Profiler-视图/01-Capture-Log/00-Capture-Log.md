# Capture Log

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > Capture Log

## Capture Log

Capture Log（捕获日志）用于捕获并记录来自声音引擎的所有信息。其中还包括特定的行为，例如游戏中触发的事件，或研发原型时在 Soundcaster 或 Game Simulator 中手动触发的事件。捕获的每条信息都会作为单独的条目记录在 Capture Log 中。双击 Capture Log 中的条目，即可在 Property Editor 或 Event Editor 中加载相关的 Wwise 对象或事件。此外，还可在条目上按下 Ctrl+\ 以便移动 Performance Monitor（性能监控器）中的时间光标，并将所有其他视图同步至同一时间。

您可以使用不同筛选条件（例如游戏对象类型、Wwise 对象名称或声音引擎执行的特定类型的活动）来筛选列表。您也可以将列表保存为 PROF 文件，以便之后在 Wwise 中重新加载它。或者，也可以选择一种文本文件格式导出，然后将其导入 Microsoft Excel 中进行排序和进一步分析。

除此之外，还可通过将 PROF 文件拖放到 Capture Log 视图上来从已有的 Profiler 捕获会话加载数据。

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
|  | 打开 Capture Log Options 视图。在此，可定义要按照怎样的条件来筛选 Capture Log 输出。 |
|  | 将 Capture Log 内容保存为 PROF 文件或制表符分隔的文本文件。文本文件将包含任何已作用于列表的筛选或分类。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| （标志） | 圆点的颜色随底色变化：在 Classic（经典）主题下显示为青绿色，在 Dark（深色）主题下显示为橙色。这样方便指示在距离 Performance Monitor 时间光标位置 100 ms 内捕获了 Capture Log 中的哪些条目。颜色越亮，条目离时间光标位置越近。您可以将光标强制移动至特定日志条目所在的时间戳：从快捷菜单 (Ctrl+\) 选择 **Move Cursor to Timestamp**（将光标移至时间戳）。或者直接双击时间戳。 |
| 关联圆点的颜色随底色变化：在 Classic（经典）主题下显示为深灰色，在 Dark（深色）主题下显示为白色。这样方便指示 Capture Log 中哪些条目是相互关联的。它们只有在日志中选择单个条目时才会显示。 |
| Timestamp | 时间戳。捕获该条目时的游戏时间。时间戳有助于识别在 Wwise 中模拟中 或游戏中发生的情形的精确时间。  |  |  | | --- | --- | | [技巧] | 技巧 | | 按下 Ctrl+\ 或双击时间戳可将 Game Profiler 光标移动至条目所对应的时间。 | |
| Type | 记录在 Capture Log 中的条目类型。有关[不同捕获信息类型](01-Capture-Log-Options.md#capture_log_types)的简短列表和说明，请参阅 Capture Log Options 页面。 |
| 描述 | 有关日志项的描述性信息。还可能包括属性值更改、状态更改等相关信息。 |
| Wwise Object Name | Wwise 对象名称。与日志条目关联的 Wwise 对象的名称（如存在）。  如果多个 Wwise 对象与日志项相关联，则会显示“Multiple Object”。如果没有与日志项相关联的 Wwise 对象，则会显示“No Element”。 |
| Wwise Object ID | Wwise 对象 ID。与日志条目关联的 Wwise 对象的 ID（如存在）。  如果多个 Wwise 对象与日志项相关联，则会显示“Multiple Object”。如果没有与日志项相关联的 Wwise 对象，则会显示“No Element”。  |  |  | | --- | --- | | [备注] | 备注 | | 在使用 Capture Log 中的搜索字段时，ID 必须完整且准确才会匹配。 | |
| Game Object Name（游戏对象名称） | 与日志项关联的游戏对象的名称。  “Transport/Soundcaster” 可跟没有关联游戏对象的 Wwise 对象所触发的条目相关。 |
| Game Object ID（游戏对象 ID） | 游戏对象 ID。与日志条目关联的游戏对象的 ID。  “Transport/Soundcaster” 可跟没有关联游戏对象的 Wwise 对象所触发的条目相关。  |  |  | | --- | --- | | [备注] | 备注 | | 在使用 Capture Log 中的搜索字段时，ID 必须完整且准确才会匹配。 | |
| Scope | 作用域。日志项作用于游戏内的对象的范围。作用域可以是两种类型之一：  - **Global**，意味着日志条目适用于所有游戏对象。 - **Game object**，意味着日志条目仅适用于在游戏对象列中的游戏对象。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“指定要捕获的信息类型”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/01-指定要捕获的信息类型.md "指定要捕获的信息类型")
- [“启动/停止捕获流程”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/02-启动停止捕获流程.md "启动/停止捕获流程")
- [“筛选 Capture Log”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/05-筛选-Capture-Log.md "筛选 Capture Log")
- [“使用 Capture Log 快捷菜单”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/06-使用-Capture-Log-快捷菜单.md "使用 Capture Log 快捷菜单")
- [“从 Capture Session 获取统计信息”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/07-从-Capture-Session-获取统计信息.md "从 Capture Session 获取统计信息")
- [“保存 Capture Log”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/08-保存-Capture-Log.md "保存 Capture Log")
- [“从已有的远程捕获会话加载数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/09-从已有的远程捕获会话加载数据.md "从已有的远程捕获会话加载数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")
- [“Capture Log Options”一节](01-Capture-Log-Options.md "Capture Log Options")
- [“Capture Log 中报告的错误”一节](02-Capture-Log-中报告的错误/00-Capture-Log-中报告的错误.md "Capture Log 中报告的错误")

---