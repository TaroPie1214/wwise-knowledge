# Generated Files 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [File Manager](00-File-Manager.md) > Generated Files 选项卡

### Generated Files 选项卡

File Manager（文件管理器）的 Generated Files（生成的文件）选项卡会显示有关工程内输出文件夹所含文件的信息。Generated Files 选项卡允许逐一查看针对工程的各个平台生成的文件。

工程的输出文件夹可通过工程的 SoundBank Settings（音频包设置）进行配置。工程的输出文件夹包含两个文件夹：一个用于工程层级的文件，一个用于工程的各个平台。在默认情况下，工程输出文件夹为 <Project>/GeneratedSoundBanks。各个平台文件夹为工程文件夹的子对象，其使用平台名称分别进行命名。比如，有个名为 MyProject 的工程，其支持 Windows 和 Mac 平台。那么，输出文件夹会跟下面一样：

- <Project>/GeneratedSoundBanks
- <Project>/GeneratedSoundBanks/Windows
- <Project>/GeneratedSoundBanks/Mac

输出文件夹中所含的文件由 SoundBank Settings 决定。有关详细信息，请参阅[“SoundBanks 选项卡”一节](../08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡")

在 File Manager 中，您可以确定所生成文件的状态和所有者以及哪些文件为只读文件。而且，直接在 File Manager 中就可移动或删除已经生成但不再需要的文件。但如果您使用的是版本控制插件，则右键点击列表中的文件将显示一组额外的命令，如 Submit Change和 Check out。 具体显示什么命令取决于结合 Wwise 使用的版本控制系统类型。

| 界面元素 | 描述 |
| --- | --- |
| Platform | 平台。 针对该平台显示生成的文件。 |
| Folder | 文件夹。在该位置或路径下的文件夹保存生成的文件。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| File（文件） | 文件或文件夹的名称。 |
| Status | 状态。文件的状态（如 Edit 或 Add）。文件的状态通过 Wwise 版本控制插件从您的版本控制软件种获取。  比如，若您使用的是 Perforce 插件，则文件可能具有以下任一状态：  - **Add** —— 添加。文件位于 changelist（更改列表）中，可 check-in 到文档库中。 - **Branch** —— 分支。现有文档库文件的一个副本已添加至 changelist ，可 check-in 至文档库中。 - **Delete** —— 删除。该文件位于 changelist 中，可从文档库中删除。 - **Edit** —— 编辑。文档库文件的一个工作副本已 check-out 到工作区，以便进行编辑。 - **Local only** —— 仅本地。已在本地创建文件，但尚未 check-in 到文档库。 - **Lock** —— 锁定。文档库文件被锁定，其它用户无法 check-out 该文件进行编辑。 - **Normal** —— 正常。该文件已 check-in 到文档库。  如果文件的状态为未知，则会显示一条横线 (-)。 |
| Owner(s) | 所有者。文件的所有者。  如果文件的所有者为未知，则会显示一条横线 (-)。 |
| Read-Only | 只读。显示文件是否为只读。 |
|  | 复制到剪贴板。将对话框的内容复制到 Windows 剪贴板以便将信息粘贴到新的文件中。 |
|  | 关闭 File Manager。 |

**相关主题**

- [“SoundBanks 选项卡”一节](../08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡")
- [*管理 SoundBank*](../../../07-完善工程/07-管理-SoundBank/00-管理-SoundBank.md "管理 SoundBank")

---