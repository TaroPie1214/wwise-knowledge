# System ran out of resources while loading plug-in dynamic library.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > System ran out of resources while loading plug-in dynamic library.

#### System ran out of resources while loading plug-in dynamic library.

“在加载插件动态库时系统耗尽资源”。系统需要分配内存以满足插件的静态分配需求。在加载库时，系统耗尽了相应资源。

**可能的原因：**

- 插件需要加载大量静态内存。
- 在加载插件时，游戏已经预留了太多虚拟内存。

**推荐的解决步骤：**

- 避免为所用插件分配过多的静态内存。
- 检查游戏的内存消耗，并确保在加载 SoundBank 时为插件留有足够的内存。

---