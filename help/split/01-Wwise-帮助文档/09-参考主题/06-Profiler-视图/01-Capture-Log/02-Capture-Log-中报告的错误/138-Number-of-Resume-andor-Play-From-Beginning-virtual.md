# Number of Resume and/or Play-From-Beginning virtual voices has reached warning limit (see Project Settings &gt; Log tab). There may be some infinite, leaked voices.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Number of Resume and/or Play-From-Beginning virtual voices has reached warning limit (see Project Settings > Log tab). There may be some infinite, leaked voices.

#### Number of Resume and/or Play-From-Beginning virtual voices has reached warning limit (see Project Settings > Log tab). There may be some infinite, leaked voices.

“设置为‘恢复’或‘从头开始播放’的虚声部数达到警告限值（参见 Project Settings > Log 选项卡）。可能存在无限声部的泄漏现象”。虚声部数已达到临界值，这表示游戏中很可能存在错误，或者 Wwise 工程中的设置不合理。在以下情况下，虚声部可能会永远保持活跃状态：

- 声音设为无限循环，Virtual Voice Behavior（虚声部行为）设为 Kill（终止）以外的选项。此声音必须由 Stop Event（停止事件）主动停止。
- 声音的 Virtual Voice Behavior 设为 Resume（恢复）或 Play From Beginning（从头开始播放），但因音量不够高而一直没有恢复为 **Physical**（实声部）。因此，一直没有播放到结尾。

**另请参阅：**

- [“Advanced category”一节](../../../../08-使用-Wwise/03-了解-Property-Editor/08-Advanced-category.md "Advanced category")

---