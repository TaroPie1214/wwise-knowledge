# 了解 Virtual Voice

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

了解 Virtual Voice

为了在同时播放大量声音时保持最佳性能，可使用 Virtual Voice 来确保低于特定音量的声音不会占用宝贵的处理资源和内存。声音引擎会将听不到的声音放入 Virtual Voice 列表而不进行播放。Wwise 会持续管理并监控这些声音。不过只要其在 Virtual Voice 列表中，声音引擎就不会对其进行处理，因而不会占用硬件的 Physical Voice。

在使用 Virtual Voice 功能时，声音会根据以下情形在 Physical Voice 和 Virtual Voice 之间来回切换：音量电平是否低于阈值、是否超出播放限值、是否允许将声音转为 Virtual Voice（如 [了解播放限值和播放优先级](concept_advanced_settings.html) 中所述）。在声音达到 Wwise 设计工具中设定的阈值时，系统会将其添加到 Virtual Voice 列表并停止声音处理。在对象移动到最大距离半径之内且音量电平升高时，会将声音从 Virtual Voice 列表中移出并转为 Physical Voice。这时声音引擎会重新开始对声音进行处理。

在声音由 Virtual Voice 转为 Physical Voice 时，可为其选择三种不同的播放行为。每种行为都有自己的性能特点：

|  |  |  |
| --- | --- | --- |
| **On Return to Physical Voice** | **CPU cost** | Memory cost |
| Play from beginning | 中：在转为 Virtual Voice 时不对声音进行处理。在 Virtual Voice 和 Physical Voice 之间切换时，会执行一些额外的操作。 | 低：在转为 Virtual Voice 时清空所有内部处理缓冲区。 |
| Play from elapsed time | 高：在转为 Virtual Voice 时在各个缓冲区对声音进行处理。在 Virtual Voice 和 Physical Voice 之间切换时，会执行一些额外的操作。 | 低：在转为 Virtual Voice 时清空所有内部处理缓冲区。 |
| Resume | 低：在转为 Virtual Voice 时不对声音进行处理。在 Virtual Voice 和 Physical Voice 之间切换时，不会对声音执行任何操作。 | 高：在转为 Virtual Voice 时保留所有内部处理缓冲区。 |

流播放声音在转为 Virtual Voice 时不会占用 I/O 带宽。在选择 **Play from beginning** 或 **Play from elapsed time** 时，会清空 I/O 缓冲区。这会导致在由 Virtual Voice 转为 Physical Voice 时再次听到声音前有一定延迟。

如需详细了解声音设计师如何看待 Virtual Voice，请参阅[优化声部](https://www.audiokinetic.com/library/edge/?source=Help&id=optimizing_cpu#optimizing_cpu_voices)。