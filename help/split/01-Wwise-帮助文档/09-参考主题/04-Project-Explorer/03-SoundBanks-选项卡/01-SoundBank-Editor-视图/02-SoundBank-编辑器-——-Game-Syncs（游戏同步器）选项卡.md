# SoundBank 编辑器 —— Game Syncs（游戏同步器）选项卡

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [SoundBanks 选项卡](../00-SoundBanks-选项卡.md) > [SoundBank Editor 视图](00-SoundBank-Editor-视图.md) > SoundBank 编辑器 —— Game Syncs（游戏同步器）选项卡

#### SoundBank 编辑器 —— Game Syncs（游戏同步器）选项卡

SoundBank 编辑器的 Game Syncs 选项卡显示了被已添加至 SoundBank 的声音结构所引用的一组 Game Sync。您可以在该列表中调整 SoundBank 的内容，基于特定游戏同步器来启用或弃用特定事件、对象结构或媒体文件。例如，假设您为主要角色的脚步声使用了切换容器，且该切换容器包含木头、瓦片、毯子和水四个切换开关。水切换开关仅用于游戏中的一个区域，因此为了避免不必要地加载“水材质脚步”声，除了仅包含水材质的 SoundBank 外，您可以为其它材质域的 SoundBank 将水材质切换开关弃用。通过根据游戏同步器来启用／弃用声音，可以更好地控制在游戏特定时刻加载的声音。这意味着您可以更好地管理游戏平台的内存限制。要从 SoundBank中 弃用特定游戏同步器及其相应的对象和媒体文件，只需将该游戏同步器旁的复选框取消选择即可。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 游戏参数将不包含在 Game Sync 列表中。 |

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | SoundBank 的名称。 |
| Notes | 备注。SoundBank 的其它信息。 |
| 包含 | 决定 SoundBank 中是否包含特定的游戏同步器，及其相应的对象或媒体文件。  要从 SoundBank 中弃用游戏同步器，请将其取消选择。 |
| Game Sync | 游戏同步器。列出 Add 选项卡中所含 Event 和声音结构引用的 State（状态）、Switch（切换开关）和 Trigger（触发器）。  点击列标题栏，可以按字母升序或降序来排序信息。  游戏同步器可以手动从 SoundBank 中弃用，也可以通过导入 SoundBank 定义文件弃用。为帮助您区分这两种方法，被手动弃用的游戏同步器名称会添加一个星号 (\*)。 |
|  | 在 SoundBank 中包含所有游戏同步器及其相关的对象和媒体文件。 |
|  | 在 SoundBank 中弃用所有游戏同步器及其相关的对象和媒体文件。 |

**相关主题**

- [“使用 Game Sync 启用/弃用工程元素”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/02-使用-Game-Sync-启用弃用工程元素.md "使用 Game Sync 启用/弃用工程元素")
- [“在 SoundBank 中启用/弃用工程元素”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/01-在-SoundBank-中启用弃用工程元素.md "在 SoundBank 中启用/弃用工程元素")
- [“搜索 SoundBank 中的元素”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/04-搜索-SoundBank-中的元素.md "搜索 SoundBank 中的元素")
- [“筛选 SoundBank 中的元素列表”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/05-筛选-SoundBank-中的元素列表.md "筛选 SoundBank 中的元素列表")

---