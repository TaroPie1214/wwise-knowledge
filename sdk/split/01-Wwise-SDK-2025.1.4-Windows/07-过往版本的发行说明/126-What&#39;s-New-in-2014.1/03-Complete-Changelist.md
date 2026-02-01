# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

以下各节列举并描述 Wwise 版本 2013.2.9 和版本 2014.1 之间的变化。

# 平台 SDK 更新（2014.1 beta 1）

- **WG-24801** (iOS) 添加了对 ARM64 架构的支持。

# 平台 SDK 更新（2014.1 beta 2）

- **WG-25720** (iOS) 添加了 iOS 8 支持

# 平台 SDK 更新（2014.1 最终版）

- 3DS 已更新至 SDK 7.2.1
- Xbox One XDK 已更新至 2014 年 9 月
- PS4 SDK 已更新至 1.750
- WiiU SDK 已更新至 2.10.12
- iOS SDK 已更新至 8.0

# 新功能（2014.1 beta 1）

请参阅 [新功能](whatsnew_2014_1_new_features.html) 了解更多详情。

- [MIDI](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_MIDI)
- [Music Switch Tracks（音乐切换开关轨）](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Switch_Tracks)
- [Wwise Synth One](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Wwise_Synth_One)
- [LFO 和包络调制器](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Modulators)
- [高通滤波器](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_HPF)
- [新声道配置](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Channel_Configs)
- [混音器插件框架](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Mixer_Plugin)
- [控制设备支持](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Control_Surface)
- [通过用制表符分隔的内容文件来导入波形文件](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_tab_delimited)
- [内置游戏参数](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Builtin_Game_Parameter)
- [所有平台上可用的挂起/后台模式](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Constrained)
- [在 Mac 上使用 Wwise Authoring](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Mac_Authoring)
- [游戏参数插值](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Game_Parameter_Interpolation)
- [新增衰减属性：Focus](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_Focus)
- [SDK 带来增强的声部/总线音量回调（AkSpeakerVolumeMatrixCallbackInfo）和节拍访问](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_SpeakerVolumeCallback)
- **WG-4735** 现在可在 RTPC 坐标图中以线性和对数尺度查看频率属性。
- **WG-20728** 在高级性能分析器中右键单击游戏对象可直接把游戏对象添加到监视列表中。
- **WG-23619** 在 Xbox One 控制器的触发器上支持 Rumble。
- **WG-24268** 添加了当发生源匮乏时调用的回调。
- **WG-24332** 音乐播放列表“循环计数”有可能随机化。
- **WG-24457** SeekOnEvent 现在有了一个可选输入参数：目标播放 ID。
- **WG-24479** DSP 相关内存分配器只有在加载需要它的 SoundBank 时才会被调用。
- **WG-24646** 总线上的节拍数据现在可通过 SDK 获取。
- **WG-24903** Crankcase REV 支持 Xbox 360 控制器。
- **WG-25004** 用于导出 SoundbanksInfo.xml 中 SoundBank GUID 的新选项。
- **WG-25048** 可查询给定播放 ID 的流缓冲量。
- **WG-25089** 可选的 JSON SoundBank 内容文件。
- **WG-25246** WwiseCLI.exe：添加了命令行选项 -verbose 和 -quiet。
- **WG-25274** 在补偿增益上添加了随机化器。
- **WG-25391** 现在可在命令行中指定要生成的包含 SoundBank 名称的文本文件。
- **WG-25418** 查询：新增查询条件“Is Source of Override”。

# 新功能（2014.1 beta 2）

- **WG-25445** 无论 SoundBank 中是否包括 XMA，都在 SoundbanksInfo.xml 中暴露。

# 新功能（2014.1 最终版）

- **WG-25900**（3DS）暴露核心选择
- **WG-25864** 新增的 宏可通过文件系统中的 .txt 文件把 SoundBank 的列表传递给自定义生成步骤（以在生成大量 SoundBank 时避免命令行长度限制）。更新 CopyStreamedFiles 以支持此功能。

# API 变化（2014.1 beta 1）

