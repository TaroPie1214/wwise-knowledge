# What&#39;s New in 2014.1.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2014.1.1

2014.1.1 属于补丁包。下面各节列举并描述 Wwise 版本 2014.1 与版本 2014.1.1 之间的变化。

# 平台 SDK 的变化

- Windows Phone：添加了对 Windows Phone 8.1（作为 WinPhone\_vc120）的支持

# 新增功能

- **WG-18790** Advanced Profiler 现在可以显示通过内存指针加载的 SoundBank 的内存占用。
- **WG-25835** Center% 属性现在可通过 RTPC 控制。
- **WG-25932** Auro Panner：添加了对 Dolby 声道配置的支持。
- **WG-26040** IOSONO 现在可用于 PS4 和 Xbox One。
- **WG-26227** 移除了 Mac 中的声道限制。

# 性能改进

- **WG-26022** 优化了 Wwise Synth One：最高比 2014.1 快 4 倍。
- **WG-26060** 提高了 StopAll 动作的性能。
- **WG-26192**（Xbox One）提高了 XMA 解码器同步机制。

# 漏洞修复

- **WG-24782** 已解决：（Xbox One）带 LFE 的多声道 XMA 文件在其它声道中存在滤波问题。
- **WG-24841** 已解决：当对音乐切换容器使用 None 状态时，捕获日志中显示“Wrong Argument Value”。
- **WG-25444** 已解决：在加载包含名称冲突的工程后发生复制/粘贴问题。
- **WG-25460** 已解决：当不选择向下折叠复选框时，Auro Panner 不会恢复默认设置。
- **WG-25863** 已解决：（Windows RT）Wwise 未对插入平板电脑的耳机做出反应。
- **WG-25997** 已解决：当单击 Effect 按钮时，WwiseLib.dll!CProp ~CProp() 崩溃。
- **WG-26003** 已解决：WMusicTransitionAware::FixChildrenReferences 崩溃。
- **WG-26007** 已解决：加载工程时 WEventAction::ChangeAction 崩溃。
- **WG-26016** 已解决：内存不足时，Auro 插件发生各种崩溃。
- **WG-26023** 已解决：在预读和淡入时，流播放音乐文件上发生源匮乏。
- **WG-26028** 已解决：IOSONO Proximity 声道在每个声音的第一帧期间淡入。
- **WG-26053** 已解决：（WiiU）在 Wii-mote 上播放音频时崩溃。
- **WG-26058** 已解决：在为 Linux 和 Windows Phone 平台创建文件包时，文件打包程序使用错误的字节顺序。
- **WG-26096** 已解决：如果定位选项由 2D/3D RTPC 驱动，则衰减不会显示在“Shared by”列表中。
- **WG-26120** 已解决：在互动音乐中，HandleTrigger() 很少崩溃。
- **WG-26133** 已解决：在连接到游戏时内存不足会导致崩溃/死机。
- **WG-26143** 已解决：PS3 中流管理器存在竞争危害（2014.1 的回归）。
- **WG-26146** 已解决：声笼和声障内置参数颠倒。
- **WG-26147** 已解决：音频输出设备断开时播放时间不准确。
- **WG-26151** 已解决：对于不兼容的对象类型，使用制表符隔离的值导入功能将导致崩溃。
- **WG-26158** 已解决：当游戏对象名称长于 128 个字符时，Wwise 连接将崩溃。
- **WG-26160** 已解决：如果在游戏对象损坏时参数正在过渡，则 AkRTPCMgr 将崩溃。
- **WG-26163** 已解决：当音频从中断中恢复时，(iOS) AAC 声音将发生卡顿。
- **WG-26171** 已解决：设置为 MIDI 目标的切换容器不执行切换。
- **WG-26193** 已解决：归一化游戏对象朝向向量的 [AK::SoundEngine::SetPosition()](namespace_a_k_1_1_sound_engine_a789e25bda32d1e11849afb6584942455.html#a789e25bda32d1e11849afb6584942455) 要求没有对应文档。
- **WG-26199** 已解决：使用针对非总线对象的 Set Bus Volume 动作打开工程时崩溃。
- **WG-26202** 已解决：在少数情况下，总线上的声部音量 RTPC 计算不正确。
- **WG-26205** 已解决：（PS4）在 Release 配置中使用 PAD 输出时可能死机。
- **WG-26226** 已解决：RemoveFileExtension()（针对 SoundBank 和文件包名称散列）从字符串开头而不是结尾搜索点。
- **WG-26243** 已解决：（Vita，PS4）ATRAC-9 播放中存在各种断言。
- **WG-26257** 已解决：在播放期间修改 3D 用户定义声音中的路径时发生崩溃或内存泄漏。
- **WG-26262** 已解决：每次值变化时，控制切换开关的游戏参数都会触发 None 切换开关。
- **WG-26280** 已解决：删除音乐容器时，Wwise Authoring 崩溃。
- **WG-26292** 已解决：从 2014.1 beta 1 迁移后，AudioFilesManager::InvalidateAllConvertedFileIDs() 崩溃。
- **WG-26300** 已解决：对于某些特定角度，IAkMixerPluginContext::ComputeSphericalVBAPGains() 服务返回无效增益。