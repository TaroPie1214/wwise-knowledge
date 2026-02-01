# Profiler Statistics 视图

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > Profiler Statistics 视图

## Profiler Statistics 视图

在您已经完成捕获会话之后，您可以使用 Profiler Statistic（性能分析器统计）视图获取有关 Wwise 工程或游戏中某些音频元素的统计信息。您甚至可以一边正在捕获声音引擎来的信息，一边提取统计信息。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 目前，仅限 Dynamic Dialogue（动态对话）的相关信息可以从捕获会话中提取。为了完全理解统计信息，必须明确 Wwise 生成 Dynamic Dialogue 时涉及的各个步骤。有关 Dynamic Dialogue 的详细信息，请参阅[“了解 Dynamic Dialogue 系统”一节](../../../04-与游戏互动/02-管理动态对话/00-管理动态对话.md#understanding_dynamic_dialogue_system "了解 Dynamic Dialogue 系统")。 |

Profiler Statistic 视图包含一系列预定义查询功能，为您提供有关不同信息子集的统计信息。比如，您可以获悉在 Capture Session 期间解析了哪些路径，解析次数和致使音频播放的次数。您可以从任何活动的捕获会话中提取统计数据，也就是说您可以收集与从远程游戏捕获的数据或在 Wwise 内本地捕获的数据有关的统计信息。只要 Capture Log 中显示信息，就说明 Capture Session 处于激活状态。

Profiler Statistic 视图是上下文相关的，也就是说根据您已经选择的查询，视图中会显示不同的选项。以下查询可供选用：

- [“Profiler Statistics (Query - Paths Used)”一节](01-Profiler-Statistics-(Query-Paths-Used).md "Profiler Statistics (Query - Paths Used")")
- [“Profiler Statistics (Query - Dialogue Events Added)”一节](02-Profiler-Statistics-(Query-Dialogue-Events-Added).md "Profiler Statistics (Query - Dialogue Events Added")")
- [“Profiler Statistics (Query - Dialogue Events Distribution)”一节](03-Profiler-Statistics-(Query-Dialogue-Events-Distrib.md "Profiler Statistics (Query - Dialogue Events Distribution")")
- None - Profiler Statistics 视图中将不显示任何信息。

| 界面元素 | 描述 |
| --- | --- |
| Queries | 一系列预定义的查询，使用当前捕获会话显示有关特定子集的统计信息。 |
|  | 对当前捕获会话期间收集的信息运行所选查询。所有 Dialogue Event 信息都将显示在 Result 面板中。 |
|  | 清空所有查询中的累积统计数据。 |
| Update automatically | 自动更新。勾选该选项后，当有来自游戏的捕获数据时，所选查询将会实时更新。未勾选该选项时，可使用“Run”来手动更新数据。 |
| Keep statistics across sessions | 跨会话保存统计数据。在启用该选项的情况下，当新捕获会话开始时，不会清除统计数据。这允许针对许多不同游戏场景来累积统计信息。  |  |  | | --- | --- | | [注意] | 注意 | | 点击 **Run** 按钮将清除跨会话累积的数据并仅显示有关当前捕获会话的统计信息。 | |

---