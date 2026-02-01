# 处理用户音乐（BGM）和DVR

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

处理用户音乐（BGM）和DVR

在许多主机上，可以将游戏音乐替换成用户个人收藏的音乐。在 Wwise 中，此功能几乎是自动完成的。然而，某些平台在实现和行为上有一些差异。

在所有平台上，初始设置是相同的：启动用户音乐时，声音设计师可以标记若干条总线让其静音。这一点通过“Mute for Background Music”复选框来实现。在程序方面，根据具体的平台另有细节处理。

# 针对 Android 的 BGM 详情

确保为 [AkPlatformInitSettings](struct_ak_platform_init_settings.html) 的 jActivity 成员赋值。只有当用户从音乐播放器应用程序切换到游戏时才会发生 Mute/Unmute（静音／取消静音）操作。这意味着，如果用户音乐自行结束，则不会发生“Unmute”操作。

# 针对 iOS 的 BGM 详情

只有外部音乐应用程序使用可混音音频会话配置，才能使用其来替换游戏音乐。您可以通过以下两种方式获取可混音音频会话：

- 使用 Ambient 音频会话类别。
- 使用 PlayAndRecord 或 Playback 音频会话类别，同时结合运用 MixWithOthers 类别选项。

若采用除上述外的其他配置，当游戏在前台运行时，将停止用户的音乐应用程序。

# 在启用 DVR 的平台（Xbox One、Xbox Series X、PlayStation 4 和 PlayStation 5）上播放背景音乐

某些平台具有 DVR 功能，可让游戏玩家记录和发布其游戏过程。这会带来一些法律问题，其中涉及到游戏音频当中受版权保护的音乐或用户可替换音乐。虽然游戏工作室有权在其游戏中使用所述音乐，但最终用户可能无权以任何形式对其进行分发。因此，平台要求中通常会声明不允许录制用户背景音乐。

针对这个问题，一个高性价比的解决方案（对 CPU 而言）是将音乐和游戏的其他内容分开混音。这通过使用 Secondary Output （二路输出）功能来实现。

# 在设计工具中设置背景音乐

In the authoring tool, you will need to route your music objects to a separate Main Audio Bus than the default or primary one. In most projects, this means creating a brand new Main Audio Bus (right click on the Busses Hierarchy's Work Unit and select Add > Child). 在默认情况下，所有总线均连通至 System 输出。请更改 Audio Device ShareSet，使其指向 DVR 输出。

请记住，并非所有平台都支持 DVR。对于不支持 DVR 的平台，必须取消链接 Audio Device 属性，以便指向 System 输出。另外，也可取消链接音乐对象的 Output Bus 属性。

# 在游戏代码中设置 DVR 输出

如果游戏中要使用 DVR 输出，则必须手动添加这个输出。实现方式为使用 `AK::SoundEngine::AddOutput()` 一并传递 Audio Device ShareSet 名称/ID 和 `AkOutputSettings` 中的其他参数。

有关 示例，请参阅 *<Wwise installation path>/SDK/samples/IntegrationDemo/DemoPages/DemoBGM.cpp*。