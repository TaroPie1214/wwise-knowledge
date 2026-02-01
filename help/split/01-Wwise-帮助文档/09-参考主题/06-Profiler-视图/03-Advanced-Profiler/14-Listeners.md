# Listeners

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Listeners

### Listeners

听者。Advanced Profiler — Listener 选项卡显示有关游戏中活跃听者的信息。听者是游戏中的一个虚拟话筒或振动传感器，用于帮助用户把声音分配给特定的扬声器或将振动分配给特定的电机，从而模拟一个三维环境。例如，在多人赛车游戏中，轨道上各个玩家控制的赛车可以是一个听者。该选项卡显示哪个听者与游戏中的哪个玩家相关联，以及哪个游戏对象的声音和振动与哪个听者相关联。

Wwise 必须为每个听者注册一个游戏对象，并为每个听者进行完整的混音过程。这些需要在 Wwise SDK 中设置。为方便起见，可以将 `listenerID` 字段设置为 `AK_INVALID_GAME_OBJECT` ，这将告知声音引擎，只需使用 `SetListeners()` 或 `SetDefaultListeners()` API 函数已经指定的听者。这个功能有助于代码迁移以及最常见的辅助发送场景，这样可以让听者与直接输出的听者相同。请参考  [Wwise SDK documentation](https://www.audiokinetic.com/library/?source=SDK&id=soundengine__listeners.html)中的 集成 Listener 章节来了解更多信息。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Listener | 听者的名称。 |
| Spatialization | 听者的空间定位状态。 |
| L | 左扬声器偏置。 |
| R | 右扬声器偏置。 |
| C | 中置扬声器偏置。 |
| RR | 右后扬声器偏置。 |
| RL | 左后扬声器偏置。 |
| LFE | 低频效果扬声器偏置。 |
| Game Object | 游戏对象的名称。 |
| Listener | 列出关联的听者游戏对象。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

---