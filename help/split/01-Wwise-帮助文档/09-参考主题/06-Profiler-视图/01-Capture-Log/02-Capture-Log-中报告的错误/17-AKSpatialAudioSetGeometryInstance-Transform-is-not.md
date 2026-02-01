# AK::SpatialAudio::SetGeometryInstance - Transform is not valid.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SpatialAudio::SetGeometryInstance - Transform is not valid.

#### AK::SpatialAudio::SetGeometryInstance - Transform is not valid.

“AK::SpatialAudio::SetGeometryInstance - 变换无效。”没有正确定义提供给 [`AK::SpatialAudio::SetGeometryInstance`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_ac2d5e660de0cc2a323d50f44a2731fa9.html) 的变换。

**可能的原因：**

- 该问题的原因是，输入位置不是有效的矢量或朝向矢量没有归一化或不互相垂直。

---