- **WG-23828** AkSpeakerVolumes 结构体替换成 [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) 或 AK::SpeakerVolumes::MatrixPtr，并附带在名字空间 [AK::SpeakerVolumes](namespace_a_k_1_1_speaker_volumes.html "Multi-channel volume definitions and services.") 中定义的一系列助手函数。影响 [AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html) 和 [AK::SoundEngine::SetListenerSpatialization()](namespace_a_k_1_1_sound_engine_a3e3e9e5335df01fca37f9b3ed518e2bd.html#a3e3e9e5335df01fca37f9b3ed518e2bd)。
- **WG-24628** (iOS) AK::SoundEngine::iOS::Suspend 和 WakeupFromSuspend 现在是 [AK::SoundEngine](namespace_a_k_1_1_sound_engine.html) 名字空间（所有平台）的一部分。
- **WG-24968** 为 Get/SetSpeakerAngles() 添加了“高度层”角度。
- **WG-25210** [AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html) 彻底改变。请参阅 [SDK 带来增强的声部/总线音量回调（AkSpeakerVolumeMatrixCallbackInfo）和节拍访问](whatsnew_2014_1_new_features.html#whatsnew_2014_1_new_feature_SpeakerVolumeCallback) 、AkSpeakerVolumeMatrixCallbackInfo 、AK::SpeakerVolumes 和 [重要的迁移说明 2014.1](whatsnew_2014_1_migration.html) 。
- **WG-25290** 新增函数：SetRandomSeed()。可以在运行时设置随机种子。 – 添加了新的回调函数，以使应用程序能够根据应用程序自身的需求处理音频会话中断。声音引擎仍然在内部执行音频相关中断处理。 – 移除了 bAppListensToInterruption 以使应用程序随时能够处理音频会话中断。 – 移除了回调注册 API。输入回调和中断回调通过 PlatformInitSettings 注册。

# API 变化（2014.1 beta 2）

- **WG-24628** (iOS) Ak::SoundEngine::iOS::Suspend 和 WakeupFromSuspend 现在是 Ak::SoundEngine 名字空间（所有平台）的一部分。
- **WG-24990** AkSinkType 现在分成 AkAudioAPI（结合 Ak::SoundEngine::Init 使用）和 AkAudioOutputType（结合 Ak::SoundEngine::AddSecondaryOutput 使用）

# API 变化（2014.1 最终版）

- **WG-25586** (iOS) 用户必须在用户中断回调中显式地执行暂停和恢复声音引擎的自定义策略。
- **WG-25586** (iOS) 从 ListenToAudioSessionInterruption() API 中移除了用于跳过用户回调的标志。现在可随时调用用户回调。

# 行为变化（2014.1 beta 1）

- **WG-19458** 如果没有真正使用属性，现在查询属性不会返回结果，因此它反而会使用父代覆盖。
- **WG-22295** 改进了转码结果文件 ID 分配，当在新对象中重新使用媒体时将保留现有 ID。
- **WG-25210** 每次从声部连接到总线时都会调用 [AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html) 回调函数，例如一次连接到直接/干声输出，一次将每个发送连接到辅助总线。

# 行为变化（2014.1 beta 2）

- **WG-25753** 根据 [Microsoft](namespace_microsoft.html) 的准则，Xbox One 最终混音始终是 7.1。

# 性能变化

- **WG-24453** 音频文件转码在 SoundBank 生成期间能够更好地利用多核机器。

# 其它更改（2014.1 beta 1）

- **WG-23663** Subversion SDK 已更新至 1.8.5
- **WG-24487** 基于 C++ 的新 CopyStreamedFiles 助手应用程序替代基于 C# 的 AkCopyStreamedFiles 采样工具。设计工具的 Windows 和 Mac 版本均可提供。
- **WG-24488**（Mac Authoring）：添加了工程示例和 Wwise 工程大冒险。
- **WG-25309**（Android）与所有其它平台一样，异常处理和 RTTI 现已被禁用。

# 其它更改（2014.1 beta 2）

- **WG-25139**（Mac）添加了 Mac 接收端插件的例程。
- **WG-25713** Perforce SDK 已更新至 Perforce 2014.1

# 其它更改（2014.1 最终版）

- **WG-25139**（Mac）添加了 Mac 接收端插件（CoreAudio）的例程。

# 漏洞修复（2014.1 beta 1）

- **WG-19832** 已解决：当指定的恢复时间短于 21 毫秒时，总线闪避出现异常行为。
- **WG-20383** 已解决：当声音时间短于它的预读时间时，内存中可能无法准备预读数据。
- **WG-21868** 已解决：当第一个音乐段落短于下一段落的前导段时，CAkSegmentCtx::NotifyAction 崩溃。
- **WG-23324** 已解决：总线输出模式中的错误 HDR 窗口位置。
- **WG-23588** 已解决：（iOS）在允许应用程序之间进行音频混音的情况下，使用 playAndRecord 音频会话类别时发生崩溃。
- **WG-23777** 已解决：当声音有低频效果时，已渲染的效果器的后置声道顺序错误。
- **WG-23837** 已解决：硬件解码器的预读重定位不安全（当串流的“零延迟”声音正在播放时，交换 SoundBank）。rs.
- **WG-23871** 已解决：即使在流管理器缓存中可以轻松地获得数据，流播放声音也可能被置于预缓冲模式下。这将导致不必要的延迟。
- **WG-23916** 已解决：总线上的静音动作在 Wwise 设计工具中不工作（间歇性错误）（仅限于设计工具）。
- **WG-24236** 已解决：当 Wwise 设计工具与游戏断开时的情形可能使针对定位所设置的参数无效。
- **WG-24610** 已解决：在 Advanced Profiler 中对特定列排序时崩溃。
- **WG-24649** 已解决：当关闭并重新打开 Wwise 工程时，无益地重新转换卷积混响 IR。
- **WG-24737** 已解决：如果干声衰减为 -200 dB，即使湿声衰减高于阈值，声部也会降到阈值以下。
- **WG-24800** 已解决：无法导入 6.x 文件。
- **WG-24804** 已解决：即使相关听者不活跃，音频也会发送到二路设备。
- **WG-24817** 已解决：移动嵌套工作单元将导致连接在下一次加载时断开。
- **WG-24819** 已解决：（Mac）IntegrationDemo 中话筒演示崩溃。
- **WG-25001** 已解决：将使用 7.1 总线配置的平台/工程的扬声器角度设置为立体声或 5.1 配置后崩溃。
- **WG-25003** 已解决：如果虚声部依赖它的发送音量执行，则虚声部可能不会成为实声部。
- **WG-25061** 已解决：低于阈值的声部不会先被播放限制系统终止。
- **WG-25066** 已解决：“Reset Bus Volume All”动作范围应始终为全局。
- **WG-25070** 已解决：当取值单位为 dB 时，UI 错误地输出峰值 Y 轴刻度尺。

# 漏洞修复（2014.1 beta 2）

- **WG-22242** 已解决：（Mac 设计工具）在 Project Explorer 中无法使用“Delete”键删除对象。
- **WG-24600** Fixed: (Xbox One) XMA with sample rate different than 48KHz does not seek at the proper location.
- **WG-24845** 已解决：纠正无用的可变编译警告。
- **WG-25067** 已解决：Audio-To-Motion 对连通到控制器扬声器的声音无效。
- **WG-25110** 已解决：当段落最后音频帧生命期间发生事件（提示、网格）时未发布音乐通知。
- **WG-25502** 已解决：如果原始波形文件路径在转换为 Vorbis 时超过 Windows 最大路径，则 SoundBank 生成操作可能崩溃。
- **WG-25571** 已解决：某些查询操作导致 Wwise 设计工具崩溃。
- **WG-25587** 已解决：（Xbox One）当 Xbox One 以 5.1 输出时发生错误行为。
- **WG-25618** 已解决：当通过 POSIX 未找到文件时，从 LoadBank 返回无用的错误代码。
- **WG-25623** 已解决：预置文件夹中的 CrossfadingParameterRef 未正确迁移。
- **WG-25655** 已解决：路径列表中的 Music Switch Editor 字符串排序不一致。
- **WG-25663** 已解决：定位类型的 SetRTPCValue 应用于全局。
- **WG-25670** 已解决：AK\_EndOfEvent 回调中返回的 eventID 值错误。
- **WG-25721** 已解决：SetSwitchInternal 可能发生崩溃。
- **WG-25738** 已解决：HDR 包络跟踪对外部源无效。
- **WG-25746** 已解决：针对 Atrac9 的最小采样数量发出错误的错误消息。
- **WG-25751** 已解决：（Vita）由于流媒体内存小于 4 M，无法以流播放 2 个 ATRAC9 声音。
- **WG-25755** 已解决：XAudio2 在某些场景中不能正确加载（添加 LoadLibrary 解决方案）。
- **WG-25756** 已解决：在打开工程时，可能发生转码结果文件 ID 冲突。
- **WG-25761** 已解决：缺少源解决方案文件 Visual Studio 2013。
- **WG-25770** 已解决：（Vita 硬件）Vita 延迟效果器不起作用。
- **WG-25772** 已解决：Crankcase REV 在多线程上转码时可能发生崩溃
- **WG-25779** 已解决：更换插件媒体文件不会更新 ConvertedFileIDList，而是在工程重新加载时更新。

# 漏洞修复（2014.1 最终版）

- **WG-24404** 已解决：（Android、iOS、Mac、PS4）CAkIOThread——已纠正内核资源分配失败时的互斥属性清理。
- **WG-25057** 已解决：（Xbox One）Xbox One 控制器振动错误地将触发器保持在活跃状态。
- **WG-25448** 已解决：（PS4）当音高超过 2400 音分时，AT9 存在断言。最高将固定为原始音高的 4 倍。
- **WG-25586** 已解决：（iOS）在 IntegrationDemo 中，动态对白演示测试事件积累在一起，然后在音频中断结束后一起播放。
- **WG-25658** 已解决：（Windows 商店）在 Windows 商店应用程序的实用程序脚本中非法使用 HandleRef。
- **WG-25727** 已解决：无法加载注释中含空白的 Wwise 工程。
- **WG-25745** 已解决：（iOS）当您在某些情况下从 Apple Music 应用程序中播放音乐时，IntegrationDemo 音频发出杂声。
- **WG-25783** 已解决：在实用程序中 CancelEventCallback 导致内存不足。
- **WG-25787** 已解决：（Mac Authoring）Wwise 无法迁移更早版本的 Wwise 工程。
- **WG-25789** 已解决：Transport Control 的播放按钮被卡住。
- **WG-25800** 已解决：在某些 vorbis 文件结束时越界访问内存。
- **WG-25819** 已解决：当在没有听者的游戏对象上播放声音时使用 Don't Follow Listener Orientation 将发生崩溃。
- **WG-25838** 已解决：（Vita）硬件混响效果器受损。
- **WG-25845** 已解决：HDR 系统误判在 HDR 层级结构外的辅助总线中传输的信号电平。
- **WG-25848** 已解决：（iOS）从挂起中唤醒后崩溃。
- **WG-25862** 已解决：（iOS）在升级到 Xcode 5.0.1 后，无法对 iOS 的 Game Simulator 应用程序进行代码签名。
- **WG-25871** 已解决：（Linux，Android x86）在 GCC 4.6.3 的 Bypass\_I16\_2ChanSSE2 中使用无效的对齐 opcode。
- **WG-25891** 已解决：在执行工作组文件操作时，DirectoryWatcher 中发生崩溃。
- **WG-25904** 已解决：当对象包含 LPF 曲线时，Query::GetPositioningInfo 发生崩溃。
- **WG-25925** 已解决：（Xbox One）如果 SHAPE 已经初始化，则 [AK::SoundEngine::Init](namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a9a26da64092b97243844df77cbcdbf5f) 发生崩溃。
- **WG-25938** 已解决：MIDI 临时图处理不正确。
- **WG-25958** 已解决：在“无有效切换开关”错误消息中缺少组名。
- **WG-25980** 已解决：当 Perforce 询问密码时，命令行发生崩溃。
- **WG-25988** 已解决：在少数情况下还有尚未执行的过渡段但音乐切换容器却停止，此时 NotifyMusicCallbacks() 将发生崩溃。
- **WG-25982** 已解决：（Mac Authoring）当音频文件路径采用 Unix 格式时，使用用制表符分隔的文件导入音频文件不可行。
- **WG-26006** 已解决：GetSourcePlayPosition() 在尾音期间返回无用信息。
- **WG-26046** 已解决：当使用辅助总线在总线上应用状态时，LPF 和 HPF 可能丢失。