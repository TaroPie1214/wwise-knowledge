# What&#39;s New in 2014.1.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2014.1.3

2014.1.3 属于补丁发布。以下各节列举并描述 Wwise 版本 2014.1.2 和版本 2014.1.3 之间的变化。

# 性能改进

- **WG-26630** 改进了 UI 性能。

# 新功能

- **WG-13970** 设计工具：现在可在 User Settings 中配置输出缓冲区的采样点数。
- **WG-23400** 支持在 XBox One 和 PS4 上更换背景音乐总线。在标记为“Background Music”的总线的静音/取消静音上添加了新的 API MuteBackgroundMusic。

# 漏洞修复

- **WG-26349** 已解决：对于带混合 2D 和 3D 源的容器，SoundBanksInfo 最大半径不是无限的。
- **WG-26408** 已解决：在带 AkOutput\_Personal 的 PS4 上发生 AddSecondaryOutput 断言。
- **WG-26412** 已解决：当全局采样率不是 48 kHz 时，发生高通滤波尖峰，并且 HPF 值超过 90。
- **WG-26415** 已解决：应用到其它调制器的调制器因为没有以正确顺序加载，所以可能无法工作。
- **WG-26435** 已解决：SVN 插件不支持不可信的证书（而使用弃用的 SSL 函数）。
- **WG-26445** 已解决：REDO MIDI 文件导入时崩溃。
- **WG-26454** 已解决：当卷积混响位于第一槽时，将音频发送到包含一串带尾音的效果器的总线时发生崩溃。
- **WG-26459** 已解决：在 ControlSurfaceMidiAction 期间连接设计工具时发生崩溃。
- **WG-26469** 已解决：在调制器包络衰减时 MIDI 音符关闭没有正确释放。
- **WG-26482** 已解决：总线音量从 dB 转换为线性，然后再转为 dB 会导致低效，并会对 HDR 造成危险的数值问题。
- **WG-26499** 已解决：当排除有多个源在引用的媒体时，SoundBank Editor 的 Edit 选项卡中的 Exclusion 复选框无法正常工作。
- **WG-26513** 已解决：当预置文件夹不存在时，加载工程会导致崩溃。
- **WG-26514** 已解决：当复制或移动声音，或者编辑声音的 HDR 包络时，转码结果文件 ID 有时候无法正常作废。
- **WG-26535** 已解决：当声部低于音量阈值被设为“Kill Voice”时，有时会忽略 HDR 包络。
- **WG-26538** 已解决：对于某些编译程序，性能分析代码中存在潜在的堆栈溢出。
- **WG-26539** 已解决：从输入为总线的混音器插件 OnInputConnected() 中调用 GetInputParam() 时，CAkBusVolumes::CreateAttachedPropsParam() 崩溃。
- **WG-26569** 已解决：在启用延迟设备和缓存的情况下，I/O 计数不一致导致断言和未定义的行为。
- **WG-26572** 已解决：振动发生器：当在设计工具中单独执行 XboxOne Trigger 时，发生 ASSERT(vector)。
- **WG-26573** 已解决：XML schema 读数不一致阻止混音插件添加数据文件。
- **WG-26583** 已解决：当调制器在仍在播放的声音上工作时卸载 SoundBank，卸载后发生崩溃。
- **WG-26584** 已解决：在播放 XMA 和 ATRAC9 流时，GetSourceStreamBuffering() 返回 AK\_Fail。
- **WG-26601** 已解决：在 SFTest 中禁用然后启用空间定位导致 Wwise 崩溃。
- **WG-26607** 已解决：当外部源不完整时，无 Ak\_EndOfEvent 回调。
- **WG-26636** 已解决：如果先播放二路主总线，则二路主总线将使其它总线静音。
- **WG-26650** 已解决：MusicEngine::Term（由于 CAkMidiDeviceMgr）而崩溃。