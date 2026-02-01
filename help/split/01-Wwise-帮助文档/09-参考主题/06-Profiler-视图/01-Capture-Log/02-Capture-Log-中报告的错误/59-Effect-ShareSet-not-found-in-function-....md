# Effect ShareSet not found in function ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Effect ShareSet not found in function ...

#### Effect ShareSet not found in function ...

“未在函数…中找到效果器共享集。”没有在当前加载的 SoundBank 中找到指定函数的参数引用的 Effect ShareSet。

**可能的原因：**

- 尚未加载或在调用前已卸载包含此 Effect ShareSet 的 SoundBank。
- 工程中没有任何 SoundBank 包含该 Effect ShareSet。
- 函数参数中传递的 ID 拼写有误。
- 在将 Effect ShareSet 添加到工程中之后没有重新生成或重新部署 SoundBank。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若 Audio Bus 指向所用的 Audio Device ShareSet，则会将 Audio Bus 所用的 Effect ShareSet 打包到 Init SoundBank 中。若非如此，则须将 Effect ShareSet 手动添加到 User-Defined SoundBank。并且，该 SoundBank 必须由游戏加载。 |

**推荐的解决步骤：**

- 连接 Wwise Profiler（性能分析器）并检查是否在发生此错误之前加载了包含该 ShareSet（共享集）的 SoundBank（音频包）。
- 打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings")（性能分析器设置），并启用 **API Calls**（API 调用）。连接 Wwise Profiler（性能分析器）并检查是否将参数传给了触发此错误的函数。或者，也可针对指定函数调用在游戏代码中放置断点。
- 在测试主机上重新生成并重新部署 SoundBank（音频包）。

---