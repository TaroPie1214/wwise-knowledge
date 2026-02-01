# Project Explorer

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > Project Explorer

## Project Explorer

在 Project Explorer（工程资源管理器）中，可以组织并管理 Wwise 工程的各种元素，如音频素材、总线、Event（事件）和 Game Sync（游戏同步器）。在各个选项卡中，您可以创建、重命名、剪切、复制、粘贴和删除选项卡层级结构中显示的独特元素。各个选项卡还包含工具栏，您可以通过它快速将父对象和子对象添加到工程层级结构。

若您的团队合作处理同一个工程，则还可将工程元素划分成不同的 Work Unit（工作单元），以便各个成员同时处理工程的不同部分。有关创建工作单元的详细信息，请参阅[*Working with a team*](../../03-设置工程/04-Working-with-a-team/00-Working-with-a-team.md "Working with a team")/>。

Project Explorer 包含以下选项卡：

- [“Audio tab”一节](01-Audio-tab/00-Audio-tab.md "Audio tab"): Displays all the Audio Devices, sound, music, motion, and bus
  structures in your project.
- [“Events 选项卡”一节](02-Events-选项卡/00-Events-选项卡.md "Events 选项卡")：显示工程中的所有 Action Event（动作事件）和 Dynamic Dialogue Event（动态对白事件）。
- [“SoundBanks 选项卡”一节](03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡")：显示工程中的 SoundBank 列表。
- [“Game Syncs 选项卡”一节](04-Game-Syncs-选项卡/00-Game-Syncs-选项卡.md "Game Syncs 选项卡")：显示工程中的所有Switch（切换开关）、State（状态）、Game Parameters（游戏参数）和Trigger（触发器）。
- [“ShareSets 选项卡”一节](05-ShareSets-选项卡/00-ShareSets-选项卡.md "ShareSets 选项卡")：显示工程中的所有 Effects、Attenuations、Conversion Settings、Modulators（调制器）、Audio Devices（音频设备）和 Virtual Acoustics（虚拟声学）共享集。
- [“Sessions 选项卡”一节](06-Sessions-选项卡/00-Sessions-选项卡.md "Sessions 选项卡")：显示工程中的所有 Soundcaster、Mixing Desk 和 Control Surface 会话。
- [“Queries 选项卡”一节](07-Queries-选项卡/00-Queries-选项卡.md "Queries 选项卡")：显示工程中的所有 Queries。

## Project Explorer Search

您可以使用 Project Explorer（工程资源管理器）的 Search（搜索）字段来查找并聚焦于 Project Explorer 视图的任一选项卡内的特定对象。此搜索功能对包含大量对象的大型工程特别有用。该字段设在 Project Explorer 的最上面，其包含下图所示的三个组件：

![](../../../images/pe_filter_overview.png)

|  |  |
| --- | --- |
|  | 通过在字段中键入或将一个或多个对象从任意视图拖到字段中来搜索 Project Explorer 内容。在将对象拖到字段中时，其会替换所有现有内容。  在搜索处于活跃状态时，字段最右侧会显示 **x**。单击 **x** 可重置搜索。 |
|  | 基于 Wwise 中所有参数的当前状态重新应用搜索并重置显示的结果。上次执行搜索后展开或收起的所有分支将恢复为执行搜索操作后的原始展开状态。  注意，在更改对象的父对象或创建、重命名或删除对象时会自动刷新搜索结果，但不会对其他参数更改（比如可能对评估音量的 WAQL 查询产生影响的音量更改）做出反应。Refresh 按钮在这些情况下特别有用。 |
|  | 在搜索文本与对象及其下级对象匹配时，只会展开到第一个匹配对象所在的层级。单击此按钮可展开所有包含与搜索匹配的对象的分支。 |

有关更多详细信息，请参阅 [“Using the Project Explorer search”一节](../../08-使用-Wwise/01-认识-Project-Explorer-视图/02-Using-the-Project-Explorer-search.md "Using the Project Explorer search") 章节。

---