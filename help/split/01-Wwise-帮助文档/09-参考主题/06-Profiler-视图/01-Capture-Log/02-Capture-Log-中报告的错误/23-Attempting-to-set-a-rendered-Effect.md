# Attempting to set a rendered Effect

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Attempting to set a rendered Effect

#### Attempting to set a rendered Effect

This error occurs when setting an Effect on an object in the Containers hierarchy in a slot and either:

- 效果器插槽已经包含经过渲染的效果器。
- 具有更高索引的效果器插槽包含经过渲染的效果器。

An Effect slot can be set using either the SDK function [`AK::SoundEngine::SetContainerEffect`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a00256bfd86c2bed14c626922fc4417b0.html) or using an Event Set Effect Action.

---