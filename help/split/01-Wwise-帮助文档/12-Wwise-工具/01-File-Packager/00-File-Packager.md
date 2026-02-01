# File Packager

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 工具](../00-Wwise-工具.md) > File Packager

## File Packager

在 File Packager 窗口中，可将 Wwise 工程的SoundBank、零散媒体或流播放文件分组到若干个文件包中。根据游戏的需求，您可以将这些文件进行任意组合，并创建文件包。

通过将 SoundBanksInfo.xml 文件导入 File Packager 来进行检索，可以获取Wwise 工程的 SoundBank 和流文件的所有信息。默认情况下，所有文件都会添加到 default.pck 包文件中，该包文件的创建位置在各个平台的 SoundBank 路径根目录下。也可以创建新的文件包，手动将文件添加至其中并修改文件包的储存位置。

|  |  |
| --- | --- |
| [备注] | 备注 |
| In the Project Settings' or the SoundBanks Settings' SoundBanks tab, ensure that the **Generate All Banks Metadata File** and **Generate XML Metadata** options are selected. When these options are selected, Wwise generates the `SoundbanksInfo.xml` file whenever you generate SoundBanks. |

File Packager 窗口还包含文件通路工具，它用来基于语言和文件类型自动将 SoundBank 和流播放文件指派给特定包。

File Packager 中创建的各个会话都可保存为一个工程，以便您可在会话中途随时轻松保存您的工作并随时返回到保存的会话。

有关命令行选项，请参阅[“在命令行中使用 File Packager 参数”一节](../../07-完善工程/08-管理-File-Package/06-在命令行中使用-File-Packager-参数.md "在命令行中使用 File Packager 参数")。

| 菜单 | 描述 |
| --- | --- |
| Tools > Create and assign packages for all language | 工具 > 为所有语言创建和指派包。为语言创建一个新包。针对创建的各个包，将流播放文件、零散媒体和 SoundBank 指派给相应语音的包。如果该语言的包已经存在，则不创建任何包并且不会修改现有包。 |
| Tools > Freeze selected packages | 工具 > 冻结所选包。获取所选包并确保所有内容都非常明确（的确在手动添加的文件中）并且没有隐含的内容。该过程将确保没有指派规则引用所选包。做好的包内容将不会更改。  在您可为其准备可下载内容的游戏版本之后，可使用该功能。它将确保传输的动态创建包已冻结。 |

