# Failed to connect System Audio Object to Apple Spatial Audio. Some sounds will not be audible.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Failed to connect System Audio Object to Apple Spatial Audio. Some sounds will not be audible.

#### Failed to connect System Audio Object to Apple Spatial Audio. Some sounds will not be audible.

“无法将系统音频对象连接到 Apple Spatial Audio。有些声音会听不到。”Audio Device（音频设备）接收了用于新的 System Audio Object（系统音频对象）的输入，但无法将其作为 Apple Spatial Audio 点声源连接到音频输出信号网络。Audio Device 会在播放的时候一直尝试连接对象，所以声音的开头部分可能是无声的，也可能完全听不到。

只有在 macOS、iOS 或 tvOS 上使用通过 Apple Spatial Audio 实现的 3D Audio 管线时才会出现这种情况。

**可能的原因：**

- Apple Spatial Audio 要处理的点声源过多。

**推荐的解决步骤：**

- 减少 AkPlatformInitSettings::uNumSpatialAudioPointSources 中分配的 Spatial Audio 点声源数。

**另请参阅：**

- [“了解基于对象的音频”一节](../../../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/00-了解基于对象的音频.md "了解基于对象的音频")
- [“System Audio Device 的作用”一节](../../../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/02-System-Audio-Device-的作用.md "System Audio Device 的作用")

---