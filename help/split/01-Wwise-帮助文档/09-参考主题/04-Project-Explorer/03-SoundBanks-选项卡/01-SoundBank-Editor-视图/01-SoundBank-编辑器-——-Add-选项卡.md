# SoundBank 编辑器 —— Add 选项卡

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [SoundBanks 选项卡](../00-SoundBanks-选项卡.md) > [SoundBank Editor 视图](00-SoundBank-Editor-视图.md) > SoundBank 编辑器 —— Add 选项卡

#### SoundBank 编辑器 —— Add 选项卡

您可以通过 SoundBank 编辑器的 Add 选项卡来为 SoundBank 添加内容。您可以从 Project Explorer（工程资源管理器）或 Event Viewer（事件查看器）拖动各种工程元素（包括 Event、声音对象和 Work Unit），来将其添加至 SoundBank。当您添加父对象元素时，所有相应的子对象也将被自动添加至 SoundBank。对于各个工程元素，您还须决定是否在 SoundBank 内包含所有相应的事件、对象结构和媒体。

Wwise 对已添加至 SoundBank 的工程元素使用以下颜色显示，来区分不同的问题：

- **红色** —— 工程中缺少该工程元素。
- **黄色** —— 该工程元素已从工程中卸载。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | SoundBank 的名称。 |
| Notes | 备注。SoundBank 的其它信息。 |
| 包含的层级结构 | 层级结构内该层的对象被包含在 SoundBank 中。低于该层的所有对象也会自动包含在 SoundBank 中。  工程元素可以手动添加至 SoundBank 中，也可以通过导入 SoundBank 定义文件来添加。为了帮助您区分这两种方法，手动添加的工程元素名称后面会添加一个星号 (\*)。 |
| Event | 事件。确定是否在 SoundBank 中包含与特定工程元素关联的 Event。 |
| 声音结构 | 结构。确定是否在 SoundBank 中包含与特定工程元素关联的声音、音乐和振动结构。 |
| 媒体 | 决定是否在 SoundBank 中包含与该工程元素相关联的媒体。 |
|  | 从 SoundBank 中移除所选工程元素和相应的事件、结构和媒体文件。 |

**相关主题**

- [“通过导入定义文件创建并填充 SoundBank”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/02-通过导入定义文件创建并填充-SoundBank.md "通过导入定义文件创建并填充 SoundBank")
- [“手动填充 SoundBank”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/03-手动填充-SoundBank.md "手动填充 SoundBank")
- [“在 SoundBank 中启用/弃用工程元素”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/01-在-SoundBank-中启用弃用工程元素.md "在 SoundBank 中启用/弃用工程元素")
- [“使用 Game Sync 启用/弃用工程元素”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/02-使用-Game-Sync-启用弃用工程元素.md "使用 Game Sync 启用/弃用工程元素")
- [“在 SoundBank 之间移动工程元素”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/06-在-SoundBank-之间移动工程元素.md "在 SoundBank 之间移动工程元素")
- [“从 SoundBank 中移除工程元素”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/07-从-SoundBank-中移除工程元素.md "从 SoundBank 中移除工程元素")

---