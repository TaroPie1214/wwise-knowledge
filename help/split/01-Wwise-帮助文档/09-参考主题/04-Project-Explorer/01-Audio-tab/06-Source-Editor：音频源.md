# Source Editor：音频源

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [Audio tab](00-Audio-tab.md) > Source Editor：音频源

### Source Editor：音频源

音频源的 Source Editor（源编辑器）与[插件的 Source Editor](03-Containers-hierarchy-sound-and-motion-objects/14-Source-Editor-plug-ins.md "Source Editor: plug-ins") 有所不同。它可以从 [“Contents Editor: Sound SFX”一节](03-Containers-hierarchy-sound-and-motion-objects/12-Contents-Editor-Sound-SFX.md "Contents Editor: Sound SFX")、[“Contents Editor（内容编辑器)：Music Track（音乐轨）”一节](04-Containers-hierarchy-music-objects/07-Contents-Editor（内容编辑器)：Music-Track（音乐轨）.md "Contents Editor（内容编辑器")：Music Track（音乐轨）")、 或 [“Contents Editor: Sound Voice”一节](03-Containers-hierarchy-sound-and-motion-objects/13-Contents-Editor-Sound-Voice.md "Contents Editor: Sound Voice")打开。为此，可直接双击音频源图标或使用键盘快捷方式（默认为 Shift + X）。

![](../../../../../images/open_source_editors.png)

|  |  |
| --- | --- |
|  | 打开与音频源对应的 Source Editor |
|  | 打开与插件对应的 Source Editor |

|  |  |
| --- | --- |
| [备注] | 备注 |
| SoundSeed Grain 是一款付费插件，可为 Wwise 用户提供粒子合成功能。与其他插件不同的是，其设有 Source 选项卡。它跟音频源的 Source Editor 大致相同。除此页面中提供的信息外，Soundseed Grain 用户可查阅 [“Source settings”一节](../../../10-Wwise-插件/03-源插件/10-Soundseed-Grain/02-Source-Editor-Soundseed-Grain.md#ssg_source_settings "Source settings")，了解 Soundseed Grain 特定功能的详细信息。 |

这里提供了音频源的相关信息，包括音频文件的名称和时长。音频源是音频文件与对象之间的独立抽象层。音频源在原始音频文件导入工程时创建，并链接到原始音频文件。

有关 Source Editor 的详细信息，请参阅[“利用 Source Editor 编辑音频源”一节](../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/01-利用-Source-Editor-编辑音频源.md "利用 Source Editor 编辑音频源")。

| 音频源属性 | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| [source name] | 音频源。音频源文件的名称。 |
| Notes | 备注。对象属性的额外信息。 |

| Source 选项卡 | |
| --- | --- |
| 界面元素 | 描述 |
| **Graph View（坐标图视图）**（请参阅[*了解坐标图视图*](../../../08-使用-Wwise/07-了解坐标图视图/00-了解坐标图视图.md "了解坐标图视图")了解概述。） | |
| Waveform  |  | | --- | |  | | 波形。在时间线上显示 PCM（WAV 或 AMB）文件的内容，提供 [Peak 或 RMS 模式](06-Source-Editor：音频源.md#mode)。  有关声道名称和配置的详细信息，请参阅[“了解总线配置”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。 |
| Envelope Edit - HDR | 包络编辑 - HDR。定义是否启用 HDR 包络的编辑功能。要显示此选项，必须满足以下条件：  - 父对象连到启用了 HDR 的总线 - 父对象启用了 Envelope Tracking（包络跟踪） |
| Fade-in handle | 淡入起点。定义淡入区域。可右键点击淡入曲线来选择要应用的淡变曲线。 |
| Fade-out handle | 淡出终点。定义淡出区域。可右键点击淡出曲线来选择要应用的淡变曲线。 |
| /  (Play cursor) | 时间线与波形在 Play Cursor 操作方面有所不同。The timeline allows you to drag and drop the Play Cursor to wherever you want the playback to start from. 而在波形上则无法拖放 Play Cursor。不过，可通过直接单击波形实现同样的效果。  将 Play Cursor 移动至所需起始点来自定义 Sound SFX（音效）或 Sound Voice（语音）的起始位置时，只会影响创作工具中的声音播放。在游戏中，无论通过哪种间接对象（比如与 Sound SFX 或 Sound Voice 的父对象或 Event）来调整 Play Cursor，片段都不会从自定义起始点开始播放，而只会从头开始。  单击 Transport 的 Play 按钮会从播放光标的位置播放片段。当播放光标前进时单击 Play 按钮将添加新的播放光标，并从第一个播放光标的起始位置同时播放。  |  |  | | --- | --- | | [备注] | 备注 | | 对于 Vorbis 编码的音频源，只有当转码时启用了 Seek Table（寻址表）时，Source Editor 的 Play Cursor 才会起作用。 | |
| |  | | --- | |  | | 标识音频源完好度问题。  将鼠标放在图标上方以查看有关工具提示点的完好度问题。  点击黄色三角形图标以尝试解决问题。  有关完好度问题的详细信息，请参阅[“解决音频源完好度问题”一节](../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/02-解决音频源完好度问题.md "解决音频源完好度问题")。  |  |  | | --- | --- | | [注意] | 注意 | | 如果聚焦到坐标图的特定区域，则用来显示提醒图标的坐标图右上角可能会隐藏起来。 | |
| Mode | 模式。定义用于显示波形的模式。  - **Peak**：标准显示模式。显示各个声道。这些值代表绘制区域的峰值 PCM 值，单位：分贝。 - **RMS**：显示 RMS（均方根）值。折叠所有声道。这些值代表绘制区域的峰值 RMS 值。 |
| Reset | 重置以下元素：  - 裁剪区的开头和结尾 - 循环开头和结尾 - Override file loop points - 淡入和淡出 - Crossfade duration - HDR 包络 - 播放指针 |

| Conversion 选项卡 | |
| --- | --- |
| 界面元素 | 描述 |
| **Conversion Settings（转码设置）**  For a description of the Conversion Settings group properties, refer to [“Conversion category: Containers hierarchy objects”一节](05-Common-tabs-and-categories-audio-structures/09-Conversion-category-Containers-hierarchy-objects.md "Conversion category: Containers hierarchy objects"). | |
| **File Properties**  The File Properties group has three columns:  - [property name] - Original（原始）：表示文件的原始版本。 - Converted（转码后）：表示文件的转码后版本。 | |
| File Path | 文件路径。源文件的完整路径。  |  |  | | --- | --- | | [技巧] | 技巧 | | As paths can be too long to fit the group, you may want to drag the column header splitters to see the full path. 或者，也可使用 **Open containing folder** 快捷菜单选项直接转到文件存放位置。 | |
| Channels（声道） | 声道。音频源文件中包含的不同音频声道的数量。 |
| 采样率 | 采样率。表示音频源数字音频信号的每秒采样次数，单位：赫兹（Hz）。 |
| File Size | 文件大小。描述音频源文件所占内存大小的值和度量单位。 |
| Duration | 时长。音频源文件从开始到结束的时间长度，单位：秒。 |
| Bandwidth | 带宽。在给定时间内可能传输的最大数据量。  单位：KB/s（每秒千字节数） |
| Format | 格式。音频源文件的音频格式，例如 PCM 或 ADPCM。 |

**相关主题**

- [“利用 Source Editor 编辑音频源”一节](../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/01-利用-Source-Editor-编辑音频源.md "利用 Source Editor 编辑音频源")

---