# Profiler Statistics (Query - Dialogue Events Added)

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Profiler Statistics 视图](00-Profiler-Statistics-视图.md) > Profiler Statistics (Query - Dialogue Events Added)

### Profiler Statistics (Query - Dialogue Events Added)

“Dialogue Events Added”查询将显示在捕获会话期间触发了哪些 Dialogue Event。对于触发的每个 Dialogue Event，都会显示添加到动态序列列表的对应音频对象，以及该对象被添加的次数。同时有多个可用筛选器时，用来快速分类信息，以确定是否需要采取什么动作。

| 界面元素 | 描述 |
| --- | --- |
| **Filters** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Filter | 筛选器。可以用于筛选 Result 窗格中显示信息的筛选器类型。您可以使用以下任何筛选器来筛选信息：  - **Event Name** —— 显示有关特定 Dialogue Event 的相关信息。 - **Target Object** – 显示与特定音频对象有关的信息。 - **Count** – 根据针对各个 Dialogue Event 将特定音频对象添加到动态序列的次数筛选 Results 窗格中显示的信息。 |
| Parameters | 参数。一系列属性，用来为各个筛选器定义特定条件。  对于接受文本字符串的字段，您可以键入名称的一部分；但是不支持通配符。 |
| **Results** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Event Name | 事件名称。捕获会话期间触发的 Dialogue Event 的名称。 |
| Target Object | 目标对象。针对特定 Dialogue Event 添加到动态序列列表的音频对象的名称。 |
| Count | 计数。针对特定 Dialogue Event 将音频对象添加到动态序列列表的次数。 |

**相关主题**

- [“启动/停止捕获流程”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/02-启动停止捕获流程.md "启动/停止捕获流程")
- [“从 Capture Session 获取统计信息”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/07-从-Capture-Session-获取统计信息.md "从 Capture Session 获取统计信息")
- [“从已有的远程捕获会话加载数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/09-从已有的远程捕获会话加载数据.md "从已有的远程捕获会话加载数据")

---