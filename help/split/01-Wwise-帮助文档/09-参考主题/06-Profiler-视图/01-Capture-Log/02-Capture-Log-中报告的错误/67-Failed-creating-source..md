# Failed creating source.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Failed creating source.

#### Failed creating source.

“无法创建音频源。”此为一般性错误，表示无法启动音频源。

**可能的原因：**

- 源使用了一个未注册的插件。此错误之前可能会出现插件错误。
- 没有足够的内存，无法创建源（在此之前应会出现内存不足错误）
- 此源的总线不存在。**Init** SoundBank（初始化音频包）可能没有更新。
- 某意外错误。

**推荐的解决步骤：**

- 检查日志中的“内存不足”错误，并通过分配更多内存来加以解决。请参阅 [“Memory allocation failed.”一节](115-Memory-allocation-failed..md "Memory allocation failed.")。
- 确保 **Init** SoundBank 与包含此源的 SoundBank 同步。重新生成并重新复制这些 SoundBank。
- 联系 Audiokinetic 技术支持部门。在重现问题时，最好捕获 ProfilingSession.prof。有关详细信息，请参阅[“保存 Capture Log”一节](../../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/08-保存-Capture-Log.md "保存 Capture Log")。

---