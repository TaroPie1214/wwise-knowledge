# Generating SoundBanks 对话框

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [视图](../00-视图.md) > [SoundBank Manager 视图](00-SoundBank-Manager-视图.md) > Generating SoundBanks 对话框

### Generating SoundBanks 对话框

几个 Generating SoundBanks（生成音频包）对话框基本相同，只不过使用了不同的标签名称来指示当前状态。因此在处理时，对话框标签为“In Progress”；停止时标签为“Stopped”；处理完成时标签为“Completed”。因此，开始时会显示 **Generating SoundBanks - In Progress** 对话框，结束时显示 **Generating SoundBanks - Completed** 对话框。

所有这些对话框均包含三个信息面板，其会显示以下信息（详见下表）：

- 文件转码过程中不同操作的进度；
- 不同 SoundBank 生成的结果；以及
- 进度日志，包括信息和警告（如果出现错误或可能出现错误）。

在处理过程中，顶部面板将显示一个整体进度的主要进度条，以及一组针对各个正在转码文件的次要进度条。次级进度条的数量取决于设备中的处理器内核数。Wwise 使用所有处理内核来对声音包中的文件做转码，以尽快地执行生成过程。日志面板显示与生成过程（包括生成状态和错误）相关的信息。

您可以随时停止生成过程。在生成过程中断时，Wwise 会自动显示 **Generating SoundBanks - Stopped**（生成音频包 - 已停止）对话框。除使用红色字体 Stopped 替代上部面板中列出的所有操作外，此对话框基本上没什么变化。您仍可以查看结果，并在日志中查看生成停止前发生的问题。

| 界面元素 | 描述 |
| --- | --- |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Operation | 操作。在生成 SoundBank 时，该列显示正在执行的各个任务的名称。在生成过程完成时，将显示“Completed”。 |
| Progress | 在生成 SoundBank 时，该列包含一系列进度条，显示 SoundBank 的生成进度。  主要进度条显示 SoundBank 的整个生成进度。一系列次要进度条将显示 SoundBank 生成过程中，正在执行的各个操作的进度。若设备使用的是多核处理器，则会将各个内核用于对 SoundBank 中的文件实施转码并显示与之对应的进度条。  当生成完成后，该列将显示为空。 |
| Details | 在生成 SoundBank 时，该列显示当前执行的任务的其它信息。  当生成完成后，该列将显示为空。 |
| **Results** | |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| SoundBanks | 已生成的 SoundBank 的名称。  |  |  | | --- | --- | | [备注] | 备注 | | **Init** 是 [Initialization Bank](../../../14-词汇表.md#glossary_initialization_bank "Initialization Bank（初始化库）") 的默认名称。每个工程都包含这个特殊的 SoundBank，其会与生成的各个 SoundBank 列在一起。 | |
| Platforms（平台） | 平台。生成的 SoundBank 将用于哪些平台。 |
| Language/SFX | 语言／音效。生成 SoundBank 的语言。如果 SoundBank 不包含任何声部对象，则该列将显示“SFX”。 |
| Created | 已创建。显示“Yes”或“No”以指示 SoundBank 是否成功生成。如果未生成 SoundBank，则显示“Up to Date”，因为自上一次生成后没有任何更改。 |
| Status | 描述 SoundBank 生成状态的信息。报告与生成有关的任何异常，如缺失文件或 SoundBank 超出上限。 |
| **日志**：请参阅 [“SoundBank Generation 选项卡”一节](../03-Logs-视图/00-Logs-视图.md#soundbank_generation_log "SoundBank Generation 选项卡")。 | |
|  | 关闭。关闭 SoundBanks Generation - Completed 对话框。 |

---