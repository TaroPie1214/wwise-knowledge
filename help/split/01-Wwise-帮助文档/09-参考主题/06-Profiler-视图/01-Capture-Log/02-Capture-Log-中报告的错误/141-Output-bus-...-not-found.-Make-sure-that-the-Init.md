# Output bus ... not found. Make sure that the Init bank is loaded first.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Output bus ... not found. Make sure that the Init bank is loaded first.

#### Output bus ... not found. Make sure that the Init bank is loaded first.

“未找到输出总线…。确保先加载 Init 音频包。”没有在当前加载的结构中找到指定的输出总线。错误消息的结尾会报告当前加载的引用该总线的对象。

**可能的原因：**

- 尚未加载 Init SoundBank，或者加载时出现错误。
- 没有在对工程中的总线结构做出更改后重新生成 Init SoundBank。

**推荐的解决步骤：**

- 重新生成 SoundBank。
- 确保通过成功调用 [`AK::SoundEngine::LoadBank`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a496b9917fe035f301bcff0accd61f80f.html) 来加载 Init.bnk。

---