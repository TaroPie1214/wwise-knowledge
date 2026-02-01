# Import Conflict Manager 对话框

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Importing](00-Importing.md)  > Import Conflict Manager 对话框

### Import Conflict Manager 对话框

In the Import Conflict Manager dialog, you can view and resolve, if possible, the two types of errors that occur during the import process:

- **Recoverable errors**（可恢复错误）是您可以更正或可以自动更正的错误；例如，媒体文件已经存在或文件名不正确。
- **Non-recoverable errors**（不可恢复的错误）需要您替换无法导入的文件，或者修改这些文件后才能导入。导入 Wwise 不支持的音频格式，或者导入属性超出 Wwise 指定范围的文件，都会导致不可恢复的错误。

The Import Conflict Manager dialog has two sections:

- Error
- Import File

|  |  |
| --- | --- |
| [备注] | 备注 |
| 导入文件。在 Import Conflict Manager 中选择 Replace（替换）操作将替换现有文件。此操作无法撤消，即使通过 Undo 操作也无法撤消。找回被替换文件的唯一方法是重新导入该文件，即用该文件之前的版本替换该文件。 |

| 界面元素 | 描述 |
| --- | --- |
| Import destination | 导入目标。文件将导入至此对象 |
| Import language/SFX | 文件作为 Sound Voice 对象导入时的指定语言。对于音效声和音乐对象，将显示为 SFX。 |
| Set all to | 将所有项设置为。选择其中一个命令键，会将操作应用于 Error 列表中的所有可恢复错误。  - **Replace** -- 替换。当存在同名媒体文件时，选择此命令会将所有现有媒体文件替换为导入的文件。 - **Use Existing** -- 使用现有文件。当存在同名媒体文件时，选择此命令会使用现有文件，而非导入的文件。 - **Cancel** -- 取消。在存在同名媒体文件时，选择此命令会取消媒体文件导入。  |  |  | | --- | --- | | [备注] | 备注 | | 导入文件。在 Import Conflict Manager 中选择 Replace（替换）操作将替换现有文件。此操作无法撤消，即使通过 Undo 操作也无法撤消。找回被替换文件的唯一方法是重新导入该文件，即用该文件之前的版本替换该文件。 | |
| **Error** | |
| Audio File | 出错媒体文件的名称。 |
| Status | 导入文件的错误状态：  - 不可恢复的错误会显示为红色。 - 可恢复错误会显示为白色。 - 已恢复错误会显示为白色的 Ready（就绪）状态。 |
| Message | 提供有关错误和解决方案（如果有的话）的信息。 |
| Operation | 操作。可能解决可恢复错误的操作列表。  - **Replace** —— 当存在同名媒体文件时，选择此命令会将现有文件替换为导入的文件。如果您选择了 **Create new objects** 导入模式，使用该选项将替换现有文件并创建新的 Wwise 对象。 - **Use Existing** - 若已经存在媒体文件，选择此选项会使用现有文件而非导入的文件。 - **Cancel** - 若已经存在媒体文件，选择此选项会取消音频导入。如果出现了不可恢复的错误，则只能使用 Cancel 操作。  |  |  | | --- | --- | | [备注] | 备注 | | 导入文件。在 Import Conflict Manager 中选择 Replace（替换）操作将替换现有文件。此操作无法撤消，即使使用 Undo（撤消）操作也无法撤消。找回被替换文件的唯一方法是重新导入该文件，即用该文件之前的版本替换该文件。 | |
|  | 将错误日志中的信息复制到 Windows 剪贴板，以便将信息粘贴到新的文件中。 |
| **Import Files（导入文件）** | |
| Audio File | 音频文件。显示可供导入的文件的名称。 |
| Status | 状态。显示要导入文件是否为 Ready 状态。 |
|  | Opens the Importing dialog where you can view the progress of the file import and stop the import if required. |
|  | Closes the Import Conflict Manager dialog without performing any operations on the files. |

**相关主题**

- [“管理文件导入问题”一节](../../../03-设置工程/05-管理工程中的媒体文件/04-管理文件导入问题.md "管理文件导入问题")
- [“管理可恢复的错误”一节](../../../03-设置工程/05-管理工程中的媒体文件/04-管理文件导入问题.md#managing_recoverable_errors "管理可恢复的错误")
- [“管理不可恢复的错误”一节](../../../03-设置工程/05-管理工程中的媒体文件/04-管理文件导入问题.md#managing_non_recoverable_errors "管理不可恢复的错误")

---