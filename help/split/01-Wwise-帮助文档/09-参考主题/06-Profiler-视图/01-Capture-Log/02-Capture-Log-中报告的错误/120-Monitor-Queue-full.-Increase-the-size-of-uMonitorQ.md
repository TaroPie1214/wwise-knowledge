# Monitor Queue full. Increase the size of uMonitorQueuePoolSize. Message size ... bytes.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Monitor Queue full. Increase the size of uMonitorQueuePoolSize. Message size ... bytes.

#### Monitor Queue full. Increase the size of uMonitorQueuePoolSize. Message size ... bytes.

“监控队列已满。增大 uMonitorQueuePoolSize。消息大小…字节。”Wwise Profiler（性能分析器）所用的 Monitor Queue（监控队列）已满而无法包含一条消息。此错误的唯一不良后果是 Wwise Profiler 中会缺少一条消息。

**可能的原因：**

- 在使用 API 性能分析时，若 API 调用骤然增多，则可能会出现此错误。
- 同一 CPU 内核上的线程具有不同的优先级，导致无法及时运行监控线程。

**推荐的解决步骤：**

- 增大 `AkInitSettings::uMonitorQueuePoolSize`。
- 更有规律地调用 `AK::SoundEngine::RenderAudio` 以免 API 调用突然增多。
- 利用 CPU 性能分析器检查共用同一 CPU 内核的所有线程的线程优先级。

---