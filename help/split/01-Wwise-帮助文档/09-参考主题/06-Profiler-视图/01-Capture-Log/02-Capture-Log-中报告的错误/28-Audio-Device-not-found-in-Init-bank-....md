# Audio Device not found in Init bank: ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Audio Device not found in Init bank: ...

#### Audio Device not found in Init bank: ...

“未在 Init 音频包中找到音频设备: …。”没有找到 API 调用引用的 Audio Device。

**可能的原因：**

- 尚未加载 Init SoundBank。
- 函数参数中传递的名称拼写有误。
- 在将 Audio Device 添加到工程中之后没有重新生成或重新部署 Init SoundBank。

**推荐的解决步骤：**

- 连接 Wwise Profiler（性能分析器）并检查是否在发生此错误之前加载了 Init SoundBank（音频包）。
- 打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。连接 Wwise Profiler（性能分析器）并检查是否将参数传给了触发此错误的函数。
- 在测试主机上重新生成并重新部署 SoundBank（音频包）。

---