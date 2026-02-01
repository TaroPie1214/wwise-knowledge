# Performance Monitor

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > Performance Monitor

## Performance Monitor

Performance Monitor（性能监视器）显示有关性能的信息，包括声音引擎执行的各个活动的 CPU、内存和流播放等内容。在从声音引擎捕获到信息时，相应信息会以坐标图形式实时进行显示。曲线图的右侧列出了一系列关键性能计数器，用于显示图形中各时间点的实际性能。您可以通过在坐标图中拖动 Performance Monitor 的时间光标来查看特定时间点上各个计数器的性能。除此之外，还可按下 **Alt+逗点** (,) 来向左移动一个音频帧，或按下 **Alt+句点** (.) 来向右移动一个音频帧。

You can add, remove, or change the counters that are displayed in the Performance Monitor in the
[“Performance Monitor Setting”一节](01-Performance-Monitor-Setting.md "Performance Monitor Setting")
dialog. To open the Performance Monitor Settings dialog, click the View Settings icon in the title bar of the Performance Monitor.

| 界面元素 | 描述 |
| --- | --- |
|  | 单击视图右上角的 View Settings 图标以弹出 [“Performance Monitor Setting”一节](01-Performance-Monitor-Setting.md "Performance Monitor Setting") ，可在其中指定曲线图和性能数据列表中显示哪些内容。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| 坐标图视图 | 在捕获过程中会实时更新的一系列性能坐标图。其中会显示性能 [计数器](01-Performance-Monitor-Setting.md#profiler_counters) ，可以在 [“Performance Monitor Setting”一节](01-Performance-Monitor-Setting.md "Performance Monitor Setting") 的 **Show in Graph** 列中指定。  |  |  | | --- | --- | | [备注] | 备注 | | 性能坐标图将一直处于坐标图视图中，直到新捕获过程开始为止。 | |
|  | 向 Performance Monitor 视图的中心放大。 |
|  | 将坐标图视图重置为默认的 1:1 缩放比例。 |
|  | 从 Performance Monitor 坐标图视图中心缩小。 |
| 性能数据列表 | 性能[计数器](01-Performance-Monitor-Setting.md#profiler_counters)的列表，在捕捉过程中会实时更新相应数值，并且根据曲线图时间轴中的选定时刻显示数值。  可以在 [“Performance Monitor Setting”一节](01-Performance-Monitor-Setting.md "Performance Monitor Setting") 的 **Show in List** 列中选定要列出的的性能计数器。 |

**相关主题**

- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")
- [“自定义 Performance Monitor”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md#customizing_performance_monitor "自定义 Performance Monitor")
- [“从已有的远程捕获会话加载数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/09-从已有的远程捕获会话加载数据.md "从已有的远程捕获会话加载数据")
- [“Using keyboard shortcuts”一节](../../../02-入门/05-提供工作效率/00-提供工作效率.md#using_keyboard_shortcuts "Using keyboard shortcuts")

---