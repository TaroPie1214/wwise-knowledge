# General 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Project Settings](00-Project-Settings.md) > General 选项卡

### General 选项卡

常规。在 General 选项卡中，您可为工程定义以下工程：

- 版本控制插件配置
- 原始音频文件夹位置
- 缓存文件夹位置
- 事件创建
- 用户界面首选项

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| **Filter Behavior（滤波器行为）** | |
| Voice LPF and HPF behavior | 声部 LPF 和 HPF 行为。决定如何计算 LPF 和 HPF 属性值。  - **Sum All Values (Default)**。累加所有值 (默认)。将属性值加在一起。 - **Use Highest Value**。使用最大值。使用属性值当中的最大值。  请参阅 [“了解滤波器属性行为（LPF 和 HPF）”一节](../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/03-了解滤波器属性行为（LPF-和-HPF）.md "了解滤波器属性行为（LPF 和 HPF）")。 |
| DSF Emphasis | Applies a global emphasis property to all DSF filters in the Wwise project. 请参阅 [“Understanding the dual-shelf filter”一节](../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/04-Understanding-the-dual-shelf-filter.md "Understanding the dual-shelf filter")。 |
| **Source Control（版本控制）** | |
| Plug-in | 插件。工程版本控制插件的名称。您可以选择以下任一选项：  有关 Wwise 支持哪些版本的详细信息，请参阅 [“Supported Perforce/Subversion versions”一节](../../../03-设置工程/04-Working-with-a-team/05-利用版本控制插件管理工程文件.md#supported_perforce_subversion_versions "Supported Perforce/Subversion versions")。  - **No Source Control** —— 无版本控制。如果您不使用版本控制系统管理素材和工程文件。 - **Perforce**。 - **Subversion（已弃用）**：若工作站上所装 Subversion 版本与版本控制插件构建所用版本不兼容，则 Plug-in 列表中不会显示 Subversion 选项。 - **Other Source Control**（其他版本控制）– 如果使用别的版本控制系统（已自行创建版本控制插件）。 |
|  | 配置...。在选择版本控制插件时可用。打开 Source Control Plug-in Configuration 对话框以便定义插件的配置。比如，**Use Audiokinetic Wave Viewer to diff WAV files**。请参阅 [*Wwise Wave Viewer*](../../../12-Wwise-工具/03-Wwise-Wave-Viewer.md "Wwise Wave Viewer")。 |
| Show source control file status in user interface | 在用户界面中显示版本控制文件状态。启用对版本控制插件的文件状态查询，以便显示版本控制状态和所有者。  启用后会显示：  - Work Unit 状态图标 - Work Unit 状态图标和所有者（视图标题栏工具提示中） - Wwise 工程 (WPROJ) 状态和所有者（Wwise 标题栏中）  遇到版本控制插件或服务器性能问题时，禁用该选项。 |
| Prompt for checkout on edit | 编辑时提示签出。若启用，则在修改已添加到版本控制系统但未签出的文件时自动打开 Pending Source Control Operations（待处理版本控制操作）对话框。该对话框会提示签出被修改的文件。  若禁用，则只有尝试保存 Wwise 工程才会提示签出被修改的文件。 |
| **Original Audio Files** | |
| Use project's location | 使用工程的位置。指定保存工程的原始媒体文件文件夹的位置。该路径可与工程的目录相关，也可以是绝对路径。默认位置为“Originals”。 |
|  | 打开 Browse for Folder 对话框以选择要将原始媒体文件存储到哪个位置。  |  |  | | --- | --- | | [备注] | 备注 | | 使用浏览按钮选择文件时，如有可能，Wwise 将自动将路径解析为（相对于工程的）相对路径。 | |
| 不沿用当前用户的位置 | 仅为当前用户指定新位置。该路径可与工程的目录相关，也可以是绝对路径。  这在以下情形中十分实用：  - 您暂时没有 Originals 文件夹的访问权限。 - 您没有更改 Originals 文件夹内容的权限。 - 您需要为 Originals 文件夹创建临时位置，而不更改工程的 Originals 文件夹的位置。 |
|  | 打开 Browse for Folder 对话框以重新选择要将当前用户的原始媒体文件存储到哪个位置。  |  |  | | --- | --- | | [备注] | 备注 | | 使用浏览按钮选择文件时，如有可能，Wwise 将自动将路径解析为（相对于工程的）相对路径。 | |
| **Cached Audio Files（缓存音频文件）** | |
| Use project's location | 使用工程的位置。指定保存工程的缓存文件文件夹的位置。该路径可与工程的目录相关，也可以是绝对路径。默认位置为“.cache”。 |
|  | 打开 Browse for Folder 对话框以选择要在将工程缓存文件存储到哪个位置。  |  |  | | --- | --- | | [备注] | 备注 | | 使用浏览按钮选择文件时，如有可能，Wwise 将自动将路径解析为（相对于工程的）相对路径。 | |
| 不沿用当前用户的位置 | 仅为当前用户指定新位置。该路径可与工程的目录相关，也可以是绝对路径。  这在以下情形中十分实用：  - 您暂时没有权限访问缓存文件夹。 - 您没有权限改变缓存文件夹的内容。 - 您需要为缓存文件夹创建一个临时存储位置，同时不改变工程的缓存文件夹的位置。 |
|  | 打开 Browse for Folder 对话框以重新选择要将当前用户的工程缓存文件存储到哪个位置。  |  |  | | --- | --- | | [备注] | 备注 | | 使用浏览按钮选择文件时，如有可能，Wwise 将自动将路径解析为（相对于工程的）相对路径。 | |
| **Event Creation（事件创建）** | |
|  | Event Creation 设置为新创建的事件指定的名称。  - **Define settings for project** —— 定义工程的设置。为工程指定 Event Creation 设置。 - **Override settings for current user** —— 不沿用当前用户的设置。仅为当前用户指定 Event Creation 设置。 |
| Add action name | 添加动作名称。在启用后，新建事件的动作名称将用来创建事件名称：  - **set as prefix** —— 设置为前缀。该 action 名称用作前缀：<action\_name>\_<object\_name>。 - **set as suffix** —— 设置为后缀。该 action 名称用作后缀：<object\_name>\_<action\_name>。 |
| Modify case | 修改大小写。如果启用，则新事件名称的大小写将设置为：  - **all lowercase** —— 全部小写。新事件de名称为全部小写。 - **all uppercase** —— 全部大写。新事件的名称为全部大写。 |
| **User Interface** | |
| Project color  |  | | --- | |  | | 单击图标可打开颜色选择器。  |  | | --- | |  |  选择颜色并将其应用于此工程的 Wwise 菜单条。  |  |  | | --- | --- | | [备注] | 备注 | | 若选中颜色选择器最左侧方块，则对象沿用其父对象的颜色。若针对对象显式选择某种颜色，则显示调色板图标并在右下角标注黄色三角（如图所示）。 | |
| **Saved Files** | |
| Line Ending | 行结束符。指定以下文件中的行结束符：  - 工程文件：`.wproj` - 工程设置文件：`.wsettings` - Work Unit 文件：`.wwu` - `Wwise_IDS.h` - SoundBank 文件：  - Bank、Event 和 Bus 文件：`.xml`、`.json`、`.txt`   - `ProjectInfo.xml`、`ProjectInfo.json`   - `PlatformInfo.xml`、`Platform.json`   - `SoundbanksInfo.xml`、`SoundbanksInfo.json`   - `PluginInfo.xml`、`PluginInfo.json`  选项包括：  - **LF (default)** - **CRLF** – 在有些版本控制工作流程中可能更好一些。详请参阅[“结合版本控制系统使用 Wwise”一节](../../../03-设置工程/04-Working-with-a-team/03-结合版本控制系统使用-Wwise.md "结合版本控制系统使用 Wwise")。 |
|  | 确定。关闭 Project Settings 对话框并保存设置。 |
|  | 取消。关闭 Project Settings 对话框而不保存设置。 |

**相关主题**

- [“配置版本控制插件”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/01-定义工程的常规设置.md#configuring_source_control_plug_ins "配置版本控制插件")
- [“定义 Originals 文件夹设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/01-定义工程的常规设置.md#defining_originals_folder_settings "定义 Originals 文件夹设置")
- [“定义缓存文件夹设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/01-定义工程的常规设置.md#defining_cache_folder_settings "定义缓存文件夹设置")
- [“了解滤波器属性行为（LPF 和 HPF）”一节](../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/03-了解滤波器属性行为（LPF-和-HPF）.md "了解滤波器属性行为（LPF 和 HPF）")

---