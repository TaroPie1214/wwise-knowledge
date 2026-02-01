# 多个完整的 SoundBank

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > [SoundBank 管理策略](00-SoundBank-管理策略.md) > 多个完整的 SoundBank

### 多个完整的 SoundBank

此方法适用于以下情形：

- 游戏或其音频／振动内容可以分成多个部分。

此方法非常适用于单人游戏，在单人游戏中，所有可能用到的声音和振动都只是由玩家在游戏中的当前位置决定的。通过将内容分割成多个 SoundBank，管理内存的效率比第一种方法更高，同时仍可轻松地将音频和振动集成到游戏中。

首先，确定如何拆分 SoundBank（音频包）。以下为示例策略：

- 一个通用 SoundBank，其中包含在游戏任何时刻都可能发生的所有 Event。此 SoundBank 将一直保持载入内存。
- 每个关卡或环境配备一个 SoundBank。根据主人公实际位置变化而需要用到的声音和振动。
- 以及一些额外 SoundBank，具体取决于特定游戏的需求。

**在 Wwise 中创建多个完整 SoundBank 的方法是：**

1. 创建游戏所需的多个 SoundBank，并正确地为它们命名，例如"CommonEvent"、"Level\_1"、"Level\_2"和"Level\_3"。
2. 在 Wwise 中把事件分组到虚文件夹中。为每个 SoundBank 创建一个虚文件夹，然后把每个文件夹拖到相应 SoundBank 中。通过文件夹来添加 SoundBank 内容，就可以避免每次工程中加了新事件时都必须编辑 SoundBank 内容的情况。当虚文件夹中的内容改变时， SoundBank 会自动更新。
3. 将所有 Event 添加到各自的 SoundBank。只有在添加原始文件夹之外的 Event 时（如果有的话）才需要此步骤。如果多个 SoundBank 中需要某个 Event，则只需将它添加到必需的 SoundBank 即可。
4. 生成 SoundBank，并将生成的 SoundBank 文件夹复制到游戏应用程序。

#### 集成

有关集成的详细信息，请参阅 Wwise SDK 文档中的[多个完整的 SoundBank](https://www.audiokinetic.com/library/edge/?source=SDK&id=sdk_bank_training.html#sdk_bank_training_Method_2) 章节。

#### 有关此方法的补充说明

下表列举了“多个完整的”SoundBank 方法的优点和缺点。

| 优点 | 缺点 |
| --- | --- |
| 需要的内存可能比 All-in-one SoundBank 少很多。  非常易于集成到游戏中。 | 不太适合在线游戏或基于 Event 的游戏，在这些游戏中，音频或振动需求不仅仅由主人公的位置等简单因素来驱动。  因为 SoundBank 可能包含重复的数据，所以可能导致内存中重复加载某些媒体文件。  因为不同的 SoundBank 可能包含类似的内容，所以可能导致 SoundBank 的总体磁盘占用空间增大。 |

---