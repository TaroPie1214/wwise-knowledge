# Localizing your project

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [管理平台和语言版本](00-管理平台和语言版本.md) > Localizing your project

## Localizing your project

一个良好的本地化工程不仅包括将 Sound Voice （Sound Voice）对象替换成经过翻译的版本。本地化版本必须能够成功地重建原始语言中创建的同一种音频体验。在技术上，这包括调整和同步不同语言版本的属性，以使本地化工程的品质可与原始版本媲美。根据游戏的发行计划，可以在开发期间同时进行本地化，也可以在游戏完成后再进行本地化。在 Wwise 中，您可以在开发周期中随时进行本地化。与您在一个工程中同时针对多个平台进行制作一样，您也可以在 Wwise 为一个工程中同时创建多个语言版本，并编辑各个语言版本。请参阅 [*管理语言*](../../03-设置工程/03-管理语言.md "管理语言")。

在 Wwise 中，管理工程的本地化包括以下任务：

- 为工程创建语言。
- 定义参考语言。
- 导入语言文件。
- 试听和分析语言版本。

在 Wwise 中，语言版本保存为 Sound Voice 对象的源，并与各个源的不同音频文件相关联。下图展示了声音对象、其语言源和语言文件之间的关系。

|  |
| --- |
|  |

### Importing language files

当语言文件准备就绪时，您可以使用 Audio File Importer 将它们导入工程。导入这些文件时，在 Project Explorer 的 Audio 选项卡内的选定语音对象中会创建语言源，并显示在 Contents Editor 中。如果要立即对工程进行本地化，则可在层级结构的最上层导入经过本地化的文件。

在 Contents Editor 中，您可以根据平台灵活地启用或弃用语言源，以及根据平台选择语言源。有关如何根据语言和源版本进行自定义以及根据平台确定要使用的语言源的详细信息，请参阅：

- [“Selecting sources per platform”一节](01-Authoring-across-platforms.md#selecting_sources_per_platform "Selecting sources per platform")
- [“Excluding project elements from a platform”一节](01-Authoring-across-platforms.md#excluding_project_elements_from_platform "Excluding project elements from a platform").

![](../../../../images/Language_files_importing_online.png)

|  |  |
| --- | --- |
|  | Double-click the voice object to open it in the Property Editor. |
|  | Include or exclude the language for the current platform by selecting or deselecting the **Inc.** check box in the Contents Editor. |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 当您导入音频文件对工程进行本地化时，请确保这些文件的名称与参考语言中的音频文件名称完全相同。 |

**将语言音频文件导入工程的方法是：**

1. Select an object in the Containers hierarchy into which you want to import the language files.

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | You can quickly localize your entire project by selecting the top level parent in the Containers hierarchy and importing the language files at this level. |
2. From the Wwise menu bar, click **Project > Import Audio Files** (or click Shift + I).

   此时将会打开 Audio File Importer。
3. 选择 **Localize languages** 作为**Import Mode**（导入模式）。

   **Import as Sound Voice** 选项将自动选择 ，并且 **Destination language** 菜单变为可用。您正在导入的语言必须是工程中已添加的语言。
4. 点击以下选项之一：

   - **Add Files**

     The File Open dialog, where you can select the media files - AMB, MID, or WAV - that you want to import, opens.
   - **Add Folders**

     The Folder Open dialog, where you can select a folder which contains the media files that you want to import, opens.
   - **Import Tab Delimited**

     The Open dialog, where you can select a tab delimited text file - TXT or TSV - that defines the audio files to import and the structures to create, opens.

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 一个好习惯是先将新文件导入 Originals 文件夹，然后再将新文件从 Originals 文件夹导入工程。 |
5. 浏览至导入的文件或文件夹所在的位置。
6. 选择后，点击**Open**。

   所选文件于是加载到 Audio File Importer 中了。
7. 点击 **Import**（导入）

   这时会打开 Importing（导入）对话框。在此，可查看文件导入流程的进度。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果存在错误或冲突，则将会打开 Import Conflict Manager。有关如何处理这些冲突的详细信息，请参阅[“管理文件导入问题”一节](../../03-设置工程/05-管理工程中的媒体文件/04-管理文件导入问题.md "管理文件导入问题")。 |

   When the import is successfully completed, the Importing dialog closes, and you are returned to the Audio File Importer.
8. When you are finished importing audio files, click **Close** to close the Audio File Importer.

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果您使用版本控制，Wwise 则会提示您将导入文件添加到版本控制系统中。 |

### Switching to a different project language

工程可支持多种语言。请参阅 [*管理语言*](../../03-设置工程/03-管理语言.md "管理语言")。The languages are listed in the Language Selector. 在开发周期内的任何时间点，都可使用 Language Selector 从一种语言切换到另一语言。

**切换工程语言：**

1. 在工具栏中，单击 Language Selector（语言选择器）打开列表。

   ![](../../../../images/ovr_language_selector.png)
2. 选择另一工程语言。

   这时将显示本地化版本的工程。

### Auditioning and profiling language versions

在 Wwise 中您可以像平常一样进行试听，创建模拟，并分析各个语言版本。根据分析结果，您可以决定对平台使用特定的语言源版本或源，以获得最佳和效率最高的效果。

有关试听、模拟和分析语言版本的详细信息，请参阅以下各节：

- [*认识 Transport Control 视图*](../../08-使用-Wwise/05-认识-Transport-Control-视图/00-认识-Transport-Control-视图.md "认识 Transport Control 视图")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")
- [*创建模拟*](../03-创建模拟/00-创建模拟.md "创建模拟")

---