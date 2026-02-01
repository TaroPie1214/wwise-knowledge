# Ignoring seek after end of playlist.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Ignoring seek after end of playlist.

#### Ignoring seek after end of playlist.

“避免在播放列表结束后寻址。”播放列表中当前所含全部条目播完后，又尝试对 Interactive Music（互动音乐）播放列表进行寻址。

**推荐的解决步骤：**

- 在 Wwise Profiler（性能分析器）的 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings")（性能分析器设置）中，启用 **API Calls**（API 调用），并查明哪个 [`SeekOnEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a602a2d51d394c55e1896d3ffa521adff.html) API 调用使用了错误的值。

---