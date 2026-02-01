# Audio Device could not honor the channel config requested with AkOutputSettings; default config will be used.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Audio Device could not honor the channel config requested with AkOutputSettings; default config will be used.

#### Audio Device could not honor the channel config requested with AkOutputSettings; default config will be used.

“音频设备无法遵守 AkOutputSettings 所请求的声道配置；将使用默认配置。”`AkOutputSettings` 包含有效的声道配置，但其与输出设备不兼容。

在这种情况下，Audio Device（音频设备）会忽略请求，并根据硬件性能选择最适宜的声道配置。

**可能的原因：**

- 请求将多声道配置用于单声道或立体声设备。
- 请求将 Ambisonics 配置用于非 3D 音频管线。

**推荐的解决步骤：**

- 将 `AkOutputSettings` 的声道配置改为输出设备支持的配置。
- 将 `AkOutputSettings` 的声道配置重置为默认配置，以便 Audio Device 根据硬件性能选择对管线来说最适宜的声道配置。

**另请参阅：**

- [“System Audio Device 的作用”一节](../../../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/02-System-Audio-Device-的作用.md "System Audio Device 的作用")

---