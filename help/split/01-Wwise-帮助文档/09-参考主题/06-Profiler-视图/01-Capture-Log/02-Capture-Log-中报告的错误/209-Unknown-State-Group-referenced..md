# Unknown State Group referenced.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Unknown State Group referenced.

#### Unknown State Group referenced.

“引用了未知的状态组。”SoundBank（音频包）中所含的一个或多个条目引用了未知的 State Group（状态组）。已知的 State Group 包含在 Init.bnk 中。此问题很可能是因为没有更新 Init.bnk 导致的。

Soundbank 加载并不会失败，但会将默认过渡时间设为 0s 并在内部创建 State Group。其他一些加载的对象以及 API 函数调用都可引用 State Group。

**推荐的解决步骤：**

- 重新生成 SoundBank（音频包）。

---