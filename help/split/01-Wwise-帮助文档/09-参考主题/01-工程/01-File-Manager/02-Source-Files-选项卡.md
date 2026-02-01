# Source Files 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [File Manager](00-File-Manager.md) > Source Files 选项卡

### Source Files 选项卡

File Manager 的 Source Files 选项卡显示工程 Original 文件夹中包含的媒体文件的相关信息。 在 File Manager 内，您可以确定媒体文件的状态和所有者，以及哪些文件为只读。

您也可以直接在 File Manager 中移动或删除不再需要的源文件。但如果您使用的是版本控制插件，则右键点击列表中的文件将显示一组额外的命令，如 Submit Change和 Check out。 具体显示什么命令将取决于 Wwise 使用的版本控制系统类型。

| 界面元素 | 描述 |
| --- | --- |
| Sources Folder | 源文件夹。保存原始源媒体文件的文件夹的位置或路径。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| File（文件） | 文件或文件夹的名称。 |
| Status | 源媒体文件的状态，如编辑或添加。 文件的状态通过 Wwise 版本控制插件从您的版本控制软件种获取。  例如，如果您使用的是 Perforce 插件，则文件具有以下任一状态：  - **Add** —— 添加。文件位于 changelist（更改列表）中，可 check-in 到文档库中。 - **Branch** —— 分支。现有文档库文件的一个副本已添加至 changelist ，可 check-in 至文档库中。 - **Delete** —— 删除。该文件位于 changelist 中，可从文档库中删除。 - **Edit** —— 编辑。文档库文件的一个工作副本已 check-out 到工作区，以便进行编辑。 - **Local only** —— 仅本地。已在本地创建文件，但尚未 check-in 到文档库。 - **Lock** —— 锁定。文档库文件被锁定，其它用户无法 check-out 该文件进行编辑。 - **Normal** —— 正常。该文件已 check-in 到文档库。  如果文件的状态为未知，则会显示一条横线 (-)。 |
| Owner | 文件的所有者。  如果文件的所有者为未知，则会显示一条横线 (-)。 |
| Read-Only | 只读。显示文件是否为只读。 |
| 用途 | 显示源文件是否被工程内的若干个音频/振动源使用。 音频源可有以下任一使用状态：  - **In use** —— 源文件与工程中的音频源相关联。 - **Not used** —— 源文件不再与工程中的音频源相关联。 - **Unknown** —— Wwise 无法区分未使用的文件与从工程中卸载了的文件。 此使用状态仅在从工程内上传 Work Unit（工作单元）后显示。  **Usage** 列中所示信息会受到 Undo（撤消）列表中所有操作的影响，包括文件导入和对象删除。因此，信息看起来可能不会是最新的。 在删除被标记为“Not used”的任何文件之前，最好关闭并重新打开工程，以确保信息是最新的。 |
|  | 复制到剪贴板。将对话框的内容复制到 Windows 剪贴板以便将信息粘贴到新的文件中。 |
|  | 关闭 File Manager。 |

**相关主题**

- [“查看工程文件的状态”一节](../../../03-设置工程/04-Working-with-a-team/02-查看工程文件的状态.md "查看工程文件的状态")
- [“配置版本控制插件”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/01-定义工程的常规设置.md#configuring_source_control_plug_ins "配置版本控制插件")
- [“利用版本控制插件管理工程文件”一节](../../../03-设置工程/04-Working-with-a-team/05-利用版本控制插件管理工程文件.md "利用版本控制插件管理工程文件")
- [“Moving source files within the Originals folder using Perforce”一节](../../../03-设置工程/04-Working-with-a-team/05-利用版本控制插件管理工程文件.md#moving_source_files_within_originals_folder_using_perforce "Moving source files within the Originals folder using Perforce")
- [“Renaming files when using Perforce”一节](../../../03-设置工程/04-Working-with-a-team/05-利用版本控制插件管理工程文件.md#renaming_files_when_using_perforce "Renaming files when using Perforce")
- [“Deleting files from your project when using Perforce”一节](../../../03-设置工程/04-Working-with-a-team/05-利用版本控制插件管理工程文件.md#deleting_files_from_project_when_using_perforce "Deleting files from your project when using Perforce")

---