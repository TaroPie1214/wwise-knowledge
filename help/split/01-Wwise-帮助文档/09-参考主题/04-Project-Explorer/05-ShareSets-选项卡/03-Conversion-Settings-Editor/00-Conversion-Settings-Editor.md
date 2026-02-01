# Conversion Settings Editor

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [ShareSets 选项卡](../00-ShareSets-选项卡.md) > Conversion Settings Editor

### Conversion Settings Editor

将文件导入 Wwise 后，这些文件需要针对工程中的各个有效平台做转码。由于许多音频源将使用相同的转码设置，因此可以用 ShareSet 来管理工程中的转码设置。在每个 ShareSet 中，您可以定义各种不同的转码设置，包括声道数、音频格式、质量和采样率。通过这些设置，您可以为各个平台优化最终的声音。创建 ShareSet 并进行转码设置后，可以将它们应用于工程中的各种对象。

这里的一些属性将对工程中的品质、性能、内存和 CPU 占用产生重大影响。有关这些问题的详细信息，请参阅[“转码设置的策略”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/05-转码技巧和窍门.md#strategies_for_conversion_settings "转码设置的策略")。

**Conversion Settings Editor** 还显示有关每个平台的原始音频源和转码音频源的信息。利用该信息可以轻松地比较两个文件并找到工程中每个平台的最佳转码设置。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。转码设置共享集的名称。 |
| Shared by | 共享对象。当前采用所选转码设置共享集的对象列表。  使用自定义 Conversion Settings 时，此字段将变为“Used by（使用对象）”。 |
| Notes | 备注。有关转码的详细信息。 |
| Platform | 工程中的平台列表。  转码设置是为工程中的每个平台设置的。 |
| Channels | 声道数。您希望包含在转码文件中的音频声道数。  以下选项可用：  - **As Input** – 同输入。将音频声道数保持与原始媒体文件相同。 - **Mono** – 单声道。所有声道将混合为一个声道，但 LFE 除外，该声道将被弃用。 - **Mono drop** – 单声道弃用。除了第一个声道外，其它所有声道都将被弃用。 - **Stereo** – 立体声。所有声道都将混合到左前和右前声道，但 LFE 除外，该声道将被弃用。 - **Stereo drop** – 立体声弃用。除了左声道和右声道外，其它所有声道都被弃用。  有关 Wwise 如何处理音频声道的下混转换的详细信息，请参阅 [创建音频转码设置 ShareSet](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/01-Creating-audio-Conversion-Settings-ShareSets.md "Creating audio Conversion Settings ShareSets") 。  Default value: As Input |
| L-R Mix | 左右混音。左扬声器和右扬声器的信号功率电平，其中 <C> 代表两个扬声器上的功率均等指派。  L-R Mix 控制仅在将单声道声音转换为立体声（反之亦然）时应用。对于所有其它转换，混音都由 Wwise 完成。有关 Wwise 如何处理 L-R Mix 的详细信息，请参阅[“About audio channels”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/01-Creating-audio-Conversion-Settings-ShareSets.md#about_audio_channels "About audio channels")。 |
| Sample Rate | 数字音频信号每秒采样的次数，单位为赫兹 (Hz)。  您可以选择以下选项中的任何一个选项：  - **As Input** - 使用与原始音频文件相同的采样率对文件做转码。如果特定平台或音频格式不支持该采样率，则会改用最接近的可用采样率。 - **Auto (Low/Medium/High)** - 在对文件执行 FFT 分析后，使用 Wwise 选定的采样率对文件做转码。低品质、中品质和高品质设置之间的区别是截止频率阈值，该阈值将用于确定转码结果文件的最佳采样率。您可以通过在 Project Setting 对话框中定义其阈值来微调各种设置的品质高低。 - **300 to 48,000** – 300 至 48,000。使用特定采样率对文件做转码。各种平台和格式对应的采样率范围可能有所不同。  Default value: 0 |
| Min Sample Rate | 最小采样率。仅在 **Sample Rate** 设置为 **As Input** 或 **Auto** 时才会采用。定义转码文件的最小采样率。 |
| Max Sample Rate | 最小采样率。仅在 **Sample Rate** 设置为 **As Input** 或 **Auto** 时才会采用。定义转码文件的最大采样率。 |
| Format | 格式。要针对各个平台将音频源转码成的音频格式。其中包括：  - **[ADPCM](../../../../14-词汇表.md#glossary_adpcm "ADPCM (Adaptive Differential Pulse Code Modulation")")** - **[WEM Opus](../../../../14-词汇表.md#glossary_opus "Opus")** - **[PCM](../../../../14-词汇表.md#glossary_pcm "PCM（脉冲编码调制）")** - **[Vorbis](../../../../14-词汇表.md#glossary_vorbis "Vorbis")**  [并非所有音频格式都支持多声道文件](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/01-Creating-audio-Conversion-Settings-ShareSets.md#about_audio_channels "About audio channels")。比如，若原始文件为多声道文件并要使用对接受的声道配置有限制的编解码器进行转码，则应从 Channels 列表中选择以下选项之一：Mono、Mono drop、Stereo 或 Stereo drop。如果选择 **As Input** 选项，Wwise 将强制下混为立体声或单声道。 |
| Sample rate conversion quality | 品质。压缩文件的品质设置。  某些音频格式（例如 Vorbis）允许进行品质设置。更高的品质设置意味着：  - 更多的磁盘空间需求。 - 更好的音频品质。  Default value: Normal |
| Adv. | 高级。针对某些音频格式的特殊设置。点击 **Edit**（编辑）以对这些格式进行设置。 |
| **Options（选项）** | |
| 采样率转码品质 | 采样率转换品质。确定用于转换采样率的方法。您可以选择以下方法之一；  - **Normal**: 正常。转码品质较好，比“High”（高）选项快 3 到 6 倍。 - **High** —: 最佳转码品质。  如果原始音频内容包含高频，并且您的转码采样率低于 24 kHz，则建议您使用“High”选项。 |
| Insert filename marker | 插入文件名标记。确定是否在文件开头添加带有文件名的标记。  对于将特定动作绑定到声音引擎中的特定文件，例如对口型这种情况，可能会非常有用。  标记仅包含文件名，而没有文件的路径和扩展名。  Default value: false |
| Remove DC offset | 移除直流偏置。移除已转码音频文件的 [DC Offset](../../../../14-词汇表.md#glossary_dc_offset "DC Offset（直流偏置）") 。直流偏置可能会导致 clicking 噪声、音量损失和失真。  下列情况下，最好移除直流偏置：  - 源文件录制质量较差，波形相对于 0 点不对称； - 效果器导致声音存在累积偏置（这种情况很难预测，但有可能是造成问题的原因。）  不过对于以下情况，最好不要移除直流偏置：  - 位于精确到采样点的容器中的声音。 - 归一化为 0 dB 的声音。 - 精确到采样点的循环播放声音。事实上，我们建议不要为循环播放的声音消除直流偏置。消除机制采用高通滤波器，因此不保证将以相同方法修改循环的第一个采样和最后一个采样，因为并不知道这两个样本将连续播放。这可能产生信号中断，导致听到爆音。  Default value: false |
| Apply dither | 应用抖动。对音频源进行比特率转换时应用抖动。  抖动是在量化之前添加到信号中的噪声，目的是减少量化过程导致的失真和噪声调制。抖动仅在采样位深更改（例如从 16 位变为 8 位）时才会应用。  如果不勾选此选项，则将不会应用抖动。默认情况下，此选项已启用。  Default value: false |
| Allow channel upmix | 允许声道上混。如果选中此选项并且 Channel 列表设置为 Stereo 或 Stereo drop，则单声道源文件将在转码期间上混为该立体声配置。如果未选中此选项，则无论 Channel 如何设置，单声道源文件转码时都不会进行上混。  Default value: true |
| **Audio Sources** | |
| Show | 显示。确定哪些信息显示在 Audio Source 列中。您可以选择以下选项之一：  - **Name**: 名称。仅显示音频源名称。 - **Path**: 路径。显示完整路径，包括音频源名称。 |
|  | Opens the Audio File Conversion dialog for the audio sources using this Conversion Setting. 还可以使用音频源列表中的快捷菜单，来对音频源做转码。 |
|  | 将所选平台的转码结果复制到 Windows 剪贴板，以便将它们粘贴到其它应用程序。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Audio Source | 音频源。音频源的名称。在 Show 选项设置为 Path（路径）时，完整路径将会与音频源的名称一起显示。 |
| Language | 音频源的语言。 |
| Orig. Chan. | 源声道。原始音频源的声道配置。 |
| Conv. Chan. | 转码后声道。转码后音频源的声道配置。 |
| Original SR | 原始音频源的采样率。 |
| Converted SR | 转码后音频源的实际采样率。 |
| Original Size | 原始音频源大小。 |
| Converted Size | 转码后的源大小。 |
| Size Ratio | 大小比率。原始音频源大小和转码源大小的比率。 |
| Duration | 时长。转码后音频源的长度（单位为秒）。 |
| Bandwidth | 带宽。在给定时间内可能传输的最大数据量。  单位：KB/s（每秒千字节数）  如果您将鼠标指针放在带宽列中的某个值上，则将会出现以千位/秒（kbps）显示的带宽值提示点。 |

**相关主题**

- [“Creating audio Conversion Settings ShareSets”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/01-Creating-audio-Conversion-Settings-ShareSets.md "Creating audio Conversion Settings ShareSets")
- [“Assigning Conversion Settings ShareSets to objects”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/03-Assigning-Conversion-Settings-ShareSets-to-objects.md "Assigning Conversion Settings ShareSets to objects")
- [“对音频文件做转码”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/04-对音频文件做转码.md "对音频文件做转码")

---