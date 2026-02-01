# SoundBank编辑器 —— Edit（编辑）选项卡

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [SoundBanks 选项卡](../00-SoundBanks-选项卡.md) > [SoundBank Editor 视图](00-SoundBank-Editor-视图.md) > SoundBank编辑器 —— Edit（编辑）选项卡

#### SoundBank编辑器 —— Edit（编辑）选项卡

SoundBank 编辑器的 Edit 选项卡中显示了将包含在 SoundBank 中的各个工程元素。该列表详细列出了被添加至 Add 选项卡的对象层级包含的各个元素。您可通过该详细列表来调整 SoundBank 中的内容，弃用特定事件、对象结构或媒体文件。

显示 SoundBank 中媒体文件的详情，包括采样率、音频格式和文件大小。通过掌握这些附加信息，您可以轻松地微调各个文件的转码设置，以遵守特定平台的限制。要更改媒体文件的转码设置，只需右键点击列表中的条目并选择 Conversion Settings 即可。

如果要从 SoundBank 中弃用特定元素，则只需将该元素取消勾选即可。点击任一列的标题栏可按字母升序/降序来排列工程元素。您也可以使用搜索或筛选器来快速找到特定元素。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | SoundBank 的名称。 |
| Notes | 备注。SoundBank 的其它信息。 |
| Search | 筛选列表中显示的工程元素。  在该文本框中输入全部或部分名称，则仅有名称中包含相应字符的元素会被显示。 |
|  | 清除 Search 栏中的内容。  清除 Search 栏后，将重新显示 SoundBank 中工程元素的完整列表。 |
| （语言筛选器） | 按语言筛选列表。  您可通过语言筛选器来查看每种语言的 SoundBank 内容。 |
| （对象筛选器） | 按对象类型筛选列表。  您可使用以下任意对象类型对列表进行筛选：  **Events**（事件）：仅显示添加至 SoundBank 的 Event。  **Structures**（结构）— 仅显示添加至 SoundBank 的对象结构。  **Media**（媒体）— 仅显示添加至 SoundBank 的媒体文件。 |
| 包含 | 决定 SoundBank 中是否包含某个事件、对象或媒体文件。  要从 SoundBank 中弃用对象元素，请取消选中相应的复选框。  如果弃用了父对象，则也将自动弃用所有相应的子对象。 |
| Object（对象） | 对象。当前 SoundBank 中所有对象结构、事件和媒体文件的列表。  点击列标题栏，可以按字母升序或降序来排序信息。 |
| 采样率 | 采样率。SoundBank 中的音频文件的采样率。  采样率定义了每秒内对数字音频信号进行采样的次数，单位为赫兹 (Hz)。各个平台的采样率范围各不相同，最高 48,000 Hz。  如果媒体文件尚未针对当前平台转码，则采样率信息将以蓝色显示；如果工程缺失原始媒体文件，则以红色显示。 |
| Format | SoundBank 中的音频文件的格式，例如 PCM、Vorbis 或 ADPCM。请参阅 [“About audio formats”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/01-Creating-audio-Conversion-Settings-ShareSets.md#about_audio_formats "About audio formats") 了解关于为平台选择音频文件格式的详细信息。  如果媒体文件尚未针对当前平台转码，则格式信息将以蓝色显示；如果工程缺失原始媒体文件，则以红色显示。 |
| Memory Size | 内存大小。当 SoundBank 加载至内存中时，已转码的媒体文件将占用的平台内存量。  **Unit**（单位）：字节  如果选择流播放媒体文件，则内存大小将为零。 |
| Decoded Size | 解码后大小。在当前所选平台下，包含解码后 Opus 或 Vorbis 媒体的 SoundBank 所要使用的游戏内存量。若 SoundBank 不含 Opus 或 Vorbis 媒体文件，则此值与 Data Size 相同。  |  |  | | --- | --- | | [备注] | 备注 | | 如果 SoundBank 包含 Sound Voice 对象，则与 Data Size 列一样， 根据当前所选语言不同，Decoded Size 列也将更新。 |    **Units**：字节 |
| Prefetch Size | 预取大小。当 SoundBank 加载至内存中时，流播放媒体文件的预取数据将占用多少平台内存量。  预取数据将被加载至内存中，以确保流播放媒体文件没有延迟。  **Unit**（单位）：字节 |
| File Size | 已转码媒体文件的总大小。  该数字不代表将生成 SoundBank 中的数据量，因为还取决于是否流播放媒体文件及其预取状态。  **Unit**（单位）：字节 |
| ID | 媒体文件的 9 位唯一识别号。 |
|  | 包括 SoundBank 中的所有事件、对象和媒体文件。 |

**相关主题**

- [“在 SoundBank 中启用/弃用工程元素”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/01-在-SoundBank-中启用弃用工程元素.md "在 SoundBank 中启用/弃用工程元素")
- [“搜索 SoundBank 中的元素”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/04-搜索-SoundBank-中的元素.md "搜索 SoundBank 中的元素")
- [“筛选 SoundBank 中的元素列表”一节](../../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/05-筛选-SoundBank-中的元素列表.md "筛选 SoundBank 中的元素列表")
- [“Creating audio Conversion Settings ShareSets”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/01-Creating-audio-Conversion-Settings-ShareSets.md "Creating audio Conversion Settings ShareSets")
- [“对音频文件做转码”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/04-对音频文件做转码.md "对音频文件做转码")

---