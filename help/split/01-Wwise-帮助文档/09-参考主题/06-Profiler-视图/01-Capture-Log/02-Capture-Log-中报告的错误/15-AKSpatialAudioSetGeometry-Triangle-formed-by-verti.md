# AK::SpatialAudio::SetGeometry - Triangle formed by vertices [v0, v1, v2] is too large.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SpatialAudio::SetGeometry - Triangle formed by vertices [v0, v1, v2] is too large.

#### AK::SpatialAudio::SetGeometry - Triangle formed by vertices [v0, v1, v2] is too large.

“AK::SpatialAudio::SetGeometry - 顶点 [v0, v1, v2] 构成的三角形太大。”提供给 [`AK::SpatialAudio::SetGeometry`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a0cada36fab682ebb3005a79dd05a5640.html) 的三角形太大。

**可能的原因：**

- 该问题的原因是，三角形的两个或多个顶点离得太远，导致在执行某些计算时出现浮点溢出。

**推荐的解决步骤：**

- 分析游戏执行的 API 调用：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。重新测试场景，并检查函数在此错误之前收到的参数。

  对于太大的三角形来说，错误消息中的数字表示三角形数组中的三角形索引以及顶点数组中对应的顶点索引。

---