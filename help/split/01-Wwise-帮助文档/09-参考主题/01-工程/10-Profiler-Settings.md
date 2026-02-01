# Profiler Settings

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [工程](00-工程.md) > Profiler Settings

## Profiler Settings

Profiler Settings（性能分析器设置）对话框允许指定在捕获过程中 Game Profiler 要捕获哪些类型的信息。如果您选择过多的信息类型，Wwise 的性能则可能会受到影响。通过清除一些选项，您可以获得以下好处：

- 节省网络传输带宽。
- 节省 Wwise 中的内存空间。
- 省略数据计算，从而节省游戏中的 CPU 时间。
- 省略数据处理或显示，从而节省 Wwise 中的 CPU 时间。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在 Profiler Settings 对话框中取消选择某种数据类型时，通常会从 Advanced Profiler 中移除对应的选项卡。不过，Spatial Audio（空间音频）信息并无对应选项卡。事实上，该数据类型所对应的是发送至 [“Game Object 3D Viewer”一节](../06-Profiler-视图/11-Game-Object-3D-Viewer/00-Game-Object-3D-Viewer.md "Game Object 3D Viewer") 的信息。 |

| 界面元素 | 描述 |
| --- | --- |
| CPU Data | CPU 数据。决定 Game Profiler 是否捕获与 CPU 用量有关的信息。其中包括各种插件的 CPU 用量。 |
| Memory Data | 内存数据。决定 Game Profiler 是否捕获与声音引擎的 Memory Manager 中注册的内存类别相关的信息。 |
| Stream Data | 播放流数据。决定 Game Profiler 是否捕获与声音引擎管理的各条播放流有关的信息。 |
| Voices Data | 声部数据。决定 Game Profiler 是否捕获与声音引擎管理的各个声部有关的信息。 |
| Listener Data | 听者数据。决定 Game Profiler 是否捕获与声音引擎管理的各个听者有关的信息。 |
| Obstruction/Occlusion Data | 声障/声笼数据。决定 Game Profiler 是否捕获影响游戏对象的声障、声笼、衍射、透射损失和发声体散布等信息。注意，必须启用该项才能在 [“Game Object 3D Viewer”一节](../06-Profiler-视图/11-Game-Object-3D-Viewer/00-Game-Object-3D-Viewer.md "Game Object 3D Viewer") 中查看散布声锥。 |
| Markers Notification Data | 标记通知数据。确定 Game Profiler 是否捕获音频文件标记和 Music Segment 自定义提示点的相关信息。 |
| SoundBanks | 音频包。决定 Game Profiler 是否捕获与已加载到内存中的 SoundBank 相关的信息。 |
| Loaded Media | 已加载的媒体。决定 Game Profiler 是否捕获与加载到内存中的媒体相关的信息。 |
| Prepared Events and Busses | Determines whether prepared object information is captured, and whether the Prepared Events and Busses tab in the Advanced Profiler is usable. |
| Prepared Game Sync | 预备游戏同步器。决定 Game Profiler 是否捕获与使用 `PrepareGameSyncs` 函数预备的游戏同步器相关的信息。 |
| Interactive Music | 互动音乐。决定 Game Profiler 是否捕获与互动音乐相关的信息，即 Music Playlist Container 回调和音乐对象之间的过渡。 |
| Streaming Device Data | 流播放设备数据。允许捕获来自所有流播放设备的信息并使用 Advanced Profiler 的 Streaming 选项卡。 |
| Meter | 电平表。允许使用信号测量数据来驱动总线和电平表视图中的电平表以及输出峰值和输出 DC 偏置。 |
| Auxiliary Sends Data | 辅助发送数据。决定 Game Profiler 是否捕获与声音引擎管理的各个辅助发送有关的信息。 |
| API Calls | API 调用。决定 Game Profiler 是否捕获 Wwise API 调用。 |
| Game Syncs | 游戏同步器。决定 Game Profiler 是否捕获与 Game Sync 相关的信息并显示在 Game Sync Monitor 中。 |
| Spatial Audio | Spatial Audio。决定 Game Profiler 是否捕获与 Spatial Audio 有关的数据。其中包括发声体、听者、几何构造、房间及关联门户。 |
| Spatial Audio Ray Casting | Spatial Audio 射线投射。决定 Game Profiler 是否捕获与 Spatial Audio 射线投射引擎有关的数据。其中包括反射射线、衍射射线和边缘受体。 |
| Voice Inspector Data | 声部检视器数据。决定 Game Profiler 是否捕获与 Voice Inspector 和 Game Sync Monitor 视图有关的数据。 |
| Audio Object Data | 音频对象数据。决定 Game Profiler 是否捕获与 Audio Object 有关的数据。 |
| **Capture Log** | |
| Maximum File Size (MB) | 最大文件大小 (MB)。指定 Capture Log 可写入的最大文件大小。  最小值：10 MB  最大值：32,000 MB  默认值：2,000 MB |
| Number of sessions kept | 保留会话数。指定将捕获会话保存为 PROF 文件的最大数量。当超出限制数量时，Wwise 会删除最早的捕获会话。 |
| Enable CPU Timeline | 启用 CPU 时间线。在 Advanced Profiler 的 CPU 选项卡中启用 CPU 时间线视图。CPU Timeline 提供详细的 CPU 计时信息（包括跨线程的信息）以便在 Wwise 中深入分析 CPU 活动。注意，该选项仅供高级用户使用。它可以与其他工具一起用来对整个进程的 CPU 活动进行深入的分析，以详细说明为何有些任务比较耗时或者为何没有按时调度相关作业。 |
| Reduce thread heights dynamically | 动态降低线程高度。在启用此选项时，会降低 CPU 时间线中的线程高度以与视图中的当前 CPU 计时区间协调一致（相对于整个性能分析会话中 CPU 计时区间的高度）。您可以在游戏要求 Wwise 在多个线程之间执行操作时启用此选项。这样方便一并查看整个时钟周期内的活动。 |
|  | 应用您对 Game Profiler 设置所做的更改。 |
|  | 取消。关闭 Profiler Settings 对话框而不应用对 Game Profiler 设置所做的任何更改。 |

**相关主题**

- [“指定要捕获的信息类型”一节](../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/01-指定要捕获的信息类型.md "指定要捕获的信息类型")
- [“连接至本地/远程游戏系统”一节](../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")

---