# Stinger could not be scheduled in this segment or was dropped.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Stinger could not be scheduled in this segment or was dropped.

#### Stinger could not be scheduled in this segment or was dropped.

“插播乐句无法安排到此段落中或已被弃用”。若 Trigger（触发器）调用了 Stinger（插播乐句），但在当前或下一段落中再次播放 Stinger 的时机太晚，因此弃用了 Stinger，则将出现此错误。

**推荐的解决步骤：**

- 在 Stinger（插播乐句）属性中设置 **Allow playing Stinger in next segment**（允许在下一段落中播放插播乐句）。

---