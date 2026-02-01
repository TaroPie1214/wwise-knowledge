# 集成详情—— SoundBank

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

集成详情—— SoundBank

SoundBank（声音包）是由 Wwise 生成的文件，里面包括了事件、声音结构或媒体，这些内容会在游戏中特定时刻加载到游戏平台的内存中。

- 想了解使用 Wwise 来生成包的更多信息，请参阅 [Wwise Help](https://www.audiokinetic.com/library/edge/?source=Help&id=generating_soundbanks_for_project)。

  |  |  |
  | --- | --- |
  |  | **备注:** 您也可能会想参考 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节来了解如何使用 Wwise 的全套设计工具 API。该 API 已取代原来用于构建 SoundBank 的 SoundFrame 系统。为了使用 WAAPI 来生成包，您需要学习使用 [Wwise Authoring API Reference](waapi_index.html) 来调用 `ak.wwise.ui.commands.execute` 命令，并向其传递合适的 [Wwise 设计工具命令标识符](globalcommandsids.html) “标识”，如 `GenerateSelectedSoundbanksCurrentPlatform` 。 |
- 有关 SoundBank、如何在游戏中引用 SoundBank 及 SoundBank I/O 概念的基本信息，请参阅 [一般信息](soundengine_banks_general.html) 章节。
- 有关 SoundBank 加载 API 的详细信息，请参阅 [加载 SoundBank](soundengine_banks_loading.html) 章节。
- 有关如何集成 SoundBank 的详细示例，请参阅 [SoundBank 集成示例](sdk_bank_training.html) 章节。

参见
:   - [了解 SoundBank](concept_banks.html)
    - [SoundBank 集成示例](sdk_bank_training.html)