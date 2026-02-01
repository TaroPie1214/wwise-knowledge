# Cannot schedule music segments: Stopping music.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Cannot schedule music segments: Stopping music.

#### Cannot schedule music segments: Stopping music.

“无法安排音乐段落: 停止音乐”。音乐播放列表内播放的段落太多或包含无限循环。

**可能的原因：**

- 段落的入口提示点与出口提示点重叠。
- 队列中包含大量很短的段落。

**推荐的解决步骤：**

- 检查入口提示点和出口提示点，确保两者没有重叠。
- 降低音乐容器的复杂度。

---