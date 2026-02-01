# 为工程生成 SoundBank

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [管理 SoundBank](00-管理-SoundBank.md) > 为工程生成 SoundBank

## 为工程生成 SoundBank

您可以为要创建的各个游戏平台和语言生成 SoundBank。在开发过程中，随时都可以生成 SoundBank，以便您测试如何将它们集成到各种游戏平台中。为了更加方便，Wwise 还可以同时为所有平台和所有语言生成 SoundBank。

在生成 SoundBank 时，SoundBank 可包含以下任何信息：

- Event 信息
- Sound, music, motion, Property Container, and container information
- 内存媒体的声音、音乐或振动数据
- 零延迟流播放文件的预读数据
- 流播放文件的引用

SoundBank 中包含的信息仅可在同一工程中使用，这意味着 SoundBank 只可与同一工程中生成的其它 SoundBank 一起使用。

如果 SoundBank 包含的 Event 或对象结构已从工程中删除，您则仍可以生成该 SoundBank。这些无效的工程元素在生成过程中将被 Wwise 忽略，不会导致错误或占用额外的空间。建议从 SoundBank 中移除这些无效的 Event 和对象结构以保证工程的完好度。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 当 SoundBank 中的 Event 或对象结构变得无效时，相应的图标会被移除，并且在 SoundBank Editor 的 Add 选项卡上，无效 Event 或对象结构的名称后面将显示“Missing”一词。 |

在生成 SoundBank 前，需要设置一系列选项来确定是否生成内容和头文件、是否可使用 SoundBank 名称、SoundBank 的保存位置、是否要将流播放文件复制到 SoundBank 目录等。您可以在 Wwise 内的两个不同层级配置这些 SoundBank 设置：

