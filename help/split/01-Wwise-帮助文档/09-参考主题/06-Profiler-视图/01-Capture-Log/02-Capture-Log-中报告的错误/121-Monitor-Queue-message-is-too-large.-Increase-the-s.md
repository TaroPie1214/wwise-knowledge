# Monitor Queue message is too large. Increase the size of uMonitorQueuePoolSize. Message size ... bytes.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Monitor Queue message is too large. Increase the size of uMonitorQueuePoolSize. Message size ... bytes.

#### Monitor Queue message is too large. Increase the size of uMonitorQueuePoolSize. Message size ... bytes.

“监控队列消息太长。增大 uMonitorQueuePoolSize。消息大小…字节。”Wwise Profiler（性能分析器）所用的 Monitor Queue（监控队列）无法包含其中一条要发送到 Profiler 的消息。消息的最大大小为 `AkInitSettings::uMonitorQueuePoolSize` 的一半。在分析 API 调用时可能会触发此错误，因为有些 API 会传递不受值域限制的参数数组。此错误的唯一不良后果是 Wwise Profiler 中会缺少一条消息。

**推荐的解决步骤：**

- 确认对 `AK::SoundEngine::SetMultiplePositions` 和所有 Spatial Audio 几何构造函数的调用以减少参数数组的数量。此消息通常表示 API 调用格式不正确。
- 增大 `AkInitSettings::uMonitorQueuePoolSize`。

---