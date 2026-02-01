# SoundBank 相关技巧和窍门

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > SoundBank 相关技巧和窍门

## SoundBank 相关技巧和窍门

在定义 SoundBank（音频包）的内容前，最好仔细查看以下章节。您可以参照其中的技巧和窍门来更好地管理游戏中的 SoundBank。

### 更新 Initialization Bank

每次生成若干个 SoundBank 时，Wwise 会根据需要更新初始化库。这样做时为了确保两套声音包同步。初始化库包含有关工程的所有通用信息（包括有关总线层级结构的信息）以及有关状态、切换开关和 RTPC 的信息。如果更改工程中的任何这些元素，Wwise 则将随着新生成的 SoundBank 为您的游戏更新此声音包。然而，如果没有更改这些工程元素，Wwise 则将不会生成 Init.bnk 的新版本。

**Initialization Bank** —— 一种特殊库，其中包含有关工程的所有通用信息（包括有关总线层级结构的信息）以及有关状态、切换开关、RTPC 和环境效果器的信息。每次 Wwise 生成 SoundBank 时都会自动生成 "Init" SoundBank。Initialization Bank 通常在游戏开始时加载，以便在游戏期间可以轻松获得工程的所有通用信息。在启动游戏时，必须先加载该 SoundBank；否则，可能无法加载其他 SoundBank。在默认情况下，Initialization Bank 命名为“Init.bnk”。

### SoundBank 和内存

若在 SoundBank 中包含长的声音，其可能会占用平台的大量内存。为避免占用过多内存，请尝试对长的声音或音乐文件进行流播放。详情参阅[“对声音采用流播放”一节](../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/05-对象播放相关的技巧和经验总结.md#streaming_sounds "对声音采用流播放")和/或[“流播放音乐”一节](../../../06-创建互动音乐/04-使用-Music-Track-和-Music-Segment/01-定义-Music-Track-的播放行为.md#streaming_music "流播放音乐")。

### 将常用元素分组存放到 SoundBank 中

将通用元素全部集中到一个 SoundBank 中是一个好方法。比如，可将所有在游戏当中保持加载状态的元素（如菜单、主角等）分组存放到同一 SoundBank 中。对于游戏当中不断加载和卸载的元素，可分组存放到逻辑单元或构成模块中，以便于在游戏当中根据需要进行调换。

### 使用 Work Unit 和文件夹

为避免每次更改工程时必须编辑 SoundBank，您可以使用文件夹和／或工作单元重新创建设置 SoundBank 的方式。由于 Wwise 在 SoundBank 元素与工程元素之间保持着有效的链接，因此这些文件夹一旦添加到 SoundBank，您就无需再编辑这些 SoundBank了，它们会自动更新。

### 在 SoundBank 中使用 Event ID

在工程的最后阶段，使用 Event ID 而不是 Event 字符串是一个好办法，因为在继续进行前，声音引擎无需对名称执行哈希算法，Event ID 验证起来会更快。

### 生成 Integrity Report

在生成 SoundBank 前生成完好度报告（Integrity Report）是一个好主意。完好度报告能展示工程中的错误列表，以及可能的解决方法。通过在生成 SoundBank 前解决所有工程错误，您可以尽可能地减少游戏中的音频或振动问题。

### 在 SoundBank Editor 中使用多选功能

如果正在使用 SoundBank Editor 的 Add 选项卡，并且需要为多个条目弃用同一类型的工程元素，则您可以在 Hierarchy Inclusion 列表中选择多项，然后取消勾选其中一个复选框。这将为所有选定项弃用该类型。您还可以使用多选功能为多个项来添加类型。

### SoundBank 名称限制

要规避平台文件系统对文件名的限制，可以将 SoundBank 打成文件包。文件包是个独立的单元。它将平台的文件系统完全分离了出来，消除了系统可能对文件名施加的限制。

### SoundBank 版本控制

您可以通过多种方式来使用版本控制系统管理工程中生成的文件（SoundBank 和媒体文件）和文件夹。

- 使用版本控制应用程序来手动更新版本控制状态。
- 在 SoundBank Settings（音频包设置）中添加生成前和生成后步骤来更新版本控制状态。有关详细信息，请参阅[“SoundBanks Settings — SoundBanks 选项卡”一节](../../../09-参考主题/02-视图/09-SoundBank-Manager-视图/01-SoundBanks-Settings-对话框/01-SoundBanks-Settings-—-SoundBanks-选项卡.md "SoundBanks Settings — SoundBanks 选项卡")。
- 在 SoundBank Settings 中启用 **Use Source Control for Generated Files**（针对生成的文件使用版本控制）选项，以通过配置 Wwise 来自动更新工程中所生成文件的版本控制状态。要了解详细信息，请参阅[“SoundBanks Settings — SoundBanks 选项卡”一节](../../../09-参考主题/02-视图/09-SoundBank-Manager-视图/01-SoundBanks-Settings-对话框/01-SoundBanks-Settings-—-SoundBanks-选项卡.md "SoundBanks Settings — SoundBanks 选项卡")。

无论针对所生成文件如何配置版本控制系统，都请考虑启用以下版本控制选项（如有）：

- **Make files writable**（将文件设为可写状态）：通常，版本控制系统会将处于控制下的文件/文件夹设为只读状态来将其锁定。在将其设为可写状态后，团队成员便可在本地机器上禁用版本控制，并在不更改文件权限的情况下生成 SoundBank。
- **Preserve timestamps**（保留时间戳）：在启用此选项时，会在版本控制同步的过程中保留文件时间戳。这样可在生成 SoundBank 时略微提升 Wwise 的性能。

---