# 什么是 Music Segment？

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [Building your interactive music hierarchies](00-Building-your-interactive-music-hierarchies.md) > 什么是 Music Segment？

## 什么是 Music Segment？

The Wwise Music Segment is the core music object at the base of interactive music. Like the sound object, it contains the audio assets for the music project. However, there are some important differences between a sound object and a Music Segment:

- Music Segment 可以与其它段落对齐。
- Music Segment 与音乐源之间还有另一个层次，即 Music Track（音乐轨）。

### 对齐 Music Segment

Music Segment 可在指定点严格对齐，让配乐编曲无缝衔接。下图说明了如何使用 Sync Point（同步点）或 Cue（提示点）来排列和对齐段落。Cue 是附加在 Music Segment 上的标记，用来指示关键时间点，例如 Entry（入点）和 Exit（出点）。将 Cue 结合曲速拍号设置一起使用，就可以按需对齐播放列表中的各段落。

|  |
| --- |
|  |

### Music Segment 和 Music Track

通常，Music Segment 中至少包含一个 Music Track，您需要用 Music Track 作为中间层来处理 Music Clip（音乐片段）。每个 Music Clip 代表一个音频源，它包含针对不同游戏平台的转码设置，用于转换相应的音频文件。转码过程中，会为各平台创建新文件，而原始音乐文件则保持不变。这样您的互动音乐就可以针对不同目标平台进行优化了。关于针对平台进行音频文件转码，更多信息请参阅[“Authoring across platforms”一节](../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md "Authoring across platforms")。

下图说明了音频文件和声音对象、音频文件和 Music Segment 之间的关系。

|  |
| --- |
|  |

同一声音对象中，可以添加多个音频源，各自链接不同的音频文件，并允许选择其一来播放。不过，若在 Music Track 中添加新的音频源，则会作为另一 Music Clip 添加到该 Music Track，并显示在 Music Segment Editor（音乐段落编辑器）中。

除此之外，还可将 Event 放在 Music Segment Editor 音轨内的特定时间点。

为了便于在界面中识别 Music Segment 和 Music Track，Wwise 分别为其使用了不同的图标。

| 图标 | 代表 |
| --- | --- |
| |  | | --- | |  | | Music Track （音乐轨） |
| |  | | --- | |  | | Music Segment （音乐段落） |

---