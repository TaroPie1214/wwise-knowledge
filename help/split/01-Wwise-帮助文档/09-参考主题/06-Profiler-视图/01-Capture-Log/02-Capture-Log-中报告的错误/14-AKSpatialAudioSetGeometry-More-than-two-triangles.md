# AK::SpatialAudio::SetGeometry - More than two triangles are connected to the same edge.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SpatialAudio::SetGeometry - More than two triangles are connected to the same edge.

#### AK::SpatialAudio::SetGeometry - More than two triangles are connected to the same edge.

“AK::SpatialAudio::SetGeometry - 两个以上三角形连到了同一边缘。”[`AK::SpatialAudio::SetGeometry`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a0cada36fab682ebb3005a79dd05a5640.html) 中提供的某个三角形的构造不正确。API 要求只能有两个三角形共用同一边缘。

**推荐的解决步骤：**

- 分析游戏执行的 API 调用：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。重新测试场景，并检查函数在此错误之前收到的参数。

  错误字符串会指示三角形数组内错误共享同一边缘的三个三角形的索引，以及构成所述边缘的顶点数组中的索引。

---