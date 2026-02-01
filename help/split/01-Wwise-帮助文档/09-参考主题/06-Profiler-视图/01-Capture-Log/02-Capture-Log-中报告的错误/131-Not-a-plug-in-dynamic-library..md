# Not a plug-in dynamic library.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Not a plug-in dynamic library.

#### Not a plug-in dynamic library.

“不是插件动态库。”加载了有效的动态库，但没有导出与 Wwise 声音引擎插件相符的符号。

**可能的原因：**

- 插件代码未使用 `AK_IMPLEMEMENT_PLUGIN_FACTORY` 宏。

**推荐的解决步骤：**

- 将编译单元添加到使用 `AK_IMPLEMENT_PLUGIN_FACTORY` 宏的插件。有关如何编写相符 Wwise 声音引擎插件的更多详细信息，请参阅 Wwise SDK 文档中的[声音引擎插件概述](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_plugins.html)章节。

---