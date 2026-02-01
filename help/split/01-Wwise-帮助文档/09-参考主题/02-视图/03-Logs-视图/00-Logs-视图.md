# Logs 视图

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [视图](../00-视图.md) > Logs 视图

## Logs 视图

Logs（日志）视图包含以下五个选项卡，可显示所有 Wwise 信息、警告和错误：

- [General](00-Logs-视图.md#general_tab_log "General 选项卡")
- [Project Load](../../../03-设置工程/01-处理工程/01-管理工程.md#project_load_log "打开和关闭工程")
- [SoundBank Generation](00-Logs-视图.md#soundbank_generation_log "SoundBank Generation 选项卡")
- [Conversion](00-Logs-视图.md#conversion_tab_log "Conversion 选项卡")
- [WAAPI](00-Logs-视图.md#waapi_tab_log "WAAPI 选项卡")

您可以通过以下方式打开 Logs 视图：

- [Wwise 工具栏](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md "Wwise 界面基础知识")：单击日志标志
- [Views 菜单](../00-视图.md "视图")
- F4 [键盘快捷方式](../../01-工程/12-键盘快捷方式和自定义命令.md "键盘快捷方式和自定义命令")

Logs 视图中的所有选项卡均采用标准的列和按钮布局（详见下表）。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Severity | 严重性。显示以下用于指示严重级别的图标：  - ：白色，表示常规信息，通常不会影响当前操作的完整性。 - ：黄色，表示警告，可能会影响当前操作的完整性。 - ：红色，表示错误，会影响当前操作的完整性。 - ：黑色，表示重大错误，会导致当前操作无法完成。  |  |  | | --- | --- | | [备注] | 备注 | | 您可以更改 SoundBank Generation 和 Conversion 日志中显示的大部分消息的严重性。有关详细信息，请参阅[“管理在日志中出现的消息”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/04-管理在日志中出现的消息.md "管理在日志中出现的消息")。 | |
| Time | 时间。错误、警告或消息的生成时间。 |
| ID | 该错误、警告或消息的 ID。 |
| Message | 消息。有关所遇问题的描述。 |
| Parameters | 参数。与错误、警告或消息有关的工程元素列表。  您可以双击某个工程元素，将其加载到编辑器中。 |
|  | 将信息复制到剪贴板中，这样您可将该信息粘贴至新文件中。 |
|  | 清除。移除当前所选选项卡中的所有条目。 |

### General 选项卡

General（常规）选项卡会记录 Wwise 核心系统相关问题，包括 Command Manager、自定义属性、Layout Manager、插件和 Theme Manager 问题。

### Project Load 选项卡

Project Load（工程加载）选项卡会记录 [“打开和关闭工程”一节](../../../03-设置工程/01-处理工程/01-管理工程.md#project_load_log "打开和关闭工程") 中报告的 Wwise 工程问题。其中大部分都是有关迁移到当前工程版本的概要消息。不过，在出现 XML 错误和各种工程不一致情况时也会显示相应问题。

### SoundBank Generation 选项卡

SoundBank Generation（音频包生成）选项卡会记录生成过程中发现的问题或潜在问题相关信息。下面列出了可能遇到的几类问题：

- The custom post-generation executable can't be found. 无法找到自定义生成后可执行步骤。在这种情况下，将不会执行您指定的自定义生成后步骤。
- A generated SoundBank references data or media in another SoundBank that is not being generated. 生成的 SoundBank 引用了另一未生成的 SoundBank 中的数据或媒体。在这种情况下将自动生成被引用的 SoundBank。
- If media files are duplicated in more than one SoundBanks. 媒体文件在多个 SoundBank 中重复出现。这只是一个警告，旨在帮助您查找和移除重复的媒体文件。
- If a sound object references a media file that cannot be found in any of the generated SoundBanks. 声音对象引用了已生成 SoundBank 中无法找到的媒体文件。在这种情况下，游戏中将不会播放声音对象。
- SoundBank 引用了工程中已卸载的 Event 或对象。在这种情况下，您可以将对应的 Work Unit 重新加载至工程来解决该问题。
- SoundBank names have a 252-character limit. The limit is evaluated when generating a SoundBank, which is written to disk within your project hierarchy's full file path. If that path exceeds your operating system's limit, then generation will fail with `error 14: Can't write bank file`. 详请参阅[“Understanding file length limitations and naming conventions”一节](../../../02-入门/03-Wwise-界面基础知识/02-Understanding-file-length-limitations-and-naming-c.md "Understanding file length limitations and naming conventions")。

### Conversion 选项卡

The Conversion tab keeps a record of issues reported in the Log panel of the Conversion - Completed dialog.

If Wwise encounters any issues while converting the audio source, such as an empty or invalid file, it will display information about them in the Conversion Log at the bottom of the dialog.

### WAAPI 选项卡

WAAPI 选项卡会记录使用 [Wwise Authoring API](https://www.audiokinetic.com/library/edge/?source=SDK&id=waapi.html) 的过程中遇到的所有问题。其中包括连接、服务器和有效性问题。详请参阅[“Configuring the Wwise Authoring API (WAAPI)”一节](../../../02-入门/04-个性化您的工作空间/04-设置用户偏好.md#user_prefs_waapi "Configuring the Wwise Authoring API (WAAPI")")。

### 忽略日志条目

若不想在日志中继续显示特定警告或消息，则可使用 Project Settings（工程设置）对话框将这些警告和消息添加到 Log Ignore List（日志忽略列表）。有关详细信息，请参阅[“管理在日志中出现的消息”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/04-管理在日志中出现的消息.md "管理在日志中出现的消息")。

对于 General、Project Load 和 WAAPI 日志，请单击 View Settings（视图设置）图标，以便打开 [“Logs Settings”一节](01-Logs-Settings.md "Logs Settings") 并选择要忽略的消息。

**相关主题**

- [“解决工程中的不一致现象”一节](../../../03-设置工程/04-Working-with-a-team/04-解决工程中的不一致现象.md "解决工程中的不一致现象")
- [“Logs 选项卡”一节](../../01-工程/08-Project-Settings/04-Logs-选项卡.md "Logs 选项卡")
- [“管理在日志中出现的消息”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/04-管理在日志中出现的消息.md "管理在日志中出现的消息")

---