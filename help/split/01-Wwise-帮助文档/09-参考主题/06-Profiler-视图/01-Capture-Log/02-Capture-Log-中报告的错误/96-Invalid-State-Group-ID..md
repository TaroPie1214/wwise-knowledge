# Invalid State Group ID.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Invalid State Group ID.

#### Invalid State Group ID.

“状态组 ID 无效。”[`AK::SoundEngine::SetState`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a68dc9be195962c671b82fbb354b68cc5.html) 未找到要使用的 State Group（状态组）的名称或数字 ID。

**可能的原因：**

- 尚未加载或无法正确加载 Init SoundBank（初始化音频包）。
- Init SoundBank 没有更新，未包含最新更改。
- 代码中的 State Group 名称或 ID 拼写有误。

**推荐的解决步骤：**

- 查看 Wwise Profiler（性能分析器）的 SoundBanks（音频包）选项卡，并确认已加载 Init SoundBank。
- 重新生成 SoundBank，并重新部署至目标平台。
- 检查 State Group 的名称。

---