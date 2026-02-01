# Another process is using Microsoft Spatial Sound objects. Some audio objects may be mixed.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Another process is using Microsoft Spatial Sound objects. Some audio objects may be mixed.

#### Another process is using Microsoft Spatial Sound objects. Some audio objects may be mixed.

“另一进程正在使用 Microsoft Spatial Sound 对象。可能会对某些音频对象实施混音。”在 Windows 上，所有当前运行的进程（包括游戏和应用）只能共用一定数量的 Microsoft Spatial Sound 对象。若 Capture Log（捕获日志）中显示此消息，则表示声音引擎无法保有这些对象，因为另一进程已经保有它们。最终，会将本来要作为 System Audio Object（系统音频对象）发送的 Audio Object 混音到 Main Mix（主混音）中。

**可能的原因：**

- Wwise 设计工具保有全部系统对象，导致同一 PC 上运行的游戏无法使用它们。
- 正在后台运行另一使用 Microsoft Spatial Sound 的游戏或应用。

**推荐的解决步骤：**

- If you are trying to audition System Audio Objects from within Wwise, first stop all other applications or games using the Microsoft Spatial Sound API. Then enable **Allow System Audio Objects**. 详请参阅[“Reserving system audio objects”一节](../../../../02-入门/04-个性化您的工作空间/05-Setting-authoring-audio-preferences.md#allow_system_audio_objects "Reserving system audio objects")。
- 若想在同一 PC 上与 Wwise 同时运行的游戏中试听 System Audio Object，首先要确保停止运行其他所有使用 Microsoft Spatial Sound API 的应用或游戏。Then disable **Allow System Audio Objects**. 详请参阅[“Reserving system audio objects”一节](../../../../02-入门/04-个性化您的工作空间/05-Setting-authoring-audio-preferences.md#allow_system_audio_objects "Reserving system audio objects")。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 有些 Windows 版本存在漏洞，会禁止活跃的 Spatial Sound 媒体流获取已被另一进程释放的对象。在这种情况下，必须重新启动媒体流，才能获取这些对象。  若确定游戏是唯一在使用 Microsoft Spatial Sound 的进程，而 Capture Log 中依然显示此错误，则可能需要重新启动声音引擎来规避这一问题。 |

---