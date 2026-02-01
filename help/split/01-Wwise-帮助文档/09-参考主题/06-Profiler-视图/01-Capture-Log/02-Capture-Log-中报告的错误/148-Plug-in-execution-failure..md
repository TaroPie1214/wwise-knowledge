# Plug-in execution failure.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Plug-in execution failure.

#### Plug-in execution failure.

“插件执行失败”。此错误表示在运行当中处理音频数据时无法执行所列插件（源、效果器、混音器或 sink）。

**可能的原因：**

- 通常在因内存不足而无法分配临时处理缓冲区时发生。
- 部分第三方插件可能因内部原因而生成此错误。

**推荐的解决步骤：**

- 检查此 Plug-in execution failure 错误之前出现的内存错误。可能需要增大内存总量。

---