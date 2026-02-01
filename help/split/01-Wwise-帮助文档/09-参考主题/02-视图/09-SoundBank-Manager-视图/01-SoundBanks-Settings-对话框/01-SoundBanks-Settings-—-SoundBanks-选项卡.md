# SoundBanks Settings — SoundBanks 选项卡

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [视图](../../00-视图.md) > [SoundBank Manager 视图](../00-SoundBank-Manager-视图.md) > [SoundBanks Settings 对话框](00-SoundBanks-Settings-对话框.md) > SoundBanks Settings — SoundBanks 选项卡

#### SoundBanks Settings — SoundBanks 选项卡

您可以在 SoundBanks Settings（音频包设置）对话框的 SoundBanks 选项卡中为自己的 SoundBank 设定自定义设置。例如，您可以指定是否为 SoundBank 生成内容和头文件、是否使用 SoundBank 名称，以及 SoundBank 的存储位置。在此对话框内，还可指定要在生成 SoundBank 之前/之后执行的预定义或自定义操作。这些用户设置会覆盖 Project Settings 对话框中定义的 SoundBank 工程设置。

| 界面元素 | 描述 |
| --- | --- |
| 不沿用工程 SoundBank 设置 | 不沿用工程 SoundBank 设置，用来为 SoundBank 创建自定义设置。 |
| Enable Auto-Defined SoundBanks | 启用自动定义的音频包。指定 Wwise 是否针对各个对象自动定义 SoundBank。在设置后，Wwise 可能会针对有些对象自动定义 SoundBank。有关详细信息，请参阅“[“Auto-defined SoundBank”一节](../../../../07-完善工程/07-管理-SoundBank/02-SoundBank-管理策略/05-Auto-defined-SoundBank.md "Auto-defined SoundBank")”。  |  |  | | --- | --- | | [备注] | 备注 | | Wwise 为 Event 自动定义的 SoundBank 仅包含 Event 和引用的 Structure，其会以显式方式排除媒体。若要使用这种 SoundBank，需在游戏代码内添加额外的代码。有关详细信息，请参阅[“了解如何在游戏中加载 SoundBank”一节](../../../../07-完善工程/07-管理-SoundBank/01-了解如何在游戏中加载-SoundBank.md "了解如何在游戏中加载 SoundBank")。 | |
| Copy Loose/Streamed Media | 复制零散/流播放媒体。指定 Wwise 是否在 SoundBank 生成过程中将媒体自动复制到输出文件夹。若启用，则 Wwise：  - 将生成的 SoundBank 所需的媒体文件从 Cache 文件夹复制到输出文件夹。这些文件会被复制到 <output-folder-name>/Media 文件夹。 - 若启用了 **Remove Unused Generated Files**，请从 Media 文件夹移除不必要的文件。  |  |  | | --- | --- | | [备注] | 备注 | | This option replaces CopyStreamedFiles.exe. 之前都是在构建后操作中使用 CopyStreamedFiles.exe 来复制媒体文件。现在已经移除该应用程序。 | |
| Create Sub-Folders for Generated Files | 为生成的文件创建子文件夹。指定是否在输出文件夹中创建子文件夹。若启用，则 Wwise 将为以下内容创建子文件夹：  - 复制的媒体文件。有关详细信息，请参阅 [“管理 SoundBank 媒体”一节](../../../../07-完善工程/07-管理-SoundBank/07-管理-SoundBank-媒体/00-管理-SoundBank-媒体.md "管理 SoundBank 媒体") 章节。 - 自动定义的 SoundBank。有关详细信息，请参阅 [“Auto-defined SoundBank”一节](../../../../07-完善工程/07-管理-SoundBank/02-SoundBank-管理策略/05-Auto-defined-SoundBank.md "Auto-defined SoundBank") 章节。  这些文件将被放在使用关联条目的 ID 命名的子文件夹中。该 ID 的前两个十进制数位按照如下所述确定：  - 对于媒体文件，将媒体的 ID 用于文件名称。 - 对于 SoundBank 文件，可在关联元数据文件 <soundbank-name>.(json|xml) 中找到该 ID。  有关详细信息，请参阅[“SoundBank 输出文件夹布局”一节](../../../../07-完善工程/07-管理-SoundBank/06-SoundBank-输出文件夹布局.md "SoundBank 输出文件夹布局")。  |  |  | | --- | --- | | [备注] | 备注 | | 若要将工程的输出文件夹添加到版本控制系统中，请考虑启用此选项。有些版本控制系统会为每个文件夹的文件数设置固定的限值。此选项可在各个子文件夹中平均分配文件。 | |
| Remove Unused Generated Files | 移除生成但未使用的文件。若选中，则在 SoundBank 生成过程中从输出文件夹移除生成但未使用的文件。移除的文件包括：  - SoundBank (.bnk) 文件。 - 元数据文件（.json、.xml、.txt）。只有在名称已知（如 SoundBanksInfo.json）或同时存在关联 SoundBank (.bnk) 文件时才会移除带有此扩展名的文件。 - 媒体 (.wem) 文件。  若选中该项，还会移除空白文件夹。移除的文件夹包括：  - Auto-Defined SoundBank 文件夹：Event 和 Bus。  |  |  | | --- | --- | | [备注] | 备注 | | 若要将工程的输出文件夹添加到版本控制系统中，请考虑启用此选项。版本控制系统中也会移除所述文件。 | |
| Use Source Control for Generated Files | |  |  | | --- | --- | | [注意] | 注意 | | 若禁用此选项，则即便添加到了版本控制系统中，也不会更新生成的文件的状态。 |  将版本控制系统应用于生成的文件。若选中，则在 SoundBank 生成过程中基于对所生成文件的更改（添加、删除或编辑）来更新版本控制系统状态。更新的文件包括：  - SoundBank (.bnk) 文件。 - 元数据文件（.json、.xml、.txt）。只有在名称已知（如 SoundBanksInfo.json）或同时存在关联 SoundBank (.bnk) 文件时才会移除带有此扩展名的文件。 - 媒体 (.wem) 文件。  |  |  | | --- | --- | | [备注] | 备注 | | 只有配置了版本控制系统，此选项才有效。有关详细信息，请参阅[“General 选项卡”一节](../../../01-工程/08-Project-Settings/01-General-选项卡.md "General 选项卡")。 | |
| Use SoundBank Names for Filenames | 决定在进行以下任务时，使用 SoundBank 名称还是 ID：  - 为生成的 SoundBank 文件命名（如 Init.bnk 或 1355168291.bnk） - 在某一 SoundBank 引用另一 SoundBank 中的媒体时识别目标文件  根据游戏中使用的低级 I/O 实现，该选项可能会影响如何调用 AK::SoundBank::LoadBank()。有关详细信息，请参阅 Wwise SDK 文档中的 [使用 SoundBank 名称](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__banks__general.html) 章节。路径为“声音引擎集成纵览 > 将 Wwise 元素集成到游戏中 > 集成 SoundBank > 集成详情 – SoundBank > 一般信息”。  Default value: true |
| Allow SoundBanks to Exceed Maximum Size | 决定是否允许生成超出大小上限的 SoundBank。 |
| Generate All Banks Metadata File | 为所有音频包生成元数据文件。为每个指定类型（XML 或 JSON）创建一个文件 (SoundbanksInfo.xml/SoundbanksInfo.json)，并在其中列出所有生成的 SoundBank 的信息。此文件包含 SoundBank 名称、路径、语言、所含 Event 和文件（AMB、WAV 和 WEM）以及为 Metadata Options 指定的各项详细信息。  此选项还会创建以下文件（XML 或 JSON）：  - **PluginInfo**：包含工程中所用全部插件的信息。 - **PlatformInfo**：包含工程中所用平台的特定信息。 - **ProjectInfo**：包含工程全局信息（如平台和语言列表）。 |
| Generate Per Bank Metadata Files | 为每个音频包生成元数据文件。为每个指定类型（XML 或 JSON）和单独生成的 SoundBank 创建文件，并在其中列出相关信息。这些文件包含 SoundBank 名称、路径、语言、所含 Event 和文件（AMB、WAV 和 WEM）以及为 Metadata Options 选项指定的各项详细信息。  此选项还会创建以下文件（XML 或 JSON）：  - **PluginInfo**：包含工程中所用全部插件的信息。 - **PlatformInfo**：包含工程中所用平台的特定信息。 - **ProjectInfo**：包含工程全局信息（如平台和语言列表）。 |
| Generate XML Metadata | 生成 XML 元数据。无论启用了哪个 Generate Metadata File 选项，都可在此指定创建 XML 版本。若未启用任何 Generate Metadata File 选项，则将禁用此选项。 |
| Generate JSON Metadata | 生成 JSON 元数据。无论启用了哪个 Generate Metadata File 选项，都可在此指定创建 JSON 版本。若未启用任何 Generate Metadata File 选项，则将禁用此选项。 |
| **Include in Metadata** | |
| Object GUID | 对象 GUID。向被引用对象添加全局唯一标识符。 |
| Object Path | 对象路径。向被引用对象添加对象路径。 |
| Object Color | Adds the color index to referenced objects. To determine the RGB values, consult the theme color definitions in `Authoring\Data\Themes\dark\main.json`, and locate the `ObjectColor_PaletteColor` entries. |
| Max Attenuation | 最大衰减。决定是否在每个 Event 的元数据文件中包含最大衰减信息（详见 [Attenuation Editor](../../../04-Project-Explorer/05-ShareSets-选项卡/02-Attenuation-Editor.md "Attenuation Editor") 中的 Max distance 属性）。只有 “Play Event” 和 “Post Event” Action 可以设为非零值。  Default value: true |
| Estimated duration | 将尝试计算 SoundBank 中每个 Event 的预期时长。对于各个事件，soundbanksinfo.xml 文件中将包含 DurationType、MinDuration 和 MaxDurations 属性。DurationType 可以是以下值：“OneShot”、“Infinite”、“Mixed”或“Unknown”。“OneShot”表示非循环声音；“Infinite”表示循环声音；“Mixed”表示声音可能无限循环（可能基于随机因素或切换开关）；“Unknown”表示 Wwise 无法确定时长。MinDuration 和 MaxDuration 属性表示事件的最短和最长时长。请注意，这些范围仅为估算值，根据运行时条件不同，可能并不完全准确。  Default value: true |
| Root Output Path | 根输出路径。在该文件夹下保存生成的跟平台无关的全局文件。这些文件包括：  - 头文件 (.h)。 - ProjectInfo 元数据文件（.json、.xml）。 |
|  | 浏览。打开 Windows 资源管理器或 Mac Finder，以便更改 SoundBank 头文件的默认保存位置。 |
| Generate header file | 创建包含名称与 ID 映射关系的头文件。头文件用于映射 Event、State、Switch 和 Game Parameter。  该文件将保存在头文件路径中，其命名为“Wwise\_IDs.h”。  如果程序员倾向于在代码中使用 ID，则必须生成头文件。  Default value: false |
| Generate Bank Content TXT Files | 创建文件，其中列出各个 SoundBank 内容。内容文件包含有关 Event、总线、State 和 Switch 的信息以及流播放媒体文件和内存中媒体文件的完整列表。  您可以通过关联列表指定 SoundBank 内容文件的文本文件类型。 |
| **SoundBank Paths（SoundBank 路径）** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Platform | 平台。与特定路径或位置关联的平台的名称。 |
| SoundBank Folder | 保存 SoundBank 的路径或特定文件夹。  根据您使用的是工程位置还是当前用户的自定义位置，该路径或位置可能不同。 |
| (浏览) | 打开 Browse For Folder 对话框以指定新的文件夹来保存各个平台的 SoundBank。 |
| **Pre-Generation Step（预生成步骤）** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Platform | 平台。执行自定义步骤的平台名称，如 Windows、Mac、iOS 和 PlayStation 4。  Global opening step（全局初始步骤）是独立于各平台的步骤，将在其它任何步骤之前执行。 |
| 描述 | 描述命令行的信息。  点击描述后按下 F2，即可在表中直接编辑描述。 |
| Command Line | 一种 shell 命令行，允许在 SoundBank 生成后执行自定义步骤。将流播放文件复制到 SoundBank 保存位置的默认命令行。  点击命令，然后按下 F2 即可直接在表中编辑命令行。如果有多个命令行，则必须打开 Post-Generation Step Editor 才能编辑其它的命令行。 |
| （编辑） | 打开 Pre-Generation Step Editor，以创建和编辑命令行来执行自定义任务。例如，您可以编写命令行，从版本控制系统中 checkout 特定 SoundBank 文件。  除点击 **Edit** 按钮外，您还可以双击表中的行，在 Pre-Generation Step Editor 中打开命令行。 |
| **Post-Generation Step（生成后步骤）** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Platform | 平台。执行自定义步骤的平台名称，如 Windows、Mac、iOS 和 PlayStation 4。  Global opening step（全局初始步骤）是独立于各平台的步骤，将在其它任何步骤之前执行。 |
| 描述 | 描述命令行的信息。  点击描述后按下 F2，即可在表中直接编辑描述。 |
| Command Line | 一种 shell 命令行，允许在 SoundBank 生成后执行自定义步骤。将流播放文件复制到 SoundBank 保存位置的默认命令行。  点击命令，然后按下 F2 即可直接在表中编辑命令行。如果有多个命令行，则必须打开 Post-Generation Step Editor 才能编辑其它的命令行。 |
| （编辑） | 打开 Post-Generation Step Editor，可以创建和编辑命令行，来执行自定义任务。例如，您可以编写命令行，从版本控制系统中 checkout 特定 SoundBank 文件。  除点击 **Edit** 按钮外，您还可双击表中的行，在 Post-Generation Step Editor 中打开命令行。 |
|  | 确定。保存工程设置并关闭对话框。 |
|  | 取消。关闭 Project Settings 对话框而不保存设置。 |

**相关主题**

- [“配置用户 SoundBank 设置”一节](../../../../07-完善工程/07-管理-SoundBank/04-配置用户-SoundBank-设置.md "配置用户 SoundBank 设置")
- [“覆盖工程 SoundBank 路径”一节](../../../../07-完善工程/07-管理-SoundBank/04-配置用户-SoundBank-设置.md#specifying_custom_location_for_saved_soundbanks "覆盖工程 SoundBank 路径")
- [“覆盖工程生成前和生成后操作”一节](../../../../07-完善工程/07-管理-SoundBank/04-配置用户-SoundBank-设置.md#defining_custom_user_steps_to_be_performed_pre_post_soundbank_generation "覆盖工程生成前和生成后操作")
- [“Managing file packages in File Packager projects”一节](../../../../07-完善工程/08-管理-File-Package/02-Managing-file-packages-in-File-Packager-projects/00-Managing-file-packages-in-File-Packager-projects.md "Managing file packages in File Packager projects")
- [“在命令行中使用 File Packager 参数”一节](../../../../07-完善工程/08-管理-File-Package/06-在命令行中使用-File-Packager-参数.md "在命令行中使用 File Packager 参数")

---