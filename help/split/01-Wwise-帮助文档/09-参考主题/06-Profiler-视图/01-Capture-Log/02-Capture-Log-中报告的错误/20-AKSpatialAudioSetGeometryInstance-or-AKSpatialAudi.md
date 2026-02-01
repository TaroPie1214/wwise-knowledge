# AK::SpatialAudio::SetGeometryInstance or AK::SpatialAudio::SetRoom: Geometry instances which are not watertight cannot be used for the definition of a room.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SpatialAudio::SetGeometryInstance or AK::SpatialAudio::SetRoom: Geometry instances which are not watertight cannot be used for the definition of a room.

#### AK::SpatialAudio::SetGeometryInstance or AK::SpatialAudio::SetRoom: Geometry instances which are not watertight cannot be used for the definition of a room.

“AK::SpatialAudio::SetGeometryInstance 或 AK::SpatialAudio::SetRoom: 无法将不严密的几何构造实例用于房间定义。”Room（房间）定义所用的几何构造实例必须是严密的。

**推荐的解决步骤：**

- 在将几何构造用于 Room 定义前确保其是严密的（不含任何开口）。

---