# 了解 SoundBank

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

了解 SoundBank

SoundBank 是包含游戏音频数据的文件。这些文件可由声音设计师在 Wwise 设计工具中借助 SoundBank Manager 来生成。除此之外，也可通过自动化流程定义和生成。

有两种类型的 SoundBank：

- **初始化 SoundBank**：这种 SoundBank 包含工程的所有通用信息。比如，有关控制总线层级结构、State、Switch 和 RTPC 的信息。初始化 Bank是在 Wwise 生成 SoundBank 时自动生成的。每个工程只有一个名为 `Init.bnk` 的初始化 SoundBank。
- **普通 SoundBank**：这种 SoundBank 包含在游戏中播放声音所需的 Event 数据。它又分为 Auto-defined SoundBank 和 User-defined SoundBank。两者可单独使用，也可结合使用。这些 SoundBank 会对内存用量、文件打包、文件大小和 SoundBank 加载方式产生不同的影响。
  - **Auto-defined SoundBank**：Auto-defined SoundBank 由系统自动创建。系统会为未包含在 User-defined SoundBank 中的 Event 和 Auxiliary Bus 创建单独的 SoundBank。各个 SoundBank 只包含 Event 和结构信息。媒体存储在 SoundBank 之外。因此，若多个 Event 使用同一媒体素材，则只在磁盘上生成并加载一次该素材。Auto-defined SoundBank 不需要 Wwise 用户怎么管理，并且可将文件大小减到最小。
  - **User-defined SoundBank**：User-defined SoundBank 包含多个 Event 以及用来播放这些 Event 所需的全部对象和音频数据。声音设计师可在 Wwise 设计工具中创建任意数量的 SoundBank 并为其添加 Event、结构和媒体。另外，还可通过导入 SoundBank 定义文件来在 Wwise 设计工具中创建 User-defined SoundBank。这些定义文件可由游戏关卡编辑器等外部程序自动创建。When user-defined SoundBanks are generated, Wwise packages all the Containers, Sounds, and so on that are used by the Events contained within each SoundBank. 若 SoundBank 中的有些声音为语音，则会为 Wwise 工程支持的各种语言生成不同版本的 SoundBank。

您的游戏必须首先加载初始化 Bank。然后，便可根据需要加载和卸载 SoundBank。

- 如需详细了解声音设计师如何看待 SoundBank，请参阅[为工程定义 SoundBank 设置](https://www.audiokinetic.com/library/edge/?source=Help&id=defining_soundbank_settings_for_project)和[管理 SoundBank](https://www.audiokinetic.com/library/edge/?source=Help&id=managing_soundbanks)。
- 如需简要了解 SoundBank 在 Wwise 声音引擎集成中的作用，请参阅 [SoundBank 集成示例](quickstart_sample_integration_banks.html#soundengine_integration_banks) 章节。有关更多详细信息，请参阅 [集成详情—— SoundBank](soundengine_banks.html) 章节。
- 有关如何通过 API 生成 SoundBank 的信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。具体来说，必须使用 [Wwise Authoring API Reference](waapi_index.html) 调用 `ak.wwise.ui.commands.execute` 命令并向其传递相应的 [Wwise 设计工具命令标识符](globalcommandsids.html) 标识符（如 `GenerateSelectedSoundbanksCurrentPlatform` ）。