| 界面元素 | 描述 |
| --- | --- |
| SoundBanks Info file | SoundBank 信息文件。SoundBanksInfo.xml 文件的路径，该文件提供 Wwise 工程内 SoundBank、零散媒体和流播放文件的列表。  SoundBanksInfo.xml 文件的内容将显示在 Files to Package 视图中。  路径可以是绝对路径或相对路径。相对路径相对的是 File Packager 工程文件目录。 |
| |  | | --- | |  | | Opens the Windows Open File dialog where you can select the SoundbanksInfo.xml file that creates a list of all SoundBanks and streamed media files that can be packaged. |
| Output directory | 输出目录。文件包将被保存的网络位置。  路径可以是绝对路径或相对路径。相对路径相对的是 SoundbanksInfo.xml 文件目录。默认情况下，File Packager 使用 SoundbanksInfo.xml 文件目录。 |
| |  | | --- | |  | | Opens the Browse for Folder dialog where you can navigate to the location where you want the package files to be saved. |
| **Files to package（待打包的文件）** | |
| Filename | 文件名。可添加到若干个包的 SoundBank、流播放文件或零散媒体的名称。 |
| File type | 文件类型：SoundBank、流播放文件或零散媒体。 |
| Language/SFX | 语言/音效。与该文件关联的语言。如果文件与任何语言都不关联，则该文件会被认为是音效。 |
| File size | 文件的大小。 |
| Packages | 已经包含了文件的包。 |
| |  | | --- | |  | | 将所选文件添加到 Package Manager 中所选的包中去。 |
| **Packages（文件包）** | |
| Name | 名称。文件包的名称。  该名称是输出目录的相对路径，可包含子文件夹，例如“my\_folder\package1.pck”。 |
| Added | 手动添加到包里的文件数量。 |
| Resulting | 包中包含的结果文件总数。 |
| Missing | 包中缺失的文件数量。  如果文件是手动添加到包中的并且之后从原始 Wwise 工程中删除掉了的话，则这些文件可能会缺失。 |
| Data size | 数据大小。列在包结果内容中的所有文件总和。 |
| Header size | 包的近似文件头大小。它表示将包加载到声音引擎中的近似内存占用量。 |
| |  | | --- | |  | | 创建新的包。 |
| |  | | --- | |  | | 删除当前所选包。 |
| |  | | --- | |  | | 打开 File Order Editor（文件顺序编辑器），您可以在其中以特定顺序排列包内的文件。  排列包内文件的顺序可优化磁盘寻道事件。 |
| Block Size | 块大小。包内数据对齐的字节数。指定什么数字将取决于平台 I/O 设备的要求。有关块大小和各个平台 I/O 设备限制的详细信息，请参阅 SDK 文档的 [Streaming > Low-Level I/O](https://www.audiokinetic.com/library/?source=SDK&id=streamingmanager__lowlevel.html)（流式 > 底层 I/O）部分。  每个平台的默认值都是 1。  默认值 1 表示无需对齐。 |
| **默认文件指派** | |
| Assign Language/SFX files to: | 将语言/音效文件指派给。此版块内的选项用来将与特定语音或音效关联的 SoundBank、零散媒体和流播放文件指派给特定包。  仅在文件并非手动指派给包时才会使用默认指派。 |
| Language | 语言。SoundBank和流播放文件存在的语言/音效列表。 |
| SoundBanks | 音频包。与相应语言/音效关联的 SoundBank 自动指派到的包。  仅在文件并非手动指派给包时才会使用默认指派。 |
| Streams | 流播放。与相应语言/音效关联的流播放文件自动指派到的包。  仅在文件并非手动指派给包时才会使用默认指派。 |
| LooseMedia | 零散媒体。如果文件没有与相应语言/音效存在特定关联，则会自动指派到这种包中。  仅在文件并非手动指派给包时才会使用默认指派。 |
| Assign remaining files to: | 将剩余文件指派给。此版块内的选项用来将所有剩余 SoundBank、流播放文件、外部源和零散媒体连通到特定包。 |
| SoundBanks | 任何剩余的 SoundBank 会自动指派给这种包。 |
| Streamed files | 流播放文件。任何剩余流播放文件会自动指派给这种包。 |
| External source | 外部源。任何剩余外部源都会自动指派给这种包。 |
| Loose media | 零散媒体。任何其它剩余文件都会自动指派给这种包。 |
| **包内容** | |
| Manually added file | 已手动添加到包的 SoundBank、流播放文件、外部源或零散媒体。 |
| Filename | SoundBank、流播放文件、零散媒体或外部源的名称。 |
| File type | 文件类型：SoundBank、流播放文件、外部源或零散文件。 |
| Language/SFX | 语言/音效。与该文件关联的语言。如果文件与任何语言都不关联，则该文件会被认为是音效。 |
| File size | 文件的大小。 |
| Inclusion Mode（仅在 Manually added file 选项卡中可用） | 包含模式。决定SoundBank、其关联的流播放文件或所有零散媒体是否包含在包中。您可以选择以下选项之一：  - **SoundBank only（仅有SoundBank）** - **Streamed file（流播放文件）** - **SoundBank 和流播放文件** - **Loose media（零散媒体）** - **SoundBank 和零散媒体** - **Streamed files and loose media（流播放文件和零散媒体）** - **All files** |
| |  | | --- | |  | | 所有文件。从包中删除所选文件。 |
| Resulting content（结果内容） | SoundBank、流播放文件或零散媒体都包含在包里。  此选项卡标题栏中显示的数字表示包中包含的文件总数。  此选项卡上的数字可能与 Manually added file 选项卡上的数字不同，因为当手动添加 SoundBank 时，会有多个流播放文件自动添加到相同的包的，而 SoundBank 可能包含对这些流播放文件的引用。 |
| Filename | 可添加到包中的SoundBank、零散媒体或流播放文件的名称。 |
| File type | 文件的类型：SoundBank、流播放文件、零散媒体或混合类型。 |
| Language/SFX | 语言／音效。相应文件关联的语言。如果文件与任何语言都不关联，则该文件会被认为是音效。 |
| File size | 文件的大小。 |
| |  | | --- | |  | | 将 Resulting Content 窗格中的信息复制到 Windows 剪贴板，以便您可以将信息粘贴到新的文件中。 |

**相关主题**

- [“使用 File Packager 工程”一节](../../07-完善工程/08-管理-File-Package/01-使用-File-Packager-工程.md "使用 File Packager 工程")
- [“将 SoundBank 信息导入到工程中”一节](../../07-完善工程/08-管理-File-Package/01-使用-File-Packager-工程.md#importing_soundbank_information_into_project "将 SoundBank 信息导入到工程中")
- [“Opening File Packager projects”一节](../../07-完善工程/08-管理-File-Package/01-使用-File-Packager-工程.md#opening_existing_file_packager_projects "Opening File Packager projects")
- [“保存 File Packager 工程”一节](../../07-完善工程/08-管理-File-Package/01-使用-File-Packager-工程.md#saving_file_packager_projects "保存 File Packager 工程")
- [“在工程中添加文件包”一节](../../07-完善工程/08-管理-File-Package/02-Managing-file-packages-in-File-Packager-projects/00-Managing-file-packages-in-File-Packager-projects.md#adding_file_packages_to_project "在工程中添加文件包")
- [“从工程中移除文件包”一节](../../07-完善工程/08-管理-File-Package/02-Managing-file-packages-in-File-Packager-projects/00-Managing-file-packages-in-File-Packager-projects.md#removing_file_packages_from_project "从工程中移除文件包")
- [“Assigning files to packages”一节](../../07-完善工程/08-管理-File-Package/02-Managing-file-packages-in-File-Packager-projects/01-Assigning-files-to-packages.md "Assigning files to packages")
- [“Automatically assigning files to a package”一节](../../07-完善工程/08-管理-File-Package/02-Managing-file-packages-in-File-Packager-projects/01-Assigning-files-to-packages.md#assigning_files_to_package_automatically "Automatically assigning files to a package")
- [“Manually assigning files to a package”一节](../../07-完善工程/08-管理-File-Package/02-Managing-file-packages-in-File-Packager-projects/01-Assigning-files-to-packages.md#manually_adding_files_to_package "Manually assigning files to a package")
- [“对文件包内的文件排序”一节](../../07-完善工程/08-管理-File-Package/02-Managing-file-packages-in-File-Packager-projects/02-对文件包内的文件排序.md "对文件包内的文件排序")
- [“生成文件包”一节](../../07-完善工程/08-管理-File-Package/04-生成文件包.md "生成文件包")

---