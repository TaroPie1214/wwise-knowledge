# Reverting to Dummy Audio device (no output).

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Reverting to Dummy Audio device (no output).

#### Reverting to Dummy Audio device (no output).

此消息始终显示在另一错误之后。它表示音频输出不会发送到任何物理设备，而会被直接忽略。在这种情况下，不会有任何声音。声音引擎的其余操作会继续正常执行；处理 Event 和声音、在声音播完时产生回调等。在 Capture Log（捕获日志）中查看此前出现的错误，并逐项查明原因以便解决此问题。

---