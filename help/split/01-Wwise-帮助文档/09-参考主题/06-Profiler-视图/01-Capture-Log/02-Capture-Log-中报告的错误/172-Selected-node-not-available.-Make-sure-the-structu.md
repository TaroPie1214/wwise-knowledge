# Selected node not available. Make sure the structure associated to the event is loaded or that the event has been prepared.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Selected node not available. Make sure the structure associated to the event is loaded or that the event has been prepared.

#### Selected node not available. Make sure the structure associated to the event is loaded or that the event has been prepared.

“所选节点不可用。确保加载与事件关联的结构或已经预备好事件。 ”选择了但没有加载要播放的声音。该声音的 ID 已在同一行进行报告。

**可能的原因：**

- Event（事件）指向未加载的声音。
- Random Container（随机容器）尝试启用未加载的子声音。
- Switch Container（切换容器）尝试启用未加载的子声音。
- 音乐播放列表尝试启用未加载的子声音。
- 动态对话事件尝试启用未加载的子声音。
- 音频包没有更新，导致所选声音 ID 无效。

**推荐的解决步骤：**

- 查看 Capture Log 并选择该错误。根据相关通知（用互连圆点标记）来寻找导致此错误的 Event。
- 确保将声音添加到 SoundBank（音频包）中并加载该 SoundBank。
- 确保 SoundBank 已经更新。
- 确保在测试主机上正确部署 SoundBank（音频包）。

---