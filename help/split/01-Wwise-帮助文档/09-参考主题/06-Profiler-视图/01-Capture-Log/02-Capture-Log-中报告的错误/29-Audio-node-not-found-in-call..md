# Audio node not found in call.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Audio node not found in call.

#### Audio node not found in call.

“未在调用中找到音频节点。”没有在当前加载的 SoundBank 中找到指定函数的参数引用的音频节点。

**可能的原因：**

- 尚未加载或在调用前已卸载包含此音频节点的 SoundBank。
- 工程中没有任何 SoundBank 包含该音频节点。
- 函数参数中传递的 ID 拼写有误。
- 在将音频节点添加到工程中之后没有重新生成或重新部署 SoundBank。

**推荐的解决步骤：**

- 连接 Wwise Profiler（性能分析器）并检查是否在发生此错误之前加载了包含该对象的 SoundBank（音频包）。
- 打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。连接 Wwise Profiler（性能分析器）并检查是否将参数传给了触发此错误的函数。或者，也可针对指定函数调用在游戏代码中放置断点。
- 在测试主机上重新生成并重新部署 SoundBank（音频包）。

---