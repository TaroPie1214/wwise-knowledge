# Non-empty array of listeners specified for AddOutput() but uNumListeners is set to zero.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Non-empty array of listeners specified for AddOutput() but uNumListeners is set to zero.

#### Non-empty array of listeners specified for AddOutput() but uNumListeners is set to zero.

“为 AddOutput() 指定了一组听者(数量不为零)，但却将 uNumListeners 设为了零。”函数 AK::SoundEngine::AddOutput() 的参数 in\_pListenerIDs 和 uNumListeners 负责用来指定一组听者。两者必须一致。

**推荐的解决步骤：**

- 确保将 uNumListeners 设为合适的值。
- 或者将 in\_pListenerIDs 设为 null。

---