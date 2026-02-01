# Event ID not found.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Event ID not found.

#### Event ID not found.

“未找到事件 ID。”调用了 `PostEvent`，但声音引擎无法找到指定 Event。相关 Event 会显示在同一行。

**可能的原因：**

- 未加载或未正确加载 SoundBank（音频包）。
- SoundBank 没有更新。
- Event 名称拼写有误。
- Event ID 拼写有误。

**推荐的解决步骤：**

- 请确保游戏代码中的名称或 ID 拼写正确。
- 检查并修复此错误之前出现的 SoundBank 加载错误。
- 检查 Advanced Profiler（高级性能分析器）中的 SoundBanks（音频包）选项卡，确保 Event 包含在 SoundBank 中且该 SoundBank 已加载。
- 确保 SoundBank 已经更新。
- 确保已在游戏构建过程中正确打包 SoundBank。
- 确保在目标平台/移动端上正确部署 SoundBank。

---