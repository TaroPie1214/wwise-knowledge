# Profiler Statistics (Query - Dialogue Events Distribution)

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Profiler Statistics 视图](00-Profiler-Statistics-视图.md) > Profiler Statistics (Query - Dialogue Events Distribution)

### Profiler Statistics (Query - Dialogue Events Distribution)

“Dialogue Events Distribution”查询将显示捕获会话期间触发的 Dialogue Event 相关的统计信息。确切地说，它会显示每个 Dialogue Event 被解析的次数，以及实际触发音频对象播放的次数。您可以进一步深入发掘每个 Dialogue Event，查看解析了哪些路径及解析次数（实际数量和占总数的百分比）。有多个筛选器时，用来快速分类信息，以确定是否需要采取什么动作。

| 界面元素 | 描述 |
| --- | --- |
| **Filters** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Filter | 筛选器。您可以用于筛选所选查询找到的信息的筛选器类型。您可以使用以下任何筛选器来筛选信息：  - **Event Name** —— 显示有关特定 Dialogue Event 的信息 - **Added** —— 根据 Dialogue Event 被添加到动态序列中的次数来筛选信息。 - **Played** – 根据音频对象播放期间生成 Dialogue Event 的次数筛选信息。 |
| Parameters | 参数。一系列属性，用来为各个筛选器定义特定条件。  对于接受文本字符串的字段，您可以键入名称的一部分；但是不支持通配符。 |
| **Results** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Event Name | Dialogue Event 的名称。 |
| Added | 添加。解析对应 Dialogue Event 并将音频对象添加到动态序列列表的次数。 |
| Played | 播放。音频对象播放期间生成 Dialogue Event 的次数。 |
| Selected Event | 针对结果列表中选择的 Event ，显示其更多统计信息。 |
| **Filters** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Filter | 可用于筛选所选 Dialogue Event 信息的筛选器类型。您可以使用以下任何筛选器来筛选信息：  - **Value** —— 显示有关特定状态组或状态的信息。 - **Count** —— 基于路径被解析的次数筛选信息。 - **%** —— 基于路径被解析的实际百分比筛选信息。 |
| Parameters | 参数。用来为各个筛选器定义条件的属性。  对于接受文本字符串的字段，您可以键入名称的一部分；但是不支持通配符。 |
| **值分布** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Value | 当前捕获会话期间，显示所选 Dialogue Event 相关联的 State Group 和/或 State 的名称。 |
| Count | 相应状态在当前捕获会话中的发布次数。 |
| % | 百分比。相应状态的发布次数表示为在当前捕获会话期间发布的状态总数的百分比。 |

**相关主题**

- [“启动/停止捕获流程”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/02-启动停止捕获流程.md "启动/停止捕获流程")
- [“从 Capture Session 获取统计信息”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/07-从-Capture-Session-获取统计信息.md "从 Capture Session 获取统计信息")
- [“从已有的远程捕获会话加载数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/09-从已有的远程捕获会话加载数据.md "从已有的远程捕获会话加载数据")

---