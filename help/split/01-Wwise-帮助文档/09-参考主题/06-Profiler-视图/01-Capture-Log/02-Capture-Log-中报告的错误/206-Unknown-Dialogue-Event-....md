# Unknown Dialogue Event: ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Unknown Dialogue Event: ...

#### Unknown Dialogue Event: ...

“未知对白事件: …。”[`AK::SoundEngine::DynamicDialogue::ResolveDialogueEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a18385d0523eb14ff57bd4ea9f18c08f6.html) 调用无法找到给定 Dialogue Event。

**可能的原因：**

- Event 名称拼写有误。
- 在更改 Project（工程）中的 Dialogue Event（对白事件）后，未重新生成并重新部署包含该 Dialogue Event 的 SoundBank（音频包）。

---