# Could not initialize 3D audio.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Could not initialize 3D audio.

#### Could not initialize 3D audio.

“无法初始化 3D 音频。”Audio Device（音频设备）无法初始化 Wwise 3D Audio 管线所需的硬件资源。Audio Device 不会激活 3D 音频功能（如 Passthrough Mix 和 System Audio Objects）。

**可能的原因：**

- 配置用于 Audio Device 的硬件设备不支持双耳合成。
- 操作系统错误导致无法初始化双耳合成系统。

**推荐的解决步骤：**

- 通过 `AkOutputSettings::idDevice` 将 Audio Device 配置为使用不同的硬件设备。
- 若希望当前硬件设备支持双耳合成，请联系 Audiokinetic 技术支持部门。

**另请参阅：**

- [“了解基于对象的音频”一节](../../../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/00-了解基于对象的音频.md "了解基于对象的音频")
- [“System Audio Device 的作用”一节](../../../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/02-System-Audio-Device-的作用.md "System Audio Device 的作用")

---