- **工程层级** – 配置工程的默认设置。这些设置在 Project Settings（工程设置）对话框中配置。有关如何在工程层级配置 SoundBank 设置的详细信息，请参阅[“定义工程的 SoundBank 设置”一节](../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md "定义工程的 SoundBank 设置")。
- **用户层级** – 配置自定义用户设置以覆盖工程设置。用户设置在 SoundBank User Settings（音频包用户设置）对话框中配置。有关如何配置自定义用户设置的详细信息，请参阅[“配置用户 SoundBank 常规设置”一节](04-配置用户-SoundBank-设置.md#defining_custom_soundbank_settings "配置用户 SoundBank 常规设置")。

**为工程生成 SoundBank 的方法是：**

1. 通过执行以下任一操作切换到 SoundBank 布局：

   - 在菜单栏中，点击 **Layouts** > **SoundBank**。
   - 按 **F7**。

   除此之外，还可依次单击 Views > SoundBank Manager 或使用快捷键 (Shift+B) 来从其他布局打开 SoundBank Manager 的浮动视图。
2. 在 SoundBank Manager 中，选择您要生成的 SoundBank。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 若在 Project Settings 中选中 **Enable Auto-Defined SoundBanks**，将无法选择单个 SoundBank。这是因为 Wwise 会为 User-defined SoundBank 中没有包含的 Event 自动定义 SoundBank。您可以通过同时生成所有 SoundBank 来对此进行准确的评估。 |

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 在 User-Defined SoundBanks、Platforms 和 Languages 窗格中，可通过 Shift+单击、Ctrl+单击或 Ctrl+A 来选择多个条目。在此之后，只需切换与选定条目对应的复选框，就可将同一状态应用于所有选定条目。 |
3. 在 Platform 列表中，选择您要为它生成 SoundBank 的平台。
4. 在 Language 列表中，选择您要为它生成 SoundBank 的语言。
5. 单击 **Generate Checked**（生成选中项）开始生成 SoundBank（音频包）。

   此时将打开 Generating SoundBank 对话框，您可以在此查看 SoundBank 生成过程的进度。在生成这些 SoundBank 后，会打开 Generating SoundBanks - Completed 对话框。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 先前生成的并且没有更改的 SoundBank 不会再生成。在这种情况下，**Results** 面板的 **Created** 列中将显示“Up to date”。 |
6. 仔细查看对话框中的消息，确保已成功生成所有 SoundBank（音频包）。这当中包括查看 Log（日志）窗格中的条目。日志中完整列出了各项错误、警告以及其他与生成过程相关的信息。在大部分情况下，这些消息都包含解决步骤。您也可以在 Logs（日志）视图的 [“SoundBank Generation 选项卡”一节](../../09-参考主题/02-视图/03-Logs-视图/00-Logs-视图.md#soundbank_generation_log "SoundBank Generation 选项卡")中查看日志。

   若要自定义日志，请参阅[“管理在日志中出现的消息”一节](../../03-设置工程/01-处理工程/02-定义工程设置/04-管理在日志中出现的消息.md "管理在日志中出现的消息")。
7. 关闭 Generating SoundBanks - Completed（生成音频包 - 已完成）对话框。

   SoundBank 文件位于您指定的文件夹中，现在可以集成到您的游戏中了。

### 监控 SoundBank 的详细信息

由于遵循各个平台的内存限制很关键，因此能够管理工程中的各个 SoundBank 和对它们进行故障排查非常重要。您需要确定哪些 SoundBank 超出了最大体积、哪些语言文件缺失了、生成的 SoundBank 的总大小以及高效管理 SoundBank 所需要的其它重要信息。

Wwise 将在 SoundBank Editor 的 Detail 选项卡中显示这些详情。

![](../../../../images/SB_Details_Pane.png)

如果您的 SoundBank 包含 Sound Voice 对象，则 Detail 选项卡上的信息将按照语言进行组织。Wwise 还会以红色显示一些信息，帮助您迅速找出潜在问题。

|  |  |
| --- | --- |
| [备注] | 备注 |
| SoundBank Manager 和 SoundBank Editor 中的所有内存信息均以字节为单位。 |

**监视 SoundBank 的详情的方法是：**

1. 在 SoundBank Manager 中，双击想要查看详细信息的 SoundBank。

   相关信息会显示在 SoundBank Editor 的 Details 选项卡中。
2. 请查看 Detail 选项卡的内容了解有关下列内容的信息：

   - **Type** -- 类型。SoundBank 中包含的对象类型，例如音效、声部、音乐和振动。
   - **Language** -- 语言。相应 SoundBank 的语言。
   - **SFX** -- 音效。音效声对象占用的内存量。
   - **Music** -- 音乐。音乐对象占用的内存量。
   - **Voice** -- 声部。特定语言的 Sound Voice 对象占用的内存量。
   - **Data Size** -- 数据大小。特定语言的音效、语音和振动对象占用的总内存量。
   - **Free Space** -- 空闲空间。SoundBank 中的剩余空间。只有指定最大体积时才会显示此值。
   - **Missing Files** -- 缺失文件。特定语言缺失的媒体文件数量。
   - **Files Replaced** -- 被替换文件。当前被参考语言的音频文件所替换的、缺失的 Sound Voice 音频文件的数量。
   - **Memory Size** -- 内存大小。将加载到内存中的 SoundBank 数据所占用的空间量。
   - **Prefetch Size** -- 预读大小。流播放文件的预读数据所占用的空间量。该部分数据通过 SoundBank 加载到内存中，以确保流媒体文件零延迟播放。
   - **File Size** -- 文件大小。生成的 SoundBank 文件的总大小。

### 使用脚本生成 SoundBank

若打算定期生成 SoundBank（音频包），可创建脚本来自动执行生成过程。为了做到这一点，您可以使用 Wwise SDK 从命令行来生成多个 SoundBank。有关此功能的完整描述，请参阅 Wwise SDK 文档中的 [Wwise SDK >深入探索 >通过命令行生成 SoundBank](https://www.audiokinetic.com/library/?source=SDK&id=bankscommandline.html) 章节。

---