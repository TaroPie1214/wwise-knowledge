# What&#39;s New in 2014.1.5

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2014.1.5

2014.1.5 属于补丁发布。以下各节列举并描述 Wwise 版本 2014.1.4 和版本 2014.1.5 之间的变化。

# 平台 SDK 的变化

- PS3：已更新至 SDK 470
- PS4：已更新至 SDK 2.5
- Xbox One：已更新至 SDK 2015 年 4 月。
- Android：已更新至 NDK r10d，可与 Lollipop 兼容。现在支持 arm64-v8a 和 x86\_64 ABI。

# 新功能

- **WG-27277** Crankcase REV 添加了对立体声和 5.1 音源的支持。

# API 变化

- **WG-26655** (iOS) 添加了回调函数，以让用户可以在另一应用程序的音频开始或停止播放后采取行动。为 [AkPlatformInitSettings](struct_ak_platform_init_settings.html) 添加了新成员，此成员指向新的回调函数。

# 行为变化

- **WG-26655** (iOS) 用户不再需要在音频会话中断（例如电话或用户音乐活跃）后提供 UI 来恢复音频。声音引擎正确处理音频挂起和恢复。
- **WG-27174** (iOS) 如果 AAC 编码音频对象的虚行为是 Continue to Play，则在设备挂起期间，此行为将自动切换到 Send to Virtual Voice，并且 Return to Physical Voice 行为将自动设置为 Play from Elapsed Time。两种行为将在它们的整个生命期间保持这种状态。

# 漏洞修复

- **WG-20048** 已解决：完好度报告错误地对包含寻址表的 Vorbis 声音发出警告。
- **WG-26591** 已解决：（iOS）在通过 iTunes 商店应用程序购买期间锁定和解锁设备时发生崩溃。
- **WG-26655** 已解决：（iOS）AmbientSound 类别下的音频在 iOS 8 电话中断后发生故障。
- **WG-26656** 已解决：原始 WAV 不存在但缓存中存在它的文件时未报错。
- **WG-26744** 已解决：（iOS）在忙于播放声音的同时暂停用户音乐会使 iOS 中的应用程序崩溃。
- **WG-26813** 已解决：振动（PS4 和 Xbox One）：时长超过 3 秒的恒定振动会自动终止。
- **WG-26869** 已解决：（Mac）默认声道设置始终设为立体声。
- **WG-27026** 已解决：不支持 Android ARM64 和 x64。
- **WG-27047** 已解决：当使用选择器按钮更改属性时，如果显示了 List View 或 Reference View，则 Property Editor 的内容会被迫改变。
- **WG-27054** 已解决：互动音乐：由于不当的“Jump to playlist item”按钮刷新，断言（MusicTransitionPane.cpp）崩溃。
- **WG-27064** 已解决：AkSoundEngineWindows\_vc### 工程引用不存在的属性表。
- **WG-27087** 已解决：当在 PS4 上从循环点周围的两个连续小缓冲区流播放时发生 AT9 解码问题。
- **WG-27101** 已解决：在 Xbox One 上，多声道 XMA 文件发生断言或挂起。
- **WG-27109** 已解决：Vorbis 流播放中存在未处理源匮乏场景，这可能导致崩溃。
- **WG-27119** 已解决：应用于声像摆位的 LFO 或包络未添加到 SoundBank 的内容中。
- **WG-27167** 已解决：在对新的或不活跃的游戏对象使用内置游戏参数时进行阈值决策，可能选择错误的切换开关。
- **WG-27170** 已解决：当选择“Show in Schematic View”时，示意图视图断言（NotifyMgr.cpp）崩溃。
- **WG-27174** 已解决：（iOS）当应用程序调用 API Suspend(true) 时，AAC 解码管线崩溃。
- **WG-27180** 已解决：当设置的游戏对象位置坐标非常靠近听者时，除数为 0。
- **WG-27182** 已解决：当声音有初始延时时会跳过事件淡入。
- **WG-27190** 已解决：对 2D/3D 设置 RTPC 会阻止 SoundBanks.xml 中的 MaxAttenuation 信息。现在 RTPC 将被视为“3D”，并生成 MaxAttenuation。
- **WG-27192** 已解决：延迟设备 Cancel() 中存在竞争危害。
- **WG-27220** 已解决：（3DS）IAkSourcePluginContext::GetVoiceInfo 返回无效的指针。
- **WG-27241** 已解决：当超出并行过渡段的最大数量时可能发生崩溃或堆栈溢出。
- **WG-27275** 已解决：如果存在目标，并且修改时间比源更晚，则 CopyStreamedFiles 不会复制文件。
- **WG-27314** 已解决：减少了外部源的命名限制（在某些工程中，此漏洞可能妨碍 Profiler 连接）。
- **WG-27329** 已解决：在更换 X 轴时，RTPC 列表可能崩溃。
- **WG-27374** 已解决：当生成 SoundBank 时，错误日志系统中发生罕见的随机崩溃。
- **WG-27410** 已解决：消息队列中罕见的竞争危害可能导致内存溢出。