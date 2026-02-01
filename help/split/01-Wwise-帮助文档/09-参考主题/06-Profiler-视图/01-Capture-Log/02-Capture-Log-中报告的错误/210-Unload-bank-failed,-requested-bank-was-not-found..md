# Unload bank failed, requested bank was not found.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Unload bank failed, requested bank was not found.

#### Unload bank failed, requested bank was not found.

“音频包卸载失败，未找到所需音频包。”[`AK::SoundEngine::UnloadBank`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a14f24a29c85709544f68d13cbfe8ab69.html) 调用无法将作为参数传递的 SoundBank ID（音频包 ID）解析为现有音频包。已忽略调用。

**可能的原因：**

- 已经卸载 SoundBank
- SoundBank 的名称/ID 拼写有误。

---