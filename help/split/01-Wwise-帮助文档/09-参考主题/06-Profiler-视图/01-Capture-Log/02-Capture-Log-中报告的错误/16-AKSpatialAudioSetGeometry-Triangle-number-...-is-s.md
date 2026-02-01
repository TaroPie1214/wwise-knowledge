# AK::SpatialAudio::SetGeometry - Triangle number ... is skipped because it is invalid; two or more of its vertices are at the same position.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SpatialAudio::SetGeometry - Triangle number ... is skipped because it is invalid; two or more of its vertices are at the same position.

#### AK::SpatialAudio::SetGeometry - Triangle number ... is skipped because it is invalid; two or more of its vertices are at the same position.

“AK::SpatialAudio::SetGeometry - 忽略了三角形数量…，因为它是无效的；其有两个或多个顶点处于同一位置。”没有正确定义提供给 [`AK::SpatialAudio::SetGeometry`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a0cada36fab682ebb3005a79dd05a5640.html) 的三角形。

**可能的原因：**

- 该问题的原因是，在同一三角形中使用了具有相同坐标的顶点，因而只定义了一条线或一个点。

**推荐的解决步骤：**

- 分析游戏执行的 API 调用：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。重新测试场景，并检查函数在此错误之前收到的参数。

  错误消息中的数字表示三角形数组中的三角形索引以及顶点数组中对应的顶点索引。

---