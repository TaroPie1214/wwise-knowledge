# Portal ... not found in function ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Portal ... not found in function ...

#### Portal ... not found in function ...

“未在函数…中找到门户…。”之前未使用 [`AK::SpatialAudio::SetPortal`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aeffa58bec3569a1bac5feac3e0c370d9.html) 将传递给 [`AK::SpatialAudio::SetPortalObstructionAndOcclusion`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aaf04c21b13be01b9f66cd77618423110.html) 或 [`AK::SpatialAudio::SetGameObjectToPortalObstruction`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a97160dbbde1cd5d6dd6a78332e4739a7.html) 的 Portal ID（门户 ID）注册到 Spatial Audio。

**推荐的解决步骤：**

- 分析游戏执行的 API 调用：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。重新测试场景，并检查函数在此错误之前收到的参数。
- 根据错误字符串中所写 ID，使用 [`AK::SpatialAudio::SetPortal`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aeffa58bec3569a1bac5feac3e0c370d9.html) 将 Portal 注册到 Spatial Audio。

---