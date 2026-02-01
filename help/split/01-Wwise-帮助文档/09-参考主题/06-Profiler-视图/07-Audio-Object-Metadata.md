# Audio Object Metadata

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [Profiler 视图](00-Profiler-视图.md) > Audio Object Metadata

## Audio Object Metadata

Audio Object Metadata（音频对象元数据）视图提供了当前所选 Audio Object 的详细元数据信息。要想在此视图中显示内容，必须在 [“Audio Object List”一节](06-Audio-Object-List.md "Audio Object List") 中选择 Audio Object。此视图中显示的信息基于当前性能分析器光标时间。

元数据是随 Audio Object 一并存储的各种信息。Metadata includes the positioning information from Wwise, as well as the custom Metadata plug-in’s information inserted from the Containers hierarchy or the Busses Hierarchy.

元数据可由效果器插件或终端用来渲染 Audio Object。有关元数据的详细信息，请参阅 [“Metadata”一节](../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/03-Metadata.md "Metadata") 章节。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要在此视图中显示信息，则须在 [“Profiler Settings”一节](../01-工程/10-Profiler-Settings.md "Profiler Settings") 中启用 **Audio Object Data** 以捕获数据，同时在捕获会话中选择时间点。 |

| 界面元素 | 描述 |
| --- | --- |
|  | Click the View Settings icon in the upper right corner of the view to open the [“Profiler Settings”一节](../01-工程/10-Profiler-Settings.md "Profiler Settings") dialog, where you can specify the type of data to capture. |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Metadata | 元数据。显示元数据条目的名称和元数据中各项数值的名称。 |
| Value | 值。显示元数据条目的值。 |
| Source | 源。对于用户应用的元数据，显示在 Wwise 工程的哪个位置设置了此元数据。For example, if the metadata was added to a Property Container object, you would see the Property Container object here. 通过双击对象可打开相应视图并定义元数据。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |

**相关主题**

- [“了解基于对象的音频”一节](../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/00-了解基于对象的音频.md "了解基于对象的音频")
- [“对 Audio Object 实施性能分析”一节](../../07-完善工程/06-性能分析/12-对-Audio-Object-实施性能分析.md "对 Audio Object 实施性能分析")

---