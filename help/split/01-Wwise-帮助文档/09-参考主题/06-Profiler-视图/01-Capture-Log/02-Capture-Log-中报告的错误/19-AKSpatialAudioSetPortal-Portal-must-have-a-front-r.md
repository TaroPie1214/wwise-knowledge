# AK::SpatialAudio::SetPortal: Portal must have a front room which is distinct from its back room.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SpatialAudio::SetPortal: Portal must have a front room which is distinct from its back room.

#### AK::SpatialAudio::SetPortal: Portal must have a front room which is distinct from its back room.

“AK::SpatialAudio::SetPortal: 门户必须设有前方房间和后方房间”。Portal（门户）必须连接两个不同的 Room（房间）。通过 `AkPortalParams::FrontRoom` 和 `AkPortalParams::BackRoom` 传给  [`AK::SpatialAudio::SetPortal`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aeffa58bec3569a1bac5feac3e0c370d9.html) 的 Room ID（房间 ID）完全相同。

**推荐的解决步骤：**

- 分析游戏执行的 API 调用：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。重新测试场景，并检查函数在此错误之前收到的参数。
- 通过 `AkPortalParams::FrontRoom` 和 `AkPortalParams::BackRoom` 传递给  [`AK::SpatialAudio::SetPortal`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aeffa58bec3569a1bac5feac3e0c370d9.html)  的 Room 不得相同。

---