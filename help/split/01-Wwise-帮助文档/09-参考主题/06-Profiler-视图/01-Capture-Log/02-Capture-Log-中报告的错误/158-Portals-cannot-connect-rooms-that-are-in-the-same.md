# Portals cannot connect rooms that are in the same Reverb Zone hierarchy.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Portals cannot connect rooms that are in the same Reverb Zone hierarchy.

#### Portals cannot connect rooms that are in the same Reverb Zone hierarchy.

“门户无法连通相同混响区域层级结构下的房间。”Portal（门户）必须连通属于独立 Room（房间）层级结构的 Room。通过  [`AK::SpatialAudio::SetReverbZone`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_af57f04a0250faecc0246cf0552c03ca6.html) 创建 Room 层级结构，由此创建 Room 之间的父子关系。

**推荐的解决步骤：**

- 分析游戏执行的 API 调用：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。重新测试场景，并检查函数在出现此错误之前收到的参数。
- 确保通过 `AkPortalParams::FrontRoom` 和 `AkPortalParams::BackRoom` 指定并传给  [`AK::SpatialAudio::SetPortal`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aeffa58bec3569a1bac5feac3e0c370d9.html) 的 Room 具有不同的父对象且不在由 Reverb Zone（混响区域）创建的相同 Room 层级结构下。
- [`AK::SpatialAudio::SetReverbZone`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_af57f04a0250faecc0246cf0552c03ca6.html) 不得在已通过 Portal 连通的 Room 之间创建父子或同级关系。

---