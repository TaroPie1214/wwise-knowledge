# Memory allocation failed.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Memory allocation failed.

#### Memory allocation failed.

“内存分配失败。”可用内存不足，导致内存分配失败。在初始化时通过设置 `AkMemSettings::uMemAllocationSizeLimit` 在代码中定义了 Wwise 可以使用的最大内存量。注意，Advanced Profiler（高级性能分析器）中的 Memory（内存）选项卡会显示每隔 200 ms 截取的内存当前状态快照。因此，即使是在报告错误的相应时间点，有可能也会显示内存充足。

**推荐的解决步骤：**

- 通过卸载未使用的 SoundBank（音频包）或将 SoundBank 拆分为更小的文件来降低内存用量。这样可以节省大量内存。
- 通过注销更少的 Game Object（游戏对象）来降低内存用量。
- 增大 `AkMemSettings::uMemAllocationSizeLimit`。

**另请参阅：**

- [“Memory”一节](../../03-Advanced-Profiler/08-Memory.md "Memory")
- [Memory Manager](https://www.audiokinetic.com/library/edge/?source=SDK&id=memorymanager.html)

---