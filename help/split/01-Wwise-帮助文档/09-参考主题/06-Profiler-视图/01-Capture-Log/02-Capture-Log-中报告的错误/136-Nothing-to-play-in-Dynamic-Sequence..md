# Nothing to play in Dynamic Sequence.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Nothing to play in Dynamic Sequence.

#### Nothing to play in Dynamic Sequence.

“动态序列中无可播放内容”。在使用  [`AK::SoundEngine::DynamicSequence`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence.html) 时，若队列中插入了无效声音 ID，则将出现此错误。在此之前，通常会显示 ResolveDialogueEvent 通知及其他信息。

**可能的原因：**

- [`AK::SoundEngine::DynamicDialogue::ResolveDialogueEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a18385d0523eb14ff57bd4ea9f18c08f6.html)  未能解析实际声音的参数路径。
- 音频包可能没有更新。

**推荐的解决步骤：**

- 更改  [`AK::SoundEngine::DynamicDialogue::ResolveDialogueEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a18385d0523eb14ff57bd4ea9f18c08f6.html) 调用中的 Dialogue Event（对白事件）路径和参数，使其指向有效的声音。
- 重新生成并部署 SoundBank（音频包）。

**另请参阅：**

- [`AK::SoundEngine::DynamicSequence`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence.html)
- [`AK::SoundEngine::DynamicDialogue::ResolveDialogueEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a18385d0523eb14ff57bd4ea9f18c08f6.html)

---