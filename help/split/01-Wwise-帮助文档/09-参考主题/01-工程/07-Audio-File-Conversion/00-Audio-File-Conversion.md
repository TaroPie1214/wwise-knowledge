# Audio File Conversion

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > Audio File Conversion

## Audio File Conversion

在 Audio File Conversion（音频文件转码）对话框中，可指定要基于哪些平台、语言和源版本对所选媒体文件进行转码。所选媒体文件会在此过程中进行采样率、比特率、声道格式和格式属性的转换。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若通过 **Project** 菜单的 **Convert All Audio Files** 选项打开 Audio File Conversion 对话框，则将对工程中的所有文件进行转码。若想仅对一个或多个所选音频文件进行转码，请通过 **Edit** 菜单或快捷菜单打开 **Convert** 选项。 |

| 界面元素 | 描述 |
| --- | --- |
| Platforms（平台） | 平台。在 [“Platform Manager”一节](../09-Platform-Manager/00-Platform-Manager.md "Platform Manager") 中为工程定义的所有平台中，根据所选的平台对媒体文件做转码。 |
| Languages（语言） | |
| Current language（当前语言） | 当前语言。仅对当前所选语言的媒体文件做转码。 |
| All languages（所有语言） | 所有语言。针对工程中所有可用的语言，对媒体文件做转码。 |
| **Source（源）** | |
| In Use version（正在使用的版本） | 正在使用的版本。仅对声音对象 Contents Editor 中指定为 In Use（正在使用）的媒体资源版本做转码。 |
| All version（所有版本） | 所有版本。对声音对象的所有媒体资源版本做转码。 |
|  | 确定。基于给定设置对媒体文件进行转码，并关闭 Audio File Conversion 对话框。 |
|  | 取消。关闭 Audio File Conversion 对话框而不执行转码操作。 |

**相关主题**

- [“对音频文件做转码”一节](../../../07-完善工程/01-管理输出/10-对音频文件做转码/04-对音频文件做转码.md "对音频文件做转码")
- [“Creating audio Conversion Settings ShareSets”一节](../../../07-完善工程/01-管理输出/10-对音频文件做转码/01-Creating-audio-Conversion-Settings-ShareSets.md "Creating audio Conversion Settings ShareSets")
- [“Assigning Conversion Settings ShareSets to objects”一节](../../../07-完善工程/01-管理输出/10-对音频文件做转码/03-Assigning-Conversion-Settings-ShareSets-to-objects.md "Assigning Conversion Settings ShareSets to objects")
- [“Authoring across platforms”一节](../../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md "Authoring across platforms")
- [*管理语言*](../../../03-设置工程/03-管理语言.md "管理语言")

---