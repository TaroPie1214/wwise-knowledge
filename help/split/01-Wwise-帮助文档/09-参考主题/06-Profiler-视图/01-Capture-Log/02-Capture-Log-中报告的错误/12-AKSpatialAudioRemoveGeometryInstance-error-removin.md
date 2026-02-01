# AK::SpatialAudio::RemoveGeometryInstance: error removing a geometry instance.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SpatialAudio::RemoveGeometryInstance: error removing a geometry instance.

#### AK::SpatialAudio::RemoveGeometryInstance: error removing a geometry instance.

“AK::SpatialAudio::RemoveGeometryInstance: 移除几何构造实例时出错。”在使用 [`AK::SpatialAudio::RemoveGeometryInstance`](https://www.audiokinetic.com/en/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aca44a83a0ffcdde183bed22e0827e4ab.html) 设置几何构造时出现错误。

**可能的原因：**

- 在尝试移除几何构造实例时，若其尚未使用 [`AK::SpatialAudio::SetGeometryInstance`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_ac2d5e660de0cc2a323d50f44a2731fa9.html) 进行设置，则将出现此错误。

---