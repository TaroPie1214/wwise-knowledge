# Prepare 动作事件

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > [SoundBank 管理策略](00-SoundBank-管理策略.md) > Prepare 动作事件

### Prepare 动作事件

此方法适用于以下情形：

- 需要将媒体设为很高的粒度级别以保持较低的内存用量。
- 不用为管理哪些媒体素材必须指派给哪个 SoundBank 而烦恼。

什么叫预备 Action Event（动作事件）？在调用 [`PrepareEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a98b617d05618e6d18680d198845ff3d7.html)  函数时，系统会对 Action Event 进行分析，以确保所有与此 Event 相关的结构和媒体均已加载到内存中。否则，系统会自动从磁盘流式传入缺失的信息。在明确撤消以前，Event 一直处于 Prepare 状态。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 只有动作 Event 可事先 Prepare。"PrepareEvent"方法不适用于对话事件。 |

此方法要求创建至少一个 SoundBank，然而结构部件可以位于与 Event 所在的同一个 SoundBank 中，也可处于完全独立的一个 SoundBank 中。

在构建使用 PrepareEvent 机制的 SoundBank 时，条件是至少在一个 SoundBank 中能够找到所需的所有 Event 和结构，而且文件系统必须能够访问这些松散媒体素材。记住，将结构划分到多个 SoundBank 中可以提高内存的管理效率。

在预备 Action Event 之前，Event 本身必须已从某个 SoundBank 加载到内存中（使用 LoadBank()）。由于 Event 中包含在 Prepare Event 时所需的依赖项的信息，因此必须首先加载 Event 所在的 SoundBank。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 另外还可结合 AK::SoundEngine::PrepareBank 来 Prepare Event。使用 PrepareBank 机制的主要优势是无需将 SoundBank 划分为“Event 库”和“媒体库”。在这种方法下，所有内容包含在同一个 SoundBank 中，但是在调用 AK::SoundEngine::PrepareBank 时，只有 SoundBank 的元数据内容加载到内存。当游戏需要媒体时，您可以使用 PrepareEvent 加载媒体。 |

**在 Prepare Event 时在 Wwise 中设置 SoundBank 的方法是：**

1. 创建一个名为"Event"的 SoundBank，并加载到 SoundBank Editor 中。
2. 把工程中的一些动作事件添加到"Events" SoundBank 中，或仅添加事件工作单元。
3. 禁用 **Media** 复选框，只将 **Events** 和 **Structures** 复选框保留为启用状态。在使用 PrepareEvent() 时，媒体不得位于 SoundBank 内，但可以作为松散文件直接从磁盘中加载。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在本例中，所有 Event 和结构包含在一个 SoundBank 中。虽然对于小型工程，这是可以接受的，但您很可能会需要将内容拆分到多个 SoundBank。另外还可以创建独立的"Structures"SoundBank，它无需从 SDK 命令行进行显式加载或 Prepare，因为各个 Event 都包含对需要加载的其它 SoundBank 的引用。 |
4. 生成 SoundBank，并将生成的 SoundBank 文件夹复制到游戏应用程序。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 单个 SoundBank 中包含的结构数据不可在运行时拆分。因此，如果您使用了 AK::SoundEngine::PrepareEvent()，并且需要来自独立 SoundBank 的结构数据，则该 SoundBank 中的所有结构将一次性加载。为此，您可能会想将工程中的结构内容拆分到多个 SoundBank 中，以便最大限度地减少加载到内存中的非必要信息的数量。 |

#### 集成

有关集成的详细信息，请参阅 Wwise SDK 文档中的[预备 Action Event](https://www.audiokinetic.com/library/edge/?source=SDK&id=sdk_bank_training.html#sdk_bank_training_Method_4) 章节。

#### 有关此方法的补充说明

记住，对  [`AK::SoundEngine::PrepareEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a98b617d05618e6d18680d198845ff3d7.html)  的调用必须视为 I/O 函数调用。在上例中，我们使用了阻塞函数。您可以使用 `AK::SoundEngine::PrepareEvent()` 函数的其它重载来实现非阻塞调用，然后用另一个回调来响应加载完成的通知。

下表列出了“预备 Action Event”的优点和缺点。

| 优点 | 缺点 |
| --- | --- |
| 生成 SoundBank 的过程很简单。  媒体的粒度级别很高。  内存占用总体保持在低水平。  过程自动化非常容易。 | 当逐一加载媒体素材时，可能增加磁盘上的读取和寻址次数。  对总体内存占用量的控制力减弱。  使用交互式音乐时将变得复杂。 |

---