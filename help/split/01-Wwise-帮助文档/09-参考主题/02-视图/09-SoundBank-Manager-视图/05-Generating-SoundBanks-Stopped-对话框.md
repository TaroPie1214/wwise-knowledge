# Generating SoundBanks - Stopped 对话框

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [视图](../00-视图.md) > [SoundBank Manager 视图](00-SoundBank-Manager-视图.md) > Generating SoundBanks - Stopped 对话框

### Generating SoundBanks - Stopped 对话框

Generating SoundBanks - Stopped（生成音频包 - 已停止）对话框会显示在停止生成过程前已成功生成的 SoundBank 数。它还会显示生成日志，其中包含与生成过程中出现或可能出现的问题相关的信息。您可以在对话框内查看这些错误消息，也可以将它们复制到 Windows 剪贴板，以粘贴至其它应用程序。

在生成过程中，此对话框包含一个显示整体 SoundBank 生成进度的主进度条以及一组与正在转码的各个文件对应的次级进度条。次级进度条的数量取决于设备中的处理器内核数。Wwise 使用所有处理核心来对 SoundBank 中的文件做转码，以尽快执行生成过程。

| 界面元素 | 描述 |
| --- | --- |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Operation | 操作。在生成 SoundBank 时，该列显示正在执行的各个任务的名称。当生成过程被中断时将显示“Stopped”。 |
| Progress | 在生成 SoundBank 时，该列包含一系列进度条，显示 SoundBank 的生成进度。  主要进度条显示 SoundBank 的整个生成进度。一系列次要进度条将显示 SoundBank 生成过程中，正在执行的各个操作的进度。若设备使用的是多核处理器，则会将各个内核用于对 SoundBank 中的文件实施转码并显示与之对应的进度条。  如果生成停止，则此列为空。 |
| Details | 生成 SoundBank 时，该列显示各个内核当前正在执行的特定任务的其它信息。  如果生成停止，则此列为空。 |
| **Results** | |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| SoundBanks | 已生成的 SoundBank 的名称。 |
| Platforms（平台） | 平台。生成的 SoundBank 将用于哪些平台。 |
| Language/SFX | 语言／音效。生成 SoundBank 的语言。如果 SoundBank 不包含语音对象，则该列将显示“SFX”。 |
| Created | 已创建。显示是否成功生成了 SoundBank。 |
| Status | 描述 SoundBank 生成状态的信息。报告与生成过程有关的异常情况，如缺失文件或 SoundBank 超出上限。 |
| **日志**：请参阅 [“SoundBank Generation 选项卡”一节](../03-Logs-视图/00-Logs-视图.md#soundbank_generation_log "SoundBank Generation 选项卡")。 | |
|  | 关闭。关闭 SoundBanks Generation - Stopped 对话框。 |

---