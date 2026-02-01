# Emitter-Listener Associations（发声体与听者的关系）

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Emitter-Listener Associations（发声体与听者的关系）

### Emitter-Listener Associations（发声体与听者的关系）

Advanced Profiler 中的 Emitter-Listener 选项卡显示了发声体与听者关系的信息。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Emitter（发声体） | 该发声体与听者的关系中，“发声体”游戏对象的 ID、或游戏对象的名称。与 API 调用  [`SetListeners()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a2f85a55c38afa2e0dbc6172a7bec91d1.html) 和  [`SetGameObjectAuxSendValues()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_af960fca0239e219b9d08c2659fe9e5d4.html) 的第一个参数对应。可以是任意游戏对象。  |  |  | | --- | --- | | [备注] | 备注 | | 在 Emitter-Listener 选项卡中双击列出的游戏对象将会打开由该游戏对象 ID 筛选的 Voices Graph 选项卡。 | |
| Listener | 该发声体与听者的关系中，“听者”游戏对象的 ID、或游戏对象的名称。与 API 调用  [`SetListeners()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a2f85a55c38afa2e0dbc6172a7bec91d1.html) 和  [`SetGameObjectAuxSendValues()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_af960fca0239e219b9d08c2659fe9e5d4.html) 的第二个参数对应。可以是任意游戏对象。  |  |  | | --- | --- | | [备注] | 备注 | | 在 Emitter-Listener 选项卡中双击列出的游戏对象将会打开由该游戏对象 ID 筛选的 Voices Graph 选项卡。 | |
| Bus | 与该对象关联的总线的名称。 |
| Level | 游戏对象应用的发送值百分比，与发送音量有关。 |
| Routing Type | User-defined（用户定义）：使用 API 调用  [`SetListeners()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a2f85a55c38afa2e0dbc6172a7bec91d1.html) 设置的关联。包括工程中所有的直接输出和用户定义的发送。用户关联可以应用于 Voice Graph 中的任何节点。  "Game-defined"：游戏定义的发送。使用  [`SetGameObjectAuxSendValues()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_af960fca0239e219b9d08c2659fe9e5d4.html)API 调用设置的关联。对于游戏定义的发送，不管工程设置如何，都将完全通过 API 调用来定义符合条件的 GameObjectID 和 AuxBusID 配对。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

---