# SoundBank 管理策略

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > SoundBank 管理策略

## SoundBank 管理策略

以下章节阐述了可用于在游戏中创建 SoundBank（音频包）的不同方法。在一款游戏中，您可以使用一种方法或多种不同方法的组合。由于各个游戏各不相同，因此您选择的方法将取决于游戏的具体需求。

在创建 SoundBank 时所做的选择会对管理游戏音频和振动素材所需的工作量产生很大影响。而且，还会直接影响游戏的性能。强烈建议声音设计师和音频程序员仔细查看本节内容以便双方充分了解各种可能性。通过协作，您可以提出满足游戏特定需求的策略。在决定要选用怎样的策略时，要考虑内存用量、I/O 访问以及集成到游戏中的便利度。在大多数情况下，关键在于如何很好地兼顾内存用量和集成的便利性。

以下各节中描述了以下方法：

- [“"All-in-one" SoundBank”一节](ch40s02s01.html "\"All-in-one\" SoundBank")
- [“多个完整的 SoundBank”一节](01-多个完整的-SoundBank.md "多个完整的 SoundBank")
- [“细致地管理媒体”一节](02-细致地管理媒体.md "细致地管理媒体")
- [“Prepare 动作事件”一节](03-Prepare-动作事件.md "Prepare 动作事件")
- [“预备 Event 和 Game Sync（Switch 和 State）”一节](04-预备-Event-和-Game-Sync（Switch-和-State）.md "预备 Event 和 Game Sync（Switch 和 State）")
- [“Auto-defined SoundBank”一节](05-Auto-defined-SoundBank.md "Auto-defined SoundBank")

|  |  |
| --- | --- |
| [备注] | 备注 |
| 另外还有其它两种方法，它们融合了现有 LoadBank() 和 PrepareEvent() 方法的长处。使用这两种方法可以 Prepare 整个 SoundBank，这意味着您可以将所有数据和媒体合并到同一个 SoundBank 中，避免内存中出现媒体重复，并只有在需要时才加载媒体。有关 Prepare SoundBank 的详细信息，请参阅 Wwise SDK 文档中的 [“声音引擎集成纵览” > “将 Wwise 元素集成到游戏中” > “Prepare SoundBanks” >“集成详情 —— SoundBanks” > “加载 SoundBank” > “Prepare SoundBank”](https://www.audiokinetic.com/library/?source=SDK&id=soundengine__banks__loading.html#soundengine_banks_preparingbanks)。 |

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在加载包含 [Vorbis](../../../14-词汇表.md#glossary_vorbis "Vorbis") 编码或 [WEM Opus](../../../14-词汇表.md#glossary_opus "Opus") 编码媒体的 SoundBank 时，可利用 "Preparation\_LoadAndDecode"  [PreparationType](https://www.audiokinetic.com/library/?source=SDK&id=namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html) 将媒体文件解码为非压缩 [PCM](../../../14-词汇表.md#glossary_pcm "PCM（脉冲编码调制）") 文件。这会导致 SoundBank 变大，但可缩短在调用时访问媒体的时间，因为在播放时就不用等待解压了。  此策略可与一系列其它方法结合来优化素材的管理。 |

---