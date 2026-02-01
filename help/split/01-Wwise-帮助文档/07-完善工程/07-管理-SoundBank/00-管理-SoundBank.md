# 管理 SoundBank

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > 管理 SoundBank

## 管理 SoundBank

为了高效地管理游戏的音频或振动组件，Wwise 将游戏的所有音频和振动都放到 SoundBank 中。SoundBank 其实就是一个包含音频或振动数据、媒体或两者兼有的文件。这些 SoundBank 在游戏的特定时刻加载到游戏所在平台的内存中。通过仅加载必要的内容，您可以优化每个平台上媒体文件占用的内存大小。SoundBank 是您所有工作的成果，这些成果包含的最终内容会成为游戏的一部分。

Wwise 中有两类 Bank：

- **Initialization (Init) bank** -- 初始化库。一种特殊库，其中包含有关工程的所有通用信息，包括有关总线层级结构、状态、切换开关和 RTPC 的信息。如果条件具备，则它还可能包括音频设备 ShareSet。

  每次 Wwise 生成 SoundBank 时都会自动生成 "Init" SoundBank。Initialization Bank 通常在游戏开始时加载，以便在游戏期间可以轻松获得工程的所有通用信息。在启动游戏时，必须先加载该 SoundBank；否则，可能无法加载其他 SoundBank/内容。"Init" SoundBank 的文件名为 Init.bnk。
- **SoundBank** —— 此文件中同时包含事件数据、声音、音乐和振动结构数据或音频文件。与 Initialization Bank 不同，SoundBank 一般在游戏的不同时间加载和卸载，以提高平台内存的利用率。

由于所有平台各不相同，因此 Wwise 让您能轻松地针对各个平台定制 SoundBank，并同时为所有平台生成 SoundBank。Wwise 还为您提供故障排查工具，用来排查与 SoundBank 相关的任何问题，确保您遵守不同平台的限制。

每款游戏只能使用一个 Wwise 工程。如果您有多人同时处理一个大型工程，则可以将工程划分为多个独立的工作单元。有关使用工作单元的信息，请参阅[“将工程分成 Work Units”一节](../../03-设置工程/04-Working-with-a-team/01-将工程分成-Work-Units.md "将工程分成 Work Units")。

## Wwise 中的 SoundBank 视图

为了帮助您提高工作效率，Wwise 提供了 SoundBank 布局。此布局包含为工程创建、管理和生成 SoundBank 所需的全部视图，包括 Project Explorer、Event Viewer、SoundBank Manager、SoundBank Editor 以及 Property Editor 或 Event Editor（因所选对象类型而异）。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在 Wwise 中，默认情况下您可以按 **F7** 切换到 SoundBank 布局。 |

  

在 SoundBank Editor 中，可通过将不同的 Event、音效、音乐、振动 (motion) 结构和音频文件添加到 SoundBank 来构建 SoundBank。您可以通过在 Project Explorer 或 SoundBank Manager 中选中 SoundBank 来打开 SoundBank Editor。

SoundBank Editor 包括以下四个选项卡：

- **Add** - 仅显示实际添加到 SoundBank 中的事件、对象层次结构、工作单元和文件夹。自动添加到 SoundBank 中的相应子对象将只显示在 Edit（编辑）选项卡中。在 Add（添加）选项卡中，用户还可以决定各个层级结构元素中那些素信息或媒体类型将包含在 SoundBank 中。
- **Add** —— 只显示已添加到 SoundBank 的实际事件、对象层级结构、工作单元和文件夹。在此选项卡上，您可以从 SoundBank 中弃用掉特定的 Game Sync。如果弃用了 Game Sync 的话，您则也弃用了与 Game Sync 相关的声音结构和媒体文件。
- **Game Sync** —— 显示与 Add 选项卡中所包含的事件和声音结构相关的状态、切换开关和触发器的列表。SoundBank 中媒体文件的其它信息也会显示出来，包括采样率、音频格式和文件大小。通过掌握这些附加信息，您可以轻松地微调各个文件的转码设置，以遵守特定平台的限制。用户可以根据语言和对象类型来对列表进行筛选，并将需要从 SoundBank 中弃用的任何工程元素取消选择。
- **Details**（详细信息）– 显示与选定 SoundBank 中不同元素的大小相关的详细信息，并报告所有可能缺失或已被替换的文件。

![](../../../images/SB_SoundBank_Editor.png)

在工程开发期间，您可以随时从 SoundBank Manager 中生成 SoundBank。SoundBank Manager 中会列出 User-defined SoundBank 和 Auto-defined SoundBank。每个列表都包含有关各个 SoundBank 的类型和大小的一些基本信息。另外，SoundBank Manager 中还包含单独的平台和语言列表。在做出选择后，将决定要生成哪些 SoundBank。

![](../../../images/sbm_sound_bank_manager.png)

**相关主题**

- [Wwise Fundamentals Module 18: Working with Multiple
  SoundBanks](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=working_with_multiple_soundbanks)
- [Wwise Fundamentals Module 19: Managing SoundBank size](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=managing_memory)

---