# SoundBank 编辑器 —— Details（详细信息）选项卡

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [SoundBanks 选项卡](../00-SoundBanks-选项卡.md) > [SoundBank Editor 视图](00-SoundBank-Editor-视图.md) > SoundBank 编辑器 —— Details（详细信息）选项卡

#### SoundBank 编辑器 —— Details（详细信息）选项卡

SoundBank 编辑器的 Details 选项卡将显示所选 SoundBank 内不同元素的大小，以及缺失文件相关的信息。该选项卡中的信息将按语言种类排序。

| 界面元素 | 描述 |
| --- | --- |
| Name | SoundBank 的名称。 |
| Notes | 备注。SoundBank 的其它信息。 |
| Maximum size | 最大内存量。为该 SoundBank 设置的最大游戏内存占用量。  **Units**：字节 |
| Date updated | 更新日期。SoundBank 创建或最后一次更新的日期和时间。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Types（类型） | 类型。对应 SoundBank 中包含的各种对象类型，如 SFX、Voice 和 Music。如果 SoundBank 包含所有四种对象，则该列将显示“All”（全部）。 |
| Languages（语言） | 语言。当前工程中使用的语言列表。如果使用了多种语言，则这些语言将按字母顺序显示。  如果 SoundBank 中不包含 Voice 对象，则该栏为空。 |
| SFX（音效） | 音效。当前 SoundBank 中声音 SFX 对象占用的内存量。  **Units**：字节 |
| Music | 当前 SoundBank 中音乐对象占用的内存量。  **Units**：字节 |
| Voice | 语音。特定语言的 Sound Voice 对象占用的内存量。  **Units**：字节 |
| Data Size（数据大小） | 数据大小。音效声和特定语言的 Sound Voice 对象占用的内存量。  如果超出为该 SoundBank 设置的最大内存量，则当前大小将显示为红色。  **Units**：字节  |  |  | | --- | --- | | [备注] | 备注 | | 即使超出您指定的最大内存量，仍然可以成功生成 SoundBank。 | |
| Free Space | 剩余空间。SoundBank 中的剩余空间量。剩余空间是由最大内存量减去数据大小得到的。如果数据大小超出最大内存量，则剩余空间值将显示为红色。  **Units**：字节 |
| Missing Files | 缺失文件。该语言缺失的媒体文件（音效声和 Sound Voice ）数量。 |
| Files Replaced | 已替换的文件。该语言中缺失且被参考语言的音频文件所取代的 Sound Voice 音频文件数量。 |
| Memory Size | 内存大小。要加载至内存的 SoundBank 数据所占用的空间量。  **Units**：字节 |
| Prefetch Size | 预取大小。流播放媒体文件的预取数据占用的空间量。当加载 SoundBank 时会将该信息加载至内存，以确保流播放媒体文件没有延迟。  **Units**：字节 |
| File Size | 文件大小。生成的 SoundBank 文件的总大小。  **Units**：字节 |

**相关主题**

- [“监控 SoundBank 的详细信息”一节](../../../../07-完善工程/07-管理-SoundBank/05-为工程生成-SoundBank.md#monitoring_details_of_soundbank "监控 SoundBank 的详细信息")

---