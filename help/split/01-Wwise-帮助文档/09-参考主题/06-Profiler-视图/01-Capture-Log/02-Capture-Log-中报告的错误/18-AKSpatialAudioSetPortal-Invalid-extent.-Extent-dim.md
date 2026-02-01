# AK::SpatialAudio::SetPortal: Invalid extent. Extent dimensions must be positive.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SpatialAudio::SetPortal: Invalid extent. Extent dimensions must be positive.

#### AK::SpatialAudio::SetPortal: Invalid extent. Extent dimensions must be positive.

“AK::SpatialAudio::SetPortal: 边界无效。边界尺寸必须为正值。”传给 [`AK::SoundEngine::SetPortal`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aeffa58bec3569a1bac5feac3e0c370d9.html) 的尺寸无效。

**可能的原因：**

- 将负的 Portal 边界值传给了函数。

**推荐的解决步骤：**

- 检查传给函数的所有值，并确保其全部都是正值。

---