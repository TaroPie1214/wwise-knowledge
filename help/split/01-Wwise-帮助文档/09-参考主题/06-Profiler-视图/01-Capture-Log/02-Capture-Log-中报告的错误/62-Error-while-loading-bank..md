# Error while loading bank.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Error while loading bank.

#### Error while loading bank.

“在加载音频包时出错。”此错误表示在解码 SoundBank（音频包）结构时 SoundBank 加载进程失败。这是一个万不得已时给出的错误，可能由各种差错类型导致。请在 Capture Log（捕获日志）中查看此前出现的其他错误。

**可能的原因：**

- 磁盘上的 SoundBank 损坏。
- 出现未处理的“内存不足”错误。此错误应向技术支持部门报告。
- 某意外错误。

**推荐的解决步骤：**

- 检查日志中的内存不足错误并解决这些错误。
- 重新生成 SoundBank，并重新部署至目标平台。
- 联系 Audiokinetic 技术支持部门。在重现问题时，最好捕获 ProfilingSession.prof。有关详细信息，请参阅[“保存 Capture Log”一节](../../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/08-保存-Capture-Log.md "保存 Capture Log")。

---