# Work Units 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [File Manager](00-File-Manager.md) > Work Units 选项卡

### Work Units 选项卡

File Manager 的 Work Units 选项卡显示有关各个工作单元的信息，包括有关文件状态和所有者的信息，以及哪些文件为只读文件。

您还可以执行某些工程管理任务，如文件重命名和删除。 不过，假如使用了版本控制插件，则右键单击列表中的 Wwise 工程文件或 Work Unit 将显示一组附加命令（如 Check-in 和 Check-out）。具体显示什么命令将取决于 Wwise 使用的版本控制系统类型。

|  |  |
| --- | --- |
| [注意] | 注意 |
| Default Work Units 是关键的工程文件，不得重命名或删除。 |

| 界面元素 | 描述 |
| --- | --- |
| Perforce:    Subversion（已弃用）： | 将待处理文件发送至服务器进行处理。 您可以选择以下任一选项：  - **Work Units**（工作单元）：仅将待处理 Work Unit 发送至服务器以供处理。 - **Sources** —— 仅将待处理源文件发送至服务器进行处理。 - **All**（全部）：同时将待处理 Work Unit 和源文件发送至服务器以供处理。  此按钮仅在使用版本控制插件时可用。 |
| Perforce:    Subversion（已弃用）： | 从文档库（depot）中检索文件的最新版本来更新文件的工作副本。 您可以选择以下任一选项：  - **Work Units**：从文档库检索最新版本，但仅更新 Work Unit 文件。 - **Sources** —— 通过从文档库中获取文件的最新版本，仅更新源文件。 - **All**：从文档库检索最新版本，并同时更新 Work Unit 和源文件。  此按钮仅在使用版本控制插件时可用。 |
| Project Folder | 工程文件夹。保存当前工程的文件夹的位置或路径。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| File（文件） | 当前文件或文件夹的名称。 该文件可为 Wwise 工程文件、Work Unit 文件或文件夹。 |
| Status | 状态。文件的版本控制状态（如 Edit 或 Add）。文件的状态通过 Wwise 版本控制插件从您的版本控制软件种获取。  例如，如果您使用的是 Perforce 插件，则文件可能具有以下任一状态：  - **Add** —— 添加。文件位于 changelist（更改列表）中，可 check-in 到文档库中。 - **Branch** —— 分支。现有文档库文件的一个副本已添加至 changelist ，可 check-in 至文档库中。 - **Delete** —— 删除。该文件位于 changelist 中，可从文档库中删除。 - **Edit** —— 编辑。文档库文件的一个工作副本已 check-out 到工作区，以便进行编辑。 - **Local only** —— 仅本地。已在本地创建文件，但尚未 check-in 到文档库。 - **Lock** —— 锁定。文档库文件被锁定，其它用户无法 check-out 该文件进行编辑。 - **Normal** —— 正常。该文件已 check-in 到文档库。  如果文件的状态为未知，则会显示一条横线 (-)。 |
| Owner(s) | 文件的所有者。  如果文件的所有者为未知，则会显示一条横线 (-)。 |
| Modified | 已修改。显示文件是否被修改过。 |
| Read-Only | 只读。显示文件是否为只读。 |
|  | 复制到剪贴板。将对话框的内容复制到 Windows 剪贴板以便将信息粘贴到新的文件中。 |
|  | 关闭 File Manager。 |

**相关主题**

- [“查看工程文件的状态”一节](../../../03-设置工程/04-Working-with-a-team/02-查看工程文件的状态.md "查看工程文件的状态")
- [“配置版本控制插件”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/01-定义工程的常规设置.md#configuring_source_control_plug_ins "配置版本控制插件")
- [“利用版本控制插件管理工程文件”一节](../../../03-设置工程/04-Working-with-a-team/05-利用版本控制插件管理工程文件.md "利用版本控制插件管理工程文件")

---