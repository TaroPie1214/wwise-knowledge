# Source plug-in not found in currently loaded banks.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Source plug-in not found in currently loaded banks.

#### Source plug-in not found in currently loaded banks.

“未在当前所加载音频包中找到源插件”。若声音使用了源插件，但其属性未包含在 SoundBank（音频包）中或未加载所述 SoundBank，则将出现此错误。出现此错误的唯一原因是 SoundBank Editor（音频包编辑器）的 Edit（编辑）选项卡中明确排除了部分结构。

**推荐的解决步骤：**

- 查找哪些 SoundBank 应包含该 Sound（声音）和 Source（源）插件。在 SoundBank Editor 中打开该 SoundBank，并确认其中包含了所有与该 Sound 相关的元素。

---