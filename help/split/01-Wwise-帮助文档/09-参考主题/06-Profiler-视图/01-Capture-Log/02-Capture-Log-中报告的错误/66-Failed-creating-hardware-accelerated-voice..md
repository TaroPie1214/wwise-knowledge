# Failed creating hardware-accelerated voice.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Failed creating hardware-accelerated voice.

#### Failed creating hardware-accelerated voice.

“无法创建启用了硬件加速的声部。”若声音采用了硬件加速的音频格式，而其又无法从平台操作系统获取相应的资源来启动解码，则会出现此错误。这时将无法播放该声音。

**可能的原因：**

- SoundBank 或媒体损坏可能会导致出现此问题。
- 超出声部数限值或为硬件操作预留的内存量。

**推荐的解决步骤：**

- 重新生成 SoundBank 和媒体。若问题依然存在，则表示可能硬件发生了故障、游戏存在漏洞或 Wwise 本身出现了问题。在这种情况下，请联系 Audiokinetic 技术支持部门。

---