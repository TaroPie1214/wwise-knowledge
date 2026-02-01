# AK::SpatialAudio::RemoveGeometry: error removing geometry set.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SpatialAudio::RemoveGeometry: error removing geometry set.

#### AK::SpatialAudio::RemoveGeometry: error removing geometry set.

“AK::SpatialAudio::RemoveGeometry: 移除几何构造集时出错。”在使用 [`AK::SpatialAudio::RemoveGeometry`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_ae450803c582e5e6e2f8906cfdd384a25.html) 移除几何构造时出现错误。

**可能的原因：**

- 在尝试移除几何构造时，若其尚未使用 [`AK::SpatialAudio::SetGeometry`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a0cada36fab682ebb3005a79dd05a5640.html) 进行设置，则将出现此错误。
- 作为参数给定的标识符跟设置几何构造时所用的标识符不一致。
- 可用内存不足，无法完成操作。

---