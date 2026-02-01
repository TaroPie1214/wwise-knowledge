# File Order Editor 视图

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 工具](../00-Wwise-工具.md) > [File Packager](00-File-Packager.md) > File Order Editor 视图

## File Order Editor 视图

在 File Order Editor（文件顺序编辑器）中，您可以按特定顺序排列包内的文件。对包内的所有文件排序非常耗时而且没有必要。如果包内只有几个文件需要以特定顺序排列，则您可以排列这些文件，然后使用“Remaining files inserted here”（在此处插入剩余文件）占位符来放置包内的所有其它文件。

要访问 File Order Editor，请在 File Packager（（文件打包器））窗口的 Package（包）视图中点击 **Edit file order**（编辑文件顺序）按钮。

| 界面元素 | 描述 |
| --- | --- |
| **Package files（包文件）** | |
| Filename | 添加到包中的SoundBank、流播放文件或零散媒体的名称。 |
| File Type | 文件的类型：SoundBank、流播放文件、零散媒体或混合类型。 |
| Language/SFX | 语言／音效。相应文件关联的语言。如果文件与任何语言都不关联，则该文件会被认为是音效。 |
| File size | 文件的大小。 |
| |  | | --- | |  | | 将所选文件添加到有序列表内的下一个位置。  您还可以从 Package file 视图中直接将文件拖到有序列表内的特定位置。 |
| **File order（文件顺序）** | |
| Filename | 包内已按特定顺序排列的SoundBank、零散媒体或流播放文件的名称。  “Remaining files inserted here”占位符表示包内尚未按具体顺序排列的所有文件。 |
| File Type | 文件的类型：SoundBank、流播放文件、零散媒体或混合类型。 |
| Language/SFX | 语言／音效。相应文件关联的语言。如果文件与任何语言都不关联，则该文件会被认为是音效。 |
| File size | 文件的大小。 |
| |  | | --- | |  | | 从有序列表中删除所选文件。  当某个文件从有序列表中显式删除时，该文件仍保留在包中，但已添加回“Remaining files inserted here”占位符。 |
| |  | | --- | |  | | 从有序列表中删除标记为“missing”的所有文件。 |

**相关主题**

- [“对文件包内的文件排序”一节](../../07-完善工程/08-管理-File-Package/02-Managing-file-packages-in-File-Packager-projects/02-对文件包内的文件排序.md "对文件包内的文件排序")

---