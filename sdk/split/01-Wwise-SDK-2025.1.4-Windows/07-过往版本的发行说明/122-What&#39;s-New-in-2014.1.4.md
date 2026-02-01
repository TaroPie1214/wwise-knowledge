# What&#39;s New in 2014.1.4

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2014.1.4

2014.1.4 属于补丁发布。以下各节列举并描述 Wwise 版本 2014.1.3 和版本 2014.1.4 之间的变化。

# 平台 SDK 的变化

- Xbox One XDK 已更新到 2015 年 2 月。

# 性能改进

- **WG-26700** 提高了 Wwise Profiler 性能。

# 行为变化

- **WG-25995** 更改了 [SetGameObjectOutputBusVolume()](namespace_a_k_1_1_sound_engine_adf1401ce64872af26cdff05b36e98161.html#adf1401ce64872af26cdff05b36e98161)，现在即使声部没有发送到用户或游戏定义的辅助总线，也可影响声部的（主要）输出总线音量。

# 新功能

- **WG-27008** 添加了简体中文版的 Wwise Project Adventure 手册。

# 其它更改

- **WG-26841** 在 PS4 发布版中删除了一些编译警告。
- **WG-26784** 为 Mac Authoring 添加了 Wwise 命令行工具。

# 漏洞修复

- **WG-26197** 已解决：在对多声道 XMA 编码时发生 XMA 转码错误。
- **WG-26518** 已解决：如果原始文件不存在，则无法从 Transport 中以“非原始”模式播放循环声音。
- **WG-26688** 已解决：当被检查的总线不是 HDR 时，声部监视总线输入模式不能显示正确值。
- **WG-26717** 已解决：在已卸载切换容器仍在工作的情况下更改状态时发生崩溃。
- **WG-26738** 已解决：Property Editor：当在浮动视图中添加 All Properties 选项卡时，改选项卡会隐藏。
- **WG-26750** 已解决：重命名或更改自定义属性位置时发生崩溃。
- **WG-26826** 已解决：在保存时可能显示的“Work Unit modified”消息现在可通过 Windows 注册表进行配置。
- **WG-26842** 已解决：音频硬件故障导致 Wii U 死机。
- **WG-26862** 已解决：每次调用 AK::SoundEngine::SetActiveListeners() 时都会出现“Sound is not attached to any listener”消息。
- **WG-26870** 已解决：在控制设备绑定中添加新绑定时可能发生崩溃。
- **WG-26871** 已解决：在播放音乐切换容器时可能发生崩溃。
- **WG-26881** 已解决：当使用 [AK::SoundEngine::GetSourceStreamBuffering()](namespace_a_k_1_1_sound_engine_a05ad41555fe186f82043626ad616ac3d.html#a05ad41555fe186f82043626ad616ac3d) 查询多个声音时存在轻微的返回码混乱。
- **WG-26897** 已解决：在某些互动音乐用例中，音频存在间隙。
- **WG-26899** 已解决：音乐切换轨上的淡入操作可能失败。
- **WG-26902** 已解决：没有分析所有混音器插件函数的 CPU 占用率。
- **WG-26912** 已解决：在另一布局中打开视图时，更改控制设备中的对象选择后，绑定组没有更新。
- **WG-26914** 已解决：控制设备绑定到有不同值域的游戏参数将相互影响。
- **WG-26917** [已解决：AK::SoundEngine::UnloadBank()](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64) 中的竞争危害导致默认池中偶尔发生内存损坏。
- **WG-26932** 已解决：没有保存自动修改的预置。
- **WG-26946** 已解决：实例限制功能在“Continue To Play”模式下忽略低于音量阀值的声部，并让它们播放。
- **WG-26962** 已解决：延迟流播放设备中不一致的 `AkDeviceSettings::uNumConcurrentIO` 导致 I/O 冻结。
- **WG-26963** 已解决：ConvertExternalSources 选项区分大小写，失败时不发出声音。
- **WG-26979** 已解决：不可缓冲流播放标志有时候被游戏侧 Wwise 忽略。
- **WG-26985** 已解决：当连续多次设置同一状态时，会错误地处理状态过渡时间。
- **WG-26922** 已解决：在 PS4 上使用 Atrac9 和 HDR 时发生崩溃。
- **WG-27006** 已解决：在使用 WwiseCLI.exe 生成 SoundBank 时发生 ControlSurfacesConfig.xml 错误。
- **WG-27025** 已解决：每次生成的初始化包，其 SoundbanksInfo.xml GUID 都不同。
- **WG-27027** 已解决：在 Atrac9 流播放文件上检测到解码错误时，PS4 上可能发生崩溃。