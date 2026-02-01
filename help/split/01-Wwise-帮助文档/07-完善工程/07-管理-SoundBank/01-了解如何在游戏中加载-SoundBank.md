# 了解如何在游戏中加载 SoundBank

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [管理 SoundBank](00-管理-SoundBank.md) > 了解如何在游戏中加载 SoundBank

## 了解如何在游戏中加载 SoundBank

在学习如何在 Wwise 中创建、填充和生成 SoundBank 之前，要先了解游戏加载和管理 SoundBank 信息的不同方式。最佳方式取决于各种不同的因素，包括开发的游戏类型、运行游戏的平台以及项目团队设定的限制。

为了提高灵活性和满足几乎所有游戏类型的需求，Wwise 提供了多种将音频和振动加载到游戏中的方法，包括以下几种：

- [“加载整个 SoundBank”一节](01-了解如何在游戏中加载-SoundBank.md#loading_bank "加载整个 SoundBank")
- [“Prepare SoundBank（全部内容）”一节](01-了解如何在游戏中加载-SoundBank.md#preparing_bank_all_content "Prepare SoundBank（全部内容）")
- [“Prepare 动作事件”一节](01-了解如何在游戏中加载-SoundBank.md#preparing_action_events "Prepare 动作事件")

### 加载整个 SoundBank

加载 SoundBank 的传统方法使用同时包含事件数据、对象结构数据和媒体的 SoundBank。这些 SoundBank 的全部内容在游戏的特定时刻加载和卸载，确保事件数据和相关媒体在被触发时就可以播放。

下图演示在游戏中使用传统方法创建的 SoundBank 如何在玩家从 1 级升级到 2 级时加载到平台内存和从平台内存中卸载。

|  |
| --- |
|  |

由于特定 SoundBank 的所有数据和媒体同时加载到内存中，因此这种方法不仅确保所有数据和媒体可以在需要时播放，而且在游戏中需要执行极少的磁盘寻址，从而将磁盘腾出来执行对磁盘需求较大的其它任务。

此方法的主要缺点是在 SoundBank 的整个加载期间将占用大量的内存，使您无法灵活地处理复杂的大型游戏。此方法还显式加载 SoundBank 中的所有内容，而不验证媒体文件是否已经加载到内存。这可能会导致同一媒体文件被多次加载到内存中。尽管此传统方法有上述缺点，但是在许多情况下仍非常有用。例如，用于所有数据和媒体必须随时可用的经典弹珠游戏。

### Prepare SoundBank（全部内容）

为了克服 LoadBank() 机制的一些缺点，您可以先采用 Prepare 操作来"预备" SoundBank 而不是使用 AkBankContent\_All() 加载它们（译注：为了突出 Prepare 是一种 API 调用，文档尽量用英语原文来代表这种预备操作，而不做通篇翻译）。在使用此方法时，SoundBank（音频包）仍可包含所有内容类型（Event、结构数据和媒体文件）；不过，此方法不会立即加载媒体文件，而是借助 PrepareEvent() 机制将所有媒体加载到内存中。通过使用此机制加载媒体，Wwise 首先查看媒体文件是否已经存在内存中，然后再加载它。这可以避免内存中出现媒体文件重复，从而将内存占用保持在最低水平。

除了可以节省内存外，此方法还可以保证顺序访问磁盘，这将避免在使用 PrepareEvent() 中一次 Prepare 一个 Event 时可能发生的随机磁盘寻址。

下图演示了"Prepare Bank（All Content）"（预备 SoundBank（全部内容））机制如何将元数据和内容加载到平台内存中。

|  |
| --- |
|  |

在加载包含 [Vorbis](../../14-词汇表.md#glossary_vorbis "Vorbis") 编码或 [WEM Opus](../../14-词汇表.md#glossary_opus "Opus") 编码媒体的 SoundBank 时，可利用  [Preparation\_LoadAndDecode](https://www.audiokinetic.com/library/?source=SDK&id=namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html) 预备类型将这些媒体文件解码为非压缩 [PCM](../../14-词汇表.md#glossary_pcm "PCM（脉冲编码调制）") 文件。这会使 SoundBank 体积变大，但当事件调用媒体文件时，将立即播放而无需进行解码。

### Prepare 动作事件

The PrepareEvent() method dynamically loads media when it is required. To use method, the
Action Event metadata must be in a loaded SoundBank and the associated media files
must be accessible in the file system. The corresponding structure metadata can be
included in the same SoundBank as Events or placed in a separate SoundBank, either
user-defined or auto-defined. It can therefore simplify Event and SoundBank
management because you can prepare multiple Events without the need to remember
which SoundBanks contain the necessary media: the Wwise sound engine automatically
retrieves the required files, wherever they are.

This method ensures that after a PostEvent call, the Action Event audio is played
immediately (on the same frame) because there is no need to load the media. However,
it uses more memory than other methods because the media and metadata are loaded and
remain in memory.

|  |  |
| --- | --- |
| [备注] | 备注 |
| - 只有动作 Event 可事先 Prepare。"PrepareEvent()"方法不适用于对话事件。 - Avoid using PrepareEvent() when working with the Wwise Unreal   Integration. Unreal embeds media files in their respective events or   Asset Libraries, so PrepareEvent() would not be able to function   correctly. - Streamed audio that does not have a prefetch buffer cannot be prepared   because the audio is played directly from storage. |

To use this method, call the LoadBank() method to load the SoundBank that contains the
Action Event metadata and keeps it in memory. When PrepareEvent() is called, the
sound engine then "prepares" the Action Events before the game calls PostEvent(). To
prepare an Event, the sound engine loads all non-streaming, referenced media files
from the file system and all referenced structure metadata from a SoundBank, if it
is not already loaded. When the Action Event is no longer required, unload it with
Preparation\_Unload so the corresponding media files are purged from memory.

下图说明如何事先 Preapre Event，以便只将必需的媒体文件加载到内存中。

|  |
| --- |
|  |

When the metadata (also referred to as structure data) is not stored in the same SoundBank as the Events, Wwise includes references to the corresponding content stored in other SoundBanks. Wwise 可以使用名称或 ID 来引用其它 SoundBank。若要在声音引擎中使用 SoundBank 名称，则须在 Project Settings（工程设置）对话框的 SoundBanks（音频包）选项卡中选中 **Use SoundBank Names**（使用音频包名称）选项。To use IDs, clear the option. For more information, see [“SoundBanks 选项卡”一节](../../09-参考主题/01-工程/08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡").

Media that a SoundBank references must be stored as loose files on disk or be resolvable by
the low-level IO (such as in a File Package).

This method uses memory efficiently but performs more disk seeking than other methods,
which might not be appropriate in situations when many files are already being
streamed from the disk. Also, if the game uses States and Switches, media files
could be loaded into memory unnecessarily. For example, if there are different
sounds for the different moods or energy levels of a crowd in your game, they are
all loaded into memory even if only some of the Switch sounds are valid within a
particular zone of the game. To avoid this problem, you can prepare specific States
or Switches that only load the media files associated with the prepared States or
Switches.

The following illustration shows how you can prepare Switches in advance to limit the
amount of media that is loaded into memory at any particular point in the
game.

|  |
| --- |
|  |

虽然提前 Prepare Game Sync 可以优化内存占用，但注意，这也会降低媒体加载到内存中的速度。Read times are longer when the sound engine needs to search the disk to find the sounds that correspond to the prepared game syncs.

By dynamically loading only the required audio files, The second method provides
flexibility to handle situations where you have either large zones or levels with
many sounds, or limited amounts of memory available to store Event data, structure
data, and media.

|  |  |
| --- | --- |
| [备注] | 备注 |
| [LoadBank](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a496b9917fe035f301bcff0accd61f80f.html)、[AkBankContent\_All](https://www.audiokinetic.com/library/?source=SDK&id=namespace_a_k_1_1_sound_engine_ae775cb922db262649dbbaa3fa8117d83.html)、[PrepareEvent](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a98b617d05618e6d18680d198845ff3d7.html)、[PrepareGameSyncs](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ad5fc8ab51eecee6511d5c61b03659fa4.html) 和 [AkBankContent\_StructureOnly](https://www.audiokinetic.com/library/?source=SDK&id=namespace_a_k_1_1_sound_engine_ae775cb922db262649dbbaa3fa8117d83.html) 函数均可通过 Wwise API 访问。For more information on loading SoundBanks and preparing Events and game syncs, see the [Integrating Banks](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__banks.html) section of the Wwise SDK. |

For a detailed overview of the different methods you can use to manage your SoundBanks, see
[“SoundBank 管理策略”一节](02-SoundBank-管理策略/00-SoundBank-管理策略.md "SoundBank 管理策略").

---