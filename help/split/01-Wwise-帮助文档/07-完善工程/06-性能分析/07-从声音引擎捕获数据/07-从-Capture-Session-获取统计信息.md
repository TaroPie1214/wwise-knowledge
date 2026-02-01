# 从 Capture Session 获取统计信息

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [性能分析](../00-性能分析.md) > [从声音引擎捕获数据](00-从声音引擎捕获数据.md) > 从 Capture Session 获取统计信息

### 从 Capture Session 获取统计信息

在 Capture Session（捕获会话）期间或捕获结束后，您可以随时用 Wwise 分析捕获的信息，来获取 Wwise 工程或游戏中特定音频元素相关的统计数据。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 目前，仅限 Dynamic Dialogue（动态对话）的相关信息可以从捕获会话中提取。为了完全理解统计信息，必须明确 Wwise 生成 Dynamic Dialogue 时涉及的各个步骤。有关 Dynamic Dialogue 的详细信息，请参阅[“了解 Dynamic Dialogue 系统”一节](../../../04-与游戏互动/02-管理动态对话/00-管理动态对话.md#understanding_dynamic_dialogue_system "了解 Dynamic Dialogue 系统")。 |

Profiler Statistics（Profiler 统计数据）视图显示了从 Capture Session 中提取的统计信息，其中包含一系列预定义的查询，方便获取 Capture Log（捕获日志）内各类信息的统计数据。比如，您可以获悉在 Capture Session 期间解析了哪些路径，解析次数和致使音频播放的次数。还可以筛选信息来缩小搜索范围，发现问题并确定必要的对策。

所有激活的 Capture Session 都可以用来提取统计数据，即对于游戏远程捕获的数据或 Wwise 本地捕获的数据，都可以提取相关统计信息。只要 Capture Log 中显示信息，就说明 Capture Session 处于激活状态。

**从 Capture Session 收集统计信息的方法如下：**

1. 启动本地或远程 Capture Session。
2. 在菜单栏中，点击 **Views** > **Profiler Statistics**（视图 > Profiler 统计数据）。

   Profiler Statistics 视图将打开。
3. 从 Queries 列表中，选择以下查询功能：

   - **Paths Used** -- 已使用的路径。表明哪些路径在 Capture Session 期间被解析或添加到动态序列列表中，路径被解析的次数，以及致使音频播放的次数。
   - **Paths Added** -- 已添加的路径。表明在 Capture Session 期间触发了哪些对白事件。对于触发的每个 Dialogue Event，都会显示添加到动态序列列表的对应音频对象，以及该对象被添加的次数。
   - **Dialogue Events Distribution** -- 对白事件分布。显示 Capture Session 期间触发的对白事件相关的统计信息，确切地说，它会显示每个 Dialogue Event 被解析的次数，以及实际触发音频对象播放的次数。
4. 点击 **Run**（运行）。

   查询的结果会显示在 Results（结果）中。
5. 用筛选器来排除不需要的信息。这样可以缩小搜索范围，并快速确定是否应采取必要对策。

---