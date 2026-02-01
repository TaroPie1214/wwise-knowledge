# No default Switch value selected in group ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > No default Switch value selected in group ...

#### No default Switch value selected in group ...

“未在分组…中选择默认的切换开关值。”有个 Switch Container 被设为了在未设 Switch 的 Game Object 上播放。为此，其尝试了改为使用默认的 Switch，但 Wwise 工程中没有选择任何默认的 Switch 值。注意，如果 Game Object 上设有 Switch 值，可以选择不指派默认的 Switch 值。

**可能的原因：**

- 没有在 Switch Container 上设置默认的 Switch 值。
- 没有在发送 Event 前在 Game Object 上设置 Switch 值。
- 在 Switch Container 中选择了默认值，但没有更新 SoundBank。
- 内存不足，无法完全创建 Switch Container。

**推荐的解决步骤：**

- 确保在 Switch Container（切换开关容器）中设置默认的 Switch 值。
- 确保在播放此 Switch Container（切换开关容器）的 Game Object（游戏对象）上设置 Switch 值。
- 重新生成并重新部署音乐 SoundBank。
- 确认 Capture Log（捕获日志）中是否显示了 "Memory allocation failed" 错误。若是，请查看如何修复相应错误：[“Memory allocation failed.”一节](115-Memory-allocation-failed..md "Memory allocation failed.")

---