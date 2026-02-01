# SoundBanks Settings - External Sources 选项卡

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [视图](../../00-视图.md) > [SoundBank Manager 视图](../00-SoundBank-Manager-视图.md) > [SoundBanks Settings 对话框](00-SoundBanks-Settings-对话框.md) > SoundBanks Settings - External Sources 选项卡

#### SoundBanks Settings - External Sources 选项卡

您可以在 SoundBanks Settings（音频包设置）对话框的 External Sources（外部源）选项卡中为 [“External Source（外部源）”一节](../../../../10-Wwise-插件/03-源插件/03-External-Source（外部源）/00-External-Source（外部源）.md "External Source（外部源）") 插件所用的外部源指定自定义设置。您可以选择不沿用现有的工程设置，转而使用自己的 External Sources List 文件。您也可以指定不同的输出文件夹来将 External Source 音频文件保存在其中以供游戏使用。

| 界面元素 | 描述 |
| --- | --- |
| Convert external sources when generating banks | 在生成 SoundBank 时对外部源进行转码。若启用，则在生成 SoundBank 时将 [External Source](../../../../10-Wwise-插件/03-源插件/03-External-Source（外部源）/00-External-Source（外部源）.md "External Source（外部源）") 音频文件转码为 WEM 格式。只有将文件转码为 WEM 格式，声音引擎才能在运行时使用；不过，若不在本地使用这些文件，则可禁用该选项来加快 SoundBank 生成速度。  Default value: true |
| Override Input Path | 不沿用输入路径。不沿用现有的工程设置，转而使用不同的 External Sources List 文件。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Platform | 工程中当前处于激活状态的各种平台的名称。 |
| External Sources List | 外部源列表。External Sources List 文件所在的完整路径。  此数据文件包含与 External Sources 插件所用外部源相关的信息。 |
| (浏览) | 打开 Windows 浏览器，您可以前往输入音频源列表文件所在的文件夹。 |
| Override Output Path | 不沿用输出路径。不沿用现有的工程设置，转而为 External Sources 插件所用的转码音频文件指定自定义的输出文件夹。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Platform | 工程中当前处于激活状态的各种平台的名称。 |
| External Sources Output Folder | 外部源输出文件夹。将转码后的 External Source 输出到该文件夹。 |
| (浏览) | 打开 Browse For Folder 对话框以选择要将转码后的外部音频源保存到哪个文件夹。 |
|  | 确定。关闭 Project Settings 对话框并保存设置。 |
|  | 取消。关闭 Project Settings 对话框而不保存设置。 |

**相关主题**

- [“为 External Source 指定用户设置”一节](../../../../07-完善工程/07-管理-SoundBank/04-配置用户-SoundBank-设置.md#specifying_input_ouput_location_for_external_source_files "为 External Source 指定用户设置")
- [“Auto-defined SoundBank”一节](../../../../07-完善工程/07-管理-SoundBank/02-SoundBank-管理策略/05-Auto-defined-SoundBank.md "Auto-defined SoundBank")

---