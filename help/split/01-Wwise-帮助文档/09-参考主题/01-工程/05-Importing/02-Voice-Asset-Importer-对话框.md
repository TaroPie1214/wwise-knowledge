# Voice Asset Importer 对话框

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Importing](00-Importing.md)  > Voice Asset Importer 对话框

### Voice Asset Importer 对话框

在 Voice Asset Importer 中，您可以将制表符分隔文件的内容导入到 Wwise 中，从而在工程中自动创建多个 Sound Voice 对象。Voice Asset Importer 不仅能加速创建过程，而且可以减少可能出现的错误。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 可以在 Microsoft Excel 等外部应用中生成制表符分隔的文本文件。 |

虽然电子表格可能含有各种类型的信息，但 Wwise 仅会读取以下四种类型信息：

- **Filename** —— 文件名。此信息用于创建 Sound Voice 对象和其对应的音频源。最初音频源将为空，但它的确包含对相同名称的音频文件的引用。也就是说，您可以在 Wwise 中像处理其它音频文件那样替换它。
- **Random Container name** —— 随机容器名称。如果文本文件中包含此信息，则将被用于创建相应 Sound Voice 对象的父随机容器。
- **Sound Voice notes** -- 声音对象备注。此信息会添加到 Sound Voice 对象的 Notes（备注）字段。
- **Audio source note** —— 音频源备注。此信息会添加到音频源的 Notes 字段。

文本文件中信息的顺序和信息量并不重要，因为在导入文件之前，您必须指定要导入文本文件中的哪些列。可以通过将文本文件中的列指定为四种信息类型中的一种，来完成此操作。如果文本文件中的某列尚未指定为四种信息类型中的一种，则该列将被 Wwise 忽略。

这其中，只有文件名是必须导入的信息。由于该文件名用于创建 Wwise 的 Sound Voice 对象和音频源，因此文本文件中的每个文件名必须独一无二。关联到音频源的音频文件（WAV）也会使用该文件名。

为了帮您确保各列已正确指定，Voice Assets Importer 还会显示将要创建的对象和导入信息的预览。

| 界面元素 | 描述 |
| --- | --- |
| File to import | 要导入的文件。显示要导入的制表符分隔文本文件的名称和位置。 |
|  | Opens a dialog where you can specify which tab delimited text file you want to import. |
| **导入选项** | |
| Use header | 使用标题。确定标题行名称是否显现在 Column Index（列索引）列表中。如果不选择此选项，Column Index 列表则将使用数字来标记列，例如，Column 1、Column 2 等。 |
| Header row | 标题行。指定文本文件中的哪行包含了列标题。 |
| Start import at row | 数据导入起始行。指定 Wwise 从哪一行开始读取语音素材信息。 |
| Column Type | 列类型。Wwise 可导入的四种类型信息如下所示：  - **Filename** - 将导入的 Sound Voice 对象和音频源名称。 - **Random Container Name** -- 随机容器名称。随机容器的名称。 - **Sound Voice Note** - 将添加到 Sound Voice对象 **Notes** 字段中的信息。例如，您可能会需要添加说话角色的名称。 - **Audio Source Note** - 将添加到音频源 **Notes** 字段的信息。例如，您可能会需要包含所说的实际对话文本。  在 Wwise 中创建语音素材仅需要 Filename 信息。 |
| Column Index | 列索引。用制表符分割的文本文件中包含的可用列列表。您可以将文本文件中的各列映射到 Wwise 中的不同列类型。 |
| **语音素材预览** | |
| Sound Voice（语音声） | Wwise 中将导入的 Sound Voice 对象名称。如果不存在文件名，则列表单元格将显示一个短划线。  这是您在 Wwise 中所创建内容的预览。 |
| Random Container （随机容器） | 随机容器。Wwise 中随机容器的名称。如果没有随机容器，则列表单元格将显示一个短划线。  这是您在 Wwise 中所创建内容的预览。 |
| Sound Note | 将添加到相应 Sound Voice 对象 Notes 字段的信息。如果 Sound Voice 对象没有注释，则单元格中会显示短横线。  这是您在 Wwise 中所创建内容的预览。 |
| Source Note | 源说明。该信息将添加到相应音频源的 Note 字段。如果音频源没有任何备注，则列表单元格将显示一个短划线。  这是您在 Wwise 中所创建内容的预览。 |
| Import Destination | 导入目标。工程层级结构中将创建新语音素材的位置。 |
|  | 打开 Project Explorer - Browser（工程浏览器 —— 浏览器），您可以在其中指定要将新的语音素材创建到哪个 Wwise 对象或文件夹中。 |
| **Custom Properties** 按钮 | 显示 Custom Properties 编辑器对话框，方便为导入的对象设置自定义属性。  |  |  | | --- | --- | | [备注] | 备注 | | 此选项仅在 Project Settings（工程设置）中设置了自定义属性时才可用。 | |
|  | Opens the Importing dialog where you can view the progress of the file import and stop the import if required. |
|  | Closes the Voice Asset Importer dialog without importing the assets from the text file. |

**相关主题**

- [“导入文本文件中的语音素材”一节](../../../03-设置工程/05-管理工程中的媒体文件/02-导入媒体文件/06-导入文本文件中的语音素材.md "导入文本文件中的语音素材")
- [“替换 Sound Voice 媒体文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/03-替换媒体文件.md#replacing_sound_voice_media_files "替换 Sound Voice 媒体文件")

---