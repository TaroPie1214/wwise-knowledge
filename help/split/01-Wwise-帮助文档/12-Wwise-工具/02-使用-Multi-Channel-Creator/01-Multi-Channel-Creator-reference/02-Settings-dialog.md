# Settings dialog

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 工具](../../00-Wwise-工具.md) > [使用 Multi-Channel Creator](../00-使用-Multi-Channel-Creator.md) > [Multi-Channel Creator reference](00-Multi-Channel-Creator-reference.md) > Settings dialog

### Settings dialog

In the Settings dialog, you can define the file name suffixes that the Multi-Channel Creator will use to identify which channels exist for each audio file. 单声道和立体声文件必须使用不同的前缀。您还可以指定当组合不同长度的文件来创建多声道文件时将如何处理这些文件。

To access the Settings dialog, click **Settings > Settings** in the Multi-Channel Creator window.

| 界面元素 | 描述 |
| --- | --- |
| When file lengths are different | 当文件长度不相同时。确定不同长度的源文件在合并后如何进行处理。您可以选择以下选项之一：  - **Abort operation** —— 停止特定文件的生成过程，但继续批量生成其它文件。 - **Pad shortest files with silence** —— 向短文件的结尾添加无声音源，使所有源文件具有相同长度。 |
| **Suffixes** | |
| **后缀。设置单声道前缀** | |
| Channels | 声道。构成多声道音频文件的不同单声道音频声道。 |
| Suffixes | 后缀。代表不同音频声道的若干个字母。这些前缀必须添加至各个源文件名的末尾，以使 Multi-Channel Creator 能够识别特定音频文件中包含的声道。 |
| **设置立体声声道前缀** | |
| Channels | 声道。不同类型的立体声音频声道。 |
| Suffixes | 后缀。代表不同音频声道的若干个字母。这些前缀必须添加至各个源文件名的末尾，以使 Multi-Channel Creator 能够识别特定音频文件中包含的声道。 |
| Anonymous configuration separator | 匿名配置分隔符。定义匿名配置的前缀分隔符。此类配置的前缀定义为 [匿名配置的前缀分隔符][数字]。例如，输入“.”作为分隔符。这样有效的前缀示例为“.45”。将字段保留空白，以禁用全部匿名配置。 |
|  | Closes the dialog after saving the changes you made to the settings. |
|  | Closes the dialog without saving any changes you have made to the settings. |

---